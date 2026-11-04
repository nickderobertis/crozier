

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .scope_with_description import ScopeWithDescription
from .service_requirement_for_user_connection_status import ServiceRequirementForUserConnectionStatus
from .service_requirement_for_user_requirement_type import ServiceRequirementForUserRequirementType


class ServiceRequirementForUser(UniversalBaseModel):
    service_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="serviceId"),
        pydantic.Field(alias="serviceId", description="Unique identifier for third-party service"),
    ]
    """
    Unique identifier for third-party service
    """

    service_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="serviceName"),
        pydantic.Field(alias="serviceName", description="Human-readable service name for display"),
    ]
    """
    Human-readable service name for display
    """

    requirement_type: typing_extensions.Annotated[
        ServiceRequirementForUserRequirementType,
        FieldMetadata(alias="requirementType"),
        pydantic.Field(
            alias="requirementType", description="Whether this service is required or optional for the agent"
        ),
    ]
    """
    Whether this service is required or optional for the agent
    """

    required_scopes: typing_extensions.Annotated[
        typing.List[ScopeWithDescription],
        FieldMetadata(alias="requiredScopes"),
        pydantic.Field(
            alias="requiredScopes",
            description="OAuth2 permissions the agent can receive for this service. For an explicit-scope\nrequirement, this is its required scope ceiling. For `require_all_scopes`, this is\nthe sorted, deduplicated union supplied by the agent's assigned Permission Sets for\nthis service only; unrelated Permission Set services are excluded.",
        ),
    ]
    """
    OAuth2 permissions the agent can receive for this service. For an explicit-scope
    requirement, this is its required scope ceiling. For `require_all_scopes`, this is
    the sorted, deduplicated union supplied by the agent's assigned Permission Sets for
    this service only; unrelated Permission Set services are excluded.
    """

    connection_status: typing_extensions.Annotated[
        ServiceRequirementForUserConnectionStatus,
        FieldMetadata(alias="connectionStatus"),
        pydantic.Field(alias="connectionStatus", description="User's current connection status with this service"),
    ]
    """
    User's current connection status with this service
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
