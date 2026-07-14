

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TimeStamp(UniversalBaseModel):
    nano_seconds: typing_extensions.Annotated[int, FieldMetadata(alias="nanoSeconds")] = pydantic.Field()
    """
    The nanoseconds part of the Time. Time is defined as Unix-time since January 1, 1970, 00:00:00 UTC.
    """

    seconds: int = pydantic.Field()
    """
    The seconds part of the Time. Time is defined as Unix-time since January 1, 1970, 00:00:00 UTC.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
