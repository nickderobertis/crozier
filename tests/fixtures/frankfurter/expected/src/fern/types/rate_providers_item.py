

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RateProvidersItem(UniversalBaseModel):
    key: str = pydantic.Field()
    """
    Provider key
    """

    date: dt.date = pydantic.Field()
    """
    Provider observation date used for this entry
    """

    rate: float = pydantic.Field()
    """
    Provider's rate, rebased to the row's base
    """

    excluded: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present and true when this entry did not contribute to the blended rate
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
