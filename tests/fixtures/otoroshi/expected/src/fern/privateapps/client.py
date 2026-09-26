

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.empty import Empty
from .raw_client import AsyncRawPrivateappsClient, RawPrivateappsClient


OMIT = typing.cast(typing.Any, ...)


class PrivateappsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPrivateappsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPrivateappsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPrivateappsClient
        """
        return self._raw_client

    def otoroshi_controllers_private_apps_controller_send_self_update_link(
        self, id: str, username: str, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> Empty:
        """
        Parameters
        ----------
        id : str
            the id parameter

        username : str
            the username parameter

        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Empty
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.privateapps.otoroshi_controllers_private_apps_controller_send_self_update_link(
            id="id",
            username="username",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_private_apps_controller_send_self_update_link(
            id, username, request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_private_apps_controller_register_session(
        self, id: str, username: str, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> Empty:
        """
        Parameters
        ----------
        id : str
            the id parameter

        username : str
            the username parameter

        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Empty
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.privateapps.otoroshi_controllers_private_apps_controller_register_session(
            id="id",
            username="username",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_private_apps_controller_register_session(
            id, username, request=request, request_options=request_options
        )
        return _response.data


class AsyncPrivateappsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPrivateappsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPrivateappsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPrivateappsClient
        """
        return self._raw_client

    async def otoroshi_controllers_private_apps_controller_send_self_update_link(
        self, id: str, username: str, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> Empty:
        """
        Parameters
        ----------
        id : str
            the id parameter

        username : str
            the username parameter

        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Empty
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
            await client.privateapps.otoroshi_controllers_private_apps_controller_send_self_update_link(
                id="id",
                username="username",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_private_apps_controller_send_self_update_link(
            id, username, request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_private_apps_controller_register_session(
        self, id: str, username: str, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> Empty:
        """
        Parameters
        ----------
        id : str
            the id parameter

        username : str
            the username parameter

        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Empty
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
            await client.privateapps.otoroshi_controllers_private_apps_controller_register_session(
                id="id",
                username="username",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_private_apps_controller_register_session(
            id, username, request=request, request_options=request_options
        )
        return _response.data
