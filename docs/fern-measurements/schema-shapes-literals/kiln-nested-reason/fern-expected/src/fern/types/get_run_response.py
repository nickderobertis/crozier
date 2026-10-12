

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .get_run_response_stop_reason import GetRunResponseStopReason


class GetRunResponse(UniversalBaseModel):
    stop_reason: typing_extensions.Annotated[
        typing.Optional[GetRunResponseStopReason], FieldMetadata(alias="stopReason"), pydantic.Field(alias="stopReason")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
