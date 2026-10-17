

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CheckpointConfig(UniversalBaseModel):
    """
    Checkpoint config.
    """

    thread_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the thread associated with this checkpoint.
    """

    checkpoint_ns: typing.Optional[str] = pydantic.Field(default=None)
    """
    Namespace for the checkpoint, used for organization and retrieval.
    """

    checkpoint_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional unique identifier for the checkpoint itself.
    """

    checkpoint_map: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Optional dictionary containing checkpoint-specific data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
