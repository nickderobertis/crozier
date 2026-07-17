

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RelativeDelta(UniversalBaseModel):
    """
    Relative delta
    """

    type: typing_extensions.Annotated[str, FieldMetadata(alias="__type"), pydantic.Field(alias="__type")]
    day: int
    days: int
    hour: int
    hours: int
    leapdays: int
    microsecond: int
    microseconds: int
    minute: int
    minutes: int
    month: int
    months: int
    second: int
    seconds: int
    year: int
    years: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
