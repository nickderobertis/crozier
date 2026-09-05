

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1alpha1resource_metadata import V1Alpha1ResourceMetadata
from ..types.v1alpha1workflow_resource_create_response import V1Alpha1WorkflowResourceCreateResponse
from ..types.v1alpha1workflow_resource_read_response import V1Alpha1WorkflowResourceReadResponse
from ..types.v1alpha1workflow_resource_spec import V1Alpha1WorkflowResourceSpec
from ..types.v1alpha1workflow_resource_update_response import V1Alpha1WorkflowResourceUpdateResponse
from ..types.v1alpha1workflow_run_read_response import V1Alpha1WorkflowRunReadResponse
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

    def list_workflows(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1Alpha1WorkflowResourceReadResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Alpha1WorkflowResourceReadResponse]
            List of Workflows

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workflows.list_workflows()
        """
        _response = self._raw_client.list_workflows(request_options=request_options)
        return _response.data

    def create_workflow(
        self,
        *,
        metadata: V1Alpha1ResourceMetadata,
        spec: V1Alpha1WorkflowResourceSpec,
        kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Alpha1WorkflowResourceCreateResponse:
        """
        Parameters
        ----------
        metadata : V1Alpha1ResourceMetadata

        spec : V1Alpha1WorkflowResourceSpec

        kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1WorkflowResourceCreateResponse
            The created Workflow

        Examples
        --------
        from fern import (
            FernApi,
            V1Alpha1ResourceMetadata,
            V1Alpha1WorkflowResourceSpec,
            V1Alpha1WorkflowStage,
        )

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workflows.create_workflow(
            metadata=V1Alpha1ResourceMetadata(
                name="name",
            ),
            spec=V1Alpha1WorkflowResourceSpec(
                stages=[
                    V1Alpha1WorkflowStage(
                        target="target",
                        name="name",
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.create_workflow(
            metadata=metadata, spec=spec, kind=kind, request_options=request_options
        )
        return _response.data

    def get_workflow(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1WorkflowResourceReadResponse:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1WorkflowResourceReadResponse
            The Workflow Definition

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workflows.get_workflow(
            identifier="identifier",
        )
        """
        _response = self._raw_client.get_workflow(identifier, request_options=request_options)
        return _response.data

    def update_workflow(
        self,
        identifier: str,
        *,
        metadata: V1Alpha1ResourceMetadata,
        spec: V1Alpha1WorkflowResourceSpec,
        kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Alpha1WorkflowResourceUpdateResponse:
        """
        Parameters
        ----------
        identifier : str

        metadata : V1Alpha1ResourceMetadata

        spec : V1Alpha1WorkflowResourceSpec

        kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1WorkflowResourceUpdateResponse
            The updated Workflow

        Examples
        --------
        from fern import (
            FernApi,
            V1Alpha1ResourceMetadata,
            V1Alpha1WorkflowResourceSpec,
            V1Alpha1WorkflowStage,
        )

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workflows.update_workflow(
            identifier="identifier",
            metadata=V1Alpha1ResourceMetadata(
                name="name",
            ),
            spec=V1Alpha1WorkflowResourceSpec(
                stages=[
                    V1Alpha1WorkflowStage(
                        target="target",
                        name="name",
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.update_workflow(
            identifier, metadata=metadata, spec=spec, kind=kind, request_options=request_options
        )
        return _response.data

    def delete_workflow(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1WorkflowResourceReadResponse:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1WorkflowResourceReadResponse
            The Workflow that was deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workflows.delete_workflow(
            identifier="identifier",
        )
        """
        _response = self._raw_client.delete_workflow(identifier, request_options=request_options)
        return _response.data

    def list_workflow_runs(
        self,
        identifier: str,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1Alpha1WorkflowRunReadResponse]:
        """
        Parameters
        ----------
        identifier : str

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Alpha1WorkflowRunReadResponse]
            List of Workflow Runs

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workflows.list_workflow_runs(
            identifier="identifier",
        )
        """
        _response = self._raw_client.list_workflow_runs(identifier, limit=limit, request_options=request_options)
        return _response.data

    def run_workflow(
        self,
        identifier: str,
        *,
        request: typing.Dict[str, typing.Any],
        namespace: typing.Optional[str] = None,
        wait: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Alpha1WorkflowRunReadResponse:
        """
        Parameters
        ----------
        identifier : str

        request : typing.Dict[str, typing.Any]

        namespace : typing.Optional[str]

        wait : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1WorkflowRunReadResponse
            The WorkflowRun that was created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workflows.run_workflow(
            identifier="identifier",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.run_workflow(
            identifier, request=request, namespace=namespace, wait=wait, request_options=request_options
        )
        return _response.data

    def get_workflow_run(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1WorkflowRunReadResponse:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1WorkflowRunReadResponse
            The Workflow Run

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workflows.get_workflow_run(
            identifier="identifier",
        )
        """
        _response = self._raw_client.get_workflow_run(identifier, request_options=request_options)
        return _response.data

    def delete_workflow_run(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1WorkflowRunReadResponse:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1WorkflowRunReadResponse
            The deleted Workflow Run

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workflows.delete_workflow_run(
            identifier="identifier",
        )
        """
        _response = self._raw_client.delete_workflow_run(identifier, request_options=request_options)
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

    async def list_workflows(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1Alpha1WorkflowResourceReadResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Alpha1WorkflowResourceReadResponse]
            List of Workflows

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workflows.list_workflows()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_workflows(request_options=request_options)
        return _response.data

    async def create_workflow(
        self,
        *,
        metadata: V1Alpha1ResourceMetadata,
        spec: V1Alpha1WorkflowResourceSpec,
        kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Alpha1WorkflowResourceCreateResponse:
        """
        Parameters
        ----------
        metadata : V1Alpha1ResourceMetadata

        spec : V1Alpha1WorkflowResourceSpec

        kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1WorkflowResourceCreateResponse
            The created Workflow

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            V1Alpha1ResourceMetadata,
            V1Alpha1WorkflowResourceSpec,
            V1Alpha1WorkflowStage,
        )

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workflows.create_workflow(
                metadata=V1Alpha1ResourceMetadata(
                    name="name",
                ),
                spec=V1Alpha1WorkflowResourceSpec(
                    stages=[
                        V1Alpha1WorkflowStage(
                            target="target",
                            name="name",
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_workflow(
            metadata=metadata, spec=spec, kind=kind, request_options=request_options
        )
        return _response.data

    async def get_workflow(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1WorkflowResourceReadResponse:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1WorkflowResourceReadResponse
            The Workflow Definition

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workflows.get_workflow(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_workflow(identifier, request_options=request_options)
        return _response.data

    async def update_workflow(
        self,
        identifier: str,
        *,
        metadata: V1Alpha1ResourceMetadata,
        spec: V1Alpha1WorkflowResourceSpec,
        kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Alpha1WorkflowResourceUpdateResponse:
        """
        Parameters
        ----------
        identifier : str

        metadata : V1Alpha1ResourceMetadata

        spec : V1Alpha1WorkflowResourceSpec

        kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1WorkflowResourceUpdateResponse
            The updated Workflow

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            V1Alpha1ResourceMetadata,
            V1Alpha1WorkflowResourceSpec,
            V1Alpha1WorkflowStage,
        )

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workflows.update_workflow(
                identifier="identifier",
                metadata=V1Alpha1ResourceMetadata(
                    name="name",
                ),
                spec=V1Alpha1WorkflowResourceSpec(
                    stages=[
                        V1Alpha1WorkflowStage(
                            target="target",
                            name="name",
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_workflow(
            identifier, metadata=metadata, spec=spec, kind=kind, request_options=request_options
        )
        return _response.data

    async def delete_workflow(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1WorkflowResourceReadResponse:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1WorkflowResourceReadResponse
            The Workflow that was deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workflows.delete_workflow(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_workflow(identifier, request_options=request_options)
        return _response.data

    async def list_workflow_runs(
        self,
        identifier: str,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1Alpha1WorkflowRunReadResponse]:
        """
        Parameters
        ----------
        identifier : str

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Alpha1WorkflowRunReadResponse]
            List of Workflow Runs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workflows.list_workflow_runs(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_workflow_runs(identifier, limit=limit, request_options=request_options)
        return _response.data

    async def run_workflow(
        self,
        identifier: str,
        *,
        request: typing.Dict[str, typing.Any],
        namespace: typing.Optional[str] = None,
        wait: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Alpha1WorkflowRunReadResponse:
        """
        Parameters
        ----------
        identifier : str

        request : typing.Dict[str, typing.Any]

        namespace : typing.Optional[str]

        wait : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1WorkflowRunReadResponse
            The WorkflowRun that was created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workflows.run_workflow(
                identifier="identifier",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_workflow(
            identifier, request=request, namespace=namespace, wait=wait, request_options=request_options
        )
        return _response.data

    async def get_workflow_run(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1WorkflowRunReadResponse:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1WorkflowRunReadResponse
            The Workflow Run

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workflows.get_workflow_run(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_workflow_run(identifier, request_options=request_options)
        return _response.data

    async def delete_workflow_run(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Alpha1WorkflowRunReadResponse:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1WorkflowRunReadResponse
            The deleted Workflow Run

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.workflows.delete_workflow_run(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_workflow_run(identifier, request_options=request_options)
        return _response.data
