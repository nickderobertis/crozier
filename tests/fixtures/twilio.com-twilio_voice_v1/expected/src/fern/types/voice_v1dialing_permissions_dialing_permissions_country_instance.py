

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VoiceV1DialingPermissionsDialingPermissionsCountryInstance(UniversalBaseModel):
    continent: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the continent in which the country is located.
    """

    country_codes: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The E.164 assigned [country codes(s)](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html)
    """

    high_risk_special_numbers_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether dialing to high-risk special services numbers is enabled. These prefixes include number ranges allocated by the country and include premium numbers, special services, shared cost, and others
    """

    high_risk_tollfraud_numbers_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether dialing to high-risk [toll fraud](https://www.twilio.com/learn/voice-and-video/toll-fraud) numbers is enabled. These prefixes include narrow number ranges that have a high-risk of international revenue sharing fraud (IRSF) attacks, also known as [toll fraud](https://www.twilio.com/learn/voice-and-video/toll-fraud). These prefixes are collected from anti-fraud databases and verified by analyzing calls on our network. These prefixes are not available for download and are updated frequently
    """

    iso_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    """

    links: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    A list of URLs related to this resource.
    """

    low_risk_numbers_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether dialing to low-risk numbers is enabled.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the country.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The absolute URL of this resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
