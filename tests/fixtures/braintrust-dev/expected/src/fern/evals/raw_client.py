

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.function_id import FunctionId
from ..types.git_metadata_settings import GitMetadataSettings
from ..types.summarize_experiment_response import SummarizeExperimentResponse
from .types.run_eval_data import RunEvalData
from .types.run_eval_mcp_auth_value import RunEvalMcpAuthValue
from .types.run_eval_parent import RunEvalParent
from .types.run_eval_repo_info import RunEvalRepoInfo
from .types.run_eval_scores_item import RunEvalScoresItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEvalsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[SummarizeExperimentResponse]:
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
        HttpResponse[SummarizeExperimentResponse]
            Eval launch response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/eval",
            method="POST",
            json={
                "project_id": project_id,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=RunEvalData, direction="write"
                ),
                "name": name,
                "parameters": parameters,
                "task": convert_and_respect_annotation_metadata(object_=task, annotation=FunctionId, direction="write"),
                "scores": convert_and_respect_annotation_metadata(
                    object_=scores, annotation=typing.Sequence[RunEvalScoresItem], direction="write"
                ),
                "experiment_name": experiment_name,
                "metadata": metadata,
                "parent": convert_and_respect_annotation_metadata(
                    object_=parent, annotation=RunEvalParent, direction="write"
                ),
                "stream": stream,
                "trial_count": trial_count,
                "is_public": is_public,
                "timeout": timeout,
                "max_concurrency": max_concurrency,
                "base_experiment_name": base_experiment_name,
                "base_experiment_id": base_experiment_id,
                "git_metadata_settings": convert_and_respect_annotation_metadata(
                    object_=git_metadata_settings, annotation=typing.Optional[GitMetadataSettings], direction="write"
                ),
                "repo_info": convert_and_respect_annotation_metadata(
                    object_=repo_info, annotation=typing.Optional[RunEvalRepoInfo], direction="write"
                ),
                "strict": strict,
                "stop_token": stop_token,
                "extra_messages": extra_messages,
                "tags": tags,
                "mcp_auth": convert_and_respect_annotation_metadata(
                    object_=mcp_auth, annotation=typing.Dict[str, RunEvalMcpAuthValue], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SummarizeExperimentResponse,
                    parse_obj_as(
                        type_=SummarizeExperimentResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawEvalsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[SummarizeExperimentResponse]:
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
        AsyncHttpResponse[SummarizeExperimentResponse]
            Eval launch response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/eval",
            method="POST",
            json={
                "project_id": project_id,
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=RunEvalData, direction="write"
                ),
                "name": name,
                "parameters": parameters,
                "task": convert_and_respect_annotation_metadata(object_=task, annotation=FunctionId, direction="write"),
                "scores": convert_and_respect_annotation_metadata(
                    object_=scores, annotation=typing.Sequence[RunEvalScoresItem], direction="write"
                ),
                "experiment_name": experiment_name,
                "metadata": metadata,
                "parent": convert_and_respect_annotation_metadata(
                    object_=parent, annotation=RunEvalParent, direction="write"
                ),
                "stream": stream,
                "trial_count": trial_count,
                "is_public": is_public,
                "timeout": timeout,
                "max_concurrency": max_concurrency,
                "base_experiment_name": base_experiment_name,
                "base_experiment_id": base_experiment_id,
                "git_metadata_settings": convert_and_respect_annotation_metadata(
                    object_=git_metadata_settings, annotation=typing.Optional[GitMetadataSettings], direction="write"
                ),
                "repo_info": convert_and_respect_annotation_metadata(
                    object_=repo_info, annotation=typing.Optional[RunEvalRepoInfo], direction="write"
                ),
                "strict": strict,
                "stop_token": stop_token,
                "extra_messages": extra_messages,
                "tags": tags,
                "mcp_auth": convert_and_respect_annotation_metadata(
                    object_=mcp_auth, annotation=typing.Dict[str, RunEvalMcpAuthValue], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SummarizeExperimentResponse,
                    parse_obj_as(
                        type_=SummarizeExperimentResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
