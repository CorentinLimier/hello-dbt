{% snapshot games_snapshot %}

{{
    config(
      target_database='postgres',
      target_schema='public',
      unique_key='id',
      strategy='check',
      check_cols=['name'],
    )
}}

select * from {{ source('public', 'games') }}

{% endsnapshot %}