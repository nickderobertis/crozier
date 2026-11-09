

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_id import AppId
from ..types.process import Process
from ..types.process_id import ProcessId
from ..types.process_with_rooms import ProcessWithRooms
from ..types.region import Region
from .raw_client import AsyncRawProcessesV1Client, RawProcessesV1Client


class ProcessesV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProcessesV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProcessesV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProcessesV1Client
        """
        return self._raw_client

    def get_running_processes(
        self,
        app_id: AppId,
        *,
        region: typing.Optional[Region] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ProcessWithRooms]:
        """
        Retrieve 10 most recently started [process](https://hathora.dev/docs/concepts/hathora-entities#process) objects for an [application](https://hathora.dev/docs/concepts/hathora-entities#application). Filter the array by optionally passing in a `region`.

        Parameters
        ----------
        app_id : AppId

        region : typing.Optional[Region]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProcessWithRooms]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.processes_v1.get_running_processes(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
        )
        """
        _response = self._raw_client.get_running_processes(app_id, region=region, request_options=request_options)
        return _response.data

    def get_stopped_processes(
        self,
        app_id: AppId,
        *,
        region: typing.Optional[Region] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Process]:
        """
        Retrieve 10 most recently stopped [process](https://hathora.dev/docs/concepts/hathora-entities#process) objects for an [application](https://hathora.dev/docs/concepts/hathora-entities#application). Filter the array by optionally passing in a `region`.

        Parameters
        ----------
        app_id : AppId

        region : typing.Optional[Region]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Process]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.processes_v1.get_stopped_processes(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
        )
        """
        _response = self._raw_client.get_stopped_processes(app_id, region=region, request_options=request_options)
        return _response.data

    def get_process_info_deprecated(
        self, app_id: AppId, process_id: ProcessId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Process:
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
        Process
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.processes_v1.get_process_info_deprecated(
            app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
        )
        """
        _response = self._raw_client.get_process_info_deprecated(app_id, process_id, request_options=request_options)
        return _response.data


class AsyncProcessesV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProcessesV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProcessesV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProcessesV1Client
        """
        return self._raw_client

    async def get_running_processes(
        self,
        app_id: AppId,
        *,
        region: typing.Optional[Region] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ProcessWithRooms]:
        """
        Retrieve 10 most recently started [process](https://hathora.dev/docs/concepts/hathora-entities#process) objects for an [application](https://hathora.dev/docs/concepts/hathora-entities#application). Filter the array by optionally passing in a `region`.

        Parameters
        ----------
        app_id : AppId

        region : typing.Optional[Region]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProcessWithRooms]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.processes_v1.get_running_processes(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_running_processes(app_id, region=region, request_options=request_options)
        return _response.data

    async def get_stopped_processes(
        self,
        app_id: AppId,
        *,
        region: typing.Optional[Region] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Process]:
        """
        Retrieve 10 most recently stopped [process](https://hathora.dev/docs/concepts/hathora-entities#process) objects for an [application](https://hathora.dev/docs/concepts/hathora-entities#application). Filter the array by optionally passing in a `region`.

        Parameters
        ----------
        app_id : AppId

        region : typing.Optional[Region]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Process]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.processes_v1.get_stopped_processes(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_stopped_processes(app_id, region=region, request_options=request_options)
        return _response.data

    async def get_process_info_deprecated(
        self, app_id: AppId, process_id: ProcessId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Process:
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
        Process
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.processes_v1.get_process_info_deprecated(
                app_id="app-af469a92-5b45-4565-b3c4-b79878de67d2",
                process_id="cbfcddd2-0006-43ae-996c-995fff7bed2e",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_process_info_deprecated(
            app_id, process_id, request_options=request_options
        )
        return _response.data
