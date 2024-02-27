We have set up the environment and we are ready to start building our data pipeline. We will start by building a simple data pipeline using Apache Kafka and Apache Flink. We will use docker-compose to run the environment. W

- We now have the following files in our elt directory:

  - docker-compose.yml
  - Dockerfile
  - init.sql
  - pipeline.py

- We will use docker-compose to run the environment. We will use the following command to start the environment:

```bash
cd elt
docker compose up

# To take down the environment
docker compose down

# To take down the environment and remove the volumes
docker compose down -v

# To take down the environment and remove the images
docker compose down --rmi all

# To take down the environment and remove the images and volumes
docker compose down -v --rmi all

# To take down the environment and remove the images and volumes docker compose down -v --rmi all

# To take down the environment and remove the images and volumes and start the environment
docker compose down -v --rmi all && docker compose up

# To take down the environment and remove the images and volumes and start the environment in the background
docker compose down -v --rmi all && docker compose up -d

# To take down the environment and remove the images and volumes and start the environment in the background and follow the logs
docker compose down -v --rmi all && docker compose up -d && docker compose logs -f

# ---
# We can use docker to take down images, volumes, containers, and networks
# Stop all containers
docker stop $(docker ps -a -q)

# Remove all containers
docker rm $(docker ps -a -q)

# Remove all images
docker rmi $(docker images -a -q)

# Remove all volumes
docker volume rm $(docker volume ls -q)
```

Now, let us get into PostgresSQL and see what happened after we run the environment.

```bash
docker exec -it elt-destination_postgres-1 psql -U postgres
```

```sql
-- List the databases
\l

-- Connect to the destination database
\c destination_db

-- List the tables
\dt

-- Describe the table
\d+ destination_table

-- Select the data from the table
SELECT * FROM actors;
```
