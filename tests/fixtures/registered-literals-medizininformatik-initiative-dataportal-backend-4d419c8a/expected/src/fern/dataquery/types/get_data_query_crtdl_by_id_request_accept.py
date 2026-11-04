

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetDataQueryCrtdlByIdRequestAccept(enum.StrEnum):
    APPLICATION_JSON = "application/json"
    APPLICATION_ZIP = "application/zip"

    def visit(
        self, application_json: typing.Callable[[], T_Result], application_zip: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is GetDataQueryCrtdlByIdRequestAccept.APPLICATION_JSON:
            return application_json()
        if self is GetDataQueryCrtdlByIdRequestAccept.APPLICATION_ZIP:
            return application_zip()
