

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.item import Item
from ..types.list_namespace_response import ListNamespaceResponse
from ..types.search_items_response import SearchItemsResponse
from .raw_client import AsyncRawStoreClient, RawStoreClient


OMIT = typing.cast(typing.Any, ...)


class StoreClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStoreClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStoreClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStoreClient
        """
        return self._raw_client

    def get_item(
        self,
        *,
        key: str,
        namespace: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Item:
        """
        Parameters
        ----------
        key : str

        namespace : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Item
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.store.get_item(
            key="key",
        )
        """
        _response = self._raw_client.get_item(key=key, namespace=namespace, request_options=request_options)
        return _response.data

    def put_item(
        self,
        *,
        namespace: typing.Sequence[str],
        key: str,
        value: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        namespace : typing.Sequence[str]
            A list of strings representing the namespace path.

        key : str
            The unique identifier for the item within the namespace.

        value : typing.Dict[str, typing.Any]
            A dictionary containing the item's data.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.store.put_item(
            namespace=["namespace"],
            key="key",
            value={"key": "value"},
        )
        """
        _response = self._raw_client.put_item(
            namespace=namespace, key=key, value=value, request_options=request_options
        )
        return _response.data

    def delete_item(
        self,
        *,
        key: str,
        namespace: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        key : str
            The unique identifier for the item.

        namespace : typing.Optional[typing.Sequence[str]]
            A list of strings representing the namespace path.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.store.delete_item(
            key="key",
        )
        """
        _response = self._raw_client.delete_item(key=key, namespace=namespace, request_options=request_options)
        return _response.data

    def search_items(
        self,
        *,
        namespace_prefix: typing.Optional[typing.Sequence[str]] = OMIT,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchItemsResponse:
        """
        Parameters
        ----------
        namespace_prefix : typing.Optional[typing.Sequence[str]]
            List of strings representing the namespace prefix.

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            Optional dictionary of key-value pairs to filter results.

        limit : typing.Optional[int]
            Maximum number of items to return (default is 10).

        offset : typing.Optional[int]
            Number of items to skip before returning results (default is 0).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchItemsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.store.search_items()
        """
        _response = self._raw_client.search_items(
            namespace_prefix=namespace_prefix,
            filter=filter,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def list_namespaces(
        self,
        *,
        prefix: typing.Optional[typing.Sequence[str]] = OMIT,
        suffix: typing.Optional[typing.Sequence[str]] = OMIT,
        max_depth: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListNamespaceResponse:
        """
        Parameters
        ----------
        prefix : typing.Optional[typing.Sequence[str]]
            Optional list of strings representing the prefix to filter namespaces.

        suffix : typing.Optional[typing.Sequence[str]]
            Optional list of strings representing the suffix to filter namespaces.

        max_depth : typing.Optional[int]
            Optional integer specifying the maximum depth of namespaces to return.

        limit : typing.Optional[int]
            Maximum number of namespaces to return (default is 100).

        offset : typing.Optional[int]
            Number of namespaces to skip before returning results (default is 0).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListNamespaceResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.store.list_namespaces()
        """
        _response = self._raw_client.list_namespaces(
            prefix=prefix,
            suffix=suffix,
            max_depth=max_depth,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data


class AsyncStoreClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStoreClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStoreClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStoreClient
        """
        return self._raw_client

    async def get_item(
        self,
        *,
        key: str,
        namespace: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Item:
        """
        Parameters
        ----------
        key : str

        namespace : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Item
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.store.get_item(
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_item(key=key, namespace=namespace, request_options=request_options)
        return _response.data

    async def put_item(
        self,
        *,
        namespace: typing.Sequence[str],
        key: str,
        value: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        namespace : typing.Sequence[str]
            A list of strings representing the namespace path.

        key : str
            The unique identifier for the item within the namespace.

        value : typing.Dict[str, typing.Any]
            A dictionary containing the item's data.

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.store.put_item(
                namespace=["namespace"],
                key="key",
                value={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_item(
            namespace=namespace, key=key, value=value, request_options=request_options
        )
        return _response.data

    async def delete_item(
        self,
        *,
        key: str,
        namespace: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        key : str
            The unique identifier for the item.

        namespace : typing.Optional[typing.Sequence[str]]
            A list of strings representing the namespace path.

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.store.delete_item(
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_item(key=key, namespace=namespace, request_options=request_options)
        return _response.data

    async def search_items(
        self,
        *,
        namespace_prefix: typing.Optional[typing.Sequence[str]] = OMIT,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchItemsResponse:
        """
        Parameters
        ----------
        namespace_prefix : typing.Optional[typing.Sequence[str]]
            List of strings representing the namespace prefix.

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            Optional dictionary of key-value pairs to filter results.

        limit : typing.Optional[int]
            Maximum number of items to return (default is 10).

        offset : typing.Optional[int]
            Number of items to skip before returning results (default is 0).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchItemsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.store.search_items()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_items(
            namespace_prefix=namespace_prefix,
            filter=filter,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def list_namespaces(
        self,
        *,
        prefix: typing.Optional[typing.Sequence[str]] = OMIT,
        suffix: typing.Optional[typing.Sequence[str]] = OMIT,
        max_depth: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListNamespaceResponse:
        """
        Parameters
        ----------
        prefix : typing.Optional[typing.Sequence[str]]
            Optional list of strings representing the prefix to filter namespaces.

        suffix : typing.Optional[typing.Sequence[str]]
            Optional list of strings representing the suffix to filter namespaces.

        max_depth : typing.Optional[int]
            Optional integer specifying the maximum depth of namespaces to return.

        limit : typing.Optional[int]
            Maximum number of namespaces to return (default is 100).

        offset : typing.Optional[int]
            Number of namespaces to skip before returning results (default is 0).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListNamespaceResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.store.list_namespaces()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_namespaces(
            prefix=prefix,
            suffix=suffix,
            max_depth=max_depth,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data
