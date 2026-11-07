

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_id import AppId
from ..types.lobby_v3 import LobbyV3
from ..types.lobby_visibility import LobbyVisibility
from ..types.region import Region
from ..types.room_config import RoomConfig
from ..types.room_id import RoomId
from ..types.short_code import ShortCode
from .raw_client import AsyncRawLobbyV3Client, RawLobbyV3Client


OMIT = typing.cast(typing.Any, ...)


class LobbyV3Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLobbyV3Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLobbyV3Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLobbyV3Client
        """
        return self._raw_client

    def create_lobby(
        self,
        app_id: AppId,
        *,
        visibility: LobbyVisibility,
        region: Region,
        short_code: typing.Optional[ShortCode] = None,
        room_id: typing.Optional[RoomId] = None,
        room_config: typing.Optional[RoomConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LobbyV3:
        """
        Create a new lobby for an [application](https://hathora.dev/docs/concepts/hathora-entities#application). A lobby object is a wrapper around a [room](https://hathora.dev/docs/concepts/hathora-entities#room) object. With a lobby, you get additional functionality like configuring the visibility of the room, managing the state of a match, and retrieving a list of public lobbies to display to players.

        Parameters
        ----------
        app_id : AppId

        visibility : LobbyVisibility

        region : Region

        short_code : typing.Optional[ShortCode]

        room_id : typing.Optional[RoomId]

        room_config : typing.Optional[RoomConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyV3


        Examples
        --------
        from fern import FernApi, LobbyVisibility, Region

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lobby_v3.create_lobby(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            short_code="LFG4",
            room_id="2swovpy1fnunu",
            visibility=LobbyVisibility.PRIVATE,
            region=Region.SEATTLE,
        )
        """
        _response = self._raw_client.create_lobby(
            app_id,
            visibility=visibility,
            region=region,
            short_code=short_code,
            room_id=room_id,
            room_config=room_config,
            request_options=request_options,
        )
        return _response.data

    def list_active_public_lobbies(
        self,
        app_id: AppId,
        *,
        region: typing.Optional[Region] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[LobbyV3]:
        """
        Get all active lobbies for a given [application](https://hathora.dev/docs/concepts/hathora-entities#application). Filter the array by optionally passing in a `region`. Use this endpoint to display all public lobbies that a player can join in the game client.

        Parameters
        ----------
        app_id : AppId

        region : typing.Optional[Region]
            If omitted, active public lobbies in all regions will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LobbyV3]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lobby_v3.list_active_public_lobbies(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
        )
        """
        _response = self._raw_client.list_active_public_lobbies(app_id, region=region, request_options=request_options)
        return _response.data

    def get_lobby_info_by_room_id(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LobbyV3:
        """
        Get details for a lobby.

        Parameters
        ----------
        app_id : AppId

        room_id : RoomId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyV3
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lobby_v3.get_lobby_info_by_room_id(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            room_id="2swovpy1fnunu",
        )
        """
        _response = self._raw_client.get_lobby_info_by_room_id(app_id, room_id, request_options=request_options)
        return _response.data

    def get_lobby_info_by_short_code(
        self, app_id: AppId, short_code: ShortCode, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LobbyV3:
        """
        Get details for a lobby. If 2 or more lobbies have the same `shortCode`, then the most recently created lobby will be returned.

        Parameters
        ----------
        app_id : AppId

        short_code : ShortCode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyV3
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lobby_v3.get_lobby_info_by_short_code(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            short_code="LFG4",
        )
        """
        _response = self._raw_client.get_lobby_info_by_short_code(app_id, short_code, request_options=request_options)
        return _response.data


class AsyncLobbyV3Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLobbyV3Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLobbyV3Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLobbyV3Client
        """
        return self._raw_client

    async def create_lobby(
        self,
        app_id: AppId,
        *,
        visibility: LobbyVisibility,
        region: Region,
        short_code: typing.Optional[ShortCode] = None,
        room_id: typing.Optional[RoomId] = None,
        room_config: typing.Optional[RoomConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LobbyV3:
        """
        Create a new lobby for an [application](https://hathora.dev/docs/concepts/hathora-entities#application). A lobby object is a wrapper around a [room](https://hathora.dev/docs/concepts/hathora-entities#room) object. With a lobby, you get additional functionality like configuring the visibility of the room, managing the state of a match, and retrieving a list of public lobbies to display to players.

        Parameters
        ----------
        app_id : AppId

        visibility : LobbyVisibility

        region : Region

        short_code : typing.Optional[ShortCode]

        room_id : typing.Optional[RoomId]

        room_config : typing.Optional[RoomConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyV3


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LobbyVisibility, Region

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lobby_v3.create_lobby(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                short_code="LFG4",
                room_id="2swovpy1fnunu",
                visibility=LobbyVisibility.PRIVATE,
                region=Region.SEATTLE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_lobby(
            app_id,
            visibility=visibility,
            region=region,
            short_code=short_code,
            room_id=room_id,
            room_config=room_config,
            request_options=request_options,
        )
        return _response.data

    async def list_active_public_lobbies(
        self,
        app_id: AppId,
        *,
        region: typing.Optional[Region] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[LobbyV3]:
        """
        Get all active lobbies for a given [application](https://hathora.dev/docs/concepts/hathora-entities#application). Filter the array by optionally passing in a `region`. Use this endpoint to display all public lobbies that a player can join in the game client.

        Parameters
        ----------
        app_id : AppId

        region : typing.Optional[Region]
            If omitted, active public lobbies in all regions will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LobbyV3]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lobby_v3.list_active_public_lobbies(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_active_public_lobbies(
            app_id, region=region, request_options=request_options
        )
        return _response.data

    async def get_lobby_info_by_room_id(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LobbyV3:
        """
        Get details for a lobby.

        Parameters
        ----------
        app_id : AppId

        room_id : RoomId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyV3
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lobby_v3.get_lobby_info_by_room_id(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                room_id="2swovpy1fnunu",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_lobby_info_by_room_id(app_id, room_id, request_options=request_options)
        return _response.data

    async def get_lobby_info_by_short_code(
        self, app_id: AppId, short_code: ShortCode, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LobbyV3:
        """
        Get details for a lobby. If 2 or more lobbies have the same `shortCode`, then the most recently created lobby will be returned.

        Parameters
        ----------
        app_id : AppId

        short_code : ShortCode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyV3
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lobby_v3.get_lobby_info_by_short_code(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                short_code="LFG4",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_lobby_info_by_short_code(
            app_id, short_code, request_options=request_options
        )
        return _response.data
