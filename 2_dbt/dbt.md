Let us by creating a new directory called dbt.

```bash
mkdir 2_dbt
```

Now, let us create a conda environment for dbt.

```bash
conda create -n dbt python=3.8
```

Now, let us activate the conda environment.

```bash
conda activate dbt
```

Now, let us install dbt for Postgres.

```bash
pip install dbt-postgres
```

Now, let us create a new dbt project.

```bash
dbt init
```

You need to make sure the profile is set to the correct database. You can do this by editing the profiles.yml file.

```bash
nano ~/.dbt/profiles.yml
```

```yaml
custom_postgres:
  outputs:
    dev:
      dbname: destination_db
      host: host.docker.internal
      pass: secret
      port: 5432
      schema: public
      threads: 1
      type: postgres
      user: postgres
  target: dev
```

Now, let us analyze the dbt_project.yml file.
Change the +materialized from view to table because we are using Postgres.

```yaml
# files using the `{{ config(...) }}` macro.
models:
  custom_postgres:
    # Config indicated by + and applies to all files under models/example/
    example:
      +materialized: table # Because we are using postgres, we will use tables instead of views
```

Now, You can check some custom examples they have already created.

```sh
cd models/example
ls
```

```sql

/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='table') }}

with source_data as (

    select 1 as id
    union all
    select null as id

)

select *
from source_data

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null
```

Once the models are created, even macros are integrated into the models, we can run cluster against the models.

```bash
docker compose down -v --rmi all # To make sure it can start from scratch with clean slate
docker compose up
```

Get in destination container and run the dbt commands.

```bash
docker exec -it destination_postgres psql -U postgres -d destination_db
```
