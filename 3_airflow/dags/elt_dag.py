from datetime import datetime
from airflow import DAG
from docker.types import Mount

from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator

# Replace this string with the ID generated from your Airbyte instance
CONN_ID = 'your_string_here'

CONN_ID = ''

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
}


def run_elt_script():
    script_path = "/opt/airflow/pipeline.py"
    result = subprocess.run(["python", script_path],
                            capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Script failed with error: {result.stderr}")
    else:
        print(result.stdout)


dag = DAG(
    'elt_and_dbt',
    default_args=default_args,
    description='An ELT workflow with dbt',
    start_date=datetime(2023, 10, 3),
    catchup=False,
)


# Changed for an Airbyte DAG instead
t1 = AirbyteTriggerSyncOperator(
    task_id='airbyte_postgres_postgres',
    airbyte_conn_id='airbyte',
    connection_id=CONN_ID,
    asynchronous=False,
    timeout=3600,
    wait_seconds=3,
    dag=dag
)

t2 = DockerOperator(
    task_id='dbt_run',
    image='ghcr.io/dbt-labs/dbt-postgres:1.5.8',
    command=[
        "run",
        "--profiles-dir",
        "/root",
        "--project-dir",
        "/dbt",
        "--full-refresh"
    ],
    auto_remove=True,
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    mounts=[
        Mount(source='/Users/aindamutsa/projects/personal-projects/data-engineering/crash-course/2_dbt/custom_postgres',
              target='/dbt', type='bind'),
        Mount(source='/Users/aindamutsa/.dbt', target='/root', type='bind'),
    ],
    mount_tmp_dir=False,  # Disable mounting of temporary directory
    retries=1,
    retry_delay=timedelta(seconds=15),
    environment={
        'DBT_PROFILE': 'default',
        'DBT_TARGET': 'dev',
    },
    dag=dag
)

t1 >> t2