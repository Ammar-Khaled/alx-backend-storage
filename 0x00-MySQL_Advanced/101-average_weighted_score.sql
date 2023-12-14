-- Creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for all students.

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
DECLARE i INT DEFAULT 1;

WHILE i <= (SELECT COUNT(*) FROM users) DO
    UPDATE users
    SET average_score = (	
    -- SELECT weighted avg for user
    SELECT SUM(score * weight) / SUM(weight) weighted_avg
    FROM corrections c INNER JOIN projects p
    ON c.project_id = p.id
    WHERE c.user_id = i
    )
    WHERE id = i;
    SET i = i + 1;
END WHILE;
END//

