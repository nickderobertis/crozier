

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FleetUiMessageChunkToolOutputAvailable(UniversalBaseModel):
    tool_call_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="toolCallId"), pydantic.Field(alias="toolCallId")
    ]
    output: typing.Any
    dynamic: typing.Optional[bool] = None
    provider_executed: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="providerExecuted"), pydantic.Field(alias="providerExecuted")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
