



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .action import Action
    from .channel import Channel
    from .channel_from import (
        ChannelFrom,
        ChannelFrom_App,
        ChannelFrom_Phone,
        ChannelFrom_Sip,
        ChannelFrom_Vbc,
        ChannelFrom_Websocket,
    )
    from .channel_from_app import ChannelFromApp
    from .channel_from_phone import ChannelFromPhone
    from .channel_from_sip import ChannelFromSip
    from .channel_from_vbc import ChannelFromVbc
    from .channel_from_websocket import ChannelFromWebsocket
    from .channel_from_websocket_content_type import ChannelFromWebsocketContentType
    from .channel_from_websocket_headers import ChannelFromWebsocketHeaders
    from .channel_leg_ids_item import ChannelLegIdsItem
    from .channel_number import ChannelNumber
    from .channel_to import ChannelTo, ChannelTo_App, ChannelTo_Phone, ChannelTo_Sip, ChannelTo_Vbc, ChannelTo_Websocket
    from .channel_to_phone import ChannelToPhone
    from .channel_type import ChannelType
    from .components_schemas_channel_properties_from_one_of0 import ComponentsSchemasChannelPropertiesFromOneOf0
    from .components_schemas_channel_properties_from_one_of2 import ComponentsSchemasChannelPropertiesFromOneOf2
    from .components_schemas_channel_properties_from_one_of3 import ComponentsSchemasChannelPropertiesFromOneOf3
    from .components_schemas_channel_properties_from_one_of3content_type import (
        ComponentsSchemasChannelPropertiesFromOneOf3ContentType,
    )
    from .components_schemas_channel_properties_from_one_of3headers import (
        ComponentsSchemasChannelPropertiesFromOneOf3Headers,
    )
    from .components_schemas_channel_properties_from_one_of4 import ComponentsSchemasChannelPropertiesFromOneOf4
    from .conversation_id import ConversationId
    from .conversation_properties import ConversationProperties
    from .display_name import DisplayName
    from .display_name_user import DisplayNameUser
    from .event_body import EventBody
    from .event_id import EventId
    from .event_method import EventMethod
    from .event_retrieved import EventRetrieved
    from .event_type import EventType
    from .event_url import EventUrl
    from .format import Format
    from .href import Href
    from .href_conversation import HrefConversation
    from .href_conversations_list import HrefConversationsList
    from .href_event import HrefEvent
    from .href_member import HrefMember
    from .href_rtc import HrefRtc
    from .href_user import HrefUser
    from .image_url import ImageUrl
    from .initiator import Initiator
    from .initiator_joined import InitiatorJoined
    from .knocker_id import KnockerId
    from .leg_id import LegId
    from .leg_state import LegState
    from .links_conversation import LinksConversation
    from .links_conversation_self import LinksConversationSelf
    from .links_conversations_list import LinksConversationsList
    from .links_conversations_list_self import LinksConversationsListSelf
    from .media import Media
    from .member_action import MemberAction
    from .member_id import MemberId
    from .member_id_inviting import MemberIdInviting
    from .member_state import MemberState
    from .name import Name
    from .name_conversation import NameConversation
    from .name_user import NameUser
    from .page_size import PageSize
    from .record_index import RecordIndex
    from .split import Split
    from .timestamp import Timestamp
    from .timestamp_created import TimestampCreated
    from .timestamp_destroyed import TimestampDestroyed
    from .timestamp_leg_end_time import TimestampLegEndTime
    from .timestamp_leg_start_time import TimestampLegStartTime
    from .timestamp_obj_leg import TimestampObjLeg
    from .timestamp_res_conversation import TimestampResConversation
    from .timestamp_res_event import TimestampResEvent
    from .timestamp_res_member import TimestampResMember
    from .timestamp_updated import TimestampUpdated
    from .user_id import UserId
    from .user_id_or_user_name import UserIdOrUserName
