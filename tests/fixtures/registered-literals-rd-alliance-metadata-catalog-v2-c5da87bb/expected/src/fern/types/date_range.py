

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DateRange(UniversalBaseModel):
    start: typing.Optional[str] = pydantic.Field(default=None)
    """
    The start date of the period.
    """

    end: typing.Optional[str] = pydantic.Field(default=None)
    """
    The end date of the period (if applicable).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
