



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_big_blue_button_video_call_response import CreateBigBlueButtonVideoCallResponse
    from .create_channel_folder_response import CreateChannelFolderResponse
    from .create_channel_response import CreateChannelResponse
    from .create_constructor_groups_video_call_response import CreateConstructorGroupsVideoCallResponse
    from .create_nextcloud_talk_video_call_response import CreateNextcloudTalkVideoCallResponse
    from .create_webex_video_call_response import CreateWebexVideoCallResponse
    from .delete_topic_response import DeleteTopicResponse
    from .get_channel_folders_response import GetChannelFoldersResponse
    from .get_stream_by_id_response import GetStreamByIdResponse
    from .get_stream_email_address_response import GetStreamEmailAddressResponse
    from .get_stream_id_response import GetStreamIdResponse
    from .get_stream_topics_response import GetStreamTopicsResponse
    from .get_stream_topics_response_topics_item import GetStreamTopicsResponseTopicsItem
    from .get_streams_response import GetStreamsResponse
    from .get_streams_response_streams_item import GetStreamsResponseStreamsItem
    from .get_subscribers_response import GetSubscribersResponse
    from .get_subscription_status_response import GetSubscriptionStatusResponse
    from .get_subscriptions_request_include_subscribers import GetSubscriptionsRequestIncludeSubscribers
    from .get_subscriptions_response import GetSubscriptionsResponse
    from .get_user_channels_response import GetUserChannelsResponse
    from .mute_topic_request_op import MuteTopicRequestOp
    from .subscribe_request_subscriptions_item import SubscribeRequestSubscriptionsItem
    from .subscribe_response import SubscribeResponse
    from .unsubscribe_response import UnsubscribeResponse
    from .update_stream_request_can_add_subscribers_group import UpdateStreamRequestCanAddSubscribersGroup
    from .update_stream_request_can_add_subscribers_group_new import UpdateStreamRequestCanAddSubscribersGroupNew
    from .update_stream_request_can_add_subscribers_group_new_direct_members import (
        UpdateStreamRequestCanAddSubscribersGroupNewDirectMembers,
    )
    from .update_stream_request_can_add_subscribers_group_old import UpdateStreamRequestCanAddSubscribersGroupOld
    from .update_stream_request_can_add_subscribers_group_old_direct_members import (
        UpdateStreamRequestCanAddSubscribersGroupOldDirectMembers,
    )
    from .update_stream_request_can_administer_channel_group import UpdateStreamRequestCanAdministerChannelGroup
    from .update_stream_request_can_administer_channel_group_new import UpdateStreamRequestCanAdministerChannelGroupNew
    from .update_stream_request_can_administer_channel_group_new_direct_members import (
        UpdateStreamRequestCanAdministerChannelGroupNewDirectMembers,
    )
    from .update_stream_request_can_administer_channel_group_old import UpdateStreamRequestCanAdministerChannelGroupOld
    from .update_stream_request_can_administer_channel_group_old_direct_members import (
        UpdateStreamRequestCanAdministerChannelGroupOldDirectMembers,
    )
    from .update_stream_request_can_create_topic_group import UpdateStreamRequestCanCreateTopicGroup
    from .update_stream_request_can_create_topic_group_new import UpdateStreamRequestCanCreateTopicGroupNew
    from .update_stream_request_can_create_topic_group_new_direct_members import (
        UpdateStreamRequestCanCreateTopicGroupNewDirectMembers,
    )
    from .update_stream_request_can_create_topic_group_old import UpdateStreamRequestCanCreateTopicGroupOld
    from .update_stream_request_can_create_topic_group_old_direct_members import (
        UpdateStreamRequestCanCreateTopicGroupOldDirectMembers,
    )
    from .update_stream_request_can_delete_any_message_group import UpdateStreamRequestCanDeleteAnyMessageGroup
    from .update_stream_request_can_delete_any_message_group_new import UpdateStreamRequestCanDeleteAnyMessageGroupNew
    from .update_stream_request_can_delete_any_message_group_new_direct_members import (
        UpdateStreamRequestCanDeleteAnyMessageGroupNewDirectMembers,
    )
    from .update_stream_request_can_delete_any_message_group_old import UpdateStreamRequestCanDeleteAnyMessageGroupOld
    from .update_stream_request_can_delete_any_message_group_old_direct_members import (
        UpdateStreamRequestCanDeleteAnyMessageGroupOldDirectMembers,
    )
    from .update_stream_request_can_delete_own_message_group import UpdateStreamRequestCanDeleteOwnMessageGroup
    from .update_stream_request_can_delete_own_message_group_new import UpdateStreamRequestCanDeleteOwnMessageGroupNew
    from .update_stream_request_can_delete_own_message_group_new_direct_members import (
        UpdateStreamRequestCanDeleteOwnMessageGroupNewDirectMembers,
    )
    from .update_stream_request_can_delete_own_message_group_old import UpdateStreamRequestCanDeleteOwnMessageGroupOld
    from .update_stream_request_can_delete_own_message_group_old_direct_members import (
        UpdateStreamRequestCanDeleteOwnMessageGroupOldDirectMembers,
    )
    from .update_stream_request_can_move_messages_out_of_channel_group import (
        UpdateStreamRequestCanMoveMessagesOutOfChannelGroup,
    )
    from .update_stream_request_can_move_messages_out_of_channel_group_new import (
        UpdateStreamRequestCanMoveMessagesOutOfChannelGroupNew,
    )
    from .update_stream_request_can_move_messages_out_of_channel_group_new_direct_members import (
        UpdateStreamRequestCanMoveMessagesOutOfChannelGroupNewDirectMembers,
    )
    from .update_stream_request_can_move_messages_out_of_channel_group_old import (
        UpdateStreamRequestCanMoveMessagesOutOfChannelGroupOld,
    )
    from .update_stream_request_can_move_messages_out_of_channel_group_old_direct_members import (
        UpdateStreamRequestCanMoveMessagesOutOfChannelGroupOldDirectMembers,
    )
    from .update_stream_request_can_move_messages_within_channel_group import (
        UpdateStreamRequestCanMoveMessagesWithinChannelGroup,
    )
    from .update_stream_request_can_move_messages_within_channel_group_new import (
        UpdateStreamRequestCanMoveMessagesWithinChannelGroupNew,
    )
    from .update_stream_request_can_move_messages_within_channel_group_new_direct_members import (
        UpdateStreamRequestCanMoveMessagesWithinChannelGroupNewDirectMembers,
    )
    from .update_stream_request_can_move_messages_within_channel_group_old import (
        UpdateStreamRequestCanMoveMessagesWithinChannelGroupOld,
    )
    from .update_stream_request_can_move_messages_within_channel_group_old_direct_members import (
        UpdateStreamRequestCanMoveMessagesWithinChannelGroupOldDirectMembers,
    )
    from .update_stream_request_can_remove_subscribers_group import UpdateStreamRequestCanRemoveSubscribersGroup
    from .update_stream_request_can_remove_subscribers_group_new import UpdateStreamRequestCanRemoveSubscribersGroupNew
    from .update_stream_request_can_remove_subscribers_group_new_direct_members import (
        UpdateStreamRequestCanRemoveSubscribersGroupNewDirectMembers,
    )
    from .update_stream_request_can_remove_subscribers_group_old import UpdateStreamRequestCanRemoveSubscribersGroupOld
    from .update_stream_request_can_remove_subscribers_group_old_direct_members import (
        UpdateStreamRequestCanRemoveSubscribersGroupOldDirectMembers,
    )
    from .update_stream_request_can_resolve_topics_group import UpdateStreamRequestCanResolveTopicsGroup
    from .update_stream_request_can_resolve_topics_group_new import UpdateStreamRequestCanResolveTopicsGroupNew
    from .update_stream_request_can_resolve_topics_group_new_direct_members import (
        UpdateStreamRequestCanResolveTopicsGroupNewDirectMembers,
    )
    from .update_stream_request_can_resolve_topics_group_old import UpdateStreamRequestCanResolveTopicsGroupOld
    from .update_stream_request_can_resolve_topics_group_old_direct_members import (
        UpdateStreamRequestCanResolveTopicsGroupOldDirectMembers,
    )
    from .update_stream_request_can_send_message_group import UpdateStreamRequestCanSendMessageGroup
    from .update_stream_request_can_send_message_group_new import UpdateStreamRequestCanSendMessageGroupNew
    from .update_stream_request_can_send_message_group_new_direct_members import (
        UpdateStreamRequestCanSendMessageGroupNewDirectMembers,
    )
    from .update_stream_request_can_send_message_group_old import UpdateStreamRequestCanSendMessageGroupOld
    from .update_stream_request_can_send_message_group_old_direct_members import (
        UpdateStreamRequestCanSendMessageGroupOldDirectMembers,
    )
    from .update_stream_request_can_subscribe_group import UpdateStreamRequestCanSubscribeGroup
    from .update_stream_request_can_subscribe_group_new import UpdateStreamRequestCanSubscribeGroupNew
    from .update_stream_request_can_subscribe_group_new_direct_members import (
        UpdateStreamRequestCanSubscribeGroupNewDirectMembers,
    )
    from .update_stream_request_can_subscribe_group_old import UpdateStreamRequestCanSubscribeGroupOld
    from .update_stream_request_can_subscribe_group_old_direct_members import (
        UpdateStreamRequestCanSubscribeGroupOldDirectMembers,
    )
    from .update_subscription_settings_request_subscription_data_item import (
        UpdateSubscriptionSettingsRequestSubscriptionDataItem,
    )
    from .update_subscriptions_request_add_item import UpdateSubscriptionsRequestAddItem
    from .update_subscriptions_response import UpdateSubscriptionsResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateBigBlueButtonVideoCallResponse": ".create_big_blue_button_video_call_response",
    "CreateChannelFolderResponse": ".create_channel_folder_response",
    "CreateChannelResponse": ".create_channel_response",
    "CreateConstructorGroupsVideoCallResponse": ".create_constructor_groups_video_call_response",
    "CreateNextcloudTalkVideoCallResponse": ".create_nextcloud_talk_video_call_response",
    "CreateWebexVideoCallResponse": ".create_webex_video_call_response",
    "DeleteTopicResponse": ".delete_topic_response",
    "GetChannelFoldersResponse": ".get_channel_folders_response",
    "GetStreamByIdResponse": ".get_stream_by_id_response",
    "GetStreamEmailAddressResponse": ".get_stream_email_address_response",
    "GetStreamIdResponse": ".get_stream_id_response",
    "GetStreamTopicsResponse": ".get_stream_topics_response",
    "GetStreamTopicsResponseTopicsItem": ".get_stream_topics_response_topics_item",
    "GetStreamsResponse": ".get_streams_response",
    "GetStreamsResponseStreamsItem": ".get_streams_response_streams_item",
    "GetSubscribersResponse": ".get_subscribers_response",
    "GetSubscriptionStatusResponse": ".get_subscription_status_response",
    "GetSubscriptionsRequestIncludeSubscribers": ".get_subscriptions_request_include_subscribers",
    "GetSubscriptionsResponse": ".get_subscriptions_response",
    "GetUserChannelsResponse": ".get_user_channels_response",
    "MuteTopicRequestOp": ".mute_topic_request_op",
    "SubscribeRequestSubscriptionsItem": ".subscribe_request_subscriptions_item",
    "SubscribeResponse": ".subscribe_response",
    "UnsubscribeResponse": ".unsubscribe_response",
    "UpdateStreamRequestCanAddSubscribersGroup": ".update_stream_request_can_add_subscribers_group",
    "UpdateStreamRequestCanAddSubscribersGroupNew": ".update_stream_request_can_add_subscribers_group_new",
    "UpdateStreamRequestCanAddSubscribersGroupNewDirectMembers": ".update_stream_request_can_add_subscribers_group_new_direct_members",
    "UpdateStreamRequestCanAddSubscribersGroupOld": ".update_stream_request_can_add_subscribers_group_old",
    "UpdateStreamRequestCanAddSubscribersGroupOldDirectMembers": ".update_stream_request_can_add_subscribers_group_old_direct_members",
    "UpdateStreamRequestCanAdministerChannelGroup": ".update_stream_request_can_administer_channel_group",
    "UpdateStreamRequestCanAdministerChannelGroupNew": ".update_stream_request_can_administer_channel_group_new",
    "UpdateStreamRequestCanAdministerChannelGroupNewDirectMembers": ".update_stream_request_can_administer_channel_group_new_direct_members",
    "UpdateStreamRequestCanAdministerChannelGroupOld": ".update_stream_request_can_administer_channel_group_old",
    "UpdateStreamRequestCanAdministerChannelGroupOldDirectMembers": ".update_stream_request_can_administer_channel_group_old_direct_members",
    "UpdateStreamRequestCanCreateTopicGroup": ".update_stream_request_can_create_topic_group",
    "UpdateStreamRequestCanCreateTopicGroupNew": ".update_stream_request_can_create_topic_group_new",
    "UpdateStreamRequestCanCreateTopicGroupNewDirectMembers": ".update_stream_request_can_create_topic_group_new_direct_members",
    "UpdateStreamRequestCanCreateTopicGroupOld": ".update_stream_request_can_create_topic_group_old",
    "UpdateStreamRequestCanCreateTopicGroupOldDirectMembers": ".update_stream_request_can_create_topic_group_old_direct_members",
    "UpdateStreamRequestCanDeleteAnyMessageGroup": ".update_stream_request_can_delete_any_message_group",
    "UpdateStreamRequestCanDeleteAnyMessageGroupNew": ".update_stream_request_can_delete_any_message_group_new",
    "UpdateStreamRequestCanDeleteAnyMessageGroupNewDirectMembers": ".update_stream_request_can_delete_any_message_group_new_direct_members",
    "UpdateStreamRequestCanDeleteAnyMessageGroupOld": ".update_stream_request_can_delete_any_message_group_old",
    "UpdateStreamRequestCanDeleteAnyMessageGroupOldDirectMembers": ".update_stream_request_can_delete_any_message_group_old_direct_members",
    "UpdateStreamRequestCanDeleteOwnMessageGroup": ".update_stream_request_can_delete_own_message_group",
    "UpdateStreamRequestCanDeleteOwnMessageGroupNew": ".update_stream_request_can_delete_own_message_group_new",
    "UpdateStreamRequestCanDeleteOwnMessageGroupNewDirectMembers": ".update_stream_request_can_delete_own_message_group_new_direct_members",
    "UpdateStreamRequestCanDeleteOwnMessageGroupOld": ".update_stream_request_can_delete_own_message_group_old",
    "UpdateStreamRequestCanDeleteOwnMessageGroupOldDirectMembers": ".update_stream_request_can_delete_own_message_group_old_direct_members",
    "UpdateStreamRequestCanMoveMessagesOutOfChannelGroup": ".update_stream_request_can_move_messages_out_of_channel_group",
    "UpdateStreamRequestCanMoveMessagesOutOfChannelGroupNew": ".update_stream_request_can_move_messages_out_of_channel_group_new",
    "UpdateStreamRequestCanMoveMessagesOutOfChannelGroupNewDirectMembers": ".update_stream_request_can_move_messages_out_of_channel_group_new_direct_members",
    "UpdateStreamRequestCanMoveMessagesOutOfChannelGroupOld": ".update_stream_request_can_move_messages_out_of_channel_group_old",
    "UpdateStreamRequestCanMoveMessagesOutOfChannelGroupOldDirectMembers": ".update_stream_request_can_move_messages_out_of_channel_group_old_direct_members",
    "UpdateStreamRequestCanMoveMessagesWithinChannelGroup": ".update_stream_request_can_move_messages_within_channel_group",
    "UpdateStreamRequestCanMoveMessagesWithinChannelGroupNew": ".update_stream_request_can_move_messages_within_channel_group_new",
    "UpdateStreamRequestCanMoveMessagesWithinChannelGroupNewDirectMembers": ".update_stream_request_can_move_messages_within_channel_group_new_direct_members",
    "UpdateStreamRequestCanMoveMessagesWithinChannelGroupOld": ".update_stream_request_can_move_messages_within_channel_group_old",
    "UpdateStreamRequestCanMoveMessagesWithinChannelGroupOldDirectMembers": ".update_stream_request_can_move_messages_within_channel_group_old_direct_members",
    "UpdateStreamRequestCanRemoveSubscribersGroup": ".update_stream_request_can_remove_subscribers_group",
    "UpdateStreamRequestCanRemoveSubscribersGroupNew": ".update_stream_request_can_remove_subscribers_group_new",
    "UpdateStreamRequestCanRemoveSubscribersGroupNewDirectMembers": ".update_stream_request_can_remove_subscribers_group_new_direct_members",
    "UpdateStreamRequestCanRemoveSubscribersGroupOld": ".update_stream_request_can_remove_subscribers_group_old",
    "UpdateStreamRequestCanRemoveSubscribersGroupOldDirectMembers": ".update_stream_request_can_remove_subscribers_group_old_direct_members",
    "UpdateStreamRequestCanResolveTopicsGroup": ".update_stream_request_can_resolve_topics_group",
    "UpdateStreamRequestCanResolveTopicsGroupNew": ".update_stream_request_can_resolve_topics_group_new",
    "UpdateStreamRequestCanResolveTopicsGroupNewDirectMembers": ".update_stream_request_can_resolve_topics_group_new_direct_members",
    "UpdateStreamRequestCanResolveTopicsGroupOld": ".update_stream_request_can_resolve_topics_group_old",
    "UpdateStreamRequestCanResolveTopicsGroupOldDirectMembers": ".update_stream_request_can_resolve_topics_group_old_direct_members",
    "UpdateStreamRequestCanSendMessageGroup": ".update_stream_request_can_send_message_group",
    "UpdateStreamRequestCanSendMessageGroupNew": ".update_stream_request_can_send_message_group_new",
    "UpdateStreamRequestCanSendMessageGroupNewDirectMembers": ".update_stream_request_can_send_message_group_new_direct_members",
    "UpdateStreamRequestCanSendMessageGroupOld": ".update_stream_request_can_send_message_group_old",
    "UpdateStreamRequestCanSendMessageGroupOldDirectMembers": ".update_stream_request_can_send_message_group_old_direct_members",
    "UpdateStreamRequestCanSubscribeGroup": ".update_stream_request_can_subscribe_group",
    "UpdateStreamRequestCanSubscribeGroupNew": ".update_stream_request_can_subscribe_group_new",
    "UpdateStreamRequestCanSubscribeGroupNewDirectMembers": ".update_stream_request_can_subscribe_group_new_direct_members",
    "UpdateStreamRequestCanSubscribeGroupOld": ".update_stream_request_can_subscribe_group_old",
    "UpdateStreamRequestCanSubscribeGroupOldDirectMembers": ".update_stream_request_can_subscribe_group_old_direct_members",
    "UpdateSubscriptionSettingsRequestSubscriptionDataItem": ".update_subscription_settings_request_subscription_data_item",
    "UpdateSubscriptionsRequestAddItem": ".update_subscriptions_request_add_item",
    "UpdateSubscriptionsResponse": ".update_subscriptions_response",
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
    "CreateBigBlueButtonVideoCallResponse",
    "CreateChannelFolderResponse",
    "CreateChannelResponse",
    "CreateConstructorGroupsVideoCallResponse",
    "CreateNextcloudTalkVideoCallResponse",
    "CreateWebexVideoCallResponse",
    "DeleteTopicResponse",
    "GetChannelFoldersResponse",
    "GetStreamByIdResponse",
    "GetStreamEmailAddressResponse",
    "GetStreamIdResponse",
    "GetStreamTopicsResponse",
    "GetStreamTopicsResponseTopicsItem",
    "GetStreamsResponse",
    "GetStreamsResponseStreamsItem",
    "GetSubscribersResponse",
    "GetSubscriptionStatusResponse",
    "GetSubscriptionsRequestIncludeSubscribers",
    "GetSubscriptionsResponse",
    "GetUserChannelsResponse",
    "MuteTopicRequestOp",
    "SubscribeRequestSubscriptionsItem",
    "SubscribeResponse",
    "UnsubscribeResponse",
    "UpdateStreamRequestCanAddSubscribersGroup",
    "UpdateStreamRequestCanAddSubscribersGroupNew",
    "UpdateStreamRequestCanAddSubscribersGroupNewDirectMembers",
    "UpdateStreamRequestCanAddSubscribersGroupOld",
    "UpdateStreamRequestCanAddSubscribersGroupOldDirectMembers",
    "UpdateStreamRequestCanAdministerChannelGroup",
    "UpdateStreamRequestCanAdministerChannelGroupNew",
    "UpdateStreamRequestCanAdministerChannelGroupNewDirectMembers",
    "UpdateStreamRequestCanAdministerChannelGroupOld",
    "UpdateStreamRequestCanAdministerChannelGroupOldDirectMembers",
    "UpdateStreamRequestCanCreateTopicGroup",
    "UpdateStreamRequestCanCreateTopicGroupNew",
    "UpdateStreamRequestCanCreateTopicGroupNewDirectMembers",
    "UpdateStreamRequestCanCreateTopicGroupOld",
    "UpdateStreamRequestCanCreateTopicGroupOldDirectMembers",
    "UpdateStreamRequestCanDeleteAnyMessageGroup",
    "UpdateStreamRequestCanDeleteAnyMessageGroupNew",
    "UpdateStreamRequestCanDeleteAnyMessageGroupNewDirectMembers",
    "UpdateStreamRequestCanDeleteAnyMessageGroupOld",
    "UpdateStreamRequestCanDeleteAnyMessageGroupOldDirectMembers",
    "UpdateStreamRequestCanDeleteOwnMessageGroup",
    "UpdateStreamRequestCanDeleteOwnMessageGroupNew",
    "UpdateStreamRequestCanDeleteOwnMessageGroupNewDirectMembers",
    "UpdateStreamRequestCanDeleteOwnMessageGroupOld",
    "UpdateStreamRequestCanDeleteOwnMessageGroupOldDirectMembers",
    "UpdateStreamRequestCanMoveMessagesOutOfChannelGroup",
    "UpdateStreamRequestCanMoveMessagesOutOfChannelGroupNew",
    "UpdateStreamRequestCanMoveMessagesOutOfChannelGroupNewDirectMembers",
    "UpdateStreamRequestCanMoveMessagesOutOfChannelGroupOld",
    "UpdateStreamRequestCanMoveMessagesOutOfChannelGroupOldDirectMembers",
    "UpdateStreamRequestCanMoveMessagesWithinChannelGroup",
    "UpdateStreamRequestCanMoveMessagesWithinChannelGroupNew",
    "UpdateStreamRequestCanMoveMessagesWithinChannelGroupNewDirectMembers",
    "UpdateStreamRequestCanMoveMessagesWithinChannelGroupOld",
    "UpdateStreamRequestCanMoveMessagesWithinChannelGroupOldDirectMembers",
    "UpdateStreamRequestCanRemoveSubscribersGroup",
    "UpdateStreamRequestCanRemoveSubscribersGroupNew",
    "UpdateStreamRequestCanRemoveSubscribersGroupNewDirectMembers",
    "UpdateStreamRequestCanRemoveSubscribersGroupOld",
    "UpdateStreamRequestCanRemoveSubscribersGroupOldDirectMembers",
    "UpdateStreamRequestCanResolveTopicsGroup",
    "UpdateStreamRequestCanResolveTopicsGroupNew",
    "UpdateStreamRequestCanResolveTopicsGroupNewDirectMembers",
    "UpdateStreamRequestCanResolveTopicsGroupOld",
    "UpdateStreamRequestCanResolveTopicsGroupOldDirectMembers",
    "UpdateStreamRequestCanSendMessageGroup",
    "UpdateStreamRequestCanSendMessageGroupNew",
    "UpdateStreamRequestCanSendMessageGroupNewDirectMembers",
    "UpdateStreamRequestCanSendMessageGroupOld",
    "UpdateStreamRequestCanSendMessageGroupOldDirectMembers",
    "UpdateStreamRequestCanSubscribeGroup",
    "UpdateStreamRequestCanSubscribeGroupNew",
    "UpdateStreamRequestCanSubscribeGroupNewDirectMembers",
    "UpdateStreamRequestCanSubscribeGroupOld",
    "UpdateStreamRequestCanSubscribeGroupOldDirectMembers",
    "UpdateSubscriptionSettingsRequestSubscriptionDataItem",
    "UpdateSubscriptionsRequestAddItem",
    "UpdateSubscriptionsResponse",
]
