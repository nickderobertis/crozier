

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OtoroshiUtilsMailerConsoleMailerSettingsType(enum.StrEnum):
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
        if self is OtoroshiUtilsMailerConsoleMailerSettingsType.ELASTIC:
            return elastic()
        if self is OtoroshiUtilsMailerConsoleMailerSettingsType.WEBHOOK:
            return webhook()
        if self is OtoroshiUtilsMailerConsoleMailerSettingsType.KAFKA:
            return kafka()
        if self is OtoroshiUtilsMailerConsoleMailerSettingsType.PULSAR:
            return pulsar()
        if self is OtoroshiUtilsMailerConsoleMailerSettingsType.FILE:
            return file()
        if self is OtoroshiUtilsMailerConsoleMailerSettingsType.MAILER:
            return mailer()
        if self is OtoroshiUtilsMailerConsoleMailerSettingsType.CUSTOM:
            return custom()
        if self is OtoroshiUtilsMailerConsoleMailerSettingsType.CONSOLE:
            return console()
        if self is OtoroshiUtilsMailerConsoleMailerSettingsType.METRICS:
            return metrics()
