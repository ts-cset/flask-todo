-- Mock data for tests

INSERT INTO todos (description, completed, created_at)
VALUES ('clean room', FALSE, NOW()),
       ('do homework', TRUE, NOW()),
       ('get groceries', FALSE, NOW());

