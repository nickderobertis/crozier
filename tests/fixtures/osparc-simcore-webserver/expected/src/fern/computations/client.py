

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.envelope_computation_get import EnvelopeComputationGet
from ..types.job_encryption_context_metadata import JobEncryptionContextMetadata
from ..types.page_computation_collection_run_rest_get import PageComputationCollectionRunRestGet
from ..types.page_computation_collection_run_task_rest_get import PageComputationCollectionRunTaskRestGet
from ..types.page_computation_run_rest_get import PageComputationRunRestGet
from ..types.page_computation_task_rest_get import PageComputationTaskRestGet
from .raw_client import AsyncRawComputationsClient, RawComputationsClient


OMIT = typing.cast(typing.Any, ...)


class ComputationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawComputationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawComputationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawComputationsClient
        """
        return self._raw_client

    def get_computation(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeComputationGet:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeComputationGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.computations.get_computation(
            project_id="project_id",
        )
        """
        _response = self._raw_client.get_computation(project_id, request_options=request_options)
        return _response.data

    def start_computation(
        self,
        project_id: str,
        *,
        force_restart: typing.Optional[bool] = OMIT,
        subgraph: typing.Optional[typing.Sequence[str]] = OMIT,
        encryption: typing.Optional[JobEncryptionContextMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeComputationGet:
        """
        Parameters
        ----------
        project_id : str

        force_restart : typing.Optional[bool]

        subgraph : typing.Optional[typing.Sequence[str]]

        encryption : typing.Optional[JobEncryptionContextMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeComputationGet
            Pipeline is up-to-date, nothing was started

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.computations.start_computation(
            project_id="project_id",
        )
        """
        _response = self._raw_client.start_computation(
            project_id,
            force_restart=force_restart,
            subgraph=subgraph,
            encryption=encryption,
            request_options=request_options,
        )
        return _response.data

    def stop_computation(self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.computations.stop_computation(
            project_id="project_id",
        )
        """
        _response = self._raw_client.stop_computation(project_id, request_options=request_options)
        return _response.data

    def list_computations_latest_iteration(
        self,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter_only_running: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageComputationRunRestGet:
        """
        Parameters
        ----------
        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        filter_only_running : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageComputationRunRestGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.computations.list_computations_latest_iteration()
        """
        _response = self._raw_client.list_computations_latest_iteration(
            order_by=order_by,
            limit=limit,
            offset=offset,
            filter_only_running=filter_only_running,
            request_options=request_options,
        )
        return _response.data

    def list_computation_iterations(
        self,
        project_id: str,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_children: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageComputationRunRestGet:
        """
        Parameters
        ----------
        project_id : str

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        include_children : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageComputationRunRestGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.computations.list_computation_iterations(
            project_id="project_id",
        )
        """
        _response = self._raw_client.list_computation_iterations(
            project_id,
            order_by=order_by,
            limit=limit,
            offset=offset,
            include_children=include_children,
            request_options=request_options,
        )
        return _response.data

    def list_computations_latest_iteration_tasks(
        self,
        project_id: str,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_children: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageComputationTaskRestGet:
        """
        Parameters
        ----------
        project_id : str

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        include_children : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageComputationTaskRestGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.computations.list_computations_latest_iteration_tasks(
            project_id="project_id",
        )
        """
        _response = self._raw_client.list_computations_latest_iteration_tasks(
            project_id,
            order_by=order_by,
            limit=limit,
            offset=offset,
            include_children=include_children,
            request_options=request_options,
        )
        return _response.data

    def list_computation_collection_runs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter_only_running: typing.Optional[bool] = None,
        filter_by_root_project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageComputationCollectionRunRestGet:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        filter_only_running : typing.Optional[bool]

        filter_by_root_project_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageComputationCollectionRunRestGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.computations.list_computation_collection_runs()
        """
        _response = self._raw_client.list_computation_collection_runs(
            limit=limit,
            offset=offset,
            filter_only_running=filter_only_running,
            filter_by_root_project_id=filter_by_root_project_id,
            request_options=request_options,
        )
        return _response.data

    def list_computation_collection_run_tasks(
        self,
        collection_run_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageComputationCollectionRunTaskRestGet:
        """
        Parameters
        ----------
        collection_run_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageComputationCollectionRunTaskRestGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.computations.list_computation_collection_run_tasks(
            collection_run_id="collection_run_id",
        )
        """
        _response = self._raw_client.list_computation_collection_run_tasks(
            collection_run_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data


class AsyncComputationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawComputationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawComputationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawComputationsClient
        """
        return self._raw_client

    async def get_computation(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeComputationGet:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeComputationGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.computations.get_computation(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_computation(project_id, request_options=request_options)
        return _response.data

    async def start_computation(
        self,
        project_id: str,
        *,
        force_restart: typing.Optional[bool] = OMIT,
        subgraph: typing.Optional[typing.Sequence[str]] = OMIT,
        encryption: typing.Optional[JobEncryptionContextMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeComputationGet:
        """
        Parameters
        ----------
        project_id : str

        force_restart : typing.Optional[bool]

        subgraph : typing.Optional[typing.Sequence[str]]

        encryption : typing.Optional[JobEncryptionContextMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeComputationGet
            Pipeline is up-to-date, nothing was started

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.computations.start_computation(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_computation(
            project_id,
            force_restart=force_restart,
            subgraph=subgraph,
            encryption=encryption,
            request_options=request_options,
        )
        return _response.data

    async def stop_computation(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.computations.stop_computation(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_computation(project_id, request_options=request_options)
        return _response.data

    async def list_computations_latest_iteration(
        self,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter_only_running: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageComputationRunRestGet:
        """
        Parameters
        ----------
        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        filter_only_running : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageComputationRunRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.computations.list_computations_latest_iteration()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_computations_latest_iteration(
            order_by=order_by,
            limit=limit,
            offset=offset,
            filter_only_running=filter_only_running,
            request_options=request_options,
        )
        return _response.data

    async def list_computation_iterations(
        self,
        project_id: str,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_children: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageComputationRunRestGet:
        """
        Parameters
        ----------
        project_id : str

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        include_children : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageComputationRunRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.computations.list_computation_iterations(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_computation_iterations(
            project_id,
            order_by=order_by,
            limit=limit,
            offset=offset,
            include_children=include_children,
            request_options=request_options,
        )
        return _response.data

    async def list_computations_latest_iteration_tasks(
        self,
        project_id: str,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_children: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageComputationTaskRestGet:
        """
        Parameters
        ----------
        project_id : str

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        include_children : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageComputationTaskRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.computations.list_computations_latest_iteration_tasks(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_computations_latest_iteration_tasks(
            project_id,
            order_by=order_by,
            limit=limit,
            offset=offset,
            include_children=include_children,
            request_options=request_options,
        )
        return _response.data

    async def list_computation_collection_runs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter_only_running: typing.Optional[bool] = None,
        filter_by_root_project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageComputationCollectionRunRestGet:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        filter_only_running : typing.Optional[bool]

        filter_by_root_project_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageComputationCollectionRunRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.computations.list_computation_collection_runs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_computation_collection_runs(
            limit=limit,
            offset=offset,
            filter_only_running=filter_only_running,
            filter_by_root_project_id=filter_by_root_project_id,
            request_options=request_options,
        )
        return _response.data

    async def list_computation_collection_run_tasks(
        self,
        collection_run_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageComputationCollectionRunTaskRestGet:
        """
        Parameters
        ----------
        collection_run_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageComputationCollectionRunTaskRestGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.computations.list_computation_collection_run_tasks(
                collection_run_id="collection_run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_computation_collection_run_tasks(
            collection_run_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data
