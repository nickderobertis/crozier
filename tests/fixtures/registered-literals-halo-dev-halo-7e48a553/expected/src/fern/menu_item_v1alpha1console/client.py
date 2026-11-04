

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.menu_item_tree_node import MenuItemTreeNode
from .raw_client import AsyncRawMenuItemV1Alpha1ConsoleClient, RawMenuItemV1Alpha1ConsoleClient


OMIT = typing.cast(typing.Any, ...)


class MenuItemV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMenuItemV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMenuItemV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMenuItemV1Alpha1ConsoleClient
        """
        return self._raw_client

    def list_menu_item_tree(
        self, *, menu_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MenuItemTreeNode]:
        """
        List MenuItems as a canonical tree for console menu management.

        Parameters
        ----------
        menu_name : str
            Menu metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MenuItemTreeNode]
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.menu_item_v1alpha1console.list_menu_item_tree(
            menu_name="menuName",
        )
        """
        _response = self._raw_client.list_menu_item_tree(menu_name=menu_name, request_options=request_options)
        return _response.data

    def update_menu_item_position(
        self,
        name: str,
        *,
        menu_name: str,
        before_name: typing.Optional[str] = OMIT,
        parent_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[MenuItemTreeNode]:
        """
        Move a MenuItem within its owning Menu.

        Parameters
        ----------
        name : str
            MenuItem metadata.name

        menu_name : str
            selected Menu metadata.name

        before_name : typing.Optional[str]
            target next sibling MenuItem metadata.name, or null to append

        parent_name : typing.Optional[str]
            target parent MenuItem metadata.name, or null for root

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MenuItemTreeNode]
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.menu_item_v1alpha1console.update_menu_item_position(
            name="name",
            menu_name="menuName",
        )
        """
        _response = self._raw_client.update_menu_item_position(
            name, menu_name=menu_name, before_name=before_name, parent_name=parent_name, request_options=request_options
        )
        return _response.data


class AsyncMenuItemV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMenuItemV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMenuItemV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMenuItemV1Alpha1ConsoleClient
        """
        return self._raw_client

    async def list_menu_item_tree(
        self, *, menu_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MenuItemTreeNode]:
        """
        List MenuItems as a canonical tree for console menu management.

        Parameters
        ----------
        menu_name : str
            Menu metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MenuItemTreeNode]
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
            await client.menu_item_v1alpha1console.list_menu_item_tree(
                menu_name="menuName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_menu_item_tree(menu_name=menu_name, request_options=request_options)
        return _response.data

    async def update_menu_item_position(
        self,
        name: str,
        *,
        menu_name: str,
        before_name: typing.Optional[str] = OMIT,
        parent_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[MenuItemTreeNode]:
        """
        Move a MenuItem within its owning Menu.

        Parameters
        ----------
        name : str
            MenuItem metadata.name

        menu_name : str
            selected Menu metadata.name

        before_name : typing.Optional[str]
            target next sibling MenuItem metadata.name, or null to append

        parent_name : typing.Optional[str]
            target parent MenuItem metadata.name, or null for root

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MenuItemTreeNode]
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
            await client.menu_item_v1alpha1console.update_menu_item_position(
                name="name",
                menu_name="menuName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_menu_item_position(
            name, menu_name=menu_name, before_name=before_name, parent_name=parent_name, request_options=request_options
        )
        return _response.data
