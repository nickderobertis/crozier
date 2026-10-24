

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWorkflowsClient, RawWorkflowsClient
from .types.run_config_input_user_input import RunConfigInputUserInput
from .types.run_config_input_workflow import RunConfigInputWorkflow


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

    def terravibes_list_workflows(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        List all workflows available in FarmVibes.AI.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.workflows.terravibes_list_workflows()
        """
        _response = self._raw_client.terravibes_list_workflows(request_options=request_options)
        return _response.data

    def terravibes_describe_workflow(
        self,
        workflow: str,
        *,
        return_format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Get a workflow by name, either as JSON description, or YAML graph implementation.

        Parameters
        ----------
        workflow : str
            The name of the workflow to be described.

        return_format : typing.Optional[str]
            The format to return the workflow in [description, yaml].

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.workflows.terravibes_describe_workflow(
            workflow="workflow",
        )
        """
        _response = self._raw_client.terravibes_describe_workflow(
            workflow, return_format=return_format, request_options=request_options
        )
        return _response.data

    def terravibes_create_run(
        self,
        *,
        name: str,
        workflow: RunConfigInputWorkflow,
        parameters: typing.Dict[str, typing.Any],
        user_input: RunConfigInputUserInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Submit a new workflow run.

        Parameters
        ----------
        name : str

        workflow : RunConfigInputWorkflow

        parameters : typing.Dict[str, typing.Any]

        user_input : RunConfigInputUserInput

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import datetime

        from fern import FernApi, SpatioTemporalJson

        client = FernApi()
        client.workflows.terravibes_create_run(
            name="example workflow run for sample region",
            workflow="helloworld",
            parameters={"key": "value"},
            user_input=SpatioTemporalJson(
                start_date=datetime.datetime.fromisoformat(
                    "2021-02-02 00:00:00+00:00",
                ),
                end_date=datetime.datetime.fromisoformat(
                    "2021-08-02 00:00:00+00:00",
                ),
                geojson={
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "type": "Feature",
                            "geometry": {
                                "type": "Polygon",
                                "coordinates": [
                                    [
                                        [-88.068487, 37.058836],
                                        [-88.036059, 37.048687],
                                        [-88.012895, 37.068984],
                                        [-88.026622, 37.085711],
                                        [-88.062482, 37.081461],
                                        [-88.068487, 37.058836],
                                    ]
                                ],
                            },
                        }
                    ],
                },
            ),
        )
        """
        _response = self._raw_client.terravibes_create_run(
            name=name, workflow=workflow, parameters=parameters, user_input=user_input, request_options=request_options
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

    async def terravibes_list_workflows(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        List all workflows available in FarmVibes.AI.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.workflows.terravibes_list_workflows()


        asyncio.run(main())
        """
        _response = await self._raw_client.terravibes_list_workflows(request_options=request_options)
        return _response.data

    async def terravibes_describe_workflow(
        self,
        workflow: str,
        *,
        return_format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Get a workflow by name, either as JSON description, or YAML graph implementation.

        Parameters
        ----------
        workflow : str
            The name of the workflow to be described.

        return_format : typing.Optional[str]
            The format to return the workflow in [description, yaml].

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.workflows.terravibes_describe_workflow(
                workflow="workflow",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.terravibes_describe_workflow(
            workflow, return_format=return_format, request_options=request_options
        )
        return _response.data

    async def terravibes_create_run(
        self,
        *,
        name: str,
        workflow: RunConfigInputWorkflow,
        parameters: typing.Dict[str, typing.Any],
        user_input: RunConfigInputUserInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Submit a new workflow run.

        Parameters
        ----------
        name : str

        workflow : RunConfigInputWorkflow

        parameters : typing.Dict[str, typing.Any]

        user_input : RunConfigInputUserInput

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, SpatioTemporalJson

        client = AsyncFernApi()


        async def main() -> None:
            await client.workflows.terravibes_create_run(
                name="example workflow run for sample region",
                workflow="helloworld",
                parameters={"key": "value"},
                user_input=SpatioTemporalJson(
                    start_date=datetime.datetime.fromisoformat(
                        "2021-02-02 00:00:00+00:00",
                    ),
                    end_date=datetime.datetime.fromisoformat(
                        "2021-08-02 00:00:00+00:00",
                    ),
                    geojson={
                        "type": "FeatureCollection",
                        "features": [
                            {
                                "type": "Feature",
                                "geometry": {
                                    "type": "Polygon",
                                    "coordinates": [
                                        [
                                            [-88.068487, 37.058836],
                                            [-88.036059, 37.048687],
                                            [-88.012895, 37.068984],
                                            [-88.026622, 37.085711],
                                            [-88.062482, 37.081461],
                                            [-88.068487, 37.058836],
                                        ]
                                    ],
                                },
                            }
                        ],
                    },
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.terravibes_create_run(
            name=name, workflow=workflow, parameters=parameters, user_input=user_input, request_options=request_options
        )
        return _response.data
