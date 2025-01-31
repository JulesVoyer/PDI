SELECT 
    p.prod_strength,
    CASE 
        WHEN matches[1] IS NOT NULL THEN CAST(matches[1] AS FLOAT)
        ELSE NULL
    END AS quantity,
    CASE 
        WHEN matches[2] IS NOT NULL THEN matches[2]
        ELSE NULL
    END AS unit,
    CASE 
        WHEN matches[2] IS NOT NULL THEN TRIM(BOTH ' ' FROM REGEXP_REPLACE(p.prod_strength, '^([0-9]+(\.[0-9]+)?)?[ ]?([a-zA-Z/ ]+)$', ''))
        ELSE p.prod_strength
    END AS substance
FROM 
    prescriptions p,
    LATERAL REGEXP_MATCHES(p.prod_strength, '^([0-9]+[\.[0-9]+]?)?[ ]?([a-zA-Z]+[[ ]?/[ ]?[a-zA-Z]+]?)?[ ]([a-zA-Z ]+)$') AS matches;