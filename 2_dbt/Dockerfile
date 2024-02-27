# Assuming you're extending from the DBT image or creating a new one
FROM ghcr.io/dbt-labs/dbt-postgres:1.5.8

# Copy the retry script into the container
COPY dbt_retry.sh /dbt_retry.sh

# Make the script executable
RUN chmod +x /dbt_retry.sh
