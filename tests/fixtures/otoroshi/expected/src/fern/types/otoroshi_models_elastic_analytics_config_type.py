

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OtoroshiModelsElasticAnalyticsConfigType(enum.StrEnum):
    """
    Object type
    """

    ELASTIC = "elastic"
    WEBHOOK = "webhook"
    KAFKA = "kafka"
    PULSAR = "pulsar"
    FILE = "file"
    MAILER = "mailer"
    CUSTOM = "custom"
    CONSOLE = "console"
    METRICS = "metrics"

    def visit(
        self,
        elastic: typing.Callable[[], T_Result],
        webhook: typing.Callable[[], T_Result],
        kafka: typing.Callable[[], T_Result],
        pulsar: typing.Callable[[], T_Result],
        file: typing.Callable[[], T_Result],
        mailer: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
        console: typing.Callable[[], T_Result],
        metrics: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OtoroshiModelsElasticAnalyticsConfigType.ELASTIC:
            return elastic()
        if self is OtoroshiModelsElasticAnalyticsConfigType.WEBHOOK:
            return webhook()
        if self is OtoroshiModelsElasticAnalyticsConfigType.KAFKA:
            return kafka()
        if self is OtoroshiModelsElasticAnalyticsConfigType.PULSAR:
            return pulsar()
        if self is OtoroshiModelsElasticAnalyticsConfigType.FILE:
            return file()
        if self is OtoroshiModelsElasticAnalyticsConfigType.MAILER:
            return mailer()
        if self is OtoroshiModelsElasticAnalyticsConfigType.CUSTOM:
            return custom()
        if self is OtoroshiModelsElasticAnalyticsConfigType.CONSOLE:
            return console()
        if self is OtoroshiModelsElasticAnalyticsConfigType.METRICS:
            return metrics()
