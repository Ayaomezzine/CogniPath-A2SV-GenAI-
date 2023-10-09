-- Create Users_temp with the same structure as Users
CREATE TABLE Users_temp (
    id INTEGER PRIMARY KEY,
    user VARCHAR(64) UNIQUE,
    email VARCHAR(120) UNIQUE,
    password VARCHAR(500),
    progression INTEGER DEFAULT 0,
    Language INTEGER DEFAULT 0,
    Intellect INTEGER DEFAULT 0,
    Social_Skills INTEGER DEFAULT 0,
    pathology VARCHAR(50) CHECK (pathology IN ('ADHD', 'ASD', 'Dyslexia')),
    isPremium BOOLEAN DEFAULT 0
);

-- Copy data from Users to Users_temp
INSERT INTO Users_temp (id, user, email, password, progression, Language, Intellect, Social_Skills, pathology, isPremium)
SELECT id, user, email, password, IFNULL(progression, 0), IFNULL(Language, 0), IFNULL(Intellect, 0), IFNULL(Social_Skills, 0),
       CASE
           WHEN pathology = 'ADHD' THEN 'ADHD'
           WHEN pathology = 'ASD' THEN 'ASD'
           WHEN pathology = 'Dyslexia' THEN 'Dyslexia'
           ELSE 'ASD'
       END, IFNULL(isPremium, 0)
FROM Users;

-- Drop the original Users table
DROP TABLE Users;

-- Rename the temporary table to Users
ALTER TABLE Users_temp RENAME TO Users;
