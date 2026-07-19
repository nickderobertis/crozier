

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037JobTimeSystem(UniversalBaseModel):
    """
    System time values
    """

    seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of CPU-seconds used by the system on behalf of the process (in kernel mode), in seconds
    """

    microseconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of CPU-seconds used by the system on behalf of the process (in kernel mode), in microseconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
