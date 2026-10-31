

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaskProgress(UniversalBaseModel):
    """
    Helps the user to keep track of the progress. Progress is expected to be
    defined as a float bound between 0.0 and 1.0
    """

    task_id: typing.Optional[str] = None
    message: typing.Optional[str] = None
    percent: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
