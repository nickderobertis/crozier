

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InsightPreferenceDateListing(UniversalBaseModel):
    day_of_month: typing.Optional[int] = pydantic.Field(default=None)
    """
    The day of month at which budgeting/insights should start.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
