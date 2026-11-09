

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_id import AppId
from ..types.connection_info_v2 import ConnectionInfoV2
from ..types.create_room_response import CreateRoomResponse
from ..types.process_id import ProcessId
from ..types.region import Region
from ..types.room import Room
from ..types.room_config import RoomConfig
from ..types.room_id import RoomId
from ..types.room_without_allocations import RoomWithoutAllocations
from .raw_client import AsyncRawRoomV2Client, RawRoomV2Client


OMIT = typing.cast(typing.Any, ...)


class RoomV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRoomV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRoomV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRoomV2Client
        """
        return self._raw_client

    def create_room(
        self,
        app_id: AppId,
        *,
        region: Region,
        room_id: typing.Optional[RoomId] = None,
        room_config: typing.Optional[RoomConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateRoomResponse:
        """
        Create a new [room](https://hathora.dev/docs/concepts/hathora-entities#room) for an existing [application](https://hathora.dev/docs/concepts/hathora-entities#application). Poll the [`GetConnectionInfo()`](https://hathora.dev/api#tag/RoomV2/operation/GetConnectionInfo) endpoint to get connection details for an active room.

        Parameters
        ----------
        app_id : AppId

        region : Region

        room_id : typing.Optional[RoomId]

        room_config : typing.Optional[RoomConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateRoomResponse


        Examples
        --------
        from fern import FernApi, Region

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.room_v2.create_room(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            room_id="2swovpy1fnunu",
            region=Region.SEATTLE,
        )
        """
        _response = self._raw_client.create_room(
            app_id, region=region, room_id=room_id, room_config=room_config, request_options=request_options
        )
        return _response.data

    def get_room_info(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Room:
        """
        Retreive current and historical allocation data for a [room](https://hathora.dev/docs/concepts/hathora-entities#room).

        Parameters
        ----------
        app_id : AppId

        room_id : RoomId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Room
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.room_v2.get_room_info(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            room_id="2swovpy1fnunu",
        )
        """
        _response = self._raw_client.get_room_info(app_id, room_id, request_options=request_options)
        return _response.data

    def get_active_rooms_for_process(
        self, app_id: AppId, process_id: ProcessId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RoomWithoutAllocations]:
        """
        Get all active [rooms](https://hathora.dev/docs/concepts/hathora-entities#room) for a given [process](https://hathora.dev/docs/concepts/hathora-entities#process).

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RoomWithoutAllocations]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.room_v2.get_active_rooms_for_process(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
        )
        """
        _response = self._raw_client.get_active_rooms_for_process(app_id, process_id, request_options=request_options)
        return _response.data

    def get_inactive_rooms_for_process(
        self, app_id: AppId, process_id: ProcessId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RoomWithoutAllocations]:
        """
        Get all inactive [rooms](https://hathora.dev/docs/concepts/hathora-entities#room) for a given [process](https://hathora.dev/docs/concepts/hathora-entities#process).

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RoomWithoutAllocations]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.room_v2.get_inactive_rooms_for_process(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
        )
        """
        _response = self._raw_client.get_inactive_rooms_for_process(app_id, process_id, request_options=request_options)
        return _response.data

    def destroy_room(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Destroy a [room](https://hathora.dev/docs/concepts/hathora-entities#room). All associated metadata is deleted.

        Parameters
        ----------
        app_id : AppId

        room_id : RoomId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.room_v2.destroy_room(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            room_id="2swovpy1fnunu",
        )
        """
        _response = self._raw_client.destroy_room(app_id, room_id, request_options=request_options)
        return _response.data

    def suspend_room(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Suspend a [room](https://hathora.dev/docs/concepts/hathora-entities#room). The room is unallocated from the process but can be rescheduled later using the same `roomId`.

        Parameters
        ----------
        app_id : AppId

        room_id : RoomId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.room_v2.suspend_room(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            room_id="2swovpy1fnunu",
        )
        """
        _response = self._raw_client.suspend_room(app_id, room_id, request_options=request_options)
        return _response.data

    def get_connection_info(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionInfoV2:
        """
        Poll this endpoint to get connection details to a [room](https://hathora.dev/docs/concepts/hathora-entities#room). Clients can call this endpoint without authentication.

        Parameters
        ----------
        app_id : AppId

        room_id : RoomId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionInfoV2
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.room_v2.get_connection_info(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            room_id="2swovpy1fnunu",
        )
        """
        _response = self._raw_client.get_connection_info(app_id, room_id, request_options=request_options)
        return _response.data

    def update_room_config(
        self,
        app_id: AppId,
        room_id: RoomId,
        *,
        room_config: RoomConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        app_id : AppId

        room_id : RoomId

        room_config : RoomConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.room_v2.update_room_config(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            room_id="2swovpy1fnunu",
            room_config='{"name":"my-room"}',
        )
        """
        _response = self._raw_client.update_room_config(
            app_id, room_id, room_config=room_config, request_options=request_options
        )
        return _response.data


class AsyncRoomV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRoomV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRoomV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRoomV2Client
        """
        return self._raw_client

    async def create_room(
        self,
        app_id: AppId,
        *,
        region: Region,
        room_id: typing.Optional[RoomId] = None,
        room_config: typing.Optional[RoomConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateRoomResponse:
        """
        Create a new [room](https://hathora.dev/docs/concepts/hathora-entities#room) for an existing [application](https://hathora.dev/docs/concepts/hathora-entities#application). Poll the [`GetConnectionInfo()`](https://hathora.dev/api#tag/RoomV2/operation/GetConnectionInfo) endpoint to get connection details for an active room.

        Parameters
        ----------
        app_id : AppId

        region : Region

        room_id : typing.Optional[RoomId]

        room_config : typing.Optional[RoomConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateRoomResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Region

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.room_v2.create_room(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                room_id="2swovpy1fnunu",
                region=Region.SEATTLE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_room(
            app_id, region=region, room_id=room_id, room_config=room_config, request_options=request_options
        )
        return _response.data

    async def get_room_info(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Room:
        """
        Retreive current and historical allocation data for a [room](https://hathora.dev/docs/concepts/hathora-entities#room).

        Parameters
        ----------
        app_id : AppId

        room_id : RoomId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Room
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.room_v2.get_room_info(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                room_id="2swovpy1fnunu",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_room_info(app_id, room_id, request_options=request_options)
        return _response.data

    async def get_active_rooms_for_process(
        self, app_id: AppId, process_id: ProcessId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RoomWithoutAllocations]:
        """
        Get all active [rooms](https://hathora.dev/docs/concepts/hathora-entities#room) for a given [process](https://hathora.dev/docs/concepts/hathora-entities#process).

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RoomWithoutAllocations]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.room_v2.get_active_rooms_for_process(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_active_rooms_for_process(
            app_id, process_id, request_options=request_options
        )
        return _response.data

    async def get_inactive_rooms_for_process(
        self, app_id: AppId, process_id: ProcessId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RoomWithoutAllocations]:
        """
        Get all inactive [rooms](https://hathora.dev/docs/concepts/hathora-entities#room) for a given [process](https://hathora.dev/docs/concepts/hathora-entities#process).

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RoomWithoutAllocations]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.room_v2.get_inactive_rooms_for_process(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_inactive_rooms_for_process(
            app_id, process_id, request_options=request_options
        )
        return _response.data

    async def destroy_room(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Destroy a [room](https://hathora.dev/docs/concepts/hathora-entities#room). All associated metadata is deleted.

        Parameters
        ----------
        app_id : AppId

        room_id : RoomId

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.room_v2.destroy_room(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                room_id="2swovpy1fnunu",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.destroy_room(app_id, room_id, request_options=request_options)
        return _response.data

    async def suspend_room(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Suspend a [room](https://hathora.dev/docs/concepts/hathora-entities#room). The room is unallocated from the process but can be rescheduled later using the same `roomId`.

        Parameters
        ----------
        app_id : AppId

        room_id : RoomId

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.room_v2.suspend_room(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                room_id="2swovpy1fnunu",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.suspend_room(app_id, room_id, request_options=request_options)
        return _response.data

    async def get_connection_info(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionInfoV2:
        """
        Poll this endpoint to get connection details to a [room](https://hathora.dev/docs/concepts/hathora-entities#room). Clients can call this endpoint without authentication.

        Parameters
        ----------
        app_id : AppId

        room_id : RoomId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionInfoV2
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.room_v2.get_connection_info(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                room_id="2swovpy1fnunu",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_connection_info(app_id, room_id, request_options=request_options)
        return _response.data

    async def update_room_config(
        self,
        app_id: AppId,
        room_id: RoomId,
        *,
        room_config: RoomConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        app_id : AppId

        room_id : RoomId

        room_config : RoomConfig

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.room_v2.update_room_config(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                room_id="2swovpy1fnunu",
                room_config='{"name":"my-room"}',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_room_config(
            app_id, room_id, room_config=room_config, request_options=request_options
        )
        return _response.data
