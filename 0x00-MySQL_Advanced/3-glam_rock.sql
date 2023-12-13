-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
-- Requirements:
-- Column names must be: band_name and lifespan (in years)
-- Use attributes formed and split for computing the lifespan
-- Hint: SELECT band_name, (IFNULL(split, YEAR(CURRENT_DATE())) - formed) AS lifespan

SELECT band_name, 
	CASE
		WHEN split IS NULL THEN 2022 - formed 
		ELSE split - formed
	END
	AS lifespan 
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY 2 DESC;

