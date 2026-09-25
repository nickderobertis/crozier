



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .audio import Audio
    from .audio_audio import AudioAudio
    from .audio_message_type import AudioMessageType
    from .base_message_type import BaseMessageType
    from .channel_options_messenger import ChannelOptionsMessenger
    from .channel_options_messenger_channel import ChannelOptionsMessengerChannel
    from .channel_options_messenger_messenger import ChannelOptionsMessengerMessenger
    from .channel_options_messenger_messenger_category import ChannelOptionsMessengerMessengerCategory
    from .channel_options_mms import ChannelOptionsMms
    from .channel_options_mms_channel import ChannelOptionsMmsChannel
    from .channel_options_sms import ChannelOptionsSms
    from .channel_options_sms_channel import ChannelOptionsSmsChannel
    from .channel_options_viber import ChannelOptionsViber
    from .channel_options_viber_channel import ChannelOptionsViberChannel
    from .channel_options_viber_viber_service import ChannelOptionsViberViberService
    from .channel_options_viber_viber_service_category import ChannelOptionsViberViberServiceCategory
    from .channel_options_viber_video import ChannelOptionsViberVideo
    from .channel_options_viber_video_channel import ChannelOptionsViberVideoChannel
    from .channel_options_viber_video_viber_service import ChannelOptionsViberVideoViberService
    from .channel_options_viber_video_viber_service_category import ChannelOptionsViberVideoViberServiceCategory
    from .channel_options_viber_with_button import ChannelOptionsViberWithButton
    from .channel_options_viber_with_button_channel import ChannelOptionsViberWithButtonChannel
    from .channel_options_viber_with_button_viber_service import ChannelOptionsViberWithButtonViberService
    from .channel_options_viber_with_button_viber_service_action import ChannelOptionsViberWithButtonViberServiceAction
    from .channel_options_viber_with_button_viber_service_category import (
        ChannelOptionsViberWithButtonViberServiceCategory,
    )
    from .channel_options_whatsapp import ChannelOptionsWhatsapp
    from .channel_options_whatsapp_channel import ChannelOptionsWhatsappChannel
    from .context import Context
    from .context_whatsapp_referred_product import ContextWhatsappReferredProduct
    from .custom import Custom
    from .custom_message_type import CustomMessageType
    from .error_channel import ErrorChannel
    from .error_channel_params import ErrorChannelParams
    from .error_channel_params_invalid_parameters_item import ErrorChannelParamsInvalidParametersItem
    from .error_client_reference import ErrorClientReference
    from .error_internal import ErrorInternal
    from .error_invalid_json import ErrorInvalidJson
    from .error_message_params import ErrorMessageParams
    from .error_message_params_invalid_parameters_item import ErrorMessageParamsInvalidParametersItem
    from .error_message_type import ErrorMessageType
    from .error_payment_required import ErrorPaymentRequired
    from .error_recipient import ErrorRecipient
    from .error_sender import ErrorSender
    from .error_throttled import ErrorThrottled
    from .error_unauthorized_invalid_application import ErrorUnauthorizedInvalidApplication
    from .error_unauthorized_missing_credentials import ErrorUnauthorizedMissingCredentials
    from .file import File
    from .file_file import FileFile
    from .file_message_type import FileMessageType
    from .from_id import FromId
    from .from_number import FromNumber
    from .image import Image
    from .image_image import ImageImage
    from .image_message_type import ImageMessageType
    from .inbound_message_mms import InboundMessageMms
    from .inbound_message_mms_channel import InboundMessageMmsChannel
    from .inbound_message_sms import InboundMessageSms
    from .inbound_message_sms_channel import InboundMessageSmsChannel
    from .inbound_message_sms_sms import InboundMessageSmsSms
    from .inbound_messenger_message_common import InboundMessengerMessageCommon
    from .inbound_messenger_message_common_channel import InboundMessengerMessageCommonChannel
    from .inbound_viber_message_common import InboundViberMessageCommon
    from .inbound_viber_message_common_channel import InboundViberMessageCommonChannel
    from .inbound_viber_message_common_context import InboundViberMessageCommonContext
    from .inbound_whats_app_message_common import InboundWhatsAppMessageCommon
    from .inbound_whats_app_message_common_channel import InboundWhatsAppMessageCommonChannel
    from .location import Location
    from .location_location import LocationLocation
    from .location_message_type import LocationMessageType
    from .message_status_base import MessageStatusBase
    from .message_status_base_error import MessageStatusBaseError
    from .message_status_base_status import MessageStatusBaseStatus
    from .message_status_base_usage import MessageStatusBaseUsage
    from .message_status_base_usage_currency import MessageStatusBaseUsageCurrency
    from .message_status_messenger import MessageStatusMessenger
    from .message_status_messenger_channel import MessageStatusMessengerChannel
    from .message_status_messenger_status import MessageStatusMessengerStatus
    from .message_status_mms import MessageStatusMms
    from .message_status_mms_channel import MessageStatusMmsChannel
    from .message_status_sms import MessageStatusSms
    from .message_status_sms_channel import MessageStatusSmsChannel
    from .message_status_viber import MessageStatusViber
    from .message_status_viber_channel import MessageStatusViberChannel
    from .message_status_viber_status import MessageStatusViberStatus
    from .message_status_whats_app import MessageStatusWhatsApp
    from .message_status_whats_app_channel import MessageStatusWhatsAppChannel
    from .message_status_whats_app_status import MessageStatusWhatsAppStatus
    from .message_status_whats_app_usage import MessageStatusWhatsAppUsage
    from .message_status_whats_app_usage_currency import MessageStatusWhatsAppUsageCurrency
    from .message_status_whats_app_whatsapp import MessageStatusWhatsAppWhatsapp
    from .message_status_whats_app_whatsapp_conversation import MessageStatusWhatsAppWhatsappConversation
    from .message_status_whats_app_whatsapp_conversation_origin import MessageStatusWhatsAppWhatsappConversationOrigin
    from .message_uuid import MessageUuid
    from .order import Order
    from .order_message_type import OrderMessageType
    from .order_order import OrderOrder
    from .order_order_product_items_item import OrderOrderProductItemsItem
    from .profile import Profile
    from .reply import Reply
    from .reply_message_type import ReplyMessageType
    from .reply_reply import ReplyReply
    from .send_message_request import SendMessageRequest
    from .send_message_request_four import SendMessageRequestFour
    from .send_message_request_four_one import SendMessageRequestFourOne
    from .send_message_request_four_one_image import SendMessageRequestFourOneImage
    from .send_message_request_four_three import SendMessageRequestFourThree
    from .send_message_request_four_three_file import SendMessageRequestFourThreeFile
    from .send_message_request_four_two import SendMessageRequestFourTwo
    from .send_message_request_four_two_video import SendMessageRequestFourTwoVideo
    from .send_message_request_four_zero import SendMessageRequestFourZero
    from .send_message_request_one import SendMessageRequestOne
    from .send_message_request_one_one import SendMessageRequestOneOne
    from .send_message_request_one_one_vcard import SendMessageRequestOneOneVcard
    from .send_message_request_one_three import SendMessageRequestOneThree
    from .send_message_request_one_three_message_type import SendMessageRequestOneThreeMessageType
    from .send_message_request_one_three_video import SendMessageRequestOneThreeVideo
    from .send_message_request_one_two import SendMessageRequestOneTwo
    from .send_message_request_one_two_audio import SendMessageRequestOneTwoAudio
    from .send_message_request_one_two_message_type import SendMessageRequestOneTwoMessageType
    from .send_message_request_one_zero import SendMessageRequestOneZero
    from .send_message_request_one_zero_image import SendMessageRequestOneZeroImage
    from .send_message_request_three import SendMessageRequestThree
    from .send_message_request_three_four import SendMessageRequestThreeFour
    from .send_message_request_three_four_file import SendMessageRequestThreeFourFile
    from .send_message_request_three_one import SendMessageRequestThreeOne
    from .send_message_request_three_one_image import SendMessageRequestThreeOneImage
    from .send_message_request_three_three import SendMessageRequestThreeThree
    from .send_message_request_three_three_video import SendMessageRequestThreeThreeVideo
    from .send_message_request_three_two import SendMessageRequestThreeTwo
    from .send_message_request_three_two_audio import SendMessageRequestThreeTwoAudio
    from .send_message_request_three_zero import SendMessageRequestThreeZero
    from .send_message_request_two import SendMessageRequestTwo
    from .send_message_request_two_five import SendMessageRequestTwoFive
    from .send_message_request_two_five_file import SendMessageRequestTwoFiveFile
    from .send_message_request_two_four import SendMessageRequestTwoFour
    from .send_message_request_two_four_video import SendMessageRequestTwoFourVideo
    from .send_message_request_two_one import SendMessageRequestTwoOne
    from .send_message_request_two_seven import SendMessageRequestTwoSeven
    from .send_message_request_two_six import SendMessageRequestTwoSix
    from .send_message_request_two_six_whatsapp import SendMessageRequestTwoSixWhatsapp
    from .send_message_request_two_six_whatsapp_policy import SendMessageRequestTwoSixWhatsappPolicy
    from .send_message_request_two_three import SendMessageRequestTwoThree
    from .send_message_request_two_three_audio import SendMessageRequestTwoThreeAudio
    from .send_message_request_two_two import SendMessageRequestTwoTwo
    from .send_message_request_two_two_image import SendMessageRequestTwoTwoImage
    from .send_message_request_two_zero import SendMessageRequestTwoZero
    from .send_message_request_zero import SendMessageRequestZero
    from .send_message_response import SendMessageResponse
    from .send_message_response_message_uuid import SendMessageResponseMessageUuid
    from .send_message_response_one import SendMessageResponseOne
    from .send_message_response_three import SendMessageResponseThree
    from .send_message_response_two import SendMessageResponseTwo
    from .send_message_response_zero import SendMessageResponseZero
    from .template import Template
    from .template_message_type import TemplateMessageType
    from .template_parameters import TemplateParameters
    from .template_template import TemplateTemplate
    from .text import Text
    from .text_message_type import TextMessageType
    from .timestamp import Timestamp
    from .to_id import ToId
    from .to_number import ToNumber
    from .unauthorized_error_body import (
        UnauthorizedErrorBody,
        UnauthorizedErrorBody_HttpsDeveloperNexmoComApiErrorsUnathorized,
        UnauthorizedErrorBody_HttpsDeveloperNexmoComApiErrorsUnprovisioned,
    )
    from .unprocessable_entity_error_body import (
        UnprocessableEntityErrorBody,
        UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsInvalidJson,
        UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1060,
        UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus110,
        UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1100,
        UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1110,
        UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1120,
        UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1140,
        UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1150,
    )
    from .unsupported import Unsupported
    from .unsupported_message_type import UnsupportedMessageType
    from .usage import Usage
    from .usage_currency import UsageCurrency
    from .v_card import VCard
    from .v_card_message_type import VCardMessageType
    from .v_card_vcard import VCardVcard
    from .video import Video
    from .video_message_type import VideoMessageType
    from .video_video import VideoVideo
