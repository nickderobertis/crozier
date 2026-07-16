

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DataExporterConfigTyp(str, enum.Enum):
    """
    Type of data exporter
    """

    KAFKA = "kafka"
    PULSAR = "pulsar"
    FILE = "file"
    MAILER = "mailer"
    ELASTIC = "elastic"
    CONSOLE = "console"
    CUSTOM = "custom"

    def visit(
        self,
        kafka: typing.Callable[[], T_Result],
        pulsar: typing.Callable[[], T_Result],
        file: typing.Callable[[], T_Result],
        mailer: typing.Callable[[], T_Result],
        elastic: typing.Callable[[], T_Result],
        console: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DataExporterConfigTyp.KAFKA:
            return kafka()
        if self is DataExporterConfigTyp.PULSAR:
            return pulsar()
        if self is DataExporterConfigTyp.FILE:
            return file()
        if self is DataExporterConfigTyp.MAILER:
            return mailer()
        if self is DataExporterConfigTyp.ELASTIC:
            return elastic()
        if self is DataExporterConfigTyp.CONSOLE:
            return console()
        if self is DataExporterConfigTyp.CUSTOM:
            return custom()
