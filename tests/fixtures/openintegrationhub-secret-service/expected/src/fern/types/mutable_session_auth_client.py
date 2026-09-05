

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .mutable_session_auth_client_endpoints import MutableSessionAuthClientEndpoints
from .mutable_session_auth_client_type import MutableSessionAuthClientType
from .owner import Owner
from .session_field import SessionField


class MutableSessionAuthClient(UniversalBaseModel):
    name: str
    owners: typing.List[Owner]
    type: MutableSessionAuthClientType
    preprocessor: typing.Optional[str] = None
    tenant: typing.Optional[str] = None
    fields: typing.List[SessionField]
    token_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tokenPath"), pydantic.Field(alias="tokenPath")
    ] = None
    expiration_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="expirationPath"), pydantic.Field(alias="expirationPath")
    ] = None
    endpoints: MutableSessionAuthClientEndpoints

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
