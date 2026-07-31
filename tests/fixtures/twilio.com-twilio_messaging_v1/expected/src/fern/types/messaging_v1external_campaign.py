

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MessagingV1ExternalCampaign(UniversalBaseModel):
    account_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that the Campaign belongs to.
    """

    campaign_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the preregistered campaign.
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    messaging_service_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) that the resource is associated with.
    """

    sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique string that identifies a US A2P Compliance resource `QE2c6890da8086d771620e9b13fadeba0b`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
