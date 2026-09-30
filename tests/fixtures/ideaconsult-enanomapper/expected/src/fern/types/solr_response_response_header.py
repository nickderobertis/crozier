

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SolrResponseResponseHeader(UniversalBaseModel):
    q_time: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="QTime"), pydantic.Field(alias="QTime")
    ] = None
    params: typing.Optional[typing.Dict[str, typing.Any]] = None
    status: typing.Optional[int] = None
    zk_connected: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="zkConnected"), pydantic.Field(alias="zkConnected")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
