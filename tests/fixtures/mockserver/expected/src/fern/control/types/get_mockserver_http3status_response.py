

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetMockserverHttp3StatusResponse(UniversalBaseModel):
    enabled: typing.Optional[bool] = None
    port: typing.Optional[int] = None
    active_connections: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="activeConnections"), pydantic.Field(alias="activeConnections")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
