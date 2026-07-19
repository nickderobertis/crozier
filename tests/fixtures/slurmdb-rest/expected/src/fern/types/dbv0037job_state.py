

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037JobState(UniversalBaseModel):
    """
    State properties of job
    """

    current: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current state of job
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Last reason job didn't run
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
