

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BadGatewayErrorBodyCode(enum.StrEnum):
    CREDENTIAL_RESOLUTION_FAILED = "CREDENTIAL_RESOLUTION_FAILED"

    def visit(self, credential_resolution_failed: typing.Callable[[], T_Result]) -> T_Result:
        if self is BadGatewayErrorBodyCode.CREDENTIAL_RESOLUTION_FAILED:
            return credential_resolution_failed()
