

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .mutable_oa1three_legged_client_endpoints import MutableOa1ThreeLeggedClientEndpoints
from .mutable_oa1three_legged_client_type import MutableOa1ThreeLeggedClientType
from .owner import Owner


class MutableOa1ThreeLeggedClient(UniversalBaseModel):
    name: str
    owners: typing.List[Owner]
    type: MutableOa1ThreeLeggedClientType
    preprocessor: typing.Optional[str] = None
    tenant: typing.Optional[str] = None
    app_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="appName"), pydantic.Field(alias="appName")
    ] = None
    key: str
    secret: str
    nonce: typing.Optional[str] = None
    signature: typing.Optional[str] = None
    signature_method: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="signatureMethod"), pydantic.Field(alias="signatureMethod")
    ] = None
    endpoints: typing.Optional[MutableOa1ThreeLeggedClientEndpoints] = None
    redirect_uri: typing_extensions.Annotated[
        str, FieldMetadata(alias="redirectUri"), pydantic.Field(alias="redirectUri")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
