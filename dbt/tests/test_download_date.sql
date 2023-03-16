SELECT 
    * 
FROM {{ source('public', 'downloads') }}
WHERE downloaded_at < '1999-1-1'
