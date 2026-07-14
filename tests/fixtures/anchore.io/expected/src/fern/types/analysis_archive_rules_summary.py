

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AnalysisArchiveRulesSummary(UniversalBaseModel):
    """
    Summary of the transition rule set
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of rules for this account
    """

    last_updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The newest last_updated timestamp from the set of rules
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
