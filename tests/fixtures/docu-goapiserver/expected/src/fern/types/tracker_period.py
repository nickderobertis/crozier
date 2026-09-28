

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tracker_space import TrackerSpace


class TrackerPeriod(UniversalBaseModel):
    """
    Tracker Period.
    """

    period: str
    total_occupied_spaces: int
    is_over_enrolled: bool
    spaces: typing.Optional[typing.List[TrackerSpace]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
