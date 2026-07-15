

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .connection_id import ConnectionId
from .connection_state_type import ConnectionStateType
from .global_state import GlobalState
from .state_blob import StateBlob
from .stream_state import StreamState


class ConnectionState(UniversalBaseModel):
    """
    Contains the state for a connection. The stateType field identifies what type of state it is. Only the field corresponding to that type will be set, the rest will be null. If stateType=not_set, then none of the fields will be set.
    """

    connection_id: typing_extensions.Annotated[ConnectionId, FieldMetadata(alias="connectionId")]
    global_state: typing_extensions.Annotated[typing.Optional[GlobalState], FieldMetadata(alias="globalState")] = None
    state: typing.Optional[StateBlob] = None
    state_type: typing_extensions.Annotated[ConnectionStateType, FieldMetadata(alias="stateType")]
    stream_state: typing_extensions.Annotated[
        typing.Optional[typing.List[StreamState]], FieldMetadata(alias="streamState")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
