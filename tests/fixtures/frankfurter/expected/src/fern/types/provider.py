

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provider_publish_cadence import ProviderPublishCadence


class Provider(UniversalBaseModel):
    key: str = pydantic.Field()
    """
    Provider identifier
    """

    name: str = pydantic.Field()
    """
    Full provider name
    """

    country_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO 3166-1 alpha-2 country code
    """

    rate_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Official rate type as used by the source
    """

    pivot_currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    Base currency for published rates
    """

    data_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to the data source
    """

    terms_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to terms of use
    """

    start_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Earliest available date
    """

    end_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Latest available date
    """

    publish_cadence: typing.Optional[ProviderPublishCadence] = pydantic.Field(default=None)
    """
    How often the provider publishes rates. Determines the unit of publishes_missed: a count of days, ISO weeks, or calendar months. Null for historical-only providers with no scheduled cadence.
    """

    publishes_missed: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of expected publishes missed since end_date, in units of publish_cadence. For daily providers, counts scheduled publish days strictly between end_date and today. For weekly and monthly providers, counts ISO weeks or calendar months between the latest imported bucket and the bucket whose publish window has already started. Null when the provider has no scheduled cadence or no imported data.
    """

    currencies: typing.List[str] = pydantic.Field()
    """
    Currency codes covered by this provider
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
