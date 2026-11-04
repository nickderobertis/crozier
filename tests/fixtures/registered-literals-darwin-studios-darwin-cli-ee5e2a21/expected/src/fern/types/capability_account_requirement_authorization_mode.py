

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CapabilityAccountRequirementAuthorizationMode(enum.StrEnum):
    REMOTE_MCP_ELICITATION = "REMOTE_MCP_ELICITATION"
    REMOTE_UCP_IDENTITY = "REMOTE_UCP_IDENTITY"
    DARWIN_BROKERED = "DARWIN_BROKERED"
    SELLER_HOSTED = "SELLER_HOSTED"
    UNAVAILABLE = "UNAVAILABLE"

    def visit(
        self,
        remote_mcp_elicitation: typing.Callable[[], T_Result],
        remote_ucp_identity: typing.Callable[[], T_Result],
        darwin_brokered: typing.Callable[[], T_Result],
        seller_hosted: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CapabilityAccountRequirementAuthorizationMode.REMOTE_MCP_ELICITATION:
            return remote_mcp_elicitation()
        if self is CapabilityAccountRequirementAuthorizationMode.REMOTE_UCP_IDENTITY:
            return remote_ucp_identity()
        if self is CapabilityAccountRequirementAuthorizationMode.DARWIN_BROKERED:
            return darwin_brokered()
        if self is CapabilityAccountRequirementAuthorizationMode.SELLER_HOSTED:
            return seller_hosted()
        if self is CapabilityAccountRequirementAuthorizationMode.UNAVAILABLE:
            return unavailable()
