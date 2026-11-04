

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AgentDelegation(UniversalBaseModel):
    agent_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="agentId"), pydantic.Field(alias="agentId", description="Unique agent identifier")
    ]
    """
    Unique agent identifier
    """

    display_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Human-readable agent name"),
    ]
    """
    Human-readable agent name
    """

    logo_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="logoUrl"),
        pydantic.Field(alias="logoUrl", description="Optional URL to agent's logo or icon"),
    ] = None
    """
    Optional URL to agent's logo or icon
    """

    active_grant_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="activeGrantCount"),
        pydantic.Field(
            alias="activeGrantCount",
            description="Number of permission sets currently granted to this agent.\nReflects the count of granted_permission_sets in the active grant.",
        ),
    ]
    """
    Number of permission sets currently granted to this agent.
    Reflects the count of granted_permission_sets in the active grant.
    """

    last_modified_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="lastModifiedAt"),
        pydantic.Field(
            alias="lastModifiedAt",
            description="ISO 8601 timestamp when the delegation was last modified.\nCorresponds to the grant's updated_at timestamp.",
        ),
    ]
    """
    ISO 8601 timestamp when the delegation was last modified.
    Corresponds to the grant's updated_at timestamp.
    """

    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(
            alias="expiresAt",
            description="Optional grant expiration timestamp (ISO 8601).\nNull value indicates indefinite grant (no expiration).",
        ),
    ] = None
    """
    Optional grant expiration timestamp (ISO 8601).
    Null value indicates indefinite grant (no expiration).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
