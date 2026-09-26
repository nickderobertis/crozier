

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ThreadCheckpoint(UniversalBaseModel):
    """
    Structured identifier for a thread checkpoint, ie. an entry in the thread's history.
    """

    checkpoint_id: str = pydantic.Field()
    """
    The ID of the checkpoint.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
