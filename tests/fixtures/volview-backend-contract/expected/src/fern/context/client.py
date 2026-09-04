

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.job_history_page import JobHistoryPage
from ..types.job_ref import JobRef
from ..types.stage_input_descriptor import StageInputDescriptor
from ..types.stage_response import StageResponse
from ..types.task_spec import TaskSpec
from ..types.task_summary import TaskSummary
from .raw_client import AsyncRawContextClient, RawContextClient
from .types.run_task_request_values_value import RunTaskRequestValuesValue


OMIT = typing.cast(typing.Any, ...)


class ContextClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContextClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContextClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContextClient
        """
        return self._raw_client

    def list_tasks(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[TaskSummary]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TaskSummary]
            The available tasks as advisory summaries.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.context.list_tasks()
        """
        _response = self._raw_client.list_tasks(request_options=request_options)
        return _response.data

    def get_task_spec(self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> TaskSpec:
        """
        Parameters
        ----------
        task_id : str
            Opaque task identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskSpec
            The task's neutral task spec.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.context.get_task_spec(
            task_id="taskId",
        )
        """
        _response = self._raw_client.get_task_spec(task_id, request_options=request_options)
        return _response.data

    def run_task(
        self,
        task_id: str,
        *,
        values: typing.Dict[str, typing.Optional[RunTaskRequestValuesValue]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobRef:
        """
        Parameters
        ----------
        task_id : str
            Opaque task identifier.

        values : typing.Dict[str, typing.Optional[RunTaskRequestValuesValue]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobRef
            The submitted job handle.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.context.run_task(
            task_id="taskId",
            values={},
        )
        """
        _response = self._raw_client.run_task(task_id, values=values, request_options=request_options)
        return _response.data

    def list_job_history(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobHistoryPage:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        cursor : typing.Optional[str]
            Opaque continuation cursor returned by the prior page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobHistoryPage
            One bounded lightweight page; logs and parameters are absent.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.context.list_job_history()
        """
        _response = self._raw_client.list_job_history(limit=limit, cursor=cursor, request_options=request_options)
        return _response.data

    def stage_input(
        self,
        *,
        file: core.File,
        descriptor: StageInputDescriptor,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StageResponse:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        descriptor : StageInputDescriptor

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StageResponse
            The backend-minted URIs for the staged bytes.

        Examples
        --------
        from fern import (
            FernApi,
            StageInputDescriptor_Labelmap,
            StageInputDescriptorLabelmapReferenceImage,
            StageInputDescriptorLabelmapReferenceImageType,
        )

        client = FernApi()
        client.context.stage_input(
            descriptor=StageInputDescriptor_Labelmap(
                name="name",
                reference_image=StageInputDescriptorLabelmapReferenceImage(
                    type=StageInputDescriptorLabelmapReferenceImageType.IMAGE,
                    uris=["uris"],
                ),
            ),
        )
        """
        _response = self._raw_client.stage_input(file=file, descriptor=descriptor, request_options=request_options)
        return _response.data


class AsyncContextClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContextClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContextClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContextClient
        """
        return self._raw_client

    async def list_tasks(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[TaskSummary]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TaskSummary]
            The available tasks as advisory summaries.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.context.list_tasks()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tasks(request_options=request_options)
        return _response.data

    async def get_task_spec(self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> TaskSpec:
        """
        Parameters
        ----------
        task_id : str
            Opaque task identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskSpec
            The task's neutral task spec.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.context.get_task_spec(
                task_id="taskId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_task_spec(task_id, request_options=request_options)
        return _response.data

    async def run_task(
        self,
        task_id: str,
        *,
        values: typing.Dict[str, typing.Optional[RunTaskRequestValuesValue]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobRef:
        """
        Parameters
        ----------
        task_id : str
            Opaque task identifier.

        values : typing.Dict[str, typing.Optional[RunTaskRequestValuesValue]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobRef
            The submitted job handle.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.context.run_task(
                task_id="taskId",
                values={},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_task(task_id, values=values, request_options=request_options)
        return _response.data

    async def list_job_history(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobHistoryPage:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        cursor : typing.Optional[str]
            Opaque continuation cursor returned by the prior page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobHistoryPage
            One bounded lightweight page; logs and parameters are absent.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.context.list_job_history()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_job_history(limit=limit, cursor=cursor, request_options=request_options)
        return _response.data

    async def stage_input(
        self,
        *,
        file: core.File,
        descriptor: StageInputDescriptor,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StageResponse:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        descriptor : StageInputDescriptor

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StageResponse
            The backend-minted URIs for the staged bytes.

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            StageInputDescriptor_Labelmap,
            StageInputDescriptorLabelmapReferenceImage,
            StageInputDescriptorLabelmapReferenceImageType,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.context.stage_input(
                descriptor=StageInputDescriptor_Labelmap(
                    name="name",
                    reference_image=StageInputDescriptorLabelmapReferenceImage(
                        type=StageInputDescriptorLabelmapReferenceImageType.IMAGE,
                        uris=["uris"],
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stage_input(
            file=file, descriptor=descriptor, request_options=request_options
        )
        return _response.data
