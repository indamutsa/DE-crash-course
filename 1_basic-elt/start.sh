docker compose up init airflow

sleep 5

docker compose up -d

sleep

cd airbyte


if [ -d "../docker-compose.yaml" ]; then
    docker compose up -d
else
    ./run-ab-platform.sh
fi



# ----

# cron &

# python3 /app/pipeline.py

