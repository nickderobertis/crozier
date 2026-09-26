

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdateOwnerBriefRequest(UniversalBaseModel):
    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable or disable the weekly owner-brief DM. Setting false is the
    one-tap opt-out. Absent leaves the enabled flag unchanged.
    """

    weekday: typing.Optional[int] = pydantic.Field(default=None)
    """
    Weekday the brief fires on (0=Sunday .. 6=Saturday).
    """

    hour: typing.Optional[int] = pydantic.Field(default=None)
    """
    Hour-of-day (0-23) the brief fires at.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
