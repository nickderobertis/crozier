

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .baseline_info_status import BaselineInfoStatus


class BaselineInfo(UniversalBaseModel):
    """
    Contains baseline information for a feature.
    """

    status: typing.Optional[BaselineInfoStatus] = None
    low_date: typing.Optional[dt.date] = None
    high_date: typing.Optional[dt.date] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
