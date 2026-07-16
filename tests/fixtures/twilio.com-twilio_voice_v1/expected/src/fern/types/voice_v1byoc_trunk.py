

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .voice_v1byoc_trunk_status_callback_method import VoiceV1ByocTrunkStatusCallbackMethod
from .voice_v1byoc_trunk_voice_fallback_method import VoiceV1ByocTrunkVoiceFallbackMethod
from .voice_v1byoc_trunk_voice_method import VoiceV1ByocTrunkVoiceMethod


class VoiceV1ByocTrunk(UniversalBaseModel):
    account_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the BYOC Trunk resource.
    """

    cnam_lookup_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
    """

    connection_policy_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    """

    date_updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    """

    friendly_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The string that you assigned to describe the resource.
    """

    from_domain_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to "call back" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to "sip.twilio.com".
    """

    sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique string that that we created to identify the BYOC Trunk resource.
    """

    status_callback_method: typing.Optional[VoiceV1ByocTrunkStatusCallbackMethod] = pydantic.Field(default=None)
    """
    The HTTP method we use to call `status_callback_url`. Either `GET` or `POST`.
    """

    status_callback_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL that we call to pass status parameters (such as call ended) to your application.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The absolute URL of the resource.
    """

    voice_fallback_method: typing.Optional[VoiceV1ByocTrunkVoiceFallbackMethod] = pydantic.Field(default=None)
    """
    The HTTP method we use to call `voice_fallback_url`. Can be: `GET` or `POST`.
    """

    voice_fallback_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL that we call when an error occurs while retrieving or executing the TwiML requested from `voice_url`.
    """

    voice_method: typing.Optional[VoiceV1ByocTrunkVoiceMethod] = pydantic.Field(default=None)
    """
    The HTTP method we use to call `voice_url`. Can be: `GET` or `POST`.
    """

    voice_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL we call using the `voice_method` when the BYOC Trunk receives a call.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
