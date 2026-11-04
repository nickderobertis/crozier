

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .listed_auth_provider_auth_type import ListedAuthProviderAuthType


class ListedAuthProvider(UniversalBaseModel):
    """
    A listed value object for {@link run.halo.app.core.extension.AuthProvider run.halo.app.core.extension.AuthProvider}.
    """

    auth_type: typing_extensions.Annotated[
        typing.Optional[ListedAuthProviderAuthType], FieldMetadata(alias="authType"), pydantic.Field(alias="authType")
    ] = None
    authentication_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="authenticationUrl"), pydantic.Field(alias="authenticationUrl")
    ] = None
    binding_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bindingUrl"), pydantic.Field(alias="bindingUrl")
    ] = None
    description: typing.Optional[str] = None
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    enabled: typing.Optional[bool] = None
    help_page: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="helpPage"), pydantic.Field(alias="helpPage")
    ] = None
    is_bound: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isBound"), pydantic.Field(alias="isBound")
    ] = None
    logo: typing.Optional[str] = None
    name: str
    priority: typing.Optional[int] = None
    privileged: typing.Optional[bool] = None
    supports_binding: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="supportsBinding"), pydantic.Field(alias="supportsBinding")
    ] = None
    unbinding_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="unbindingUrl"), pydantic.Field(alias="unbindingUrl")
    ] = None
    website: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
