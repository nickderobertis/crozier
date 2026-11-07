

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_id import AppId
from ..types.process_id import ProcessId
from ..types.process_status import ProcessStatus
from ..types.process_v2 import ProcessV2
from ..types.region import Region
from .raw_client import AsyncRawProcessesV2Client, RawProcessesV2Client


class ProcessesV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProcessesV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProcessesV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProcessesV2Client
        """
        return self._raw_client

    def get_process_info(
        self, app_id: AppId, process_id: ProcessId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProcessV2:
        """
        Get details for a [process](https://hathora.dev/docs/concepts/hathora-entities#process).

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessV2
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.processes_v2.get_process_info(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
        )
        """
        _response = self._raw_client.get_process_info(app_id, process_id, request_options=request_options)
        return _response.data

    def get_latest_processes(
        self,
        app_id: AppId,
        *,
        status: typing.Optional[typing.Union[ProcessStatus, typing.Sequence[ProcessStatus]]] = None,
        region: typing.Optional[typing.Union[Region, typing.Sequence[Region]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ProcessV2]:
        """
        Retrieve the 10 most recent [processes](https://hathora.dev/docs/concepts/hathora-entities#process) objects for an [application](https://hathora.dev/docs/concepts/hathora-entities#application). Filter the array by optionally passing in a `status` or `region`.

        Parameters
        ----------
        app_id : AppId

        status : typing.Optional[typing.Union[ProcessStatus, typing.Sequence[ProcessStatus]]]

        region : typing.Optional[typing.Union[Region, typing.Sequence[Region]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProcessV2]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.processes_v2.get_latest_processes(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
        )
        """
        _response = self._raw_client.get_latest_processes(
            app_id, status=status, region=region, request_options=request_options
        )
        return _response.data

    def stop_process(
        self, app_id: AppId, process_id: ProcessId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Stops a [process](https://hathora.dev/docs/concepts/hathora-entities#process) immediately.

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

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
        client.processes_v2.stop_process(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
        )
        """
        _response = self._raw_client.stop_process(app_id, process_id, request_options=request_options)
        return _response.data

    def create_process(
        self, app_id: AppId, region: Region, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProcessV2:
        """
        Creates a [process](https://hathora.dev/docs/concepts/hathora-entities#process) without a room. Use this to pre-allocate processes ahead of time so that subsequent room assignment via [CreateRoom()](https://hathora.dev/api#tag/RoomV2/operation/CreateRoom) can be instant.

        Parameters
        ----------
        app_id : AppId

        region : Region

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessV2


        Examples
        --------
        from fern import FernApi, Region

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.processes_v2.create_process(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            region=Region.SEATTLE,
        )
        """
        _response = self._raw_client.create_process(app_id, region, request_options=request_options)
        return _response.data


class AsyncProcessesV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProcessesV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProcessesV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProcessesV2Client
        """
        return self._raw_client

    async def get_process_info(
        self, app_id: AppId, process_id: ProcessId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProcessV2:
        """
        Get details for a [process](https://hathora.dev/docs/concepts/hathora-entities#process).

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessV2
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.processes_v2.get_process_info(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_process_info(app_id, process_id, request_options=request_options)
        return _response.data

    async def get_latest_processes(
        self,
        app_id: AppId,
        *,
        status: typing.Optional[typing.Union[ProcessStatus, typing.Sequence[ProcessStatus]]] = None,
        region: typing.Optional[typing.Union[Region, typing.Sequence[Region]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ProcessV2]:
        """
        Retrieve the 10 most recent [processes](https://hathora.dev/docs/concepts/hathora-entities#process) objects for an [application](https://hathora.dev/docs/concepts/hathora-entities#application). Filter the array by optionally passing in a `status` or `region`.

        Parameters
        ----------
        app_id : AppId

        status : typing.Optional[typing.Union[ProcessStatus, typing.Sequence[ProcessStatus]]]

        region : typing.Optional[typing.Union[Region, typing.Sequence[Region]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProcessV2]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.processes_v2.get_latest_processes(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_latest_processes(
            app_id, status=status, region=region, request_options=request_options
        )
        return _response.data

    async def stop_process(
        self, app_id: AppId, process_id: ProcessId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Stops a [process](https://hathora.dev/docs/concepts/hathora-entities#process) immediately.

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

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
            await client.processes_v2.stop_process(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_process(app_id, process_id, request_options=request_options)
        return _response.data

    async def create_process(
        self, app_id: AppId, region: Region, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProcessV2:
        """
        Creates a [process](https://hathora.dev/docs/concepts/hathora-entities#process) without a room. Use this to pre-allocate processes ahead of time so that subsequent room assignment via [CreateRoom()](https://hathora.dev/api#tag/RoomV2/operation/CreateRoom) can be instant.

        Parameters
        ----------
        app_id : AppId

        region : Region

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessV2


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Region

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.processes_v2.create_process(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                region=Region.SEATTLE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_process(app_id, region, request_options=request_options)
        return _response.data
