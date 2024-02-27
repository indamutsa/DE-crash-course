# Use the official Airflow image as the base
FROM apache/airflow:2.8.2

# Install the Docker provider for Airflow
RUN pip install apache-airflow-providers-docker \
    && pip install apache-airflow-providers-http \
    && pip install apache-airflow-providers-airbyte