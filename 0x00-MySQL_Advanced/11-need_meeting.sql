-- Creates a view need_meeting that lists all students
-- that have a score under 80 (strict)
-- and (has no last_meeting or has but since more than 1 month).

DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR (CURDATE() - INTERVAL 1 MONTH) > last_meeting)

