CREATE TABLE activities (
    id INTEGER PRIMARY KEY,
    date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    title TEXT,
    input TEXT,
    output TEXT,
    user_email TEXT,
    activity TEXT,
    social_score INTEGER,
    intellect_score INTEGER,
    language_score INTEGER,
    avg_score INTEGER
);
