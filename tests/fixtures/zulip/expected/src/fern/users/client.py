

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ignored_parameters_success import IgnoredParametersSuccess
from ..types.json_success import JsonSuccess
from ..types.profile_data_update import ProfileDataUpdate
from .raw_client import AsyncRawUsersClient, RawUsersClient
from .types.add_alert_words_response import AddAlertWordsResponse
from .types.create_user_group_request_can_add_members_group import CreateUserGroupRequestCanAddMembersGroup
from .types.create_user_group_request_can_join_group import CreateUserGroupRequestCanJoinGroup
from .types.create_user_group_request_can_leave_group import CreateUserGroupRequestCanLeaveGroup
from .types.create_user_group_request_can_manage_group import CreateUserGroupRequestCanManageGroup
from .types.create_user_group_request_can_mention_group import CreateUserGroupRequestCanMentionGroup
from .types.create_user_group_request_can_remove_members_group import CreateUserGroupRequestCanRemoveMembersGroup
from .types.create_user_group_response import CreateUserGroupResponse
from .types.create_user_response import CreateUserResponse
from .types.delete_avatar_response import DeleteAvatarResponse
from .types.get_alert_words_response import GetAlertWordsResponse
from .types.get_attachments_response import GetAttachmentsResponse
from .types.get_bot_api_key_response import GetBotApiKeyResponse
from .types.get_is_user_group_member_response import GetIsUserGroupMemberResponse
from .types.get_own_user_response import GetOwnUserResponse
from .types.get_user_by_email_response import GetUserByEmailResponse
from .types.get_user_group_members_response import GetUserGroupMembersResponse
from .types.get_user_group_subgroups_response import GetUserGroupSubgroupsResponse
from .types.get_user_groups_response import GetUserGroupsResponse
from .types.get_user_presence_response import GetUserPresenceResponse
from .types.get_user_response import GetUserResponse
from .types.get_user_status_response import GetUserStatusResponse
from .types.get_users_response import GetUsersResponse
from .types.regenerate_api_key_response import RegenerateApiKeyResponse
from .types.regenerate_bot_api_key_response import RegenerateBotApiKeyResponse
from .types.remove_alert_words_response import RemoveAlertWordsResponse
from .types.set_typing_status_for_message_edit_request_op import SetTypingStatusForMessageEditRequestOp
from .types.set_typing_status_request_op import SetTypingStatusRequestOp
from .types.set_typing_status_request_type import SetTypingStatusRequestType
from .types.update_presence_request_status import UpdatePresenceRequestStatus
from .types.update_presence_response import UpdatePresenceResponse
from .types.update_settings_request_resolved_topic_notice_auto_read_policy import (
    UpdateSettingsRequestResolvedTopicNoticeAutoReadPolicy,
)
from .types.update_settings_request_target_users import UpdateSettingsRequestTargetUsers
from .types.update_settings_request_web_animate_image_previews import UpdateSettingsRequestWebAnimateImagePreviews
from .types.update_user_group_request_can_add_members_group import UpdateUserGroupRequestCanAddMembersGroup
from .types.update_user_group_request_can_join_group import UpdateUserGroupRequestCanJoinGroup
from .types.update_user_group_request_can_leave_group import UpdateUserGroupRequestCanLeaveGroup
from .types.update_user_group_request_can_manage_group import UpdateUserGroupRequestCanManageGroup
from .types.update_user_group_request_can_mention_group import UpdateUserGroupRequestCanMentionGroup
from .types.update_user_group_request_can_remove_members_group import UpdateUserGroupRequestCanRemoveMembersGroup
from .types.upload_avatar_response import UploadAvatarResponse


