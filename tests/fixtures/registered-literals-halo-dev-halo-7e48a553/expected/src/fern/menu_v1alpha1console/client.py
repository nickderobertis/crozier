

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.menu import Menu
from .raw_client import AsyncRawMenuV1Alpha1ConsoleClient, RawMenuV1Alpha1ConsoleClient


class MenuV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMenuV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMenuV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMenuV1Alpha1ConsoleClient
        """
        return self._raw_client

    def delete_menu(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Menu:
        """
        Delete a Menu and MenuItems owned by the Menu.

        Parameters
        ----------
        name : str
            Menu metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Menu
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.menu_v1alpha1console.delete_menu(
            name="name",
        )
        """
        _response = self._raw_client.delete_menu(name, request_options=request_options)
        return _response.data


class AsyncMenuV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMenuV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMenuV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMenuV1Alpha1ConsoleClient
        """
        return self._raw_client

    async def delete_menu(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Menu:
        """
        Delete a Menu and MenuItems owned by the Menu.

        Parameters
        ----------
        name : str
            Menu metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Menu
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
            await client.menu_v1alpha1console.delete_menu(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_menu(name, request_options=request_options)
        return _response.data
