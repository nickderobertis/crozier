

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_id import AppId
from ..types.lobby import Lobby
from ..types.lobby_initial_config import LobbyInitialConfig
from ..types.lobby_visibility import LobbyVisibility
from ..types.region import Region
from ..types.room_id import RoomId
from .raw_client import AsyncRawLobbyV2Client, RawLobbyV2Client


OMIT = typing.cast(typing.Any, ...)


class LobbyV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLobbyV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLobbyV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLobbyV2Client
        """
        return self._raw_client

    def create_private_lobby(
        self,
        app_id: AppId,
        *,
        initial_config: LobbyInitialConfig,
        region: Region,
        room_id: typing.Optional[RoomId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Lobby:
        """
        Parameters
        ----------
        app_id : AppId

        initial_config : LobbyInitialConfig

        region : Region

        room_id : typing.Optional[RoomId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Lobby


        Examples
        --------
        from fern import FernApi, Region

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lobby_v2.create_private_lobby(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            room_id="2swovpy1fnunu",
            initial_config={"key": "value"},
            region=Region.SEATTLE,
        )
        """
        _response = self._raw_client.create_private_lobby(
            app_id, initial_config=initial_config, region=region, room_id=room_id, request_options=request_options
        )
        return _response.data

    def create_public_lobby(
        self,
        app_id: AppId,
        *,
        initial_config: LobbyInitialConfig,
        region: Region,
        room_id: typing.Optional[RoomId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Lobby:
        """
        Parameters
        ----------
        app_id : AppId

        initial_config : LobbyInitialConfig

        region : Region

        room_id : typing.Optional[RoomId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Lobby


        Examples
        --------
        from fern import FernApi, Region

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lobby_v2.create_public_lobby(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            room_id="2swovpy1fnunu",
            initial_config={"key": "value"},
            region=Region.SEATTLE,
        )
        """
        _response = self._raw_client.create_public_lobby(
            app_id, initial_config=initial_config, region=region, room_id=room_id, request_options=request_options
        )
        return _response.data

    def create_local_lobby(
        self,
        app_id: AppId,
        *,
        initial_config: LobbyInitialConfig,
        region: Region,
        room_id: typing.Optional[RoomId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Lobby:
        """
        Parameters
        ----------
        app_id : AppId

        initial_config : LobbyInitialConfig

        region : Region

        room_id : typing.Optional[RoomId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Lobby


        Examples
        --------
        from fern import FernApi, Region

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lobby_v2.create_local_lobby(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            room_id="2swovpy1fnunu",
            initial_config={"key": "value"},
            region=Region.SEATTLE,
        )
        """
        _response = self._raw_client.create_local_lobby(
            app_id, initial_config=initial_config, region=region, room_id=room_id, request_options=request_options
        )
        return _response.data

    def create_lobby_deprecated(
        self,
        app_id: AppId,
        *,
        visibility: LobbyVisibility,
        initial_config: LobbyInitialConfig,
        region: Region,
        room_id: typing.Optional[RoomId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Lobby:
        """
        Create a new lobby for an [application](https://hathora.dev/docs/concepts/hathora-entities#application). A lobby object is a wrapper around a [room](https://hathora.dev/docs/concepts/hathora-entities#room) object. With a lobby, you get additional functionality like configuring the visibility of the room, managing the state of a match, and retrieving a list of public lobbies to display to players.

        Parameters
        ----------
        app_id : AppId

        visibility : LobbyVisibility

        initial_config : LobbyInitialConfig

        region : Region

        room_id : typing.Optional[RoomId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Lobby


        Examples
        --------
        from fern import FernApi, LobbyVisibility, Region

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lobby_v2.create_lobby_deprecated(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            room_id="2swovpy1fnunu",
            visibility=LobbyVisibility.PRIVATE,
            initial_config={"key": "value"},
            region=Region.SEATTLE,
        )
        """
        _response = self._raw_client.create_lobby_deprecated(
            app_id,
            visibility=visibility,
            initial_config=initial_config,
            region=region,
            room_id=room_id,
            request_options=request_options,
        )
        return _response.data

    def list_active_public_lobbies_deprecated_v2(
        self,
        app_id: AppId,
        *,
        region: typing.Optional[Region] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Lobby]:
        """
        Get all active lobbies for a an [application](https://hathora.dev/docs/concepts/hathora-entities#application). Filter by optionally passing in a `region`. Use this endpoint to display all public lobbies that a player can join in the game client.

        Parameters
        ----------
        app_id : AppId

        region : typing.Optional[Region]
            Region to filter by. If omitted, active public lobbies in all regions will be returned.

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
        client.lobby_v2.list_active_public_lobbies_deprecated_v2(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
        )
        """
        _response = self._raw_client.list_active_public_lobbies_deprecated_v2(
            app_id, region=region, request_options=request_options
        )
        return _response.data

    def get_lobby_info(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Lobby:
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
        Lobby
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lobby_v2.get_lobby_info(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            room_id="2swovpy1fnunu",
        )
        """
        _response = self._raw_client.get_lobby_info(app_id, room_id, request_options=request_options)
        return _response.data

    def set_lobby_state(
        self,
        app_id: AppId,
        room_id: RoomId,
        *,
        state: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Lobby:
        """
        Set the state of a lobby. State is intended to be set by the server and must be smaller than 1MB. Use this endpoint to store match data like live player count to enforce max number of clients or persist end-game data (i.e. winner or final scores).

        Parameters
        ----------
        app_id : AppId

        room_id : RoomId

        state : typing.Dict[str, typing.Any]
            JSON blob to store metadata for a room. Must be smaller than 1MB.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Lobby
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.lobby_v2.set_lobby_state(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            room_id="2swovpy1fnunu",
            state={"key": "value"},
        )
        """
        _response = self._raw_client.set_lobby_state(app_id, room_id, state=state, request_options=request_options)
        return _response.data


class AsyncLobbyV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLobbyV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLobbyV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLobbyV2Client
        """
        return self._raw_client

    async def create_private_lobby(
        self,
        app_id: AppId,
        *,
        initial_config: LobbyInitialConfig,
        region: Region,
        room_id: typing.Optional[RoomId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Lobby:
        """
        Parameters
        ----------
        app_id : AppId

        initial_config : LobbyInitialConfig

        region : Region

        room_id : typing.Optional[RoomId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Lobby


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Region

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lobby_v2.create_private_lobby(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                room_id="2swovpy1fnunu",
                initial_config={"key": "value"},
                region=Region.SEATTLE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_private_lobby(
            app_id, initial_config=initial_config, region=region, room_id=room_id, request_options=request_options
        )
        return _response.data

    async def create_public_lobby(
        self,
        app_id: AppId,
        *,
        initial_config: LobbyInitialConfig,
        region: Region,
        room_id: typing.Optional[RoomId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Lobby:
        """
        Parameters
        ----------
        app_id : AppId

        initial_config : LobbyInitialConfig

        region : Region

        room_id : typing.Optional[RoomId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Lobby


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Region

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lobby_v2.create_public_lobby(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                room_id="2swovpy1fnunu",
                initial_config={"key": "value"},
                region=Region.SEATTLE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_public_lobby(
            app_id, initial_config=initial_config, region=region, room_id=room_id, request_options=request_options
        )
        return _response.data

    async def create_local_lobby(
        self,
        app_id: AppId,
        *,
        initial_config: LobbyInitialConfig,
        region: Region,
        room_id: typing.Optional[RoomId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Lobby:
        """
        Parameters
        ----------
        app_id : AppId

        initial_config : LobbyInitialConfig

        region : Region

        room_id : typing.Optional[RoomId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Lobby


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Region

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lobby_v2.create_local_lobby(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                room_id="2swovpy1fnunu",
                initial_config={"key": "value"},
                region=Region.SEATTLE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_local_lobby(
            app_id, initial_config=initial_config, region=region, room_id=room_id, request_options=request_options
        )
        return _response.data

    async def create_lobby_deprecated(
        self,
        app_id: AppId,
        *,
        visibility: LobbyVisibility,
        initial_config: LobbyInitialConfig,
        region: Region,
        room_id: typing.Optional[RoomId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Lobby:
        """
        Create a new lobby for an [application](https://hathora.dev/docs/concepts/hathora-entities#application). A lobby object is a wrapper around a [room](https://hathora.dev/docs/concepts/hathora-entities#room) object. With a lobby, you get additional functionality like configuring the visibility of the room, managing the state of a match, and retrieving a list of public lobbies to display to players.

        Parameters
        ----------
        app_id : AppId

        visibility : LobbyVisibility

        initial_config : LobbyInitialConfig

        region : Region

        room_id : typing.Optional[RoomId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Lobby


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LobbyVisibility, Region

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lobby_v2.create_lobby_deprecated(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                room_id="2swovpy1fnunu",
                visibility=LobbyVisibility.PRIVATE,
                initial_config={"key": "value"},
                region=Region.SEATTLE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_lobby_deprecated(
            app_id,
            visibility=visibility,
            initial_config=initial_config,
            region=region,
            room_id=room_id,
            request_options=request_options,
        )
        return _response.data

    async def list_active_public_lobbies_deprecated_v2(
        self,
        app_id: AppId,
        *,
        region: typing.Optional[Region] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Lobby]:
        """
        Get all active lobbies for a an [application](https://hathora.dev/docs/concepts/hathora-entities#application). Filter by optionally passing in a `region`. Use this endpoint to display all public lobbies that a player can join in the game client.

        Parameters
        ----------
        app_id : AppId

        region : typing.Optional[Region]
            Region to filter by. If omitted, active public lobbies in all regions will be returned.

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
            await client.lobby_v2.list_active_public_lobbies_deprecated_v2(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_active_public_lobbies_deprecated_v2(
            app_id, region=region, request_options=request_options
        )
        return _response.data

    async def get_lobby_info(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Lobby:
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
        Lobby
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lobby_v2.get_lobby_info(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                room_id="2swovpy1fnunu",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_lobby_info(app_id, room_id, request_options=request_options)
        return _response.data

    async def set_lobby_state(
        self,
        app_id: AppId,
        room_id: RoomId,
        *,
        state: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Lobby:
        """
        Set the state of a lobby. State is intended to be set by the server and must be smaller than 1MB. Use this endpoint to store match data like live player count to enforce max number of clients or persist end-game data (i.e. winner or final scores).

        Parameters
        ----------
        app_id : AppId

        room_id : RoomId

        state : typing.Dict[str, typing.Any]
            JSON blob to store metadata for a room. Must be smaller than 1MB.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Lobby
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.lobby_v2.set_lobby_state(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                room_id="2swovpy1fnunu",
                state={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_lobby_state(
            app_id, room_id, state=state, request_options=request_options
        )
        return _response.data