OMIT = typing.cast(typing.Any, ...)


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsersClient
        """
        return self._raw_client

    def get_attachments(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetAttachmentsResponse:
        """
        Fetch metadata on files uploaded by the requesting user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAttachmentsResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.get_attachments()
        """
        _response = self._raw_client.get_attachments(request_options=request_options)
        return _response.data

    def remove_attachment(
        self, attachment_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Delete an uploaded file given its attachment ID.

        Note that uploaded files that have been referenced in at least
        one message are automatically deleted once the last message
        containing a link to them is deleted (whether directly or via
        a [message retention policy](/help/message-retention-policy)).

        Uploaded files that are never used in a message are
        automatically deleted a few weeks after being uploaded.

        Attachment IDs can be contained from [GET /attachments](/api/get-attachments).

        Parameters
        ----------
        attachment_id : int
            The ID of the attachment to be deleted.

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
        client.users.remove_attachment(
            attachment_id=1,
        )
        """
        _response = self._raw_client.remove_attachment(attachment_id, request_options=request_options)
        return _response.data

    def get_users(
        self,
        *,
        client_gravatar: typing.Optional[bool] = None,
        include_custom_profile_fields: typing.Optional[bool] = None,
        user_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUsersResponse:
        """
        Retrieve details on users in the organization.

        By default, returns all accessible users in the organization.
        The `user_ids` query parameter can be used to limit the
        results to a specific set of user IDs.

        Optionally includes values of [custom profile fields](/help/custom-profile-fields).

        You can also [fetch details on a single user](/api/get-user).

        **Changes**: In Zulip 12.0 (feature level 437), fixed a bug
        dating to feature level 232, which caused guest users to
        receive fake backwards-compatibility users in the format
        intended for clients using `POST /register` without the
        `user_list_incomplete` client capability.

        This endpoint did not support unauthenticated
        access in organizations using the [public access
        option](/help/public-access-option) prior to Zulip 11.0
        (feature level 387).

        Parameters
        ----------
        client_gravatar : typing.Optional[bool]
            Whether the client supports computing gravatars URLs. If
            enabled, `avatar_url` will be included in the response only
            if there is a Zulip avatar, and will be `null` for users who
            are using gravatar as their avatar. This option
            significantly reduces the compressed size of user data,
            since gravatar URLs are long, random strings and thus do not
            compress well. The `client_gravatar` field is set to `true` if
            clients can compute their own gravatars.

            **Changes**: The default value of this parameter was `false`
            prior to Zulip 5.0 (feature level 92).

        include_custom_profile_fields : typing.Optional[bool]
            Whether the client wants [custom profile field](/help/custom-profile-fields)
            data to be included in the response.

            **Changes**: New in Zulip 2.1.0. Previous versions do not offer these
            data via the API.

        user_ids : typing.Optional[str]
            Limits the results to the specified user IDs. If not
            provided, the server will return all accessible users in
            the organization.

            **Changes**: New in Zulip 11.0 (feature level 384).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUsersResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.get_users()
        """
        _response = self._raw_client.get_users(
            client_gravatar=client_gravatar,
            include_custom_profile_fields=include_custom_profile_fields,
            user_ids=user_ids,
            request_options=request_options,
        )
        return _response.data

    def create_user(
        self, *, email: str, password: str, full_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateUserResponse:
        """
        Create a new user account via the API.

        !!! warn ""

            **Note**: On Zulip Cloud, this feature is available only for
            organizations on a [Zulip Cloud Standard](https://zulip.com/plans/)
            or [Zulip Cloud Plus](https://zulip.com/plans/) plan. Administrators
            can request the required `can_create_users` permission for a bot or
            user by contacting [Zulip Cloud support][support] with an
            explanation for why it is needed. Self-hosted installations can
            toggle `can_create_users` on an account using the `manage.py
            change_user_role` [management command][management-commands].

        **Changes**: Before Zulip 4.0 (feature level 36), this endpoint was
        available to all organization administrators.

        [support]: /help/contact-support
        [management-commands]: https://zulip.readthedocs.io/en/latest/production/management-commands.html

        Parameters
        ----------
        email : str
            The email address of the new user.

        password : str
            The password of the new user.

        full_name : str
            The full name of the new user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateUserResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.create_user(
            email="username@example.com",
            password="abcd1234",
            full_name="New User",
        )
        """
        _response = self._raw_client.create_user(
            email=email, password=password, full_name=full_name, request_options=request_options
        )
        return _response.data

    def reactivate_user(self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> JsonSuccess:
        """
        [Reactivates a
        user](https://zulip.com/help/deactivate-or-reactivate-a-user)
        given their user ID.

        Parameters
        ----------
        user_id : int
            The target user's ID.

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
        client.users.reactivate_user(
            user_id=1,
        )
        """
        _response = self._raw_client.reactivate_user(user_id, request_options=request_options)
        return _response.data

    def get_user_status(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserStatusResponse:
        """
        Get the [status](/help/status-and-availability) currently set by a
        user in the organization.

        **Changes**: New in Zulip 9.0 (feature level 262). Previously,
        user statuses could only be fetched via the [`POST
        /register`](/api/register-queue) endpoint.

        Parameters
        ----------
        user_id : int
            The target user's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserStatusResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.get_user_status(
            user_id=1,
        )
        """
        _response = self._raw_client.get_user_status(user_id, request_options=request_options)
        return _response.data

    def update_status_for_user(
        self,
        user_id: int,
        *,
        status_text: typing.Optional[str] = OMIT,
        emoji_name: typing.Optional[str] = OMIT,
        emoji_code: typing.Optional[str] = OMIT,
        reaction_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Administrator endpoint for changing the [status](/help/status-and-availability) of
        another user.

        **Changes**: Prior to Zulip 12.0 (feature level 473), only
        bots could not access this API endpoint, regardless of the
        role of the bot.

        New in Zulip 11.0 (feature level 407).

        Parameters
        ----------
        user_id : int
            The target user's ID.

        status_text : typing.Optional[str]
            The text content of the status message. Sending the empty string
            will clear the user's status.

            **Note**: The limit on the size of the message is 60 Unicode code points.

        emoji_name : typing.Optional[str]
            The name for the emoji to associate with this status.

            **Changes**: New in Zulip 5.0 (feature level 86).

        emoji_code : typing.Optional[str]
            A unique identifier, defining the specific emoji codepoint requested,
            within the namespace of the `reaction_type`.

            **Changes**: New in Zulip 5.0 (feature level 86).

        reaction_type : typing.Optional[str]
            A string indicating the type of emoji. Each emoji `reaction_type`
            has an independent namespace for values of `emoji_code`.

            Must be one of the following values:

            - `unicode_emoji` : In this namespace, `emoji_code` will be a
              dash-separated hex encoding of the sequence of Unicode codepoints
              that define this emoji in the Unicode specification.

            - `realm_emoji` : In this namespace, `emoji_code` will be the ID of
              the uploaded [custom emoji](/help/custom-emoji).

            - `zulip_extra_emoji` : These are special emoji included with Zulip.
              In this namespace, `emoji_code` will be the name of the emoji (e.g.
              "zulip").

            **Changes**: New in Zulip 5.0 (feature level 86).

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
        client.users.update_status_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.update_status_for_user(
            user_id,
            status_text=status_text,
            emoji_name=emoji_name,
            emoji_code=emoji_code,
            reaction_type=reaction_type,
            request_options=request_options,
        )
        return _response.data

    def get_user_presence(
        self, user_id_or_email: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserPresenceResponse:
        """
        Get the presence status for a specific user.

        This endpoint is most useful for embedding data about a user's
        presence status in other sites (e.g. an employee directory). Full
        Zulip clients like mobile/desktop apps will want to use the [main
        presence endpoint](/api/get-presence), which returns data for all
        active users in the organization, instead.

        Parameters
        ----------
        user_id_or_email : str
            The ID or Zulip API email address of the user whose presence you want to fetch.

            **Changes**: New in Zulip 4.0 (feature level 43). Previous versions only supported
            identifying the user by Zulip API email.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserPresenceResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.get_user_presence(
            user_id_or_email="iago@zulip.com",
        )
        """
        _response = self._raw_client.get_user_presence(user_id_or_email, request_options=request_options)
        return _response.data

    def get_own_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetOwnUserResponse:
        """
        Get basic data about the user/bot that requests this endpoint.

        **Changes**: Removed `is_billing_admin` field in Zulip 10.0 (feature level 363), as it was
        replaced by the `can_manage_billing_group` realm setting.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetOwnUserResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.get_own_user()
        """
        _response = self._raw_client.get_own_user(request_options=request_options)
        return _response.data

    def deactivate_own_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> JsonSuccess:
        """
        Deactivates the current user's account. See also the administrative endpoint for
        [deactivating another user](/api/deactivate-user).

        This endpoint is primarily useful to Zulip clients providing a user settings UI.

        Parameters
        ----------
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
        client.users.deactivate_own_user()
        """
        _response = self._raw_client.deactivate_own_user(request_options=request_options)
        return _response.data

    def regenerate_api_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RegenerateApiKeyResponse:
        """
        !!! warn ""

             **Note**: Users should treat their Zulip API key as
             [carefully as they would their password](/help/protect-your-account).

        Generate a new API key for the user making the request.

        Changing a user's API key will immediately log them out of Zulip
        on devices registered for [mobile push notifications][mobile-push].

        **Changes**: Before Zulip 12.0 (feature level 492),
        regenerating a user's API key didn't remove all of the user's
        [E2EE push device registrations](/api/register-push-device),
        so E2EE push notifications could still be sent.

        [mobile-push]: https://zulip.readthedocs.io/en/latest/production/mobile-push-notifications.html

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegenerateApiKeyResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.regenerate_api_key()
        """
        _response = self._raw_client.regenerate_api_key(request_options=request_options)
        return _response.data

    def get_alert_words(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetAlertWordsResponse:
        """
        Get all of the user's configured [alert words][alert-words].

        [alert-words]: /help/dm-mention-alert-notifications#alert-words

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAlertWordsResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.get_alert_words()
        """
        _response = self._raw_client.get_alert_words(request_options=request_options)
        return _response.data

    def add_alert_words(
        self, *, alert_words: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> AddAlertWordsResponse:
        """
        Add words (or phrases) to the user's set of configured [alert words][alert-words].

        [alert-words]: /help/dm-mention-alert-notifications#alert-words

        Parameters
        ----------
        alert_words : typing.Sequence[str]
            An array of strings to be added to the user's set of configured
            alert words. Strings already present in the user's set of alert words
            already are ignored.

            Alert words are case insensitive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddAlertWordsResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.add_alert_words(
            alert_words=["foo", "bar"],
        )
        """
        _response = self._raw_client.add_alert_words(alert_words=alert_words, request_options=request_options)
        return _response.data

    def remove_alert_words(
        self, *, alert_words: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> RemoveAlertWordsResponse:
        """
        Remove words (or phrases) from the user's set of configured [alert words][alert-words].

        Alert words are case insensitive.

        [alert-words]: /help/dm-mention-alert-notifications#alert-words

        Parameters
        ----------
        alert_words : typing.Sequence[str]
            An array of strings to be removed from the user's set of configured
            alert words. Strings that are not in the user's set of alert words
            are ignored.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoveAlertWordsResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.remove_alert_words(
            alert_words=["foo"],
        )
        """
        _response = self._raw_client.remove_alert_words(alert_words=alert_words, request_options=request_options)
        return _response.data

    def update_presence(
        self,
        *,
        status: UpdatePresenceRequestStatus,
        last_update_id: typing.Optional[int] = OMIT,
        history_limit_days: typing.Optional[int] = OMIT,
        new_user_input: typing.Optional[bool] = OMIT,
        ping_only: typing.Optional[bool] = OMIT,
        slim_presence: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdatePresenceResponse:
        """
        Update the current user's [presence][availability] and fetch presence data
        of other users in the organization.

        This endpoint is meant to be used by clients for both:

        - Reporting the current user's presence status (`"active"` or `"idle"`)
          to the server.

        - Obtaining the presence data of all other users in the organization via
          regular polling.

        Accurate user presence is one of the most expensive parts of any
        chat application (in terms of bandwidth and other resources). Therefore,
        it is important that clients implementing Zulip's user presence system
        use the modern [`last_update_id`](#parameter-last_update_id) protocol to
        minimize fetching duplicate user presence data.

        Client apps implementing presence are recommended to also consume [`presence`
        events](/api/get-events#presence)), in order to learn about newly online users
        immediately.

        The Zulip server is responsible for implementing [invisible mode][invisible],
        which disables sharing a user's presence data. Nonetheless, clients
        should check the `presence_enabled` field in user objects in order to
        display the current user as online or offline based on whether they are
        sharing their presence information.

        **Changes**: As of Zulip 8.0 (feature level 228), if the
        `CAN_ACCESS_ALL_USERS_GROUP_LIMITS_PRESENCE` server-level setting is
        `true`, then user presence data in the response is [limited to users
        the current user can see/access][limit-visibility].

        [limit-visibility]: /help/guest-users#configure-whether-guests-can-see-all-other-users
        [invisible]: /help/status-and-availability#invisible-mode
        [availability]: /help/status-and-availability#availability

        Parameters
        ----------
        status : UpdatePresenceRequestStatus
            The status of the user on this client.

            Clients should report the user as `"active"` on this device if the client
            knows that the user is presently using the device (and thus would
            potentially see a notification immediately), even if the user
            has not directly interacted with the Zulip client.

            Otherwise, it should report the user as `"idle"`.

            See the related [`new_user_input`](#parameter-new_user_input) parameter
            for how a client should report whether the user is actively using the
            Zulip client.

        last_update_id : typing.Optional[int]
            The identifier that specifies what presence data the client already
            has received, which allows the server to only return more recent
            user presence data.

            This should be set to `-1` during initialization of the client in
            order to fetch all user presence data, unless the client is obtaining
            initial user presence metadata from the
            [`POST /register`](/api/register-queue) endpoint.

            In subsequent queries to this endpoint, this value should be set to the
            most recent value of `presence_last_update_id` returned by the server
            in this endpoint's response, which implements incremental fetching
            of user presence data.

            When this parameter is passed, the user presence data in the response
            will always be in the modern format.

            **Changes**: New in Zulip 9.0 (feature level 263). Previously, the
            server sent user presence data for all users who had been active in the
            last two weeks unconditionally.

        history_limit_days : typing.Optional[int]
            Limits how far back in time to fetch user presence data. If not specified,
            defaults to 14 days. A value of N means that the oldest presence data
            fetched will be from at most N days ago.

            Note that this is only useful during the initial user presence data fetch,
            as subsequent fetches should use the `last_update_id` parameter, which
            will act as the limit on how much presence data is returned. `history_limit_days`
            is ignored if `last_update_id` is passed with a value greater than `0`,
            indicating that the client already has some presence data.

            **Changes**: New in Zulip 10.0 (feature level 288).

        new_user_input : typing.Optional[bool]
            Whether the user has interacted with the client (e.g. moved the mouse,
            used the keyboard, etc.) since the previous presence request from this
            client.

            The server uses data from this parameter to implement certain [usage
            statistics](/help/analytics).

            User interface clients that might run in the background, without the
            user ever interacting with them, should be careful to only pass `true`
            if the user has actually interacted with the client in order to avoid
            corrupting usage statistics graphs.

        ping_only : typing.Optional[bool]
            Whether the client is sending a ping-only request, meaning it only
            wants to update the user's presence `status` on the server.

            Otherwise, also requests the server return user presence data for all
            users in the organization, which is further specified by the
            [`last_update_id`](#parameter-last_update_id) parameter.

        slim_presence : typing.Optional[bool]
            Legacy parameter for configuring the format (modern or legacy) in
            which the server will return user presence data for the organization.

            Modern clients should use
            [`last_update_id`](#parameter-last_update_id), which guarantees that
            user presence data will be returned in the modern format, and
            should not pass this parameter as `true` unless interacting with an
            older server.

            Legacy clients that do not yet support `last_update_id` may use the
            value of `true` to request the modern format for user presence data.

            **Note**: The legacy format for user presence data will be removed
            entirely in a future release.

            **Changes**: **Deprecated** in Zulip 9.0 (feature level 263). Using
            the modern `last_update_id` parameter is the recommended way to
            request the modern format for user presence data.

            New in Zulip 3.0 (no feature level as it was an unstable API at that
            point).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdatePresenceResponse
            Success.

        Examples
        --------
        from fern.users import UpdatePresenceRequestStatus

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.update_presence(
            status=UpdatePresenceRequestStatus.IDLE,
        )
        """
        _response = self._raw_client.update_presence(
            status=status,
            last_update_id=last_update_id,
            history_limit_days=history_limit_days,
            new_user_input=new_user_input,
            ping_only=ping_only,
            slim_presence=slim_presence,
            request_options=request_options,
        )
        return _response.data

    def remove_profile_data(
        self, *, data: typing.Sequence[int], request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Remove the current user's [profile data](/help/edit-your-profile) for
        one or more of the [custom profile fields](/help/custom-profile-fields)
        configured in the organization.

        Parameters
        ----------
        data : typing.Sequence[int]
            An array of custom profile field IDs to remove any data set for
            the user.

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
        client.users.remove_profile_data(
            data=[1],
        )
        """
        _response = self._raw_client.remove_profile_data(data=data, request_options=request_options)
        return _response.data

    def update_profile_data(
        self, *, data: typing.Sequence[ProfileDataUpdate], request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Update the current user's [profile data](/help/edit-your-profile) for
        one or more of the [custom profile fields](/help/custom-profile-fields)
        configured in the organization.

        Parameters
        ----------
        data : typing.Sequence[ProfileDataUpdate]
            An array of objects describing updates to the custom profile
            field data for the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi, ProfileDataUpdate

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.update_profile_data(
            data=[
                ProfileDataUpdate(
                    id=4,
                    value="0",
                ),
                ProfileDataUpdate(
                    id=5,
                    value="1909-04-05",
                ),
            ],
        )
        """
        _response = self._raw_client.update_profile_data(data=data, request_options=request_options)
        return _response.data

    def update_status(
        self,
        *,
        status_text: typing.Optional[str] = OMIT,
        away: typing.Optional[bool] = OMIT,
        emoji_name: typing.Optional[str] = OMIT,
        emoji_code: typing.Optional[str] = OMIT,
        reaction_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Change your [status](/help/status-and-availability).

        A request to this endpoint will only change the parameters passed.
        For example, passing just `status_text` requests a change in the status
        text, but will leave the status emoji unchanged.

        Clients that wish to set the user's status to a specific value should
        pass all supported parameters.

        **Changes**: In Zulip 5.0 (feature level 86), added support for
        `emoji_name`, `emoji_code`, and `reaction_type` parameters.

        Parameters
        ----------
        status_text : typing.Optional[str]
            The text content of the status message. Sending the empty string
            will clear the user's status.

            **Note**: The limit on the size of the message is 60 Unicode code points.

        away : typing.Optional[bool]
            Whether the user should be marked as "away".

            **Changes**: Deprecated in Zulip 6.0 (feature level 148);
            starting with that feature level, `away` is a legacy way to
            access the user's `presence_enabled` setting, with
            `away = !presence_enabled`. To be removed in a future release.

        emoji_name : typing.Optional[str]
            The name for the emoji to associate with this status.

            **Changes**: New in Zulip 5.0 (feature level 86).

        emoji_code : typing.Optional[str]
            A unique identifier, defining the specific emoji codepoint requested,
            within the namespace of the `reaction_type`.

            **Changes**: New in Zulip 5.0 (feature level 86).

        reaction_type : typing.Optional[str]
            A string indicating the type of emoji. Each emoji `reaction_type`
            has an independent namespace for values of `emoji_code`.

            Must be one of the following values:

            - `unicode_emoji` : In this namespace, `emoji_code` will be a
              dash-separated hex encoding of the sequence of Unicode codepoints
              that define this emoji in the Unicode specification.

            - `realm_emoji` : In this namespace, `emoji_code` will be the ID of
              the uploaded [custom emoji](/help/custom-emoji).

            - `zulip_extra_emoji` : These are special emoji included with Zulip.
              In this namespace, `emoji_code` will be the name of the emoji (e.g.
              "zulip").

            **Changes**: New in Zulip 5.0 (feature level 86).

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
        client.users.update_status()
        """
        _response = self._raw_client.update_status(
            status_text=status_text,
            away=away,
            emoji_name=emoji_name,
            emoji_code=emoji_code,
            reaction_type=reaction_type,
            request_options=request_options,
        )
        return _response.data

    def mute_user(self, muted_user_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> JsonSuccess:
        """
        [Mute a user](/help/mute-a-user) from the perspective of the requesting
        user. Messages sent by muted users will be automatically marked as read
        and hidden for the user who muted them.

        Muted users should be implemented by clients as follows:

        - The server will immediately mark all messages sent by the muted
          user as read. This will automatically clear any existing mobile
          push notifications related to the muted user.
        - The server will mark any new messages sent by the muted user as read
          for the requesting user's account, which prevents all email and mobile
          push notifications.
        - Clients should exclude muted users from presence lists or other UI
          for viewing or composing one-on-one direct messages. One-on-one direct
          messages sent by muted users should be hidden everywhere in the Zulip UI.
        - Channel messages and group direct messages sent by the muted
          user should avoid displaying the content and name/avatar,
          but should display that N messages by a muted user were
          hidden (so that it is possible to interpret the messages by
          other users who are talking with the muted user).
        - Group direct message conversations including the muted user
          should display muted users as "Muted user", rather than
          showing their name, in lists of such conversations, along with using
          a blank grey avatar where avatars are displayed.
        - Administrative/settings UI elements for showing "All users that exist
          on this channel or realm", e.g. for organization
          administration or showing channel subscribers, should display
          the user's name as normal.

        **Changes**: New in Zulip 4.0 (feature level 48).

        Parameters
        ----------
        muted_user_id : int
            The ID of the user to mute/unmute.

            **Changes**: Before Zulip 8.0 (feature level 188), bot users could not
            be muted/unmuted, and specifying a bot user's ID returned an error response.

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
        client.users.mute_user(
            muted_user_id=1,
        )
        """
        _response = self._raw_client.mute_user(muted_user_id, request_options=request_options)
        return _response.data

    def unmute_user(
        self, muted_user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        [Unmute a user](/help/mute-a-user#see-your-list-of-muted-users)
        from the perspective of the requesting user.

        **Changes**: New in Zulip 4.0 (feature level 48).

        Parameters
        ----------
        muted_user_id : int
            The ID of the user to mute/unmute.

            **Changes**: Before Zulip 8.0 (feature level 188), bot users could not
            be muted/unmuted, and specifying a bot user's ID returned an error response.

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
        client.users.unmute_user(
            muted_user_id=1,
        )
        """
        _response = self._raw_client.unmute_user(muted_user_id, request_options=request_options)
        return _response.data

    def add_apns_token(
        self, *, token: str, appid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        This endpoint adds an APNs device token to register for iOS push notifications.

        **Changes**: Deprecated in Zulip 11.0 (feature level 406). Clients connecting
        to newer servers and with E2EE push notifications support should use the
        [Register E2EE push device](/api/register-push-device) endpoint, as this
        endpoint will be removed in a future release.

        Parameters
        ----------
        token : str
            The token provided by the device.

        appid : str
            The ID of the Zulip app that is making the request.

            **Changes**: In Zulip 8.0 (feature level 223), this parameter was made
            required. Previously, if it was unspecified, the server would use a default
            value (based on the `ZULIP_IOS_APP_ID` server setting, which
            defaulted to `"org.zulip.Zulip"`).

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
        client.users.add_apns_token(
            token="c0ffee",
            appid="org.zulip.Zulip",
        )
        """
        _response = self._raw_client.add_apns_token(token=token, appid=appid, request_options=request_options)
        return _response.data

    def remove_apns_token(self, *, token: str, request_options: typing.Optional[RequestOptions] = None) -> JsonSuccess:
        """
        This endpoint removes an APNs device token for iOS push notifications.

        **Changes**: Deprecated in Zulip 11.0 (feature level 406) and will be
        removed in a future release. Clients connecting to newer servers and
        with E2EE push notifications support should delete the account record
        in their local accounts table that corresponds to the `push_account_id`
        supplied when registering via the [Register E2EE push device](/api/register-push-device)
        endpoint, to stop displaying notifications for that registration.

        Parameters
        ----------
        token : str
            The token provided by the device.

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
        client.users.remove_apns_token(
            token="c0ffee",
        )
        """
        _response = self._raw_client.remove_apns_token(token=token, request_options=request_options)
        return _response.data

    def add_fcm_token(self, *, token: str, request_options: typing.Optional[RequestOptions] = None) -> JsonSuccess:
        """
        This endpoint adds an FCM registration token for push notifications.

        **Changes**: Deprecated in Zulip 11.0 (feature level 406). Clients connecting
        to newer servers and with E2EE push notifications support should use the
        [Register E2EE push device](/api/register-push-device) endpoint, as this
        endpoint will be removed in a future release.

        Parameters
        ----------
        token : str
            The token provided by the device.

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
        client.users.add_fcm_token(
            token="android-token",
        )
        """
        _response = self._raw_client.add_fcm_token(token=token, request_options=request_options)
        return _response.data

    def remove_fcm_token(self, *, token: str, request_options: typing.Optional[RequestOptions] = None) -> JsonSuccess:
        """
        This endpoint removes an FCM registration token for push notifications.

        **Changes**: Deprecated in Zulip 11.0 (feature level 406) and will be
        removed in a future release. Clients connecting to newer servers and
        with E2EE push notifications support should delete the account record
        in their local accounts table that corresponds to the `push_account_id`
        supplied when registering via the [Register E2EE push device](/api/register-push-device)
        endpoint, to stop displaying notifications for that registration.

        Parameters
        ----------
        token : str
            The token provided by the device.

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
        client.users.remove_fcm_token(
            token="android-token",
        )
        """
        _response = self._raw_client.remove_fcm_token(token=token, request_options=request_options)
        return _response.data

    def upload_avatar(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> UploadAvatarResponse:
        """
        Upload a new [profile picture](/help/change-your-profile-picture)
        for the current user.

        The maximum allowed file size is available in the `max_avatar_file_size_mib`
        field in the [`POST /register`](/api/register-queue) response.

        In organizations that
        [restrict profile picture changes](/help/restrict-profile-picture-changes),
        only administrators can use this endpoint.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadAvatarResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.upload_avatar()
        """
        _response = self._raw_client.upload_avatar(file=file, request_options=request_options)
        return _response.data

    def delete_avatar(self, *, request_options: typing.Optional[RequestOptions] = None) -> DeleteAvatarResponse:
        """
        Delete the current user's uploaded [profile picture](/help/change-your-profile-picture),
        reverting to the organization's
        [default style for profile pictures](/help/configure-default-profile-pictures).

        This endpoint is idempotent: if the current user has not uploaded a
        custom profile picture, the request succeeds without making any
        changes.

        In organizations that
        [restrict profile picture changes](/help/restrict-profile-picture-changes),
        only administrators can use this endpoint.

        **Changes**: Prior to Zulip 12.0 (feature level 443), this endpoint
        was not idempotent; calling it when the current user had not
        uploaded a custom profile picture would still increment their
        avatar version and send a redundant user update event to
        clients.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAvatarResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.delete_avatar()
        """
        _response = self._raw_client.delete_avatar(request_options=request_options)
        return _response.data

    def get_user_by_email(
        self,
        email: str,
        *,
        client_gravatar: typing.Optional[bool] = None,
        include_custom_profile_fields: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUserByEmailResponse:
        """
        Fetch details for a single user in the organization given a Zulip
        API email address.

        You can also fetch details on [all users in the organization](/api/get-users)
        or [by user ID](/api/get-user).

        Fetching by user ID is generally recommended when possible,
        as a user might [change their email address](/help/change-your-email-address)
        or change their [email address visibility](/help/configure-email-visibility),
        either of which could change the client's ability to look them up by that
        email address.

        **Changes**: In Zulip 12.0 (feature level 437), fixed a bug
        dating to feature level 232, which caused guest users to
        receive fake backwards-compatibility users in the format
        intended for clients using `POST /register` without the
        `user_list_incomplete` client capability.

        Starting with Zulip 10.0 (feature level 302), the real email
        address can be used in the `email` parameter and will fetch the target user's
        data if and only if the target's email visibility setting permits the requester
        to see the email address.
        The dummy email addresses of the form `user{id}@{realm.host}` still work, and
        will now work for **all** users, via identifying them by the embedded user ID.

        New in Zulip Server 4.0 (feature level 39).

        Parameters
        ----------
        email : str
            The email address of the user to fetch. Two forms are supported:

            - The real email address of the user (`delivery_email`). The lookup will
              succeed if and only if the user exists and their email address visibility
              setting permits the client to see the email address.

            - The dummy Zulip API email address of the form `user{user_id}@{realm_host}`. This
              is identical to simply [getting user by ID](/api/get-user). If the server or
              realm change domains, the dummy email address used has to be adjustment to
              match the new realm domain. This is legacy behavior for
              backwards-compatibility, and will be removed in a future release.

            **Changes**: Starting with Zulip 10.0 (feature level 302), lookups by real email
            address match the semantics of the target's email visibility setting and dummy
            email addresses work for all users, independently of their email visibility
            setting.

            Previously, lookups were done only using the Zulip API email addresses.

        client_gravatar : typing.Optional[bool]
            Whether the client supports computing gravatars URLs. If
            enabled, `avatar_url` will be included in the response only
            if there is a Zulip avatar, and will be `null` for users who
            are using gravatar as their avatar. This option
            significantly reduces the compressed size of user data,
            since gravatar URLs are long, random strings and thus do not
            compress well. The `client_gravatar` field is set to `true` if
            clients can compute their own gravatars.

            **Changes**: The default value of this parameter was `false`
            prior to Zulip 5.0 (feature level 92).

        include_custom_profile_fields : typing.Optional[bool]
            Whether the client wants [custom profile field](/help/custom-profile-fields)
            data to be included in the response.

            **Changes**: New in Zulip 2.1.0. Previous versions do not offer these
            data via the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserByEmailResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.get_user_by_email(
            email="iago@zulip.com",
        )
        """
        _response = self._raw_client.get_user_by_email(
            email,
            client_gravatar=client_gravatar,
            include_custom_profile_fields=include_custom_profile_fields,
            request_options=request_options,
        )
        return _response.data

    def update_user_by_email(
        self,
        email: str,
        *,
        full_name: typing.Optional[str] = OMIT,
        role: typing.Optional[int] = OMIT,
        profile_data: typing.Optional[typing.Sequence[ProfileDataUpdate]] = OMIT,
        new_email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Administrative endpoint to update the details of another user in the organization by their email address.
        Works the same way as [`PATCH /users/{user_id}`](/api/update-user) but fetching the target user by their
        real email address.

        The requester needs to have permission to view the target user's real email address, subject to the
        user's email address visibility setting. Otherwise, the dummy address of the format
        `user{id}@{realm.host}` needs be used. This follows the same rules as `GET /users/{email}`.

        **Changes**: New in Zulip 10.0 (feature level 313).

        Parameters
        ----------
        email : str
            The email address of the user, specified following the same rules as
            [`GET /users/{email}`](/api/get-user-by-email).

        full_name : typing.Optional[str]
            The user's full name.

            **Changes**: Removed unnecessary JSON-encoding of this parameter in
            Zulip 5.0 (feature level 106).

        role : typing.Optional[int]
            New [role](/api/roles-and-permissions) for the user. Roles are encoded as:

            - Organization owner: 100
            - Organization administrator: 200
            - Organization moderator: 300
            - Member: 400
            - Guest: 600

            Only organization owners can add or remove the owner role.

            The owner role cannot be removed from the only organization owner.

            **Changes**: New in Zulip 3.0 (feature level 8), replacing the previous
            pair of `is_admin` and `is_guest` boolean parameters. Organization moderator
            role added in Zulip 4.0 (feature level 60).

        profile_data : typing.Optional[typing.Sequence[ProfileDataUpdate]]
            An array of objects describing updates to the [custom profile
            field](/help/custom-profile-fields) data for the user.

        new_email : typing.Optional[str]
            New email address for the user. Requires the user making the request
            to be an organization owner and additionally have the `.can_change_user_emails`
            special permission.

            **Changes**: New in Zulip 10.0 (feature level 285).

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
        client.users.update_user_by_email(
            email="hamlet@zulip.com",
        )
        """
        _response = self._raw_client.update_user_by_email(
            email,
            full_name=full_name,
            role=role,
            profile_data=profile_data,
            new_email=new_email,
            request_options=request_options,
        )
        return _response.data

    def get_user(
        self,
        user_id: int,
        *,
        client_gravatar: typing.Optional[bool] = None,
        include_custom_profile_fields: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUserResponse:
        """
        Fetch details for a single user in the organization.

        You can also fetch details on [all users in the organization](/api/get-users)
        or [by a user's Zulip API email](/api/get-user-by-email).

        **Changes**: In Zulip 12.0 (feature level 437), fixed a bug
        dating to feature level 232, which caused guest users to
        receive fake backwards-compatibility users in the format
        intended for clients using `POST /register` without the
        `user_list_incomplete` client capability.

        New in Zulip 3.0 (feature level 1).

        Parameters
        ----------
        user_id : int
            The target user's ID.

        client_gravatar : typing.Optional[bool]
            Whether the client supports computing gravatars URLs. If
            enabled, `avatar_url` will be included in the response only
            if there is a Zulip avatar, and will be `null` for users who
            are using gravatar as their avatar. This option
            significantly reduces the compressed size of user data,
            since gravatar URLs are long, random strings and thus do not
            compress well. The `client_gravatar` field is set to `true` if
            clients can compute their own gravatars.

            **Changes**: The default value of this parameter was `false`
            prior to Zulip 5.0 (feature level 92).

        include_custom_profile_fields : typing.Optional[bool]
            Whether the client wants [custom profile field](/help/custom-profile-fields)
            data to be included in the response.

            **Changes**: New in Zulip 2.1.0. Previous versions do not offer these
            data via the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.get_user(
            user_id=1,
        )
        """
        _response = self._raw_client.get_user(
            user_id,
            client_gravatar=client_gravatar,
            include_custom_profile_fields=include_custom_profile_fields,
            request_options=request_options,
        )
        return _response.data

    def deactivate_user(
        self,
        user_id: int,
        *,
        actions: typing.Optional[str] = None,
        deactivation_notification_comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        [Deactivates a
        user](https://zulip.com/help/deactivate-or-reactivate-a-user)
        given their user ID.

        Note that any bots controlled by the user will be deactivated
        before the user; clients that don't want this behavior are
        expected to prompt the user to adjust the bot's owners before
        making this API request.

        Parameters
        ----------
        user_id : int
            The target user's ID.

        actions : typing.Optional[str]
            Additional actions for the server to perform while deactivating the user.

            As with the actual deactivation, actions are first applied
            to any bots controlled by the target user, and then to the
            target user.

            **Changes**: New in Zulip 12.0 (feature level 459).

        deactivation_notification_comment : typing.Optional[str]
            If not `null`, requests that the deactivated user receive
            a notification email about their account deactivation.

            If not `""`, encodes custom text written by the administrator
            to be included in the notification email.

            **Changes**: New in Zulip 5.0 (feature level 135).

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
        client.users.deactivate_user(
            user_id=1,
        )
        """
        _response = self._raw_client.deactivate_user(
            user_id,
            actions=actions,
            deactivation_notification_comment=deactivation_notification_comment,
            request_options=request_options,
        )
        return _response.data

    def update_user(
        self,
        user_id: int,
        *,
        full_name: typing.Optional[str] = OMIT,
        role: typing.Optional[int] = OMIT,
        profile_data: typing.Optional[typing.Sequence[ProfileDataUpdate]] = OMIT,
        new_email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Administrative endpoint to update the details of another user in the organization.

        Supports everything an administrator can do to edit details of another
        user's account, including editing full name,
        [role](/help/user-roles), and [custom profile
        fields](/help/custom-profile-fields).

        Parameters
        ----------
        user_id : int
            The target user's ID.

        full_name : typing.Optional[str]
            The user's full name.

            **Changes**: Removed unnecessary JSON-encoding of this parameter in
            Zulip 5.0 (feature level 106).

        role : typing.Optional[int]
            New [role](/api/roles-and-permissions) for the user. Roles are encoded as:

            - Organization owner: 100
            - Organization administrator: 200
            - Organization moderator: 300
            - Member: 400
            - Guest: 600

            Only organization owners can add or remove the owner role.

            The owner role cannot be removed from the only organization owner.

            **Changes**: New in Zulip 3.0 (feature level 8), replacing the previous
            pair of `is_admin` and `is_guest` boolean parameters. Organization moderator
            role added in Zulip 4.0 (feature level 60).

        profile_data : typing.Optional[typing.Sequence[ProfileDataUpdate]]
            An array of objects describing updates to the [custom profile
            field](/help/custom-profile-fields) data for the user.

        new_email : typing.Optional[str]
            New email address for the user. Requires the user making the request
            to be an organization owner and additionally have the `.can_change_user_emails`
            special permission.

            **Changes**: New in Zulip 10.0 (feature level 285).

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
        client.users.update_user(
            user_id=1,
        )
        """
        _response = self._raw_client.update_user(
            user_id,
            full_name=full_name,
            role=role,
            profile_data=profile_data,
            new_email=new_email,
            request_options=request_options,
        )
        return _response.data

    def update_settings(
        self,
        *,
        target_users: typing.Optional[UpdateSettingsRequestTargetUsers] = OMIT,
        full_name: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        old_password: typing.Optional[str] = OMIT,
        new_password: typing.Optional[str] = OMIT,
        twenty_four_hour_time: typing.Optional[bool] = OMIT,
        web_mark_read_on_scroll_policy: typing.Optional[int] = OMIT,
        web_channel_default_view: typing.Optional[int] = OMIT,
        starred_message_counts: typing.Optional[bool] = OMIT,
        receives_typing_notifications: typing.Optional[bool] = OMIT,
        web_suggest_update_timezone: typing.Optional[bool] = OMIT,
        fluid_layout_width: typing.Optional[bool] = OMIT,
        high_contrast_mode: typing.Optional[bool] = OMIT,
        web_font_size_px: typing.Optional[int] = OMIT,
        web_line_height_percent: typing.Optional[int] = OMIT,
        color_scheme: typing.Optional[int] = OMIT,
        enable_drafts_synchronization: typing.Optional[bool] = OMIT,
        translate_emoticons: typing.Optional[bool] = OMIT,
        display_emoji_reaction_users: typing.Optional[bool] = OMIT,
        default_language: typing.Optional[str] = OMIT,
        web_home_view: typing.Optional[str] = OMIT,
        web_escape_navigates_to_home_view: typing.Optional[bool] = OMIT,
        left_side_userlist: typing.Optional[bool] = OMIT,
        emojiset: typing.Optional[str] = OMIT,
        demote_inactive_streams: typing.Optional[int] = OMIT,
        user_list_style: typing.Optional[int] = OMIT,
        web_animate_image_previews: typing.Optional[UpdateSettingsRequestWebAnimateImagePreviews] = OMIT,
        web_stream_unreads_count_display_policy: typing.Optional[int] = OMIT,
        hide_ai_features: typing.Optional[bool] = OMIT,
        web_inbox_show_channel_folders: typing.Optional[bool] = OMIT,
        web_left_sidebar_show_channel_folders: typing.Optional[bool] = OMIT,
        web_left_sidebar_unreads_count_summary: typing.Optional[bool] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        enable_stream_desktop_notifications: typing.Optional[bool] = OMIT,
        enable_stream_email_notifications: typing.Optional[bool] = OMIT,
        enable_stream_push_notifications: typing.Optional[bool] = OMIT,
        enable_stream_audible_notifications: typing.Optional[bool] = OMIT,
        notification_sound: typing.Optional[str] = OMIT,
        enable_desktop_notifications: typing.Optional[bool] = OMIT,
        enable_sounds: typing.Optional[bool] = OMIT,
        email_notifications_batching_period_seconds: typing.Optional[int] = OMIT,
        enable_offline_email_notifications: typing.Optional[bool] = OMIT,
        enable_offline_push_notifications: typing.Optional[bool] = OMIT,
        enable_online_push_notifications: typing.Optional[bool] = OMIT,
        enable_followed_topic_desktop_notifications: typing.Optional[bool] = OMIT,
        enable_followed_topic_email_notifications: typing.Optional[bool] = OMIT,
        enable_followed_topic_push_notifications: typing.Optional[bool] = OMIT,
        enable_followed_topic_audible_notifications: typing.Optional[bool] = OMIT,
        enable_digest_emails: typing.Optional[bool] = OMIT,
        enable_marketing_emails: typing.Optional[bool] = OMIT,
        enable_login_emails: typing.Optional[bool] = OMIT,
        message_content_in_email_notifications: typing.Optional[bool] = OMIT,
        pm_content_in_desktop_notifications: typing.Optional[bool] = OMIT,
        wildcard_mentions_notify: typing.Optional[bool] = OMIT,
        enable_followed_topic_wildcard_mentions_notify: typing.Optional[bool] = OMIT,
        desktop_icon_count_display: typing.Optional[int] = OMIT,
        realm_name_in_email_notifications_policy: typing.Optional[int] = OMIT,
        automatically_follow_topics_policy: typing.Optional[int] = OMIT,
        automatically_unmute_topics_in_muted_streams_policy: typing.Optional[int] = OMIT,
        automatically_follow_topics_where_mentioned: typing.Optional[bool] = OMIT,
        resolved_topic_notice_auto_read_policy: typing.Optional[
            UpdateSettingsRequestResolvedTopicNoticeAutoReadPolicy
        ] = OMIT,
        presence_enabled: typing.Optional[bool] = OMIT,
        enter_sends: typing.Optional[bool] = OMIT,
        send_private_typing_notifications: typing.Optional[bool] = OMIT,
        send_stream_typing_notifications: typing.Optional[bool] = OMIT,
        send_read_receipts: typing.Optional[bool] = OMIT,
        allow_private_data_export: typing.Optional[bool] = OMIT,
        email_address_visibility: typing.Optional[int] = OMIT,
        web_navigate_to_sent_message: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IgnoredParametersSuccess:
        """
        This endpoint is used to edit the current user's settings.

        When invoked by a realm admin, it supports bulk updates to
        settings for specified users or members of user groups using
        the `target_users` parameter.

        **Changes**: Removed `dense_mode` setting in Zulip 10.0 (feature level 364)
        as we now have `web_font_size_px` and `web_line_height_percent`
        settings for more control.

        Prior to Zulip 5.0 (feature level 80), this endpoint only
        supported the `full_name`, `email`, `old_password`, and
        `new_password` parameters. Notification settings were
        managed by `PATCH /settings/notifications`, and all other
        settings by `PATCH /settings/display`.

        The feature level 80 migration to merge these endpoints did not
        change how request parameters are encoded. However, it did change
        the handling of any invalid parameters present in a request
        (see feature level 78 change below).

        As of feature level 80, the `PATCH /settings/display` and
        `PATCH /settings/notifications` endpoints are deprecated aliases
        for this endpoint for backwards-compatibility, and will be removed
        once clients have migrated to use this endpoint.

        Prior to Zulip 5.0 (feature level 78), this endpoint indicated
        which parameters it had processed by including in the response
        object `"key": value` entries for values successfully changed by
        the request. That was replaced by the more ergonomic
        [`ignored_parameters_unsupported`][ignored-parameters] array.

        The `PATCH /settings/notifications` and `PATCH /settings/display`
        endpoints also had this behavior of indicating processed parameters
        before they became aliases of this endpoint in Zulip 5.0 (see
        feature level 80 change above).

        Before feature level 78, request parameters that were not supported
        (or were unchanged) were silently ignored.

        [ignored-parameters]: /api/rest-error-handling#ignored-parameters

        Parameters
        ----------
        target_users : typing.Optional[UpdateSettingsRequestTargetUsers]
            An object specifying the collection of users whose settings should be modified,
            for modification of other users' settings by an organization administrator.
            When this parameter is absent, this API endpoint always modifies the current
            user's own settings.

            **Changes**: New in Zulip 12.0 (feature level 444).

        full_name : typing.Optional[str]
            A new display name for the user.

        email : typing.Optional[str]
            Asks the server to initiate a confirmation sequence to change the user's email
            address to the indicated value. The user will need to demonstrate control of the
            new email address by clicking a confirmation link sent to that address.

        old_password : typing.Optional[str]
            The user's old Zulip password (or LDAP password, if LDAP authentication is in use).

            Required only when sending the `new_password` parameter.

        new_password : typing.Optional[str]
            The user's new Zulip password (or LDAP password, if LDAP authentication is in use).

            The `old_password` parameter must be included in the request.

        twenty_four_hour_time : typing.Optional[bool]
            Whether time should be [displayed in 24-hour notation](/help/change-the-time-format).

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

        web_mark_read_on_scroll_policy : typing.Optional[int]
            Whether or not to mark messages as read when the user scrolls through their
            feed.

            - 1 - Always
            - 2 - Only in conversation views
            - 3 - Never

            **Changes**: New in Zulip 7.0 (feature level 175). Previously, there was no
            way for the user to configure this behavior on the web, and the Zulip web and
            desktop apps behaved like the "Always" setting when marking messages as read.

        web_channel_default_view : typing.Optional[int]
            Web/desktop app setting controlling the default navigation
            behavior when clicking on a channel link.

            - 1 - Top topic in the channel
            - 2 - Channel feed
            - 3 - List of topics
            - 4 - Top unread topic in channel

            **Changes**: The "Top unread topic in channel" is new in Zulip 11.0
            (feature level 401).

            The "List of topics" option is new in Zulip 11.0 (feature level 383).

            New in Zulip 9.0 (feature level 269). Previously, this
            was not configurable, and every user had the "Channel feed" behavior.

        starred_message_counts : typing.Optional[bool]
            Whether clients should display the [number of starred
            messages](/help/star-a-message#display-the-number-of-starred-messages).

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

        receives_typing_notifications : typing.Optional[bool]
            Whether the user is configured to receive typing notifications from other users.
            The server will only deliver typing notifications events to users who for whom this
            is enabled.

            By default, this is set to true, enabling user to receive typing
            notifications from other users.

            **Changes**: New in Zulip 9.0 (feature level 253). Previously, there were only
            options to disable sending typing notifications.

        web_suggest_update_timezone : typing.Optional[bool]
            Whether the user should be shown an alert, offering to update their
            [profile time zone](/help/change-your-timezone), when the time displayed
            for the profile time zone differs from the current time displayed by the
            time zone configured on their device.

            **Changes**: New in Zulip 10.0 (feature level 329).

        fluid_layout_width : typing.Optional[bool]
            Whether to use the [maximum available screen width](/help/enable-full-width-display)
            for the web app's center panel (message feed, recent conversations) on wide screens.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

        high_contrast_mode : typing.Optional[bool]
            This setting is reserved for use to control variations in Zulip's design
            to help visually impaired users.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

        web_font_size_px : typing.Optional[int]
            User-configured primary `font-size` for the web application, in pixels.

            **Changes**: New in Zulip 9.0 (feature level 245). Previously, font size was
            only adjustable via browser zoom. Note that this setting was not fully
            implemented at this feature level.

        web_line_height_percent : typing.Optional[int]
            User-configured primary `line-height` for the web application, in percent, so a
            value of 120 represents a `line-height` of 1.2.

            **Changes**: New in Zulip 9.0 (feature level 245). Previously, line height was
            not user-configurable. Note that this setting was not fully implemented at this
            feature level.

        color_scheme : typing.Optional[int]
            Controls which [color theme](/help/dark-theme) to use.

            - 1 - Automatic
            - 2 - Dark theme
            - 3 - Light theme

            Automatic detection is implementing using the standard `prefers-color-scheme`
            media query.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

        enable_drafts_synchronization : typing.Optional[bool]
            A boolean parameter to control whether synchronizing drafts is enabled for
            the user. When synchronization is disabled, all drafts stored in the server
            will be automatically deleted from the server.

            This does not do anything (like sending events) to delete local copies of
            drafts stored in clients.

            **Changes**: New in Zulip 5.0 (feature level 87).

        translate_emoticons : typing.Optional[bool]
            Whether to [translate emoticons to emoji](/help/configure-emoticon-translations)
            in messages the user sends.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

        display_emoji_reaction_users : typing.Optional[bool]
            Whether to display the names of reacting users on a message.

            When enabled, clients should display the names of reacting users, rather than
            a count, for messages with few total reactions. The ideal cutoff may depend on
            the space available for displaying reactions; the official web application
            displays names when 3 or fewer total reactions are present with this setting
            enabled.

            **Changes**: New in Zulip 6.0 (feature level 125).

        default_language : typing.Optional[str]
            What [default language](/help/change-your-language) to use for the account.

            This controls both the Zulip UI as well as email notifications sent to the user.

            The value needs to be a standard language code that the Zulip server has
            translation data for; for example, `"en"` for English or `"de"` for German.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

            Unnecessary JSON-encoding of this parameter was removed in Zulip 4.0 (feature level 63).

        web_home_view : typing.Optional[str]
            The [home view](/help/configure-home-view) used when opening a new
            Zulip web app window or hitting the `Esc` keyboard shortcut repeatedly.

            - "recent" - Recent conversations view
            - "inbox" - Inbox view
            - "all_messages" - Combined feed view

            **Changes**: Before Zulip 12.0 (feature level 454), the Recent
            view had `"recent_topics"` as its string encoding.

            New in Zulip 8.0 (feature level 219). Previously, this was called
            `default_view`, which was new in Zulip 4.0 (feature level 42).

            Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

            Unnecessary JSON-encoding of this parameter was removed in Zulip 4.0 (feature level 64).

        web_escape_navigates_to_home_view : typing.Optional[bool]
            Whether the escape key navigates to the
            [configured home view](/help/configure-home-view).

            **Changes**: New in Zulip 8.0 (feature level 219). Previously, this
            was called `escape_navigates_to_default_view`, which was new in Zulip
            5.0 (feature level 107).

        left_side_userlist : typing.Optional[bool]
            Whether the users list on left sidebar in narrow windows.

            This feature is not heavily used and is likely to be reworked.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

        emojiset : typing.Optional[str]
            The user's configured [emoji set](/help/emoji-and-emoticons#use-emoticons),
            used to display emoji to the user everywhere they appear in the UI.

            - "google" - Google modern
            - "twitter" - Twitter
            - "text" - Plain text

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

            Unnecessary JSON-encoding of this parameter was removed in Zulip 4.0 (feature level 64).

        demote_inactive_streams : typing.Optional[int]
            Whether to [hide inactive channels](/help/manage-inactive-channels) in the left sidebar.

            - 1 - Automatic
            - 2 - Always
            - 3 - Never

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

        user_list_style : typing.Optional[int]
            The style selected by the user for the right sidebar user list.

            - 1 - Compact
            - 2 - With status
            - 3 - With avatar and status

            **Changes**: New in Zulip 6.0 (feature level 141).

        web_animate_image_previews : typing.Optional[UpdateSettingsRequestWebAnimateImagePreviews]
            Controls how animated images should be played in the message feed in the web/desktop application.

            - "always" - Always play the animated images in the message feed.
            - "on_hover" - Play the animated images on hover over them in the message feed.
            - "never" - Never play animated images in the message feed.

            **Changes**: New in Zulip 9.0 (feature level 275).

        web_stream_unreads_count_display_policy : typing.Optional[int]
            Configuration for which channels should be displayed with a numeric unread count in the left sidebar.
            Channels that do not have an unread count will have a simple dot indicator for whether there are any
            unread messages.

            - 1 - All channels
            - 2 - Unmuted channels and topics
            - 3 - No channels

            **Changes**: New in Zulip 8.0 (feature level 210).

        hide_ai_features : typing.Optional[bool]
            Controls whether user wants AI features like topic summarization to
            be hidden in all Zulip clients.

            **Changes**: New in Zulip 10.0 (feature level 350).

        web_inbox_show_channel_folders : typing.Optional[bool]
            Determines whether [channel folders](/help/channel-folders)
            are used to organize how conversations with unread messages
            are displayed in the web/desktop application's Inbox view.

            **Changes**: New in Zulip 12.0 (feature level 431).

        web_left_sidebar_show_channel_folders : typing.Optional[bool]
            Determines whether [channel folders](/help/channel-folders)
            are used to organize how channels are displayed in the
            web/desktop application's left sidebar.

            **Changes**: New in Zulip 11.0 (feature level 411).

        web_left_sidebar_unreads_count_summary : typing.Optional[bool]
            Determines whether the web/desktop application's left sidebar displays
            the unread message count summary.

            **Changes**: New in Zulip 11.0 (feature level 398).

        timezone : typing.Optional[str]
            The IANA identifier of the user's [profile time zone](/help/change-your-timezone),
            which is used primarily to display the user's local time to other users.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

            Unnecessary JSON-encoding of this parameter was removed in Zulip 4.0 (feature level 64).

        enable_stream_desktop_notifications : typing.Optional[bool]
            Enable visual desktop notifications for channel messages.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_stream_email_notifications : typing.Optional[bool]
            Enable email notifications for channel messages.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_stream_push_notifications : typing.Optional[bool]
            Enable mobile notifications for channel messages.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_stream_audible_notifications : typing.Optional[bool]
            Enable audible desktop notifications for channel messages.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        notification_sound : typing.Optional[str]
            Notification sound name.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

            Unnecessary JSON-encoding of this parameter was removed in Zulip 4.0 (feature level 63).

        enable_desktop_notifications : typing.Optional[bool]
            Enable visual desktop notifications for direct messages and @-mentions.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_sounds : typing.Optional[bool]
            Enable audible desktop notifications for direct messages and
            @-mentions.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        email_notifications_batching_period_seconds : typing.Optional[int]
            The duration (in seconds) for which the server should wait to batch
            email notifications before sending them.

            **Changes**: New in Zulip 5.0 (feature level 82)

        enable_offline_email_notifications : typing.Optional[bool]
            Enable email notifications for direct messages and @-mentions received
            when the user is offline.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_offline_push_notifications : typing.Optional[bool]
            Enable mobile notification for direct messages and @-mentions received
            when the user is offline.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_online_push_notifications : typing.Optional[bool]
            Enable mobile notification for direct messages and @-mentions received
            when the user is online.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_followed_topic_desktop_notifications : typing.Optional[bool]
            Enable visual desktop notifications for messages sent to followed topics.

            **Changes**: New in Zulip 8.0 (feature level 189).

        enable_followed_topic_email_notifications : typing.Optional[bool]
            Enable email notifications for messages sent to followed topics.

            **Changes**: New in Zulip 8.0 (feature level 189).

        enable_followed_topic_push_notifications : typing.Optional[bool]
            Enable push notifications for messages sent to followed topics.

            **Changes**: New in Zulip 8.0 (feature level 189).

        enable_followed_topic_audible_notifications : typing.Optional[bool]
            Enable audible desktop notifications for messages sent to followed topics.

            **Changes**: New in Zulip 8.0 (feature level 189).

        enable_digest_emails : typing.Optional[bool]
            Enable digest emails when the user is away.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_marketing_emails : typing.Optional[bool]
            Enable marketing emails. Has no function outside Zulip Cloud.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_login_emails : typing.Optional[bool]
            Enable email notifications for new logins to account.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        message_content_in_email_notifications : typing.Optional[bool]
            Include the message's content in email notifications for new messages.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        pm_content_in_desktop_notifications : typing.Optional[bool]
            Include content of direct messages in desktop notifications.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        wildcard_mentions_notify : typing.Optional[bool]
            Whether wildcard mentions (E.g. @**all**) should send notifications
            like a personal mention.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_followed_topic_wildcard_mentions_notify : typing.Optional[bool]
            Whether wildcard mentions (e.g., @**all**) in messages sent to followed topics
            should send notifications like a personal mention.

            **Changes**: New in Zulip 8.0 (feature level 189).

        desktop_icon_count_display : typing.Optional[int]
            Unread count badge (appears in desktop sidebar and browser tab)

            - 1 - All unread messages
            - 2 - DMs, mentions, and followed topics
            - 3 - DMs and mentions
            - 4 - None

            **Changes**: In Zulip 8.0 (feature level 227), added `DMs, mentions, and followed
            topics` option, renumbering the options to insert it in order.

            Before Zulip 5.0 (feature level 80), this setting was managed by the
            `PATCH /settings/notifications` endpoint.

        realm_name_in_email_notifications_policy : typing.Optional[int]
            Whether to [include organization name in subject of message notification
            emails](/help/email-notifications#include-organization-name-in-subject-line).

            - 1 - Automatic
            - 2 - Always
            - 3 - Never

            **Changes**: New in Zulip 7.0 (feature level 168), replacing the
            previous `realm_name_in_notifications` boolean;
            `true` corresponded to `Always`, and `false` to `Never`.

            Before Zulip 5.0 (feature level 80), the previous `realm_name_in_notifications`
            setting was managed by the `PATCH /settings/notifications` endpoint.

        automatically_follow_topics_policy : typing.Optional[int]
            Which [topics to follow automatically](/help/mute-a-topic).

            - 1 - Topics the user participates in
            - 2 - Topics the user sends a message to
            - 3 - Topics the user starts
            - 4 - Never

            **Changes**: New in Zulip 8.0 (feature level 214).

        automatically_unmute_topics_in_muted_streams_policy : typing.Optional[int]
            Which [topics to unmute automatically in muted channels](/help/mute-a-topic).

            - 1 - Topics the user participates in
            - 2 - Topics the user sends a message to
            - 3 - Topics the user starts
            - 4 - Never

            **Changes**: New in Zulip 8.0 (feature level 214).

        automatically_follow_topics_where_mentioned : typing.Optional[bool]
            Whether the server will automatically mark the user as following
            topics where the user is mentioned.

            **Changes**: New in Zulip 8.0 (feature level 235).

        resolved_topic_notice_auto_read_policy : typing.Optional[UpdateSettingsRequestResolvedTopicNoticeAutoReadPolicy]
            Controls whether the resolved-topic notices are marked as read.

            - "always" - Always mark resolved-topic notices as read.
            - "except_followed" - Mark resolved-topic notices as read in topics not followed by the user.
            - "never" - Never mark resolved-topic notices as read.

            **Changes**: New in Zulip 11.0 (feature level 385).

        presence_enabled : typing.Optional[bool]
            Display the presence status to other users when online.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enter_sends : typing.Optional[bool]
            Whether pressing Enter in the compose box sends a message
            (or saves a message edit).

            **Changes**: Before Zulip 5.0 (feature level 81), this setting was managed by
            the `POST /users/me/enter-sends` endpoint, with the same parameter format.

        send_private_typing_notifications : typing.Optional[bool]
            Whether [typing notifications](/help/typing-notifications) be sent when composing
            direct messages.

            **Changes**: New in Zulip 5.0 (feature level 105).

        send_stream_typing_notifications : typing.Optional[bool]
            Whether [typing notifications](/help/typing-notifications) be sent when composing
            channel messages.

            **Changes**: New in Zulip 5.0 (feature level 105).

        send_read_receipts : typing.Optional[bool]
            Whether other users are allowed to see whether you've
            read messages.

            **Changes**: New in Zulip 5.0 (feature level 105).

        allow_private_data_export : typing.Optional[bool]
            Whether organization administrators are allowed to
            export your private data.

            **Changes**: New in Zulip 10.0 (feature level 293).

        email_address_visibility : typing.Optional[int]
            The [policy][permission-level] this user has selected for [which other
            users][help-email-visibility] in this organization can see their real
            email address.

            - 1 = Everyone
            - 2 = Members only
            - 3 = Administrators only
            - 4 = Nobody
            - 5 = Moderators only

            **Changes**: New in Zulip 7.0 (feature level 163), replacing the
            realm-level setting.

            [permission-level]: /api/roles-and-permissions#permission-levels
            [help-email-visibility]: /help/configure-email-visibility

        web_navigate_to_sent_message : typing.Optional[bool]
            Web/desktop app setting for whether the user's view should
            automatically go to the conversation where they sent a message.

            **Changes**: New in Zulip 9.0 (feature level 268). Previously,
            this behavior was not configurable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IgnoredParametersSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.update_settings()
        """
        _response = self._raw_client.update_settings(
            target_users=target_users,
            full_name=full_name,
            email=email,
            old_password=old_password,
            new_password=new_password,
            twenty_four_hour_time=twenty_four_hour_time,
            web_mark_read_on_scroll_policy=web_mark_read_on_scroll_policy,
            web_channel_default_view=web_channel_default_view,
            starred_message_counts=starred_message_counts,
            receives_typing_notifications=receives_typing_notifications,
            web_suggest_update_timezone=web_suggest_update_timezone,
            fluid_layout_width=fluid_layout_width,
            high_contrast_mode=high_contrast_mode,
            web_font_size_px=web_font_size_px,
            web_line_height_percent=web_line_height_percent,
            color_scheme=color_scheme,
            enable_drafts_synchronization=enable_drafts_synchronization,
            translate_emoticons=translate_emoticons,
            display_emoji_reaction_users=display_emoji_reaction_users,
            default_language=default_language,
            web_home_view=web_home_view,
            web_escape_navigates_to_home_view=web_escape_navigates_to_home_view,
            left_side_userlist=left_side_userlist,
            emojiset=emojiset,
            demote_inactive_streams=demote_inactive_streams,
            user_list_style=user_list_style,
            web_animate_image_previews=web_animate_image_previews,
            web_stream_unreads_count_display_policy=web_stream_unreads_count_display_policy,
            hide_ai_features=hide_ai_features,
            web_inbox_show_channel_folders=web_inbox_show_channel_folders,
            web_left_sidebar_show_channel_folders=web_left_sidebar_show_channel_folders,
            web_left_sidebar_unreads_count_summary=web_left_sidebar_unreads_count_summary,
            timezone=timezone,
            enable_stream_desktop_notifications=enable_stream_desktop_notifications,
            enable_stream_email_notifications=enable_stream_email_notifications,
            enable_stream_push_notifications=enable_stream_push_notifications,
            enable_stream_audible_notifications=enable_stream_audible_notifications,
            notification_sound=notification_sound,
            enable_desktop_notifications=enable_desktop_notifications,
            enable_sounds=enable_sounds,
            email_notifications_batching_period_seconds=email_notifications_batching_period_seconds,
            enable_offline_email_notifications=enable_offline_email_notifications,
            enable_offline_push_notifications=enable_offline_push_notifications,
            enable_online_push_notifications=enable_online_push_notifications,
            enable_followed_topic_desktop_notifications=enable_followed_topic_desktop_notifications,
            enable_followed_topic_email_notifications=enable_followed_topic_email_notifications,
            enable_followed_topic_push_notifications=enable_followed_topic_push_notifications,
            enable_followed_topic_audible_notifications=enable_followed_topic_audible_notifications,
            enable_digest_emails=enable_digest_emails,
            enable_marketing_emails=enable_marketing_emails,
            enable_login_emails=enable_login_emails,
            message_content_in_email_notifications=message_content_in_email_notifications,
            pm_content_in_desktop_notifications=pm_content_in_desktop_notifications,
            wildcard_mentions_notify=wildcard_mentions_notify,
            enable_followed_topic_wildcard_mentions_notify=enable_followed_topic_wildcard_mentions_notify,
            desktop_icon_count_display=desktop_icon_count_display,
            realm_name_in_email_notifications_policy=realm_name_in_email_notifications_policy,
            automatically_follow_topics_policy=automatically_follow_topics_policy,
            automatically_unmute_topics_in_muted_streams_policy=automatically_unmute_topics_in_muted_streams_policy,
            automatically_follow_topics_where_mentioned=automatically_follow_topics_where_mentioned,
            resolved_topic_notice_auto_read_policy=resolved_topic_notice_auto_read_policy,
            presence_enabled=presence_enabled,
            enter_sends=enter_sends,
            send_private_typing_notifications=send_private_typing_notifications,
            send_stream_typing_notifications=send_stream_typing_notifications,
            send_read_receipts=send_read_receipts,
            allow_private_data_export=allow_private_data_export,
            email_address_visibility=email_address_visibility,
            web_navigate_to_sent_message=web_navigate_to_sent_message,
            request_options=request_options,
        )
        return _response.data

    def set_typing_status(
        self,
        *,
        op: SetTypingStatusRequestOp,
        type: typing.Optional[SetTypingStatusRequestType] = OMIT,
        to: typing.Optional[typing.Sequence[int]] = OMIT,
        stream_id: typing.Optional[int] = OMIT,
        topic: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Notify other users whether the current user is
        [typing a message][help-typing].

        Clients implementing Zulip's typing notifications
        protocol should work as follows:

        - Send a request to this endpoint with `"op": "start"` when a user
          starts composing a message.
        - While the user continues to actively type or otherwise interact with
          the compose UI (e.g. interacting with the compose box emoji picker),
          send regular `"op": "start"` requests to this endpoint, using
          `server_typing_started_wait_period_milliseconds` in the
          [`POST /register`][api-register] response as the time interval
          between each request.
        - Send a request to this endpoint with `"op": "stop"` when a user
          has stopped using the compose UI for the time period indicated by
          `server_typing_stopped_wait_period_milliseconds` in the
          [`POST /register`][api-register] response or when a user
          cancels the compose action (if it had previously sent a "start"
          notification for that compose action).
        - Start displaying a visual typing indicator for a given conversation
          when a [`typing op:start`][start-typing] event is received
          from the server.
        - Continue displaying a visual typing indicator for the conversation
          until a [`typing op:stop`][stop-typing] event is received
          from the server or the time period indicated by
          `server_typing_started_expiry_period_milliseconds` in the
          [`POST /register`][api-register] response has passed without
          a new `typing "op": "start"` event for the conversation.

        This protocol is designed to allow the server-side typing notifications
        implementation to be stateless while being resilient as network failures
        will not result in a user being incorrectly displayed as perpetually
        typing.

        See the subsystems documentation on [typing indicators][typing-protocol-docs]
        for additional design details on Zulip's typing notifications protocol.

        **Changes**: Clients shouldn't care about the APIs prior to Zulip 8.0 (feature level 215)
        for channel typing notifications, as no client actually implemented
        the previous API for those.

        Support for displaying channel typing notifications was new
        in Zulip 4.0 (feature level 58). Clients should indicate they support
        processing channel typing notifications via the `stream_typing_notifications`
        value in the `client_capabilities` parameter of the
        [`POST /register`][client-capabilities] endpoint.

        [help-typing]: /help/typing-notifications
        [api-register]: /api/register-queue
        [start-typing]: /api/get-events#typing-start
        [stop-typing]: /api/get-events#typing-stop
        [client-capabilities]: /api/register-queue#parameter-client_capabilities
        [typing-protocol-docs]: https://zulip.readthedocs.io/en/latest/subsystems/typing-indicators.html

        Parameters
        ----------
        op : SetTypingStatusRequestOp
            Whether the user has started (`"start"`) or stopped (`"stop"`) typing.

        type : typing.Optional[SetTypingStatusRequestType]
            Type of the message being composed.

            **Changes**: In Zulip 9.0 (feature level 248), `"channel"` was added as
            an additional value for this parameter to indicate a channel message is
            being composed.

            In Zulip 8.0 (feature level 215), stopped supporting
            `"private"` as a valid value for this parameter.

            In Zulip 7.0 (feature level 174), `"direct"` was added
            as the preferred way to indicate a direct message is being composed,
            becoming the default value for this parameter and deprecating the
            original `"private"`.

            New in Zulip 4.0 (feature level 58). Previously, typing notifications
            were only for direct messages.

        to : typing.Optional[typing.Sequence[int]]
            User IDs of the recipients of the message being typed. Required for the
            `"direct"` type. Ignored in the case of `"stream"` or `"channel"` type.

            Clients should send a JSON-encoded list of user IDs, even if there is only
            one recipient.

            **Changes**: In Zulip 8.0 (feature level 215), stopped using this parameter
            for the `"stream"` type. Previously, in the case of the `"stream"` type, it
            accepted a single-element list containing the ID of the channel. A new parameter,
            `stream_id`, is now used for this. Note that the `"channel"` type did not
            exist at this feature level.

            Support for typing notifications for channel' messages
            is new in Zulip 4.0 (feature level 58). Previously, typing
            notifications were only for direct messages.

            Before Zulip 2.0.0, this parameter accepted only a JSON-encoded
            list of email addresses. Support for the email address-based format was
            removed in Zulip 3.0 (feature level 11).

        stream_id : typing.Optional[int]
            ID of the channel in which the message is being typed. Required for the `"stream"`
            or `"channel"` type. Ignored in the case of `"direct"` type.

            **Changes**: New in Zulip 8.0 (feature level 215). Previously, a single-element
            list containing the ID of the channel was passed in `to` parameter.

        topic : typing.Optional[str]
            Topic to which message is being typed. Required for the `"stream"` or `"channel"`
            type. Ignored in the case of `"direct"` type.

            Note: When `"(no topic)"` or the value of `realm_empty_topic_display_name`
            found in the [POST /register](/api/register-queue) response is used for this
            parameter, it is interpreted as an empty string.

            **Changes**: Before Zulip 10.0 (feature level 372),
            `"(no topic)"` was not interpreted as an empty string.

            Before Zulip 10.0 (feature level 334), empty string
            was not a valid topic name for channel messages.

            New in Zulip 4.0 (feature level 58). Previously, typing notifications
            were only for direct messages.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern.users import SetTypingStatusRequestOp

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.set_typing_status(
            op=SetTypingStatusRequestOp.START,
        )
        """
        _response = self._raw_client.set_typing_status(
            op=op, type=type, to=to, stream_id=stream_id, topic=topic, request_options=request_options
        )
        return _response.data

    def set_typing_status_for_message_edit(
        self,
        message_id: int,
        *,
        op: SetTypingStatusForMessageEditRequestOp,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Notify other users whether the current user is editing a message.

        Typing notifications for editing messages follow the same protocol as
        [set-typing-status](/api/set-typing-status), see that endpoint for
        details.

        **Changes**: Before Zulip 10.0 (feature level 361), the endpoint was
        named `/message_edit_typing` with `message_id` a required parameter in
        the request body. Clients are recommended to start using sending these
        typing notifications starting from this feature level.

        New in Zulip 10.0 (feature level 351). Previously, typing notifications were
        not available when editing messages.

        Parameters
        ----------
        message_id : int
            The target message's ID.

        op : SetTypingStatusForMessageEditRequestOp
            Whether the user has started (`"start"`) or stopped (`"stop"`) editing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern.users import SetTypingStatusForMessageEditRequestOp

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.set_typing_status_for_message_edit(
            message_id=1,
            op=SetTypingStatusForMessageEditRequestOp.START,
        )
        """
        _response = self._raw_client.set_typing_status_for_message_edit(
            message_id, op=op, request_options=request_options
        )
        return _response.data

    def create_user_group(
        self,
        *,
        name: str,
        description: str,
        members: typing.Sequence[int],
        subgroups: typing.Optional[typing.Sequence[int]] = OMIT,
        can_add_members_group: typing.Optional[CreateUserGroupRequestCanAddMembersGroup] = OMIT,
        can_join_group: typing.Optional[CreateUserGroupRequestCanJoinGroup] = OMIT,
        can_leave_group: typing.Optional[CreateUserGroupRequestCanLeaveGroup] = OMIT,
        can_manage_group: typing.Optional[CreateUserGroupRequestCanManageGroup] = OMIT,
        can_mention_group: typing.Optional[CreateUserGroupRequestCanMentionGroup] = OMIT,
        can_remove_members_group: typing.Optional[CreateUserGroupRequestCanRemoveMembersGroup] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateUserGroupResponse:
        """
        Create a new [user group](/help/user-groups).

        **Changes**: Prior to Zulip 12.0 (feature level 496), bot
        users were not permitted to call this endpoint.

        Parameters
        ----------
        name : str
            The name of the user group.

        description : str
            The description of the user group.

        members : typing.Sequence[int]
            An array containing the user IDs of the initial members for the
            new user group.

        subgroups : typing.Optional[typing.Sequence[int]]
            An array containing the IDs of the initial subgroups for the new
            user group.

            User can add subgroups to the new group irrespective of other
            permissions for the new group.

            **Changes**: New in Zulip 10.0 (feature level 311).

        can_add_members_group : typing.Optional[CreateUserGroupRequestCanAddMembersGroup]
            A [group-setting value][setting-values] defining the set of users who
            have permission to add members to this user group.

            **Changes**: New in Zulip 10.0 (feature level 305). Previously, this
            permission was controlled by the `can_manage_group` setting.

            [setting-values]: /api/group-setting-values
            [system-groups]: /api/group-setting-values#system-groups

        can_join_group : typing.Optional[CreateUserGroupRequestCanJoinGroup]
            A [group-setting value][setting-values] defining the set of users who
            have permission to join this user group.

            **Changes**: New in Zulip 10.0 (feature level 301).

            [setting-values]: /api/group-setting-values
            [system-groups]: /api/group-setting-values#system-groups

        can_leave_group : typing.Optional[CreateUserGroupRequestCanLeaveGroup]
            A [group-setting value][setting-values] defining the set of users who
            have permission to leave this user group.

            **Changes**: New in Zulip 10.0 (feature level 308).

            [setting-values]: /api/group-setting-values
            [system-groups]: /api/group-setting-values#system-groups

        can_manage_group : typing.Optional[CreateUserGroupRequestCanManageGroup]
            A [group-setting value][setting-values] defining the set of users who
            have permission to [manage this user group][manage-user-groups].

            This setting cannot be set to `"role:internet"` and `"role:everyone"`
            [system groups][system-groups].

            **Changes**: New in Zulip 10.0 (feature level 283).

            [setting-values]: /api/group-setting-values
            [system-groups]: /api/group-setting-values#system-groups
            [manage-user-groups]: /help/manage-user-groups

        can_mention_group : typing.Optional[CreateUserGroupRequestCanMentionGroup]
            A [group-setting value][setting-values] defining the set of users who
            have permission to [mention this user group][mentions].

            This setting cannot be set to `"role:internet"` and `"role:owners"`
            [system groups][system-groups].

            Before Zulip 9.0 (feature level 258), this parameter could only be the
            integer form of a [group-setting value][setting-values].

            Before Zulip 8.0 (feature level 198), this parameter was named
            `can_mention_group_id`.

            New in Zulip 8.0 (feature level 191). Previously, groups could be
            mentioned only if they were not [system groups][system-groups].

            [setting-values]: /api/group-setting-values
            [system-groups]: /api/group-setting-values#system-groups
            [mentions]: /help/mention-a-user-or-group

        can_remove_members_group : typing.Optional[CreateUserGroupRequestCanRemoveMembersGroup]
            A [group-setting value][setting-values] defining the set of users who
            have permission to remove members from this user group.

            **Changes**: New in Zulip 10.0 (feature level 324). Previously, this
            permission was controlled by the `can_manage_group` setting.

            [setting-values]: /api/group-setting-values
            [system-groups]: /api/group-setting-values#system-groups

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateUserGroupResponse
            A success response containing the unique ID of the user group.
            This field provides a straightforward way to reference the
            newly created user group.

            **Changes**: New in Zulip 10.0 (feature level 317).

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.create_user_group(
            name="marketing",
            description="The marketing team.",
            members=[1, 2, 3, 4],
        )
        """
        _response = self._raw_client.create_user_group(
            name=name,
            description=description,
            members=members,
            subgroups=subgroups,
            can_add_members_group=can_add_members_group,
            can_join_group=can_join_group,
            can_leave_group=can_leave_group,
            can_manage_group=can_manage_group,
            can_mention_group=can_mention_group,
            can_remove_members_group=can_remove_members_group,
            request_options=request_options,
        )
        return _response.data

    def get_user_group_members(
        self,
        user_group_id: int,
        *,
        direct_member_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUserGroupMembersResponse:
        """
        Get the members of a [user group](/help/user-groups).

        **Changes**: Prior to Zulip 12.0 (feature level 496), bot
        users were not permitted to call this endpoint.

        New in Zulip 6.0 (feature level 127).

        Parameters
        ----------
        user_group_id : int
            The ID of the target user group.

        direct_member_only : typing.Optional[bool]
            Whether to consider only the direct members of user group and not members
            of its subgroups. Default is `false`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserGroupMembersResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.get_user_group_members(
            user_group_id=1,
        )
        """
        _response = self._raw_client.get_user_group_members(
            user_group_id, direct_member_only=direct_member_only, request_options=request_options
        )
        return _response.data

    def update_user_group_members(
        self,
        user_group_id: int,
        *,
        delete: typing.Optional[typing.Sequence[int]] = OMIT,
        add: typing.Optional[typing.Sequence[int]] = OMIT,
        delete_subgroups: typing.Optional[typing.Sequence[int]] = OMIT,
        add_subgroups: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Update the members of a [user group](/help/user-groups). The
        user IDs must correspond to non-deactivated users.

        **Changes**: Prior to Zulip 12.0 (feature level 496), bot
        users were not permitted to call this endpoint.

        Prior to Zulip 11.0 (feature level 391), members
        could not be added or removed from a deactivated group.

        **Changes**: Prior to Zulip 10.0 (feature level 303), group memberships of
        deactivated users were visible to the API and could be edited via this endpoint.

        Parameters
        ----------
        user_group_id : int
            The ID of the target user group.

        delete : typing.Optional[typing.Sequence[int]]
            The list of user IDs to be removed from the user group.

        add : typing.Optional[typing.Sequence[int]]
            The list of user IDs to be added to the user group.

        delete_subgroups : typing.Optional[typing.Sequence[int]]
            The list of user group IDs to be removed from the user group.

            **Changes**: New in Zulip 10.0 (feature level 311).

        add_subgroups : typing.Optional[typing.Sequence[int]]
            The list of user group IDs to be added to the user group.

            **Changes**: New in Zulip 10.0 (feature level 311).

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
        client.users.update_user_group_members(
            user_group_id=1,
        )
        """
        _response = self._raw_client.update_user_group_members(
            user_group_id,
            delete=delete,
            add=add,
            delete_subgroups=delete_subgroups,
            add_subgroups=add_subgroups,
            request_options=request_options,
        )
        return _response.data

    def update_user_group(
        self,
        user_group_id: int,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        can_add_members_group: typing.Optional[UpdateUserGroupRequestCanAddMembersGroup] = OMIT,
        can_join_group: typing.Optional[UpdateUserGroupRequestCanJoinGroup] = OMIT,
        can_leave_group: typing.Optional[UpdateUserGroupRequestCanLeaveGroup] = OMIT,
        can_manage_group: typing.Optional[UpdateUserGroupRequestCanManageGroup] = OMIT,
        can_mention_group: typing.Optional[UpdateUserGroupRequestCanMentionGroup] = OMIT,
        can_remove_members_group: typing.Optional[UpdateUserGroupRequestCanRemoveMembersGroup] = OMIT,
        deactivated: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Update the name, description or any of the permission settings
        of a [user group](/help/user-groups).

        This endpoint is also used to reactivate a user group.

        Note that while permissions settings of deactivated groups can
        be edited by this API endpoint, and those permissions settings
        do affect the ability to modify the deactivated group and its
        membership, the deactivated group itself cannot be mentioned
        or used in the value of any permission without first being reactivated.

        **Changes**: Prior to Zulip 12.0 (feature level 496), bot
        users were not permitted to call this endpoint.

        Starting with Zulip 11.0 (feature level 386), this
        endpoint can be used to reactivate a user group.

        Prior to Zulip 10.0 (feature level 340), only the name field
        of deactivated groups could be modified.

        Parameters
        ----------
        user_group_id : int
            The ID of the target user group.

        name : typing.Optional[str]
            The new name of the group.

            **Changes**: Before Zulip 7.0 (feature level 165), this was
            a required field.

        description : typing.Optional[str]
            The new description of the group.

            **Changes**: Before Zulip 7.0 (feature level 165), this was
            a required field.

        can_add_members_group : typing.Optional[UpdateUserGroupRequestCanAddMembersGroup]
            The set of users who have permission to add members to this user group
            expressed as an [update to a group-setting value][update-group-setting].

            **Changes**: New in Zulip 10.0 (feature level 305). Previously, this
            permission was controlled by the `can_manage_group` setting.

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values
            [system-groups]: /api/group-setting-values#system-groups

        can_join_group : typing.Optional[UpdateUserGroupRequestCanJoinGroup]
            The set of users who have permission to join this user group
            expressed as an [update to a group-setting value][update-group-setting].

            **Changes**: New in Zulip 10.0 (feature level 301).

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values
            [system-groups]: /api/group-setting-values#system-groups

        can_leave_group : typing.Optional[UpdateUserGroupRequestCanLeaveGroup]
            The set of users who have permission to leave this user group
            expressed as an [update to a group-setting value][update-group-setting].

            **Changes**: New in Zulip 10.0 (feature level 308).

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values
            [system-groups]: /api/group-setting-values#system-groups

        can_manage_group : typing.Optional[UpdateUserGroupRequestCanManageGroup]
            The set of users who have permission to [manage this user group][manage-user-groups]
            expressed as an [update to a group-setting value][update-group-setting].

            This setting cannot be set to `"role:internet"` and `"role:everyone"`
            [system groups][system-groups].

            **Changes**: New in Zulip 10.0 (feature level 283).

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values
            [system-groups]: /api/group-setting-values#system-groups
            [manage-user-groups]: /help/manage-user-groups

        can_mention_group : typing.Optional[UpdateUserGroupRequestCanMentionGroup]
            The set of users who have permission to [mention this group][mentions],
            expressed as an [update to a group-setting value][update-group-setting].

            This setting cannot be set to `"role:internet"` and `"role:owners"`
            [system groups][system-groups].

            **Changes**: In Zulip 9.0 (feature level 260), this parameter was
            updated to only accept an object with the `old` and `new` fields
            described below. Prior to this feature level, this parameter could be
            either of the two forms of a [group-setting value][setting-values].

            Before Zulip 9.0 (feature level 258), this parameter could only be the
            integer form of a [group-setting value][setting-values].

            Before Zulip 8.0 (feature level 198), this parameter was named
            `can_mention_group_id`.

            New in Zulip 8.0 (feature level 191). Previously, groups could be
            mentioned only if they were not [system groups][system-groups].

            [mentions]: /help/mention-a-user-or-group
            [update-group-setting]: /api/group-setting-values#updating-group-setting-values
            [system-groups]: /api/group-setting-values#system-groups
            [setting-values]: /api/group-setting-values

        can_remove_members_group : typing.Optional[UpdateUserGroupRequestCanRemoveMembersGroup]
            The set of users who have permission to remove members from this user group
            expressed as an [update to a group-setting value][update-group-setting].

            **Changes**: New in Zulip 10.0 (feature level 324). Previously, this
            permission was controlled by the `can_manage_group` setting.

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values
            [system-groups]: /api/group-setting-values#system-groups

        deactivated : typing.Optional[bool]
            A deactivated user group can be reactivated by passing this
            parameter as `false`.

            Passing `true` does nothing as user group is deactivated
            using [`POST /user_groups/{user_group_id}/deactivate`](deactivate-user-group)
            endpoint.

            **Changes**: New in Zulip 11.0 (feature level 386).

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
        client.users.update_user_group(
            user_group_id=1,
        )
        """
        _response = self._raw_client.update_user_group(
            user_group_id,
            name=name,
            description=description,
            can_add_members_group=can_add_members_group,
            can_join_group=can_join_group,
            can_leave_group=can_leave_group,
            can_manage_group=can_manage_group,
            can_mention_group=can_mention_group,
            can_remove_members_group=can_remove_members_group,
            deactivated=deactivated,
            request_options=request_options,
        )
        return _response.data

    def get_user_groups(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetUserGroupsResponse:
        """
        Fetches all of the user groups in the organization.

        !!! warn ""

            **Note**: This endpoint is not available to
            [guest users](/help/user-roles).

        **Changes**: Prior to Zulip 12.0 (feature level 496), bot
        users were not permitted to call this endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserGroupsResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.get_user_groups()
        """
        _response = self._raw_client.get_user_groups(request_options=request_options)
        return _response.data

    def get_user_group_subgroups(
        self,
        user_group_id: int,
        *,
        direct_subgroup_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUserGroupSubgroupsResponse:
        """
        Get the subgroups of a [user group](/help/user-groups).

        **Changes**: Prior to Zulip 12.0 (feature level 496), bot
        users were not permitted to call this endpoint.

        New in Zulip 6.0 (feature level 127).

        Parameters
        ----------
        user_group_id : int
            The ID of the target user group.

        direct_subgroup_only : typing.Optional[bool]
            Whether to consider only direct subgroups of the user group
            or subgroups of subgroups also.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserGroupSubgroupsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.get_user_group_subgroups(
            user_group_id=1,
        )
        """
        _response = self._raw_client.get_user_group_subgroups(
            user_group_id, direct_subgroup_only=direct_subgroup_only, request_options=request_options
        )
        return _response.data

    def update_user_group_subgroups(
        self,
        user_group_id: int,
        *,
        delete: typing.Optional[typing.Sequence[int]] = OMIT,
        add: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Update the subgroups of a [user group](/help/user-groups).

        **Changes**: Prior to Zulip 12.0 (feature level 496), bot
        users were not permitted to call this endpoint.

        Prior to Zulip 11.0 (feature level 391), subgroups
        could not be added or removed from a deactivated group.

        New in Zulip 6.0 (feature level 127).

        Parameters
        ----------
        user_group_id : int
            The ID of the target user group.

        delete : typing.Optional[typing.Sequence[int]]
            The list of user group IDs to be removed from the user group.

        add : typing.Optional[typing.Sequence[int]]
            The list of user group IDs to be added to the user group.

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
        client.users.update_user_group_subgroups(
            user_group_id=1,
        )
        """
        _response = self._raw_client.update_user_group_subgroups(
            user_group_id, delete=delete, add=add, request_options=request_options
        )
        return _response.data

    def get_is_user_group_member(
        self,
        user_group_id: int,
        user_id: int,
        *,
        direct_member_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetIsUserGroupMemberResponse:
        """
        Check whether a user is member of user group.

        **Changes**: Prior to Zulip 12.0 (feature level 496), bot
        users were not permitted to call this endpoint.

        Prior to Zulip 12.0 (feature level 458), this endpoint
        did not support querying group membership of bot users.

        Prior to Zulip 10.0 (feature level 303),
        this would return true when passed a deactivated user
        who was a member of the user group before being deactivated.

        New in Zulip 6.0 (feature level 127).

        Parameters
        ----------
        user_group_id : int
            The ID of the target user group.

        user_id : int
            The target user's ID.

        direct_member_only : typing.Optional[bool]
            Whether to consider only the direct members of user group and not members
            of its subgroups. Default is `false`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetIsUserGroupMemberResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.get_is_user_group_member(
            user_group_id=1,
            user_id=1,
        )
        """
        _response = self._raw_client.get_is_user_group_member(
            user_group_id, user_id, direct_member_only=direct_member_only, request_options=request_options
        )
        return _response.data

    def deactivate_user_group(
        self, user_group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Deactivate a user group. Deactivated user groups cannot be
        used for mentions, permissions, or any other purpose, but can
        be reactivated or renamed.

        Deactivating user groups is preferable to deleting them from
        the database, since the deactivation model allows audit logs
        of changes to sensitive group-valued permissions to be
        maintained.

        **Changes**: New in Zulip 10.0 (feature level 290).

        Parameters
        ----------
        user_group_id : int
            The ID of the target user group.

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
        client.users.deactivate_user_group(
            user_group_id=1,
        )
        """
        _response = self._raw_client.deactivate_user_group(user_group_id, request_options=request_options)
        return _response.data

    def get_bot_api_key(
        self, bot_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBotApiKeyResponse:
        """
        Fetch the API key for a bot user. Only the bot's owner and
        organization administrators have access to a bot's API key.

        **Changes**: New in Zulip 12.0 (feature level 463).

        Parameters
        ----------
        bot_id : int
            The user ID of the target bot.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBotApiKeyResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.get_bot_api_key(
            bot_id=1,
        )
        """
        _response = self._raw_client.get_bot_api_key(bot_id, request_options=request_options)
        return _response.data

    def regenerate_bot_api_key(
        self, bot_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RegenerateBotApiKeyResponse:
        """
        Generate a new API key for a bot user. Only the bot's owner and
        organization administrators have access to a bot's API key.

        Parameters
        ----------
        bot_id : int
            The user ID of the target bot.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegenerateBotApiKeyResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.regenerate_bot_api_key(
            bot_id=1,
        )
        """
        _response = self._raw_client.regenerate_bot_api_key(bot_id, request_options=request_options)
        return _response.data


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsersClient
        """
        return self._raw_client

    async def get_attachments(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAttachmentsResponse:
        """
        Fetch metadata on files uploaded by the requesting user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAttachmentsResponse
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
            await client.users.get_attachments()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_attachments(request_options=request_options)
        return _response.data

    async def remove_attachment(
        self, attachment_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Delete an uploaded file given its attachment ID.

        Note that uploaded files that have been referenced in at least
        one message are automatically deleted once the last message
        containing a link to them is deleted (whether directly or via
        a [message retention policy](/help/message-retention-policy)).

        Uploaded files that are never used in a message are
        automatically deleted a few weeks after being uploaded.

        Attachment IDs can be contained from [GET /attachments](/api/get-attachments).

        Parameters
        ----------
        attachment_id : int
            The ID of the attachment to be deleted.

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
            await client.users.remove_attachment(
                attachment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_attachment(attachment_id, request_options=request_options)
        return _response.data

    async def get_users(
        self,
        *,
        client_gravatar: typing.Optional[bool] = None,
        include_custom_profile_fields: typing.Optional[bool] = None,
        user_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUsersResponse:
        """
        Retrieve details on users in the organization.

        By default, returns all accessible users in the organization.
        The `user_ids` query parameter can be used to limit the
        results to a specific set of user IDs.

        Optionally includes values of [custom profile fields](/help/custom-profile-fields).

        You can also [fetch details on a single user](/api/get-user).

        **Changes**: In Zulip 12.0 (feature level 437), fixed a bug
        dating to feature level 232, which caused guest users to
        receive fake backwards-compatibility users in the format
        intended for clients using `POST /register` without the
        `user_list_incomplete` client capability.

        This endpoint did not support unauthenticated
        access in organizations using the [public access
        option](/help/public-access-option) prior to Zulip 11.0
        (feature level 387).

        Parameters
        ----------
        client_gravatar : typing.Optional[bool]
            Whether the client supports computing gravatars URLs. If
            enabled, `avatar_url` will be included in the response only
            if there is a Zulip avatar, and will be `null` for users who
            are using gravatar as their avatar. This option
            significantly reduces the compressed size of user data,
            since gravatar URLs are long, random strings and thus do not
            compress well. The `client_gravatar` field is set to `true` if
            clients can compute their own gravatars.

            **Changes**: The default value of this parameter was `false`
            prior to Zulip 5.0 (feature level 92).

        include_custom_profile_fields : typing.Optional[bool]
            Whether the client wants [custom profile field](/help/custom-profile-fields)
            data to be included in the response.

            **Changes**: New in Zulip 2.1.0. Previous versions do not offer these
            data via the API.

        user_ids : typing.Optional[str]
            Limits the results to the specified user IDs. If not
            provided, the server will return all accessible users in
            the organization.

            **Changes**: New in Zulip 11.0 (feature level 384).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUsersResponse
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
            await client.users.get_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users(
            client_gravatar=client_gravatar,
            include_custom_profile_fields=include_custom_profile_fields,
            user_ids=user_ids,
            request_options=request_options,
        )
        return _response.data

    async def create_user(
        self, *, email: str, password: str, full_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateUserResponse:
        """
        Create a new user account via the API.

        !!! warn ""

            **Note**: On Zulip Cloud, this feature is available only for
            organizations on a [Zulip Cloud Standard](https://zulip.com/plans/)
            or [Zulip Cloud Plus](https://zulip.com/plans/) plan. Administrators
            can request the required `can_create_users` permission for a bot or
            user by contacting [Zulip Cloud support][support] with an
            explanation for why it is needed. Self-hosted installations can
            toggle `can_create_users` on an account using the `manage.py
            change_user_role` [management command][management-commands].

        **Changes**: Before Zulip 4.0 (feature level 36), this endpoint was
        available to all organization administrators.

        [support]: /help/contact-support
        [management-commands]: https://zulip.readthedocs.io/en/latest/production/management-commands.html

        Parameters
        ----------
        email : str
            The email address of the new user.

        password : str
            The password of the new user.

        full_name : str
            The full name of the new user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateUserResponse
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
            await client.users.create_user(
                email="username@example.com",
                password="abcd1234",
                full_name="New User",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_user(
            email=email, password=password, full_name=full_name, request_options=request_options
        )
        return _response.data

    async def reactivate_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        [Reactivates a
        user](https://zulip.com/help/deactivate-or-reactivate-a-user)
        given their user ID.

        Parameters
        ----------
        user_id : int
            The target user's ID.

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
            await client.users.reactivate_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reactivate_user(user_id, request_options=request_options)
        return _response.data

    async def get_user_status(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserStatusResponse:
        """
        Get the [status](/help/status-and-availability) currently set by a
        user in the organization.

        **Changes**: New in Zulip 9.0 (feature level 262). Previously,
        user statuses could only be fetched via the [`POST
        /register`](/api/register-queue) endpoint.

        Parameters
        ----------
        user_id : int
            The target user's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserStatusResponse
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
            await client.users.get_user_status(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_status(user_id, request_options=request_options)
        return _response.data

    async def update_status_for_user(
        self,
        user_id: int,
        *,
        status_text: typing.Optional[str] = OMIT,
        emoji_name: typing.Optional[str] = OMIT,
        emoji_code: typing.Optional[str] = OMIT,
        reaction_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Administrator endpoint for changing the [status](/help/status-and-availability) of
        another user.

        **Changes**: Prior to Zulip 12.0 (feature level 473), only
        bots could not access this API endpoint, regardless of the
        role of the bot.

        New in Zulip 11.0 (feature level 407).

        Parameters
        ----------
        user_id : int
            The target user's ID.

        status_text : typing.Optional[str]
            The text content of the status message. Sending the empty string
            will clear the user's status.

            **Note**: The limit on the size of the message is 60 Unicode code points.

        emoji_name : typing.Optional[str]
            The name for the emoji to associate with this status.

            **Changes**: New in Zulip 5.0 (feature level 86).

        emoji_code : typing.Optional[str]
            A unique identifier, defining the specific emoji codepoint requested,
            within the namespace of the `reaction_type`.

            **Changes**: New in Zulip 5.0 (feature level 86).

        reaction_type : typing.Optional[str]
            A string indicating the type of emoji. Each emoji `reaction_type`
            has an independent namespace for values of `emoji_code`.

            Must be one of the following values:

            - `unicode_emoji` : In this namespace, `emoji_code` will be a
              dash-separated hex encoding of the sequence of Unicode codepoints
              that define this emoji in the Unicode specification.

            - `realm_emoji` : In this namespace, `emoji_code` will be the ID of
              the uploaded [custom emoji](/help/custom-emoji).

            - `zulip_extra_emoji` : These are special emoji included with Zulip.
              In this namespace, `emoji_code` will be the name of the emoji (e.g.
              "zulip").

            **Changes**: New in Zulip 5.0 (feature level 86).

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
            await client.users.update_status_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_status_for_user(
            user_id,
            status_text=status_text,
            emoji_name=emoji_name,
            emoji_code=emoji_code,
            reaction_type=reaction_type,
            request_options=request_options,
        )
        return _response.data

    async def get_user_presence(
        self, user_id_or_email: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserPresenceResponse:
        """
        Get the presence status for a specific user.

        This endpoint is most useful for embedding data about a user's
        presence status in other sites (e.g. an employee directory). Full
        Zulip clients like mobile/desktop apps will want to use the [main
        presence endpoint](/api/get-presence), which returns data for all
        active users in the organization, instead.

        Parameters
        ----------
        user_id_or_email : str
            The ID or Zulip API email address of the user whose presence you want to fetch.

            **Changes**: New in Zulip 4.0 (feature level 43). Previous versions only supported
            identifying the user by Zulip API email.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserPresenceResponse
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
            await client.users.get_user_presence(
                user_id_or_email="iago@zulip.com",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_presence(user_id_or_email, request_options=request_options)
        return _response.data

    async def get_own_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetOwnUserResponse:
        """
        Get basic data about the user/bot that requests this endpoint.

        **Changes**: Removed `is_billing_admin` field in Zulip 10.0 (feature level 363), as it was
        replaced by the `can_manage_billing_group` realm setting.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetOwnUserResponse
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
            await client.users.get_own_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_own_user(request_options=request_options)
        return _response.data

    async def deactivate_own_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> JsonSuccess:
        """
        Deactivates the current user's account. See also the administrative endpoint for
        [deactivating another user](/api/deactivate-user).

        This endpoint is primarily useful to Zulip clients providing a user settings UI.

        Parameters
        ----------
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
            await client.users.deactivate_own_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.deactivate_own_user(request_options=request_options)
        return _response.data

    async def regenerate_api_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RegenerateApiKeyResponse:
        """
        !!! warn ""

             **Note**: Users should treat their Zulip API key as
             [carefully as they would their password](/help/protect-your-account).

        Generate a new API key for the user making the request.

        Changing a user's API key will immediately log them out of Zulip
        on devices registered for [mobile push notifications][mobile-push].

        **Changes**: Before Zulip 12.0 (feature level 492),
        regenerating a user's API key didn't remove all of the user's
        [E2EE push device registrations](/api/register-push-device),
        so E2EE push notifications could still be sent.

        [mobile-push]: https://zulip.readthedocs.io/en/latest/production/mobile-push-notifications.html

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegenerateApiKeyResponse
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
            await client.users.regenerate_api_key()


        asyncio.run(main())
        """
        _response = await self._raw_client.regenerate_api_key(request_options=request_options)
        return _response.data

    async def get_alert_words(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAlertWordsResponse:
        """
        Get all of the user's configured [alert words][alert-words].

        [alert-words]: /help/dm-mention-alert-notifications#alert-words

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAlertWordsResponse
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
            await client.users.get_alert_words()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_alert_words(request_options=request_options)
        return _response.data

    async def add_alert_words(
        self, *, alert_words: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> AddAlertWordsResponse:
        """
        Add words (or phrases) to the user's set of configured [alert words][alert-words].

        [alert-words]: /help/dm-mention-alert-notifications#alert-words

        Parameters
        ----------
        alert_words : typing.Sequence[str]
            An array of strings to be added to the user's set of configured
            alert words. Strings already present in the user's set of alert words
            already are ignored.

            Alert words are case insensitive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddAlertWordsResponse
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
            await client.users.add_alert_words(
                alert_words=["foo", "bar"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_alert_words(alert_words=alert_words, request_options=request_options)
        return _response.data

    async def remove_alert_words(
        self, *, alert_words: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> RemoveAlertWordsResponse:
        """
        Remove words (or phrases) from the user's set of configured [alert words][alert-words].

        Alert words are case insensitive.

        [alert-words]: /help/dm-mention-alert-notifications#alert-words

        Parameters
        ----------
        alert_words : typing.Sequence[str]
            An array of strings to be removed from the user's set of configured
            alert words. Strings that are not in the user's set of alert words
            are ignored.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoveAlertWordsResponse
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
            await client.users.remove_alert_words(
                alert_words=["foo"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_alert_words(alert_words=alert_words, request_options=request_options)
        return _response.data

    async def update_presence(
        self,
        *,
        status: UpdatePresenceRequestStatus,
        last_update_id: typing.Optional[int] = OMIT,
        history_limit_days: typing.Optional[int] = OMIT,
        new_user_input: typing.Optional[bool] = OMIT,
        ping_only: typing.Optional[bool] = OMIT,
        slim_presence: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdatePresenceResponse:
        """
        Update the current user's [presence][availability] and fetch presence data
        of other users in the organization.

        This endpoint is meant to be used by clients for both:

        - Reporting the current user's presence status (`"active"` or `"idle"`)
          to the server.

        - Obtaining the presence data of all other users in the organization via
          regular polling.

        Accurate user presence is one of the most expensive parts of any
        chat application (in terms of bandwidth and other resources). Therefore,
        it is important that clients implementing Zulip's user presence system
        use the modern [`last_update_id`](#parameter-last_update_id) protocol to
        minimize fetching duplicate user presence data.

        Client apps implementing presence are recommended to also consume [`presence`
        events](/api/get-events#presence)), in order to learn about newly online users
        immediately.

        The Zulip server is responsible for implementing [invisible mode][invisible],
        which disables sharing a user's presence data. Nonetheless, clients
        should check the `presence_enabled` field in user objects in order to
        display the current user as online or offline based on whether they are
        sharing their presence information.

        **Changes**: As of Zulip 8.0 (feature level 228), if the
        `CAN_ACCESS_ALL_USERS_GROUP_LIMITS_PRESENCE` server-level setting is
        `true`, then user presence data in the response is [limited to users
        the current user can see/access][limit-visibility].

        [limit-visibility]: /help/guest-users#configure-whether-guests-can-see-all-other-users
        [invisible]: /help/status-and-availability#invisible-mode
        [availability]: /help/status-and-availability#availability

        Parameters
        ----------
        status : UpdatePresenceRequestStatus
            The status of the user on this client.

            Clients should report the user as `"active"` on this device if the client
            knows that the user is presently using the device (and thus would
            potentially see a notification immediately), even if the user
            has not directly interacted with the Zulip client.

            Otherwise, it should report the user as `"idle"`.

            See the related [`new_user_input`](#parameter-new_user_input) parameter
            for how a client should report whether the user is actively using the
            Zulip client.

        last_update_id : typing.Optional[int]
            The identifier that specifies what presence data the client already
            has received, which allows the server to only return more recent
            user presence data.

            This should be set to `-1` during initialization of the client in
            order to fetch all user presence data, unless the client is obtaining
            initial user presence metadata from the
            [`POST /register`](/api/register-queue) endpoint.

            In subsequent queries to this endpoint, this value should be set to the
            most recent value of `presence_last_update_id` returned by the server
            in this endpoint's response, which implements incremental fetching
            of user presence data.

            When this parameter is passed, the user presence data in the response
            will always be in the modern format.

            **Changes**: New in Zulip 9.0 (feature level 263). Previously, the
            server sent user presence data for all users who had been active in the
            last two weeks unconditionally.

        history_limit_days : typing.Optional[int]
            Limits how far back in time to fetch user presence data. If not specified,
            defaults to 14 days. A value of N means that the oldest presence data
            fetched will be from at most N days ago.

            Note that this is only useful during the initial user presence data fetch,
            as subsequent fetches should use the `last_update_id` parameter, which
            will act as the limit on how much presence data is returned. `history_limit_days`
            is ignored if `last_update_id` is passed with a value greater than `0`,
            indicating that the client already has some presence data.

            **Changes**: New in Zulip 10.0 (feature level 288).

        new_user_input : typing.Optional[bool]
            Whether the user has interacted with the client (e.g. moved the mouse,
            used the keyboard, etc.) since the previous presence request from this
            client.

            The server uses data from this parameter to implement certain [usage
            statistics](/help/analytics).

            User interface clients that might run in the background, without the
            user ever interacting with them, should be careful to only pass `true`
            if the user has actually interacted with the client in order to avoid
            corrupting usage statistics graphs.

        ping_only : typing.Optional[bool]
            Whether the client is sending a ping-only request, meaning it only
            wants to update the user's presence `status` on the server.

            Otherwise, also requests the server return user presence data for all
            users in the organization, which is further specified by the
            [`last_update_id`](#parameter-last_update_id) parameter.

        slim_presence : typing.Optional[bool]
            Legacy parameter for configuring the format (modern or legacy) in
            which the server will return user presence data for the organization.

            Modern clients should use
            [`last_update_id`](#parameter-last_update_id), which guarantees that
            user presence data will be returned in the modern format, and
            should not pass this parameter as `true` unless interacting with an
            older server.

            Legacy clients that do not yet support `last_update_id` may use the
            value of `true` to request the modern format for user presence data.

            **Note**: The legacy format for user presence data will be removed
            entirely in a future release.

            **Changes**: **Deprecated** in Zulip 9.0 (feature level 263). Using
            the modern `last_update_id` parameter is the recommended way to
            request the modern format for user presence data.

            New in Zulip 3.0 (no feature level as it was an unstable API at that
            point).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdatePresenceResponse
            Success.

        Examples
        --------
        import asyncio

        from fern.users import UpdatePresenceRequestStatus

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.users.update_presence(
                status=UpdatePresenceRequestStatus.IDLE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_presence(
            status=status,
            last_update_id=last_update_id,
            history_limit_days=history_limit_days,
            new_user_input=new_user_input,
            ping_only=ping_only,
            slim_presence=slim_presence,
            request_options=request_options,
        )
        return _response.data

    async def remove_profile_data(
        self, *, data: typing.Sequence[int], request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Remove the current user's [profile data](/help/edit-your-profile) for
        one or more of the [custom profile fields](/help/custom-profile-fields)
        configured in the organization.

        Parameters
        ----------
        data : typing.Sequence[int]
            An array of custom profile field IDs to remove any data set for
            the user.

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
            await client.users.remove_profile_data(
                data=[1],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_profile_data(data=data, request_options=request_options)
        return _response.data

    async def update_profile_data(
        self, *, data: typing.Sequence[ProfileDataUpdate], request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Update the current user's [profile data](/help/edit-your-profile) for
        one or more of the [custom profile fields](/help/custom-profile-fields)
        configured in the organization.

        Parameters
        ----------
        data : typing.Sequence[ProfileDataUpdate]
            An array of objects describing updates to the custom profile
            field data for the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ProfileDataUpdate

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.users.update_profile_data(
                data=[
                    ProfileDataUpdate(
                        id=4,
                        value="0",
                    ),
                    ProfileDataUpdate(
                        id=5,
                        value="1909-04-05",
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_profile_data(data=data, request_options=request_options)
        return _response.data

    async def update_status(
        self,
        *,
        status_text: typing.Optional[str] = OMIT,
        away: typing.Optional[bool] = OMIT,
        emoji_name: typing.Optional[str] = OMIT,
        emoji_code: typing.Optional[str] = OMIT,
        reaction_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Change your [status](/help/status-and-availability).

        A request to this endpoint will only change the parameters passed.
        For example, passing just `status_text` requests a change in the status
        text, but will leave the status emoji unchanged.

        Clients that wish to set the user's status to a specific value should
        pass all supported parameters.

        **Changes**: In Zulip 5.0 (feature level 86), added support for
        `emoji_name`, `emoji_code`, and `reaction_type` parameters.

        Parameters
        ----------
        status_text : typing.Optional[str]
            The text content of the status message. Sending the empty string
            will clear the user's status.

            **Note**: The limit on the size of the message is 60 Unicode code points.

        away : typing.Optional[bool]
            Whether the user should be marked as "away".

            **Changes**: Deprecated in Zulip 6.0 (feature level 148);
            starting with that feature level, `away` is a legacy way to
            access the user's `presence_enabled` setting, with
            `away = !presence_enabled`. To be removed in a future release.

        emoji_name : typing.Optional[str]
            The name for the emoji to associate with this status.

            **Changes**: New in Zulip 5.0 (feature level 86).

        emoji_code : typing.Optional[str]
            A unique identifier, defining the specific emoji codepoint requested,
            within the namespace of the `reaction_type`.

            **Changes**: New in Zulip 5.0 (feature level 86).

        reaction_type : typing.Optional[str]
            A string indicating the type of emoji. Each emoji `reaction_type`
            has an independent namespace for values of `emoji_code`.

            Must be one of the following values:

            - `unicode_emoji` : In this namespace, `emoji_code` will be a
              dash-separated hex encoding of the sequence of Unicode codepoints
              that define this emoji in the Unicode specification.

            - `realm_emoji` : In this namespace, `emoji_code` will be the ID of
              the uploaded [custom emoji](/help/custom-emoji).

            - `zulip_extra_emoji` : These are special emoji included with Zulip.
              In this namespace, `emoji_code` will be the name of the emoji (e.g.
              "zulip").

            **Changes**: New in Zulip 5.0 (feature level 86).

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
            await client.users.update_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_status(
            status_text=status_text,
            away=away,
            emoji_name=emoji_name,
            emoji_code=emoji_code,
            reaction_type=reaction_type,
            request_options=request_options,
        )
        return _response.data

    async def mute_user(
        self, muted_user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        [Mute a user](/help/mute-a-user) from the perspective of the requesting
        user. Messages sent by muted users will be automatically marked as read
        and hidden for the user who muted them.

        Muted users should be implemented by clients as follows:

        - The server will immediately mark all messages sent by the muted
          user as read. This will automatically clear any existing mobile
          push notifications related to the muted user.
        - The server will mark any new messages sent by the muted user as read
          for the requesting user's account, which prevents all email and mobile
          push notifications.
        - Clients should exclude muted users from presence lists or other UI
          for viewing or composing one-on-one direct messages. One-on-one direct
          messages sent by muted users should be hidden everywhere in the Zulip UI.
        - Channel messages and group direct messages sent by the muted
          user should avoid displaying the content and name/avatar,
          but should display that N messages by a muted user were
          hidden (so that it is possible to interpret the messages by
          other users who are talking with the muted user).
        - Group direct message conversations including the muted user
          should display muted users as "Muted user", rather than
          showing their name, in lists of such conversations, along with using
          a blank grey avatar where avatars are displayed.
        - Administrative/settings UI elements for showing "All users that exist
          on this channel or realm", e.g. for organization
          administration or showing channel subscribers, should display
          the user's name as normal.

        **Changes**: New in Zulip 4.0 (feature level 48).

        Parameters
        ----------
        muted_user_id : int
            The ID of the user to mute/unmute.

            **Changes**: Before Zulip 8.0 (feature level 188), bot users could not
            be muted/unmuted, and specifying a bot user's ID returned an error response.

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
            await client.users.mute_user(
                muted_user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mute_user(muted_user_id, request_options=request_options)
        return _response.data

    async def unmute_user(
        self, muted_user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        [Unmute a user](/help/mute-a-user#see-your-list-of-muted-users)
        from the perspective of the requesting user.

        **Changes**: New in Zulip 4.0 (feature level 48).

        Parameters
        ----------
        muted_user_id : int
            The ID of the user to mute/unmute.

            **Changes**: Before Zulip 8.0 (feature level 188), bot users could not
            be muted/unmuted, and specifying a bot user's ID returned an error response.

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
            await client.users.unmute_user(
                muted_user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unmute_user(muted_user_id, request_options=request_options)
        return _response.data

    async def add_apns_token(
        self, *, token: str, appid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        This endpoint adds an APNs device token to register for iOS push notifications.

        **Changes**: Deprecated in Zulip 11.0 (feature level 406). Clients connecting
        to newer servers and with E2EE push notifications support should use the
        [Register E2EE push device](/api/register-push-device) endpoint, as this
        endpoint will be removed in a future release.

        Parameters
        ----------
        token : str
            The token provided by the device.

        appid : str
            The ID of the Zulip app that is making the request.

            **Changes**: In Zulip 8.0 (feature level 223), this parameter was made
            required. Previously, if it was unspecified, the server would use a default
            value (based on the `ZULIP_IOS_APP_ID` server setting, which
            defaulted to `"org.zulip.Zulip"`).

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
            await client.users.add_apns_token(
                token="c0ffee",
                appid="org.zulip.Zulip",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_apns_token(token=token, appid=appid, request_options=request_options)
        return _response.data

    async def remove_apns_token(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        This endpoint removes an APNs device token for iOS push notifications.

        **Changes**: Deprecated in Zulip 11.0 (feature level 406) and will be
        removed in a future release. Clients connecting to newer servers and
        with E2EE push notifications support should delete the account record
        in their local accounts table that corresponds to the `push_account_id`
        supplied when registering via the [Register E2EE push device](/api/register-push-device)
        endpoint, to stop displaying notifications for that registration.

        Parameters
        ----------
        token : str
            The token provided by the device.

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
            await client.users.remove_apns_token(
                token="c0ffee",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_apns_token(token=token, request_options=request_options)
        return _response.data

    async def add_fcm_token(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        This endpoint adds an FCM registration token for push notifications.

        **Changes**: Deprecated in Zulip 11.0 (feature level 406). Clients connecting
        to newer servers and with E2EE push notifications support should use the
        [Register E2EE push device](/api/register-push-device) endpoint, as this
        endpoint will be removed in a future release.

        Parameters
        ----------
        token : str
            The token provided by the device.

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
            await client.users.add_fcm_token(
                token="android-token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_fcm_token(token=token, request_options=request_options)
        return _response.data

    async def remove_fcm_token(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        This endpoint removes an FCM registration token for push notifications.

        **Changes**: Deprecated in Zulip 11.0 (feature level 406) and will be
        removed in a future release. Clients connecting to newer servers and
        with E2EE push notifications support should delete the account record
        in their local accounts table that corresponds to the `push_account_id`
        supplied when registering via the [Register E2EE push device](/api/register-push-device)
        endpoint, to stop displaying notifications for that registration.

        Parameters
        ----------
        token : str
            The token provided by the device.

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
            await client.users.remove_fcm_token(
                token="android-token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_fcm_token(token=token, request_options=request_options)
        return _response.data

    async def upload_avatar(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> UploadAvatarResponse:
        """
        Upload a new [profile picture](/help/change-your-profile-picture)
        for the current user.

        The maximum allowed file size is available in the `max_avatar_file_size_mib`
        field in the [`POST /register`](/api/register-queue) response.

        In organizations that
        [restrict profile picture changes](/help/restrict-profile-picture-changes),
        only administrators can use this endpoint.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadAvatarResponse
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
            await client.users.upload_avatar()


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_avatar(file=file, request_options=request_options)
        return _response.data

    async def delete_avatar(self, *, request_options: typing.Optional[RequestOptions] = None) -> DeleteAvatarResponse:
        """
        Delete the current user's uploaded [profile picture](/help/change-your-profile-picture),
        reverting to the organization's
        [default style for profile pictures](/help/configure-default-profile-pictures).

        This endpoint is idempotent: if the current user has not uploaded a
        custom profile picture, the request succeeds without making any
        changes.

        In organizations that
        [restrict profile picture changes](/help/restrict-profile-picture-changes),
        only administrators can use this endpoint.

        **Changes**: Prior to Zulip 12.0 (feature level 443), this endpoint
        was not idempotent; calling it when the current user had not
        uploaded a custom profile picture would still increment their
        avatar version and send a redundant user update event to
        clients.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAvatarResponse
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
            await client.users.delete_avatar()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_avatar(request_options=request_options)
        return _response.data

    async def get_user_by_email(
        self,
        email: str,
        *,
        client_gravatar: typing.Optional[bool] = None,
        include_custom_profile_fields: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUserByEmailResponse:
        """
        Fetch details for a single user in the organization given a Zulip
        API email address.

        You can also fetch details on [all users in the organization](/api/get-users)
        or [by user ID](/api/get-user).

        Fetching by user ID is generally recommended when possible,
        as a user might [change their email address](/help/change-your-email-address)
        or change their [email address visibility](/help/configure-email-visibility),
        either of which could change the client's ability to look them up by that
        email address.

        **Changes**: In Zulip 12.0 (feature level 437), fixed a bug
        dating to feature level 232, which caused guest users to
        receive fake backwards-compatibility users in the format
        intended for clients using `POST /register` without the
        `user_list_incomplete` client capability.

        Starting with Zulip 10.0 (feature level 302), the real email
        address can be used in the `email` parameter and will fetch the target user's
        data if and only if the target's email visibility setting permits the requester
        to see the email address.
        The dummy email addresses of the form `user{id}@{realm.host}` still work, and
        will now work for **all** users, via identifying them by the embedded user ID.

        New in Zulip Server 4.0 (feature level 39).

        Parameters
        ----------
        email : str
            The email address of the user to fetch. Two forms are supported:

            - The real email address of the user (`delivery_email`). The lookup will
              succeed if and only if the user exists and their email address visibility
              setting permits the client to see the email address.

            - The dummy Zulip API email address of the form `user{user_id}@{realm_host}`. This
              is identical to simply [getting user by ID](/api/get-user). If the server or
              realm change domains, the dummy email address used has to be adjustment to
              match the new realm domain. This is legacy behavior for
              backwards-compatibility, and will be removed in a future release.

            **Changes**: Starting with Zulip 10.0 (feature level 302), lookups by real email
            address match the semantics of the target's email visibility setting and dummy
            email addresses work for all users, independently of their email visibility
            setting.

            Previously, lookups were done only using the Zulip API email addresses.

        client_gravatar : typing.Optional[bool]
            Whether the client supports computing gravatars URLs. If
            enabled, `avatar_url` will be included in the response only
            if there is a Zulip avatar, and will be `null` for users who
            are using gravatar as their avatar. This option
            significantly reduces the compressed size of user data,
            since gravatar URLs are long, random strings and thus do not
            compress well. The `client_gravatar` field is set to `true` if
            clients can compute their own gravatars.

            **Changes**: The default value of this parameter was `false`
            prior to Zulip 5.0 (feature level 92).

        include_custom_profile_fields : typing.Optional[bool]
            Whether the client wants [custom profile field](/help/custom-profile-fields)
            data to be included in the response.

            **Changes**: New in Zulip 2.1.0. Previous versions do not offer these
            data via the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserByEmailResponse
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
            await client.users.get_user_by_email(
                email="iago@zulip.com",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_by_email(
            email,
            client_gravatar=client_gravatar,
            include_custom_profile_fields=include_custom_profile_fields,
            request_options=request_options,
        )
        return _response.data

    async def update_user_by_email(
        self,
        email: str,
        *,
        full_name: typing.Optional[str] = OMIT,
        role: typing.Optional[int] = OMIT,
        profile_data: typing.Optional[typing.Sequence[ProfileDataUpdate]] = OMIT,
        new_email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Administrative endpoint to update the details of another user in the organization by their email address.
        Works the same way as [`PATCH /users/{user_id}`](/api/update-user) but fetching the target user by their
        real email address.

        The requester needs to have permission to view the target user's real email address, subject to the
        user's email address visibility setting. Otherwise, the dummy address of the format
        `user{id}@{realm.host}` needs be used. This follows the same rules as `GET /users/{email}`.

        **Changes**: New in Zulip 10.0 (feature level 313).

        Parameters
        ----------
        email : str
            The email address of the user, specified following the same rules as
            [`GET /users/{email}`](/api/get-user-by-email).

        full_name : typing.Optional[str]
            The user's full name.

            **Changes**: Removed unnecessary JSON-encoding of this parameter in
            Zulip 5.0 (feature level 106).

        role : typing.Optional[int]
            New [role](/api/roles-and-permissions) for the user. Roles are encoded as:

            - Organization owner: 100
            - Organization administrator: 200
            - Organization moderator: 300
            - Member: 400
            - Guest: 600

            Only organization owners can add or remove the owner role.

            The owner role cannot be removed from the only organization owner.

            **Changes**: New in Zulip 3.0 (feature level 8), replacing the previous
            pair of `is_admin` and `is_guest` boolean parameters. Organization moderator
            role added in Zulip 4.0 (feature level 60).

        profile_data : typing.Optional[typing.Sequence[ProfileDataUpdate]]
            An array of objects describing updates to the [custom profile
            field](/help/custom-profile-fields) data for the user.

        new_email : typing.Optional[str]
            New email address for the user. Requires the user making the request
            to be an organization owner and additionally have the `.can_change_user_emails`
            special permission.

            **Changes**: New in Zulip 10.0 (feature level 285).

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
            await client.users.update_user_by_email(
                email="hamlet@zulip.com",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user_by_email(
            email,
            full_name=full_name,
            role=role,
            profile_data=profile_data,
            new_email=new_email,
            request_options=request_options,
        )
        return _response.data

    async def get_user(
        self,
        user_id: int,
        *,
        client_gravatar: typing.Optional[bool] = None,
        include_custom_profile_fields: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUserResponse:
        """
        Fetch details for a single user in the organization.

        You can also fetch details on [all users in the organization](/api/get-users)
        or [by a user's Zulip API email](/api/get-user-by-email).

        **Changes**: In Zulip 12.0 (feature level 437), fixed a bug
        dating to feature level 232, which caused guest users to
        receive fake backwards-compatibility users in the format
        intended for clients using `POST /register` without the
        `user_list_incomplete` client capability.

        New in Zulip 3.0 (feature level 1).

        Parameters
        ----------
        user_id : int
            The target user's ID.

        client_gravatar : typing.Optional[bool]
            Whether the client supports computing gravatars URLs. If
            enabled, `avatar_url` will be included in the response only
            if there is a Zulip avatar, and will be `null` for users who
            are using gravatar as their avatar. This option
            significantly reduces the compressed size of user data,
            since gravatar URLs are long, random strings and thus do not
            compress well. The `client_gravatar` field is set to `true` if
            clients can compute their own gravatars.

            **Changes**: The default value of this parameter was `false`
            prior to Zulip 5.0 (feature level 92).

        include_custom_profile_fields : typing.Optional[bool]
            Whether the client wants [custom profile field](/help/custom-profile-fields)
            data to be included in the response.

            **Changes**: New in Zulip 2.1.0. Previous versions do not offer these
            data via the API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserResponse
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
            await client.users.get_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user(
            user_id,
            client_gravatar=client_gravatar,
            include_custom_profile_fields=include_custom_profile_fields,
            request_options=request_options,
        )
        return _response.data

    async def deactivate_user(
        self,
        user_id: int,
        *,
        actions: typing.Optional[str] = None,
        deactivation_notification_comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        [Deactivates a
        user](https://zulip.com/help/deactivate-or-reactivate-a-user)
        given their user ID.

        Note that any bots controlled by the user will be deactivated
        before the user; clients that don't want this behavior are
        expected to prompt the user to adjust the bot's owners before
        making this API request.

        Parameters
        ----------
        user_id : int
            The target user's ID.

        actions : typing.Optional[str]
            Additional actions for the server to perform while deactivating the user.

            As with the actual deactivation, actions are first applied
            to any bots controlled by the target user, and then to the
            target user.

            **Changes**: New in Zulip 12.0 (feature level 459).

        deactivation_notification_comment : typing.Optional[str]
            If not `null`, requests that the deactivated user receive
            a notification email about their account deactivation.

            If not `""`, encodes custom text written by the administrator
            to be included in the notification email.

            **Changes**: New in Zulip 5.0 (feature level 135).

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
            await client.users.deactivate_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deactivate_user(
            user_id,
            actions=actions,
            deactivation_notification_comment=deactivation_notification_comment,
            request_options=request_options,
        )
        return _response.data

    async def update_user(
        self,
        user_id: int,
        *,
        full_name: typing.Optional[str] = OMIT,
        role: typing.Optional[int] = OMIT,
        profile_data: typing.Optional[typing.Sequence[ProfileDataUpdate]] = OMIT,
        new_email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Administrative endpoint to update the details of another user in the organization.

        Supports everything an administrator can do to edit details of another
        user's account, including editing full name,
        [role](/help/user-roles), and [custom profile
        fields](/help/custom-profile-fields).

        Parameters
        ----------
        user_id : int
            The target user's ID.

        full_name : typing.Optional[str]
            The user's full name.

            **Changes**: Removed unnecessary JSON-encoding of this parameter in
            Zulip 5.0 (feature level 106).

        role : typing.Optional[int]
            New [role](/api/roles-and-permissions) for the user. Roles are encoded as:

            - Organization owner: 100
            - Organization administrator: 200
            - Organization moderator: 300
            - Member: 400
            - Guest: 600

            Only organization owners can add or remove the owner role.

            The owner role cannot be removed from the only organization owner.

            **Changes**: New in Zulip 3.0 (feature level 8), replacing the previous
            pair of `is_admin` and `is_guest` boolean parameters. Organization moderator
            role added in Zulip 4.0 (feature level 60).

        profile_data : typing.Optional[typing.Sequence[ProfileDataUpdate]]
            An array of objects describing updates to the [custom profile
            field](/help/custom-profile-fields) data for the user.

        new_email : typing.Optional[str]
            New email address for the user. Requires the user making the request
            to be an organization owner and additionally have the `.can_change_user_emails`
            special permission.

            **Changes**: New in Zulip 10.0 (feature level 285).

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
            await client.users.update_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user(
            user_id,
            full_name=full_name,
            role=role,
            profile_data=profile_data,
            new_email=new_email,
            request_options=request_options,
        )
        return _response.data

    async def update_settings(
        self,
        *,
        target_users: typing.Optional[UpdateSettingsRequestTargetUsers] = OMIT,
        full_name: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        old_password: typing.Optional[str] = OMIT,
        new_password: typing.Optional[str] = OMIT,
        twenty_four_hour_time: typing.Optional[bool] = OMIT,
        web_mark_read_on_scroll_policy: typing.Optional[int] = OMIT,
        web_channel_default_view: typing.Optional[int] = OMIT,
        starred_message_counts: typing.Optional[bool] = OMIT,
        receives_typing_notifications: typing.Optional[bool] = OMIT,
        web_suggest_update_timezone: typing.Optional[bool] = OMIT,
        fluid_layout_width: typing.Optional[bool] = OMIT,
        high_contrast_mode: typing.Optional[bool] = OMIT,
        web_font_size_px: typing.Optional[int] = OMIT,
        web_line_height_percent: typing.Optional[int] = OMIT,
        color_scheme: typing.Optional[int] = OMIT,
        enable_drafts_synchronization: typing.Optional[bool] = OMIT,
        translate_emoticons: typing.Optional[bool] = OMIT,
        display_emoji_reaction_users: typing.Optional[bool] = OMIT,
        default_language: typing.Optional[str] = OMIT,
        web_home_view: typing.Optional[str] = OMIT,
        web_escape_navigates_to_home_view: typing.Optional[bool] = OMIT,
        left_side_userlist: typing.Optional[bool] = OMIT,
        emojiset: typing.Optional[str] = OMIT,
        demote_inactive_streams: typing.Optional[int] = OMIT,
        user_list_style: typing.Optional[int] = OMIT,
        web_animate_image_previews: typing.Optional[UpdateSettingsRequestWebAnimateImagePreviews] = OMIT,
        web_stream_unreads_count_display_policy: typing.Optional[int] = OMIT,
        hide_ai_features: typing.Optional[bool] = OMIT,
        web_inbox_show_channel_folders: typing.Optional[bool] = OMIT,
        web_left_sidebar_show_channel_folders: typing.Optional[bool] = OMIT,
        web_left_sidebar_unreads_count_summary: typing.Optional[bool] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        enable_stream_desktop_notifications: typing.Optional[bool] = OMIT,
        enable_stream_email_notifications: typing.Optional[bool] = OMIT,
        enable_stream_push_notifications: typing.Optional[bool] = OMIT,
        enable_stream_audible_notifications: typing.Optional[bool] = OMIT,
        notification_sound: typing.Optional[str] = OMIT,
        enable_desktop_notifications: typing.Optional[bool] = OMIT,
        enable_sounds: typing.Optional[bool] = OMIT,
        email_notifications_batching_period_seconds: typing.Optional[int] = OMIT,
        enable_offline_email_notifications: typing.Optional[bool] = OMIT,
        enable_offline_push_notifications: typing.Optional[bool] = OMIT,
        enable_online_push_notifications: typing.Optional[bool] = OMIT,
        enable_followed_topic_desktop_notifications: typing.Optional[bool] = OMIT,
        enable_followed_topic_email_notifications: typing.Optional[bool] = OMIT,
        enable_followed_topic_push_notifications: typing.Optional[bool] = OMIT,
        enable_followed_topic_audible_notifications: typing.Optional[bool] = OMIT,
        enable_digest_emails: typing.Optional[bool] = OMIT,
        enable_marketing_emails: typing.Optional[bool] = OMIT,
        enable_login_emails: typing.Optional[bool] = OMIT,
        message_content_in_email_notifications: typing.Optional[bool] = OMIT,
        pm_content_in_desktop_notifications: typing.Optional[bool] = OMIT,
        wildcard_mentions_notify: typing.Optional[bool] = OMIT,
        enable_followed_topic_wildcard_mentions_notify: typing.Optional[bool] = OMIT,
        desktop_icon_count_display: typing.Optional[int] = OMIT,
        realm_name_in_email_notifications_policy: typing.Optional[int] = OMIT,
        automatically_follow_topics_policy: typing.Optional[int] = OMIT,
        automatically_unmute_topics_in_muted_streams_policy: typing.Optional[int] = OMIT,
        automatically_follow_topics_where_mentioned: typing.Optional[bool] = OMIT,
        resolved_topic_notice_auto_read_policy: typing.Optional[
            UpdateSettingsRequestResolvedTopicNoticeAutoReadPolicy
        ] = OMIT,
        presence_enabled: typing.Optional[bool] = OMIT,
        enter_sends: typing.Optional[bool] = OMIT,
        send_private_typing_notifications: typing.Optional[bool] = OMIT,
        send_stream_typing_notifications: typing.Optional[bool] = OMIT,
        send_read_receipts: typing.Optional[bool] = OMIT,
        allow_private_data_export: typing.Optional[bool] = OMIT,
        email_address_visibility: typing.Optional[int] = OMIT,
        web_navigate_to_sent_message: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IgnoredParametersSuccess:
        """
        This endpoint is used to edit the current user's settings.

        When invoked by a realm admin, it supports bulk updates to
        settings for specified users or members of user groups using
        the `target_users` parameter.

        **Changes**: Removed `dense_mode` setting in Zulip 10.0 (feature level 364)
        as we now have `web_font_size_px` and `web_line_height_percent`
        settings for more control.

        Prior to Zulip 5.0 (feature level 80), this endpoint only
        supported the `full_name`, `email`, `old_password`, and
        `new_password` parameters. Notification settings were
        managed by `PATCH /settings/notifications`, and all other
        settings by `PATCH /settings/display`.

        The feature level 80 migration to merge these endpoints did not
        change how request parameters are encoded. However, it did change
        the handling of any invalid parameters present in a request
        (see feature level 78 change below).

        As of feature level 80, the `PATCH /settings/display` and
        `PATCH /settings/notifications` endpoints are deprecated aliases
        for this endpoint for backwards-compatibility, and will be removed
        once clients have migrated to use this endpoint.

        Prior to Zulip 5.0 (feature level 78), this endpoint indicated
        which parameters it had processed by including in the response
        object `"key": value` entries for values successfully changed by
        the request. That was replaced by the more ergonomic
        [`ignored_parameters_unsupported`][ignored-parameters] array.

        The `PATCH /settings/notifications` and `PATCH /settings/display`
        endpoints also had this behavior of indicating processed parameters
        before they became aliases of this endpoint in Zulip 5.0 (see
        feature level 80 change above).

        Before feature level 78, request parameters that were not supported
        (or were unchanged) were silently ignored.

        [ignored-parameters]: /api/rest-error-handling#ignored-parameters

        Parameters
        ----------
        target_users : typing.Optional[UpdateSettingsRequestTargetUsers]
            An object specifying the collection of users whose settings should be modified,
            for modification of other users' settings by an organization administrator.
            When this parameter is absent, this API endpoint always modifies the current
            user's own settings.

            **Changes**: New in Zulip 12.0 (feature level 444).

        full_name : typing.Optional[str]
            A new display name for the user.

        email : typing.Optional[str]
            Asks the server to initiate a confirmation sequence to change the user's email
            address to the indicated value. The user will need to demonstrate control of the
            new email address by clicking a confirmation link sent to that address.

        old_password : typing.Optional[str]
            The user's old Zulip password (or LDAP password, if LDAP authentication is in use).

            Required only when sending the `new_password` parameter.

        new_password : typing.Optional[str]
            The user's new Zulip password (or LDAP password, if LDAP authentication is in use).

            The `old_password` parameter must be included in the request.

        twenty_four_hour_time : typing.Optional[bool]
            Whether time should be [displayed in 24-hour notation](/help/change-the-time-format).

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

        web_mark_read_on_scroll_policy : typing.Optional[int]
            Whether or not to mark messages as read when the user scrolls through their
            feed.

            - 1 - Always
            - 2 - Only in conversation views
            - 3 - Never

            **Changes**: New in Zulip 7.0 (feature level 175). Previously, there was no
            way for the user to configure this behavior on the web, and the Zulip web and
            desktop apps behaved like the "Always" setting when marking messages as read.

        web_channel_default_view : typing.Optional[int]
            Web/desktop app setting controlling the default navigation
            behavior when clicking on a channel link.

            - 1 - Top topic in the channel
            - 2 - Channel feed
            - 3 - List of topics
            - 4 - Top unread topic in channel

            **Changes**: The "Top unread topic in channel" is new in Zulip 11.0
            (feature level 401).

            The "List of topics" option is new in Zulip 11.0 (feature level 383).

            New in Zulip 9.0 (feature level 269). Previously, this
            was not configurable, and every user had the "Channel feed" behavior.

        starred_message_counts : typing.Optional[bool]
            Whether clients should display the [number of starred
            messages](/help/star-a-message#display-the-number-of-starred-messages).

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

        receives_typing_notifications : typing.Optional[bool]
            Whether the user is configured to receive typing notifications from other users.
            The server will only deliver typing notifications events to users who for whom this
            is enabled.

            By default, this is set to true, enabling user to receive typing
            notifications from other users.

            **Changes**: New in Zulip 9.0 (feature level 253). Previously, there were only
            options to disable sending typing notifications.

        web_suggest_update_timezone : typing.Optional[bool]
            Whether the user should be shown an alert, offering to update their
            [profile time zone](/help/change-your-timezone), when the time displayed
            for the profile time zone differs from the current time displayed by the
            time zone configured on their device.

            **Changes**: New in Zulip 10.0 (feature level 329).

        fluid_layout_width : typing.Optional[bool]
            Whether to use the [maximum available screen width](/help/enable-full-width-display)
            for the web app's center panel (message feed, recent conversations) on wide screens.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

        high_contrast_mode : typing.Optional[bool]
            This setting is reserved for use to control variations in Zulip's design
            to help visually impaired users.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

        web_font_size_px : typing.Optional[int]
            User-configured primary `font-size` for the web application, in pixels.

            **Changes**: New in Zulip 9.0 (feature level 245). Previously, font size was
            only adjustable via browser zoom. Note that this setting was not fully
            implemented at this feature level.

        web_line_height_percent : typing.Optional[int]
            User-configured primary `line-height` for the web application, in percent, so a
            value of 120 represents a `line-height` of 1.2.

            **Changes**: New in Zulip 9.0 (feature level 245). Previously, line height was
            not user-configurable. Note that this setting was not fully implemented at this
            feature level.

        color_scheme : typing.Optional[int]
            Controls which [color theme](/help/dark-theme) to use.

            - 1 - Automatic
            - 2 - Dark theme
            - 3 - Light theme

            Automatic detection is implementing using the standard `prefers-color-scheme`
            media query.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

        enable_drafts_synchronization : typing.Optional[bool]
            A boolean parameter to control whether synchronizing drafts is enabled for
            the user. When synchronization is disabled, all drafts stored in the server
            will be automatically deleted from the server.

            This does not do anything (like sending events) to delete local copies of
            drafts stored in clients.

            **Changes**: New in Zulip 5.0 (feature level 87).

        translate_emoticons : typing.Optional[bool]
            Whether to [translate emoticons to emoji](/help/configure-emoticon-translations)
            in messages the user sends.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

        display_emoji_reaction_users : typing.Optional[bool]
            Whether to display the names of reacting users on a message.

            When enabled, clients should display the names of reacting users, rather than
            a count, for messages with few total reactions. The ideal cutoff may depend on
            the space available for displaying reactions; the official web application
            displays names when 3 or fewer total reactions are present with this setting
            enabled.

            **Changes**: New in Zulip 6.0 (feature level 125).

        default_language : typing.Optional[str]
            What [default language](/help/change-your-language) to use for the account.

            This controls both the Zulip UI as well as email notifications sent to the user.

            The value needs to be a standard language code that the Zulip server has
            translation data for; for example, `"en"` for English or `"de"` for German.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

            Unnecessary JSON-encoding of this parameter was removed in Zulip 4.0 (feature level 63).

        web_home_view : typing.Optional[str]
            The [home view](/help/configure-home-view) used when opening a new
            Zulip web app window or hitting the `Esc` keyboard shortcut repeatedly.

            - "recent" - Recent conversations view
            - "inbox" - Inbox view
            - "all_messages" - Combined feed view

            **Changes**: Before Zulip 12.0 (feature level 454), the Recent
            view had `"recent_topics"` as its string encoding.

            New in Zulip 8.0 (feature level 219). Previously, this was called
            `default_view`, which was new in Zulip 4.0 (feature level 42).

            Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

            Unnecessary JSON-encoding of this parameter was removed in Zulip 4.0 (feature level 64).

        web_escape_navigates_to_home_view : typing.Optional[bool]
            Whether the escape key navigates to the
            [configured home view](/help/configure-home-view).

            **Changes**: New in Zulip 8.0 (feature level 219). Previously, this
            was called `escape_navigates_to_default_view`, which was new in Zulip
            5.0 (feature level 107).

        left_side_userlist : typing.Optional[bool]
            Whether the users list on left sidebar in narrow windows.

            This feature is not heavily used and is likely to be reworked.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

        emojiset : typing.Optional[str]
            The user's configured [emoji set](/help/emoji-and-emoticons#use-emoticons),
            used to display emoji to the user everywhere they appear in the UI.

            - "google" - Google modern
            - "twitter" - Twitter
            - "text" - Plain text

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

            Unnecessary JSON-encoding of this parameter was removed in Zulip 4.0 (feature level 64).

        demote_inactive_streams : typing.Optional[int]
            Whether to [hide inactive channels](/help/manage-inactive-channels) in the left sidebar.

            - 1 - Automatic
            - 2 - Always
            - 3 - Never

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

        user_list_style : typing.Optional[int]
            The style selected by the user for the right sidebar user list.

            - 1 - Compact
            - 2 - With status
            - 3 - With avatar and status

            **Changes**: New in Zulip 6.0 (feature level 141).

        web_animate_image_previews : typing.Optional[UpdateSettingsRequestWebAnimateImagePreviews]
            Controls how animated images should be played in the message feed in the web/desktop application.

            - "always" - Always play the animated images in the message feed.
            - "on_hover" - Play the animated images on hover over them in the message feed.
            - "never" - Never play animated images in the message feed.

            **Changes**: New in Zulip 9.0 (feature level 275).

        web_stream_unreads_count_display_policy : typing.Optional[int]
            Configuration for which channels should be displayed with a numeric unread count in the left sidebar.
            Channels that do not have an unread count will have a simple dot indicator for whether there are any
            unread messages.

            - 1 - All channels
            - 2 - Unmuted channels and topics
            - 3 - No channels

            **Changes**: New in Zulip 8.0 (feature level 210).

        hide_ai_features : typing.Optional[bool]
            Controls whether user wants AI features like topic summarization to
            be hidden in all Zulip clients.

            **Changes**: New in Zulip 10.0 (feature level 350).

        web_inbox_show_channel_folders : typing.Optional[bool]
            Determines whether [channel folders](/help/channel-folders)
            are used to organize how conversations with unread messages
            are displayed in the web/desktop application's Inbox view.

            **Changes**: New in Zulip 12.0 (feature level 431).

        web_left_sidebar_show_channel_folders : typing.Optional[bool]
            Determines whether [channel folders](/help/channel-folders)
            are used to organize how channels are displayed in the
            web/desktop application's left sidebar.

            **Changes**: New in Zulip 11.0 (feature level 411).

        web_left_sidebar_unreads_count_summary : typing.Optional[bool]
            Determines whether the web/desktop application's left sidebar displays
            the unread message count summary.

            **Changes**: New in Zulip 11.0 (feature level 398).

        timezone : typing.Optional[str]
            The IANA identifier of the user's [profile time zone](/help/change-your-timezone),
            which is used primarily to display the user's local time to other users.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/display` endpoint.

            Unnecessary JSON-encoding of this parameter was removed in Zulip 4.0 (feature level 64).

        enable_stream_desktop_notifications : typing.Optional[bool]
            Enable visual desktop notifications for channel messages.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_stream_email_notifications : typing.Optional[bool]
            Enable email notifications for channel messages.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_stream_push_notifications : typing.Optional[bool]
            Enable mobile notifications for channel messages.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_stream_audible_notifications : typing.Optional[bool]
            Enable audible desktop notifications for channel messages.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        notification_sound : typing.Optional[str]
            Notification sound name.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

            Unnecessary JSON-encoding of this parameter was removed in Zulip 4.0 (feature level 63).

        enable_desktop_notifications : typing.Optional[bool]
            Enable visual desktop notifications for direct messages and @-mentions.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_sounds : typing.Optional[bool]
            Enable audible desktop notifications for direct messages and
            @-mentions.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        email_notifications_batching_period_seconds : typing.Optional[int]
            The duration (in seconds) for which the server should wait to batch
            email notifications before sending them.

            **Changes**: New in Zulip 5.0 (feature level 82)

        enable_offline_email_notifications : typing.Optional[bool]
            Enable email notifications for direct messages and @-mentions received
            when the user is offline.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_offline_push_notifications : typing.Optional[bool]
            Enable mobile notification for direct messages and @-mentions received
            when the user is offline.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_online_push_notifications : typing.Optional[bool]
            Enable mobile notification for direct messages and @-mentions received
            when the user is online.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_followed_topic_desktop_notifications : typing.Optional[bool]
            Enable visual desktop notifications for messages sent to followed topics.

            **Changes**: New in Zulip 8.0 (feature level 189).

        enable_followed_topic_email_notifications : typing.Optional[bool]
            Enable email notifications for messages sent to followed topics.

            **Changes**: New in Zulip 8.0 (feature level 189).

        enable_followed_topic_push_notifications : typing.Optional[bool]
            Enable push notifications for messages sent to followed topics.

            **Changes**: New in Zulip 8.0 (feature level 189).

        enable_followed_topic_audible_notifications : typing.Optional[bool]
            Enable audible desktop notifications for messages sent to followed topics.

            **Changes**: New in Zulip 8.0 (feature level 189).

        enable_digest_emails : typing.Optional[bool]
            Enable digest emails when the user is away.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_marketing_emails : typing.Optional[bool]
            Enable marketing emails. Has no function outside Zulip Cloud.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_login_emails : typing.Optional[bool]
            Enable email notifications for new logins to account.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        message_content_in_email_notifications : typing.Optional[bool]
            Include the message's content in email notifications for new messages.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        pm_content_in_desktop_notifications : typing.Optional[bool]
            Include content of direct messages in desktop notifications.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        wildcard_mentions_notify : typing.Optional[bool]
            Whether wildcard mentions (E.g. @**all**) should send notifications
            like a personal mention.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enable_followed_topic_wildcard_mentions_notify : typing.Optional[bool]
            Whether wildcard mentions (e.g., @**all**) in messages sent to followed topics
            should send notifications like a personal mention.

            **Changes**: New in Zulip 8.0 (feature level 189).

        desktop_icon_count_display : typing.Optional[int]
            Unread count badge (appears in desktop sidebar and browser tab)

            - 1 - All unread messages
            - 2 - DMs, mentions, and followed topics
            - 3 - DMs and mentions
            - 4 - None

            **Changes**: In Zulip 8.0 (feature level 227), added `DMs, mentions, and followed
            topics` option, renumbering the options to insert it in order.

            Before Zulip 5.0 (feature level 80), this setting was managed by the
            `PATCH /settings/notifications` endpoint.

        realm_name_in_email_notifications_policy : typing.Optional[int]
            Whether to [include organization name in subject of message notification
            emails](/help/email-notifications#include-organization-name-in-subject-line).

            - 1 - Automatic
            - 2 - Always
            - 3 - Never

            **Changes**: New in Zulip 7.0 (feature level 168), replacing the
            previous `realm_name_in_notifications` boolean;
            `true` corresponded to `Always`, and `false` to `Never`.

            Before Zulip 5.0 (feature level 80), the previous `realm_name_in_notifications`
            setting was managed by the `PATCH /settings/notifications` endpoint.

        automatically_follow_topics_policy : typing.Optional[int]
            Which [topics to follow automatically](/help/mute-a-topic).

            - 1 - Topics the user participates in
            - 2 - Topics the user sends a message to
            - 3 - Topics the user starts
            - 4 - Never

            **Changes**: New in Zulip 8.0 (feature level 214).

        automatically_unmute_topics_in_muted_streams_policy : typing.Optional[int]
            Which [topics to unmute automatically in muted channels](/help/mute-a-topic).

            - 1 - Topics the user participates in
            - 2 - Topics the user sends a message to
            - 3 - Topics the user starts
            - 4 - Never

            **Changes**: New in Zulip 8.0 (feature level 214).

        automatically_follow_topics_where_mentioned : typing.Optional[bool]
            Whether the server will automatically mark the user as following
            topics where the user is mentioned.

            **Changes**: New in Zulip 8.0 (feature level 235).

        resolved_topic_notice_auto_read_policy : typing.Optional[UpdateSettingsRequestResolvedTopicNoticeAutoReadPolicy]
            Controls whether the resolved-topic notices are marked as read.

            - "always" - Always mark resolved-topic notices as read.
            - "except_followed" - Mark resolved-topic notices as read in topics not followed by the user.
            - "never" - Never mark resolved-topic notices as read.

            **Changes**: New in Zulip 11.0 (feature level 385).

        presence_enabled : typing.Optional[bool]
            Display the presence status to other users when online.

            **Changes**: Before Zulip 5.0 (feature level 80), this setting was managed by
            the `PATCH /settings/notifications` endpoint.

        enter_sends : typing.Optional[bool]
            Whether pressing Enter in the compose box sends a message
            (or saves a message edit).

            **Changes**: Before Zulip 5.0 (feature level 81), this setting was managed by
            the `POST /users/me/enter-sends` endpoint, with the same parameter format.

        send_private_typing_notifications : typing.Optional[bool]
            Whether [typing notifications](/help/typing-notifications) be sent when composing
            direct messages.

            **Changes**: New in Zulip 5.0 (feature level 105).

        send_stream_typing_notifications : typing.Optional[bool]
            Whether [typing notifications](/help/typing-notifications) be sent when composing
            channel messages.

            **Changes**: New in Zulip 5.0 (feature level 105).

        send_read_receipts : typing.Optional[bool]
            Whether other users are allowed to see whether you've
            read messages.

            **Changes**: New in Zulip 5.0 (feature level 105).

        allow_private_data_export : typing.Optional[bool]
            Whether organization administrators are allowed to
            export your private data.

            **Changes**: New in Zulip 10.0 (feature level 293).

        email_address_visibility : typing.Optional[int]
            The [policy][permission-level] this user has selected for [which other
            users][help-email-visibility] in this organization can see their real
            email address.

            - 1 = Everyone
            - 2 = Members only
            - 3 = Administrators only
            - 4 = Nobody
            - 5 = Moderators only

            **Changes**: New in Zulip 7.0 (feature level 163), replacing the
            realm-level setting.

            [permission-level]: /api/roles-and-permissions#permission-levels
            [help-email-visibility]: /help/configure-email-visibility

        web_navigate_to_sent_message : typing.Optional[bool]
            Web/desktop app setting for whether the user's view should
            automatically go to the conversation where they sent a message.

            **Changes**: New in Zulip 9.0 (feature level 268). Previously,
            this behavior was not configurable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IgnoredParametersSuccess
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
            await client.users.update_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_settings(
            target_users=target_users,
            full_name=full_name,
            email=email,
            old_password=old_password,
            new_password=new_password,
            twenty_four_hour_time=twenty_four_hour_time,
            web_mark_read_on_scroll_policy=web_mark_read_on_scroll_policy,
            web_channel_default_view=web_channel_default_view,
            starred_message_counts=starred_message_counts,
            receives_typing_notifications=receives_typing_notifications,
            web_suggest_update_timezone=web_suggest_update_timezone,
            fluid_layout_width=fluid_layout_width,
            high_contrast_mode=high_contrast_mode,
            web_font_size_px=web_font_size_px,
            web_line_height_percent=web_line_height_percent,
            color_scheme=color_scheme,
            enable_drafts_synchronization=enable_drafts_synchronization,
            translate_emoticons=translate_emoticons,
            display_emoji_reaction_users=display_emoji_reaction_users,
            default_language=default_language,
            web_home_view=web_home_view,
            web_escape_navigates_to_home_view=web_escape_navigates_to_home_view,
            left_side_userlist=left_side_userlist,
            emojiset=emojiset,
            demote_inactive_streams=demote_inactive_streams,
            user_list_style=user_list_style,
            web_animate_image_previews=web_animate_image_previews,
            web_stream_unreads_count_display_policy=web_stream_unreads_count_display_policy,
            hide_ai_features=hide_ai_features,
            web_inbox_show_channel_folders=web_inbox_show_channel_folders,
            web_left_sidebar_show_channel_folders=web_left_sidebar_show_channel_folders,
            web_left_sidebar_unreads_count_summary=web_left_sidebar_unreads_count_summary,
            timezone=timezone,
            enable_stream_desktop_notifications=enable_stream_desktop_notifications,
            enable_stream_email_notifications=enable_stream_email_notifications,
            enable_stream_push_notifications=enable_stream_push_notifications,
            enable_stream_audible_notifications=enable_stream_audible_notifications,
            notification_sound=notification_sound,
            enable_desktop_notifications=enable_desktop_notifications,
            enable_sounds=enable_sounds,
            email_notifications_batching_period_seconds=email_notifications_batching_period_seconds,
            enable_offline_email_notifications=enable_offline_email_notifications,
            enable_offline_push_notifications=enable_offline_push_notifications,
            enable_online_push_notifications=enable_online_push_notifications,
            enable_followed_topic_desktop_notifications=enable_followed_topic_desktop_notifications,
            enable_followed_topic_email_notifications=enable_followed_topic_email_notifications,
            enable_followed_topic_push_notifications=enable_followed_topic_push_notifications,
            enable_followed_topic_audible_notifications=enable_followed_topic_audible_notifications,
            enable_digest_emails=enable_digest_emails,
            enable_marketing_emails=enable_marketing_emails,
            enable_login_emails=enable_login_emails,
            message_content_in_email_notifications=message_content_in_email_notifications,
            pm_content_in_desktop_notifications=pm_content_in_desktop_notifications,
            wildcard_mentions_notify=wildcard_mentions_notify,
            enable_followed_topic_wildcard_mentions_notify=enable_followed_topic_wildcard_mentions_notify,
            desktop_icon_count_display=desktop_icon_count_display,
            realm_name_in_email_notifications_policy=realm_name_in_email_notifications_policy,
            automatically_follow_topics_policy=automatically_follow_topics_policy,
            automatically_unmute_topics_in_muted_streams_policy=automatically_unmute_topics_in_muted_streams_policy,
            automatically_follow_topics_where_mentioned=automatically_follow_topics_where_mentioned,
            resolved_topic_notice_auto_read_policy=resolved_topic_notice_auto_read_policy,
            presence_enabled=presence_enabled,
            enter_sends=enter_sends,
            send_private_typing_notifications=send_private_typing_notifications,
            send_stream_typing_notifications=send_stream_typing_notifications,
            send_read_receipts=send_read_receipts,
            allow_private_data_export=allow_private_data_export,
            email_address_visibility=email_address_visibility,
            web_navigate_to_sent_message=web_navigate_to_sent_message,
            request_options=request_options,
        )
        return _response.data

    async def set_typing_status(
        self,
        *,
        op: SetTypingStatusRequestOp,
        type: typing.Optional[SetTypingStatusRequestType] = OMIT,
        to: typing.Optional[typing.Sequence[int]] = OMIT,
        stream_id: typing.Optional[int] = OMIT,
        topic: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Notify other users whether the current user is
        [typing a message][help-typing].

        Clients implementing Zulip's typing notifications
        protocol should work as follows:

        - Send a request to this endpoint with `"op": "start"` when a user
          starts composing a message.
        - While the user continues to actively type or otherwise interact with
          the compose UI (e.g. interacting with the compose box emoji picker),
          send regular `"op": "start"` requests to this endpoint, using
          `server_typing_started_wait_period_milliseconds` in the
          [`POST /register`][api-register] response as the time interval
          between each request.
        - Send a request to this endpoint with `"op": "stop"` when a user
          has stopped using the compose UI for the time period indicated by
          `server_typing_stopped_wait_period_milliseconds` in the
          [`POST /register`][api-register] response or when a user
          cancels the compose action (if it had previously sent a "start"
          notification for that compose action).
        - Start displaying a visual typing indicator for a given conversation
          when a [`typing op:start`][start-typing] event is received
          from the server.
        - Continue displaying a visual typing indicator for the conversation
          until a [`typing op:stop`][stop-typing] event is received
          from the server or the time period indicated by
          `server_typing_started_expiry_period_milliseconds` in the
          [`POST /register`][api-register] response has passed without
          a new `typing "op": "start"` event for the conversation.

        This protocol is designed to allow the server-side typing notifications
        implementation to be stateless while being resilient as network failures
        will not result in a user being incorrectly displayed as perpetually
        typing.

        See the subsystems documentation on [typing indicators][typing-protocol-docs]
        for additional design details on Zulip's typing notifications protocol.

        **Changes**: Clients shouldn't care about the APIs prior to Zulip 8.0 (feature level 215)
        for channel typing notifications, as no client actually implemented
        the previous API for those.

        Support for displaying channel typing notifications was new
        in Zulip 4.0 (feature level 58). Clients should indicate they support
        processing channel typing notifications via the `stream_typing_notifications`
        value in the `client_capabilities` parameter of the
        [`POST /register`][client-capabilities] endpoint.

        [help-typing]: /help/typing-notifications
        [api-register]: /api/register-queue
        [start-typing]: /api/get-events#typing-start
        [stop-typing]: /api/get-events#typing-stop
        [client-capabilities]: /api/register-queue#parameter-client_capabilities
        [typing-protocol-docs]: https://zulip.readthedocs.io/en/latest/subsystems/typing-indicators.html

        Parameters
        ----------
        op : SetTypingStatusRequestOp
            Whether the user has started (`"start"`) or stopped (`"stop"`) typing.

        type : typing.Optional[SetTypingStatusRequestType]
            Type of the message being composed.

            **Changes**: In Zulip 9.0 (feature level 248), `"channel"` was added as
            an additional value for this parameter to indicate a channel message is
            being composed.

            In Zulip 8.0 (feature level 215), stopped supporting
            `"private"` as a valid value for this parameter.

            In Zulip 7.0 (feature level 174), `"direct"` was added
            as the preferred way to indicate a direct message is being composed,
            becoming the default value for this parameter and deprecating the
            original `"private"`.

            New in Zulip 4.0 (feature level 58). Previously, typing notifications
            were only for direct messages.

        to : typing.Optional[typing.Sequence[int]]
            User IDs of the recipients of the message being typed. Required for the
            `"direct"` type. Ignored in the case of `"stream"` or `"channel"` type.

            Clients should send a JSON-encoded list of user IDs, even if there is only
            one recipient.

            **Changes**: In Zulip 8.0 (feature level 215), stopped using this parameter
            for the `"stream"` type. Previously, in the case of the `"stream"` type, it
            accepted a single-element list containing the ID of the channel. A new parameter,
            `stream_id`, is now used for this. Note that the `"channel"` type did not
            exist at this feature level.

            Support for typing notifications for channel' messages
            is new in Zulip 4.0 (feature level 58). Previously, typing
            notifications were only for direct messages.

            Before Zulip 2.0.0, this parameter accepted only a JSON-encoded
            list of email addresses. Support for the email address-based format was
            removed in Zulip 3.0 (feature level 11).

        stream_id : typing.Optional[int]
            ID of the channel in which the message is being typed. Required for the `"stream"`
            or `"channel"` type. Ignored in the case of `"direct"` type.

            **Changes**: New in Zulip 8.0 (feature level 215). Previously, a single-element
            list containing the ID of the channel was passed in `to` parameter.

        topic : typing.Optional[str]
            Topic to which message is being typed. Required for the `"stream"` or `"channel"`
            type. Ignored in the case of `"direct"` type.

            Note: When `"(no topic)"` or the value of `realm_empty_topic_display_name`
            found in the [POST /register](/api/register-queue) response is used for this
            parameter, it is interpreted as an empty string.

            **Changes**: Before Zulip 10.0 (feature level 372),
            `"(no topic)"` was not interpreted as an empty string.

            Before Zulip 10.0 (feature level 334), empty string
            was not a valid topic name for channel messages.

            New in Zulip 4.0 (feature level 58). Previously, typing notifications
            were only for direct messages.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern.users import SetTypingStatusRequestOp

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.users.set_typing_status(
                op=SetTypingStatusRequestOp.START,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_typing_status(
            op=op, type=type, to=to, stream_id=stream_id, topic=topic, request_options=request_options
        )
        return _response.data

    async def set_typing_status_for_message_edit(
        self,
        message_id: int,
        *,
        op: SetTypingStatusForMessageEditRequestOp,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Notify other users whether the current user is editing a message.

        Typing notifications for editing messages follow the same protocol as
        [set-typing-status](/api/set-typing-status), see that endpoint for
        details.

        **Changes**: Before Zulip 10.0 (feature level 361), the endpoint was
        named `/message_edit_typing` with `message_id` a required parameter in
        the request body. Clients are recommended to start using sending these
        typing notifications starting from this feature level.

        New in Zulip 10.0 (feature level 351). Previously, typing notifications were
        not available when editing messages.

        Parameters
        ----------
        message_id : int
            The target message's ID.

        op : SetTypingStatusForMessageEditRequestOp
            Whether the user has started (`"start"`) or stopped (`"stop"`) editing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern.users import SetTypingStatusForMessageEditRequestOp

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.users.set_typing_status_for_message_edit(
                message_id=1,
                op=SetTypingStatusForMessageEditRequestOp.START,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_typing_status_for_message_edit(
            message_id, op=op, request_options=request_options
        )
        return _response.data

    async def create_user_group(
        self,
        *,
        name: str,
        description: str,
        members: typing.Sequence[int],
        subgroups: typing.Optional[typing.Sequence[int]] = OMIT,
        can_add_members_group: typing.Optional[CreateUserGroupRequestCanAddMembersGroup] = OMIT,
        can_join_group: typing.Optional[CreateUserGroupRequestCanJoinGroup] = OMIT,
        can_leave_group: typing.Optional[CreateUserGroupRequestCanLeaveGroup] = OMIT,
        can_manage_group: typing.Optional[CreateUserGroupRequestCanManageGroup] = OMIT,
        can_mention_group: typing.Optional[CreateUserGroupRequestCanMentionGroup] = OMIT,
        can_remove_members_group: typing.Optional[CreateUserGroupRequestCanRemoveMembersGroup] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateUserGroupResponse:
        """
        Create a new [user group](/help/user-groups).

        **Changes**: Prior to Zulip 12.0 (feature level 496), bot
        users were not permitted to call this endpoint.

        Parameters
        ----------
        name : str
            The name of the user group.

        description : str
            The description of the user group.

        members : typing.Sequence[int]
            An array containing the user IDs of the initial members for the
            new user group.

        subgroups : typing.Optional[typing.Sequence[int]]
            An array containing the IDs of the initial subgroups for the new
            user group.

            User can add subgroups to the new group irrespective of other
            permissions for the new group.

            **Changes**: New in Zulip 10.0 (feature level 311).

        can_add_members_group : typing.Optional[CreateUserGroupRequestCanAddMembersGroup]
            A [group-setting value][setting-values] defining the set of users who
            have permission to add members to this user group.

            **Changes**: New in Zulip 10.0 (feature level 305). Previously, this
            permission was controlled by the `can_manage_group` setting.

            [setting-values]: /api/group-setting-values
            [system-groups]: /api/group-setting-values#system-groups

        can_join_group : typing.Optional[CreateUserGroupRequestCanJoinGroup]
            A [group-setting value][setting-values] defining the set of users who
            have permission to join this user group.

            **Changes**: New in Zulip 10.0 (feature level 301).

            [setting-values]: /api/group-setting-values
            [system-groups]: /api/group-setting-values#system-groups

        can_leave_group : typing.Optional[CreateUserGroupRequestCanLeaveGroup]
            A [group-setting value][setting-values] defining the set of users who
            have permission to leave this user group.

            **Changes**: New in Zulip 10.0 (feature level 308).

            [setting-values]: /api/group-setting-values
            [system-groups]: /api/group-setting-values#system-groups

        can_manage_group : typing.Optional[CreateUserGroupRequestCanManageGroup]
            A [group-setting value][setting-values] defining the set of users who
            have permission to [manage this user group][manage-user-groups].

            This setting cannot be set to `"role:internet"` and `"role:everyone"`
            [system groups][system-groups].

            **Changes**: New in Zulip 10.0 (feature level 283).

            [setting-values]: /api/group-setting-values
            [system-groups]: /api/group-setting-values#system-groups
            [manage-user-groups]: /help/manage-user-groups

        can_mention_group : typing.Optional[CreateUserGroupRequestCanMentionGroup]
            A [group-setting value][setting-values] defining the set of users who
            have permission to [mention this user group][mentions].

            This setting cannot be set to `"role:internet"` and `"role:owners"`
            [system groups][system-groups].

            Before Zulip 9.0 (feature level 258), this parameter could only be the
            integer form of a [group-setting value][setting-values].

            Before Zulip 8.0 (feature level 198), this parameter was named
            `can_mention_group_id`.

            New in Zulip 8.0 (feature level 191). Previously, groups could be
            mentioned only if they were not [system groups][system-groups].

            [setting-values]: /api/group-setting-values
            [system-groups]: /api/group-setting-values#system-groups
            [mentions]: /help/mention-a-user-or-group

        can_remove_members_group : typing.Optional[CreateUserGroupRequestCanRemoveMembersGroup]
            A [group-setting value][setting-values] defining the set of users who
            have permission to remove members from this user group.

            **Changes**: New in Zulip 10.0 (feature level 324). Previously, this
            permission was controlled by the `can_manage_group` setting.

            [setting-values]: /api/group-setting-values
            [system-groups]: /api/group-setting-values#system-groups

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateUserGroupResponse
            A success response containing the unique ID of the user group.
            This field provides a straightforward way to reference the
            newly created user group.

            **Changes**: New in Zulip 10.0 (feature level 317).

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.users.create_user_group(
                name="marketing",
                description="The marketing team.",
                members=[1, 2, 3, 4],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_user_group(
            name=name,
            description=description,
            members=members,
            subgroups=subgroups,
            can_add_members_group=can_add_members_group,
            can_join_group=can_join_group,
            can_leave_group=can_leave_group,
            can_manage_group=can_manage_group,
            can_mention_group=can_mention_group,
            can_remove_members_group=can_remove_members_group,
            request_options=request_options,
        )
        return _response.data

    async def get_user_group_members(
        self,
        user_group_id: int,
        *,
        direct_member_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUserGroupMembersResponse:
        """
        Get the members of a [user group](/help/user-groups).

        **Changes**: Prior to Zulip 12.0 (feature level 496), bot
        users were not permitted to call this endpoint.

        New in Zulip 6.0 (feature level 127).

        Parameters
        ----------
        user_group_id : int
            The ID of the target user group.

        direct_member_only : typing.Optional[bool]
            Whether to consider only the direct members of user group and not members
            of its subgroups. Default is `false`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserGroupMembersResponse
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
            await client.users.get_user_group_members(
                user_group_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_group_members(
            user_group_id, direct_member_only=direct_member_only, request_options=request_options
        )
        return _response.data

    async def update_user_group_members(
        self,
        user_group_id: int,
        *,
        delete: typing.Optional[typing.Sequence[int]] = OMIT,
        add: typing.Optional[typing.Sequence[int]] = OMIT,
        delete_subgroups: typing.Optional[typing.Sequence[int]] = OMIT,
        add_subgroups: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Update the members of a [user group](/help/user-groups). The
        user IDs must correspond to non-deactivated users.

        **Changes**: Prior to Zulip 12.0 (feature level 496), bot
        users were not permitted to call this endpoint.

        Prior to Zulip 11.0 (feature level 391), members
        could not be added or removed from a deactivated group.

        **Changes**: Prior to Zulip 10.0 (feature level 303), group memberships of
        deactivated users were visible to the API and could be edited via this endpoint.

        Parameters
        ----------
        user_group_id : int
            The ID of the target user group.

        delete : typing.Optional[typing.Sequence[int]]
            The list of user IDs to be removed from the user group.

        add : typing.Optional[typing.Sequence[int]]
            The list of user IDs to be added to the user group.

        delete_subgroups : typing.Optional[typing.Sequence[int]]
            The list of user group IDs to be removed from the user group.

            **Changes**: New in Zulip 10.0 (feature level 311).

        add_subgroups : typing.Optional[typing.Sequence[int]]
            The list of user group IDs to be added to the user group.

            **Changes**: New in Zulip 10.0 (feature level 311).

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
            await client.users.update_user_group_members(
                user_group_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user_group_members(
            user_group_id,
            delete=delete,
            add=add,
            delete_subgroups=delete_subgroups,
            add_subgroups=add_subgroups,
            request_options=request_options,
        )
        return _response.data

    async def update_user_group(
        self,
        user_group_id: int,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        can_add_members_group: typing.Optional[UpdateUserGroupRequestCanAddMembersGroup] = OMIT,
        can_join_group: typing.Optional[UpdateUserGroupRequestCanJoinGroup] = OMIT,
        can_leave_group: typing.Optional[UpdateUserGroupRequestCanLeaveGroup] = OMIT,
        can_manage_group: typing.Optional[UpdateUserGroupRequestCanManageGroup] = OMIT,
        can_mention_group: typing.Optional[UpdateUserGroupRequestCanMentionGroup] = OMIT,
        can_remove_members_group: typing.Optional[UpdateUserGroupRequestCanRemoveMembersGroup] = OMIT,
        deactivated: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Update the name, description or any of the permission settings
        of a [user group](/help/user-groups).

        This endpoint is also used to reactivate a user group.

        Note that while permissions settings of deactivated groups can
        be edited by this API endpoint, and those permissions settings
        do affect the ability to modify the deactivated group and its
        membership, the deactivated group itself cannot be mentioned
        or used in the value of any permission without first being reactivated.

        **Changes**: Prior to Zulip 12.0 (feature level 496), bot
        users were not permitted to call this endpoint.

        Starting with Zulip 11.0 (feature level 386), this
        endpoint can be used to reactivate a user group.

        Prior to Zulip 10.0 (feature level 340), only the name field
        of deactivated groups could be modified.

        Parameters
        ----------
        user_group_id : int
            The ID of the target user group.

        name : typing.Optional[str]
            The new name of the group.

            **Changes**: Before Zulip 7.0 (feature level 165), this was
            a required field.

        description : typing.Optional[str]
            The new description of the group.

            **Changes**: Before Zulip 7.0 (feature level 165), this was
            a required field.

        can_add_members_group : typing.Optional[UpdateUserGroupRequestCanAddMembersGroup]
            The set of users who have permission to add members to this user group
            expressed as an [update to a group-setting value][update-group-setting].

            **Changes**: New in Zulip 10.0 (feature level 305). Previously, this
            permission was controlled by the `can_manage_group` setting.

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values
            [system-groups]: /api/group-setting-values#system-groups

        can_join_group : typing.Optional[UpdateUserGroupRequestCanJoinGroup]
            The set of users who have permission to join this user group
            expressed as an [update to a group-setting value][update-group-setting].

            **Changes**: New in Zulip 10.0 (feature level 301).

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values
            [system-groups]: /api/group-setting-values#system-groups

        can_leave_group : typing.Optional[UpdateUserGroupRequestCanLeaveGroup]
            The set of users who have permission to leave this user group
            expressed as an [update to a group-setting value][update-group-setting].

            **Changes**: New in Zulip 10.0 (feature level 308).

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values
            [system-groups]: /api/group-setting-values#system-groups

        can_manage_group : typing.Optional[UpdateUserGroupRequestCanManageGroup]
            The set of users who have permission to [manage this user group][manage-user-groups]
            expressed as an [update to a group-setting value][update-group-setting].

            This setting cannot be set to `"role:internet"` and `"role:everyone"`
            [system groups][system-groups].

            **Changes**: New in Zulip 10.0 (feature level 283).

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values
            [system-groups]: /api/group-setting-values#system-groups
            [manage-user-groups]: /help/manage-user-groups

        can_mention_group : typing.Optional[UpdateUserGroupRequestCanMentionGroup]
            The set of users who have permission to [mention this group][mentions],
            expressed as an [update to a group-setting value][update-group-setting].

            This setting cannot be set to `"role:internet"` and `"role:owners"`
            [system groups][system-groups].

            **Changes**: In Zulip 9.0 (feature level 260), this parameter was
            updated to only accept an object with the `old` and `new` fields
            described below. Prior to this feature level, this parameter could be
            either of the two forms of a [group-setting value][setting-values].

            Before Zulip 9.0 (feature level 258), this parameter could only be the
            integer form of a [group-setting value][setting-values].

            Before Zulip 8.0 (feature level 198), this parameter was named
            `can_mention_group_id`.

            New in Zulip 8.0 (feature level 191). Previously, groups could be
            mentioned only if they were not [system groups][system-groups].

            [mentions]: /help/mention-a-user-or-group
            [update-group-setting]: /api/group-setting-values#updating-group-setting-values
            [system-groups]: /api/group-setting-values#system-groups
            [setting-values]: /api/group-setting-values

        can_remove_members_group : typing.Optional[UpdateUserGroupRequestCanRemoveMembersGroup]
            The set of users who have permission to remove members from this user group
            expressed as an [update to a group-setting value][update-group-setting].

            **Changes**: New in Zulip 10.0 (feature level 324). Previously, this
            permission was controlled by the `can_manage_group` setting.

            [update-group-setting]: /api/group-setting-values#updating-group-setting-values
            [system-groups]: /api/group-setting-values#system-groups

        deactivated : typing.Optional[bool]
            A deactivated user group can be reactivated by passing this
            parameter as `false`.

            Passing `true` does nothing as user group is deactivated
            using [`POST /user_groups/{user_group_id}/deactivate`](deactivate-user-group)
            endpoint.

            **Changes**: New in Zulip 11.0 (feature level 386).

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
            await client.users.update_user_group(
                user_group_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user_group(
            user_group_id,
            name=name,
            description=description,
            can_add_members_group=can_add_members_group,
            can_join_group=can_join_group,
            can_leave_group=can_leave_group,
            can_manage_group=can_manage_group,
            can_mention_group=can_mention_group,
            can_remove_members_group=can_remove_members_group,
            deactivated=deactivated,
            request_options=request_options,
        )
        return _response.data

    async def get_user_groups(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserGroupsResponse:
        """
        Fetches all of the user groups in the organization.

        !!! warn ""

            **Note**: This endpoint is not available to
            [guest users](/help/user-roles).

        **Changes**: Prior to Zulip 12.0 (feature level 496), bot
        users were not permitted to call this endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserGroupsResponse
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
            await client.users.get_user_groups()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_groups(request_options=request_options)
        return _response.data

    async def get_user_group_subgroups(
        self,
        user_group_id: int,
        *,
        direct_subgroup_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUserGroupSubgroupsResponse:
        """
        Get the subgroups of a [user group](/help/user-groups).

        **Changes**: Prior to Zulip 12.0 (feature level 496), bot
        users were not permitted to call this endpoint.

        New in Zulip 6.0 (feature level 127).

        Parameters
        ----------
        user_group_id : int
            The ID of the target user group.

        direct_subgroup_only : typing.Optional[bool]
            Whether to consider only direct subgroups of the user group
            or subgroups of subgroups also.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserGroupSubgroupsResponse
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
            await client.users.get_user_group_subgroups(
                user_group_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_group_subgroups(
            user_group_id, direct_subgroup_only=direct_subgroup_only, request_options=request_options
        )
        return _response.data

    async def update_user_group_subgroups(
        self,
        user_group_id: int,
        *,
        delete: typing.Optional[typing.Sequence[int]] = OMIT,
        add: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JsonSuccess:
        """
        Update the subgroups of a [user group](/help/user-groups).

        **Changes**: Prior to Zulip 12.0 (feature level 496), bot
        users were not permitted to call this endpoint.

        Prior to Zulip 11.0 (feature level 391), subgroups
        could not be added or removed from a deactivated group.

        New in Zulip 6.0 (feature level 127).

        Parameters
        ----------
        user_group_id : int
            The ID of the target user group.

        delete : typing.Optional[typing.Sequence[int]]
            The list of user group IDs to be removed from the user group.

        add : typing.Optional[typing.Sequence[int]]
            The list of user group IDs to be added to the user group.

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
            await client.users.update_user_group_subgroups(
                user_group_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user_group_subgroups(
            user_group_id, delete=delete, add=add, request_options=request_options
        )
        return _response.data

    async def get_is_user_group_member(
        self,
        user_group_id: int,
        user_id: int,
        *,
        direct_member_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetIsUserGroupMemberResponse:
        """
        Check whether a user is member of user group.

        **Changes**: Prior to Zulip 12.0 (feature level 496), bot
        users were not permitted to call this endpoint.

        Prior to Zulip 12.0 (feature level 458), this endpoint
        did not support querying group membership of bot users.

        Prior to Zulip 10.0 (feature level 303),
        this would return true when passed a deactivated user
        who was a member of the user group before being deactivated.

        New in Zulip 6.0 (feature level 127).

        Parameters
        ----------
        user_group_id : int
            The ID of the target user group.

        user_id : int
            The target user's ID.

        direct_member_only : typing.Optional[bool]
            Whether to consider only the direct members of user group and not members
            of its subgroups. Default is `false`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetIsUserGroupMemberResponse
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
            await client.users.get_is_user_group_member(
                user_group_id=1,
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_is_user_group_member(
            user_group_id, user_id, direct_member_only=direct_member_only, request_options=request_options
        )
        return _response.data

    async def deactivate_user_group(
        self, user_group_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Deactivate a user group. Deactivated user groups cannot be
        used for mentions, permissions, or any other purpose, but can
        be reactivated or renamed.

        Deactivating user groups is preferable to deleting them from
        the database, since the deactivation model allows audit logs
        of changes to sensitive group-valued permissions to be
        maintained.

        **Changes**: New in Zulip 10.0 (feature level 290).

        Parameters
        ----------
        user_group_id : int
            The ID of the target user group.

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
            await client.users.deactivate_user_group(
                user_group_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deactivate_user_group(user_group_id, request_options=request_options)
        return _response.data

    async def get_bot_api_key(
        self, bot_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBotApiKeyResponse:
        """
        Fetch the API key for a bot user. Only the bot's owner and
        organization administrators have access to a bot's API key.

        **Changes**: New in Zulip 12.0 (feature level 463).

        Parameters
        ----------
        bot_id : int
            The user ID of the target bot.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBotApiKeyResponse
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
            await client.users.get_bot_api_key(
                bot_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bot_api_key(bot_id, request_options=request_options)
        return _response.data

    async def regenerate_bot_api_key(
        self, bot_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RegenerateBotApiKeyResponse:
        """
        Generate a new API key for a bot user. Only the bot's owner and
        organization administrators have access to a bot's API key.

        Parameters
        ----------
        bot_id : int
            The user ID of the target bot.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegenerateBotApiKeyResponse
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
            await client.users.regenerate_bot_api_key(
                bot_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.regenerate_bot_api_key(bot_id, request_options=request_options)
        return _response.data
