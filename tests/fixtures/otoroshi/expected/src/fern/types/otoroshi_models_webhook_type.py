

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OtoroshiModelsWebhookType(enum.StrEnum):
    """
    the kind of exporter
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
        if self is OtoroshiModelsWebhookType.ELASTIC:
            return elastic()
        if self is OtoroshiModelsWebhookType.WEBHOOK:
            return webhook()
        if self is OtoroshiModelsWebhookType.KAFKA:
            return kafka()
        if self is OtoroshiModelsWebhookType.PULSAR:
            return pulsar()
        if self is OtoroshiModelsWebhookType.FILE:
            return file()
        if self is OtoroshiModelsWebhookType.MAILER:
            return mailer()
        if self is OtoroshiModelsWebhookType.CUSTOM:
            return custom()
        if self is OtoroshiModelsWebhookType.CONSOLE:
            return console()
        if self is OtoroshiModelsWebhookType.METRICS:
            return metrics()
