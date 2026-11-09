

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_id import AppId
from ..types.lobby import Lobby
from ..types.region import Region
from ..types.room_id import RoomId
from .raw_client import AsyncRawLobbyV1Client, RawLobbyV1Client


class LobbyV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLobbyV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLobbyV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLobbyV1Client
        """
        return self._raw_client

    def create_private_lobby_deprecated(
        self,
        app_id: AppId,
        *,
        region: typing.Optional[Region] = None,
        local: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RoomId:
        """
        Parameters
        ----------
        app_id : AppId

        region : typing.Optional[Region]

        local : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoomId
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lobby_v1.create_private_lobby_deprecated(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
        )
        """
        _response = self._raw_client.create_private_lobby_deprecated(
            app_id, region=region, local=local, request_options=request_options
        )
        return _response.data

    def create_public_lobby_deprecated(
        self,
        app_id: AppId,
        *,
        region: typing.Optional[Region] = None,
        local: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RoomId:
        """
        Parameters
        ----------
        app_id : AppId

        region : typing.Optional[Region]

        local : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoomId
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lobby_v1.create_public_lobby_deprecated(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
        )
        """
        _response = self._raw_client.create_public_lobby_deprecated(
            app_id, region=region, local=local, request_options=request_options
        )
        return _response.data

    def list_active_public_lobbies_deprecated_v1(
        self,
        app_id: AppId,
        *,
        local: typing.Optional[bool] = None,
        region: typing.Optional[Region] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Lobby]:
        """
        Parameters
        ----------
        app_id : AppId

        local : typing.Optional[bool]

        region : typing.Optional[Region]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Lobby]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lobby_v1.list_active_public_lobbies_deprecated_v1(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
        )
        """
        _response = self._raw_client.list_active_public_lobbies_deprecated_v1(
            app_id, local=local, region=region, request_options=request_options
        )
        return _response.data


class AsyncLobbyV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLobbyV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLobbyV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLobbyV1Client
        """
        return self._raw_client

    async def create_private_lobby_deprecated(
        self,
        app_id: AppId,
        *,
        region: typing.Optional[Region] = None,
        local: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RoomId:
        """
        Parameters
        ----------
        app_id : AppId

        region : typing.Optional[Region]

        local : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoomId
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lobby_v1.create_private_lobby_deprecated(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_private_lobby_deprecated(
            app_id, region=region, local=local, request_options=request_options
        )
        return _response.data

    async def create_public_lobby_deprecated(
        self,
        app_id: AppId,
        *,
        region: typing.Optional[Region] = None,
        local: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RoomId:
        """
        Parameters
        ----------
        app_id : AppId

        region : typing.Optional[Region]

        local : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoomId
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lobby_v1.create_public_lobby_deprecated(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_public_lobby_deprecated(
            app_id, region=region, local=local, request_options=request_options
        )
        return _response.data

    async def list_active_public_lobbies_deprecated_v1(
        self,
        app_id: AppId,
        *,
        local: typing.Optional[bool] = None,
        region: typing.Optional[Region] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Lobby]:
        """
        Parameters
        ----------
        app_id : AppId

        local : typing.Optional[bool]

        region : typing.Optional[Region]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Lobby]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lobby_v1.list_active_public_lobbies_deprecated_v1(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_active_public_lobbies_deprecated_v1(
            app_id, local=local, region=region, request_options=request_options
        )
        return _response.data
