

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.computation_get import ComputationGet
from ..types.job_encryption_context_metadata import JobEncryptionContextMetadata
from ..types.task_log_file_get import TaskLogFileGet
from ..types.tasks_outputs import TasksOutputs
from ..types.user_id_int import UserIdInt
from ..types.wallet_info_input import WalletInfoInput
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

    def create_or_update_or_start_computation(
        self,
        *,
        user_id: UserIdInt,
        project_id: str,
        product_name: str,
        product_api_base_url: str,
        start_pipeline: typing.Optional[bool] = OMIT,
        subgraph: typing.Optional[typing.Sequence[str]] = OMIT,
        force_restart: typing.Optional[bool] = OMIT,
        simcore_user_agent: typing.Optional[str] = OMIT,
        use_on_demand_clusters: typing.Optional[bool] = OMIT,
        wallet_info: typing.Optional[WalletInfoInput] = OMIT,
        collection_run_id: typing.Optional[str] = OMIT,
        encryption: typing.Optional[JobEncryptionContextMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ComputationGet:
        """
        Create and optionally start a new computation

        Parameters
        ----------
        user_id : UserIdInt

        project_id : str

        product_name : str

        product_api_base_url : str
            Base url of the product

        start_pipeline : typing.Optional[bool]
            if True the computation pipeline will start right away

        subgraph : typing.Optional[typing.Sequence[str]]
            An optional set of nodes that must be executed, if empty the whole pipeline is executed

        force_restart : typing.Optional[bool]
            if True will force re-running all dependent nodes

        simcore_user_agent : typing.Optional[str]

        use_on_demand_clusters : typing.Optional[bool]
            if True, a cluster will be created as necessary (wallet_id cannot be None)

        wallet_info : typing.Optional[WalletInfoInput]
            contains information about the wallet used to bill the running service

        collection_run_id : typing.Optional[str]
            In case start_pipeline is True, this is the collection run id to which the comp run belongs.

        encryption : typing.Optional[JobEncryptionContextMetadata]
            Optional job encryption context to decrypt input files and encrypt output files

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComputationGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.computations.create_or_update_or_start_computation(
            user_id=1,
            project_id="project_id",
            product_name="product_name",
            product_api_base_url="product_api_base_url",
        )
        """
        _response = self._raw_client.create_or_update_or_start_computation(
            user_id=user_id,
            project_id=project_id,
            product_name=product_name,
            product_api_base_url=product_api_base_url,
            start_pipeline=start_pipeline,
            subgraph=subgraph,
            force_restart=force_restart,
            simcore_user_agent=simcore_user_agent,
            use_on_demand_clusters=use_on_demand_clusters,
            wallet_info=wallet_info,
            collection_run_id=collection_run_id,
            encryption=encryption,
            request_options=request_options,
        )
        return _response.data

    def get_computation(
        self, project_id: str, *, user_id: UserIdInt, request_options: typing.Optional[RequestOptions] = None
    ) -> ComputationGet:
        """
        Returns a computation pipeline state

        Parameters
        ----------
        project_id : str

        user_id : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComputationGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.computations.get_computation(
            project_id="project_id",
            user_id=1,
        )
        """
        _response = self._raw_client.get_computation(project_id, user_id=user_id, request_options=request_options)
        return _response.data

    def delete_computation(
        self,
        project_id: str,
        *,
        user_id: UserIdInt,
        force: typing.Optional[bool] = OMIT,
        wait_for: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a computation pipeline

        Parameters
        ----------
        project_id : str

        user_id : UserIdInt

        force : typing.Optional[bool]
            if True then the pipeline will be removed even if it is running

        wait_for : typing.Optional[str]
            timeout when waiting for pipeline to stop

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.computations.delete_computation(
            project_id="project_id",
            user_id=1,
        )
        """
        _response = self._raw_client.delete_computation(
            project_id, user_id=user_id, force=force, wait_for=wait_for, request_options=request_options
        )
        return _response.data

    def stop_computation(
        self, project_id: str, *, user_id: UserIdInt, request_options: typing.Optional[RequestOptions] = None
    ) -> ComputationGet:
        """
        Stops a computation pipeline

        Parameters
        ----------
        project_id : str

        user_id : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComputationGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.computations.stop_computation(
            project_id="project_id",
            user_id=1,
        )
        """
        _response = self._raw_client.stop_computation(project_id, user_id=user_id, request_options=request_options)
        return _response.data

    def get_all_tasks_log_files_v2computations_project_id_tasks_logfile_get(
        self, project_id: str, *, user_id: UserIdInt, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TaskLogFileGet]:
        """
        Returns download links to log-files of each task in a computation.
        Each log is only available when the corresponding task is done

        Parameters
        ----------
        project_id : str

        user_id : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TaskLogFileGet]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.computations.get_all_tasks_log_files_v2computations_project_id_tasks_logfile_get(
            project_id="project_id",
            user_id=1,
        )
        """
        _response = self._raw_client.get_all_tasks_log_files_v2computations_project_id_tasks_logfile_get(
            project_id, user_id=user_id, request_options=request_options
        )
        return _response.data

    def get_task_log_file(
        self,
        project_id: str,
        node_uuid: str,
        *,
        user_id: UserIdInt,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskLogFileGet:
        """
        Returns a link to download logs file of a give task.
        The log is only available when the task is done

        Parameters
        ----------
        project_id : str

        node_uuid : str

        user_id : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskLogFileGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.computations.get_task_log_file(
            project_id="project_id",
            node_uuid="node_uuid",
            user_id=1,
        )
        """
        _response = self._raw_client.get_task_log_file(
            project_id, node_uuid, user_id=user_id, request_options=request_options
        )
        return _response.data

    def get_batch_tasks_outputs_v2computations_project_id_tasks_outputs_batch_get_post(
        self,
        project_id: str,
        *,
        nodes_ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TasksOutputs:
        """
        Parameters
        ----------
        project_id : str

        nodes_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TasksOutputs
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.computations.get_batch_tasks_outputs_v2computations_project_id_tasks_outputs_batch_get_post(
            project_id="project_id",
            nodes_ids=["nodes_ids"],
        )
        """
        _response = self._raw_client.get_batch_tasks_outputs_v2computations_project_id_tasks_outputs_batch_get_post(
            project_id, nodes_ids=nodes_ids, request_options=request_options
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

    async def create_or_update_or_start_computation(
        self,
        *,
        user_id: UserIdInt,
        project_id: str,
        product_name: str,
        product_api_base_url: str,
        start_pipeline: typing.Optional[bool] = OMIT,
        subgraph: typing.Optional[typing.Sequence[str]] = OMIT,
        force_restart: typing.Optional[bool] = OMIT,
        simcore_user_agent: typing.Optional[str] = OMIT,
        use_on_demand_clusters: typing.Optional[bool] = OMIT,
        wallet_info: typing.Optional[WalletInfoInput] = OMIT,
        collection_run_id: typing.Optional[str] = OMIT,
        encryption: typing.Optional[JobEncryptionContextMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ComputationGet:
        """
        Create and optionally start a new computation

        Parameters
        ----------
        user_id : UserIdInt

        project_id : str

        product_name : str

        product_api_base_url : str
            Base url of the product

        start_pipeline : typing.Optional[bool]
            if True the computation pipeline will start right away

        subgraph : typing.Optional[typing.Sequence[str]]
            An optional set of nodes that must be executed, if empty the whole pipeline is executed

        force_restart : typing.Optional[bool]
            if True will force re-running all dependent nodes

        simcore_user_agent : typing.Optional[str]

        use_on_demand_clusters : typing.Optional[bool]
            if True, a cluster will be created as necessary (wallet_id cannot be None)

        wallet_info : typing.Optional[WalletInfoInput]
            contains information about the wallet used to bill the running service

        collection_run_id : typing.Optional[str]
            In case start_pipeline is True, this is the collection run id to which the comp run belongs.

        encryption : typing.Optional[JobEncryptionContextMetadata]
            Optional job encryption context to decrypt input files and encrypt output files

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComputationGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.computations.create_or_update_or_start_computation(
                user_id=1,
                project_id="project_id",
                product_name="product_name",
                product_api_base_url="product_api_base_url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_or_update_or_start_computation(
            user_id=user_id,
            project_id=project_id,
            product_name=product_name,
            product_api_base_url=product_api_base_url,
            start_pipeline=start_pipeline,
            subgraph=subgraph,
            force_restart=force_restart,
            simcore_user_agent=simcore_user_agent,
            use_on_demand_clusters=use_on_demand_clusters,
            wallet_info=wallet_info,
            collection_run_id=collection_run_id,
            encryption=encryption,
            request_options=request_options,
        )
        return _response.data

    async def get_computation(
        self, project_id: str, *, user_id: UserIdInt, request_options: typing.Optional[RequestOptions] = None
    ) -> ComputationGet:
        """
        Returns a computation pipeline state

        Parameters
        ----------
        project_id : str

        user_id : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComputationGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.computations.get_computation(
                project_id="project_id",
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_computation(project_id, user_id=user_id, request_options=request_options)
        return _response.data

    async def delete_computation(
        self,
        project_id: str,
        *,
        user_id: UserIdInt,
        force: typing.Optional[bool] = OMIT,
        wait_for: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a computation pipeline

        Parameters
        ----------
        project_id : str

        user_id : UserIdInt

        force : typing.Optional[bool]
            if True then the pipeline will be removed even if it is running

        wait_for : typing.Optional[str]
            timeout when waiting for pipeline to stop

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
            await client.computations.delete_computation(
                project_id="project_id",
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_computation(
            project_id, user_id=user_id, force=force, wait_for=wait_for, request_options=request_options
        )
        return _response.data

    async def stop_computation(
        self, project_id: str, *, user_id: UserIdInt, request_options: typing.Optional[RequestOptions] = None
    ) -> ComputationGet:
        """
        Stops a computation pipeline

        Parameters
        ----------
        project_id : str

        user_id : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComputationGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.computations.stop_computation(
                project_id="project_id",
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_computation(
            project_id, user_id=user_id, request_options=request_options
        )
        return _response.data

    async def get_all_tasks_log_files_v2computations_project_id_tasks_logfile_get(
        self, project_id: str, *, user_id: UserIdInt, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TaskLogFileGet]:
        """
        Returns download links to log-files of each task in a computation.
        Each log is only available when the corresponding task is done

        Parameters
        ----------
        project_id : str

        user_id : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TaskLogFileGet]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.computations.get_all_tasks_log_files_v2computations_project_id_tasks_logfile_get(
                project_id="project_id",
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_tasks_log_files_v2computations_project_id_tasks_logfile_get(
            project_id, user_id=user_id, request_options=request_options
        )
        return _response.data

    async def get_task_log_file(
        self,
        project_id: str,
        node_uuid: str,
        *,
        user_id: UserIdInt,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskLogFileGet:
        """
        Returns a link to download logs file of a give task.
        The log is only available when the task is done

        Parameters
        ----------
        project_id : str

        node_uuid : str

        user_id : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskLogFileGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.computations.get_task_log_file(
                project_id="project_id",
                node_uuid="node_uuid",
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_task_log_file(
            project_id, node_uuid, user_id=user_id, request_options=request_options
        )
        return _response.data

    async def get_batch_tasks_outputs_v2computations_project_id_tasks_outputs_batch_get_post(
        self,
        project_id: str,
        *,
        nodes_ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TasksOutputs:
        """
        Parameters
        ----------
        project_id : str

        nodes_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TasksOutputs
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.computations.get_batch_tasks_outputs_v2computations_project_id_tasks_outputs_batch_get_post(
                project_id="project_id",
                nodes_ids=["nodes_ids"],
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.get_batch_tasks_outputs_v2computations_project_id_tasks_outputs_batch_get_post(
                project_id, nodes_ids=nodes_ids, request_options=request_options
            )
        )
        return _response.data
