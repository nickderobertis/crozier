

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class QueryClientsEndpointOutput(UniversalBaseModel):
    client_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="clientId"),
        pydantic.Field(alias="clientId", description="The id of the client."),
    ] = None
    """
    The id of the client.
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="The optional display name of the client."),
    ] = None
    """
    The optional display name of the client.
    """

    organization_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="organizationId"),
        pydantic.Field(alias="organizationId", description="The id of the organization the client is authorized for."),
    ] = None
    """
    The id of the organization the client is authorized for.
    """

    organization_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="organizationName"),
        pydantic.Field(
            alias="organizationName", description="The name of the organization the client is authorized for."
        ),
    ] = None
    """
    The name of the organization the client is authorized for.
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="The time at which the client was created."),
    ] = None
    """
    The time at which the client was created.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
