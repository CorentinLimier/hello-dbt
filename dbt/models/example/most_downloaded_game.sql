{{ config(materialized='table') }}

select 
    id_game,
    name_game,
    nb_downloads
from {{ ref('download_counts_per_game') }} nb_downloads
ORDER BY nb_downloads DESC
LIMIT 1