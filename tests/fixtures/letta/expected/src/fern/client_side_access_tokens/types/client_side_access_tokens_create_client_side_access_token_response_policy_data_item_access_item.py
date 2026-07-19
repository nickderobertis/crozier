

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItemAccessItem(enum.StrEnum):
    READ_MESSAGES = "read_messages"
    WRITE_MESSAGES = "write_messages"
    READ_AGENT = "read_agent"
    WRITE_AGENT = "write_agent"

    def visit(
        self,
        read_messages: typing.Callable[[], T_Result],
        write_messages: typing.Callable[[], T_Result],
        read_agent: typing.Callable[[], T_Result],
        write_agent: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItemAccessItem.READ_MESSAGES:
            return read_messages()
        if self is ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItemAccessItem.WRITE_MESSAGES:
            return write_messages()
        if self is ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItemAccessItem.READ_AGENT:
            return read_agent()
        if self is ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItemAccessItem.WRITE_AGENT:
            return write_agent()
