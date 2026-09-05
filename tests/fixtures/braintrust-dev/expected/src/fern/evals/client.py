

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.function_id import FunctionId
from ..types.git_metadata_settings import GitMetadataSettings
from ..types.summarize_experiment_response import SummarizeExperimentResponse
from .raw_client import AsyncRawEvalsClient, RawEvalsClient
from .types.run_eval_data import RunEvalData
from .types.run_eval_mcp_auth_value import RunEvalMcpAuthValue
from .types.run_eval_parent import RunEvalParent
from .types.run_eval_repo_info import RunEvalRepoInfo
from .types.run_eval_scores_item import RunEvalScoresItem


OMIT = typing.cast(typing.Any, ...)


class EvalsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEvalsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEvalsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEvalsClient
        """
        return self._raw_client

    def eval_launch(
        self,
        *,
        project_id: str,
        data: RunEvalData,
        task: FunctionId,
        scores: typing.Sequence[RunEvalScoresItem],
        name: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        experiment_name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        parent: typing.Optional[RunEvalParent] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        trial_count: typing.Optional[float] = OMIT,
        is_public: typing.Optional[bool] = OMIT,
        timeout: typing.Optional[float] = OMIT,
        max_concurrency: typing.Optional[float] = OMIT,
        base_experiment_name: typing.Optional[str] = OMIT,
        base_experiment_id: typing.Optional[str] = OMIT,
        git_metadata_settings: typing.Optional[GitMetadataSettings] = OMIT,
        repo_info: typing.Optional[RunEvalRepoInfo] = OMIT,
        strict: typing.Optional[bool] = OMIT,
        stop_token: typing.Optional[str] = OMIT,
        extra_messages: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        mcp_auth: typing.Optional[typing.Dict[str, RunEvalMcpAuthValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SummarizeExperimentResponse:
        """
        Launch an evaluation. This is the API-equivalent of the `Eval` function that is built into the Braintrust SDK. In the Eval API, you provide pointers to a dataset, task function, and scoring functions. The API will then run the evaluation, create an experiment, and return the results along with a link to the experiment. To learn more about evals, see the [Evals guide](https://www.braintrust.dev/docs/evaluate).

        Parameters
        ----------
        project_id : str
            Unique identifier for the project to run the eval in

        data : RunEvalData
            The dataset to use

        task : FunctionId

        scores : typing.Sequence[RunEvalScoresItem]
            The functions to score the eval on

        name : typing.Optional[str]
            The name of the eval to run when multiple evals available

        parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Values for any parameters used in the eval

        experiment_name : typing.Optional[str]
            An optional name for the experiment created by this eval. If it conflicts with an existing experiment, it will be suffixed with a unique identifier.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional experiment-level metadata to store about the evaluation. You can later use this to slice & dice across experiments.

        parent : typing.Optional[RunEvalParent]
            Options for tracing the evaluation

        stream : typing.Optional[bool]
            Whether to stream the results of the eval. If true, the request will return two events: one to indicate the experiment has started, and another upon completion. If false, the request will return the evaluation's summary upon completion.

        trial_count : typing.Optional[float]
            The number of times to run the evaluator per input. This is useful for evaluating applications that have non-deterministic behavior and gives you both a stronger aggregate measure and a sense of the variance in the results.

        is_public : typing.Optional[bool]
            Whether the experiment should be public. Defaults to false.

        timeout : typing.Optional[float]
            The maximum duration, in milliseconds, to run the evaluation. Defaults to undefined, in which case there is no timeout.

        max_concurrency : typing.Optional[float]
            The maximum number of tasks/scorers that will be run concurrently. Defaults to 10. If null is provided, no max concurrency will be used.

        base_experiment_name : typing.Optional[str]
            An optional experiment name to use as a base. If specified, the new experiment will be summarized and compared to this experiment.

        base_experiment_id : typing.Optional[str]
            An optional experiment id to use as a base. If specified, the new experiment will be summarized and compared to this experiment.

        git_metadata_settings : typing.Optional[GitMetadataSettings]

        repo_info : typing.Optional[RunEvalRepoInfo]
            Optionally explicitly specify the git metadata for this experiment. This takes precedence over `gitMetadataSettings` if specified.

        strict : typing.Optional[bool]
            If true, throw an error if one of the variables in the prompt is not present in the input

        stop_token : typing.Optional[str]
            The token to stop the run

        extra_messages : typing.Optional[str]
            A template path of extra messages to append to the conversion. These messages will be appended to the end of the conversation, after the last message.

        tags : typing.Optional[typing.Sequence[str]]
            Optional tags that will be added to the experiment.

        mcp_auth : typing.Optional[typing.Dict[str, RunEvalMcpAuthValue]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SummarizeExperimentResponse
            Eval launch response

        Examples
        --------
        from fern.evals import RunEvalDataDatasetId, RunEvalScoresItemFunctionId

        from fern import FernApi, FunctionIdFunctionId

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.evals.eval_launch(
            project_id="project_id",
            data=RunEvalDataDatasetId(
                dataset_id="dataset_id",
            ),
            task=FunctionIdFunctionId(
                function_id="function_id",
            ),
            scores=[
                RunEvalScoresItemFunctionId(
                    function_id="function_id",
                )
            ],
        )
        """
        _response = self._raw_client.eval_launch(
            project_id=project_id,
            data=data,
            task=task,
            scores=scores,
            name=name,
            parameters=parameters,
            experiment_name=experiment_name,
            metadata=metadata,
            parent=parent,
            stream=stream,
            trial_count=trial_count,
            is_public=is_public,
            timeout=timeout,
            max_concurrency=max_concurrency,
            base_experiment_name=base_experiment_name,
            base_experiment_id=base_experiment_id,
            git_metadata_settings=git_metadata_settings,
            repo_info=repo_info,
            strict=strict,
            stop_token=stop_token,
            extra_messages=extra_messages,
            tags=tags,
            mcp_auth=mcp_auth,
            request_options=request_options,
        )
        return _response.data


class AsyncEvalsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEvalsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEvalsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEvalsClient
        """
        return self._raw_client

    async def eval_launch(
        self,
        *,
        project_id: str,
        data: RunEvalData,
        task: FunctionId,
        scores: typing.Sequence[RunEvalScoresItem],
        name: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        experiment_name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        parent: typing.Optional[RunEvalParent] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        trial_count: typing.Optional[float] = OMIT,
        is_public: typing.Optional[bool] = OMIT,
        timeout: typing.Optional[float] = OMIT,
        max_concurrency: typing.Optional[float] = OMIT,
        base_experiment_name: typing.Optional[str] = OMIT,
        base_experiment_id: typing.Optional[str] = OMIT,
        git_metadata_settings: typing.Optional[GitMetadataSettings] = OMIT,
        repo_info: typing.Optional[RunEvalRepoInfo] = OMIT,
        strict: typing.Optional[bool] = OMIT,
        stop_token: typing.Optional[str] = OMIT,
        extra_messages: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        mcp_auth: typing.Optional[typing.Dict[str, RunEvalMcpAuthValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SummarizeExperimentResponse:
        """
        Launch an evaluation. This is the API-equivalent of the `Eval` function that is built into the Braintrust SDK. In the Eval API, you provide pointers to a dataset, task function, and scoring functions. The API will then run the evaluation, create an experiment, and return the results along with a link to the experiment. To learn more about evals, see the [Evals guide](https://www.braintrust.dev/docs/evaluate).

        Parameters
        ----------
        project_id : str
            Unique identifier for the project to run the eval in

        data : RunEvalData
            The dataset to use

        task : FunctionId

        scores : typing.Sequence[RunEvalScoresItem]
            The functions to score the eval on

        name : typing.Optional[str]
            The name of the eval to run when multiple evals available

        parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Values for any parameters used in the eval

        experiment_name : typing.Optional[str]
            An optional name for the experiment created by this eval. If it conflicts with an existing experiment, it will be suffixed with a unique identifier.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional experiment-level metadata to store about the evaluation. You can later use this to slice & dice across experiments.

        parent : typing.Optional[RunEvalParent]
            Options for tracing the evaluation

        stream : typing.Optional[bool]
            Whether to stream the results of the eval. If true, the request will return two events: one to indicate the experiment has started, and another upon completion. If false, the request will return the evaluation's summary upon completion.

        trial_count : typing.Optional[float]
            The number of times to run the evaluator per input. This is useful for evaluating applications that have non-deterministic behavior and gives you both a stronger aggregate measure and a sense of the variance in the results.

        is_public : typing.Optional[bool]
            Whether the experiment should be public. Defaults to false.

        timeout : typing.Optional[float]
            The maximum duration, in milliseconds, to run the evaluation. Defaults to undefined, in which case there is no timeout.

        max_concurrency : typing.Optional[float]
            The maximum number of tasks/scorers that will be run concurrently. Defaults to 10. If null is provided, no max concurrency will be used.

        base_experiment_name : typing.Optional[str]
            An optional experiment name to use as a base. If specified, the new experiment will be summarized and compared to this experiment.

        base_experiment_id : typing.Optional[str]
            An optional experiment id to use as a base. If specified, the new experiment will be summarized and compared to this experiment.

        git_metadata_settings : typing.Optional[GitMetadataSettings]

        repo_info : typing.Optional[RunEvalRepoInfo]
            Optionally explicitly specify the git metadata for this experiment. This takes precedence over `gitMetadataSettings` if specified.

        strict : typing.Optional[bool]
            If true, throw an error if one of the variables in the prompt is not present in the input

        stop_token : typing.Optional[str]
            The token to stop the run

        extra_messages : typing.Optional[str]
            A template path of extra messages to append to the conversion. These messages will be appended to the end of the conversation, after the last message.

        tags : typing.Optional[typing.Sequence[str]]
            Optional tags that will be added to the experiment.

        mcp_auth : typing.Optional[typing.Dict[str, RunEvalMcpAuthValue]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SummarizeExperimentResponse
            Eval launch response

        Examples
        --------
        import asyncio

        from fern.evals import RunEvalDataDatasetId, RunEvalScoresItemFunctionId

        from fern import AsyncFernApi, FunctionIdFunctionId

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.evals.eval_launch(
                project_id="project_id",
                data=RunEvalDataDatasetId(
                    dataset_id="dataset_id",
                ),
                task=FunctionIdFunctionId(
                    function_id="function_id",
                ),
                scores=[
                    RunEvalScoresItemFunctionId(
                        function_id="function_id",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eval_launch(
            project_id=project_id,
            data=data,
            task=task,
            scores=scores,
            name=name,
            parameters=parameters,
            experiment_name=experiment_name,
            metadata=metadata,
            parent=parent,
            stream=stream,
            trial_count=trial_count,
            is_public=is_public,
            timeout=timeout,
            max_concurrency=max_concurrency,
            base_experiment_name=base_experiment_name,
            base_experiment_id=base_experiment_id,
            git_metadata_settings=git_metadata_settings,
            repo_info=repo_info,
            strict=strict,
            stop_token=stop_token,
            extra_messages=extra_messages,
            tags=tags,
            mcp_auth=mcp_auth,
            request_options=request_options,
        )
        return _response.data
