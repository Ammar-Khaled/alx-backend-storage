-- Ranks country origins of bands
-- Ordered by the number of (non-unique) fans
-- Column names must be: origin and nb_fans

SELECT origin, SUM(fans) nb_fans
FROM metal_bands
GROUP BY 1
ORDER BY 2 DESC;

