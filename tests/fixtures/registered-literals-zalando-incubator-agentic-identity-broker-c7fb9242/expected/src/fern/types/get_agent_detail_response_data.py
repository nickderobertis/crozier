

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_detail import AgentDetail
from .available_service import AvailableService
from .cimd_metadata import CimdMetadata
from .permission_set_with_requirement import PermissionSetWithRequirement
from .service_requirement_for_user import ServiceRequirementForUser


class GetAgentDetailResponseData(UniversalBaseModel):
    agent: AgentDetail
    services: typing.List[ServiceRequirementForUser] = pydantic.Field()
    """
    Array of service requirements for this agent with user connection status.
    Includes mandatory and optional third-party services the agent needs,
    sorted mandatory-first. Empty array if the agent has no service requirements.
    
    '
    """

    permission_sets: typing.Optional[typing.List[PermissionSetWithRequirement]] = pydantic.Field(default=None)
    """
    Phase 4 US2: Array of permission sets assigned to this agent with requirement types.
    Empty array if no permission sets are assigned.
    """

    active_session_service_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Phase 4 US2: Array of service IDs for which the authenticated user has active sessions.
    Empty array if no active sessions.
    """

    available_services: typing.Optional[typing.List[AvailableService]] = pydantic.Field(default=None)
    """
    Phase 4 US2: Array of all available third-party services (redacted).
    Same as services field but with reduced detail.
    """

    cimd_metadata: typing.Optional[CimdMetadata] = pydantic.Field(default=None)
    """
    CIMD trust metadata present when the authorization request used a URL-format
    client_id. Null for agents with opaque (UUID) client identifiers.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
