

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .state_blob import StateBlob
from .stream_state import StreamState


class GlobalState(UniversalBaseModel):
    shared_state: typing.Optional[StateBlob] = None
    stream_states: typing_extensions.Annotated[
        typing.List[StreamState], FieldMetadata(alias="streamStates"), pydantic.Field(alias="streamStates")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
