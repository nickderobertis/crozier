

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Currency(UniversalBaseModel):
    iso_code: str = pydantic.Field()
    """
    ISO 4217 currency code
    """

    iso_numeric: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO 4217 numeric code
    """

    name: str = pydantic.Field()
    """
    Full currency name
    """

    symbol: typing.Optional[str] = pydantic.Field(default=None)
    """
    Currency symbol
    """

    start_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Earliest available date
    """

    end_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Latest available date
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
