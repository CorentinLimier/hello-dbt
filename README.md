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

# OpenLineage with marquez
- Clone [marquez](https://github.com/MarquezProject/marquez) project
```
git clone git@github.com:MarquezProject/marquez.git
```
- See [this](https://github.com/MarquezProject/marquez/issues/1956#issuecomment-1103086809) to change marquez port mapping to avoid conflict with Airflow db  
- Launch `./docker/up.sh`