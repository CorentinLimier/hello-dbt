migrate:
	alembic upgrade head

init:
	dbt seed --project-dir dbt --profiles-dir dbt
	dbt compile --project-dir dbt --profiles-dir dbt

serve-catalog:
	python -m http.server 8081 --directory dbt/target