_dynamic_imports: typing.Dict[str, str] = {
    "Audio": ".audio",
    "AudioAudio": ".audio_audio",
    "AudioMessageType": ".audio_message_type",
    "BaseMessageType": ".base_message_type",
    "ChannelOptionsMessenger": ".channel_options_messenger",
    "ChannelOptionsMessengerChannel": ".channel_options_messenger_channel",
    "ChannelOptionsMessengerMessenger": ".channel_options_messenger_messenger",
    "ChannelOptionsMessengerMessengerCategory": ".channel_options_messenger_messenger_category",
    "ChannelOptionsMms": ".channel_options_mms",
    "ChannelOptionsMmsChannel": ".channel_options_mms_channel",
    "ChannelOptionsSms": ".channel_options_sms",
    "ChannelOptionsSmsChannel": ".channel_options_sms_channel",
    "ChannelOptionsViber": ".channel_options_viber",
    "ChannelOptionsViberChannel": ".channel_options_viber_channel",
    "ChannelOptionsViberViberService": ".channel_options_viber_viber_service",
    "ChannelOptionsViberViberServiceCategory": ".channel_options_viber_viber_service_category",
    "ChannelOptionsViberVideo": ".channel_options_viber_video",
    "ChannelOptionsViberVideoChannel": ".channel_options_viber_video_channel",
    "ChannelOptionsViberVideoViberService": ".channel_options_viber_video_viber_service",
    "ChannelOptionsViberVideoViberServiceCategory": ".channel_options_viber_video_viber_service_category",
    "ChannelOptionsViberWithButton": ".channel_options_viber_with_button",
    "ChannelOptionsViberWithButtonChannel": ".channel_options_viber_with_button_channel",
    "ChannelOptionsViberWithButtonViberService": ".channel_options_viber_with_button_viber_service",
    "ChannelOptionsViberWithButtonViberServiceAction": ".channel_options_viber_with_button_viber_service_action",
    "ChannelOptionsViberWithButtonViberServiceCategory": ".channel_options_viber_with_button_viber_service_category",
    "ChannelOptionsWhatsapp": ".channel_options_whatsapp",
    "ChannelOptionsWhatsappChannel": ".channel_options_whatsapp_channel",
    "Context": ".context",
    "ContextWhatsappReferredProduct": ".context_whatsapp_referred_product",
    "Custom": ".custom",
    "CustomMessageType": ".custom_message_type",
    "ErrorChannel": ".error_channel",
    "ErrorChannelParams": ".error_channel_params",
    "ErrorChannelParamsInvalidParametersItem": ".error_channel_params_invalid_parameters_item",
    "ErrorClientReference": ".error_client_reference",
    "ErrorInternal": ".error_internal",
    "ErrorInvalidJson": ".error_invalid_json",
    "ErrorMessageParams": ".error_message_params",
    "ErrorMessageParamsInvalidParametersItem": ".error_message_params_invalid_parameters_item",
    "ErrorMessageType": ".error_message_type",
    "ErrorPaymentRequired": ".error_payment_required",
    "ErrorRecipient": ".error_recipient",
    "ErrorSender": ".error_sender",
    "ErrorThrottled": ".error_throttled",
    "ErrorUnauthorizedInvalidApplication": ".error_unauthorized_invalid_application",
    "ErrorUnauthorizedMissingCredentials": ".error_unauthorized_missing_credentials",
    "File": ".file",
    "FileFile": ".file_file",
    "FileMessageType": ".file_message_type",
    "FromId": ".from_id",
    "FromNumber": ".from_number",
    "Image": ".image",
    "ImageImage": ".image_image",
    "ImageMessageType": ".image_message_type",
    "InboundMessageMms": ".inbound_message_mms",
    "InboundMessageMmsChannel": ".inbound_message_mms_channel",
    "InboundMessageSms": ".inbound_message_sms",
    "InboundMessageSmsChannel": ".inbound_message_sms_channel",
    "InboundMessageSmsSms": ".inbound_message_sms_sms",
    "InboundMessengerMessageCommon": ".inbound_messenger_message_common",
    "InboundMessengerMessageCommonChannel": ".inbound_messenger_message_common_channel",
    "InboundViberMessageCommon": ".inbound_viber_message_common",
    "InboundViberMessageCommonChannel": ".inbound_viber_message_common_channel",
    "InboundViberMessageCommonContext": ".inbound_viber_message_common_context",
    "InboundWhatsAppMessageCommon": ".inbound_whats_app_message_common",
    "InboundWhatsAppMessageCommonChannel": ".inbound_whats_app_message_common_channel",
    "Location": ".location",
    "LocationLocation": ".location_location",
    "LocationMessageType": ".location_message_type",
    "MessageStatusBase": ".message_status_base",
    "MessageStatusBaseError": ".message_status_base_error",
    "MessageStatusBaseStatus": ".message_status_base_status",
    "MessageStatusBaseUsage": ".message_status_base_usage",
    "MessageStatusBaseUsageCurrency": ".message_status_base_usage_currency",
    "MessageStatusMessenger": ".message_status_messenger",
    "MessageStatusMessengerChannel": ".message_status_messenger_channel",
    "MessageStatusMessengerStatus": ".message_status_messenger_status",
    "MessageStatusMms": ".message_status_mms",
    "MessageStatusMmsChannel": ".message_status_mms_channel",
    "MessageStatusSms": ".message_status_sms",
    "MessageStatusSmsChannel": ".message_status_sms_channel",
    "MessageStatusViber": ".message_status_viber",
    "MessageStatusViberChannel": ".message_status_viber_channel",
    "MessageStatusViberStatus": ".message_status_viber_status",
    "MessageStatusWhatsApp": ".message_status_whats_app",
    "MessageStatusWhatsAppChannel": ".message_status_whats_app_channel",
    "MessageStatusWhatsAppStatus": ".message_status_whats_app_status",
    "MessageStatusWhatsAppUsage": ".message_status_whats_app_usage",
    "MessageStatusWhatsAppUsageCurrency": ".message_status_whats_app_usage_currency",
    "MessageStatusWhatsAppWhatsapp": ".message_status_whats_app_whatsapp",
    "MessageStatusWhatsAppWhatsappConversation": ".message_status_whats_app_whatsapp_conversation",
    "MessageStatusWhatsAppWhatsappConversationOrigin": ".message_status_whats_app_whatsapp_conversation_origin",
    "MessageUuid": ".message_uuid",
    "Order": ".order",
    "OrderMessageType": ".order_message_type",
    "OrderOrder": ".order_order",
    "OrderOrderProductItemsItem": ".order_order_product_items_item",
    "Profile": ".profile",
    "Reply": ".reply",
    "ReplyMessageType": ".reply_message_type",
    "ReplyReply": ".reply_reply",
    "SendMessageRequest": ".send_message_request",
    "SendMessageRequestFour": ".send_message_request_four",
    "SendMessageRequestFourOne": ".send_message_request_four_one",
    "SendMessageRequestFourOneImage": ".send_message_request_four_one_image",
    "SendMessageRequestFourThree": ".send_message_request_four_three",
    "SendMessageRequestFourThreeFile": ".send_message_request_four_three_file",
    "SendMessageRequestFourTwo": ".send_message_request_four_two",
    "SendMessageRequestFourTwoVideo": ".send_message_request_four_two_video",
    "SendMessageRequestFourZero": ".send_message_request_four_zero",
    "SendMessageRequestOne": ".send_message_request_one",
    "SendMessageRequestOneOne": ".send_message_request_one_one",
    "SendMessageRequestOneOneVcard": ".send_message_request_one_one_vcard",
    "SendMessageRequestOneThree": ".send_message_request_one_three",
    "SendMessageRequestOneThreeMessageType": ".send_message_request_one_three_message_type",
    "SendMessageRequestOneThreeVideo": ".send_message_request_one_three_video",
    "SendMessageRequestOneTwo": ".send_message_request_one_two",
    "SendMessageRequestOneTwoAudio": ".send_message_request_one_two_audio",
    "SendMessageRequestOneTwoMessageType": ".send_message_request_one_two_message_type",
    "SendMessageRequestOneZero": ".send_message_request_one_zero",
    "SendMessageRequestOneZeroImage": ".send_message_request_one_zero_image",
    "SendMessageRequestThree": ".send_message_request_three",
    "SendMessageRequestThreeFour": ".send_message_request_three_four",
    "SendMessageRequestThreeFourFile": ".send_message_request_three_four_file",
    "SendMessageRequestThreeOne": ".send_message_request_three_one",
    "SendMessageRequestThreeOneImage": ".send_message_request_three_one_image",
    "SendMessageRequestThreeThree": ".send_message_request_three_three",
    "SendMessageRequestThreeThreeVideo": ".send_message_request_three_three_video",
    "SendMessageRequestThreeTwo": ".send_message_request_three_two",
    "SendMessageRequestThreeTwoAudio": ".send_message_request_three_two_audio",
    "SendMessageRequestThreeZero": ".send_message_request_three_zero",
    "SendMessageRequestTwo": ".send_message_request_two",
    "SendMessageRequestTwoFive": ".send_message_request_two_five",
    "SendMessageRequestTwoFiveFile": ".send_message_request_two_five_file",
    "SendMessageRequestTwoFour": ".send_message_request_two_four",
    "SendMessageRequestTwoFourVideo": ".send_message_request_two_four_video",
    "SendMessageRequestTwoOne": ".send_message_request_two_one",
    "SendMessageRequestTwoSeven": ".send_message_request_two_seven",
    "SendMessageRequestTwoSix": ".send_message_request_two_six",
    "SendMessageRequestTwoSixWhatsapp": ".send_message_request_two_six_whatsapp",
    "SendMessageRequestTwoSixWhatsappPolicy": ".send_message_request_two_six_whatsapp_policy",
    "SendMessageRequestTwoThree": ".send_message_request_two_three",
    "SendMessageRequestTwoThreeAudio": ".send_message_request_two_three_audio",
    "SendMessageRequestTwoTwo": ".send_message_request_two_two",
    "SendMessageRequestTwoTwoImage": ".send_message_request_two_two_image",
    "SendMessageRequestTwoZero": ".send_message_request_two_zero",
    "SendMessageRequestZero": ".send_message_request_zero",
    "SendMessageResponse": ".send_message_response",
    "SendMessageResponseMessageUuid": ".send_message_response_message_uuid",
    "SendMessageResponseOne": ".send_message_response_one",
    "SendMessageResponseThree": ".send_message_response_three",
    "SendMessageResponseTwo": ".send_message_response_two",
    "SendMessageResponseZero": ".send_message_response_zero",
    "Template": ".template",
    "TemplateMessageType": ".template_message_type",
    "TemplateParameters": ".template_parameters",
    "TemplateTemplate": ".template_template",
    "Text": ".text",
    "TextMessageType": ".text_message_type",
    "Timestamp": ".timestamp",
    "ToId": ".to_id",
    "ToNumber": ".to_number",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
    "UnauthorizedErrorBody_HttpsDeveloperNexmoComApiErrorsUnathorized": ".unauthorized_error_body",
    "UnauthorizedErrorBody_HttpsDeveloperNexmoComApiErrorsUnprovisioned": ".unauthorized_error_body",
    "UnprocessableEntityErrorBody": ".unprocessable_entity_error_body",
    "UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsInvalidJson": ".unprocessable_entity_error_body",
    "UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1060": ".unprocessable_entity_error_body",
    "UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus110": ".unprocessable_entity_error_body",
    "UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1100": ".unprocessable_entity_error_body",
    "UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1110": ".unprocessable_entity_error_body",
    "UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1120": ".unprocessable_entity_error_body",
    "UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1140": ".unprocessable_entity_error_body",
    "UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1150": ".unprocessable_entity_error_body",
    "Unsupported": ".unsupported",
    "UnsupportedMessageType": ".unsupported_message_type",
    "Usage": ".usage",
    "UsageCurrency": ".usage_currency",
    "VCard": ".v_card",
    "VCardMessageType": ".v_card_message_type",
    "VCardVcard": ".v_card_vcard",
    "Video": ".video",
    "VideoMessageType": ".video_message_type",
    "VideoVideo": ".video_video",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "Audio",
    "AudioAudio",
    "AudioMessageType",
    "BaseMessageType",
    "ChannelOptionsMessenger",
    "ChannelOptionsMessengerChannel",
    "ChannelOptionsMessengerMessenger",
    "ChannelOptionsMessengerMessengerCategory",
    "ChannelOptionsMms",
    "ChannelOptionsMmsChannel",
    "ChannelOptionsSms",
    "ChannelOptionsSmsChannel",
    "ChannelOptionsViber",
    "ChannelOptionsViberChannel",
    "ChannelOptionsViberViberService",
    "ChannelOptionsViberViberServiceCategory",
    "ChannelOptionsViberVideo",
    "ChannelOptionsViberVideoChannel",
    "ChannelOptionsViberVideoViberService",
    "ChannelOptionsViberVideoViberServiceCategory",
    "ChannelOptionsViberWithButton",
    "ChannelOptionsViberWithButtonChannel",
    "ChannelOptionsViberWithButtonViberService",
    "ChannelOptionsViberWithButtonViberServiceAction",
    "ChannelOptionsViberWithButtonViberServiceCategory",
    "ChannelOptionsWhatsapp",
    "ChannelOptionsWhatsappChannel",
    "Context",
    "ContextWhatsappReferredProduct",
    "Custom",
    "CustomMessageType",
    "ErrorChannel",
    "ErrorChannelParams",
    "ErrorChannelParamsInvalidParametersItem",
    "ErrorClientReference",
    "ErrorInternal",
    "ErrorInvalidJson",
    "ErrorMessageParams",
    "ErrorMessageParamsInvalidParametersItem",
    "ErrorMessageType",
    "ErrorPaymentRequired",
    "ErrorRecipient",
    "ErrorSender",
    "ErrorThrottled",
    "ErrorUnauthorizedInvalidApplication",
    "ErrorUnauthorizedMissingCredentials",
    "File",
    "FileFile",
    "FileMessageType",
    "FromId",
    "FromNumber",
    "Image",
    "ImageImage",
    "ImageMessageType",
    "InboundMessageMms",
    "InboundMessageMmsChannel",
    "InboundMessageSms",
    "InboundMessageSmsChannel",
    "InboundMessageSmsSms",
    "InboundMessengerMessageCommon",
    "InboundMessengerMessageCommonChannel",
    "InboundViberMessageCommon",
    "InboundViberMessageCommonChannel",
    "InboundViberMessageCommonContext",
    "InboundWhatsAppMessageCommon",
    "InboundWhatsAppMessageCommonChannel",
    "Location",
    "LocationLocation",
    "LocationMessageType",
    "MessageStatusBase",
    "MessageStatusBaseError",
    "MessageStatusBaseStatus",
    "MessageStatusBaseUsage",
    "MessageStatusBaseUsageCurrency",
    "MessageStatusMessenger",
    "MessageStatusMessengerChannel",
    "MessageStatusMessengerStatus",
    "MessageStatusMms",
    "MessageStatusMmsChannel",
    "MessageStatusSms",
    "MessageStatusSmsChannel",
    "MessageStatusViber",
    "MessageStatusViberChannel",
    "MessageStatusViberStatus",
    "MessageStatusWhatsApp",
    "MessageStatusWhatsAppChannel",
    "MessageStatusWhatsAppStatus",
    "MessageStatusWhatsAppUsage",
    "MessageStatusWhatsAppUsageCurrency",
    "MessageStatusWhatsAppWhatsapp",
    "MessageStatusWhatsAppWhatsappConversation",
    "MessageStatusWhatsAppWhatsappConversationOrigin",
    "MessageUuid",
    "Order",
    "OrderMessageType",
    "OrderOrder",
    "OrderOrderProductItemsItem",
    "Profile",
    "Reply",
    "ReplyMessageType",
    "ReplyReply",
    "SendMessageRequest",
    "SendMessageRequestFour",
    "SendMessageRequestFourOne",
    "SendMessageRequestFourOneImage",
    "SendMessageRequestFourThree",
    "SendMessageRequestFourThreeFile",
    "SendMessageRequestFourTwo",
    "SendMessageRequestFourTwoVideo",
    "SendMessageRequestFourZero",
    "SendMessageRequestOne",
    "SendMessageRequestOneOne",
    "SendMessageRequestOneOneVcard",
    "SendMessageRequestOneThree",
    "SendMessageRequestOneThreeMessageType",
    "SendMessageRequestOneThreeVideo",
    "SendMessageRequestOneTwo",
    "SendMessageRequestOneTwoAudio",
    "SendMessageRequestOneTwoMessageType",
    "SendMessageRequestOneZero",
    "SendMessageRequestOneZeroImage",
    "SendMessageRequestThree",
    "SendMessageRequestThreeFour",
    "SendMessageRequestThreeFourFile",
    "SendMessageRequestThreeOne",
    "SendMessageRequestThreeOneImage",
    "SendMessageRequestThreeThree",
    "SendMessageRequestThreeThreeVideo",
    "SendMessageRequestThreeTwo",
    "SendMessageRequestThreeTwoAudio",
    "SendMessageRequestThreeZero",
    "SendMessageRequestTwo",
    "SendMessageRequestTwoFive",
    "SendMessageRequestTwoFiveFile",
    "SendMessageRequestTwoFour",
    "SendMessageRequestTwoFourVideo",
    "SendMessageRequestTwoOne",
    "SendMessageRequestTwoSeven",
    "SendMessageRequestTwoSix",
    "SendMessageRequestTwoSixWhatsapp",
    "SendMessageRequestTwoSixWhatsappPolicy",
    "SendMessageRequestTwoThree",
    "SendMessageRequestTwoThreeAudio",
    "SendMessageRequestTwoTwo",
    "SendMessageRequestTwoTwoImage",
    "SendMessageRequestTwoZero",
    "SendMessageRequestZero",
    "SendMessageResponse",
    "SendMessageResponseMessageUuid",
    "SendMessageResponseOne",
    "SendMessageResponseThree",
    "SendMessageResponseTwo",
    "SendMessageResponseZero",
    "Template",
    "TemplateMessageType",
    "TemplateParameters",
    "TemplateTemplate",
    "Text",
    "TextMessageType",
    "Timestamp",
    "ToId",
    "ToNumber",
    "UnauthorizedErrorBody",
    "UnauthorizedErrorBody_HttpsDeveloperNexmoComApiErrorsUnathorized",
    "UnauthorizedErrorBody_HttpsDeveloperNexmoComApiErrorsUnprovisioned",
    "UnprocessableEntityErrorBody",
    "UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsInvalidJson",
    "UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1060",
    "UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus110",
    "UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1100",
    "UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1110",
    "UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1120",
    "UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1140",
    "UnprocessableEntityErrorBody_HttpsDeveloperNexmoComApiErrorsMessagesOlympus1150",
    "Unsupported",
    "UnsupportedMessageType",
    "Usage",
    "UsageCurrency",
    "VCard",
    "VCardMessageType",
    "VCardVcard",
    "Video",
    "VideoMessageType",
    "VideoVideo",
]
