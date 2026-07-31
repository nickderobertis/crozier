

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .messaging_v1service_fallback_method import MessagingV1ServiceFallbackMethod
from .messaging_v1service_inbound_method import MessagingV1ServiceInboundMethod
from .service_enum_scan_message_content import ServiceEnumScanMessageContent


class MessagingV1Service(UniversalBaseModel):
    account_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Service resource.
    """

    area_code_geomatch: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to enable [Area Code Geomatch](https://www.twilio.com/docs/sms/services#area-code-geomatch) on the Service Instance.
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    date_updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    fallback_method: typing.Optional[MessagingV1ServiceFallbackMethod] = pydantic.Field(default=None)
    """
    The HTTP method we use to call `fallback_url`. Can be: `GET` or `POST`.
    """

    fallback_to_long_code: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to enable [Fallback to Long Code](https://www.twilio.com/docs/sms/services#fallback-to-long-code) for messages sent through the Service instance.
    """

    fallback_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL that we call using `fallback_method` if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `fallback_url` defined for the Messaging Service.
    """

    friendly_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The string that you assigned to describe the resource.
    """

    inbound_method: typing.Optional[MessagingV1ServiceInboundMethod] = pydantic.Field(default=None)
    """
    The HTTP method we use to call `inbound_request_url`. Can be `GET` or `POST`.
    """

    inbound_request_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL we call using `inbound_method` when a message is received by any phone number or short code in the Service. When this property is `null`, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `inbound_request_url` defined for the Messaging Service.
    """

    links: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The absolute URLs of related resources.
    """

    mms_converter: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to enable the [MMS Converter](https://www.twilio.com/docs/sms/services#mms-converter) for messages sent through the Service instance.
    """

    scan_message_content: typing.Optional[ServiceEnumScanMessageContent] = pydantic.Field(default=None)
    """
    Reserved.
    """

    sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique string that we created to identify the Service resource.
    """

    smart_encoding: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to enable [Smart Encoding](https://www.twilio.com/docs/sms/services#smart-encoding) for messages sent through the Service instance.
    """

    status_callback: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL we call to [pass status updates](https://www.twilio.com/docs/sms/api/message-resource#message-status-values) about message delivery.
    """

    sticky_sender: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to enable [Sticky Sender](https://www.twilio.com/docs/sms/services#sticky-sender) on the Service instance.
    """

    synchronous_validation: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Reserved.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The absolute URL of the Service resource.
    """

    us_app_to_person_registered: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether US A2P campaign is registered for this Service.
    """

    use_inbound_webhook_on_number: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean value that indicates either the webhook url configured on the phone number will be used or `inbound_request_url`/`fallback_url` url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the `inbound_request_url`/`fallback_url` defined for the Messaging Service.
    """

    usecase: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string that describes the scenario in which the Messaging Service will be used. Examples: [notification, marketing, verification, poll ..]
    """

    validity_period: typing.Optional[int] = pydantic.Field(default=None)
    """
    How long, in seconds, messages sent from the Service are valid. Can be an integer from `1` to `14,400`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
