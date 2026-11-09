

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SandboxPublicTokenCreateRequestOptionsTransactions(UniversalBaseModel):
    """
    An optional set of parameters corresponding to transactions options.
    """

    end_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The most recent date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD.
    """

    start_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The earliest date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
