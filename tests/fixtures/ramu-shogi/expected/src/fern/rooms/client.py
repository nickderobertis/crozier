

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_room_response import CreateRoomResponse
from ..types.room_info import RoomInfo
from ..types.room_settings import RoomSettings
from .raw_client import AsyncRawRoomsClient, RawRoomsClient


OMIT = typing.cast(typing.Any, ...)


class RoomsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRoomsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRoomsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRoomsClient
        """
        return self._raw_client

    def create_room(
        self, *, settings: RoomSettings, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateRoomResponse:
        """
        Parameters
        ----------
        settings : RoomSettings

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateRoomResponse
            Created room

        Examples
        --------
        from fern import FernApi, RoomSettings, TimeControlSettings_Byoyomi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rooms.create_room(
            settings=RoomSettings(
                start_sfen="startSfen",
                time_control=TimeControlSettings_Byoyomi(
                    initial_ms=1,
                ),
                takeback=True,
            ),
        )
        """
        _response = self._raw_client.create_room(settings=settings, request_options=request_options)
        return _response.data

    def get_room(self, room_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RoomInfo:
        """
        Parameters
        ----------
        room_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoomInfo
            Get room information

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rooms.get_room(
            room_id="roomId",
        )
        """
        _response = self._raw_client.get_room(room_id, request_options=request_options)
        return _response.data


class AsyncRoomsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRoomsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRoomsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRoomsClient
        """
        return self._raw_client

    async def create_room(
        self, *, settings: RoomSettings, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateRoomResponse:
        """
        Parameters
        ----------
        settings : RoomSettings

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateRoomResponse
            Created room

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, RoomSettings, TimeControlSettings_Byoyomi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rooms.create_room(
                settings=RoomSettings(
                    start_sfen="startSfen",
                    time_control=TimeControlSettings_Byoyomi(
                        initial_ms=1,
                    ),
                    takeback=True,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_room(settings=settings, request_options=request_options)
        return _response.data

    async def get_room(self, room_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RoomInfo:
        """
        Parameters
        ----------
        room_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoomInfo
            Get room information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rooms.get_room(
                room_id="roomId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_room(room_id, request_options=request_options)
        return _response.data
