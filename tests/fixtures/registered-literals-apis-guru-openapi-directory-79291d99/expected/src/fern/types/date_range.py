

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .iso8601date import Iso8601Date


class DateRange(UniversalBaseModel):
    """
    A date range with a start and end date
    """

    beginning: Iso8601Date
    ending: Iso8601Date

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
