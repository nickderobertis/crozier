

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawNamedTypesClient, RawNamedTypesClient
from .types.named_types_deep_nested_response import NamedTypesDeepNestedResponse
from .types.named_types_order_items_response import NamedTypesOrderItemsResponse
from .types.named_types_profile_and_address_response import NamedTypesProfileAndAddressResponse
from .types.named_types_with_address_response import NamedTypesWithAddressResponse
from .types.named_types_with_profile_response import NamedTypesWithProfileResponse


class NamedTypesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNamedTypesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNamedTypesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNamedTypesClient
        """
        return self._raw_client

    def named_types_with_profile(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamedTypesWithProfileResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamedTypesWithProfileResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.named_types.named_types_with_profile()
        """
        _response = self._raw_client.named_types_with_profile(request_options=request_options)
        return _response.data

    def named_types_order_items(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamedTypesOrderItemsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamedTypesOrderItemsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.named_types.named_types_order_items()
        """
        _response = self._raw_client.named_types_order_items(request_options=request_options)
        return _response.data

    def named_types_with_address(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamedTypesWithAddressResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamedTypesWithAddressResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.named_types.named_types_with_address()
        """
        _response = self._raw_client.named_types_with_address(request_options=request_options)
        return _response.data

    def named_types_profile_and_address(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamedTypesProfileAndAddressResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamedTypesProfileAndAddressResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.named_types.named_types_profile_and_address()
        """
        _response = self._raw_client.named_types_profile_and_address(request_options=request_options)
        return _response.data

    def named_types_deep_nested(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamedTypesDeepNestedResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamedTypesDeepNestedResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.named_types.named_types_deep_nested()
        """
        _response = self._raw_client.named_types_deep_nested(request_options=request_options)
        return _response.data


class AsyncNamedTypesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNamedTypesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNamedTypesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNamedTypesClient
        """
        return self._raw_client

    async def named_types_with_profile(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamedTypesWithProfileResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamedTypesWithProfileResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.named_types.named_types_with_profile()


        asyncio.run(main())
        """
        _response = await self._raw_client.named_types_with_profile(request_options=request_options)
        return _response.data

    async def named_types_order_items(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamedTypesOrderItemsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamedTypesOrderItemsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.named_types.named_types_order_items()


        asyncio.run(main())
        """
        _response = await self._raw_client.named_types_order_items(request_options=request_options)
        return _response.data

    async def named_types_with_address(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamedTypesWithAddressResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamedTypesWithAddressResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.named_types.named_types_with_address()


        asyncio.run(main())
        """
        _response = await self._raw_client.named_types_with_address(request_options=request_options)
        return _response.data

    async def named_types_profile_and_address(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamedTypesProfileAndAddressResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamedTypesProfileAndAddressResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.named_types.named_types_profile_and_address()


        asyncio.run(main())
        """
        _response = await self._raw_client.named_types_profile_and_address(request_options=request_options)
        return _response.data

    async def named_types_deep_nested(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NamedTypesDeepNestedResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NamedTypesDeepNestedResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.named_types.named_types_deep_nested()


        asyncio.run(main())
        """
        _response = await self._raw_client.named_types_deep_nested(request_options=request_options)
        return _response.data
