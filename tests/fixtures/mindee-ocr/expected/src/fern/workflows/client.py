

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWorkflowsClient, RawWorkflowsClient


OMIT = typing.cast(typing.Any, ...)


class WorkflowsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWorkflowsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWorkflowsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWorkflowsClient
        """
        return self._raw_client

    def execute_workflow(
        self,
        workflow_id: str,
        *,
        document: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Execute workflow

        Parameters
        ----------
        workflow_id : str

        document : typing.Optional[core.File]
            See core.File for more documentation

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
        client.workflows.execute_workflow(
            workflow_id="workflow_id",
        )
        """
        _response = self._raw_client.execute_workflow(workflow_id, document=document, request_options=request_options)
        return _response.data

    def workflow_predict_async(
        self,
        workflow_id: str,
        *,
        document: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Async workflow prediction

        Parameters
        ----------
        workflow_id : str

        document : typing.Optional[core.File]
            See core.File for more documentation

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
        client.workflows.workflow_predict_async(
            workflow_id="workflow_id",
        )
        """
        _response = self._raw_client.workflow_predict_async(
            workflow_id, document=document, request_options=request_options
        )
        return _response.data


class AsyncWorkflowsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWorkflowsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWorkflowsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWorkflowsClient
        """
        return self._raw_client

    async def execute_workflow(
        self,
        workflow_id: str,
        *,
        document: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Execute workflow

        Parameters
        ----------
        workflow_id : str

        document : typing.Optional[core.File]
            See core.File for more documentation

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
            await client.workflows.execute_workflow(
                workflow_id="workflow_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_workflow(
            workflow_id, document=document, request_options=request_options
        )
        return _response.data

    async def workflow_predict_async(
        self,
        workflow_id: str,
        *,
        document: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Async workflow prediction

        Parameters
        ----------
        workflow_id : str

        document : typing.Optional[core.File]
            See core.File for more documentation

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
            await client.workflows.workflow_predict_async(
                workflow_id="workflow_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.workflow_predict_async(
            workflow_id, document=document, request_options=request_options
        )
        return _response.data
