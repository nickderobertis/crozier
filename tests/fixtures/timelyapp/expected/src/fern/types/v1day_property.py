

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1DayProperty(UniversalBaseModel):
    id: int = pydantic.Field()
    """
    Unique identifier for the day property
    """

    user_id: int = pydantic.Field()
    """
    User ID this day property belongs to
    """

    account_id: int = pydantic.Field()
    """
    Account ID this day property belongs to
    """

    date: dt.date = pydantic.Field()
    """
    Date in YYYY-MM-DD format
    """

    locked: bool = pydantic.Field()
    """
    Whether the day is locked for time entry modifications
    """

    updated_at: int = pydantic.Field()
    """
    Unix timestamp of when the day property was last updated
    """

    created_at: int = pydantic.Field()
    """
    Unix timestamp of when the day property was created
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
