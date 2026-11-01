

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawRecursiveTypesClient, RawRecursiveTypesClient
from .types.recursive_types_category_response import RecursiveTypesCategoryResponse
from .types.recursive_types_linked_list_response import RecursiveTypesLinkedListResponse
from .types.recursive_types_tree_response import RecursiveTypesTreeResponse


class RecursiveTypesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRecursiveTypesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRecursiveTypesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRecursiveTypesClient
        """
        return self._raw_client

    def recursive_types_tree(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RecursiveTypesTreeResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecursiveTypesTreeResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.recursive_types.recursive_types_tree()
        """
        _response = self._raw_client.recursive_types_tree(request_options=request_options)
        return _response.data

    def recursive_types_linked_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RecursiveTypesLinkedListResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecursiveTypesLinkedListResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.recursive_types.recursive_types_linked_list()
        """
        _response = self._raw_client.recursive_types_linked_list(request_options=request_options)
        return _response.data

    def recursive_types_category(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RecursiveTypesCategoryResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecursiveTypesCategoryResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.recursive_types.recursive_types_category(
            input="input",
        )
        """
        _response = self._raw_client.recursive_types_category(input=input, request_options=request_options)
        return _response.data


class AsyncRecursiveTypesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRecursiveTypesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRecursiveTypesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRecursiveTypesClient
        """
        return self._raw_client

    async def recursive_types_tree(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RecursiveTypesTreeResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecursiveTypesTreeResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.recursive_types.recursive_types_tree()


        asyncio.run(main())
        """
        _response = await self._raw_client.recursive_types_tree(request_options=request_options)
        return _response.data

    async def recursive_types_linked_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RecursiveTypesLinkedListResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecursiveTypesLinkedListResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.recursive_types.recursive_types_linked_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.recursive_types_linked_list(request_options=request_options)
        return _response.data

    async def recursive_types_category(
        self, *, input: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RecursiveTypesCategoryResponse:
        """
        Parameters
        ----------
        input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecursiveTypesCategoryResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.recursive_types.recursive_types_category(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.recursive_types_category(input=input, request_options=request_options)
        return _response.data
