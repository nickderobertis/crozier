

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1DayPropertiesCreateDayProperty(UniversalBaseModel):
    dates: typing.List[str] = pydantic.Field()
    """
    Array of dates to lock/unlock in YYYY-MM-DD format
    """

    user_ids: typing.List[int] = pydantic.Field()
    """
    Array of user IDs to apply the day property to
    """

    locked: bool = pydantic.Field()
    """
    Whether to lock (true) or unlock (false) the specified days
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
