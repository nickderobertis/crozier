

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InlineResponse2001Tasks(UniversalBaseModel):
    id: int = pydantic.Field()
    """
    The ID of task.
    """

    state: str = pydantic.Field()
    """
    The state of the task.
    """

    worker_id: str = pydantic.Field()
    """
    The worker ID of the task.
    """

    msg: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
