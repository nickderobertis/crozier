

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BadEventQueueIdError(UniversalBaseModel):
    result: typing.Any
    msg: typing.Any
    code: typing.Any
    queue_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The string that identifies the invalid event queue.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
