# Launch Airflow and database

```
docker-compose build 
docker-compose up
docker-compose down
```

# Init project

Note : Alembic is configured but you can use `dbt seed` instead

```
make init
```


# Launch dbt commands
```
cd dbt
export DBT_PROFILES_DIR=$(pwd)
dbt run 
dbt test
dbt docs generate
```

# Launch documentation server
```
make serve-catalog
```

# Materialized options for dbt
- ephemeral 
- incremental / table / view