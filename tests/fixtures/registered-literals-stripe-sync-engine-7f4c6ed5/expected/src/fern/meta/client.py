

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMetaClient, RawMetaClient
from .types.meta_destinations_get_response import MetaDestinationsGetResponse
from .types.meta_destinations_list_response import MetaDestinationsListResponse
from .types.meta_sources_get_response import MetaSourcesGetResponse
from .types.meta_sources_list_response import MetaSourcesListResponse


class MetaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMetaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMetaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMetaClient
        """
        return self._raw_client

    def sources_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetaSourcesListResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetaSourcesListResponse
            Available source connectors with their JSON Schema configs

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.meta.sources_list()
        """
        _response = self._raw_client.sources_list(request_options=request_options)
        return _response.data

    def sources_get(
        self, type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MetaSourcesGetResponse:
        """
        Parameters
        ----------
        type : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetaSourcesGetResponse
            Source connector spec

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.meta.sources_get(
            type="type",
        )
        """
        _response = self._raw_client.sources_get(type, request_options=request_options)
        return _response.data

    def destinations_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MetaDestinationsListResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetaDestinationsListResponse
            Available destination connectors with their JSON Schema configs

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.meta.destinations_list()
        """
        _response = self._raw_client.destinations_list(request_options=request_options)
        return _response.data

    def destinations_get(
        self, type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MetaDestinationsGetResponse:
        """
        Parameters
        ----------
        type : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetaDestinationsGetResponse
            Destination connector spec

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.meta.destinations_get(
            type="type",
        )
        """
        _response = self._raw_client.destinations_get(type, request_options=request_options)
        return _response.data


class AsyncMetaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMetaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMetaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMetaClient
        """
        return self._raw_client

    async def sources_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetaSourcesListResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetaSourcesListResponse
            Available source connectors with their JSON Schema configs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.meta.sources_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.sources_list(request_options=request_options)
        return _response.data

    async def sources_get(
        self, type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MetaSourcesGetResponse:
        """
        Parameters
        ----------
        type : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetaSourcesGetResponse
            Source connector spec

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.meta.sources_get(
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sources_get(type, request_options=request_options)
        return _response.data

    async def destinations_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MetaDestinationsListResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetaDestinationsListResponse
            Available destination connectors with their JSON Schema configs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.meta.destinations_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.destinations_list(request_options=request_options)
        return _response.data

    async def destinations_get(
        self, type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MetaDestinationsGetResponse:
        """
        Parameters
        ----------
        type : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetaDestinationsGetResponse
            Destination connector spec

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.meta.destinations_get(
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.destinations_get(type, request_options=request_options)
        return _response.data
