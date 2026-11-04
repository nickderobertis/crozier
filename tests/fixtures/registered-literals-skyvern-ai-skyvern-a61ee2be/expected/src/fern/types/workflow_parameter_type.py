

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowParameterType(enum.StrEnum):
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    JSON = "json"
    FILE_URL = "file_url"
    CREDENTIAL_ID = "credential_id"

    def visit(
        self,
        string: typing.Callable[[], T_Result],
        integer: typing.Callable[[], T_Result],
        float_: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        json: typing.Callable[[], T_Result],
        file_url: typing.Callable[[], T_Result],
        credential_id: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WorkflowParameterType.STRING:
            return string()
        if self is WorkflowParameterType.INTEGER:
            return integer()
        if self is WorkflowParameterType.FLOAT:
            return float_()
        if self is WorkflowParameterType.BOOLEAN:
            return boolean()
        if self is WorkflowParameterType.JSON:
            return json()
        if self is WorkflowParameterType.FILE_URL:
            return file_url()
        if self is WorkflowParameterType.CREDENTIAL_ID:
            return credential_id()
