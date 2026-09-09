

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Error415Message(enum.StrEnum):
    THE_SERVER_DOES_NOT_SUPPORT_THE_REQUEST_PAYLOADS_MEDIA_TYPE = (
        "The server does not support the request payload's media type."
    )

    def visit(
        self, the_server_does_not_support_the_request_payloads_media_type: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is Error415Message.THE_SERVER_DOES_NOT_SUPPORT_THE_REQUEST_PAYLOADS_MEDIA_TYPE:
            return the_server_does_not_support_the_request_payloads_media_type()
