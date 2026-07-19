

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037JobTimeTotal(UniversalBaseModel):
    """
    System time values
    """

    seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of CPU-seconds used by the job, in seconds
    """

    microseconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of CPU-seconds used by the job, in microseconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
