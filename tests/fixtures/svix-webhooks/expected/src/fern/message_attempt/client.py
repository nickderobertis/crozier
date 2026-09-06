

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.empty_response import EmptyResponse
from ..types.list_response_endpoint_message_out import ListResponseEndpointMessageOut
from ..types.list_response_message_attempt_out import ListResponseMessageAttemptOut
from ..types.list_response_message_endpoint_out import ListResponseMessageEndpointOut
from ..types.message_attempt_out import MessageAttemptOut
from ..types.message_status import MessageStatus
from ..types.status_code_class import StatusCodeClass
from .raw_client import AsyncRawMessageAttemptClient, RawMessageAttemptClient


class MessageAttemptClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMessageAttemptClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMessageAttemptClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMessageAttemptClient
        """
        return self._raw_client

    def v1message_attempt_list_by_endpoint(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        status: typing.Optional[MessageStatus] = None,
        status_code_class: typing.Optional[StatusCodeClass] = None,
        channel: typing.Optional[str] = None,
        before: typing.Optional[dt.datetime] = None,
        after: typing.Optional[dt.datetime] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListResponseMessageAttemptOut:
        """
        List attempts by endpoint id

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        status : typing.Optional[MessageStatus]
            Filter response based on the delivery status

        status_code_class : typing.Optional[StatusCodeClass]
            Filter response based on the HTTP status code

        channel : typing.Optional[str]
            Filter response based on the channel

        before : typing.Optional[dt.datetime]
            Only include items created before a certain date

        after : typing.Optional[dt.datetime]
            Only include items created after a certain date

        with_content : typing.Optional[bool]
            When `true` attempt content is included in the response

        event_types : typing.Optional[typing.Sequence[str]]
            Filter response based on the event type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponseMessageAttemptOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.message_attempt.v1message_attempt_list_by_endpoint(
            app_id="unique-app-identifier",
            endpoint_id="unique-ep-identifier",
            iterator="atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2",
            channel="project_1337",
            event_types=["user.signup"],
        )
        """
        _response = self._raw_client.v1message_attempt_list_by_endpoint(
            app_id,
            endpoint_id,
            limit=limit,
            iterator=iterator,
            status=status,
            status_code_class=status_code_class,
            channel=channel,
            before=before,
            after=after,
            with_content=with_content,
            event_types=event_types,
            request_options=request_options,
        )
        return _response.data

    def v1message_attempt_list_by_msg(
        self,
        app_id: str,
        msg_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        status: typing.Optional[MessageStatus] = None,
        status_code_class: typing.Optional[StatusCodeClass] = None,
        channel: typing.Optional[str] = None,
        endpoint_id: typing.Optional[str] = None,
        before: typing.Optional[dt.datetime] = None,
        after: typing.Optional[dt.datetime] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListResponseMessageAttemptOut:
        """
        List attempts by message id

        Parameters
        ----------
        app_id : str

        msg_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        status : typing.Optional[MessageStatus]
            Filter response based on the delivery status

        status_code_class : typing.Optional[StatusCodeClass]
            Filter response based on the HTTP status code

        channel : typing.Optional[str]
            Filter response based on the channel

        endpoint_id : typing.Optional[str]
            Filter the attempts based on the attempted endpoint

        before : typing.Optional[dt.datetime]
            Only include items created before a certain date

        after : typing.Optional[dt.datetime]
            Only include items created after a certain date

        with_content : typing.Optional[bool]
            When `true` attempt content is included in the response

        event_types : typing.Optional[typing.Sequence[str]]
            Filter response based on the event type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponseMessageAttemptOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.message_attempt.v1message_attempt_list_by_msg(
            app_id="unique-app-identifier",
            msg_id="unique-msg-identifier",
            iterator="atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2",
            channel="project_1337",
            endpoint_id="unique-ep-identifier",
            event_types=["user.signup"],
        )
        """
        _response = self._raw_client.v1message_attempt_list_by_msg(
            app_id,
            msg_id,
            limit=limit,
            iterator=iterator,
            status=status,
            status_code_class=status_code_class,
            channel=channel,
            endpoint_id=endpoint_id,
            before=before,
            after=after,
            with_content=with_content,
            event_types=event_types,
            request_options=request_options,
        )
        return _response.data

    def v1message_attempt_list_attempted_messages(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        status: typing.Optional[MessageStatus] = None,
        before: typing.Optional[dt.datetime] = None,
        after: typing.Optional[dt.datetime] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListResponseEndpointMessageOut:
        """
        List messages for a particular endpoint. Additionally includes metadata about the latest message attempt.

        The `before` parameter lets you filter all items created before a certain date and is ignored if an iterator is passed.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        channel : typing.Optional[str]
            Filter response based on the channel

        status : typing.Optional[MessageStatus]
            Filter response based on the delivery status

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
        ListResponseEndpointMessageOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.message_attempt.v1message_attempt_list_attempted_messages(
            app_id="unique-app-identifier",
            endpoint_id="unique-ep-identifier",
            iterator="msg_1srOrx2ZWZBpBUvZwXKQmoEYga2",
            channel="project_1337",
            event_types=["user.signup"],
        )
        """
        _response = self._raw_client.v1message_attempt_list_attempted_messages(
            app_id,
            endpoint_id,
            limit=limit,
            iterator=iterator,
            channel=channel,
            status=status,
            before=before,
            after=after,
            with_content=with_content,
            event_types=event_types,
            request_options=request_options,
        )
        return _response.data

    def v1message_attempt_get(
        self, app_id: str, msg_id: str, attempt_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessageAttemptOut:
        """
        `msg_id`: Use a message id or a message `eventId`

        Parameters
        ----------
        app_id : str

        msg_id : str

        attempt_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageAttemptOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.message_attempt.v1message_attempt_get(
            app_id="unique-app-identifier",
            msg_id="unique-msg-identifier",
            attempt_id="atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2",
        )
        """
        _response = self._raw_client.v1message_attempt_get(app_id, msg_id, attempt_id, request_options=request_options)
        return _response.data

    def v1message_attempt_expunge_content(
        self, app_id: str, msg_id: str, attempt_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes the given attempt's response body. Useful when an endpoint accidentally returned sensitive content.

        Parameters
        ----------
        app_id : str

        msg_id : str

        attempt_id : str

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
        client.message_attempt.v1message_attempt_expunge_content(
            app_id="unique-app-identifier",
            msg_id="unique-msg-identifier",
            attempt_id="atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2",
        )
        """
        _response = self._raw_client.v1message_attempt_expunge_content(
            app_id, msg_id, attempt_id, request_options=request_options
        )
        return _response.data

    def v1message_attempt_list_attempted_destinations(
        self,
        app_id: str,
        msg_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListResponseMessageEndpointOut:
        """
        `msg_id`: Use a message id or a message `eventId`

        Parameters
        ----------
        app_id : str

        msg_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponseMessageEndpointOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.message_attempt.v1message_attempt_list_attempted_destinations(
            app_id="unique-app-identifier",
            msg_id="unique-msg-identifier",
            iterator="ep_1srOrx2ZWZBpBUvZwXKQmoEYga2",
        )
        """
        _response = self._raw_client.v1message_attempt_list_attempted_destinations(
            app_id, msg_id, limit=limit, iterator=iterator, request_options=request_options
        )
        return _response.data

    def v1message_attempt_resend(
        self,
        app_id: str,
        msg_id: str,
        endpoint_id: str,
        *,
        idempotency_key: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmptyResponse:
        """
        Resend a message to the specified endpoint.

        Parameters
        ----------
        app_id : str

        msg_id : str

        endpoint_id : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.message_attempt.v1message_attempt_resend(
            app_id="unique-app-identifier",
            msg_id="unique-msg-identifier",
            endpoint_id="unique-ep-identifier",
        )
        """
        _response = self._raw_client.v1message_attempt_resend(
            app_id, msg_id, endpoint_id, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data


class AsyncMessageAttemptClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMessageAttemptClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMessageAttemptClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMessageAttemptClient
        """
        return self._raw_client

    async def v1message_attempt_list_by_endpoint(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        status: typing.Optional[MessageStatus] = None,
        status_code_class: typing.Optional[StatusCodeClass] = None,
        channel: typing.Optional[str] = None,
        before: typing.Optional[dt.datetime] = None,
        after: typing.Optional[dt.datetime] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListResponseMessageAttemptOut:
        """
        List attempts by endpoint id

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        status : typing.Optional[MessageStatus]
            Filter response based on the delivery status

        status_code_class : typing.Optional[StatusCodeClass]
            Filter response based on the HTTP status code

        channel : typing.Optional[str]
            Filter response based on the channel

        before : typing.Optional[dt.datetime]
            Only include items created before a certain date

        after : typing.Optional[dt.datetime]
            Only include items created after a certain date

        with_content : typing.Optional[bool]
            When `true` attempt content is included in the response

        event_types : typing.Optional[typing.Sequence[str]]
            Filter response based on the event type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponseMessageAttemptOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.message_attempt.v1message_attempt_list_by_endpoint(
                app_id="unique-app-identifier",
                endpoint_id="unique-ep-identifier",
                iterator="atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2",
                channel="project_1337",
                event_types=["user.signup"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1message_attempt_list_by_endpoint(
            app_id,
            endpoint_id,
            limit=limit,
            iterator=iterator,
            status=status,
            status_code_class=status_code_class,
            channel=channel,
            before=before,
            after=after,
            with_content=with_content,
            event_types=event_types,
            request_options=request_options,
        )
        return _response.data

    async def v1message_attempt_list_by_msg(
        self,
        app_id: str,
        msg_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        status: typing.Optional[MessageStatus] = None,
        status_code_class: typing.Optional[StatusCodeClass] = None,
        channel: typing.Optional[str] = None,
        endpoint_id: typing.Optional[str] = None,
        before: typing.Optional[dt.datetime] = None,
        after: typing.Optional[dt.datetime] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListResponseMessageAttemptOut:
        """
        List attempts by message id

        Parameters
        ----------
        app_id : str

        msg_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        status : typing.Optional[MessageStatus]
            Filter response based on the delivery status

        status_code_class : typing.Optional[StatusCodeClass]
            Filter response based on the HTTP status code

        channel : typing.Optional[str]
            Filter response based on the channel

        endpoint_id : typing.Optional[str]
            Filter the attempts based on the attempted endpoint

        before : typing.Optional[dt.datetime]
            Only include items created before a certain date

        after : typing.Optional[dt.datetime]
            Only include items created after a certain date

        with_content : typing.Optional[bool]
            When `true` attempt content is included in the response

        event_types : typing.Optional[typing.Sequence[str]]
            Filter response based on the event type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponseMessageAttemptOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.message_attempt.v1message_attempt_list_by_msg(
                app_id="unique-app-identifier",
                msg_id="unique-msg-identifier",
                iterator="atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2",
                channel="project_1337",
                endpoint_id="unique-ep-identifier",
                event_types=["user.signup"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1message_attempt_list_by_msg(
            app_id,
            msg_id,
            limit=limit,
            iterator=iterator,
            status=status,
            status_code_class=status_code_class,
            channel=channel,
            endpoint_id=endpoint_id,
            before=before,
            after=after,
            with_content=with_content,
            event_types=event_types,
            request_options=request_options,
        )
        return _response.data

    async def v1message_attempt_list_attempted_messages(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        status: typing.Optional[MessageStatus] = None,
        before: typing.Optional[dt.datetime] = None,
        after: typing.Optional[dt.datetime] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListResponseEndpointMessageOut:
        """
        List messages for a particular endpoint. Additionally includes metadata about the latest message attempt.

        The `before` parameter lets you filter all items created before a certain date and is ignored if an iterator is passed.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        channel : typing.Optional[str]
            Filter response based on the channel

        status : typing.Optional[MessageStatus]
            Filter response based on the delivery status

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
        ListResponseEndpointMessageOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.message_attempt.v1message_attempt_list_attempted_messages(
                app_id="unique-app-identifier",
                endpoint_id="unique-ep-identifier",
                iterator="msg_1srOrx2ZWZBpBUvZwXKQmoEYga2",
                channel="project_1337",
                event_types=["user.signup"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1message_attempt_list_attempted_messages(
            app_id,
            endpoint_id,
            limit=limit,
            iterator=iterator,
            channel=channel,
            status=status,
            before=before,
            after=after,
            with_content=with_content,
            event_types=event_types,
            request_options=request_options,
        )
        return _response.data

    async def v1message_attempt_get(
        self, app_id: str, msg_id: str, attempt_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessageAttemptOut:
        """
        `msg_id`: Use a message id or a message `eventId`

        Parameters
        ----------
        app_id : str

        msg_id : str

        attempt_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageAttemptOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.message_attempt.v1message_attempt_get(
                app_id="unique-app-identifier",
                msg_id="unique-msg-identifier",
                attempt_id="atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1message_attempt_get(
            app_id, msg_id, attempt_id, request_options=request_options
        )
        return _response.data

    async def v1message_attempt_expunge_content(
        self, app_id: str, msg_id: str, attempt_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes the given attempt's response body. Useful when an endpoint accidentally returned sensitive content.

        Parameters
        ----------
        app_id : str

        msg_id : str

        attempt_id : str

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
            await client.message_attempt.v1message_attempt_expunge_content(
                app_id="unique-app-identifier",
                msg_id="unique-msg-identifier",
                attempt_id="atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1message_attempt_expunge_content(
            app_id, msg_id, attempt_id, request_options=request_options
        )
        return _response.data

    async def v1message_attempt_list_attempted_destinations(
        self,
        app_id: str,
        msg_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListResponseMessageEndpointOut:
        """
        `msg_id`: Use a message id or a message `eventId`

        Parameters
        ----------
        app_id : str

        msg_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponseMessageEndpointOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.message_attempt.v1message_attempt_list_attempted_destinations(
                app_id="unique-app-identifier",
                msg_id="unique-msg-identifier",
                iterator="ep_1srOrx2ZWZBpBUvZwXKQmoEYga2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1message_attempt_list_attempted_destinations(
            app_id, msg_id, limit=limit, iterator=iterator, request_options=request_options
        )
        return _response.data

    async def v1message_attempt_resend(
        self,
        app_id: str,
        msg_id: str,
        endpoint_id: str,
        *,
        idempotency_key: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmptyResponse:
        """
        Resend a message to the specified endpoint.

        Parameters
        ----------
        app_id : str

        msg_id : str

        endpoint_id : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.message_attempt.v1message_attempt_resend(
                app_id="unique-app-identifier",
                msg_id="unique-msg-identifier",
                endpoint_id="unique-ep-identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1message_attempt_resend(
            app_id, msg_id, endpoint_id, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data
