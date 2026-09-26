

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.can_administer_channel_group import CanAdministerChannelGroup
from ..types.can_create_topic_group import CanCreateTopicGroup
from ..types.can_delete_any_message_group import CanDeleteAnyMessageGroup
from ..types.can_delete_own_message_group import CanDeleteOwnMessageGroup
from ..types.can_move_messages_out_of_channel_group import CanMoveMessagesOutOfChannelGroup
from ..types.can_move_messages_within_channel_group import CanMoveMessagesWithinChannelGroup
from ..types.can_remove_subscribers_group import CanRemoveSubscribersGroup
from ..types.can_resolve_topics_group import CanResolveTopicsGroup
from ..types.can_send_message_group import CanSendMessageGroup
from ..types.can_subscribe_group import CanSubscribeGroup
from ..types.channel_can_add_subscribers_group import ChannelCanAddSubscribersGroup
from ..types.default_push_notifications import DefaultPushNotifications
from ..types.history_public_to_subscribers import HistoryPublicToSubscribers
from ..types.ignored_parameters_success import IgnoredParametersSuccess
from ..types.json_success import JsonSuccess
from ..types.message_retention_days import MessageRetentionDays
from ..types.principals import Principals
from ..types.send_new_subscription_messages import SendNewSubscriptionMessages
from ..types.subscription_property import SubscriptionProperty
from ..types.subscription_property_value import SubscriptionPropertyValue
from ..types.topics_policy import TopicsPolicy
from .raw_client import AsyncRawChannelsClient, RawChannelsClient
from .types.create_big_blue_button_video_call_response import CreateBigBlueButtonVideoCallResponse
from .types.create_channel_folder_response import CreateChannelFolderResponse
from .types.create_channel_response import CreateChannelResponse
from .types.create_constructor_groups_video_call_response import CreateConstructorGroupsVideoCallResponse
from .types.create_nextcloud_talk_video_call_response import CreateNextcloudTalkVideoCallResponse
from .types.create_webex_video_call_response import CreateWebexVideoCallResponse
from .types.delete_topic_response import DeleteTopicResponse
from .types.get_channel_folders_response import GetChannelFoldersResponse
from .types.get_stream_by_id_response import GetStreamByIdResponse
from .types.get_stream_email_address_response import GetStreamEmailAddressResponse
from .types.get_stream_id_response import GetStreamIdResponse
from .types.get_stream_topics_response import GetStreamTopicsResponse
from .types.get_streams_response import GetStreamsResponse
from .types.get_subscribers_response import GetSubscribersResponse
from .types.get_subscription_status_response import GetSubscriptionStatusResponse
from .types.get_subscriptions_request_include_subscribers import GetSubscriptionsRequestIncludeSubscribers
from .types.get_subscriptions_response import GetSubscriptionsResponse
from .types.get_user_channels_response import GetUserChannelsResponse
from .types.mute_topic_request_op import MuteTopicRequestOp
from .types.subscribe_request_subscriptions_item import SubscribeRequestSubscriptionsItem
from .types.subscribe_response import SubscribeResponse
from .types.unsubscribe_response import UnsubscribeResponse
from .types.update_stream_request_can_add_subscribers_group import UpdateStreamRequestCanAddSubscribersGroup
from .types.update_stream_request_can_administer_channel_group import UpdateStreamRequestCanAdministerChannelGroup
from .types.update_stream_request_can_create_topic_group import UpdateStreamRequestCanCreateTopicGroup
from .types.update_stream_request_can_delete_any_message_group import UpdateStreamRequestCanDeleteAnyMessageGroup
from .types.update_stream_request_can_delete_own_message_group import UpdateStreamRequestCanDeleteOwnMessageGroup
from .types.update_stream_request_can_move_messages_out_of_channel_group import (
    UpdateStreamRequestCanMoveMessagesOutOfChannelGroup,
)
from .types.update_stream_request_can_move_messages_within_channel_group import (
    UpdateStreamRequestCanMoveMessagesWithinChannelGroup,
)
from .types.update_stream_request_can_remove_subscribers_group import UpdateStreamRequestCanRemoveSubscribersGroup
from .types.update_stream_request_can_resolve_topics_group import UpdateStreamRequestCanResolveTopicsGroup
from .types.update_stream_request_can_send_message_group import UpdateStreamRequestCanSendMessageGroup
from .types.update_stream_request_can_subscribe_group import UpdateStreamRequestCanSubscribeGroup
from .types.update_subscription_settings_request_subscription_data_item import (
    UpdateSubscriptionSettingsRequestSubscriptionDataItem,
)
from .types.update_subscriptions_request_add_item import UpdateSubscriptionsRequestAddItem
from .types.update_subscriptions_response import UpdateSubscriptionsResponse


OMIT = typing.cast(typing.Any, ...)


class ChannelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChannelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChannelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChannelsClient
        """
        return self._raw_client

    def get_stream_id(
        self, *, stream: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetStreamIdResponse:
        """
        Get the unique ID of a given channel.

        Parameters
        ----------
        stream : str
            The name of the channel to access.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStreamIdResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.get_stream_id(
            stream="Denmark",
        )
        """
        _response = self._raw_client.get_stream_id(stream=stream, request_options=request_options)
        return _response.data

    def add_default_stream(
        self, *, stream_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Add a channel to the set of [default channels][default-channels]
        for new users joining the organization.

        [default-channels]: /help/set-default-channels-for-new-users

        Parameters
        ----------
        stream_id : int
            The ID of the target channel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.add_default_stream(
            stream_id=10,
        )
        """
        _response = self._raw_client.add_default_stream(stream_id=stream_id, request_options=request_options)
        return _response.data

    def remove_default_stream(
        self, *, stream_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Remove a channel from the set of [default channels][default-channels]
        for new users joining the organization.

        [default-channels]: /help/set-default-channels-for-new-users

        Parameters
        ----------
        stream_id : int
            The ID of the target channel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.remove_default_stream(
            stream_id=10,
        )
        """
        _response = self._raw_client.remove_default_stream(stream_id=stream_id, request_options=request_options)
        return _response.data

    def get_stream_topics(
        self,
        stream_id: int,
        *,
        allow_empty_topic_name: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetStreamTopicsResponse:
        """
        Get all topics the user has access to in a specific channel.

        Note that for [private channels with
        protected history](/help/channel-permissions#private-channels),
        the user will only have access to topics of messages sent after they
        [subscribed to](/api/subscribe) the channel. Similarly, a user's
        [bot](/help/bots-overview#bot-type) will only have access to messages
        sent after the bot was subscribed to the channel, instead of when the
        user subscribed.

        **Changes**: Before Zulip 12.0 (feature level 480), this
        endpoint was not supported for archived channels.

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        allow_empty_topic_name : typing.Optional[bool]
            Whether the client supports processing the empty string as
            a topic name in the returned data.

            If `false`, the value of `realm_empty_topic_display_name`
            found in the [`POST /register`](/api/register-queue) response is
            returned replacing the empty string as the topic name.

            **Changes**: New in Zulip 10.0 (feature level 334). Previously,
            the empty string was not a valid topic.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStreamTopicsResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.get_stream_topics(
            stream_id=1,
        )
        """
        _response = self._raw_client.get_stream_topics(
            stream_id, allow_empty_topic_name=allow_empty_topic_name, request_options=request_options
        )
        return _response.data

    def get_subscriptions(
        self,
        *,
        include_subscribers: typing.Optional[GetSubscriptionsRequestIncludeSubscribers] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSubscriptionsResponse:
        """
        Get all channels that the user is subscribed to.

        Parameters
        ----------
        include_subscribers : typing.Optional[GetSubscriptionsRequestIncludeSubscribers]
            Whether each returned channel object should include a `subscribers`
            field containing a list of the user IDs of its subscribers.

            Client apps supporting organizations with many thousands of users
            should not pass `true`, because the full subscriber matrix may be
            several megabytes of data. The `partial` value, combined with the
            `subscriber_count` and fetching subscribers for individual channels as
            needed, is recommended to support client app features where
            channel subscriber data is useful.

            If a client passes `partial` for this parameter, the server may,
            for some channels, return a subset of the channel's subscribers
            in the `partial_subscribers` field instead of the `subscribers` field,
            which always contains the complete set of subscribers.

            The server guarantees that it will always return a `subscribers`
            field for channels with fewer than 250 total subscribers. When
            returning a `partial_subscribers` field, the server guarantees
            that all bot users and users active within the last 14 days will
            be included. For other cases, the server may use its discretion
            to determine which channels and users to include, balancing between
            payload size and usefulness of the data provided to the client.

            **Changes**: The `partial` value is new in Zulip 11.0 (feature level 412).

            New in Zulip 2.1.0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSubscriptionsResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.get_subscriptions()
        """
        _response = self._raw_client.get_subscriptions(
            include_subscribers=include_subscribers, request_options=request_options
        )
        return _response.data

    def subscribe(
        self,
        *,
        subscriptions: typing.Sequence[SubscribeRequestSubscriptionsItem],
        principals: typing.Optional[Principals] = OMIT,
        authorization_errors_fatal: typing.Optional[bool] = OMIT,
        announce: typing.Optional[bool] = OMIT,
        invite_only: typing.Optional[bool] = OMIT,
        is_web_public: typing.Optional[bool] = OMIT,
        is_default_stream: typing.Optional[bool] = OMIT,
        history_public_to_subscribers: typing.Optional[HistoryPublicToSubscribers] = OMIT,
        message_retention_days: typing.Optional[MessageRetentionDays] = OMIT,
        default_push_notifications: typing.Optional[DefaultPushNotifications] = OMIT,
        topics_policy: typing.Optional[TopicsPolicy] = OMIT,
        can_add_subscribers_group: typing.Optional[ChannelCanAddSubscribersGroup] = OMIT,
        can_remove_subscribers_group: typing.Optional[CanRemoveSubscribersGroup] = OMIT,
        can_administer_channel_group: typing.Optional[CanAdministerChannelGroup] = OMIT,
        can_delete_any_message_group: typing.Optional[CanDeleteAnyMessageGroup] = OMIT,
        can_delete_own_message_group: typing.Optional[CanDeleteOwnMessageGroup] = OMIT,
        can_move_messages_out_of_channel_group: typing.Optional[CanMoveMessagesOutOfChannelGroup] = OMIT,
        can_move_messages_within_channel_group: typing.Optional[CanMoveMessagesWithinChannelGroup] = OMIT,
        can_send_message_group: typing.Optional[CanSendMessageGroup] = OMIT,
        can_subscribe_group: typing.Optional[CanSubscribeGroup] = OMIT,
        can_resolve_topics_group: typing.Optional[CanResolveTopicsGroup] = OMIT,
        can_create_topic_group: typing.Optional[CanCreateTopicGroup] = OMIT,
        folder_id: typing.Optional[int] = OMIT,
        send_new_subscription_messages: typing.Optional[SendNewSubscriptionMessages] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscribeResponse:
        """
        Subscribe one or more users to one or more channels.

        If any of the specified channels do not exist, they are automatically
        created. The initial [channel settings](/api/update-stream) will be determined
        by the optional parameters, like `invite_only`, detailed below.

        Note that the ability to subscribe oneself and/or other users
        to a specified channel depends on the [channel's permissions
        settings](/help/channel-permissions).

        **Changes**: Before Zulip 10.0 (feature level 362),
        subscriptions in archived channels could not be modified.

        Before Zulip 10.0 (feature level 357), the
        `can_subscribe_group` permission, which allows members of the
        group to subscribe themselves to the channel, did not exist.

        Before Zulip 10.0 (feature level 349), a user cannot subscribe
        other users to a private channel without being subscribed
        to that channel themselves. Now, If a user is part of
        `can_add_subscribers_group`, they can subscribe themselves or other
        users to a private channel without being subscribed to that channel.

        Removed `stream_post_policy` and `is_announcement_only`
        parameters in Zulip 10.0 (feature level 333), as permission to post
        in the channel is now controlled by `can_send_message_group`.

        Before Zulip 8.0 (feature level 208), if a user specified by the
        [`principals`][principals-param] parameter was a deactivated user,
        or did not exist, then an HTTP status code of 403 was returned with
        `code: "UNAUTHORIZED_PRINCIPAL"` in the error response. As of this
        feature level, an HTTP status code of 400 is returned with
        `code: "BAD_REQUEST"` in the error response for these cases.

        [principals-param]: /api/subscribe#parameter-principals

        Parameters
        ----------
        subscriptions : typing.Sequence[SubscribeRequestSubscriptionsItem]
            A list of dictionaries containing the key `name` and value
            specifying the name of the channel to subscribe. If the channel does not
            exist a new channel is created. The description of the channel created can
            be specified by setting the dictionary key `description` with an
            appropriate value.

        principals : typing.Optional[Principals]

        authorization_errors_fatal : typing.Optional[bool]
            A boolean specifying whether authorization errors (such as when the
            requesting user is not authorized to access a private channel) should be
            considered fatal or not. When `true`, an authorization error is reported
            as such. When set to `false`, the response will be a 200 and any channels
            where the request encountered an authorization error will be listed
            in the `unauthorized` key.

        announce : typing.Optional[bool]
            If one of the channels specified did not exist previously and is thus created
            by this call, this determines whether [notification bot](/help/configure-automated-notices)
            will send an announcement about the new channel's creation.

        invite_only : typing.Optional[bool]
            As described above, this endpoint will create a new channel if passed
            a channel name that doesn't already exist. This parameters and the ones
            that follow are used to request an initial configuration of a created
            channel; they are ignored for channels that already exist.

            This parameter determines whether any newly created channels will be
            private channels.

        is_web_public : typing.Optional[bool]
            This parameter determines whether any newly created channels will be
            web-public channels.

            Note that creating web-public channels requires the
            `WEB_PUBLIC_STREAMS_ENABLED` [server setting][server-settings]
            to be enabled on the Zulip server in question, the organization
            to have enabled the `enable_spectator_access` realm setting, and
            the current use to have permission under the organization's
            `can_create_web_public_channel_group` realm setting.

            [server-settings]: https://zulip.readthedocs.io/en/stable/production/settings.html

            **Changes**: New in Zulip 5.0 (feature level 98).

        is_default_stream : typing.Optional[bool]
            This parameter determines whether any newly created channels will be
            added as [default channels][default-channels] for new users joining
            the organization.

            [default-channels]: /help/set-default-channels-for-new-users

            **Changes**: New in Zulip 8.0 (feature level 200). Previously, default channel status
            could only be changed using the [dedicated API endpoint](/api/add-default-stream).

        history_public_to_subscribers : typing.Optional[HistoryPublicToSubscribers]

        message_retention_days : typing.Optional[MessageRetentionDays]

        default_push_notifications : typing.Optional[DefaultPushNotifications]

        topics_policy : typing.Optional[TopicsPolicy]

        can_add_subscribers_group : typing.Optional[ChannelCanAddSubscribersGroup]

        can_remove_subscribers_group : typing.Optional[CanRemoveSubscribersGroup]

        can_administer_channel_group : typing.Optional[CanAdministerChannelGroup]

        can_delete_any_message_group : typing.Optional[CanDeleteAnyMessageGroup]

        can_delete_own_message_group : typing.Optional[CanDeleteOwnMessageGroup]

        can_move_messages_out_of_channel_group : typing.Optional[CanMoveMessagesOutOfChannelGroup]

        can_move_messages_within_channel_group : typing.Optional[CanMoveMessagesWithinChannelGroup]

        can_send_message_group : typing.Optional[CanSendMessageGroup]

        can_subscribe_group : typing.Optional[CanSubscribeGroup]

        can_resolve_topics_group : typing.Optional[CanResolveTopicsGroup]

        can_create_topic_group : typing.Optional[CanCreateTopicGroup]

        folder_id : typing.Optional[int]
            This parameter adds the newly created channel to the specified
            [channel folder](/help/channel-folders).

            **Changes**: New in Zulip 11.0 (feature level 389).

        send_new_subscription_messages : typing.Optional[SendNewSubscriptionMessages]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscribeResponse
            Success.

        Examples
        --------
        from fern.channels import SubscribeRequestSubscriptionsItem

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.subscribe(
            subscriptions=[
                SubscribeRequestSubscriptionsItem(
                    name="Verona",
                    description="Italian city",
                )
            ],
        )
        """
        _response = self._raw_client.subscribe(
            subscriptions=subscriptions,
            principals=principals,
            authorization_errors_fatal=authorization_errors_fatal,
            announce=announce,
            invite_only=invite_only,
            is_web_public=is_web_public,
            is_default_stream=is_default_stream,
            history_public_to_subscribers=history_public_to_subscribers,
            message_retention_days=message_retention_days,
            default_push_notifications=default_push_notifications,
            topics_policy=topics_policy,
            can_add_subscribers_group=can_add_subscribers_group,
            can_remove_subscribers_group=can_remove_subscribers_group,
            can_administer_channel_group=can_administer_channel_group,
            can_delete_any_message_group=can_delete_any_message_group,
            can_delete_own_message_group=can_delete_own_message_group,
            can_move_messages_out_of_channel_group=can_move_messages_out_of_channel_group,
            can_move_messages_within_channel_group=can_move_messages_within_channel_group,
            can_send_message_group=can_send_message_group,
            can_subscribe_group=can_subscribe_group,
            can_resolve_topics_group=can_resolve_topics_group,
            can_create_topic_group=can_create_topic_group,
            folder_id=folder_id,
            send_new_subscription_messages=send_new_subscription_messages,
            request_options=request_options,
        )
        return _response.data

    def unsubscribe(
        self,
        *,
        subscriptions: typing.Sequence[str],
        principals: typing.Optional[Principals] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UnsubscribeResponse:
        """
        Unsubscribe yourself or other users from one or more channels.

        In addition to managing the current user's subscriptions, this
        endpoint can be used to remove other users from channels. This
        is possible in 3 situations:

        - Organization administrators can remove any user from any
          channel.
        - Users can remove a bot that they own from any channel that
          the user [can access](/help/channel-permissions).
        - Users can unsubscribe any user from a channel if they [have
          access](/help/channel-permissions) to the channel and are a
          member of the [user group](/api/get-user-groups) specified
          by the [`can_remove_subscribers_group`][can-remove-parameter]
          for the channel.

        **Changes**: Before Zulip 10.0 (feature level 362),
        subscriptions in archived channels could not be modified.

        Before Zulip 8.0 (feature level 208), if a user specified by
        the [`principals`][principals-param] parameter was a
        deactivated user, or did not exist, then an HTTP status code
        of 403 was returned with `code: "UNAUTHORIZED_PRINCIPAL"` in
        the error response. As of this feature level, an HTTP status
        code of 400 is returned with `code: "BAD_REQUEST"` in the
        error response for these cases.

        Before Zulip 8.0 (feature level 197),
        the `can_remove_subscribers_group` setting
        was named `can_remove_subscribers_group_id`.

        Before Zulip 7.0 (feature level 161), the
        `can_remove_subscribers_group_id` for all channels was always
        the system group for organization administrators.

        Before Zulip 6.0 (feature level 145), users had no special
        privileges for managing bots that they own.

        [principals-param]: /api/unsubscribe#parameter-principals
        [can-remove-parameter]: /api/subscribe#parameter-can_remove_subscribers_group

        Parameters
        ----------
        subscriptions : typing.Sequence[str]
            A list of channel names to unsubscribe from. This parameter is called
            `streams` in our Python API.

        principals : typing.Optional[Principals]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnsubscribeResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.unsubscribe(
            subscriptions=["Verona", "Denmark"],
        )
        """
        _response = self._raw_client.unsubscribe(
            subscriptions=subscriptions, principals=principals, request_options=request_options
        )
        return _response.data

    def update_subscriptions(
        self,
        *,
        delete: typing.Optional[typing.Sequence[str]] = OMIT,
        add: typing.Optional[typing.Sequence[UpdateSubscriptionsRequestAddItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSubscriptionsResponse:
        """
        Update which channels you are subscribed to.

        **Changes**: Before Zulip 10.0 (feature level 362),
        subscriptions in archived channels could not be modified.

        Parameters
        ----------
        delete : typing.Optional[typing.Sequence[str]]
            A list of channel names to unsubscribe from.

        add : typing.Optional[typing.Sequence[UpdateSubscriptionsRequestAddItem]]
            A list of objects describing which channels to subscribe to, optionally
            including per-user subscription parameters (e.g. color) and if the
            channel is to be created, its description.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSubscriptionsResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.update_subscriptions()
        """
        _response = self._raw_client.update_subscriptions(delete=delete, add=add, request_options=request_options)
        return _response.data

    def mute_topic(
        self,
        *,
        topic: str,
        op: MuteTopicRequestOp,
        stream_id: typing.Optional[int] = OMIT,
        stream: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        [Mute or unmute a topic](/help/mute-a-topic) within a channel that
        the current user is subscribed to.

        **Changes**: Deprecated in Zulip 7.0 (feature level 170). Clients connecting
        to newer servers should use the [POST /user_topics](/api/update-user-topic)
        endpoint, as this endpoint may be removed in a future release.

        Before Zulip 7.0 (feature level 169), this endpoint
        returned an error if asked to mute a topic that was already muted
        or asked to unmute a topic that had not previously been muted.

        Parameters
        ----------
        topic : str
            The topic to (un)mute. Note that the request will succeed regardless of
            whether any messages have been sent to the specified topic.

            Clients should use the `max_topic_length` returned by the
            [`POST /register`](/api/register-queue) endpoint to determine
            the maximum topic length.

        op : MuteTopicRequestOp
            Whether to mute (`add`) or unmute (`remove`) the provided topic.

        stream_id : typing.Optional[int]
            The ID of the channel to access.

            Clients must provide either `stream` or `stream_id` as a parameter
            to this endpoint, but not both.

            **Changes**: New in Zulip 2.0.0.

        stream : typing.Optional[str]
            The name of the channel to access.

            Clients must provide either `stream` or `stream_id` as a parameter
            to this endpoint, but not both. Clients should use `stream_id`
            instead of the `stream` parameter when possible.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern.channels import MuteTopicRequestOp

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.mute_topic(
            topic="dinner",
            op=MuteTopicRequestOp.ADD,
        )
        """
        _response = self._raw_client.mute_topic(
            topic=topic, op=op, stream_id=stream_id, stream=stream, request_options=request_options
        )
        return _response.data

    def update_user_topic(
        self,
        *,
        stream_id: int,
        topic: str,
        visibility_policy: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        This endpoint is used to update the personal preferences for a topic,
        such as the topic's visibility policy, which is used to implement
        [mute a topic](/help/mute-a-topic) and related features.

        This endpoint can be used to update the visibility policy for the single
        channel and topic pair indicated by the parameters for a user.

        **Changes**: New in Zulip 7.0 (feature level 170). Previously,
        toggling whether a topic was muted or unmuted was managed by the
        [PATCH /users/me/subscriptions/muted_topics](/api/mute-topic) endpoint.

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        topic : str
            The topic for which the personal preferences needs to be updated.
            Note that the request will succeed regardless of whether
            any messages have been sent to the specified topic.

            Clients should use the `max_topic_length` returned by the
            [`POST /register`](/api/register-queue) endpoint to determine
            the maximum topic length.

            Note: When the value of `realm_empty_topic_display_name` found in
            the [POST /register](/api/register-queue) response is used for this
            parameter, it is interpreted as an empty string.

            **Changes**: Before Zulip 10.0 (feature level 334), empty string
            was not a valid topic name for channel messages.

        visibility_policy : int
            Controls which visibility policy to set.

            - 0 = None. Removes the visibility policy previously set for the topic.
            - 1 = Muted. [Mutes the topic](/help/mute-a-topic) in a channel.
            - 2 = Unmuted. [Unmutes the topic](/help/mute-a-topic) in a muted channel.
            - 3 = Followed. [Follows the topic](/help/follow-a-topic).

            In an unmuted channel, a topic visibility policy of unmuted will have the
            same effect as the "None" visibility policy.

            **Changes**: In Zulip 7.0 (feature level 219), added followed as
            a visibility policy option.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.update_user_topic(
            stream_id=1,
            topic="dinner",
            visibility_policy=1,
        )
        """
        _response = self._raw_client.update_user_topic(
            stream_id=stream_id, topic=topic, visibility_policy=visibility_policy, request_options=request_options
        )
        return _response.data

    def get_subscription_status(
        self, user_id: int, stream_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSubscriptionStatusResponse:
        """
        Check whether a user is subscribed to a channel.

        **Changes**: Prior to Zulip 12.0 (feature level 458), this endpoint
        did not support querying subscriptions of bot users.

        New in Zulip 3.0 (feature level 12).

        Parameters
        ----------
        user_id : int
            The target user's ID.

        stream_id : int
            The ID of the channel to access.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSubscriptionStatusResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.get_subscription_status(
            user_id=1,
            stream_id=1,
        )
        """
        _response = self._raw_client.get_subscription_status(user_id, stream_id, request_options=request_options)
        return _response.data

    def get_user_channels(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserChannelsResponse:
        """
        Gets the list of channels that the target user is subscribed to.

        The [channel security model](/help/channel-permissions) means only those
        subscribed channels to which the acting user has metadata access are
        returned.

        For organization administrators, this is guaranteed to be all channels
        the target user is subscribed to, since organization administrators
        implicitly have metadata access to all channels.

        **Changes**: Prior to Zulip 12.0 (feature level 458), target users that
        were bots resulted in a permissions error.

        New in Zulip 12.0 (feature level 440).

        Parameters
        ----------
        user_id : int
            The target user's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserChannelsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.get_user_channels(
            user_id=1,
        )
        """
        _response = self._raw_client.get_user_channels(user_id, request_options=request_options)
        return _response.data

    def update_subscription_settings(
        self,
        *,
        subscription_data: typing.Sequence[UpdateSubscriptionSettingsRequestSubscriptionDataItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IgnoredParametersSuccess:
        """
        Update the current user's personal settings for channels they are
        subscribed to. These settings include [color](/help/change-the-color-of-a-channel),
        [muting](/help/mute-a-channel), [pinning](/help/pin-a-channel)
        and [per-channel notification settings](/help/channel-notifications).

        There is a single channel alternative to this bulk endpoint:
        [`POST /users/me/subscriptions/{stream_id}`](/api/update-subscription-property).

        **Changes**: Prior to Zulip 5.0 (feature level 111), the response object
        included the `subscription_data` in the request. The endpoint now returns
        the more ergonomic [`ignored_parameters_unsupported`][ignored-parameters]
        array instead.

        [ignored-parameters]: /api/rest-error-handling#ignored-parameters

        Parameters
        ----------
        subscription_data : typing.Sequence[UpdateSubscriptionSettingsRequestSubscriptionDataItem]
            A list of objects that describe the changes that should be applied in
            each subscription. Each object represents a subscription, and must have
            a `stream_id` key that identifies the channel, as well as the `property`
            being modified and its new `value`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IgnoredParametersSuccess
            Success.

        Examples
        --------
        from fern.channels import UpdateSubscriptionSettingsRequestSubscriptionDataItem

        from fern import FernApi, SubscriptionProperty

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.update_subscription_settings(
            subscription_data=[
                UpdateSubscriptionSettingsRequestSubscriptionDataItem(
                    stream_id=1,
                    property=SubscriptionProperty.PIN_TO_TOP,
                    value=True,
                ),
                UpdateSubscriptionSettingsRequestSubscriptionDataItem(
                    stream_id=3,
                    property=SubscriptionProperty.COLOR,
                    value="#f00f00",
                ),
            ],
        )
        """
        _response = self._raw_client.update_subscription_settings(
            subscription_data=subscription_data, request_options=request_options
        )
        return _response.data

    def update_subscription_property(
        self,
        stream_id: int,
        *,
        property: SubscriptionProperty,
        value: SubscriptionPropertyValue,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Update the current user's personal settings for a specific channel they
        are subscribed to. These settings include [color](/help/change-the-color-of-a-channel),
        [muting](/help/mute-a-channel), [pinning](/help/pin-a-channel)
        and [per-channel notification settings](/help/channel-notifications).

        This is a single channel alternative to the bulk endpoint:
        [`POST /users/me/subscriptions/properties`](/api/update-subscription-settings).

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        property : SubscriptionProperty

        value : SubscriptionPropertyValue

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi, SubscriptionProperty

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.update_subscription_property(
            stream_id=1,
            property=SubscriptionProperty.COLOR,
            value=True,
        )
        """
        _response = self._raw_client.update_subscription_property(
            stream_id, property=property, value=value, request_options=request_options
        )
        return _response.data

    def get_subscribers(
        self, stream_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSubscribersResponse:
        """
        Get all users subscribed to a channel.

        **Changes**: Before Zulip 12.0 (feature level 480), this
        endpoint was not supported for archived channels.

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSubscribersResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.get_subscribers(
            stream_id=1,
        )
        """
        _response = self._raw_client.get_subscribers(stream_id, request_options=request_options)
        return _response.data

    def get_streams(
        self,
        *,
        include_public: typing.Optional[bool] = None,
        include_web_public: typing.Optional[bool] = None,
        include_subscribed: typing.Optional[bool] = None,
        exclude_archived: typing.Optional[bool] = None,
        include_all_active: typing.Optional[bool] = None,
        include_all: typing.Optional[bool] = None,
        include_default: typing.Optional[bool] = None,
        include_owner_subscribed: typing.Optional[bool] = None,
        include_can_access_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetStreamsResponse:
        """
        Get all channels that the user [has access to](/help/channel-permissions).

        Parameters
        ----------
        include_public : typing.Optional[bool]
            Include all public channels.

        include_web_public : typing.Optional[bool]
            Include all web-public channels.

        include_subscribed : typing.Optional[bool]
            Include all channels that the user is subscribed to.

        exclude_archived : typing.Optional[bool]
            Whether to exclude archived streams from the results.

            **Changes**: New in Zulip 10.0 (feature level 315).

        include_all_active : typing.Optional[bool]
            Deprecated parameter to include all channels. The user must
            have administrative privileges to use this parameter.

            **Changes**: Deprecated in Zulip 10.0 (feature level
            356). Clients interacting with newer servers should use
            the equivalent `include_all` parameter, which does not
            incorrectly hint that this parameter, and not
            `exclude_archived`, controls whether archived channels
            appear in the response.

        include_all : typing.Optional[bool]
            Include all channels that the user has metadata access to.

            For organization administrators, this will be all channels
            in the organization, since organization administrators
            implicitly have metadata access to all channels.

            **Changes**: New in Zulip 10.0 (feature level 356). On older
            versions, use `include_all_active`, which this replaces.

        include_default : typing.Optional[bool]
            Include all default channels for the user's realm.

        include_owner_subscribed : typing.Optional[bool]
            If the user is a bot, include all channels that the bot's owner is
            subscribed to.

        include_can_access_content : typing.Optional[bool]
            Include all the channels that the user has content access to.

            **Changes**: New in Zulip 10.0 (feature level 356).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStreamsResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.get_streams()
        """
        _response = self._raw_client.get_streams(
            include_public=include_public,
            include_web_public=include_web_public,
            include_subscribed=include_subscribed,
            exclude_archived=exclude_archived,
            include_all_active=include_all_active,
            include_all=include_all,
            include_default=include_default,
            include_owner_subscribed=include_owner_subscribed,
            include_can_access_content=include_can_access_content,
            request_options=request_options,
        )
        return _response.data

    def get_stream_by_id(
        self, stream_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetStreamByIdResponse:
        """
        Fetch details for the channel with the ID `stream_id`.

        **Changes**: Before Zulip 12.0 (feature level 480), this
        endpoint was not supported for archived channels.

        New in Zulip 6.0 (feature level 132).

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStreamByIdResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.get_stream_by_id(
            stream_id=1,
        )
        """
        _response = self._raw_client.get_stream_by_id(stream_id, request_options=request_options)
        return _response.data

    def archive_stream(self, stream_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> JsonSuccess:
        """
        [Archive the channel](/help/archive-a-channel) with the ID `stream_id`.

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.archive_stream(
            stream_id=1,
        )
        """
        _response = self._raw_client.archive_stream(stream_id, request_options=request_options)
        return _response.data

    def update_stream(
        self,
        stream_id: int,
        *,
        description: typing.Optional[str] = OMIT,
        new_name: typing.Optional[str] = OMIT,
        is_private: typing.Optional[bool] = OMIT,
        is_web_public: typing.Optional[bool] = OMIT,
        history_public_to_subscribers: typing.Optional[bool] = OMIT,
        is_default_stream: typing.Optional[bool] = OMIT,
        message_retention_days: typing.Optional[MessageRetentionDays] = OMIT,
        default_push_notifications: typing.Optional[DefaultPushNotifications] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        folder_id: typing.Optional[int] = OMIT,
        topics_policy: typing.Optional[TopicsPolicy] = OMIT,
        can_add_subscribers_group: typing.Optional[UpdateStreamRequestCanAddSubscribersGroup] = OMIT,
        can_remove_subscribers_group: typing.Optional[UpdateStreamRequestCanRemoveSubscribersGroup] = OMIT,
        can_administer_channel_group: typing.Optional[UpdateStreamRequestCanAdministerChannelGroup] = OMIT,
        can_delete_any_message_group: typing.Optional[UpdateStreamRequestCanDeleteAnyMessageGroup] = OMIT,
        can_delete_own_message_group: typing.Optional[UpdateStreamRequestCanDeleteOwnMessageGroup] = OMIT,
        can_move_messages_out_of_channel_group: typing.Optional[
            UpdateStreamRequestCanMoveMessagesOutOfChannelGroup
        ] = OMIT,
        can_move_messages_within_channel_group: typing.Optional[
            UpdateStreamRequestCanMoveMessagesWithinChannelGroup
        ] = OMIT,
        can_send_message_group: typing.Optional[UpdateStreamRequestCanSendMessageGroup] = OMIT,
        can_subscribe_group: typing.Optional[UpdateStreamRequestCanSubscribeGroup] = OMIT,
        can_resolve_topics_group: typing.Optional[UpdateStreamRequestCanResolveTopicsGroup] = OMIT,
        can_create_topic_group: typing.Optional[UpdateStreamRequestCanCreateTopicGroup] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Configure the channel with the ID `stream_id`. This endpoint supports
        an organization administrator editing any property of a channel,
        including:

        - Channel [name](/help/rename-a-channel) and [description](/help/change-the-channel-description)
        - Channel [permissions](/help/channel-permissions), including
          [privacy](/help/change-the-privacy-of-a-channel) and [who can
          send](/help/channel-posting-policy).

        Note that an organization administrator's ability to change a
        [private channel's permissions](/help/channel-permissions#private-channels)
        depends on them being subscribed to the channel.

        **Changes**: Before Zulip 10.0 (feature level 362), channel privacy could not be
        edited for archived channels.

        Removed `stream_post_policy` and `is_announcement_only`
        parameters in Zulip 10.0 (feature level 333), as permission to post
        in the channel is now controlled by `can_send_message_group`.

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        description : typing.Optional[str]
            The new [description](/help/change-the-channel-description) for
            the channel, in [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format.

            Clients should use the `max_stream_description_length` returned
            by the [`POST /register`](/api/register-queue) endpoint to
            determine the maximum channel description length.

            **Changes**: Removed unnecessary JSON-encoding of this parameter in
            Zulip 4.0 (feature level 64).

        new_name : typing.Optional[str]
            The new name for the channel.

            Clients should use the `max_stream_name_length` returned by the
            [`POST /register`](/api/register-queue) endpoint to determine
            the maximum channel name length.

            **Changes**: Removed unnecessary JSON-encoding of this parameter in
            Zulip 4.0 (feature level 64).

        is_private : typing.Optional[bool]
            Change whether the channel is a private channel.

        is_web_public : typing.Optional[bool]
            Change whether the channel is a web-public channel.

            Note that creating web-public channels requires the
            `WEB_PUBLIC_STREAMS_ENABLED` [server setting][server-settings]
            to be enabled on the Zulip server in question, the organization
            to have enabled the `enable_spectator_access` realm setting, and
            the current use to have permission under the organization's
            `can_create_web_public_channel_group` realm setting.

            [server-settings]: https://zulip.readthedocs.io/en/stable/production/settings.html

            **Changes**: New in Zulip 5.0 (feature level 98).

        history_public_to_subscribers : typing.Optional[bool]
            Whether the channel's message history should be available to
            newly subscribed members, or users can only access messages
            they actually received while subscribed to the channel.

            Corresponds to the shared history option for
            [private channels](/help/channel-permissions#private-channels).

            It's an error for this parameter to be false for a public or
            web-public channel and when is_private is false.

            This can only be `false` if `can_create_topic_group` for the channel
            is the `role:everyone` [system group][system-groups].

            **Changes**: Before Zulip 6.0 (feature level 136), `history_public_to_subscribers`
            was silently ignored unless the request also contained either `is_private` or
            `is_web_public`.

            [system-groups]: /api/group-setting-values#system-groups

        is_default_stream : typing.Optional[bool]
            Add or remove the channel as a [default channel][default-channel]
            for new users joining the organization.

            [default-channel]: /help/set-default-channels-for-new-users

            **Changes**: New in Zulip 8.0 (feature level 200). Previously, default channel status
            could only be changed using the [dedicated API endpoint](/api/add-default-stream).

        message_retention_days : typing.Optional[MessageRetentionDays]

        default_push_notifications : typing.Optional[DefaultPushNotifications]

        is_archived : typing.Optional[bool]
            A boolean indicating whether the channel is
            [archived](/help/archive-a-channel) or
            unarchived. Currently only allows unarchiving
            previously archived channels.

            **Changes**: New in Zulip 11.0 (feature level 388).

        folder_id : typing.Optional[int]
            ID of the new [channel folder](/help/channel-folders) to which the
            channel should belong.

            A `null` value indicates the user wants to remove the channel from its
            current channel folder.

            **Changes**: New in Zulip 11.0 (feature level 389).

        topics_policy : typing.Optional[TopicsPolicy]

        can_add_subscribers_group : typing.Optional[UpdateStreamRequestCanAddSubscribersGroup]
            The set of users who have permission to add subscribers to this
            channel expressed as an [update to a group-setting
            value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Users who can administer the channel or have similar realm-level
            permissions can add subscribers to a public channel regardless
            of the value of this setting.

            Users in this group need not be subscribed to a private channel to
            add subscribers to it.

            Note that a user must [have content access](/help/channel-permissions)
            to a channel and permission to administer the channel in order to
            modify this setting.

            **Changes**: New in Zulip 10.0 (feature level 342). Previously, there was no
            channel-level setting for this permission.

        can_remove_subscribers_group : typing.Optional[UpdateStreamRequestCanRemoveSubscribersGroup]
            The set of users who have permission to unsubscribe others from this
            channel expressed as an [update to a group-setting value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Organization administrators can unsubscribe others from a channel as though
            they were in this group without being explicitly listed here.

            Note that a user must have metadata access to a channel and permission
            to administer the channel in order to modify this setting.

            **Changes**: Prior to Zulip 10.0 (feature level 349), channel administrators
            could not unsubscribe other users if they were not an organization
            administrator or part of `can_remove_subscribers_group`. Realm administrators
            were not allowed to unsubscribe other users from a private channel if they
            were not subscribed to that channel.

            Prior to Zulip 10.0 (feature level 320), this value was always the integer
            ID of a system group.

            Before Zulip 8.0 (feature level 197), the `can_remove_subscribers_group`
            setting was named `can_remove_subscribers_group_id`.

            New in Zulip 7.0 (feature level 161).

        can_administer_channel_group : typing.Optional[UpdateStreamRequestCanAdministerChannelGroup]
            The set of users who have permission to administer this channel
            expressed as an [update to a group-setting value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Organization administrators can administer every channel as though they were
            in this group without being explicitly listed here.

            Note that a user must [have content access](/help/channel-permissions) to a
            channel in order to add other subscribers to the channel.

            **Changes**: Prior to Zulip 10.0 (feature level 349) a user needed to
            [have content access](/help/channel-permissions) to a channel in order
            to modify it. The exception to this rule was that organization
            administrators can edit channel names and descriptions without having
            full access to the channel.

            New in Zulip 10.0 (feature level 325). Prior to this
            change, the permission to administer channels was limited to realm
            administrators.

        can_delete_any_message_group : typing.Optional[UpdateStreamRequestCanDeleteAnyMessageGroup]
            The set of users who have permission to delete any message in the channel
            expressed as an [update to a group-setting value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Note that a user must [have content access](/help/channel-permissions) to a
            channel in order to delete any message in the channel.

            Users present in the organization-level `can_delete_any_message_group` setting
            can always delete any message in the channel if they
            [have content access](/help/channel-permissions) to that channel.

            **Changes**: New in Zulip 11.0 (feature level 407). Prior to this
            change, only the users in `can_delete_any_message_group` were able
            delete any message in the organization.

        can_delete_own_message_group : typing.Optional[UpdateStreamRequestCanDeleteOwnMessageGroup]
            The set of users who have permission to delete the messages that they have
            sent in the channel expressed as an [update to a group-setting value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Note that a user must [have content access](/help/channel-permissions) to a
            channel in order to delete their own message in the channel.

            Users with permission to delete any message in the channel
            and users present in the organization-level `can_delete_own_message_group` setting
            can always delete their own messages in the channel if they
            [have content access](/help/channel-permissions) to that channel.

            **Changes**: New in Zulip 11.0 (feature level 407). Prior to this
            change, only the users in the organization-level `can_delete_any_message_group`
            and `can_delete_own_message_group` settings were able delete their own messages in
            the organization.

        can_move_messages_out_of_channel_group : typing.Optional[UpdateStreamRequestCanMoveMessagesOutOfChannelGroup]
            The set of users who have permission to move messages out of this channel
            expressed as an [update to a group-setting value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Note that a user must [have content access](/help/channel-permissions) to a
            channel in order to move messages out of the channel.

            Channel administrators and users present in the organization-level
            `can_move_messages_between_channels_group` setting can always move messages
            out of the channel if they [have content access](/help/channel-permissions) to
            the channel.

            **Changes**: New in Zulip 11.0 (feature level 396). Prior to this
            change, only the users in `can_move_messages_between_channels_group` were able
            move messages between channels.

        can_move_messages_within_channel_group : typing.Optional[UpdateStreamRequestCanMoveMessagesWithinChannelGroup]
            The set of users who have permission to move messages within this channel
            expressed as an [update to a group-setting value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Note that a user must [have content access](/help/channel-permissions) to a
            channel in order to move messages within the channel.

            Channel administrators and users present in the organization-level
            `can_move_messages_between_topics_group` setting can always move messages
            within the channel if they [have content access](/help/channel-permissions) to
            the channel.

            **Changes**: New in Zulip 11.0 (feature level 396). Prior to this
            change, only the users in `can_move_messages_between_topics_group` were able
            move messages between topics of a channel.

        can_send_message_group : typing.Optional[UpdateStreamRequestCanSendMessageGroup]
            The set of users who have permission to post in this channel
            expressed as an [update to a group-setting value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Note that a user must have metadata access to a channel and permission
            to administer the channel in order to modify this setting.

            Note that using this permission to send a message to a new topic requires
            also having permission to create new topics in the channel.

            **Changes**: New in Zulip 10.0 (feature level 333). Previously
            `stream_post_policy` field used to control the permission to
            post in the channel.

        can_subscribe_group : typing.Optional[UpdateStreamRequestCanSubscribeGroup]
            The set of users who have permission to subscribe themselves to this channel
            expressed as an [update to a group-setting value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Everyone, excluding guests, can subscribe to any public channel
            irrespective of this setting.

            Users in this group can subscribe to a private channel as well.

            Note that a user must [have content access](/help/channel-permissions)
            to a channel and permission to administer the channel in order to
            modify this setting.

            **Changes**: New in Zulip 10.0 (feature level 357).

        can_resolve_topics_group : typing.Optional[UpdateStreamRequestCanResolveTopicsGroup]
            The set of users who have permission to resolve topics in this channel
            expressed as an [update to a group-setting value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Users who have similar realm-level permissions can resolve topics
            in a channel regardless of the value of this setting.

            **Changes**: New in Zulip 11.0 (feature level 402).

        can_create_topic_group : typing.Optional[UpdateStreamRequestCanCreateTopicGroup]
            The set of users who have permission to create new topics in this channel
            expressed as an [update to a group-setting value][update-group-setting].

            Note that using this permission requires also having permission to send
            messages in the channel.

            For [private channels with protected history](/help/channel-permissions#private-channels),
            this setting can only be set to `role:everyone` [system group][system-groups].

            **Changes**: New in Zulip 12.0 (feature level 441). Previously, if you
            could send messages in a channel, you could create topics in the channel.

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values
            [system-groups]: /api/group-setting-values#system-groups

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.update_stream(
            stream_id=1,
        )
        """
        _response = self._raw_client.update_stream(
            stream_id,
            description=description,
            new_name=new_name,
            is_private=is_private,
            is_web_public=is_web_public,
            history_public_to_subscribers=history_public_to_subscribers,
            is_default_stream=is_default_stream,
            message_retention_days=message_retention_days,
            default_push_notifications=default_push_notifications,
            is_archived=is_archived,
            folder_id=folder_id,
            topics_policy=topics_policy,
            can_add_subscribers_group=can_add_subscribers_group,
            can_remove_subscribers_group=can_remove_subscribers_group,
            can_administer_channel_group=can_administer_channel_group,
            can_delete_any_message_group=can_delete_any_message_group,
            can_delete_own_message_group=can_delete_own_message_group,
            can_move_messages_out_of_channel_group=can_move_messages_out_of_channel_group,
            can_move_messages_within_channel_group=can_move_messages_within_channel_group,
            can_send_message_group=can_send_message_group,
            can_subscribe_group=can_subscribe_group,
            can_resolve_topics_group=can_resolve_topics_group,
            can_create_topic_group=can_create_topic_group,
            request_options=request_options,
        )
        return _response.data

    def get_stream_email_address(
        self,
        stream_id: int,
        *,
        sender_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetStreamEmailAddressResponse:
        """
        Get email address of a channel.

        Note that only users with permission to post messages in the channel
        can access the channel's email address.

        **Changes**: Prior to Zulip 12.0 (feature level 448), users without
        permission to post messages in the channel could access the channel's email
        if they had metadata access.

        New in Zulip 8.0 (feature level 226).

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        sender_id : typing.Optional[int]
            The ID of a user or bot which should appear as the sender when messages
            are sent to the channel using the returned channel email address.

            `sender_id` can be:

            - ID of the current user.
            - ID of the Email gateway bot. (Default value)
            - ID of a bot owned by the current user.

            **Changes**: New in Zulip 10.0 (feature level 335).

            Previously, the sender was always Email gateway bot.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStreamEmailAddressResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.get_stream_email_address(
            stream_id=1,
        )
        """
        _response = self._raw_client.get_stream_email_address(
            stream_id, sender_id=sender_id, request_options=request_options
        )
        return _response.data

    def delete_topic(
        self, stream_id: int, *, topic_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteTopicResponse:
        """
        Delete all messages in a topic.

        Topics are a field on messages (not an independent data structure), so
        deleting all the messages in the topic deletes the topic from Zulip.

        Because this endpoint deletes messages in batches, it is possible for
        the request to time out after only deleting some messages in the topic.
        When this happens, the `complete` boolean field in the success response
        will be `false`. Clients should repeat the request when handling such a
        response. If all messages in the topic were deleted, then the success
        response will return `"complete": true`.

        **Changes**: Before Zulip 9.0 (feature level 256), the server never sent
        [`stream` op: `update`](/api/get-events#stream-update) events with an
        updated `first_message_id` for a channel when the oldest message that
        had been sent to it changed.

        Before Zulip 8.0 (feature level 211), if the server's
        processing was interrupted by a timeout, but some messages in the topic
        were deleted, then it would return `"result": "partially_completed"`,
        along with a `code` field for an error string, in the success response
        to indicate that there was a timeout and that the client should repeat
        the request.

        As of Zulip 6.0 (feature level 154), instead of returning an error
        response when a request times out after successfully deleting some of
        the messages in the topic, a success response is returned with
        `"result": "partially_completed"` to indicate that some messages were
        deleted.

        Before Zulip 6.0 (feature level 147), this request did a single atomic
        operation, which could time out for very large topics. As of this
        feature level, messages are deleted in batches, starting with the newest
        messages, so that progress is made even if the request times out and
        returns an error.

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        topic_name : str
            The name of the topic to delete.

            Note: When the value of `realm_empty_topic_display_name` found in
            the [POST /register](/api/register-queue) response is used for this
            parameter, it is interpreted as an empty string.

            **Changes**: Before Zulip 10.0 (feature level 334), empty string
            was not a valid topic name for channel messages.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTopicResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.delete_topic(
            stream_id=1,
            topic_name="new coffee machine",
        )
        """
        _response = self._raw_client.delete_topic(stream_id, topic_name=topic_name, request_options=request_options)
        return _response.data

    def create_channel(
        self,
        *,
        name: str,
        subscribers: typing.Sequence[int],
        description: typing.Optional[str] = OMIT,
        announce: typing.Optional[bool] = OMIT,
        invite_only: typing.Optional[bool] = OMIT,
        is_web_public: typing.Optional[bool] = OMIT,
        is_default_stream: typing.Optional[bool] = OMIT,
        folder_id: typing.Optional[int] = OMIT,
        topics_policy: typing.Optional[TopicsPolicy] = OMIT,
        history_public_to_subscribers: typing.Optional[HistoryPublicToSubscribers] = OMIT,
        message_retention_days: typing.Optional[MessageRetentionDays] = OMIT,
        can_add_subscribers_group: typing.Optional[ChannelCanAddSubscribersGroup] = OMIT,
        can_create_topic_group: typing.Optional[CanCreateTopicGroup] = OMIT,
        can_delete_any_message_group: typing.Optional[CanDeleteAnyMessageGroup] = OMIT,
        can_delete_own_message_group: typing.Optional[CanDeleteOwnMessageGroup] = OMIT,
        can_remove_subscribers_group: typing.Optional[CanRemoveSubscribersGroup] = OMIT,
        can_administer_channel_group: typing.Optional[CanAdministerChannelGroup] = OMIT,
        can_move_messages_out_of_channel_group: typing.Optional[CanMoveMessagesOutOfChannelGroup] = OMIT,
        can_move_messages_within_channel_group: typing.Optional[CanMoveMessagesWithinChannelGroup] = OMIT,
        can_send_message_group: typing.Optional[CanSendMessageGroup] = OMIT,
        can_subscribe_group: typing.Optional[CanSubscribeGroup] = OMIT,
        can_resolve_topics_group: typing.Optional[CanResolveTopicsGroup] = OMIT,
        default_push_notifications: typing.Optional[DefaultPushNotifications] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateChannelResponse:
        """
        Create a new [channel](/help/create-channels), and optionally subscribe
        users to the newly created channel.

        The initial [channel settings](/api/update-stream) will be determined
        by the optional parameters, like `invite_only`, detailed below.

        **Changes**: New in Zulip 11.0 (feature level 417). Previously, this was
        only possible via the [`POST /api/subscribe`](/api/subscribe) endpoint,
        which handles both channel subscription and creation.

        Parameters
        ----------
        name : str
            The name of the new channel.

            Clients should use the `max_stream_name_length` returned by the
            [`POST /register`](/api/register-queue) endpoint to determine
            the maximum channel name length.

        subscribers : typing.Sequence[int]
            A list of user IDs of the users to be subscribed to the new channel.

        description : typing.Optional[str]
            The [description](/help/change-the-channel-description)
            to use for the new channel being created, in text/markdown format.

            Clients should use the `max_stream_description_length` returned
            by the [`POST /register`](/api/register-queue) endpoint to
            determine the maximum channel description length.

        announce : typing.Optional[bool]
            This determines whether [notification bot](/help/configure-automated-notices)
            will send an announcement about the new channel's creation.

        invite_only : typing.Optional[bool]
            This parameter and the ones that follow are used to request an initial
            configuration of the new channel.

            This parameter determines whether the newly created channel will be
            a [private channel](/help/channel-permissions#private-channels).

        is_web_public : typing.Optional[bool]
            This parameter determines whether the newly created channel will be
            a web-public channel.

            Note that creating web-public channels requires the
            `WEB_PUBLIC_STREAMS_ENABLED` [server setting][server-settings]
            to be enabled on the Zulip server in question, the organization
            to have enabled the `enable_spectator_access` realm setting, and
            the current user to have permission under the organization's
            `can_create_web_public_channel_group` realm setting.

            [server-settings]: https://zulip.readthedocs.io/en/stable/production/settings.html

        is_default_stream : typing.Optional[bool]
            This parameter determines whether the newly created channel will be
            added as a [default channel][default-channels] for new users joining
            the organization.

            [default-channels]: /help/set-default-channels-for-new-users

        folder_id : typing.Optional[int]
            This parameter adds the newly created channel to the specified
            [channel folder](/help/channel-folders).

            **Changes**: New in Zulip 11.0 (feature level 389).

        topics_policy : typing.Optional[TopicsPolicy]

        history_public_to_subscribers : typing.Optional[HistoryPublicToSubscribers]

        message_retention_days : typing.Optional[MessageRetentionDays]

        can_add_subscribers_group : typing.Optional[ChannelCanAddSubscribersGroup]

        can_create_topic_group : typing.Optional[CanCreateTopicGroup]

        can_delete_any_message_group : typing.Optional[CanDeleteAnyMessageGroup]

        can_delete_own_message_group : typing.Optional[CanDeleteOwnMessageGroup]

        can_remove_subscribers_group : typing.Optional[CanRemoveSubscribersGroup]

        can_administer_channel_group : typing.Optional[CanAdministerChannelGroup]

        can_move_messages_out_of_channel_group : typing.Optional[CanMoveMessagesOutOfChannelGroup]

        can_move_messages_within_channel_group : typing.Optional[CanMoveMessagesWithinChannelGroup]

        can_send_message_group : typing.Optional[CanSendMessageGroup]

        can_subscribe_group : typing.Optional[CanSubscribeGroup]

        can_resolve_topics_group : typing.Optional[CanResolveTopicsGroup]

        default_push_notifications : typing.Optional[DefaultPushNotifications]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateChannelResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.create_channel(
            name="music",
            subscribers=[17, 12],
        )
        """
        _response = self._raw_client.create_channel(
            name=name,
            subscribers=subscribers,
            description=description,
            announce=announce,
            invite_only=invite_only,
            is_web_public=is_web_public,
            is_default_stream=is_default_stream,
            folder_id=folder_id,
            topics_policy=topics_policy,
            history_public_to_subscribers=history_public_to_subscribers,
            message_retention_days=message_retention_days,
            can_add_subscribers_group=can_add_subscribers_group,
            can_create_topic_group=can_create_topic_group,
            can_delete_any_message_group=can_delete_any_message_group,
            can_delete_own_message_group=can_delete_own_message_group,
            can_remove_subscribers_group=can_remove_subscribers_group,
            can_administer_channel_group=can_administer_channel_group,
            can_move_messages_out_of_channel_group=can_move_messages_out_of_channel_group,
            can_move_messages_within_channel_group=can_move_messages_within_channel_group,
            can_send_message_group=can_send_message_group,
            can_subscribe_group=can_subscribe_group,
            can_resolve_topics_group=can_resolve_topics_group,
            default_push_notifications=default_push_notifications,
            request_options=request_options,
        )
        return _response.data

    def create_channel_folder(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateChannelFolderResponse:
        """
        Create a new [channel folder](/help/channel-folders).

        **Changes**: New in Zulip 11.0 (feature level 389).

        Parameters
        ----------
        name : str
            The name of the channel folder.

            Clients should use the `max_channel_folder_name_length` returned
            by the [`POST /register`](/api/register-queue) endpoint to determine
            the maximum channel folder name length.

            Value cannot be an empty string.

        description : typing.Optional[str]
            The description of the channel folder.

            Clients should use the `max_channel_folder_description_length`
            returned by the [`POST /register`](/api/register-queue) endpoint
            to determine the maximum channel folder description length.

            Note that this parameter must be passed as part of the request,
            but can be an empty string if no description for the new channel
            folder is desired.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateChannelFolderResponse
            A success response containing the unique ID of the channel folder.
            This field provides a straightforward way to reference the
            newly created channel folder.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.create_channel_folder(
            name="marketing",
        )
        """
        _response = self._raw_client.create_channel_folder(
            name=name, description=description, request_options=request_options
        )
        return _response.data

    def get_channel_folders(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetChannelFoldersResponse:
        """
        Fetches all of the [channel folders](/help/channel-folders) in the
        organization, sorted by the `order` field.

        **Changes**: Before Zulip 11.0 (feature level 414), the list of channel
        folders was sorted by ID as the `order` field didn't exist.

        New in Zulip 11.0 (feature level 389).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChannelFoldersResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.get_channel_folders()
        """
        _response = self._raw_client.get_channel_folders(request_options=request_options)
        return _response.data

    def patch_channel_folders(
        self, *, order: typing.Sequence[int], request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Reorder the [channel folders](/help/channel-folders) in the user's
        organization.

        Channel folders are displayed in Zulip UI in order; this endpoint allows
        administrative settings UI to change the ordering of channel folders.

        This endpoint is used to implement the dragging feature described in the
        [manage channel folders documentation](/help/manage-channel-folders).

        **Changes**: New in Zulip 11.0 (feature level 414).

        Parameters
        ----------
        order : typing.Sequence[int]
            A list of channel folder IDs representing the new order.

            This list must include the IDs of [all the organization's channel
            folders](/api/get-channel-folders), including archived folders.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.patch_channel_folders(
            order=[2, 1],
        )
        """
        _response = self._raw_client.patch_channel_folders(order=order, request_options=request_options)
        return _response.data

    def update_channel_folder(
        self,
        channel_folder_id: int,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Update the name or description of a [channel folder](/help/channel-folders)
        with the specified ID.

        This endpoint is also used to archive or unarchive the specified channel
        folder.

        **Changes**: New in Zulip 11.0 (feature level 389).

        Parameters
        ----------
        channel_folder_id : int
            The ID of the target channel folder.

        name : typing.Optional[str]
            The new name of the channel folder.

            Clients should use the `max_channel_folder_name_length` returned
            by the [`POST /register`](/api/register-queue) endpoint to determine
            the maximum channel folder name length.

            Value cannot be an empty string.

        description : typing.Optional[str]
            The new description of the channel folder.

            Clients should use the `max_channel_folder_description_length`
            returned by the [`POST /register`](/api/register-queue) endpoint
            to determine the maximum channel folder description length.

        is_archived : typing.Optional[bool]
            Whether to archive or unarchive the channel folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.update_channel_folder(
            channel_folder_id=1,
        )
        """
        _response = self._raw_client.update_channel_folder(
            channel_folder_id,
            name=name,
            description=description,
            is_archived=is_archived,
            request_options=request_options,
        )
        return _response.data

    def create_big_blue_button_video_call(
        self,
        *,
        meeting_name: str,
        voice_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateBigBlueButtonVideoCallResponse:
        """
        Create a video call URL for a BigBlueButton video call.
        Requires [BigBlueButton 2.4+](/integrations/big-blue-button)
        to be configured on the Zulip server.

        The acting user will be given the moderator role on the call.

        **Changes**: Prior to Zulip 10.0 (feature level 337), every
        user was given the moderator role on BigBlueButton calls, via
        encoding a moderator password in the generated URLs.

        Parameters
        ----------
        meeting_name : str
            Meeting name for the BigBlueButton video call.

        voice_only : typing.Optional[bool]
            Configures whether the call is voice-only; if true,
            disables cameras for all users. Only the call
            creator/moderator can edit this configuration.

            **Changes**: New in Zulip 10.0 (feature level 337).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateBigBlueButtonVideoCallResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.create_big_blue_button_video_call(
            meeting_name="test_channel meeting",
        )
        """
        _response = self._raw_client.create_big_blue_button_video_call(
            meeting_name=meeting_name, voice_only=voice_only, request_options=request_options
        )
        return _response.data

    def create_nextcloud_talk_video_call(
        self, *, room_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateNextcloudTalkVideoCallResponse:
        """
        Create a video call URL for a Nextcloud Talk video call. Requires
        [Nextcloud Talk](/integrations/nextcloud-talk) to be configured on the
        Zulip server.

        **Changes**: New in Zulip 12.0 (feature level 465).

        Parameters
        ----------
        room_name : str
            Room name for the Nextcloud Talk conversation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateNextcloudTalkVideoCallResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.create_nextcloud_talk_video_call(
            room_name="#Test > team check-in",
        )
        """
        _response = self._raw_client.create_nextcloud_talk_video_call(
            room_name=room_name, request_options=request_options
        )
        return _response.data

    def create_webex_video_call(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateWebexVideoCallResponse:
        """
        Create a video call URL for a Webex video call.

        Requires [Webex integration](/integrations/webex) to be configured
        on the Zulip server.

        Clients should confirm that the user has completed the OAuth process
        with Webex and has a Webex token before attempting to create a video
        call URL. See the `has_webex_token` field in the [`POST /register`
        response](/api/register-queue), as well as the [`has_webex_token`
        event type](/api/get-events#has_webex_token).

        **Changes**: New in Zulip 12.0 (feature level 493).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWebexVideoCallResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.create_webex_video_call()
        """
        _response = self._raw_client.create_webex_video_call(request_options=request_options)
        return _response.data

    def create_constructor_groups_video_call(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateConstructorGroupsVideoCallResponse:
        """
        Create a video call URL for a Constructor Groups video call.
        Requires [Constructor Groups](/integrations/constructor-groups)
        to be configured on the Zulip server.

        **Changes**: New in Zulip 12.0 (feature level 460).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateConstructorGroupsVideoCallResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.channels.create_constructor_groups_video_call()
        """
        _response = self._raw_client.create_constructor_groups_video_call(request_options=request_options)
        return _response.data


class AsyncChannelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChannelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChannelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChannelsClient
        """
        return self._raw_client

    async def get_stream_id(
        self, *, stream: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetStreamIdResponse:
        """
        Get the unique ID of a given channel.

        Parameters
        ----------
        stream : str
            The name of the channel to access.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStreamIdResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.get_stream_id(
                stream="Denmark",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_stream_id(stream=stream, request_options=request_options)
        return _response.data

    async def add_default_stream(
        self, *, stream_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Add a channel to the set of [default channels][default-channels]
        for new users joining the organization.

        [default-channels]: /help/set-default-channels-for-new-users

        Parameters
        ----------
        stream_id : int
            The ID of the target channel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.add_default_stream(
                stream_id=10,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_default_stream(stream_id=stream_id, request_options=request_options)
        return _response.data

    async def remove_default_stream(
        self, *, stream_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Remove a channel from the set of [default channels][default-channels]
        for new users joining the organization.

        [default-channels]: /help/set-default-channels-for-new-users

        Parameters
        ----------
        stream_id : int
            The ID of the target channel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.remove_default_stream(
                stream_id=10,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_default_stream(stream_id=stream_id, request_options=request_options)
        return _response.data

    async def get_stream_topics(
        self,
        stream_id: int,
        *,
        allow_empty_topic_name: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetStreamTopicsResponse:
        """
        Get all topics the user has access to in a specific channel.

        Note that for [private channels with
        protected history](/help/channel-permissions#private-channels),
        the user will only have access to topics of messages sent after they
        [subscribed to](/api/subscribe) the channel. Similarly, a user's
        [bot](/help/bots-overview#bot-type) will only have access to messages
        sent after the bot was subscribed to the channel, instead of when the
        user subscribed.

        **Changes**: Before Zulip 12.0 (feature level 480), this
        endpoint was not supported for archived channels.

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        allow_empty_topic_name : typing.Optional[bool]
            Whether the client supports processing the empty string as
            a topic name in the returned data.

            If `false`, the value of `realm_empty_topic_display_name`
            found in the [`POST /register`](/api/register-queue) response is
            returned replacing the empty string as the topic name.

            **Changes**: New in Zulip 10.0 (feature level 334). Previously,
            the empty string was not a valid topic.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStreamTopicsResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.get_stream_topics(
                stream_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_stream_topics(
            stream_id, allow_empty_topic_name=allow_empty_topic_name, request_options=request_options
        )
        return _response.data

    async def get_subscriptions(
        self,
        *,
        include_subscribers: typing.Optional[GetSubscriptionsRequestIncludeSubscribers] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSubscriptionsResponse:
        """
        Get all channels that the user is subscribed to.

        Parameters
        ----------
        include_subscribers : typing.Optional[GetSubscriptionsRequestIncludeSubscribers]
            Whether each returned channel object should include a `subscribers`
            field containing a list of the user IDs of its subscribers.

            Client apps supporting organizations with many thousands of users
            should not pass `true`, because the full subscriber matrix may be
            several megabytes of data. The `partial` value, combined with the
            `subscriber_count` and fetching subscribers for individual channels as
            needed, is recommended to support client app features where
            channel subscriber data is useful.

            If a client passes `partial` for this parameter, the server may,
            for some channels, return a subset of the channel's subscribers
            in the `partial_subscribers` field instead of the `subscribers` field,
            which always contains the complete set of subscribers.

            The server guarantees that it will always return a `subscribers`
            field for channels with fewer than 250 total subscribers. When
            returning a `partial_subscribers` field, the server guarantees
            that all bot users and users active within the last 14 days will
            be included. For other cases, the server may use its discretion
            to determine which channels and users to include, balancing between
            payload size and usefulness of the data provided to the client.

            **Changes**: The `partial` value is new in Zulip 11.0 (feature level 412).

            New in Zulip 2.1.0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSubscriptionsResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.get_subscriptions()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_subscriptions(
            include_subscribers=include_subscribers, request_options=request_options
        )
        return _response.data

    async def subscribe(
        self,
        *,
        subscriptions: typing.Sequence[SubscribeRequestSubscriptionsItem],
        principals: typing.Optional[Principals] = OMIT,
        authorization_errors_fatal: typing.Optional[bool] = OMIT,
        announce: typing.Optional[bool] = OMIT,
        invite_only: typing.Optional[bool] = OMIT,
        is_web_public: typing.Optional[bool] = OMIT,
        is_default_stream: typing.Optional[bool] = OMIT,
        history_public_to_subscribers: typing.Optional[HistoryPublicToSubscribers] = OMIT,
        message_retention_days: typing.Optional[MessageRetentionDays] = OMIT,
        default_push_notifications: typing.Optional[DefaultPushNotifications] = OMIT,
        topics_policy: typing.Optional[TopicsPolicy] = OMIT,
        can_add_subscribers_group: typing.Optional[ChannelCanAddSubscribersGroup] = OMIT,
        can_remove_subscribers_group: typing.Optional[CanRemoveSubscribersGroup] = OMIT,
        can_administer_channel_group: typing.Optional[CanAdministerChannelGroup] = OMIT,
        can_delete_any_message_group: typing.Optional[CanDeleteAnyMessageGroup] = OMIT,
        can_delete_own_message_group: typing.Optional[CanDeleteOwnMessageGroup] = OMIT,
        can_move_messages_out_of_channel_group: typing.Optional[CanMoveMessagesOutOfChannelGroup] = OMIT,
        can_move_messages_within_channel_group: typing.Optional[CanMoveMessagesWithinChannelGroup] = OMIT,
        can_send_message_group: typing.Optional[CanSendMessageGroup] = OMIT,
        can_subscribe_group: typing.Optional[CanSubscribeGroup] = OMIT,
        can_resolve_topics_group: typing.Optional[CanResolveTopicsGroup] = OMIT,
        can_create_topic_group: typing.Optional[CanCreateTopicGroup] = OMIT,
        folder_id: typing.Optional[int] = OMIT,
        send_new_subscription_messages: typing.Optional[SendNewSubscriptionMessages] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscribeResponse:
        """
        Subscribe one or more users to one or more channels.

        If any of the specified channels do not exist, they are automatically
        created. The initial [channel settings](/api/update-stream) will be determined
        by the optional parameters, like `invite_only`, detailed below.

        Note that the ability to subscribe oneself and/or other users
        to a specified channel depends on the [channel's permissions
        settings](/help/channel-permissions).

        **Changes**: Before Zulip 10.0 (feature level 362),
        subscriptions in archived channels could not be modified.

        Before Zulip 10.0 (feature level 357), the
        `can_subscribe_group` permission, which allows members of the
        group to subscribe themselves to the channel, did not exist.

        Before Zulip 10.0 (feature level 349), a user cannot subscribe
        other users to a private channel without being subscribed
        to that channel themselves. Now, If a user is part of
        `can_add_subscribers_group`, they can subscribe themselves or other
        users to a private channel without being subscribed to that channel.

        Removed `stream_post_policy` and `is_announcement_only`
        parameters in Zulip 10.0 (feature level 333), as permission to post
        in the channel is now controlled by `can_send_message_group`.

        Before Zulip 8.0 (feature level 208), if a user specified by the
        [`principals`][principals-param] parameter was a deactivated user,
        or did not exist, then an HTTP status code of 403 was returned with
        `code: "UNAUTHORIZED_PRINCIPAL"` in the error response. As of this
        feature level, an HTTP status code of 400 is returned with
        `code: "BAD_REQUEST"` in the error response for these cases.

        [principals-param]: /api/subscribe#parameter-principals

        Parameters
        ----------
        subscriptions : typing.Sequence[SubscribeRequestSubscriptionsItem]
            A list of dictionaries containing the key `name` and value
            specifying the name of the channel to subscribe. If the channel does not
            exist a new channel is created. The description of the channel created can
            be specified by setting the dictionary key `description` with an
            appropriate value.

        principals : typing.Optional[Principals]

        authorization_errors_fatal : typing.Optional[bool]
            A boolean specifying whether authorization errors (such as when the
            requesting user is not authorized to access a private channel) should be
            considered fatal or not. When `true`, an authorization error is reported
            as such. When set to `false`, the response will be a 200 and any channels
            where the request encountered an authorization error will be listed
            in the `unauthorized` key.

        announce : typing.Optional[bool]
            If one of the channels specified did not exist previously and is thus created
            by this call, this determines whether [notification bot](/help/configure-automated-notices)
            will send an announcement about the new channel's creation.

        invite_only : typing.Optional[bool]
            As described above, this endpoint will create a new channel if passed
            a channel name that doesn't already exist. This parameters and the ones
            that follow are used to request an initial configuration of a created
            channel; they are ignored for channels that already exist.

            This parameter determines whether any newly created channels will be
            private channels.

        is_web_public : typing.Optional[bool]
            This parameter determines whether any newly created channels will be
            web-public channels.

            Note that creating web-public channels requires the
            `WEB_PUBLIC_STREAMS_ENABLED` [server setting][server-settings]
            to be enabled on the Zulip server in question, the organization
            to have enabled the `enable_spectator_access` realm setting, and
            the current use to have permission under the organization's
            `can_create_web_public_channel_group` realm setting.

            [server-settings]: https://zulip.readthedocs.io/en/stable/production/settings.html

            **Changes**: New in Zulip 5.0 (feature level 98).

        is_default_stream : typing.Optional[bool]
            This parameter determines whether any newly created channels will be
            added as [default channels][default-channels] for new users joining
            the organization.

            [default-channels]: /help/set-default-channels-for-new-users

            **Changes**: New in Zulip 8.0 (feature level 200). Previously, default channel status
            could only be changed using the [dedicated API endpoint](/api/add-default-stream).

        history_public_to_subscribers : typing.Optional[HistoryPublicToSubscribers]

        message_retention_days : typing.Optional[MessageRetentionDays]

        default_push_notifications : typing.Optional[DefaultPushNotifications]

        topics_policy : typing.Optional[TopicsPolicy]

        can_add_subscribers_group : typing.Optional[ChannelCanAddSubscribersGroup]

        can_remove_subscribers_group : typing.Optional[CanRemoveSubscribersGroup]

        can_administer_channel_group : typing.Optional[CanAdministerChannelGroup]

        can_delete_any_message_group : typing.Optional[CanDeleteAnyMessageGroup]

        can_delete_own_message_group : typing.Optional[CanDeleteOwnMessageGroup]

        can_move_messages_out_of_channel_group : typing.Optional[CanMoveMessagesOutOfChannelGroup]

        can_move_messages_within_channel_group : typing.Optional[CanMoveMessagesWithinChannelGroup]

        can_send_message_group : typing.Optional[CanSendMessageGroup]

        can_subscribe_group : typing.Optional[CanSubscribeGroup]

        can_resolve_topics_group : typing.Optional[CanResolveTopicsGroup]

        can_create_topic_group : typing.Optional[CanCreateTopicGroup]

        folder_id : typing.Optional[int]
            This parameter adds the newly created channel to the specified
            [channel folder](/help/channel-folders).

            **Changes**: New in Zulip 11.0 (feature level 389).

        send_new_subscription_messages : typing.Optional[SendNewSubscriptionMessages]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscribeResponse
            Success.

        Examples
        --------
        import asyncio

        from fern.channels import SubscribeRequestSubscriptionsItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.subscribe(
                subscriptions=[
                    SubscribeRequestSubscriptionsItem(
                        name="Verona",
                        description="Italian city",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.subscribe(
            subscriptions=subscriptions,
            principals=principals,
            authorization_errors_fatal=authorization_errors_fatal,
            announce=announce,
            invite_only=invite_only,
            is_web_public=is_web_public,
            is_default_stream=is_default_stream,
            history_public_to_subscribers=history_public_to_subscribers,
            message_retention_days=message_retention_days,
            default_push_notifications=default_push_notifications,
            topics_policy=topics_policy,
            can_add_subscribers_group=can_add_subscribers_group,
            can_remove_subscribers_group=can_remove_subscribers_group,
            can_administer_channel_group=can_administer_channel_group,
            can_delete_any_message_group=can_delete_any_message_group,
            can_delete_own_message_group=can_delete_own_message_group,
            can_move_messages_out_of_channel_group=can_move_messages_out_of_channel_group,
            can_move_messages_within_channel_group=can_move_messages_within_channel_group,
            can_send_message_group=can_send_message_group,
            can_subscribe_group=can_subscribe_group,
            can_resolve_topics_group=can_resolve_topics_group,
            can_create_topic_group=can_create_topic_group,
            folder_id=folder_id,
            send_new_subscription_messages=send_new_subscription_messages,
            request_options=request_options,
        )
        return _response.data

    async def unsubscribe(
        self,
        *,
        subscriptions: typing.Sequence[str],
        principals: typing.Optional[Principals] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UnsubscribeResponse:
        """
        Unsubscribe yourself or other users from one or more channels.

        In addition to managing the current user's subscriptions, this
        endpoint can be used to remove other users from channels. This
        is possible in 3 situations:

        - Organization administrators can remove any user from any
          channel.
        - Users can remove a bot that they own from any channel that
          the user [can access](/help/channel-permissions).
        - Users can unsubscribe any user from a channel if they [have
          access](/help/channel-permissions) to the channel and are a
          member of the [user group](/api/get-user-groups) specified
          by the [`can_remove_subscribers_group`][can-remove-parameter]
          for the channel.

        **Changes**: Before Zulip 10.0 (feature level 362),
        subscriptions in archived channels could not be modified.

        Before Zulip 8.0 (feature level 208), if a user specified by
        the [`principals`][principals-param] parameter was a
        deactivated user, or did not exist, then an HTTP status code
        of 403 was returned with `code: "UNAUTHORIZED_PRINCIPAL"` in
        the error response. As of this feature level, an HTTP status
        code of 400 is returned with `code: "BAD_REQUEST"` in the
        error response for these cases.

        Before Zulip 8.0 (feature level 197),
        the `can_remove_subscribers_group` setting
        was named `can_remove_subscribers_group_id`.

        Before Zulip 7.0 (feature level 161), the
        `can_remove_subscribers_group_id` for all channels was always
        the system group for organization administrators.

        Before Zulip 6.0 (feature level 145), users had no special
        privileges for managing bots that they own.

        [principals-param]: /api/unsubscribe#parameter-principals
        [can-remove-parameter]: /api/subscribe#parameter-can_remove_subscribers_group

        Parameters
        ----------
        subscriptions : typing.Sequence[str]
            A list of channel names to unsubscribe from. This parameter is called
            `streams` in our Python API.

        principals : typing.Optional[Principals]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnsubscribeResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.unsubscribe(
                subscriptions=["Verona", "Denmark"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unsubscribe(
            subscriptions=subscriptions, principals=principals, request_options=request_options
        )
        return _response.data

    async def update_subscriptions(
        self,
        *,
        delete: typing.Optional[typing.Sequence[str]] = OMIT,
        add: typing.Optional[typing.Sequence[UpdateSubscriptionsRequestAddItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSubscriptionsResponse:
        """
        Update which channels you are subscribed to.

        **Changes**: Before Zulip 10.0 (feature level 362),
        subscriptions in archived channels could not be modified.

        Parameters
        ----------
        delete : typing.Optional[typing.Sequence[str]]
            A list of channel names to unsubscribe from.

        add : typing.Optional[typing.Sequence[UpdateSubscriptionsRequestAddItem]]
            A list of objects describing which channels to subscribe to, optionally
            including per-user subscription parameters (e.g. color) and if the
            channel is to be created, its description.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSubscriptionsResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.update_subscriptions()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_subscriptions(delete=delete, add=add, request_options=request_options)
        return _response.data

    async def mute_topic(
        self,
        *,
        topic: str,
        op: MuteTopicRequestOp,
        stream_id: typing.Optional[int] = OMIT,
        stream: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        [Mute or unmute a topic](/help/mute-a-topic) within a channel that
        the current user is subscribed to.

        **Changes**: Deprecated in Zulip 7.0 (feature level 170). Clients connecting
        to newer servers should use the [POST /user_topics](/api/update-user-topic)
        endpoint, as this endpoint may be removed in a future release.

        Before Zulip 7.0 (feature level 169), this endpoint
        returned an error if asked to mute a topic that was already muted
        or asked to unmute a topic that had not previously been muted.

        Parameters
        ----------
        topic : str
            The topic to (un)mute. Note that the request will succeed regardless of
            whether any messages have been sent to the specified topic.

            Clients should use the `max_topic_length` returned by the
            [`POST /register`](/api/register-queue) endpoint to determine
            the maximum topic length.

        op : MuteTopicRequestOp
            Whether to mute (`add`) or unmute (`remove`) the provided topic.

        stream_id : typing.Optional[int]
            The ID of the channel to access.

            Clients must provide either `stream` or `stream_id` as a parameter
            to this endpoint, but not both.

            **Changes**: New in Zulip 2.0.0.

        stream : typing.Optional[str]
            The name of the channel to access.

            Clients must provide either `stream` or `stream_id` as a parameter
            to this endpoint, but not both. Clients should use `stream_id`
            instead of the `stream` parameter when possible.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern.channels import MuteTopicRequestOp

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.mute_topic(
                topic="dinner",
                op=MuteTopicRequestOp.ADD,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mute_topic(
            topic=topic, op=op, stream_id=stream_id, stream=stream, request_options=request_options
        )
        return _response.data

    async def update_user_topic(
        self,
        *,
        stream_id: int,
        topic: str,
        visibility_policy: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        This endpoint is used to update the personal preferences for a topic,
        such as the topic's visibility policy, which is used to implement
        [mute a topic](/help/mute-a-topic) and related features.

        This endpoint can be used to update the visibility policy for the single
        channel and topic pair indicated by the parameters for a user.

        **Changes**: New in Zulip 7.0 (feature level 170). Previously,
        toggling whether a topic was muted or unmuted was managed by the
        [PATCH /users/me/subscriptions/muted_topics](/api/mute-topic) endpoint.

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        topic : str
            The topic for which the personal preferences needs to be updated.
            Note that the request will succeed regardless of whether
            any messages have been sent to the specified topic.

            Clients should use the `max_topic_length` returned by the
            [`POST /register`](/api/register-queue) endpoint to determine
            the maximum topic length.

            Note: When the value of `realm_empty_topic_display_name` found in
            the [POST /register](/api/register-queue) response is used for this
            parameter, it is interpreted as an empty string.

            **Changes**: Before Zulip 10.0 (feature level 334), empty string
            was not a valid topic name for channel messages.

        visibility_policy : int
            Controls which visibility policy to set.

            - 0 = None. Removes the visibility policy previously set for the topic.
            - 1 = Muted. [Mutes the topic](/help/mute-a-topic) in a channel.
            - 2 = Unmuted. [Unmutes the topic](/help/mute-a-topic) in a muted channel.
            - 3 = Followed. [Follows the topic](/help/follow-a-topic).

            In an unmuted channel, a topic visibility policy of unmuted will have the
            same effect as the "None" visibility policy.

            **Changes**: In Zulip 7.0 (feature level 219), added followed as
            a visibility policy option.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.update_user_topic(
                stream_id=1,
                topic="dinner",
                visibility_policy=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user_topic(
            stream_id=stream_id, topic=topic, visibility_policy=visibility_policy, request_options=request_options
        )
        return _response.data

    async def get_subscription_status(
        self, user_id: int, stream_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSubscriptionStatusResponse:
        """
        Check whether a user is subscribed to a channel.

        **Changes**: Prior to Zulip 12.0 (feature level 458), this endpoint
        did not support querying subscriptions of bot users.

        New in Zulip 3.0 (feature level 12).

        Parameters
        ----------
        user_id : int
            The target user's ID.

        stream_id : int
            The ID of the channel to access.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSubscriptionStatusResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.get_subscription_status(
                user_id=1,
                stream_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_subscription_status(user_id, stream_id, request_options=request_options)
        return _response.data

    async def get_user_channels(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserChannelsResponse:
        """
        Gets the list of channels that the target user is subscribed to.

        The [channel security model](/help/channel-permissions) means only those
        subscribed channels to which the acting user has metadata access are
        returned.

        For organization administrators, this is guaranteed to be all channels
        the target user is subscribed to, since organization administrators
        implicitly have metadata access to all channels.

        **Changes**: Prior to Zulip 12.0 (feature level 458), target users that
        were bots resulted in a permissions error.

        New in Zulip 12.0 (feature level 440).

        Parameters
        ----------
        user_id : int
            The target user's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserChannelsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.get_user_channels(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_channels(user_id, request_options=request_options)
        return _response.data

    async def update_subscription_settings(
        self,
        *,
        subscription_data: typing.Sequence[UpdateSubscriptionSettingsRequestSubscriptionDataItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IgnoredParametersSuccess:
        """
        Update the current user's personal settings for channels they are
        subscribed to. These settings include [color](/help/change-the-color-of-a-channel),
        [muting](/help/mute-a-channel), [pinning](/help/pin-a-channel)
        and [per-channel notification settings](/help/channel-notifications).

        There is a single channel alternative to this bulk endpoint:
        [`POST /users/me/subscriptions/{stream_id}`](/api/update-subscription-property).

        **Changes**: Prior to Zulip 5.0 (feature level 111), the response object
        included the `subscription_data` in the request. The endpoint now returns
        the more ergonomic [`ignored_parameters_unsupported`][ignored-parameters]
        array instead.

        [ignored-parameters]: /api/rest-error-handling#ignored-parameters

        Parameters
        ----------
        subscription_data : typing.Sequence[UpdateSubscriptionSettingsRequestSubscriptionDataItem]
            A list of objects that describe the changes that should be applied in
            each subscription. Each object represents a subscription, and must have
            a `stream_id` key that identifies the channel, as well as the `property`
            being modified and its new `value`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IgnoredParametersSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern.channels import UpdateSubscriptionSettingsRequestSubscriptionDataItem

        from fern import AsyncFernApi, SubscriptionProperty

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.update_subscription_settings(
                subscription_data=[
                    UpdateSubscriptionSettingsRequestSubscriptionDataItem(
                        stream_id=1,
                        property=SubscriptionProperty.PIN_TO_TOP,
                        value=True,
                    ),
                    UpdateSubscriptionSettingsRequestSubscriptionDataItem(
                        stream_id=3,
                        property=SubscriptionProperty.COLOR,
                        value="#f00f00",
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_subscription_settings(
            subscription_data=subscription_data, request_options=request_options
        )
        return _response.data

    async def update_subscription_property(
        self,
        stream_id: int,
        *,
        property: SubscriptionProperty,
        value: SubscriptionPropertyValue,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Update the current user's personal settings for a specific channel they
        are subscribed to. These settings include [color](/help/change-the-color-of-a-channel),
        [muting](/help/mute-a-channel), [pinning](/help/pin-a-channel)
        and [per-channel notification settings](/help/channel-notifications).

        This is a single channel alternative to the bulk endpoint:
        [`POST /users/me/subscriptions/properties`](/api/update-subscription-settings).

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        property : SubscriptionProperty

        value : SubscriptionPropertyValue

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SubscriptionProperty

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.update_subscription_property(
                stream_id=1,
                property=SubscriptionProperty.COLOR,
                value=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_subscription_property(
            stream_id, property=property, value=value, request_options=request_options
        )
        return _response.data

    async def get_subscribers(
        self, stream_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSubscribersResponse:
        """
        Get all users subscribed to a channel.

        **Changes**: Before Zulip 12.0 (feature level 480), this
        endpoint was not supported for archived channels.

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSubscribersResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.get_subscribers(
                stream_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_subscribers(stream_id, request_options=request_options)
        return _response.data

    async def get_streams(
        self,
        *,
        include_public: typing.Optional[bool] = None,
        include_web_public: typing.Optional[bool] = None,
        include_subscribed: typing.Optional[bool] = None,
        exclude_archived: typing.Optional[bool] = None,
        include_all_active: typing.Optional[bool] = None,
        include_all: typing.Optional[bool] = None,
        include_default: typing.Optional[bool] = None,
        include_owner_subscribed: typing.Optional[bool] = None,
        include_can_access_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetStreamsResponse:
        """
        Get all channels that the user [has access to](/help/channel-permissions).

        Parameters
        ----------
        include_public : typing.Optional[bool]
            Include all public channels.

        include_web_public : typing.Optional[bool]
            Include all web-public channels.

        include_subscribed : typing.Optional[bool]
            Include all channels that the user is subscribed to.

        exclude_archived : typing.Optional[bool]
            Whether to exclude archived streams from the results.

            **Changes**: New in Zulip 10.0 (feature level 315).

        include_all_active : typing.Optional[bool]
            Deprecated parameter to include all channels. The user must
            have administrative privileges to use this parameter.

            **Changes**: Deprecated in Zulip 10.0 (feature level
            356). Clients interacting with newer servers should use
            the equivalent `include_all` parameter, which does not
            incorrectly hint that this parameter, and not
            `exclude_archived`, controls whether archived channels
            appear in the response.

        include_all : typing.Optional[bool]
            Include all channels that the user has metadata access to.

            For organization administrators, this will be all channels
            in the organization, since organization administrators
            implicitly have metadata access to all channels.

            **Changes**: New in Zulip 10.0 (feature level 356). On older
            versions, use `include_all_active`, which this replaces.

        include_default : typing.Optional[bool]
            Include all default channels for the user's realm.

        include_owner_subscribed : typing.Optional[bool]
            If the user is a bot, include all channels that the bot's owner is
            subscribed to.

        include_can_access_content : typing.Optional[bool]
            Include all the channels that the user has content access to.

            **Changes**: New in Zulip 10.0 (feature level 356).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStreamsResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.get_streams()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_streams(
            include_public=include_public,
            include_web_public=include_web_public,
            include_subscribed=include_subscribed,
            exclude_archived=exclude_archived,
            include_all_active=include_all_active,
            include_all=include_all,
            include_default=include_default,
            include_owner_subscribed=include_owner_subscribed,
            include_can_access_content=include_can_access_content,
            request_options=request_options,
        )
        return _response.data

    async def get_stream_by_id(
        self, stream_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetStreamByIdResponse:
        """
        Fetch details for the channel with the ID `stream_id`.

        **Changes**: Before Zulip 12.0 (feature level 480), this
        endpoint was not supported for archived channels.

        New in Zulip 6.0 (feature level 132).

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStreamByIdResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.get_stream_by_id(
                stream_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_stream_by_id(stream_id, request_options=request_options)
        return _response.data

    async def archive_stream(
        self, stream_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        [Archive the channel](/help/archive-a-channel) with the ID `stream_id`.

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.archive_stream(
                stream_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.archive_stream(stream_id, request_options=request_options)
        return _response.data

    async def update_stream(
        self,
        stream_id: int,
        *,
        description: typing.Optional[str] = OMIT,
        new_name: typing.Optional[str] = OMIT,
        is_private: typing.Optional[bool] = OMIT,
        is_web_public: typing.Optional[bool] = OMIT,
        history_public_to_subscribers: typing.Optional[bool] = OMIT,
        is_default_stream: typing.Optional[bool] = OMIT,
        message_retention_days: typing.Optional[MessageRetentionDays] = OMIT,
        default_push_notifications: typing.Optional[DefaultPushNotifications] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        folder_id: typing.Optional[int] = OMIT,
        topics_policy: typing.Optional[TopicsPolicy] = OMIT,
        can_add_subscribers_group: typing.Optional[UpdateStreamRequestCanAddSubscribersGroup] = OMIT,
        can_remove_subscribers_group: typing.Optional[UpdateStreamRequestCanRemoveSubscribersGroup] = OMIT,
        can_administer_channel_group: typing.Optional[UpdateStreamRequestCanAdministerChannelGroup] = OMIT,
        can_delete_any_message_group: typing.Optional[UpdateStreamRequestCanDeleteAnyMessageGroup] = OMIT,
        can_delete_own_message_group: typing.Optional[UpdateStreamRequestCanDeleteOwnMessageGroup] = OMIT,
        can_move_messages_out_of_channel_group: typing.Optional[
            UpdateStreamRequestCanMoveMessagesOutOfChannelGroup
        ] = OMIT,
        can_move_messages_within_channel_group: typing.Optional[
            UpdateStreamRequestCanMoveMessagesWithinChannelGroup
        ] = OMIT,
        can_send_message_group: typing.Optional[UpdateStreamRequestCanSendMessageGroup] = OMIT,
        can_subscribe_group: typing.Optional[UpdateStreamRequestCanSubscribeGroup] = OMIT,
        can_resolve_topics_group: typing.Optional[UpdateStreamRequestCanResolveTopicsGroup] = OMIT,
        can_create_topic_group: typing.Optional[UpdateStreamRequestCanCreateTopicGroup] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Configure the channel with the ID `stream_id`. This endpoint supports
        an organization administrator editing any property of a channel,
        including:

        - Channel [name](/help/rename-a-channel) and [description](/help/change-the-channel-description)
        - Channel [permissions](/help/channel-permissions), including
          [privacy](/help/change-the-privacy-of-a-channel) and [who can
          send](/help/channel-posting-policy).

        Note that an organization administrator's ability to change a
        [private channel's permissions](/help/channel-permissions#private-channels)
        depends on them being subscribed to the channel.

        **Changes**: Before Zulip 10.0 (feature level 362), channel privacy could not be
        edited for archived channels.

        Removed `stream_post_policy` and `is_announcement_only`
        parameters in Zulip 10.0 (feature level 333), as permission to post
        in the channel is now controlled by `can_send_message_group`.

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        description : typing.Optional[str]
            The new [description](/help/change-the-channel-description) for
            the channel, in [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format.

            Clients should use the `max_stream_description_length` returned
            by the [`POST /register`](/api/register-queue) endpoint to
            determine the maximum channel description length.

            **Changes**: Removed unnecessary JSON-encoding of this parameter in
            Zulip 4.0 (feature level 64).

        new_name : typing.Optional[str]
            The new name for the channel.

            Clients should use the `max_stream_name_length` returned by the
            [`POST /register`](/api/register-queue) endpoint to determine
            the maximum channel name length.

            **Changes**: Removed unnecessary JSON-encoding of this parameter in
            Zulip 4.0 (feature level 64).

        is_private : typing.Optional[bool]
            Change whether the channel is a private channel.

        is_web_public : typing.Optional[bool]
            Change whether the channel is a web-public channel.

            Note that creating web-public channels requires the
            `WEB_PUBLIC_STREAMS_ENABLED` [server setting][server-settings]
            to be enabled on the Zulip server in question, the organization
            to have enabled the `enable_spectator_access` realm setting, and
            the current use to have permission under the organization's
            `can_create_web_public_channel_group` realm setting.

            [server-settings]: https://zulip.readthedocs.io/en/stable/production/settings.html

            **Changes**: New in Zulip 5.0 (feature level 98).

        history_public_to_subscribers : typing.Optional[bool]
            Whether the channel's message history should be available to
            newly subscribed members, or users can only access messages
            they actually received while subscribed to the channel.

            Corresponds to the shared history option for
            [private channels](/help/channel-permissions#private-channels).

            It's an error for this parameter to be false for a public or
            web-public channel and when is_private is false.

            This can only be `false` if `can_create_topic_group` for the channel
            is the `role:everyone` [system group][system-groups].

            **Changes**: Before Zulip 6.0 (feature level 136), `history_public_to_subscribers`
            was silently ignored unless the request also contained either `is_private` or
            `is_web_public`.

            [system-groups]: /api/group-setting-values#system-groups

        is_default_stream : typing.Optional[bool]
            Add or remove the channel as a [default channel][default-channel]
            for new users joining the organization.

            [default-channel]: /help/set-default-channels-for-new-users

            **Changes**: New in Zulip 8.0 (feature level 200). Previously, default channel status
            could only be changed using the [dedicated API endpoint](/api/add-default-stream).

        message_retention_days : typing.Optional[MessageRetentionDays]

        default_push_notifications : typing.Optional[DefaultPushNotifications]

        is_archived : typing.Optional[bool]
            A boolean indicating whether the channel is
            [archived](/help/archive-a-channel) or
            unarchived. Currently only allows unarchiving
            previously archived channels.

            **Changes**: New in Zulip 11.0 (feature level 388).

        folder_id : typing.Optional[int]
            ID of the new [channel folder](/help/channel-folders) to which the
            channel should belong.

            A `null` value indicates the user wants to remove the channel from its
            current channel folder.

            **Changes**: New in Zulip 11.0 (feature level 389).

        topics_policy : typing.Optional[TopicsPolicy]

        can_add_subscribers_group : typing.Optional[UpdateStreamRequestCanAddSubscribersGroup]
            The set of users who have permission to add subscribers to this
            channel expressed as an [update to a group-setting
            value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Users who can administer the channel or have similar realm-level
            permissions can add subscribers to a public channel regardless
            of the value of this setting.

            Users in this group need not be subscribed to a private channel to
            add subscribers to it.

            Note that a user must [have content access](/help/channel-permissions)
            to a channel and permission to administer the channel in order to
            modify this setting.

            **Changes**: New in Zulip 10.0 (feature level 342). Previously, there was no
            channel-level setting for this permission.

        can_remove_subscribers_group : typing.Optional[UpdateStreamRequestCanRemoveSubscribersGroup]
            The set of users who have permission to unsubscribe others from this
            channel expressed as an [update to a group-setting value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Organization administrators can unsubscribe others from a channel as though
            they were in this group without being explicitly listed here.

            Note that a user must have metadata access to a channel and permission
            to administer the channel in order to modify this setting.

            **Changes**: Prior to Zulip 10.0 (feature level 349), channel administrators
            could not unsubscribe other users if they were not an organization
            administrator or part of `can_remove_subscribers_group`. Realm administrators
            were not allowed to unsubscribe other users from a private channel if they
            were not subscribed to that channel.

            Prior to Zulip 10.0 (feature level 320), this value was always the integer
            ID of a system group.

            Before Zulip 8.0 (feature level 197), the `can_remove_subscribers_group`
            setting was named `can_remove_subscribers_group_id`.

            New in Zulip 7.0 (feature level 161).

        can_administer_channel_group : typing.Optional[UpdateStreamRequestCanAdministerChannelGroup]
            The set of users who have permission to administer this channel
            expressed as an [update to a group-setting value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Organization administrators can administer every channel as though they were
            in this group without being explicitly listed here.

            Note that a user must [have content access](/help/channel-permissions) to a
            channel in order to add other subscribers to the channel.

            **Changes**: Prior to Zulip 10.0 (feature level 349) a user needed to
            [have content access](/help/channel-permissions) to a channel in order
            to modify it. The exception to this rule was that organization
            administrators can edit channel names and descriptions without having
            full access to the channel.

            New in Zulip 10.0 (feature level 325). Prior to this
            change, the permission to administer channels was limited to realm
            administrators.

        can_delete_any_message_group : typing.Optional[UpdateStreamRequestCanDeleteAnyMessageGroup]
            The set of users who have permission to delete any message in the channel
            expressed as an [update to a group-setting value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Note that a user must [have content access](/help/channel-permissions) to a
            channel in order to delete any message in the channel.

            Users present in the organization-level `can_delete_any_message_group` setting
            can always delete any message in the channel if they
            [have content access](/help/channel-permissions) to that channel.

            **Changes**: New in Zulip 11.0 (feature level 407). Prior to this
            change, only the users in `can_delete_any_message_group` were able
            delete any message in the organization.

        can_delete_own_message_group : typing.Optional[UpdateStreamRequestCanDeleteOwnMessageGroup]
            The set of users who have permission to delete the messages that they have
            sent in the channel expressed as an [update to a group-setting value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Note that a user must [have content access](/help/channel-permissions) to a
            channel in order to delete their own message in the channel.

            Users with permission to delete any message in the channel
            and users present in the organization-level `can_delete_own_message_group` setting
            can always delete their own messages in the channel if they
            [have content access](/help/channel-permissions) to that channel.

            **Changes**: New in Zulip 11.0 (feature level 407). Prior to this
            change, only the users in the organization-level `can_delete_any_message_group`
            and `can_delete_own_message_group` settings were able delete their own messages in
            the organization.

        can_move_messages_out_of_channel_group : typing.Optional[UpdateStreamRequestCanMoveMessagesOutOfChannelGroup]
            The set of users who have permission to move messages out of this channel
            expressed as an [update to a group-setting value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Note that a user must [have content access](/help/channel-permissions) to a
            channel in order to move messages out of the channel.

            Channel administrators and users present in the organization-level
            `can_move_messages_between_channels_group` setting can always move messages
            out of the channel if they [have content access](/help/channel-permissions) to
            the channel.

            **Changes**: New in Zulip 11.0 (feature level 396). Prior to this
            change, only the users in `can_move_messages_between_channels_group` were able
            move messages between channels.

        can_move_messages_within_channel_group : typing.Optional[UpdateStreamRequestCanMoveMessagesWithinChannelGroup]
            The set of users who have permission to move messages within this channel
            expressed as an [update to a group-setting value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Note that a user must [have content access](/help/channel-permissions) to a
            channel in order to move messages within the channel.

            Channel administrators and users present in the organization-level
            `can_move_messages_between_topics_group` setting can always move messages
            within the channel if they [have content access](/help/channel-permissions) to
            the channel.

            **Changes**: New in Zulip 11.0 (feature level 396). Prior to this
            change, only the users in `can_move_messages_between_topics_group` were able
            move messages between topics of a channel.

        can_send_message_group : typing.Optional[UpdateStreamRequestCanSendMessageGroup]
            The set of users who have permission to post in this channel
            expressed as an [update to a group-setting value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Note that a user must have metadata access to a channel and permission
            to administer the channel in order to modify this setting.

            Note that using this permission to send a message to a new topic requires
            also having permission to create new topics in the channel.

            **Changes**: New in Zulip 10.0 (feature level 333). Previously
            `stream_post_policy` field used to control the permission to
            post in the channel.

        can_subscribe_group : typing.Optional[UpdateStreamRequestCanSubscribeGroup]
            The set of users who have permission to subscribe themselves to this channel
            expressed as an [update to a group-setting value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Everyone, excluding guests, can subscribe to any public channel
            irrespective of this setting.

            Users in this group can subscribe to a private channel as well.

            Note that a user must [have content access](/help/channel-permissions)
            to a channel and permission to administer the channel in order to
            modify this setting.

            **Changes**: New in Zulip 10.0 (feature level 357).

        can_resolve_topics_group : typing.Optional[UpdateStreamRequestCanResolveTopicsGroup]
            The set of users who have permission to resolve topics in this channel
            expressed as an [update to a group-setting value][update-group-setting].

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values

            Users who have similar realm-level permissions can resolve topics
            in a channel regardless of the value of this setting.

            **Changes**: New in Zulip 11.0 (feature level 402).

        can_create_topic_group : typing.Optional[UpdateStreamRequestCanCreateTopicGroup]
            The set of users who have permission to create new topics in this channel
            expressed as an [update to a group-setting value][update-group-setting].

            Note that using this permission requires also having permission to send
            messages in the channel.

            For [private channels with protected history](/help/channel-permissions#private-channels),
            this setting can only be set to `role:everyone` [system group][system-groups].

            **Changes**: New in Zulip 12.0 (feature level 441). Previously, if you
            could send messages in a channel, you could create topics in the channel.

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values
            [system-groups]: /api/group-setting-values#system-groups

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.update_stream(
                stream_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_stream(
            stream_id,
            description=description,
            new_name=new_name,
            is_private=is_private,
            is_web_public=is_web_public,
            history_public_to_subscribers=history_public_to_subscribers,
            is_default_stream=is_default_stream,
            message_retention_days=message_retention_days,
            default_push_notifications=default_push_notifications,
            is_archived=is_archived,
            folder_id=folder_id,
            topics_policy=topics_policy,
            can_add_subscribers_group=can_add_subscribers_group,
            can_remove_subscribers_group=can_remove_subscribers_group,
            can_administer_channel_group=can_administer_channel_group,
            can_delete_any_message_group=can_delete_any_message_group,
            can_delete_own_message_group=can_delete_own_message_group,
            can_move_messages_out_of_channel_group=can_move_messages_out_of_channel_group,
            can_move_messages_within_channel_group=can_move_messages_within_channel_group,
            can_send_message_group=can_send_message_group,
            can_subscribe_group=can_subscribe_group,
            can_resolve_topics_group=can_resolve_topics_group,
            can_create_topic_group=can_create_topic_group,
            request_options=request_options,
        )
        return _response.data

    async def get_stream_email_address(
        self,
        stream_id: int,
        *,
        sender_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetStreamEmailAddressResponse:
        """
        Get email address of a channel.

        Note that only users with permission to post messages in the channel
        can access the channel's email address.

        **Changes**: Prior to Zulip 12.0 (feature level 448), users without
        permission to post messages in the channel could access the channel's email
        if they had metadata access.

        New in Zulip 8.0 (feature level 226).

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        sender_id : typing.Optional[int]
            The ID of a user or bot which should appear as the sender when messages
            are sent to the channel using the returned channel email address.

            `sender_id` can be:

            - ID of the current user.
            - ID of the Email gateway bot. (Default value)
            - ID of a bot owned by the current user.

            **Changes**: New in Zulip 10.0 (feature level 335).

            Previously, the sender was always Email gateway bot.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStreamEmailAddressResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.get_stream_email_address(
                stream_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_stream_email_address(
            stream_id, sender_id=sender_id, request_options=request_options
        )
        return _response.data

    async def delete_topic(
        self, stream_id: int, *, topic_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteTopicResponse:
        """
        Delete all messages in a topic.

        Topics are a field on messages (not an independent data structure), so
        deleting all the messages in the topic deletes the topic from Zulip.

        Because this endpoint deletes messages in batches, it is possible for
        the request to time out after only deleting some messages in the topic.
        When this happens, the `complete` boolean field in the success response
        will be `false`. Clients should repeat the request when handling such a
        response. If all messages in the topic were deleted, then the success
        response will return `"complete": true`.

        **Changes**: Before Zulip 9.0 (feature level 256), the server never sent
        [`stream` op: `update`](/api/get-events#stream-update) events with an
        updated `first_message_id` for a channel when the oldest message that
        had been sent to it changed.

        Before Zulip 8.0 (feature level 211), if the server's
        processing was interrupted by a timeout, but some messages in the topic
        were deleted, then it would return `"result": "partially_completed"`,
        along with a `code` field for an error string, in the success response
        to indicate that there was a timeout and that the client should repeat
        the request.

        As of Zulip 6.0 (feature level 154), instead of returning an error
        response when a request times out after successfully deleting some of
        the messages in the topic, a success response is returned with
        `"result": "partially_completed"` to indicate that some messages were
        deleted.

        Before Zulip 6.0 (feature level 147), this request did a single atomic
        operation, which could time out for very large topics. As of this
        feature level, messages are deleted in batches, starting with the newest
        messages, so that progress is made even if the request times out and
        returns an error.

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        topic_name : str
            The name of the topic to delete.

            Note: When the value of `realm_empty_topic_display_name` found in
            the [POST /register](/api/register-queue) response is used for this
            parameter, it is interpreted as an empty string.

            **Changes**: Before Zulip 10.0 (feature level 334), empty string
            was not a valid topic name for channel messages.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTopicResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.delete_topic(
                stream_id=1,
                topic_name="new coffee machine",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_topic(
            stream_id, topic_name=topic_name, request_options=request_options
        )
        return _response.data

    async def create_channel(
        self,
        *,
        name: str,
        subscribers: typing.Sequence[int],
        description: typing.Optional[str] = OMIT,
        announce: typing.Optional[bool] = OMIT,
        invite_only: typing.Optional[bool] = OMIT,
        is_web_public: typing.Optional[bool] = OMIT,
        is_default_stream: typing.Optional[bool] = OMIT,
        folder_id: typing.Optional[int] = OMIT,
        topics_policy: typing.Optional[TopicsPolicy] = OMIT,
        history_public_to_subscribers: typing.Optional[HistoryPublicToSubscribers] = OMIT,
        message_retention_days: typing.Optional[MessageRetentionDays] = OMIT,
        can_add_subscribers_group: typing.Optional[ChannelCanAddSubscribersGroup] = OMIT,
        can_create_topic_group: typing.Optional[CanCreateTopicGroup] = OMIT,
        can_delete_any_message_group: typing.Optional[CanDeleteAnyMessageGroup] = OMIT,
        can_delete_own_message_group: typing.Optional[CanDeleteOwnMessageGroup] = OMIT,
        can_remove_subscribers_group: typing.Optional[CanRemoveSubscribersGroup] = OMIT,
        can_administer_channel_group: typing.Optional[CanAdministerChannelGroup] = OMIT,
        can_move_messages_out_of_channel_group: typing.Optional[CanMoveMessagesOutOfChannelGroup] = OMIT,
        can_move_messages_within_channel_group: typing.Optional[CanMoveMessagesWithinChannelGroup] = OMIT,
        can_send_message_group: typing.Optional[CanSendMessageGroup] = OMIT,
        can_subscribe_group: typing.Optional[CanSubscribeGroup] = OMIT,
        can_resolve_topics_group: typing.Optional[CanResolveTopicsGroup] = OMIT,
        default_push_notifications: typing.Optional[DefaultPushNotifications] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateChannelResponse:
        """
        Create a new [channel](/help/create-channels), and optionally subscribe
        users to the newly created channel.

        The initial [channel settings](/api/update-stream) will be determined
        by the optional parameters, like `invite_only`, detailed below.

        **Changes**: New in Zulip 11.0 (feature level 417). Previously, this was
        only possible via the [`POST /api/subscribe`](/api/subscribe) endpoint,
        which handles both channel subscription and creation.

        Parameters
        ----------
        name : str
            The name of the new channel.

            Clients should use the `max_stream_name_length` returned by the
            [`POST /register`](/api/register-queue) endpoint to determine
            the maximum channel name length.

        subscribers : typing.Sequence[int]
            A list of user IDs of the users to be subscribed to the new channel.

        description : typing.Optional[str]
            The [description](/help/change-the-channel-description)
            to use for the new channel being created, in text/markdown format.

            Clients should use the `max_stream_description_length` returned
            by the [`POST /register`](/api/register-queue) endpoint to
            determine the maximum channel description length.

        announce : typing.Optional[bool]
            This determines whether [notification bot](/help/configure-automated-notices)
            will send an announcement about the new channel's creation.

        invite_only : typing.Optional[bool]
            This parameter and the ones that follow are used to request an initial
            configuration of the new channel.

            This parameter determines whether the newly created channel will be
            a [private channel](/help/channel-permissions#private-channels).

        is_web_public : typing.Optional[bool]
            This parameter determines whether the newly created channel will be
            a web-public channel.

            Note that creating web-public channels requires the
            `WEB_PUBLIC_STREAMS_ENABLED` [server setting][server-settings]
            to be enabled on the Zulip server in question, the organization
            to have enabled the `enable_spectator_access` realm setting, and
            the current user to have permission under the organization's
            `can_create_web_public_channel_group` realm setting.

            [server-settings]: https://zulip.readthedocs.io/en/stable/production/settings.html

        is_default_stream : typing.Optional[bool]
            This parameter determines whether the newly created channel will be
            added as a [default channel][default-channels] for new users joining
            the organization.

            [default-channels]: /help/set-default-channels-for-new-users

        folder_id : typing.Optional[int]
            This parameter adds the newly created channel to the specified
            [channel folder](/help/channel-folders).

            **Changes**: New in Zulip 11.0 (feature level 389).

        topics_policy : typing.Optional[TopicsPolicy]

        history_public_to_subscribers : typing.Optional[HistoryPublicToSubscribers]

        message_retention_days : typing.Optional[MessageRetentionDays]

        can_add_subscribers_group : typing.Optional[ChannelCanAddSubscribersGroup]

        can_create_topic_group : typing.Optional[CanCreateTopicGroup]

        can_delete_any_message_group : typing.Optional[CanDeleteAnyMessageGroup]

        can_delete_own_message_group : typing.Optional[CanDeleteOwnMessageGroup]

        can_remove_subscribers_group : typing.Optional[CanRemoveSubscribersGroup]

        can_administer_channel_group : typing.Optional[CanAdministerChannelGroup]

        can_move_messages_out_of_channel_group : typing.Optional[CanMoveMessagesOutOfChannelGroup]

        can_move_messages_within_channel_group : typing.Optional[CanMoveMessagesWithinChannelGroup]

        can_send_message_group : typing.Optional[CanSendMessageGroup]

        can_subscribe_group : typing.Optional[CanSubscribeGroup]

        can_resolve_topics_group : typing.Optional[CanResolveTopicsGroup]

        default_push_notifications : typing.Optional[DefaultPushNotifications]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateChannelResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.create_channel(
                name="music",
                subscribers=[17, 12],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_channel(
            name=name,
            subscribers=subscribers,
            description=description,
            announce=announce,
            invite_only=invite_only,
            is_web_public=is_web_public,
            is_default_stream=is_default_stream,
            folder_id=folder_id,
            topics_policy=topics_policy,
            history_public_to_subscribers=history_public_to_subscribers,
            message_retention_days=message_retention_days,
            can_add_subscribers_group=can_add_subscribers_group,
            can_create_topic_group=can_create_topic_group,
            can_delete_any_message_group=can_delete_any_message_group,
            can_delete_own_message_group=can_delete_own_message_group,
            can_remove_subscribers_group=can_remove_subscribers_group,
            can_administer_channel_group=can_administer_channel_group,
            can_move_messages_out_of_channel_group=can_move_messages_out_of_channel_group,
            can_move_messages_within_channel_group=can_move_messages_within_channel_group,
            can_send_message_group=can_send_message_group,
            can_subscribe_group=can_subscribe_group,
            can_resolve_topics_group=can_resolve_topics_group,
            default_push_notifications=default_push_notifications,
            request_options=request_options,
        )
        return _response.data

    async def create_channel_folder(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateChannelFolderResponse:
        """
        Create a new [channel folder](/help/channel-folders).

        **Changes**: New in Zulip 11.0 (feature level 389).

        Parameters
        ----------
        name : str
            The name of the channel folder.

            Clients should use the `max_channel_folder_name_length` returned
            by the [`POST /register`](/api/register-queue) endpoint to determine
            the maximum channel folder name length.

            Value cannot be an empty string.

        description : typing.Optional[str]
            The description of the channel folder.

            Clients should use the `max_channel_folder_description_length`
            returned by the [`POST /register`](/api/register-queue) endpoint
            to determine the maximum channel folder description length.

            Note that this parameter must be passed as part of the request,
            but can be an empty string if no description for the new channel
            folder is desired.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateChannelFolderResponse
            A success response containing the unique ID of the channel folder.
            This field provides a straightforward way to reference the
            newly created channel folder.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.create_channel_folder(
                name="marketing",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_channel_folder(
            name=name, description=description, request_options=request_options
        )
        return _response.data

    async def get_channel_folders(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetChannelFoldersResponse:
        """
        Fetches all of the [channel folders](/help/channel-folders) in the
        organization, sorted by the `order` field.

        **Changes**: Before Zulip 11.0 (feature level 414), the list of channel
        folders was sorted by ID as the `order` field didn't exist.

        New in Zulip 11.0 (feature level 389).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChannelFoldersResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.get_channel_folders()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_channel_folders(request_options=request_options)
        return _response.data

    async def patch_channel_folders(
        self, *, order: typing.Sequence[int], request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Reorder the [channel folders](/help/channel-folders) in the user's
        organization.

        Channel folders are displayed in Zulip UI in order; this endpoint allows
        administrative settings UI to change the ordering of channel folders.

        This endpoint is used to implement the dragging feature described in the
        [manage channel folders documentation](/help/manage-channel-folders).

        **Changes**: New in Zulip 11.0 (feature level 414).

        Parameters
        ----------
        order : typing.Sequence[int]
            A list of channel folder IDs representing the new order.

            This list must include the IDs of [all the organization's channel
            folders](/api/get-channel-folders), including archived folders.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.patch_channel_folders(
                order=[2, 1],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_channel_folders(order=order, request_options=request_options)
        return _response.data

    async def update_channel_folder(
        self,
        channel_folder_id: int,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Update the name or description of a [channel folder](/help/channel-folders)
        with the specified ID.

        This endpoint is also used to archive or unarchive the specified channel
        folder.

        **Changes**: New in Zulip 11.0 (feature level 389).

        Parameters
        ----------
        channel_folder_id : int
            The ID of the target channel folder.

        name : typing.Optional[str]
            The new name of the channel folder.

            Clients should use the `max_channel_folder_name_length` returned
            by the [`POST /register`](/api/register-queue) endpoint to determine
            the maximum channel folder name length.

            Value cannot be an empty string.

        description : typing.Optional[str]
            The new description of the channel folder.

            Clients should use the `max_channel_folder_description_length`
            returned by the [`POST /register`](/api/register-queue) endpoint
            to determine the maximum channel folder description length.

        is_archived : typing.Optional[bool]
            Whether to archive or unarchive the channel folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.update_channel_folder(
                channel_folder_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_channel_folder(
            channel_folder_id,
            name=name,
            description=description,
            is_archived=is_archived,
            request_options=request_options,
        )
        return _response.data

    async def create_big_blue_button_video_call(
        self,
        *,
        meeting_name: str,
        voice_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateBigBlueButtonVideoCallResponse:
        """
        Create a video call URL for a BigBlueButton video call.
        Requires [BigBlueButton 2.4+](/integrations/big-blue-button)
        to be configured on the Zulip server.

        The acting user will be given the moderator role on the call.

        **Changes**: Prior to Zulip 10.0 (feature level 337), every
        user was given the moderator role on BigBlueButton calls, via
        encoding a moderator password in the generated URLs.

        Parameters
        ----------
        meeting_name : str
            Meeting name for the BigBlueButton video call.

        voice_only : typing.Optional[bool]
            Configures whether the call is voice-only; if true,
            disables cameras for all users. Only the call
            creator/moderator can edit this configuration.

            **Changes**: New in Zulip 10.0 (feature level 337).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateBigBlueButtonVideoCallResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.create_big_blue_button_video_call(
                meeting_name="test_channel meeting",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_big_blue_button_video_call(
            meeting_name=meeting_name, voice_only=voice_only, request_options=request_options
        )
        return _response.data

    async def create_nextcloud_talk_video_call(
        self, *, room_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateNextcloudTalkVideoCallResponse:
        """
        Create a video call URL for a Nextcloud Talk video call. Requires
        [Nextcloud Talk](/integrations/nextcloud-talk) to be configured on the
        Zulip server.

        **Changes**: New in Zulip 12.0 (feature level 465).

        Parameters
        ----------
        room_name : str
            Room name for the Nextcloud Talk conversation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateNextcloudTalkVideoCallResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.create_nextcloud_talk_video_call(
                room_name="#Test > team check-in",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_nextcloud_talk_video_call(
            room_name=room_name, request_options=request_options
        )
        return _response.data

    async def create_webex_video_call(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateWebexVideoCallResponse:
        """
        Create a video call URL for a Webex video call.

        Requires [Webex integration](/integrations/webex) to be configured
        on the Zulip server.

        Clients should confirm that the user has completed the OAuth process
        with Webex and has a Webex token before attempting to create a video
        call URL. See the `has_webex_token` field in the [`POST /register`
        response](/api/register-queue), as well as the [`has_webex_token`
        event type](/api/get-events#has_webex_token).

        **Changes**: New in Zulip 12.0 (feature level 493).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWebexVideoCallResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.create_webex_video_call()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_webex_video_call(request_options=request_options)
        return _response.data

    async def create_constructor_groups_video_call(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateConstructorGroupsVideoCallResponse:
        """
        Create a video call URL for a Constructor Groups video call.
        Requires [Constructor Groups](/integrations/constructor-groups)
        to be configured on the Zulip server.

        **Changes**: New in Zulip 12.0 (feature level 460).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateConstructorGroupsVideoCallResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.channels.create_constructor_groups_video_call()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_constructor_groups_video_call(request_options=request_options)
        return _response.data
