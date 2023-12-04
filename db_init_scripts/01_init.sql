-- SQL statement to create a table named 'flats'

CREATE TABLE IF NOT EXISTS flats (
    -- 'id' column: An auto-incrementing integer used as the primary key.
    -- 'SERIAL' automatically increments the value and ensures uniqueness.
    id SERIAL PRIMARY KEY,

    -- 'title' column: A variable character string with a maximum length of 255 characters.
    -- It is used to store the title of the flat.
    title VARCHAR(255),

    -- 'image_url' column: A text column used to store the URL of the flat's image.
    -- The 'TEXT' data type is used for longer strings that may exceed 255 characters.
    image_url TEXT
);
