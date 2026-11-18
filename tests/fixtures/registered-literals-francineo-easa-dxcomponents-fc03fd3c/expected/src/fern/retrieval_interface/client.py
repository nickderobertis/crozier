

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawRetrievalInterfaceClient, RawRetrievalInterfaceClient


OMIT = typing.cast(typing.Any, ...)


class RetrievalInterfaceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRetrievalInterfaceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRetrievalInterfaceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRetrievalInterfaceClient
        """
        return self._raw_client

    def retrieve_uas_zones(
        self, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Note that some UAS Zones returned may lie entirely outside the requested ranges. Note that some data providers may choose not to permit unauthorized access to this endpoint, despite its definition in this specification for data providers that do choose to permit unauthorized access.

        Parameters
        ----------
        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            UAS Zones were successfully retrieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.retrieval_interface.retrieve_uas_zones(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.retrieve_uas_zones(request=request, request_options=request_options)
        return _response.data

    def retrieve_uas_zones_updates(
        self, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Note that some UAS Zones returned may lie entirely outside the requested ranges. Note that some data providers may choose not to permit unauthorized access to this endpoint, despite its definition in this specification for data providers that do choose to permit unauthorized access.

        Parameters
        ----------
        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            UAS Zones were successfully retrieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.retrieval_interface.retrieve_uas_zones_updates(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.retrieve_uas_zones_updates(request=request, request_options=request_options)
        return _response.data


class AsyncRetrievalInterfaceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRetrievalInterfaceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRetrievalInterfaceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRetrievalInterfaceClient
        """
        return self._raw_client

    async def retrieve_uas_zones(
        self, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Note that some UAS Zones returned may lie entirely outside the requested ranges. Note that some data providers may choose not to permit unauthorized access to this endpoint, despite its definition in this specification for data providers that do choose to permit unauthorized access.

        Parameters
        ----------
        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            UAS Zones were successfully retrieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.retrieval_interface.retrieve_uas_zones(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_uas_zones(request=request, request_options=request_options)
        return _response.data

    async def retrieve_uas_zones_updates(
        self, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Note that some UAS Zones returned may lie entirely outside the requested ranges. Note that some data providers may choose not to permit unauthorized access to this endpoint, despite its definition in this specification for data providers that do choose to permit unauthorized access.

        Parameters
        ----------
        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            UAS Zones were successfully retrieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.retrieval_interface.retrieve_uas_zones_updates(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_uas_zones_updates(request=request, request_options=request_options)
        return _response.data
