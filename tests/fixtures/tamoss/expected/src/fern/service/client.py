

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.service import Service
from ..types.storage_backends_list import StorageBackendsList
from .raw_client import AsyncRawServiceClient, RawServiceClient


OMIT = typing.cast(typing.Any, ...)


class ServiceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawServiceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawServiceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawServiceClient
        """
        return self._raw_client

    def get_root(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        List of paths available from this API.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service.get_root()
        """
        _response = self._raw_client.get_root(request_options=request_options)
        return _response.data

    def head_root(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, str]:
        """
        Return root path headers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service.head_root()
        """
        _response = self._raw_client.head_root(request_options=request_options)
        return _response.headers

    def get_service(self, *, request_options: typing.Optional[RequestOptions] = None) -> Service:
        """
        Provide information about the service.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service.get_service()
        """
        _response = self._raw_client.get_service(request_options=request_options)
        return _response.data

    def post_service(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the service info.

        Parameters
        ----------
        name : typing.Optional[str]
            The service instance name

        description : typing.Optional[str]
            The service instance description

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
        client.service.post_service()
        """
        _response = self._raw_client.post_service(name=name, description=description, request_options=request_options)
        return _response.data

    def head_service(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, str]:
        """
        Return service path headers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service.head_service()
        """
        _response = self._raw_client.head_service(request_options=request_options)
        return _response.headers

    def get_storage_backends(self, *, request_options: typing.Optional[RequestOptions] = None) -> StorageBackendsList:
        """
        Provide information about the storage backends available on this service instance. These are populated on deployment of the service instance.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StorageBackendsList


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service.get_storage_backends()
        """
        _response = self._raw_client.get_storage_backends(request_options=request_options)
        return _response.data

    def head_storage_backends(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return storage backends path headers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.service.head_storage_backends()
        """
        _response = self._raw_client.head_storage_backends(request_options=request_options)
        return _response.headers


class AsyncServiceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawServiceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawServiceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawServiceClient
        """
        return self._raw_client

    async def get_root(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        List of paths available from this API.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service.get_root()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_root(request_options=request_options)
        return _response.data

    async def head_root(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, str]:
        """
        Return root path headers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service.head_root()


        asyncio.run(main())
        """
        _response = await self._raw_client.head_root(request_options=request_options)
        return _response.headers

    async def get_service(self, *, request_options: typing.Optional[RequestOptions] = None) -> Service:
        """
        Provide information about the service.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service.get_service()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_service(request_options=request_options)
        return _response.data

    async def post_service(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the service info.

        Parameters
        ----------
        name : typing.Optional[str]
            The service instance name

        description : typing.Optional[str]
            The service instance description

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
            await client.service.post_service()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_service(
            name=name, description=description, request_options=request_options
        )
        return _response.data

    async def head_service(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, str]:
        """
        Return service path headers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service.head_service()


        asyncio.run(main())
        """
        _response = await self._raw_client.head_service(request_options=request_options)
        return _response.headers

    async def get_storage_backends(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StorageBackendsList:
        """
        Provide information about the storage backends available on this service instance. These are populated on deployment of the service instance.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StorageBackendsList


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service.get_storage_backends()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_storage_backends(request_options=request_options)
        return _response.data

    async def head_storage_backends(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return storage backends path headers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.service.head_storage_backends()


        asyncio.run(main())
        """
        _response = await self._raw_client.head_storage_backends(request_options=request_options)
        return _response.headers
