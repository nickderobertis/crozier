

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CurrentUserEnergyResponseEnergyDaysItem(UniversalBaseModel):
    date: dt.date = pydantic.Field()
    """
    Learner-local calendar date without a time or UTC offset
    """

    energy: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
