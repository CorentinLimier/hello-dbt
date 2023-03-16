{{ config(materialized='table') }}

select 
    games.id as id_game,
    games.name as name_game,
    count(downloads.id) as nb_downloads
from {{ source('public', 'games') }} games
left join {{ source('public', 'downloads') }} downloads
on games.id = downloads.id_game
group by games.id, games.name
