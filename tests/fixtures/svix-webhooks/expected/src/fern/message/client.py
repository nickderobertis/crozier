

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.application_in import ApplicationIn
from ..types.bulk_expunge_contents_out import BulkExpungeContentsOut
from ..types.list_response_message_out import ListResponseMessageOut
from ..types.message_out import MessageOut
from .raw_client import AsyncRawMessageClient, RawMessageClient


OMIT = typing.cast(typing.Any, ...)


class MessageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMessageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMessageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMessageClient
        """
        return self._raw_client

    def v1message_list(
        self,
        app_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        before: typing.Optional[dt.datetime] = None,
        after: typing.Optional[dt.datetime] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListResponseMessageOut:
        """
        List all of the application's messages.

        The `before` parameter lets you filter all items created before a certain date and is ignored if an iterator is passed.
        The `after` parameter lets you filter all items created after a certain date and is ignored if an iterator is passed.
        `before` and `after` cannot be used simultaneously.

        Parameters
        ----------
        app_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        channel : typing.Optional[str]
            Filter response based on the channel

        before : typing.Optional[dt.datetime]
            Only include items created before a certain date

        after : typing.Optional[dt.datetime]
            Only include items created after a certain date

        with_content : typing.Optional[bool]
            When `true` message payloads are included in the response

        event_types : typing.Optional[typing.Sequence[str]]
            Filter response based on the event type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponseMessageOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.message.v1message_list(
            app_id="app_id",
            iterator="msg_1srOrx2ZWZBpBUvZwXKQmoEYga2",
            channel="project_1337",
            event_types=["user.signup"],
        )
        """
        _response = self._raw_client.v1message_list(
            app_id,
            limit=limit,
            iterator=iterator,
            channel=channel,
            before=before,
            after=after,
            with_content=with_content,
            event_types=event_types,
            request_options=request_options,
        )
        return _response.data

    def v1message_create(
        self,
        app_id: str,
        *,
        event_type: str,
        payload: typing.Dict[str, typing.Any],
        with_content: typing.Optional[bool] = None,
        idempotency_key: typing.Optional[str] = None,
        application: typing.Optional[ApplicationIn] = OMIT,
        channels: typing.Optional[typing.Sequence[str]] = OMIT,
        event_id: typing.Optional[str] = OMIT,
        payload_retention_period: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageOut:
        """
        Creates a new message and dispatches it to all of the application's endpoints.

        The `eventId` is an optional custom unique ID. It's verified to be unique only up to a day, after that no verification will be made.
        If a message with the same `eventId` already exists for any application in your environment, a 409 conflict error will be returned.

        The `eventType` indicates the type and schema of the event. All messages of a certain `eventType` are expected to have the same schema. Endpoints can choose to only listen to specific event types.
        Messages can also have `channels`, which similar to event types let endpoints filter by them. Unlike event types, messages can have multiple channels, and channels don't imply a specific message content or schema.

        The `payload` property is the webhook's body (the actual webhook message). Svix supports payload sizes of up to ~350kb, though it's generally a good idea to keep webhook payloads small, probably no larger than 40kb.

        Parameters
        ----------
        app_id : str

        event_type : str

        payload : typing.Dict[str, typing.Any]

        with_content : typing.Optional[bool]
            When `true` message payloads are included in the response

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        application : typing.Optional[ApplicationIn]
            Optionally creates a new application alongside the message.

            If the application id or uid that is used in the path already exists, this argument is ignored.

        channels : typing.Optional[typing.Sequence[str]]
            List of free-form identifiers that endpoints can filter by

        event_id : typing.Optional[str]
            Optional unique identifier for the message

        payload_retention_period : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.message.v1message_create(
            app_id="unique-app-identifier",
            event_type="user.signup",
            payload={"email": "test@example.com", "username": "test_user"},
        )
        """
        _response = self._raw_client.v1message_create(
            app_id,
            event_type=event_type,
            payload=payload,
            with_content=with_content,
            idempotency_key=idempotency_key,
            application=application,
            channels=channels,
            event_id=event_id,
            payload_retention_period=payload_retention_period,
            request_options=request_options,
        )
        return _response.data

    def v1message_bulk_expunge_content(
        self,
        app_id: str,
        *,
        idempotency_key: typing.Optional[str] = None,
        ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkExpungeContentsOut:
        """
        Delete the payloads from the given messages under the current application

        Useful in cases when a message was accidentally sent with sensitive content.
        A message can't be replayed or resent once its payload has been deleted
        (or has expired).

        Parameters
        ----------
        app_id : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        ids : typing.Optional[typing.Sequence[str]]
            Message ID or UID to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkExpungeContentsOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.message.v1message_bulk_expunge_content(
            app_id="unique-app-identifier",
        )
        """
        _response = self._raw_client.v1message_bulk_expunge_content(
            app_id, idempotency_key=idempotency_key, ids=ids, request_options=request_options
        )
        return _response.data

    def v1message_get(
        self,
        app_id: str,
        msg_id: str,
        *,
        with_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageOut:
        """
        Get a message by its ID or eventID.

        Parameters
        ----------
        app_id : str

        msg_id : str

        with_content : typing.Optional[bool]
            When `true` message payloads are included in the response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.message.v1message_get(
            app_id="unique-app-identifier",
            msg_id="unique-msg-identifier",
        )
        """
        _response = self._raw_client.v1message_get(
            app_id, msg_id, with_content=with_content, request_options=request_options
        )
        return _response.data

    def v1message_expunge_content(
        self, app_id: str, msg_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the given message's payload. Useful in cases when a message was accidentally sent with sensitive content.

        The message can't be replayed or resent once its payload has been deleted (or has expired).

        Parameters
        ----------
        app_id : str

        msg_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.message.v1message_expunge_content(
            app_id="unique-app-identifier",
            msg_id="unique-msg-identifier",
        )
        """
        _response = self._raw_client.v1message_expunge_content(app_id, msg_id, request_options=request_options)
        return _response.data


class AsyncMessageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMessageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMessageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMessageClient
        """
        return self._raw_client

    async def v1message_list(
        self,
        app_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        before: typing.Optional[dt.datetime] = None,
        after: typing.Optional[dt.datetime] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListResponseMessageOut:
        """
        List all of the application's messages.

        The `before` parameter lets you filter all items created before a certain date and is ignored if an iterator is passed.
        The `after` parameter lets you filter all items created after a certain date and is ignored if an iterator is passed.
        `before` and `after` cannot be used simultaneously.

        Parameters
        ----------
        app_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        channel : typing.Optional[str]
            Filter response based on the channel

        before : typing.Optional[dt.datetime]
            Only include items created before a certain date

        after : typing.Optional[dt.datetime]
            Only include items created after a certain date

        with_content : typing.Optional[bool]
            When `true` message payloads are included in the response

        event_types : typing.Optional[typing.Sequence[str]]
            Filter response based on the event type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponseMessageOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.message.v1message_list(
                app_id="app_id",
                iterator="msg_1srOrx2ZWZBpBUvZwXKQmoEYga2",
                channel="project_1337",
                event_types=["user.signup"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1message_list(
            app_id,
            limit=limit,
            iterator=iterator,
            channel=channel,
            before=before,
            after=after,
            with_content=with_content,
            event_types=event_types,
            request_options=request_options,
        )
        return _response.data

    async def v1message_create(
        self,
        app_id: str,
        *,
        event_type: str,
        payload: typing.Dict[str, typing.Any],
        with_content: typing.Optional[bool] = None,
        idempotency_key: typing.Optional[str] = None,
        application: typing.Optional[ApplicationIn] = OMIT,
        channels: typing.Optional[typing.Sequence[str]] = OMIT,
        event_id: typing.Optional[str] = OMIT,
        payload_retention_period: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageOut:
        """
        Creates a new message and dispatches it to all of the application's endpoints.

        The `eventId` is an optional custom unique ID. It's verified to be unique only up to a day, after that no verification will be made.
        If a message with the same `eventId` already exists for any application in your environment, a 409 conflict error will be returned.

        The `eventType` indicates the type and schema of the event. All messages of a certain `eventType` are expected to have the same schema. Endpoints can choose to only listen to specific event types.
        Messages can also have `channels`, which similar to event types let endpoints filter by them. Unlike event types, messages can have multiple channels, and channels don't imply a specific message content or schema.

        The `payload` property is the webhook's body (the actual webhook message). Svix supports payload sizes of up to ~350kb, though it's generally a good idea to keep webhook payloads small, probably no larger than 40kb.

        Parameters
        ----------
        app_id : str

        event_type : str

        payload : typing.Dict[str, typing.Any]

        with_content : typing.Optional[bool]
            When `true` message payloads are included in the response

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        application : typing.Optional[ApplicationIn]
            Optionally creates a new application alongside the message.

            If the application id or uid that is used in the path already exists, this argument is ignored.

        channels : typing.Optional[typing.Sequence[str]]
            List of free-form identifiers that endpoints can filter by

        event_id : typing.Optional[str]
            Optional unique identifier for the message

        payload_retention_period : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.message.v1message_create(
                app_id="unique-app-identifier",
                event_type="user.signup",
                payload={"email": "test@example.com", "username": "test_user"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1message_create(
            app_id,
            event_type=event_type,
            payload=payload,
            with_content=with_content,
            idempotency_key=idempotency_key,
            application=application,
            channels=channels,
            event_id=event_id,
            payload_retention_period=payload_retention_period,
            request_options=request_options,
        )
        return _response.data

    async def v1message_bulk_expunge_content(
        self,
        app_id: str,
        *,
        idempotency_key: typing.Optional[str] = None,
        ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkExpungeContentsOut:
        """
        Delete the payloads from the given messages under the current application

        Useful in cases when a message was accidentally sent with sensitive content.
        A message can't be replayed or resent once its payload has been deleted
        (or has expired).

        Parameters
        ----------
        app_id : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        ids : typing.Optional[typing.Sequence[str]]
            Message ID or UID to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkExpungeContentsOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.message.v1message_bulk_expunge_content(
                app_id="unique-app-identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1message_bulk_expunge_content(
            app_id, idempotency_key=idempotency_key, ids=ids, request_options=request_options
        )
        return _response.data

    async def v1message_get(
        self,
        app_id: str,
        msg_id: str,
        *,
        with_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageOut:
        """
        Get a message by its ID or eventID.

        Parameters
        ----------
        app_id : str

        msg_id : str

        with_content : typing.Optional[bool]
            When `true` message payloads are included in the response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.message.v1message_get(
                app_id="unique-app-identifier",
                msg_id="unique-msg-identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1message_get(
            app_id, msg_id, with_content=with_content, request_options=request_options
        )
        return _response.data

    async def v1message_expunge_content(
        self, app_id: str, msg_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the given message's payload. Useful in cases when a message was accidentally sent with sensitive content.

        The message can't be replayed or resent once its payload has been deleted (or has expired).

        Parameters
        ----------
        app_id : str

        msg_id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.message.v1message_expunge_content(
                app_id="unique-app-identifier",
                msg_id="unique-msg-identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1message_expunge_content(app_id, msg_id, request_options=request_options)
        return _response.data
