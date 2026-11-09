

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_id import AppId
from ..types.deployment_id import DeploymentId
from ..types.logs_follow import LogsFollow
from ..types.process_id import ProcessId
from ..types.region import Region
from ..types.tail_lines import TailLines
from .raw_client import AsyncRawLogV1Client, RawLogV1Client


class LogV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLogV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLogV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLogV1Client
        """
        return self._raw_client

    def get_logs_for_app(
        self,
        app_id: AppId,
        *,
        follow: typing.Optional[LogsFollow] = None,
        tail_lines: typing.Optional[TailLines] = None,
        region: typing.Optional[Region] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Returns a stream of logs for an [application](https://hathora.dev/docs/concepts/hathora-entities#application) using `appId`.

        Parameters
        ----------
        app_id : AppId

        follow : typing.Optional[LogsFollow]

        tail_lines : typing.Optional[TailLines]

        region : typing.Optional[Region]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.log_v1.get_logs_for_app(
            app_id="appId",
        )
        """
        with self._raw_client.get_logs_for_app(
            app_id, follow=follow, tail_lines=tail_lines, region=region, request_options=request_options
        ) as r:
            yield from r.data

    def get_logs_for_process(
        self,
        app_id: AppId,
        process_id: ProcessId,
        *,
        follow: typing.Optional[LogsFollow] = None,
        tail_lines: typing.Optional[TailLines] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Returns a stream of logs for a [process](https://hathora.dev/docs/concepts/hathora-entities#process) using `appId` and `processId`.

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

        follow : typing.Optional[LogsFollow]

        tail_lines : typing.Optional[TailLines]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.log_v1.get_logs_for_process(
            app_id="appId",
            process_id="processId",
        )
        """
        with self._raw_client.get_logs_for_process(
            app_id, process_id, follow=follow, tail_lines=tail_lines, request_options=request_options
        ) as r:
            yield from r.data

    def download_log_for_process(
        self, app_id: AppId, process_id: ProcessId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Download entire log file for a stopped process.

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.log_v1.download_log_for_process(
            app_id="appId",
            process_id="processId",
        )
        """
        with self._raw_client.download_log_for_process(app_id, process_id, request_options=request_options) as r:
            yield from r.data

    def get_logs_for_deployment(
        self,
        app_id: AppId,
        deployment_id: DeploymentId,
        *,
        follow: typing.Optional[LogsFollow] = None,
        tail_lines: typing.Optional[TailLines] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Returns a stream of logs for a [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment) using `appId` and `deploymentId`.

        Parameters
        ----------
        app_id : AppId

        deployment_id : DeploymentId

        follow : typing.Optional[LogsFollow]

        tail_lines : typing.Optional[TailLines]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.log_v1.get_logs_for_deployment(
            app_id="appId",
            deployment_id=1,
        )
        """
        with self._raw_client.get_logs_for_deployment(
            app_id, deployment_id, follow=follow, tail_lines=tail_lines, request_options=request_options
        ) as r:
            yield from r.data


class AsyncLogV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLogV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLogV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLogV1Client
        """
        return self._raw_client

    async def get_logs_for_app(
        self,
        app_id: AppId,
        *,
        follow: typing.Optional[LogsFollow] = None,
        tail_lines: typing.Optional[TailLines] = None,
        region: typing.Optional[Region] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Returns a stream of logs for an [application](https://hathora.dev/docs/concepts/hathora-entities#application) using `appId`.

        Parameters
        ----------
        app_id : AppId

        follow : typing.Optional[LogsFollow]

        tail_lines : typing.Optional[TailLines]

        region : typing.Optional[Region]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.log_v1.get_logs_for_app(
                app_id="appId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_logs_for_app(
            app_id, follow=follow, tail_lines=tail_lines, region=region, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_logs_for_process(
        self,
        app_id: AppId,
        process_id: ProcessId,
        *,
        follow: typing.Optional[LogsFollow] = None,
        tail_lines: typing.Optional[TailLines] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Returns a stream of logs for a [process](https://hathora.dev/docs/concepts/hathora-entities#process) using `appId` and `processId`.

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

        follow : typing.Optional[LogsFollow]

        tail_lines : typing.Optional[TailLines]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.log_v1.get_logs_for_process(
                app_id="appId",
                process_id="processId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_logs_for_process(
            app_id, process_id, follow=follow, tail_lines=tail_lines, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def download_log_for_process(
        self, app_id: AppId, process_id: ProcessId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Download entire log file for a stopped process.

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.log_v1.download_log_for_process(
                app_id="appId",
                process_id="processId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.download_log_for_process(app_id, process_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_logs_for_deployment(
        self,
        app_id: AppId,
        deployment_id: DeploymentId,
        *,
        follow: typing.Optional[LogsFollow] = None,
        tail_lines: typing.Optional[TailLines] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Returns a stream of logs for a [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment) using `appId` and `deploymentId`.

        Parameters
        ----------
        app_id : AppId

        deployment_id : DeploymentId

        follow : typing.Optional[LogsFollow]

        tail_lines : typing.Optional[TailLines]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.log_v1.get_logs_for_deployment(
                app_id="appId",
                deployment_id=1,
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_logs_for_deployment(
            app_id, deployment_id, follow=follow, tail_lines=tail_lines, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk
