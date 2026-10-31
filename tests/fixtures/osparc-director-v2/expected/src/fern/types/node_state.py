

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .error_dict import ErrorDict
from .node_share_state import NodeShareState
from .running_state import RunningState


class NodeState(UniversalBaseModel):
    modified: typing.Optional[bool] = pydantic.Field(default=None)
    """
    true if the node's outputs need to be re-computed
    """

    dependencies: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    contains the node inputs dependencies if they need to be computed first
    """

    current_status: typing_extensions.Annotated[
        typing.Optional[RunningState],
        FieldMetadata(alias="currentStatus"),
        pydantic.Field(alias="currentStatus", description="the node's current state"),
    ] = None
    """
    the node's current state
    """

    progress: typing.Optional[float] = pydantic.Field(default=None)
    """
    current progress of the task if available (None if not started or not a computational task)
    """

    lock_state: typing.Optional[NodeShareState] = pydantic.Field(default=None)
    """
    the node's lock state
    """

    errors: typing.Optional[typing.List[ErrorDict]] = pydantic.Field(default=None)
    """
    error details when the node is in a FAILED state
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
