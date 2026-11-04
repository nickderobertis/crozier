

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWorkerClient, RawWorkerClient
from .types.worker_all_response_item import WorkerAllResponseItem
from .types.worker_delete_response import WorkerDeleteResponse
from .types.worker_get_response import WorkerGetResponse
from .types.worker_get_revisions_response_item import WorkerGetRevisionsResponseItem
from .types.worker_toggle_active_response import WorkerToggleActiveResponse
from .types.worker_upsert_response import WorkerUpsertResponse


OMIT = typing.cast(typing.Any, ...)


class WorkerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWorkerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWorkerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWorkerClient
        """
        return self._raw_client

    def all_(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WorkerAllResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WorkerAllResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.worker.all_(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.all_(workspace_id, request_options=request_options)
        return _response.data

    def get(
        self, workspace_id: str, worker_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[WorkerGetResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        worker_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[WorkerGetResponse]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.worker.get(
            workspace_id="workspaceId",
            worker_id="workerId",
        )
        """
        _response = self._raw_client.get(workspace_id, worker_id, request_options=request_options)
        return _response.data

    def upsert(
        self,
        workspace_id: str,
        *,
        name: str,
        code: str,
        id: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        active: typing.Optional[bool] = OMIT,
        enable_cron: typing.Optional[bool] = OMIT,
        cron_expression: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkerUpsertResponse:
        """
        Parameters
        ----------
        workspace_id : str

        name : str

        code : str

        id : typing.Optional[str]

        description : typing.Optional[str]

        active : typing.Optional[bool]

        enable_cron : typing.Optional[bool]

        cron_expression : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkerUpsertResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.worker.upsert(
            workspace_id="workspaceId",
            name="name",
            code="code",
        )
        """
        _response = self._raw_client.upsert(
            workspace_id,
            name=name,
            code=code,
            id=id,
            description=description,
            active=active,
            enable_cron=enable_cron,
            cron_expression=cron_expression,
            request_options=request_options,
        )
        return _response.data

    def delete(
        self, workspace_id: str, worker_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkerDeleteResponse:
        """
        Parameters
        ----------
        workspace_id : str

        worker_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkerDeleteResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.worker.delete(
            workspace_id="workspaceId",
            worker_id="workerId",
        )
        """
        _response = self._raw_client.delete(workspace_id, worker_id, request_options=request_options)
        return _response.data

    def toggleactive(
        self,
        workspace_id: str,
        worker_id: str,
        *,
        active: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkerToggleActiveResponse:
        """
        Parameters
        ----------
        workspace_id : str

        worker_id : str

        active : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkerToggleActiveResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.worker.toggleactive(
            workspace_id="workspaceId",
            worker_id="workerId",
            active=True,
        )
        """
        _response = self._raw_client.toggleactive(
            workspace_id, worker_id, active=active, request_options=request_options
        )
        return _response.data

    def getrevisions(
        self, workspace_id: str, worker_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WorkerGetRevisionsResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        worker_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WorkerGetRevisionsResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.worker.getrevisions(
            workspace_id="workspaceId",
            worker_id="workerId",
        )
        """
        _response = self._raw_client.getrevisions(workspace_id, worker_id, request_options=request_options)
        return _response.data


class AsyncWorkerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWorkerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWorkerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWorkerClient
        """
        return self._raw_client

    async def all_(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WorkerAllResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WorkerAllResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.worker.all_(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(workspace_id, request_options=request_options)
        return _response.data

    async def get(
        self, workspace_id: str, worker_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[WorkerGetResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        worker_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[WorkerGetResponse]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.worker.get(
                workspace_id="workspaceId",
                worker_id="workerId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(workspace_id, worker_id, request_options=request_options)
        return _response.data

    async def upsert(
        self,
        workspace_id: str,
        *,
        name: str,
        code: str,
        id: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        active: typing.Optional[bool] = OMIT,
        enable_cron: typing.Optional[bool] = OMIT,
        cron_expression: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkerUpsertResponse:
        """
        Parameters
        ----------
        workspace_id : str

        name : str

        code : str

        id : typing.Optional[str]

        description : typing.Optional[str]

        active : typing.Optional[bool]

        enable_cron : typing.Optional[bool]

        cron_expression : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkerUpsertResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.worker.upsert(
                workspace_id="workspaceId",
                name="name",
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert(
            workspace_id,
            name=name,
            code=code,
            id=id,
            description=description,
            active=active,
            enable_cron=enable_cron,
            cron_expression=cron_expression,
            request_options=request_options,
        )
        return _response.data

    async def delete(
        self, workspace_id: str, worker_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkerDeleteResponse:
        """
        Parameters
        ----------
        workspace_id : str

        worker_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkerDeleteResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.worker.delete(
                workspace_id="workspaceId",
                worker_id="workerId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(workspace_id, worker_id, request_options=request_options)
        return _response.data

    async def toggleactive(
        self,
        workspace_id: str,
        worker_id: str,
        *,
        active: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkerToggleActiveResponse:
        """
        Parameters
        ----------
        workspace_id : str

        worker_id : str

        active : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkerToggleActiveResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.worker.toggleactive(
                workspace_id="workspaceId",
                worker_id="workerId",
                active=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.toggleactive(
            workspace_id, worker_id, active=active, request_options=request_options
        )
        return _response.data

    async def getrevisions(
        self, workspace_id: str, worker_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WorkerGetRevisionsResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        worker_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WorkerGetRevisionsResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.worker.getrevisions(
                workspace_id="workspaceId",
                worker_id="workerId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getrevisions(workspace_id, worker_id, request_options=request_options)
        return _response.data
