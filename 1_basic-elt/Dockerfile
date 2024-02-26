FROM python:3.8-slim

# Add the PostgreSQL repository to ensure we get the latest version
# Install the repository's signing key
RUN apt-get update && apt-get install -y gnupg2 lsb-release && \
    sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list' && \
    apt-get install -y wget && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

# Update the package lists for the PostgreSQL repository
RUN apt-get update

# Install the specific version of PostgreSQL client
RUN apt-get install -y postgresql-client-16

# Copy the ELT pipeline script 
COPY pipeline.py .

# Set the default command to run the ELT pipeline script
CMD ["python", "pipeline.py"]

