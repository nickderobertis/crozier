

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OrganisationEnrol(UniversalBaseModel):
    client_name: typing_extensions.Annotated[
        typing.Any, FieldMetadata(alias="ClientName"), pydantic.Field(alias="ClientName")
    ]
    client_uri: typing_extensions.Annotated[
        str, FieldMetadata(alias="ClientUri"), pydantic.Field(alias="ClientUri", description="A compliant URI")
    ]
    """
    A compliant URI
    """

    grant_types: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="GrantTypes"), pydantic.Field(alias="GrantTypes")
    ]
    logo_uri: typing_extensions.Annotated[
        str, FieldMetadata(alias="LogoUri"), pydantic.Field(alias="LogoUri", description="A compliant URI")
    ]
    """
    A compliant URI
    """

    policy_uri: typing_extensions.Annotated[
        str, FieldMetadata(alias="PolicyUri"), pydantic.Field(alias="PolicyUri", description="A compliant URI")
    ]
    """
    A compliant URI
    """

    redirect_uris: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="RedirectUris"), pydantic.Field(alias="RedirectUris")
    ]
    response_types: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="ResponseTypes"), pydantic.Field(alias="ResponseTypes")
    ]
    scope: typing_extensions.Annotated[str, FieldMetadata(alias="Scope"), pydantic.Field(alias="Scope")]
    token_endpoint_auth_method: typing_extensions.Annotated[
        str, FieldMetadata(alias="TokenEndpointAuthMethod"), pydantic.Field(alias="TokenEndpointAuthMethod")
    ]
    tos_uri: typing_extensions.Annotated[
        str, FieldMetadata(alias="TosUri"), pydantic.Field(alias="TosUri", description="A compliant URI")
    ]
    """
    A compliant URI
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
