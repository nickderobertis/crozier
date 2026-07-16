

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_key import ApiKey
from ..types.group import Group
from ..types.service import Service
from .raw_client import AsyncRawTemplatesClient, RawTemplatesClient


class TemplatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTemplatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTemplatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTemplatesClient
        """
        return self._raw_client

    def initiate_api_key(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiKey:
        """
        Get a template of an Otoroshi Api Key. The generated entity is not persisted

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.templates.initiate_api_key()
        """
        _response = self._raw_client.initiate_api_key(request_options=request_options)
        return _response.data

    def initiate_service_group(self, *, request_options: typing.Optional[RequestOptions] = None) -> Group:
        """
        Get a template of an Otoroshi service group. The generated entity is not persisted

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.templates.initiate_service_group()
        """
        _response = self._raw_client.initiate_service_group(request_options=request_options)
        return _response.data

    def initiate_service(self, *, request_options: typing.Optional[RequestOptions] = None) -> Service:
        """
        Get a template of an Otoroshi service descriptor. The generated entity is not persisted

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.templates.initiate_service()
        """
        _response = self._raw_client.initiate_service(request_options=request_options)
        return _response.data


class AsyncTemplatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTemplatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTemplatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTemplatesClient
        """
        return self._raw_client

    async def initiate_api_key(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiKey:
        """
        Get a template of an Otoroshi Api Key. The generated entity is not persisted

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.templates.initiate_api_key()


        asyncio.run(main())
        """
        _response = await self._raw_client.initiate_api_key(request_options=request_options)
        return _response.data

    async def initiate_service_group(self, *, request_options: typing.Optional[RequestOptions] = None) -> Group:
        """
        Get a template of an Otoroshi service group. The generated entity is not persisted

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.templates.initiate_service_group()


        asyncio.run(main())
        """
        _response = await self._raw_client.initiate_service_group(request_options=request_options)
        return _response.data

    async def initiate_service(self, *, request_options: typing.Optional[RequestOptions] = None) -> Service:
        """
        Get a template of an Otoroshi service descriptor. The generated entity is not persisted

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.templates.initiate_service()


        asyncio.run(main())
        """
        _response = await self._raw_client.initiate_service(request_options=request_options)
        return _response.data
