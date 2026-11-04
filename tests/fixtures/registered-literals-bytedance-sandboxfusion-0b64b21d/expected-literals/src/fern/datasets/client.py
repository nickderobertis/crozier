

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.eval_result_input import EvalResultInput
from ..types.eval_result_output import EvalResultOutput
from ..types.get_metrics_function_result import GetMetricsFunctionResult
from ..types.prompt import Prompt
from ..types.test_config import TestConfig
from .raw_client import AsyncRawDatasetsClient, RawDatasetsClient
from .types.get_prompt_by_id_request_id import GetPromptByIdRequestId
from .types.list_ids_list_ids_post_response_item import ListIdsListIdsPostResponseItem
from .types.submit_request_id import SubmitRequestId


OMIT = typing.cast(typing.Any, ...)


class DatasetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDatasetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDatasetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDatasetsClient
        """
        return self._raw_client

    def list_datasets(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        List all registered datasets

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasets.list_datasets()
        """
        _response = self._raw_client.list_datasets(request_options=request_options)
        return _response.data

    def list_ids(
        self,
        *,
        dataset: str,
        config: TestConfig,
        offset: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ListIdsListIdsPostResponseItem]:
        """
        List all ids of a dataset

        Parameters
        ----------
        dataset : str

        config : TestConfig

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListIdsListIdsPostResponseItem]
            Successful Response

        Examples
        --------
        from fern import FernApi, TestConfig

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasets.list_ids(
            dataset="dataset",
            config=TestConfig(),
        )
        """
        _response = self._raw_client.list_ids(
            dataset=dataset, config=config, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def get_prompt(
        self,
        *,
        dataset: str,
        config: TestConfig,
        offset: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Prompt]:
        """
        Get prompts of a dataset

        Parameters
        ----------
        dataset : str

        config : TestConfig

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Prompt]
            Successful Response

        Examples
        --------
        from fern import FernApi, TestConfig

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasets.get_prompt(
            dataset="dataset",
            config=TestConfig(),
        )
        """
        _response = self._raw_client.get_prompt(
            dataset=dataset, config=config, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def get_prompt_by_id(
        self,
        *,
        dataset: str,
        config: TestConfig,
        id: GetPromptByIdRequestId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prompt:
        """
        Get a single prompt given id in a dataset

        Parameters
        ----------
        dataset : str

        config : TestConfig

        id : GetPromptByIdRequestId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt
            Successful Response

        Examples
        --------
        from fern import FernApi, TestConfig

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasets.get_prompt_by_id(
            dataset="dataset",
            config=TestConfig(),
            id=1,
        )
        """
        _response = self._raw_client.get_prompt_by_id(
            dataset=dataset, config=config, id=id, request_options=request_options
        )
        return _response.data

    def submit(
        self,
        *,
        dataset: str,
        id: SubmitRequestId,
        completion: str,
        config: TestConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EvalResultOutput:
        """
        Submit a single problem in a dataset

        Parameters
        ----------
        dataset : str

        id : SubmitRequestId

        completion : str

        config : TestConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalResultOutput
            Successful Response

        Examples
        --------
        from fern import FernApi, TestConfig

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasets.submit(
            dataset="dataset",
            id=1,
            completion="completion",
            config=TestConfig(),
        )
        """
        _response = self._raw_client.submit(
            dataset=dataset, id=id, completion=completion, config=config, request_options=request_options
        )
        return _response.data

    def get_metrics(
        self,
        *,
        dataset: str,
        config: TestConfig,
        results: typing.Sequence[EvalResultInput],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Get the metrics given all problem results in a dataset (partially supported)

        Parameters
        ----------
        dataset : str

        config : TestConfig

        results : typing.Sequence[EvalResultInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        from fern import (
            EvalResultInput,
            EvalTestCaseInput,
            FernApi,
            RunCodeResponseInput,
            TestConfig,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasets.get_metrics(
            dataset="dataset",
            config=TestConfig(),
            results=[
                EvalResultInput(
                    id=1,
                    accepted=True,
                    extracted_code="extracted_code",
                    tests=[
                        EvalTestCaseInput(
                            passed=True,
                            exec_info=RunCodeResponseInput(
                                status="Success",
                                message="message",
                            ),
                        )
                    ],
                )
            ],
        )
        """
        _response = self._raw_client.get_metrics(
            dataset=dataset, config=config, results=results, request_options=request_options
        )
        return _response.data

    def get_metrics_function(
        self, *, dataset: str, config: TestConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMetricsFunctionResult:
        """
        Get the function to generate the metrics given results (partially supported)

        Parameters
        ----------
        dataset : str

        config : TestConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMetricsFunctionResult
            Successful Response

        Examples
        --------
        from fern import FernApi, TestConfig

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasets.get_metrics_function(
            dataset="dataset",
            config=TestConfig(),
        )
        """
        _response = self._raw_client.get_metrics_function(
            dataset=dataset, config=config, request_options=request_options
        )
        return _response.data


class AsyncDatasetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDatasetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDatasetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDatasetsClient
        """
        return self._raw_client

    async def list_datasets(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        List all registered datasets

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.datasets.list_datasets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_datasets(request_options=request_options)
        return _response.data

    async def list_ids(
        self,
        *,
        dataset: str,
        config: TestConfig,
        offset: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ListIdsListIdsPostResponseItem]:
        """
        List all ids of a dataset

        Parameters
        ----------
        dataset : str

        config : TestConfig

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListIdsListIdsPostResponseItem]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TestConfig

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.datasets.list_ids(
                dataset="dataset",
                config=TestConfig(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_ids(
            dataset=dataset, config=config, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def get_prompt(
        self,
        *,
        dataset: str,
        config: TestConfig,
        offset: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Prompt]:
        """
        Get prompts of a dataset

        Parameters
        ----------
        dataset : str

        config : TestConfig

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Prompt]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TestConfig

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.datasets.get_prompt(
                dataset="dataset",
                config=TestConfig(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_prompt(
            dataset=dataset, config=config, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def get_prompt_by_id(
        self,
        *,
        dataset: str,
        config: TestConfig,
        id: GetPromptByIdRequestId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prompt:
        """
        Get a single prompt given id in a dataset

        Parameters
        ----------
        dataset : str

        config : TestConfig

        id : GetPromptByIdRequestId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TestConfig

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.datasets.get_prompt_by_id(
                dataset="dataset",
                config=TestConfig(),
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_prompt_by_id(
            dataset=dataset, config=config, id=id, request_options=request_options
        )
        return _response.data

    async def submit(
        self,
        *,
        dataset: str,
        id: SubmitRequestId,
        completion: str,
        config: TestConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EvalResultOutput:
        """
        Submit a single problem in a dataset

        Parameters
        ----------
        dataset : str

        id : SubmitRequestId

        completion : str

        config : TestConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EvalResultOutput
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TestConfig

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.datasets.submit(
                dataset="dataset",
                id=1,
                completion="completion",
                config=TestConfig(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit(
            dataset=dataset, id=id, completion=completion, config=config, request_options=request_options
        )
        return _response.data

    async def get_metrics(
        self,
        *,
        dataset: str,
        config: TestConfig,
        results: typing.Sequence[EvalResultInput],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Get the metrics given all problem results in a dataset (partially supported)

        Parameters
        ----------
        dataset : str

        config : TestConfig

        results : typing.Sequence[EvalResultInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            EvalResultInput,
            EvalTestCaseInput,
            RunCodeResponseInput,
            TestConfig,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.datasets.get_metrics(
                dataset="dataset",
                config=TestConfig(),
                results=[
                    EvalResultInput(
                        id=1,
                        accepted=True,
                        extracted_code="extracted_code",
                        tests=[
                            EvalTestCaseInput(
                                passed=True,
                                exec_info=RunCodeResponseInput(
                                    status="Success",
                                    message="message",
                                ),
                            )
                        ],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_metrics(
            dataset=dataset, config=config, results=results, request_options=request_options
        )
        return _response.data

    async def get_metrics_function(
        self, *, dataset: str, config: TestConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMetricsFunctionResult:
        """
        Get the function to generate the metrics given results (partially supported)

        Parameters
        ----------
        dataset : str

        config : TestConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMetricsFunctionResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TestConfig

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.datasets.get_metrics_function(
                dataset="dataset",
                config=TestConfig(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_metrics_function(
            dataset=dataset, config=config, request_options=request_options
        )
        return _response.data
