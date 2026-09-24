

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthComponentsDynamo(enum.StrEnum):
    """
    DynamoDB connectivity status: 'ok', 'config_error' (AWS config could not be loaded), or 'connection_error' (table could not be described).
    """

    OK = "ok"
    CONFIG_ERROR = "config_error"
    CONNECTION_ERROR = "connection_error"

    def visit(
        self,
        ok: typing.Callable[[], T_Result],
        config_error: typing.Callable[[], T_Result],
        connection_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HealthComponentsDynamo.OK:
            return ok()
        if self is HealthComponentsDynamo.CONFIG_ERROR:
            return config_error()
        if self is HealthComponentsDynamo.CONNECTION_ERROR:
            return connection_error()
