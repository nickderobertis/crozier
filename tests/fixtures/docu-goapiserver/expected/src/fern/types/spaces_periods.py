

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SpacesPeriods(UniversalBaseModel):
    """
    Spaces Periods.
    """

    school_id: str = pydantic.Field()
    """
    School id.
    """

    school_name: str
    is_active: bool
    room_count: int
    period_count: int
    periods: typing.Optional[typing.List[str]] = None
    period_start: typing.Optional[str] = None
    period_end: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