_dynamic_imports: typing.Dict[str, str] = {
    "Action": ".action",
    "Channel": ".channel",
    "ChannelFrom": ".channel_from",
    "ChannelFromApp": ".channel_from_app",
    "ChannelFromPhone": ".channel_from_phone",
    "ChannelFromSip": ".channel_from_sip",
    "ChannelFromVbc": ".channel_from_vbc",
    "ChannelFromWebsocket": ".channel_from_websocket",
    "ChannelFromWebsocketContentType": ".channel_from_websocket_content_type",
    "ChannelFromWebsocketHeaders": ".channel_from_websocket_headers",
    "ChannelFrom_App": ".channel_from",
    "ChannelFrom_Phone": ".channel_from",
    "ChannelFrom_Sip": ".channel_from",
    "ChannelFrom_Vbc": ".channel_from",
    "ChannelFrom_Websocket": ".channel_from",
    "ChannelLegIdsItem": ".channel_leg_ids_item",
    "ChannelNumber": ".channel_number",
    "ChannelTo": ".channel_to",
    "ChannelToPhone": ".channel_to_phone",
    "ChannelTo_App": ".channel_to",
    "ChannelTo_Phone": ".channel_to",
    "ChannelTo_Sip": ".channel_to",
    "ChannelTo_Vbc": ".channel_to",
    "ChannelTo_Websocket": ".channel_to",
    "ChannelType": ".channel_type",
    "ComponentsSchemasChannelPropertiesFromOneOf0": ".components_schemas_channel_properties_from_one_of0",
    "ComponentsSchemasChannelPropertiesFromOneOf2": ".components_schemas_channel_properties_from_one_of2",
    "ComponentsSchemasChannelPropertiesFromOneOf3": ".components_schemas_channel_properties_from_one_of3",
    "ComponentsSchemasChannelPropertiesFromOneOf3ContentType": ".components_schemas_channel_properties_from_one_of3content_type",
    "ComponentsSchemasChannelPropertiesFromOneOf3Headers": ".components_schemas_channel_properties_from_one_of3headers",
    "ComponentsSchemasChannelPropertiesFromOneOf4": ".components_schemas_channel_properties_from_one_of4",
    "ConversationId": ".conversation_id",
    "ConversationProperties": ".conversation_properties",
    "DisplayName": ".display_name",
    "DisplayNameUser": ".display_name_user",
    "EventBody": ".event_body",
    "EventId": ".event_id",
    "EventMethod": ".event_method",
    "EventRetrieved": ".event_retrieved",
    "EventType": ".event_type",
    "EventUrl": ".event_url",
    "Format": ".format",
    "Href": ".href",
    "HrefConversation": ".href_conversation",
    "HrefConversationsList": ".href_conversations_list",
    "HrefEvent": ".href_event",
    "HrefMember": ".href_member",
    "HrefRtc": ".href_rtc",
    "HrefUser": ".href_user",
    "ImageUrl": ".image_url",
    "Initiator": ".initiator",
    "InitiatorJoined": ".initiator_joined",
    "KnockerId": ".knocker_id",
    "LegId": ".leg_id",
    "LegState": ".leg_state",
    "LinksConversation": ".links_conversation",
    "LinksConversationSelf": ".links_conversation_self",
    "LinksConversationsList": ".links_conversations_list",
    "LinksConversationsListSelf": ".links_conversations_list_self",
    "Media": ".media",
    "MemberAction": ".member_action",
    "MemberId": ".member_id",
    "MemberIdInviting": ".member_id_inviting",
    "MemberState": ".member_state",
    "Name": ".name",
    "NameConversation": ".name_conversation",
    "NameUser": ".name_user",
    "PageSize": ".page_size",
    "RecordIndex": ".record_index",
    "Split": ".split",
    "Timestamp": ".timestamp",
    "TimestampCreated": ".timestamp_created",
    "TimestampDestroyed": ".timestamp_destroyed",
    "TimestampLegEndTime": ".timestamp_leg_end_time",
    "TimestampLegStartTime": ".timestamp_leg_start_time",
    "TimestampObjLeg": ".timestamp_obj_leg",
    "TimestampResConversation": ".timestamp_res_conversation",
    "TimestampResEvent": ".timestamp_res_event",
    "TimestampResMember": ".timestamp_res_member",
    "TimestampUpdated": ".timestamp_updated",
    "UserId": ".user_id",
    "UserIdOrUserName": ".user_id_or_user_name",
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
    "Action",
    "Channel",
    "ChannelFrom",
    "ChannelFromApp",
    "ChannelFromPhone",
    "ChannelFromSip",
    "ChannelFromVbc",
    "ChannelFromWebsocket",
    "ChannelFromWebsocketContentType",
    "ChannelFromWebsocketHeaders",
    "ChannelFrom_App",
    "ChannelFrom_Phone",
    "ChannelFrom_Sip",
    "ChannelFrom_Vbc",
    "ChannelFrom_Websocket",
    "ChannelLegIdsItem",
    "ChannelNumber",
    "ChannelTo",
    "ChannelToPhone",
    "ChannelTo_App",
    "ChannelTo_Phone",
    "ChannelTo_Sip",
    "ChannelTo_Vbc",
    "ChannelTo_Websocket",
    "ChannelType",
    "ComponentsSchemasChannelPropertiesFromOneOf0",
    "ComponentsSchemasChannelPropertiesFromOneOf2",
    "ComponentsSchemasChannelPropertiesFromOneOf3",
    "ComponentsSchemasChannelPropertiesFromOneOf3ContentType",
    "ComponentsSchemasChannelPropertiesFromOneOf3Headers",
    "ComponentsSchemasChannelPropertiesFromOneOf4",
    "ConversationId",
    "ConversationProperties",
    "DisplayName",
    "DisplayNameUser",
    "EventBody",
    "EventId",
    "EventMethod",
    "EventRetrieved",
    "EventType",
    "EventUrl",
    "Format",
    "Href",
    "HrefConversation",
    "HrefConversationsList",
    "HrefEvent",
    "HrefMember",
    "HrefRtc",
    "HrefUser",
    "ImageUrl",
    "Initiator",
    "InitiatorJoined",
    "KnockerId",
    "LegId",
    "LegState",
    "LinksConversation",
    "LinksConversationSelf",
    "LinksConversationsList",
    "LinksConversationsListSelf",
    "Media",
    "MemberAction",
    "MemberId",
    "MemberIdInviting",
    "MemberState",
    "Name",
    "NameConversation",
    "NameUser",
    "PageSize",
    "RecordIndex",
    "Split",
    "Timestamp",
    "TimestampCreated",
    "TimestampDestroyed",
    "TimestampLegEndTime",
    "TimestampLegStartTime",
    "TimestampObjLeg",
    "TimestampResConversation",
    "TimestampResEvent",
    "TimestampResMember",
    "TimestampUpdated",
    "UserId",
    "UserIdOrUserName",
]
