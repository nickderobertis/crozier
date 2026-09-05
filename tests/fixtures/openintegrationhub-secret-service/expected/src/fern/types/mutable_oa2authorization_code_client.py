

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .mutable_oa2authorization_code_client_endpoints import MutableOa2AuthorizationCodeClientEndpoints
from .mutable_oa2authorization_code_client_type import MutableOa2AuthorizationCodeClientType
from .owner import Owner


class MutableOa2AuthorizationCodeClient(UniversalBaseModel):
    name: str
    owners: typing.List[Owner]
    type: MutableOa2AuthorizationCodeClientType
    preprocessor: typing.Optional[str] = None
    tenant: typing.Optional[str] = None
    client_id: typing_extensions.Annotated[str, FieldMetadata(alias="clientId"), pydantic.Field(alias="clientId")]
    client_secret: typing_extensions.Annotated[
        str, FieldMetadata(alias="clientSecret"), pydantic.Field(alias="clientSecret")
    ]
    redirect_uri: typing_extensions.Annotated[
        str, FieldMetadata(alias="redirectUri"), pydantic.Field(alias="redirectUri")
    ]
    refresh_with_scope: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="refreshWithScope"),
        pydantic.Field(
            alias="refreshWithScope",
            description="If true, the predefinedScope and secret scope will be sent with the refresh_token request.",
        ),
    ] = None
    """
    If true, the predefinedScope and secret scope will be sent with the refresh_token request.
    """

    endpoints: MutableOa2AuthorizationCodeClientEndpoints
    predefined_scope: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="predefinedScope"), pydantic.Field(alias="predefinedScope")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
