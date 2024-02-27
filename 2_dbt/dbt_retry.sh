#!/bin/bash

# Maximum number of attempts
max_attempts=3
attempt_num=1

while [ $attempt_num -le $max_attempts ]; do
    echo "Attempt $attempt_num of $max_attempts"
    dbt run --profiles-dir /root --project-dir /dbt --full-refresh
    status=$?
    if [ $status -eq 0 ]; then
        echo "DBT command succeeded."
        exit 0
    fi
    echo "DBT command failed, retrying..."
    ((attempt_num++))
    sleep 5 # wait for 5 seconds before retrying
done

echo "DBT command failed after $max_attempts attempts."
exit 1
