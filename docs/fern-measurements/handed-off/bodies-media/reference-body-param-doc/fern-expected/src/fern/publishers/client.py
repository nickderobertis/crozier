

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.publisher_record import PublisherRecord
from .raw_client import AsyncRawPublishersClient, RawPublishersClient


OMIT = typing.cast(typing.Any, ...)


class PublishersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPublishersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPublishersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPublishersClient
        """
        return self._raw_client

    def add_publisher(
        self,
        *,
        username: typing.Optional[str] = OMIT,
        secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        username : typing.Optional[str]

        secret : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.publishers.add_publisher()
        """
        _response = self._raw_client.add_publisher(username=username, secret=secret, request_options=request_options)
        return _response.data

    def get_publisher(
        self, publisher_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PublisherRecord:
        """
        Parameters
        ----------
        publisher_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublisherRecord
            The publisher.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.publishers.get_publisher(
            publisher_id="publisherId",
        )
        """
        _response = self._raw_client.get_publisher(publisher_id, request_options=request_options)
        return _response.data


class AsyncPublishersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPublishersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPublishersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPublishersClient
        """
        return self._raw_client

    async def add_publisher(
        self,
        *,
        username: typing.Optional[str] = OMIT,
        secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        username : typing.Optional[str]

        secret : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.publishers.add_publisher()


        asyncio.run(main())
        """
        _response = await self._raw_client.add_publisher(
            username=username, secret=secret, request_options=request_options
        )
        return _response.data

    async def get_publisher(
        self, publisher_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PublisherRecord:
        """
        Parameters
        ----------
        publisher_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublisherRecord
            The publisher.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.publishers.get_publisher(
                publisher_id="publisherId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_publisher(publisher_id, request_options=request_options)
        return _response.data
