

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MetricsThisWeek(UniversalBaseModel):
    """
    Summary totals for the last 7 days
    """

    added: typing.Optional[int] = pydantic.Field(default=None)
    """
    APIs added in the last week
    """

    updated: typing.Optional[int] = pydantic.Field(default=None)
    """
    APIs updated in the last week
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
