

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_schema_customization import RemoteSchemaCustomization
from .remote_schema_def_headers_item import RemoteSchemaDefHeadersItem
from .remote_schema_def_introspection_headers_item import RemoteSchemaDefIntrospectionHeadersItem


class RemoteSchemaDef(UniversalBaseModel):
    customization: typing.Optional[RemoteSchemaCustomization] = None
    forward_client_headers: typing.Optional[bool] = None
    headers: typing.Optional[typing.List[RemoteSchemaDefHeadersItem]] = None
    introspection_headers: typing.Optional[typing.List[RemoteSchemaDefIntrospectionHeadersItem]] = None
    timeout_seconds: typing.Optional[float] = None
    url: typing.Optional[str] = None
    url_from_env: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
