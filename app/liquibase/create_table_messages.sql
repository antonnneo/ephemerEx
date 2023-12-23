-- liquibase formatted sql
CREATE TABLE
    messages (
        id VARCHAR(255) NOT NULL PRIMARY KEY,
        content TEXT NOT NULL,
        read_counter BOOLEAN NOT NULL,
        read_limit BOOLEAN NOT NULL,
        created BIGINT NOT NULL
    );

--rollback drop table delivery_resource_utilization;