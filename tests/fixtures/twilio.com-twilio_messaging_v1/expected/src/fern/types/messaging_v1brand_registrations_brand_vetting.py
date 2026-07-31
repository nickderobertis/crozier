

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .brand_vetting_enum_vetting_provider import BrandVettingEnumVettingProvider


class MessagingV1BrandRegistrationsBrandVetting(UniversalBaseModel):
    account_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the vetting record.
    """

    brand_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique string to identify Brand Registration.
    """

    brand_vetting_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Twilio SID of the third-party vetting record.
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    date_updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The absolute URL of the Brand Vetting resource.
    """

    vetting_class: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of vetting that has been conducted. One of “STANDARD” (Aegis) or “POLITICAL” (Campaign Verify).
    """

    vetting_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the vetting from the third-party provider.
    """

    vetting_provider: typing.Optional[BrandVettingEnumVettingProvider] = pydantic.Field(default=None)
    """
    The third-party provider that has conducted the vetting. One of “CampaignVerify” (Campaign Verify tokens) or “AEGIS” (Secondary Vetting).
    """

    vetting_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the import vetting attempt. One of “PENDING,” “SUCCESS,” or “FAILED”.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
