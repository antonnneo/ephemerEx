-- liquibase formatted sql
CREATE TABLE
    messages (
        id      UUID DEFAULT gen_random_uuid() PRIMARY KEY,
        content TEXT NOT NULL,
        created BIGINT DEFAULT EXTRACT(epoch FROM CURRENT_TIMESTAMP)
    );

--rollback drop table delivery_resource_utilization;