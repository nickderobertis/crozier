

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .state_blob import StateBlob
from .stream_descriptor import StreamDescriptor


class StreamState(UniversalBaseModel):
    stream_descriptor: typing_extensions.Annotated[StreamDescriptor, FieldMetadata(alias="streamDescriptor")]
    stream_state: typing_extensions.Annotated[typing.Optional[StateBlob], FieldMetadata(alias="streamState")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
