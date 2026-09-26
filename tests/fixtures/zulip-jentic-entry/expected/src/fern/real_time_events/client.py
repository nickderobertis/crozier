

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.all_public_channels import AllPublicChannels
from ..types.event_types import EventTypes
from ..types.json_success import JsonSuccess
from ..types.narrow import Narrow
from .raw_client import AsyncRawRealTimeEventsClient, RawRealTimeEventsClient
from .types.get_events_response import GetEventsResponse
from .types.register_queue_request_include_subscribers import RegisterQueueRequestIncludeSubscribers
from .types.register_queue_response import RegisterQueueResponse


OMIT = typing.cast(typing.Any, ...)


class RealTimeEventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRealTimeEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRealTimeEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRealTimeEventsClient
        """
        return self._raw_client

    def get_events(
        self,
        *,
        queue_id: str,
        last_event_id: typing.Optional[int] = None,
        dont_block: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEventsResponse:
        """
        This endpoint allows you to receive new events from
        [a registered event queue](/api/register-queue).

        Long-lived clients should use the
        `event_queue_longpoll_timeout_seconds` property returned by
        `POST /register` as the client-side HTTP request timeout for
        calls to this endpoint. It is guaranteed to be higher than
        heartbeat frequency and should be respected by clients to
        avoid breaking when heartbeat frequency increases.

        Parameters
        ----------
        queue_id : str
            The ID of an event queue that was previously registered via
            `POST /api/v1/register` (see [Register a queue](/api/register-queue)).

        last_event_id : typing.Optional[int]
            The highest event ID in this queue that you've received and
            wish to acknowledge. See the [code for
            `call_on_each_event`](https://github.com/zulip/python-zulip-api/blob/main/zulip/zulip/__init__.py)
            in the [zulip Python
            module](https://github.com/zulip/python-zulip-api) for an
            example implementation of correctly processing each event
            exactly once.

        dont_block : typing.Optional[bool]
            Set to `true` if the client is requesting a nonblocking reply. If not
            specified, the request will block until either a new event is available
            or a few minutes have passed, in which case the server will send the
            client a heartbeat event.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEventsResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.real_time_events.get_events(
            queue_id="fb67bf8a-c031-47cc-84cf-ed80accacda8",
        )
        """
        _response = self._raw_client.get_events(
            queue_id=queue_id, last_event_id=last_event_id, dont_block=dont_block, request_options=request_options
        )
        return _response.data

    def delete_queue(self, *, queue_id: str, request_options: typing.Optional[RequestOptions] = None) -> JsonSuccess:
        """
        Delete a previously registered queue.

        Parameters
        ----------
        queue_id : str
            The ID of an event queue that was previously registered via
            `POST /api/v1/register` (see [Register a queue](/api/register-queue)).

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
        client.real_time_events.delete_queue(
            queue_id="fb67bf8a-c031-47cc-84cf-ed80accacda8",
        )
        """
        _response = self._raw_client.delete_queue(queue_id=queue_id, request_options=request_options)
        return _response.data

    def register_queue(
        self,
        *,
        apply_markdown: typing.Optional[bool] = OMIT,
        client_gravatar: typing.Optional[bool] = OMIT,
        include_subscribers: typing.Optional[RegisterQueueRequestIncludeSubscribers] = OMIT,
        slim_presence: typing.Optional[bool] = OMIT,
        presence_history_limit_days: typing.Optional[int] = OMIT,
        event_types: typing.Optional[EventTypes] = OMIT,
        all_public_streams: typing.Optional[AllPublicChannels] = OMIT,
        client_capabilities: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        fetch_event_types: typing.Optional[typing.Sequence[str]] = OMIT,
        narrow: typing.Optional[Narrow] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegisterQueueResponse:
        """
        This powerful endpoint can be used to register a Zulip "event queue"
        (subscribed to certain types of "events", or updates to the messages
        and other Zulip data the current user has access to), as well as to
        fetch the current state of that data.

        (`register` also powers the `call_on_each_event` Python API, and is
        intended primarily for complex applications for which the more convenient
        `call_on_each_event` API is insufficient).

        This endpoint returns a `queue_id` and a `last_event_id`; these can be
        used in subsequent calls to the
        ["events" endpoint](/api/get-events) to request events from
        the Zulip server using long-polling.

        The server will queue events for up to 10 minutes of inactivity.
        After 10 minutes, your event queue will be garbage-collected. The
        server will send `heartbeat` events every minute, which makes it easy
        to implement a robust client that does not miss events unless the
        client loses network connectivity with the Zulip server for 10 minutes
        or longer.

        Once the server garbage-collects your event queue, the server will
        [return an error](/api/get-events#bad_event_queue_id-errors)
        with a code of `BAD_EVENT_QUEUE_ID` if you try to fetch events from
        the event queue. Your software will need to handle that error
        condition by re-initializing itself (e.g. this is what triggers your
        browser reloading the Zulip web app when your laptop comes back online
        after being offline for more than 10 minutes).

        When prototyping with this API, we recommend first calling `register`
        with no `event_types` parameter to see all the available data from all
        supported event types. Before using your client in production, you
        should set appropriate `event_types` and `fetch_event_types` filters
        so that your client only requests the data it needs. A few minutes
        doing this often saves 90% of the total bandwidth and other resources
        consumed by a client using this API.

        See the [events system developer documentation][events-system-docs]
        if you need deeper details about how the Zulip event queue system
        works, avoids clients needing to worry about large classes of
        potentially messy races, etc.

        **Changes**: Removed `dense_mode` setting in Zulip 10.0 (feature level 364)
        as we now have `web_font_size_px` and `web_line_height_percent`
        settings for more control.

        Before Zulip 7.0 (feature level 183), the
        `realm_community_topic_editing_limit_seconds` property
        was returned by the response. It was removed because it
        had not been in use since the realm setting
        `move_messages_within_stream_limit_seconds` was introduced
        in feature level 162.

        In Zulip 7.0 (feature level 163), the realm setting
        `email_address_visibility` was removed. It was replaced by a [user
        setting](/api/update-settings#parameter-email_address_visibility) with
        a [realm user default][user-defaults], with the encoding of different
        values preserved. Clients can support all versions by supporting the
        current API and treating every user as having the realm's
        `email_address_visibility` value.

        [user-defaults]: /api/update-realm-user-settings-defaults#parameter-email_address_visibility
        [events-system-docs]: https://zulip.readthedocs.io/en/latest/subsystems/events-system.html

        Parameters
        ----------
        apply_markdown : typing.Optional[bool]
            Set to `true` if you would like the content to be rendered in HTML
            format (otherwise the API will return the raw text that the user
            entered)

        client_gravatar : typing.Optional[bool]
            Whether the client supports computing gravatars URLs. If
            enabled, `avatar_url` will be included in the response only
            if there is a Zulip avatar, and will be `null` for users who
            are using gravatar as their avatar. This option
            significantly reduces the compressed size of user data,
            since gravatar URLs are long, random strings and thus do not
            compress well. The `client_gravatar` field is set to `true` if
            clients can compute their own gravatars.

            The default value is `true` for authenticated requests and
            `false` for [unauthenticated
            requests](/help/public-access-option). Passing `true` in
            an unauthenticated request is an error.

            **Changes**: Before Zulip 6.0 (feature level 149), this
            parameter was silently ignored and processed as though it
            were `false` in unauthenticated requests.

        include_subscribers : typing.Optional[RegisterQueueRequestIncludeSubscribers]
            Whether each returned channel object should include a `subscribers`
            field containing a list of the user IDs of its subscribers.

            Client apps supporting organizations with many thousands of users
            should not pass `true`, because the full subscriber matrix may be
            several megabytes of data. The `partial` value, combined with the
            `subscriber_count` and fetching subscribers for individual channels as
            needed, is recommended to support client app features where channel
            subscriber data is useful.

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

            Passing `true` in an [unauthenticated
            request](/help/public-access-option) is an error.

            **Changes**: The `partial` value is new in Zulip 11.0 (feature level 412).

            Before Zulip 6.0 (feature level 149), this parameter was silently
            ignored and processed as though it were `false` in unauthenticated
            requests.

            New in Zulip 2.1.0.

        slim_presence : typing.Optional[bool]
            If `true`, the `presences` object returned in the response will be keyed
            by user ID and the entry for each user's presence data will be in the
            modern format.

            **Changes**: New in Zulip 3.0 (no feature level; API unstable).

        presence_history_limit_days : typing.Optional[int]
            Limits how far back in time to fetch user presence data. If not specified,
            defaults to 14 days. A value of N means that the oldest presence data
            fetched will be from at most N days ago.

            **Changes**: New in Zulip 10.0 (feature level 288).

        event_types : typing.Optional[EventTypes]

        all_public_streams : typing.Optional[AllPublicChannels]

        client_capabilities : typing.Optional[typing.Dict[str, typing.Any]]
            Dictionary containing details on features the client supports that are
            relevant to the format of responses sent by the server.

            - `notification_settings_null`: Boolean for whether the
              client can handle the current API with `null` values for
              channel-level notification settings (which means the channel
              is not customized and should inherit the user's global
              notification settings for channel messages).
              <br />
              **Changes**: New in Zulip 2.1.0. In earlier Zulip releases,
              channel-level notification settings were simple booleans.

            - `bulk_message_deletion`: Boolean for whether the client's
              handler for the `delete_message` event type has been
              updated to process the new bulk format (with a
              `message_ids`, rather than a singleton `message_id`).
              Otherwise, the server will send `delete_message` events
              in a loop.
              <br />
              **Changes**: New in Zulip 3.0 (feature level 13). This
              capability is for backwards-compatibility; it will be
              required in a future server release.

            - `user_avatar_url_field_optional`: Boolean for whether the
              client required avatar URLs for all users, or supports
              using `GET /avatar/{user_id}` to access user avatars. If the
              client has this capability, the server may skip sending a
              `avatar_url` field in the `realm_user` at its sole discretion
              to optimize network performance. This is an important optimization
              in organizations with 10,000s of users.
              <br />
              **Changes**: New in Zulip 3.0 (feature level 18).

            - `stream_typing_notifications`: Boolean for whether the client
              supports channel typing notifications.
              <br />
              **Changes**: New in Zulip 4.0 (feature level 58). This capability is
              for backwards-compatibility; it will be required in a
              future server release.

            - `user_settings_object`: Has no effect with modern servers. Previously,
              this was a boolean for whether the client supported the modern
              [`user_settings` event type](/api/get-events#user_settings-update) and
              the top-level `user_settings` object in this endpoint's response.
              <br />
              **Changes**: Prior to Zulip 12.0 (feature level 439), if false, the
              server would additionally send the legacy `update_global_notifications`
              and `update_display_settings` event types, if requested.
              <br />
              New in Zulip 5.0 (feature level 89). Because the feature level 89 API
              changes were merged together, clients could safely make a request with
              this client capability, and also request all three event types
              (`user_settings`, `update_display_settings`, and
              `update_global_notifications`), and then use the `zulip_feature_level`
              in this endpoint's response or the presence/absence of a `user_settings`
              key to determine where to look for the data.

            - `linkifier_url_template`: Boolean for whether the client accepts
              [linkifiers][help-linkifiers] that use [RFC 6570][rfc6570] compliant
              URL templates for linkifying matches. If false or unset, then the
              `realm_linkifiers` array in the `/register` response will be empty
              if present, and no `realm_linkifiers` [events][events-linkifiers]
              will be sent to the client.
              <br />
              **Changes**: New in Zulip 7.0 (feature level 176). This capability
              is for backwards-compatibility.

            - `user_list_incomplete`: Boolean for whether the client supports not having an
              incomplete user database. If true, then the `realm_users` array in the `register`
              response will not include data for inaccessible users and clients of guest users will
              not receive `realm_user op:add` events for newly created users that are not accessible
              to the current user.
              <br />
              **Changes**: New in Zulip 8.0 (feature level 232). This
              capability is for backwards-compatibility.

            - `include_deactivated_groups`: Boolean for whether the client can handle
              deactivated user groups by themselves. If false, then the `realm_user_groups`
              array in the `/register` response will only include active groups, clients
              will receive a `remove` event instead of `update` event when a group is
              deactivated and no `update` event will be sent to the client if a deactivated
              user group is renamed.
              <br />
              **Changes**: New in Zulip 10.0 (feature level 294). This
              capability is for backwards-compatibility.

            - `archived_channels`: Boolean for whether the client supports processing
              [archived channels](/help/archive-a-channel) in the `stream` and
              `subscription` event types. If `false`, the server will not include data
              related to archived channels in the `register` response or in events.
              <br />
              **Changes**: New in Zulip 10.0 (feature level 315). This allows clients to
              access archived channels, without breaking backwards-compatibility for
              existing clients.

            - `empty_topic_name`: Boolean for whether the client supports processing
              the empty string as a topic name. Clients not declaring this capability
              will be sent the value of `realm_empty_topic_display_name` found in the
              [POST /register](/api/register-queue) response instead of the empty string
              wherever topic names appear in the register response or events involving
              topic names.
              <br/>
              **Changes**: New in Zulip 10.0 (feature level 334). Previously,
              the empty string was not a valid topic name.

            - `simplified_presence_events`: Boolean for whether the client supports
              receiving the [`presence` event type](/api/get-events#presence) with
              user presence data in the modern format. If true, the server will
              send these events with the `presences` field that has the user presence
              data in the modern format. Otherwise, these event will contain fields
              with legacy format user presence data.
              <br />
              **Changes**: New in Zulip 11.0 (feature level 419).

            [help-linkifiers]: /help/add-a-custom-linkifier
            [rfc6570]: https://www.rfc-editor.org/rfc/rfc6570.html
            [events-linkifiers]: /api/get-events#realm_linkifiers

        fetch_event_types : typing.Optional[typing.Sequence[str]]
            Same as the `event_types` parameter except that the values in
            `fetch_event_types` are used to fetch initial data. If
            `fetch_event_types` is not provided, `event_types` is used and if
            `event_types` is not provided, this parameter defaults to `null`.

            Event types not supported by the server are ignored, in order to simplify
            the implementation of client apps that support multiple server versions.

        narrow : typing.Optional[Narrow]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterQueueResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.real_time_events.register_queue()
        """
        _response = self._raw_client.register_queue(
            apply_markdown=apply_markdown,
            client_gravatar=client_gravatar,
            include_subscribers=include_subscribers,
            slim_presence=slim_presence,
            presence_history_limit_days=presence_history_limit_days,
            event_types=event_types,
            all_public_streams=all_public_streams,
            client_capabilities=client_capabilities,
            fetch_event_types=fetch_event_types,
            narrow=narrow,
            request_options=request_options,
        )
        return _response.data

    def post_real_time(
        self,
        *,
        event_types: typing.Optional[EventTypes] = OMIT,
        narrow: typing.Optional[Narrow] = OMIT,
        all_public_streams: typing.Optional[AllPublicChannels] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        (Ignored)

        Parameters
        ----------
        event_types : typing.Optional[EventTypes]

        narrow : typing.Optional[Narrow]

        all_public_streams : typing.Optional[AllPublicChannels]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.real_time_events.post_real_time()
        """
        _response = self._raw_client.post_real_time(
            event_types=event_types,
            narrow=narrow,
            all_public_streams=all_public_streams,
            request_options=request_options,
        )
        return _response.data

    def rest_error_handling(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Common error to many endpoints

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.real_time_events.rest_error_handling()
        """
        _response = self._raw_client.rest_error_handling(request_options=request_options)
        return _response.data


class AsyncRealTimeEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRealTimeEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRealTimeEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRealTimeEventsClient
        """
        return self._raw_client

    async def get_events(
        self,
        *,
        queue_id: str,
        last_event_id: typing.Optional[int] = None,
        dont_block: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEventsResponse:
        """
        This endpoint allows you to receive new events from
        [a registered event queue](/api/register-queue).

        Long-lived clients should use the
        `event_queue_longpoll_timeout_seconds` property returned by
        `POST /register` as the client-side HTTP request timeout for
        calls to this endpoint. It is guaranteed to be higher than
        heartbeat frequency and should be respected by clients to
        avoid breaking when heartbeat frequency increases.

        Parameters
        ----------
        queue_id : str
            The ID of an event queue that was previously registered via
            `POST /api/v1/register` (see [Register a queue](/api/register-queue)).

        last_event_id : typing.Optional[int]
            The highest event ID in this queue that you've received and
            wish to acknowledge. See the [code for
            `call_on_each_event`](https://github.com/zulip/python-zulip-api/blob/main/zulip/zulip/__init__.py)
            in the [zulip Python
            module](https://github.com/zulip/python-zulip-api) for an
            example implementation of correctly processing each event
            exactly once.

        dont_block : typing.Optional[bool]
            Set to `true` if the client is requesting a nonblocking reply. If not
            specified, the request will block until either a new event is available
            or a few minutes have passed, in which case the server will send the
            client a heartbeat event.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEventsResponse
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
            await client.real_time_events.get_events(
                queue_id="fb67bf8a-c031-47cc-84cf-ed80accacda8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_events(
            queue_id=queue_id, last_event_id=last_event_id, dont_block=dont_block, request_options=request_options
        )
        return _response.data

    async def delete_queue(
        self, *, queue_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Delete a previously registered queue.

        Parameters
        ----------
        queue_id : str
            The ID of an event queue that was previously registered via
            `POST /api/v1/register` (see [Register a queue](/api/register-queue)).

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
            await client.real_time_events.delete_queue(
                queue_id="fb67bf8a-c031-47cc-84cf-ed80accacda8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_queue(queue_id=queue_id, request_options=request_options)
        return _response.data

    async def register_queue(
        self,
        *,
        apply_markdown: typing.Optional[bool] = OMIT,
        client_gravatar: typing.Optional[bool] = OMIT,
        include_subscribers: typing.Optional[RegisterQueueRequestIncludeSubscribers] = OMIT,
        slim_presence: typing.Optional[bool] = OMIT,
        presence_history_limit_days: typing.Optional[int] = OMIT,
        event_types: typing.Optional[EventTypes] = OMIT,
        all_public_streams: typing.Optional[AllPublicChannels] = OMIT,
        client_capabilities: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        fetch_event_types: typing.Optional[typing.Sequence[str]] = OMIT,
        narrow: typing.Optional[Narrow] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegisterQueueResponse:
        """
        This powerful endpoint can be used to register a Zulip "event queue"
        (subscribed to certain types of "events", or updates to the messages
        and other Zulip data the current user has access to), as well as to
        fetch the current state of that data.

        (`register` also powers the `call_on_each_event` Python API, and is
        intended primarily for complex applications for which the more convenient
        `call_on_each_event` API is insufficient).

        This endpoint returns a `queue_id` and a `last_event_id`; these can be
        used in subsequent calls to the
        ["events" endpoint](/api/get-events) to request events from
        the Zulip server using long-polling.

        The server will queue events for up to 10 minutes of inactivity.
        After 10 minutes, your event queue will be garbage-collected. The
        server will send `heartbeat` events every minute, which makes it easy
        to implement a robust client that does not miss events unless the
        client loses network connectivity with the Zulip server for 10 minutes
        or longer.

        Once the server garbage-collects your event queue, the server will
        [return an error](/api/get-events#bad_event_queue_id-errors)
        with a code of `BAD_EVENT_QUEUE_ID` if you try to fetch events from
        the event queue. Your software will need to handle that error
        condition by re-initializing itself (e.g. this is what triggers your
        browser reloading the Zulip web app when your laptop comes back online
        after being offline for more than 10 minutes).

        When prototyping with this API, we recommend first calling `register`
        with no `event_types` parameter to see all the available data from all
        supported event types. Before using your client in production, you
        should set appropriate `event_types` and `fetch_event_types` filters
        so that your client only requests the data it needs. A few minutes
        doing this often saves 90% of the total bandwidth and other resources
        consumed by a client using this API.

        See the [events system developer documentation][events-system-docs]
        if you need deeper details about how the Zulip event queue system
        works, avoids clients needing to worry about large classes of
        potentially messy races, etc.

        **Changes**: Removed `dense_mode` setting in Zulip 10.0 (feature level 364)
        as we now have `web_font_size_px` and `web_line_height_percent`
        settings for more control.

        Before Zulip 7.0 (feature level 183), the
        `realm_community_topic_editing_limit_seconds` property
        was returned by the response. It was removed because it
        had not been in use since the realm setting
        `move_messages_within_stream_limit_seconds` was introduced
        in feature level 162.

        In Zulip 7.0 (feature level 163), the realm setting
        `email_address_visibility` was removed. It was replaced by a [user
        setting](/api/update-settings#parameter-email_address_visibility) with
        a [realm user default][user-defaults], with the encoding of different
        values preserved. Clients can support all versions by supporting the
        current API and treating every user as having the realm's
        `email_address_visibility` value.

        [user-defaults]: /api/update-realm-user-settings-defaults#parameter-email_address_visibility
        [events-system-docs]: https://zulip.readthedocs.io/en/latest/subsystems/events-system.html

        Parameters
        ----------
        apply_markdown : typing.Optional[bool]
            Set to `true` if you would like the content to be rendered in HTML
            format (otherwise the API will return the raw text that the user
            entered)

        client_gravatar : typing.Optional[bool]
            Whether the client supports computing gravatars URLs. If
            enabled, `avatar_url` will be included in the response only
            if there is a Zulip avatar, and will be `null` for users who
            are using gravatar as their avatar. This option
            significantly reduces the compressed size of user data,
            since gravatar URLs are long, random strings and thus do not
            compress well. The `client_gravatar` field is set to `true` if
            clients can compute their own gravatars.

            The default value is `true` for authenticated requests and
            `false` for [unauthenticated
            requests](/help/public-access-option). Passing `true` in
            an unauthenticated request is an error.

            **Changes**: Before Zulip 6.0 (feature level 149), this
            parameter was silently ignored and processed as though it
            were `false` in unauthenticated requests.

        include_subscribers : typing.Optional[RegisterQueueRequestIncludeSubscribers]
            Whether each returned channel object should include a `subscribers`
            field containing a list of the user IDs of its subscribers.

            Client apps supporting organizations with many thousands of users
            should not pass `true`, because the full subscriber matrix may be
            several megabytes of data. The `partial` value, combined with the
            `subscriber_count` and fetching subscribers for individual channels as
            needed, is recommended to support client app features where channel
            subscriber data is useful.

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

            Passing `true` in an [unauthenticated
            request](/help/public-access-option) is an error.

            **Changes**: The `partial` value is new in Zulip 11.0 (feature level 412).

            Before Zulip 6.0 (feature level 149), this parameter was silently
            ignored and processed as though it were `false` in unauthenticated
            requests.

            New in Zulip 2.1.0.

        slim_presence : typing.Optional[bool]
            If `true`, the `presences` object returned in the response will be keyed
            by user ID and the entry for each user's presence data will be in the
            modern format.

            **Changes**: New in Zulip 3.0 (no feature level; API unstable).

        presence_history_limit_days : typing.Optional[int]
            Limits how far back in time to fetch user presence data. If not specified,
            defaults to 14 days. A value of N means that the oldest presence data
            fetched will be from at most N days ago.

            **Changes**: New in Zulip 10.0 (feature level 288).

        event_types : typing.Optional[EventTypes]

        all_public_streams : typing.Optional[AllPublicChannels]

        client_capabilities : typing.Optional[typing.Dict[str, typing.Any]]
            Dictionary containing details on features the client supports that are
            relevant to the format of responses sent by the server.

            - `notification_settings_null`: Boolean for whether the
              client can handle the current API with `null` values for
              channel-level notification settings (which means the channel
              is not customized and should inherit the user's global
              notification settings for channel messages).
              <br />
              **Changes**: New in Zulip 2.1.0. In earlier Zulip releases,
              channel-level notification settings were simple booleans.

            - `bulk_message_deletion`: Boolean for whether the client's
              handler for the `delete_message` event type has been
              updated to process the new bulk format (with a
              `message_ids`, rather than a singleton `message_id`).
              Otherwise, the server will send `delete_message` events
              in a loop.
              <br />
              **Changes**: New in Zulip 3.0 (feature level 13). This
              capability is for backwards-compatibility; it will be
              required in a future server release.

            - `user_avatar_url_field_optional`: Boolean for whether the
              client required avatar URLs for all users, or supports
              using `GET /avatar/{user_id}` to access user avatars. If the
              client has this capability, the server may skip sending a
              `avatar_url` field in the `realm_user` at its sole discretion
              to optimize network performance. This is an important optimization
              in organizations with 10,000s of users.
              <br />
              **Changes**: New in Zulip 3.0 (feature level 18).

            - `stream_typing_notifications`: Boolean for whether the client
              supports channel typing notifications.
              <br />
              **Changes**: New in Zulip 4.0 (feature level 58). This capability is
              for backwards-compatibility; it will be required in a
              future server release.

            - `user_settings_object`: Has no effect with modern servers. Previously,
              this was a boolean for whether the client supported the modern
              [`user_settings` event type](/api/get-events#user_settings-update) and
              the top-level `user_settings` object in this endpoint's response.
              <br />
              **Changes**: Prior to Zulip 12.0 (feature level 439), if false, the
              server would additionally send the legacy `update_global_notifications`
              and `update_display_settings` event types, if requested.
              <br />
              New in Zulip 5.0 (feature level 89). Because the feature level 89 API
              changes were merged together, clients could safely make a request with
              this client capability, and also request all three event types
              (`user_settings`, `update_display_settings`, and
              `update_global_notifications`), and then use the `zulip_feature_level`
              in this endpoint's response or the presence/absence of a `user_settings`
              key to determine where to look for the data.

            - `linkifier_url_template`: Boolean for whether the client accepts
              [linkifiers][help-linkifiers] that use [RFC 6570][rfc6570] compliant
              URL templates for linkifying matches. If false or unset, then the
              `realm_linkifiers` array in the `/register` response will be empty
              if present, and no `realm_linkifiers` [events][events-linkifiers]
              will be sent to the client.
              <br />
              **Changes**: New in Zulip 7.0 (feature level 176). This capability
              is for backwards-compatibility.

            - `user_list_incomplete`: Boolean for whether the client supports not having an
              incomplete user database. If true, then the `realm_users` array in the `register`
              response will not include data for inaccessible users and clients of guest users will
              not receive `realm_user op:add` events for newly created users that are not accessible
              to the current user.
              <br />
              **Changes**: New in Zulip 8.0 (feature level 232). This
              capability is for backwards-compatibility.

            - `include_deactivated_groups`: Boolean for whether the client can handle
              deactivated user groups by themselves. If false, then the `realm_user_groups`
              array in the `/register` response will only include active groups, clients
              will receive a `remove` event instead of `update` event when a group is
              deactivated and no `update` event will be sent to the client if a deactivated
              user group is renamed.
              <br />
              **Changes**: New in Zulip 10.0 (feature level 294). This
              capability is for backwards-compatibility.

            - `archived_channels`: Boolean for whether the client supports processing
              [archived channels](/help/archive-a-channel) in the `stream` and
              `subscription` event types. If `false`, the server will not include data
              related to archived channels in the `register` response or in events.
              <br />
              **Changes**: New in Zulip 10.0 (feature level 315). This allows clients to
              access archived channels, without breaking backwards-compatibility for
              existing clients.

            - `empty_topic_name`: Boolean for whether the client supports processing
              the empty string as a topic name. Clients not declaring this capability
              will be sent the value of `realm_empty_topic_display_name` found in the
              [POST /register](/api/register-queue) response instead of the empty string
              wherever topic names appear in the register response or events involving
              topic names.
              <br/>
              **Changes**: New in Zulip 10.0 (feature level 334). Previously,
              the empty string was not a valid topic name.

            - `simplified_presence_events`: Boolean for whether the client supports
              receiving the [`presence` event type](/api/get-events#presence) with
              user presence data in the modern format. If true, the server will
              send these events with the `presences` field that has the user presence
              data in the modern format. Otherwise, these event will contain fields
              with legacy format user presence data.
              <br />
              **Changes**: New in Zulip 11.0 (feature level 419).

            [help-linkifiers]: /help/add-a-custom-linkifier
            [rfc6570]: https://www.rfc-editor.org/rfc/rfc6570.html
            [events-linkifiers]: /api/get-events#realm_linkifiers

        fetch_event_types : typing.Optional[typing.Sequence[str]]
            Same as the `event_types` parameter except that the values in
            `fetch_event_types` are used to fetch initial data. If
            `fetch_event_types` is not provided, `event_types` is used and if
            `event_types` is not provided, this parameter defaults to `null`.

            Event types not supported by the server are ignored, in order to simplify
            the implementation of client apps that support multiple server versions.

        narrow : typing.Optional[Narrow]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterQueueResponse
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
            await client.real_time_events.register_queue()


        asyncio.run(main())
        """
        _response = await self._raw_client.register_queue(
            apply_markdown=apply_markdown,
            client_gravatar=client_gravatar,
            include_subscribers=include_subscribers,
            slim_presence=slim_presence,
            presence_history_limit_days=presence_history_limit_days,
            event_types=event_types,
            all_public_streams=all_public_streams,
            client_capabilities=client_capabilities,
            fetch_event_types=fetch_event_types,
            narrow=narrow,
            request_options=request_options,
        )
        return _response.data

    async def post_real_time(
        self,
        *,
        event_types: typing.Optional[EventTypes] = OMIT,
        narrow: typing.Optional[Narrow] = OMIT,
        all_public_streams: typing.Optional[AllPublicChannels] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        (Ignored)

        Parameters
        ----------
        event_types : typing.Optional[EventTypes]

        narrow : typing.Optional[Narrow]

        all_public_streams : typing.Optional[AllPublicChannels]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.real_time_events.post_real_time()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_real_time(
            event_types=event_types,
            narrow=narrow,
            all_public_streams=all_public_streams,
            request_options=request_options,
        )
        return _response.data

    async def rest_error_handling(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Common error to many endpoints

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.real_time_events.rest_error_handling()


        asyncio.run(main())
        """
        _response = await self._raw_client.rest_error_handling(request_options=request_options)
        return _response.data
