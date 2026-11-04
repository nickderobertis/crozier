

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawNatsCoreMessagingExperimentalClient, RawNatsCoreMessagingExperimentalClient
from .types.request_response import RequestResponse
from .types.subscribe_response import SubscribeResponse


OMIT = typing.cast(typing.Any, ...)


class NatsCoreMessagingExperimentalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNatsCoreMessagingExperimentalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNatsCoreMessagingExperimentalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNatsCoreMessagingExperimentalClient
        """
        return self._raw_client

    def subscribe(
        self,
        subject: str,
        *,
        timeout: typing.Optional[int] = None,
        limit: typing.Optional[float] = None,
        nats_h: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[SubscribeResponse]:
        """
        Parameters
        ----------
        subject : str
            subject

        timeout : typing.Optional[int]
            how long to wait for a response in milliseconds. Default is 2000 milliseconds.

        limit : typing.Optional[float]
            the maximum number of keys to return, note internally it is limited to 1000

        nats_h : typing.Optional[str]
            Header prefix - any HTTP request with a header that has the `NatsH-` prefix will have the prefix dropped, and have the header included on the published message.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[SubscribeResponse]
            Success response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        response = client.nats_core_messaging_experimental.subscribe(
            subject="subject",
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.subscribe(
            subject, timeout=timeout, limit=limit, nats_h=nats_h, request_options=request_options
        ) as r:
            yield from r.data

    def request(
        self,
        subject: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RequestResponse:
        """
        Parameters
        ----------
        subject : str
            subject

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        timeout : typing.Optional[int]
            how long to wait for a response in milliseconds. Default is 2000 milliseconds.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestResponse
            Success response
        """
        _response = self._raw_client.request(subject, request=request, timeout=timeout, request_options=request_options)
        return _response.data

    def publish(
        self,
        subject: str,
        *,
        reply: str,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        timeout: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subject : str
            subject

        reply : str
            subject

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        timeout : typing.Optional[int]
            how long to wait for a response in milliseconds. Default is 2000 milliseconds.

        query : typing.Optional[str]
            queue group for the subscription

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = self._raw_client.publish(
            subject, reply=reply, request=request, timeout=timeout, query=query, request_options=request_options
        )
        return _response.data


class AsyncNatsCoreMessagingExperimentalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNatsCoreMessagingExperimentalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNatsCoreMessagingExperimentalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNatsCoreMessagingExperimentalClient
        """
        return self._raw_client

    async def subscribe(
        self,
        subject: str,
        *,
        timeout: typing.Optional[int] = None,
        limit: typing.Optional[float] = None,
        nats_h: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[SubscribeResponse]:
        """
        Parameters
        ----------
        subject : str
            subject

        timeout : typing.Optional[int]
            how long to wait for a response in milliseconds. Default is 2000 milliseconds.

        limit : typing.Optional[float]
            the maximum number of keys to return, note internally it is limited to 1000

        nats_h : typing.Optional[str]
            Header prefix - any HTTP request with a header that has the `NatsH-` prefix will have the prefix dropped, and have the header included on the published message.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[SubscribeResponse]
            Success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            response = client.nats_core_messaging_experimental.subscribe(
                subject="subject",
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.subscribe(
            subject, timeout=timeout, limit=limit, nats_h=nats_h, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def request(
        self,
        subject: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RequestResponse:
        """
        Parameters
        ----------
        subject : str
            subject

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        timeout : typing.Optional[int]
            how long to wait for a response in milliseconds. Default is 2000 milliseconds.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestResponse
            Success response
        """
        _response = await self._raw_client.request(
            subject, request=request, timeout=timeout, request_options=request_options
        )
        return _response.data

    async def publish(
        self,
        subject: str,
        *,
        reply: str,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        timeout: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subject : str
            subject

        reply : str
            subject

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        timeout : typing.Optional[int]
            how long to wait for a response in milliseconds. Default is 2000 milliseconds.

        query : typing.Optional[str]
            queue group for the subscription

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = await self._raw_client.publish(
            subject, reply=reply, request=request, timeout=timeout, query=query, request_options=request_options
        )
        return _response.data
