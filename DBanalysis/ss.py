qry = """SELECT
    DATE_TRUNC('month', \"Year-Month-Day\") as month,
    AVG(\"Yield\") as yield,
    SUM(\"Total Pax\") as pax
FROM cirium_traffic_northamerica
WHERE
    \"Orig\" IN ('LAX', 'SFO', 'DFW', 'IAH', 'HNL')
    AND \"Dest\" IN ('SYD', 'MEL', 'BNE')
	AND \"Op Al\" = ('UA')
	AND \"Stop-1 Airport\" is null
	AND \"Total Pax\" >0
    AND \"Year-Month-Day\">= '2022-01-01'
group by
  month"""