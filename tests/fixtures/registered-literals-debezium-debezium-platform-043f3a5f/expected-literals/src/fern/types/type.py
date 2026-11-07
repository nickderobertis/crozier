

import typing

Type = typing.Union[
    typing.Literal[
        "ORACLE",
        "MYSQL",
        "MARIADB",
        "SQLSERVER",
        "POSTGRESQL",
        "MONGODB",
        "KAFKA",
        "REDIS",
        "KINESIS",
        "PUBSUB",
        "HTTP",
        "PULSAR",
        "EVENTHUBS",
        "NATS-STREAMING",
        "NATS-JETSTREAM",
        "PRAVEGA",
        "INFINISPAN",
        "ROCKETMQ",
        "RABBITMQ",
        "RABBITMQ_NATIVE_STREAM",
        "MILVUS",
        "QDRANT",
        "SQS",
        "JDBC",
    ],
    typing.Any,
]
