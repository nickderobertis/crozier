

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.category_tree_node import CategoryTreeNode
from .raw_client import AsyncRawCategoryV1Alpha1ConsoleClient, RawCategoryV1Alpha1ConsoleClient


OMIT = typing.cast(typing.Any, ...)


class CategoryV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCategoryV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCategoryV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCategoryV1Alpha1ConsoleClient
        """
        return self._raw_client

    def list_category_tree(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CategoryTreeNode]:
        """
        List Categories as a canonical tree for console category management.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CategoryTreeNode]
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.category_v1alpha1console.list_category_tree()
        """
        _response = self._raw_client.list_category_tree(request_options=request_options)
        return _response.data

    def update_category_position(
        self,
        name: str,
        *,
        before_name: typing.Optional[str] = OMIT,
        parent_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CategoryTreeNode]:
        """
        Move a Category within the Console category tree.

        Parameters
        ----------
        name : str
            Category metadata.name

        before_name : typing.Optional[str]
            target next sibling Category metadata.name, or null to append

        parent_name : typing.Optional[str]
            target parent Category metadata.name, or null for root

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CategoryTreeNode]
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.category_v1alpha1console.update_category_position(
            name="name",
        )
        """
        _response = self._raw_client.update_category_position(
            name, before_name=before_name, parent_name=parent_name, request_options=request_options
        )
        return _response.data


class AsyncCategoryV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCategoryV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCategoryV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCategoryV1Alpha1ConsoleClient
        """
        return self._raw_client

    async def list_category_tree(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CategoryTreeNode]:
        """
        List Categories as a canonical tree for console category management.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CategoryTreeNode]
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.category_v1alpha1console.list_category_tree()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_category_tree(request_options=request_options)
        return _response.data

    async def update_category_position(
        self,
        name: str,
        *,
        before_name: typing.Optional[str] = OMIT,
        parent_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CategoryTreeNode]:
        """
        Move a Category within the Console category tree.

        Parameters
        ----------
        name : str
            Category metadata.name

        before_name : typing.Optional[str]
            target next sibling Category metadata.name, or null to append

        parent_name : typing.Optional[str]
            target parent Category metadata.name, or null for root

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CategoryTreeNode]
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.category_v1alpha1console.update_category_position(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_category_position(
            name, before_name=before_name, parent_name=parent_name, request_options=request_options
        )
        return _response.data
