

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_id import AppId
from ..types.connection_info import ConnectionInfo
from ..types.process_id import ProcessId
from ..types.region import Region
from ..types.room import Room
from ..types.room_config import RoomConfig
from ..types.room_id import RoomId
from ..types.room_without_allocations import RoomWithoutAllocations
from .raw_client import AsyncRawRoomV1Client, RawRoomV1Client


OMIT = typing.cast(typing.Any, ...)


class RoomV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRoomV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRoomV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRoomV1Client
        """
        return self._raw_client

    def create_room_deprecated(
        self,
        app_id: AppId,
        *,
        region: Region,
        room_id: typing.Optional[RoomId] = None,
        room_config: typing.Optional[RoomConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RoomId:
        """
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
        RoomId


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.room_v1.create_room_deprecated(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            room_id="2swovpy1fnunu",
            region="Seattle",
        )
        """
        _response = self._raw_client.create_room_deprecated(
            app_id, region=region, room_id=room_id, room_config=room_config, request_options=request_options
        )
        return _response.data

    def get_room_info_deprecated(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Room:
        """
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
        client.room_v1.get_room_info_deprecated(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            room_id="2swovpy1fnunu",
        )
        """
        _response = self._raw_client.get_room_info_deprecated(app_id, room_id, request_options=request_options)
        return _response.data

    def get_active_rooms_for_process_deprecated(
        self, app_id: AppId, process_id: ProcessId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RoomWithoutAllocations]:
        """
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
        client.room_v1.get_active_rooms_for_process_deprecated(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
        )
        """
        _response = self._raw_client.get_active_rooms_for_process_deprecated(
            app_id, process_id, request_options=request_options
        )
        return _response.data

    def get_inactive_rooms_for_process_deprecated(
        self, app_id: AppId, process_id: ProcessId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RoomWithoutAllocations]:
        """
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
        client.room_v1.get_inactive_rooms_for_process_deprecated(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
        )
        """
        _response = self._raw_client.get_inactive_rooms_for_process_deprecated(
            app_id, process_id, request_options=request_options
        )
        return _response.data

    def destroy_room_deprecated(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
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
        client.room_v1.destroy_room_deprecated(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            room_id="2swovpy1fnunu",
        )
        """
        _response = self._raw_client.destroy_room_deprecated(app_id, room_id, request_options=request_options)
        return _response.data

    def suspend_room_deprecated(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
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
        client.room_v1.suspend_room_deprecated(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            room_id="2swovpy1fnunu",
        )
        """
        _response = self._raw_client.suspend_room_deprecated(app_id, room_id, request_options=request_options)
        return _response.data

    def get_connection_info_deprecated(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionInfo:
        """
        Parameters
        ----------
        app_id : AppId

        room_id : RoomId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionInfo
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.room_v1.get_connection_info_deprecated(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            room_id="2swovpy1fnunu",
        )
        """
        _response = self._raw_client.get_connection_info_deprecated(app_id, room_id, request_options=request_options)
        return _response.data


class AsyncRoomV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRoomV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRoomV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRoomV1Client
        """
        return self._raw_client

    async def create_room_deprecated(
        self,
        app_id: AppId,
        *,
        region: Region,
        room_id: typing.Optional[RoomId] = None,
        room_config: typing.Optional[RoomConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RoomId:
        """
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
        RoomId


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.room_v1.create_room_deprecated(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                room_id="2swovpy1fnunu",
                region="Seattle",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_room_deprecated(
            app_id, region=region, room_id=room_id, room_config=room_config, request_options=request_options
        )
        return _response.data

    async def get_room_info_deprecated(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Room:
        """
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
            await client.room_v1.get_room_info_deprecated(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                room_id="2swovpy1fnunu",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_room_info_deprecated(app_id, room_id, request_options=request_options)
        return _response.data

    async def get_active_rooms_for_process_deprecated(
        self, app_id: AppId, process_id: ProcessId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RoomWithoutAllocations]:
        """
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
            await client.room_v1.get_active_rooms_for_process_deprecated(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_active_rooms_for_process_deprecated(
            app_id, process_id, request_options=request_options
        )
        return _response.data

    async def get_inactive_rooms_for_process_deprecated(
        self, app_id: AppId, process_id: ProcessId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RoomWithoutAllocations]:
        """
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
            await client.room_v1.get_inactive_rooms_for_process_deprecated(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_inactive_rooms_for_process_deprecated(
            app_id, process_id, request_options=request_options
        )
        return _response.data

    async def destroy_room_deprecated(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
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
            await client.room_v1.destroy_room_deprecated(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                room_id="2swovpy1fnunu",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.destroy_room_deprecated(app_id, room_id, request_options=request_options)
        return _response.data

    async def suspend_room_deprecated(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
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
            await client.room_v1.suspend_room_deprecated(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                room_id="2swovpy1fnunu",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.suspend_room_deprecated(app_id, room_id, request_options=request_options)
        return _response.data

    async def get_connection_info_deprecated(
        self, app_id: AppId, room_id: RoomId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionInfo:
        """
        Parameters
        ----------
        app_id : AppId

        room_id : RoomId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionInfo
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.room_v1.get_connection_info_deprecated(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                room_id="2swovpy1fnunu",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_connection_info_deprecated(
            app_id, room_id, request_options=request_options
        )
        return _response.data
