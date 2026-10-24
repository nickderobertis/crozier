

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CreateClientEndpointOutput(UniversalBaseModel):
    client_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="clientId"),
        pydantic.Field(alias="clientId", description="The id of the created client."),
    ]
    """
    The id of the created client.
    """

    client_secret: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="clientSecret"),
        pydantic.Field(alias="clientSecret", description="The secret of the created client."),
    ]
    """
    The secret of the created client.
    """

    organization_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="organizationId"),
        pydantic.Field(alias="organizationId", description="The id of the organization the client is authorized for."),
    ]
    """
    The id of the organization the client is authorized for.
    """

    organization_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="organizationName"),
        pydantic.Field(
            alias="organizationName", description="The name of the organization the client is authorized for."
        ),
    ]
    """
    The name of the organization the client is authorized for.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
