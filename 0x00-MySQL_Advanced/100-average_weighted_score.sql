-- Creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
UPDATE users
SET average_score = (	
    -- SELECT weighted avg for user
    SELECT SUM(score * weight) / SUM(weight) weighted_avg
    FROM corrections c INNER JOIN projects p
    ON c.project_id = p.id
    WHERE c.user_id = user_id
    )
WHERE id = user_id;

