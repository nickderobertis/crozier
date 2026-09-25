

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.invite_expiration_parameter import InviteExpirationParameter
from ..types.invite_role_parameter import InviteRoleParameter
from ..types.json_success import JsonSuccess
from .raw_client import AsyncRawInvitesClient, RawInvitesClient
from .types.create_invite_link_response import CreateInviteLinkResponse
from .types.get_invites_response import GetInvitesResponse
from .types.send_invites_response import SendInvitesResponse


OMIT = typing.cast(typing.Any, ...)


class InvitesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInvitesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInvitesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInvitesClient
        """
        return self._raw_client

    def get_invites(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetInvitesResponse:
        """
        Fetch all unexpired [invitations](/help/invite-new-users) (i.e. email
        invitations and reusable invitation links) that can be managed by the user.

        Note that administrators can manage invitations that were created by other users.

        **Changes**: Prior to Zulip 8.0 (feature level 209), non-admin users could
        only create email invitations, and therefore the response would never include
        reusable invitation links for these users.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetInvitesResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.invites.get_invites()
        """
        _response = self._raw_client.get_invites(request_options=request_options)
        return _response.data

    def send_invites(
        self,
        *,
        invitee_emails: str,
        stream_ids: typing.Sequence[int],
        invite_expires_in_minutes: typing.Optional[InviteExpirationParameter] = OMIT,
        invite_as: typing.Optional[InviteRoleParameter] = OMIT,
        group_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        include_realm_default_subscriptions: typing.Optional[bool] = OMIT,
        notify_referrer_on_join: typing.Optional[bool] = OMIT,
        welcome_message_custom_text: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendInvitesResponse:
        """
        Send [invitations](/help/invite-new-users) to specified email addresses.

        **Changes**: In Zulip 6.0 (feature level 126), the `invite_expires_in_days`
        parameter was removed and replaced by `invite_expires_in_minutes`.

        In Zulip 5.0 (feature level 117), added support for passing `null` as
        the `invite_expires_in_days` parameter to request an invitation that never
        expires.

        In Zulip 5.0 (feature level 96), the `invite_expires_in_days` parameter was
        added which specified the number of days before the invitation would expire.

        Parameters
        ----------
        invitee_emails : str
            The string containing the email addresses, separated by commas or
            newlines, that will be sent an invitation.

        stream_ids : typing.Sequence[int]
            A list containing the [IDs of the channels](/api/get-stream-id) that the
            newly created user will be automatically subscribed to if the invitation
            is accepted, in addition to any default channels that the new user may
            be subscribed to based on the `include_realm_default_subscriptions`
            parameter.

            Requested channels must either be default channels for the
            organization, or ones the acting user has permission to add
            subscribers to.

            This list must be empty if the current user has the unlikely
            configuration of being able to send invitations while lacking
            permission to [subscribe other users to channels][can-subscribe-others].

            **Changes**: Prior to Zulip 10.0 (feature level 342), default channels
            that the acting user did not directly have permission to add
            subscribers to would be rejected.

            Before Zulip 7.0 (feature level 180), specifying `stream_ids` as an
            empty list resulted in an error.

            [can-subscribe-others]: /help/configure-who-can-invite-to-channels

        invite_expires_in_minutes : typing.Optional[InviteExpirationParameter]

        invite_as : typing.Optional[InviteRoleParameter]

        group_ids : typing.Optional[typing.Sequence[int]]
            A list containing the [IDs of the user groups](/api/get-user-groups) that
            the newly created user will be automatically added to if the invitation
            is accepted. If the list is empty, then the new user will not be
            added to any user groups. The acting user must have permission to add users
            to the groups listed in this request.

            **Changes**: New in Zulip 10.0 (feature level 322).

        include_realm_default_subscriptions : typing.Optional[bool]
            Boolean indicating whether the newly created user should be subscribed
            to the [default channels][default-channels] for the organization.

            Note that this parameter can be `true` even if the user creating the
            invitation does not generally have permission to [subscribe other
            users to channels][can-subscribe-others].

            **Changes**: New in Zulip 9.0 (feature level 261). Previous versions
            of Zulip behaved as though this parameter was always `false`; clients
            needed to include the organization's default channels in the
            `stream_ids` parameter for a newly created user to be automatically
            subscribed to them.

            [default-channels]: /help/set-default-channels-for-new-users
            [can-subscribe-others]: /help/configure-who-can-invite-to-channels

        notify_referrer_on_join : typing.Optional[bool]
            A boolean indicating whether the referrer would like to receive a
            direct message from [notification
            bot](/help/configure-automated-notices) when a user account is created
            using this invitation.

            **Changes**: New in Zulip 9.0 (feature level 267). Previously,
            referrers always received such direct messages.

        welcome_message_custom_text : typing.Optional[str]
            Custom message text, in Zulip Markdown format, to be sent by the
            Welcome Bot to new users that join the organization via this
            invitation.

            Maximum length is 8000 Unicode code points.

            Only organization administrators can use this feature; for other
            users, the value is always `null`.

            - `null`: the organization's default `welcome_message_custom_text` is used.
            - Empty string: no Welcome Bot custom message is sent.
            - Otherwise, the provided string is the custom message.

            **Changes**: New in Zulip 11.0 (feature level 416).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendInvitesResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.invites.send_invites(
            invitee_emails="example@zulip.com, logan@zulip.com",
            stream_ids=[1, 10],
        )
        """
        _response = self._raw_client.send_invites(
            invitee_emails=invitee_emails,
            stream_ids=stream_ids,
            invite_expires_in_minutes=invite_expires_in_minutes,
            invite_as=invite_as,
            group_ids=group_ids,
            include_realm_default_subscriptions=include_realm_default_subscriptions,
            notify_referrer_on_join=notify_referrer_on_join,
            welcome_message_custom_text=welcome_message_custom_text,
            request_options=request_options,
        )
        return _response.data

    def create_invite_link(
        self,
        *,
        invite_expires_in_minutes: typing.Optional[InviteExpirationParameter] = OMIT,
        invite_as: typing.Optional[InviteRoleParameter] = OMIT,
        stream_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        group_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        include_realm_default_subscriptions: typing.Optional[bool] = OMIT,
        welcome_message_custom_text: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateInviteLinkResponse:
        """
        Create a [reusable invitation link](/help/invite-new-users#create-a-reusable-invitation-link)
        which can be used to invite new users to the organization.

        **Changes**: In Zulip 8.0 (feature level 209), added support for non-admin
        users [with permission](/help/restrict-account-creation#change-who-can-send-invitations)
        to use this endpoint. Previously, it was restricted to administrators only.

        In Zulip 6.0 (feature level 126), the `invite_expires_in_days`
        parameter was removed and replaced by `invite_expires_in_minutes`.

        In Zulip 5.0 (feature level 117), added support for passing `null` as
        the `invite_expires_in_days` parameter to request an invitation that never
        expires.

        In Zulip 5.0 (feature level 96), the `invite_expires_in_days` parameter was
        added which specified the number of days before the invitation would expire.

        Parameters
        ----------
        invite_expires_in_minutes : typing.Optional[InviteExpirationParameter]

        invite_as : typing.Optional[InviteRoleParameter]

        stream_ids : typing.Optional[typing.Sequence[int]]
            A list containing the [IDs of the channels](/api/get-stream-id) that the
            newly created user will be automatically subscribed to if the invitation
            is accepted, in addition to any default channels that the new user may
            be subscribed to based on the `include_realm_default_subscriptions`
            parameter.

            Requested channels must either be default channels for the
            organization, or ones the acting user has permission to add
            subscribers to.

            This list must be empty if the current user has the unlikely
            configuration of being able to create reusable invitation links while
            lacking permission to [subscribe other users to
            channels][can-subscribe-others].

            **Changes**: Prior to Zulip 10.0 (feature level 342), default channels
            that the acting user did not directly have permission to add
            subscribers to would be rejected.

            [can-subscribe-others]: /help/configure-who-can-invite-to-channels

        group_ids : typing.Optional[typing.Sequence[int]]
            A list containing the [IDs of the user groups](/api/get-user-groups) that
            the newly created user will be automatically added to if the invitation
            is accepted. If the list is empty, then the new user will not be
            added to any user groups. The acting user must have permission to add users
            to the groups listed in this request.

            **Changes**: New in Zulip 10.0 (feature level 322).

        include_realm_default_subscriptions : typing.Optional[bool]
            Boolean indicating whether the newly created user should be subscribed
            to the [default channels][default-channels] for the organization.

            Note that this parameter can be `true` even if the current user does
            not generally have permission to [subscribe other users to
            channels][can-subscribe-others].

            **Changes**: New in Zulip 9.0 (feature level 261). Previous versions
            of Zulip behaved as though this parameter was always `false`; clients
            needed to include the organization's default channels in the
            `stream_ids` parameter for a newly created user to be automatically
            subscribed to them.

            [default-channels]: /help/set-default-channels-for-new-users
            [can-subscribe-others]: /help/configure-who-can-invite-to-channels

        welcome_message_custom_text : typing.Optional[str]
            Custom message text, in Zulip Markdown format, to be sent by the
            Welcome Bot to new users that join the organization via this
            invitation.

            Maximum length is 8000 Unicode code points.

            Only organization administrators can use this feature; for other
            users, the value is always `null`.

            - `null`: the organization's default `welcome_message_custom_text` is used.
            - Empty string: no Welcome Bot custom message is sent.
            - Otherwise, the provided string is the custom message.

            **Changes**: New in Zulip 11.0 (feature level 416).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateInviteLinkResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.invites.create_invite_link()
        """
        _response = self._raw_client.create_invite_link(
            invite_expires_in_minutes=invite_expires_in_minutes,
            invite_as=invite_as,
            stream_ids=stream_ids,
            group_ids=group_ids,
            include_realm_default_subscriptions=include_realm_default_subscriptions,
            welcome_message_custom_text=welcome_message_custom_text,
            request_options=request_options,
        )
        return _response.data

    def revoke_email_invite(
        self, invite_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Revoke an [email invitation](/help/invite-new-users#send-email-invitations).

        A user can only revoke [invitations that they can
        manage](/help/invite-new-users#manage-pending-invitations).

        Parameters
        ----------
        invite_id : int
            The ID of the email invitation to be revoked.

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
        client.invites.revoke_email_invite(
            invite_id=1,
        )
        """
        _response = self._raw_client.revoke_email_invite(invite_id, request_options=request_options)
        return _response.data

    def revoke_invite_link(
        self, invite_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Revoke a [reusable invitation link](/help/invite-new-users#create-a-reusable-invitation-link).

        A user can only revoke [invitations that they can
        manage](/help/invite-new-users#manage-pending-invitations).

        **Changes**: Prior to Zulip 8.0 (feature level 209), only organization
        administrators were able to create and revoke reusable invitation links.

        Parameters
        ----------
        invite_id : int
            The ID of the reusable invitation link to be revoked.

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
        client.invites.revoke_invite_link(
            invite_id=1,
        )
        """
        _response = self._raw_client.revoke_invite_link(invite_id, request_options=request_options)
        return _response.data

    def resend_email_invite(
        self, invite_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Resend an [email invitation](/help/invite-new-users#send-email-invitations).

        A user can only resend [invitations that they can
        manage](/help/invite-new-users#manage-pending-invitations).

        Parameters
        ----------
        invite_id : int
            The ID of the email invitation to be resent.

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
        client.invites.resend_email_invite(
            invite_id=1,
        )
        """
        _response = self._raw_client.resend_email_invite(invite_id, request_options=request_options)
        return _response.data


class AsyncInvitesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInvitesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInvitesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInvitesClient
        """
        return self._raw_client

    async def get_invites(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetInvitesResponse:
        """
        Fetch all unexpired [invitations](/help/invite-new-users) (i.e. email
        invitations and reusable invitation links) that can be managed by the user.

        Note that administrators can manage invitations that were created by other users.

        **Changes**: Prior to Zulip 8.0 (feature level 209), non-admin users could
        only create email invitations, and therefore the response would never include
        reusable invitation links for these users.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetInvitesResponse
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
            await client.invites.get_invites()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_invites(request_options=request_options)
        return _response.data

    async def send_invites(
        self,
        *,
        invitee_emails: str,
        stream_ids: typing.Sequence[int],
        invite_expires_in_minutes: typing.Optional[InviteExpirationParameter] = OMIT,
        invite_as: typing.Optional[InviteRoleParameter] = OMIT,
        group_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        include_realm_default_subscriptions: typing.Optional[bool] = OMIT,
        notify_referrer_on_join: typing.Optional[bool] = OMIT,
        welcome_message_custom_text: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendInvitesResponse:
        """
        Send [invitations](/help/invite-new-users) to specified email addresses.

        **Changes**: In Zulip 6.0 (feature level 126), the `invite_expires_in_days`
        parameter was removed and replaced by `invite_expires_in_minutes`.

        In Zulip 5.0 (feature level 117), added support for passing `null` as
        the `invite_expires_in_days` parameter to request an invitation that never
        expires.

        In Zulip 5.0 (feature level 96), the `invite_expires_in_days` parameter was
        added which specified the number of days before the invitation would expire.

        Parameters
        ----------
        invitee_emails : str
            The string containing the email addresses, separated by commas or
            newlines, that will be sent an invitation.

        stream_ids : typing.Sequence[int]
            A list containing the [IDs of the channels](/api/get-stream-id) that the
            newly created user will be automatically subscribed to if the invitation
            is accepted, in addition to any default channels that the new user may
            be subscribed to based on the `include_realm_default_subscriptions`
            parameter.

            Requested channels must either be default channels for the
            organization, or ones the acting user has permission to add
            subscribers to.

            This list must be empty if the current user has the unlikely
            configuration of being able to send invitations while lacking
            permission to [subscribe other users to channels][can-subscribe-others].

            **Changes**: Prior to Zulip 10.0 (feature level 342), default channels
            that the acting user did not directly have permission to add
            subscribers to would be rejected.

            Before Zulip 7.0 (feature level 180), specifying `stream_ids` as an
            empty list resulted in an error.

            [can-subscribe-others]: /help/configure-who-can-invite-to-channels

        invite_expires_in_minutes : typing.Optional[InviteExpirationParameter]

        invite_as : typing.Optional[InviteRoleParameter]

        group_ids : typing.Optional[typing.Sequence[int]]
            A list containing the [IDs of the user groups](/api/get-user-groups) that
            the newly created user will be automatically added to if the invitation
            is accepted. If the list is empty, then the new user will not be
            added to any user groups. The acting user must have permission to add users
            to the groups listed in this request.

            **Changes**: New in Zulip 10.0 (feature level 322).

        include_realm_default_subscriptions : typing.Optional[bool]
            Boolean indicating whether the newly created user should be subscribed
            to the [default channels][default-channels] for the organization.

            Note that this parameter can be `true` even if the user creating the
            invitation does not generally have permission to [subscribe other
            users to channels][can-subscribe-others].

            **Changes**: New in Zulip 9.0 (feature level 261). Previous versions
            of Zulip behaved as though this parameter was always `false`; clients
            needed to include the organization's default channels in the
            `stream_ids` parameter for a newly created user to be automatically
            subscribed to them.

            [default-channels]: /help/set-default-channels-for-new-users
            [can-subscribe-others]: /help/configure-who-can-invite-to-channels

        notify_referrer_on_join : typing.Optional[bool]
            A boolean indicating whether the referrer would like to receive a
            direct message from [notification
            bot](/help/configure-automated-notices) when a user account is created
            using this invitation.

            **Changes**: New in Zulip 9.0 (feature level 267). Previously,
            referrers always received such direct messages.

        welcome_message_custom_text : typing.Optional[str]
            Custom message text, in Zulip Markdown format, to be sent by the
            Welcome Bot to new users that join the organization via this
            invitation.

            Maximum length is 8000 Unicode code points.

            Only organization administrators can use this feature; for other
            users, the value is always `null`.

            - `null`: the organization's default `welcome_message_custom_text` is used.
            - Empty string: no Welcome Bot custom message is sent.
            - Otherwise, the provided string is the custom message.

            **Changes**: New in Zulip 11.0 (feature level 416).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendInvitesResponse
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
            await client.invites.send_invites(
                invitee_emails="example@zulip.com, logan@zulip.com",
                stream_ids=[1, 10],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_invites(
            invitee_emails=invitee_emails,
            stream_ids=stream_ids,
            invite_expires_in_minutes=invite_expires_in_minutes,
            invite_as=invite_as,
            group_ids=group_ids,
            include_realm_default_subscriptions=include_realm_default_subscriptions,
            notify_referrer_on_join=notify_referrer_on_join,
            welcome_message_custom_text=welcome_message_custom_text,
            request_options=request_options,
        )
        return _response.data

    async def create_invite_link(
        self,
        *,
        invite_expires_in_minutes: typing.Optional[InviteExpirationParameter] = OMIT,
        invite_as: typing.Optional[InviteRoleParameter] = OMIT,
        stream_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        group_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        include_realm_default_subscriptions: typing.Optional[bool] = OMIT,
        welcome_message_custom_text: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateInviteLinkResponse:
        """
        Create a [reusable invitation link](/help/invite-new-users#create-a-reusable-invitation-link)
        which can be used to invite new users to the organization.

        **Changes**: In Zulip 8.0 (feature level 209), added support for non-admin
        users [with permission](/help/restrict-account-creation#change-who-can-send-invitations)
        to use this endpoint. Previously, it was restricted to administrators only.

        In Zulip 6.0 (feature level 126), the `invite_expires_in_days`
        parameter was removed and replaced by `invite_expires_in_minutes`.

        In Zulip 5.0 (feature level 117), added support for passing `null` as
        the `invite_expires_in_days` parameter to request an invitation that never
        expires.

        In Zulip 5.0 (feature level 96), the `invite_expires_in_days` parameter was
        added which specified the number of days before the invitation would expire.

        Parameters
        ----------
        invite_expires_in_minutes : typing.Optional[InviteExpirationParameter]

        invite_as : typing.Optional[InviteRoleParameter]

        stream_ids : typing.Optional[typing.Sequence[int]]
            A list containing the [IDs of the channels](/api/get-stream-id) that the
            newly created user will be automatically subscribed to if the invitation
            is accepted, in addition to any default channels that the new user may
            be subscribed to based on the `include_realm_default_subscriptions`
            parameter.

            Requested channels must either be default channels for the
            organization, or ones the acting user has permission to add
            subscribers to.

            This list must be empty if the current user has the unlikely
            configuration of being able to create reusable invitation links while
            lacking permission to [subscribe other users to
            channels][can-subscribe-others].

            **Changes**: Prior to Zulip 10.0 (feature level 342), default channels
            that the acting user did not directly have permission to add
            subscribers to would be rejected.

            [can-subscribe-others]: /help/configure-who-can-invite-to-channels

        group_ids : typing.Optional[typing.Sequence[int]]
            A list containing the [IDs of the user groups](/api/get-user-groups) that
            the newly created user will be automatically added to if the invitation
            is accepted. If the list is empty, then the new user will not be
            added to any user groups. The acting user must have permission to add users
            to the groups listed in this request.

            **Changes**: New in Zulip 10.0 (feature level 322).

        include_realm_default_subscriptions : typing.Optional[bool]
            Boolean indicating whether the newly created user should be subscribed
            to the [default channels][default-channels] for the organization.

            Note that this parameter can be `true` even if the current user does
            not generally have permission to [subscribe other users to
            channels][can-subscribe-others].

            **Changes**: New in Zulip 9.0 (feature level 261). Previous versions
            of Zulip behaved as though this parameter was always `false`; clients
            needed to include the organization's default channels in the
            `stream_ids` parameter for a newly created user to be automatically
            subscribed to them.

            [default-channels]: /help/set-default-channels-for-new-users
            [can-subscribe-others]: /help/configure-who-can-invite-to-channels

        welcome_message_custom_text : typing.Optional[str]
            Custom message text, in Zulip Markdown format, to be sent by the
            Welcome Bot to new users that join the organization via this
            invitation.

            Maximum length is 8000 Unicode code points.

            Only organization administrators can use this feature; for other
            users, the value is always `null`.

            - `null`: the organization's default `welcome_message_custom_text` is used.
            - Empty string: no Welcome Bot custom message is sent.
            - Otherwise, the provided string is the custom message.

            **Changes**: New in Zulip 11.0 (feature level 416).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateInviteLinkResponse
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
            await client.invites.create_invite_link()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_invite_link(
            invite_expires_in_minutes=invite_expires_in_minutes,
            invite_as=invite_as,
            stream_ids=stream_ids,
            group_ids=group_ids,
            include_realm_default_subscriptions=include_realm_default_subscriptions,
            welcome_message_custom_text=welcome_message_custom_text,
            request_options=request_options,
        )
        return _response.data

    async def revoke_email_invite(
        self, invite_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Revoke an [email invitation](/help/invite-new-users#send-email-invitations).

        A user can only revoke [invitations that they can
        manage](/help/invite-new-users#manage-pending-invitations).

        Parameters
        ----------
        invite_id : int
            The ID of the email invitation to be revoked.

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
            await client.invites.revoke_email_invite(
                invite_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_email_invite(invite_id, request_options=request_options)
        return _response.data

    async def revoke_invite_link(
        self, invite_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Revoke a [reusable invitation link](/help/invite-new-users#create-a-reusable-invitation-link).

        A user can only revoke [invitations that they can
        manage](/help/invite-new-users#manage-pending-invitations).

        **Changes**: Prior to Zulip 8.0 (feature level 209), only organization
        administrators were able to create and revoke reusable invitation links.

        Parameters
        ----------
        invite_id : int
            The ID of the reusable invitation link to be revoked.

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
            await client.invites.revoke_invite_link(
                invite_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_invite_link(invite_id, request_options=request_options)
        return _response.data

    async def resend_email_invite(
        self, invite_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Resend an [email invitation](/help/invite-new-users#send-email-invitations).

        A user can only resend [invitations that they can
        manage](/help/invite-new-users#manage-pending-invitations).

        Parameters
        ----------
        invite_id : int
            The ID of the email invitation to be resent.

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
            await client.invites.resend_email_invite(
                invite_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resend_email_invite(invite_id, request_options=request_options)
        return _response.data
