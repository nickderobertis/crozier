

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OtoroshiUtilsMailerMailjetSettingsType(enum.StrEnum):
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
        if self is OtoroshiUtilsMailerMailjetSettingsType.ELASTIC:
            return elastic()
        if self is OtoroshiUtilsMailerMailjetSettingsType.WEBHOOK:
            return webhook()
        if self is OtoroshiUtilsMailerMailjetSettingsType.KAFKA:
            return kafka()
        if self is OtoroshiUtilsMailerMailjetSettingsType.PULSAR:
            return pulsar()
        if self is OtoroshiUtilsMailerMailjetSettingsType.FILE:
            return file()
        if self is OtoroshiUtilsMailerMailjetSettingsType.MAILER:
            return mailer()
        if self is OtoroshiUtilsMailerMailjetSettingsType.CUSTOM:
            return custom()
        if self is OtoroshiUtilsMailerMailjetSettingsType.CONSOLE:
            return console()
        if self is OtoroshiUtilsMailerMailjetSettingsType.METRICS:
            return metrics()
