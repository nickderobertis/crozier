

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Type(enum.StrEnum):
    ORACLE = "ORACLE"
    MYSQL = "MYSQL"
    MARIADB = "MARIADB"
    SQLSERVER = "SQLSERVER"
    POSTGRESQL = "POSTGRESQL"
    MONGODB = "MONGODB"
    KAFKA = "KAFKA"
    REDIS = "REDIS"
    KINESIS = "KINESIS"
    PUBSUB = "PUBSUB"
    HTTP = "HTTP"
    PULSAR = "PULSAR"
    EVENTHUBS = "EVENTHUBS"
    NATS_STREAMING = "NATS-STREAMING"
    NATS_JETSTREAM = "NATS-JETSTREAM"
    PRAVEGA = "PRAVEGA"
    INFINISPAN = "INFINISPAN"
    ROCKETMQ = "ROCKETMQ"
    RABBITMQ = "RABBITMQ"
    RABBITMQ_NATIVE_STREAM = "RABBITMQ_NATIVE_STREAM"
    MILVUS = "MILVUS"
    QDRANT = "QDRANT"
    SQS = "SQS"
    JDBC = "JDBC"

    def visit(
        self,
        oracle: typing.Callable[[], T_Result],
        mysql: typing.Callable[[], T_Result],
        mariadb: typing.Callable[[], T_Result],
        sqlserver: typing.Callable[[], T_Result],
        postgresql: typing.Callable[[], T_Result],
        mongodb: typing.Callable[[], T_Result],
        kafka: typing.Callable[[], T_Result],
        redis: typing.Callable[[], T_Result],
        kinesis: typing.Callable[[], T_Result],
        pubsub: typing.Callable[[], T_Result],
        http: typing.Callable[[], T_Result],
        pulsar: typing.Callable[[], T_Result],
        eventhubs: typing.Callable[[], T_Result],
        nats_streaming: typing.Callable[[], T_Result],
        nats_jetstream: typing.Callable[[], T_Result],
        pravega: typing.Callable[[], T_Result],
        infinispan: typing.Callable[[], T_Result],
        rocketmq: typing.Callable[[], T_Result],
        rabbitmq: typing.Callable[[], T_Result],
        rabbitmq_native_stream: typing.Callable[[], T_Result],
        milvus: typing.Callable[[], T_Result],
        qdrant: typing.Callable[[], T_Result],
        sqs: typing.Callable[[], T_Result],
        jdbc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Type.ORACLE:
            return oracle()
        if self is Type.MYSQL:
            return mysql()
        if self is Type.MARIADB:
            return mariadb()
        if self is Type.SQLSERVER:
            return sqlserver()
        if self is Type.POSTGRESQL:
            return postgresql()
        if self is Type.MONGODB:
            return mongodb()
        if self is Type.KAFKA:
            return kafka()
        if self is Type.REDIS:
            return redis()
        if self is Type.KINESIS:
            return kinesis()
        if self is Type.PUBSUB:
            return pubsub()
        if self is Type.HTTP:
            return http()
        if self is Type.PULSAR:
            return pulsar()
        if self is Type.EVENTHUBS:
            return eventhubs()
        if self is Type.NATS_STREAMING:
            return nats_streaming()
        if self is Type.NATS_JETSTREAM:
            return nats_jetstream()
        if self is Type.PRAVEGA:
            return pravega()
        if self is Type.INFINISPAN:
            return infinispan()
        if self is Type.ROCKETMQ:
            return rocketmq()
        if self is Type.RABBITMQ:
            return rabbitmq()
        if self is Type.RABBITMQ_NATIVE_STREAM:
            return rabbitmq_native_stream()
        if self is Type.MILVUS:
            return milvus()
        if self is Type.QDRANT:
            return qdrant()
        if self is Type.SQS:
            return sqs()
        if self is Type.JDBC:
            return jdbc()
