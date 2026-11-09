

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.fine_tuning_job import FineTuningJob
from ..types.list_fine_tuning_job_checkpoints_response import ListFineTuningJobCheckpointsResponse
from ..types.list_fine_tuning_job_events_response import ListFineTuningJobEventsResponse
from ..types.list_paginated_fine_tuning_jobs_response import ListPaginatedFineTuningJobsResponse
from .types.create_fine_tuning_job_request_hyperparameters import CreateFineTuningJobRequestHyperparameters
from .types.create_fine_tuning_job_request_integrations_item import CreateFineTuningJobRequestIntegrationsItem
from .types.create_fine_tuning_job_request_model import CreateFineTuningJobRequestModel
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFineTuningClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_paginated_fine_tuning_jobs(
        self,
        *,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListPaginatedFineTuningJobsResponse]:
        """
        Parameters
        ----------
        after : typing.Optional[str]
            Identifier for the last job from the previous pagination request.

        limit : typing.Optional[int]
            Number of fine-tuning jobs to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListPaginatedFineTuningJobsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "fine_tuning/jobs",
            method="GET",
            params={
                "after": after,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPaginatedFineTuningJobsResponse,
                    parse_obj_as(
                        type_=ListPaginatedFineTuningJobsResponse,
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

    def create_fine_tuning_job(
        self,
        *,
        model: CreateFineTuningJobRequestModel,
        training_file: str,
        hyperparameters: typing.Optional[CreateFineTuningJobRequestHyperparameters] = OMIT,
        suffix: typing.Optional[str] = OMIT,
        validation_file: typing.Optional[str] = OMIT,
        integrations: typing.Optional[typing.Sequence[CreateFineTuningJobRequestIntegrationsItem]] = OMIT,
        seed: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FineTuningJob]:
        """
        Parameters
        ----------
        model : CreateFineTuningJobRequestModel
            The name of the model to fine-tune. You can select one of the
            [supported models](/docs/guides/fine-tuning/what-models-can-be-fine-tuned).

        training_file : str
            The ID of an uploaded file that contains training data.

            See [upload file](/docs/api-reference/files/upload) for how to upload a file.

            Your dataset must be formatted as a JSONL file. Additionally, you must upload your file with the purpose `fine-tune`.

            See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.

        hyperparameters : typing.Optional[CreateFineTuningJobRequestHyperparameters]
            The hyperparameters used for the fine-tuning job.

        suffix : typing.Optional[str]
            A string of up to 18 characters that will be added to your fine-tuned model name.

            For example, a `suffix` of "custom-model-name" would produce a model name like `ft:gpt-3.5-turbo:openai:custom-model-name:7p4lURel`.

        validation_file : typing.Optional[str]
            The ID of an uploaded file that contains validation data.

            If you provide this file, the data is used to generate validation
            metrics periodically during fine-tuning. These metrics can be viewed in
            the fine-tuning results file.
            The same data should not be present in both train and validation files.

            Your dataset must be formatted as a JSONL file. You must upload your file with the purpose `fine-tune`.

            See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.

        integrations : typing.Optional[typing.Sequence[CreateFineTuningJobRequestIntegrationsItem]]
            A list of integrations to enable for your fine-tuning job.

        seed : typing.Optional[int]
            The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but may differ in rare cases.
            If a seed is not specified, one will be generated for you.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FineTuningJob]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "fine_tuning/jobs",
            method="POST",
            json={
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=CreateFineTuningJobRequestModel, direction="write"
                ),
                "training_file": training_file,
                "hyperparameters": convert_and_respect_annotation_metadata(
                    object_=hyperparameters, annotation=CreateFineTuningJobRequestHyperparameters, direction="write"
                ),
                "suffix": suffix,
                "validation_file": validation_file,
                "integrations": convert_and_respect_annotation_metadata(
                    object_=integrations,
                    annotation=typing.Optional[typing.Sequence[CreateFineTuningJobRequestIntegrationsItem]],
                    direction="write",
                ),
                "seed": seed,
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
                    FineTuningJob,
                    parse_obj_as(
                        type_=FineTuningJob,
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

    def retrieve_fine_tuning_job(
        self, fine_tuning_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FineTuningJob]:
        """
        Parameters
        ----------
        fine_tuning_job_id : str
            The ID of the fine-tuning job.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FineTuningJob]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fine_tuning/jobs/{encode_path_param(fine_tuning_job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FineTuningJob,
                    parse_obj_as(
                        type_=FineTuningJob,
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

    def list_fine_tuning_events(
        self,
        fine_tuning_job_id: str,
        *,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListFineTuningJobEventsResponse]:
        """
        Parameters
        ----------
        fine_tuning_job_id : str
            The ID of the fine-tuning job to get events for.

        after : typing.Optional[str]
            Identifier for the last event from the previous pagination request.

        limit : typing.Optional[int]
            Number of events to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListFineTuningJobEventsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fine_tuning/jobs/{encode_path_param(fine_tuning_job_id)}/events",
            method="GET",
            params={
                "after": after,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListFineTuningJobEventsResponse,
                    parse_obj_as(
                        type_=ListFineTuningJobEventsResponse,
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

    def cancel_fine_tuning_job(
        self, fine_tuning_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FineTuningJob]:
        """
        Parameters
        ----------
        fine_tuning_job_id : str
            The ID of the fine-tuning job to cancel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FineTuningJob]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fine_tuning/jobs/{encode_path_param(fine_tuning_job_id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FineTuningJob,
                    parse_obj_as(
                        type_=FineTuningJob,
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

    def list_fine_tuning_job_checkpoints(
        self,
        fine_tuning_job_id: str,
        *,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListFineTuningJobCheckpointsResponse]:
        """
        Parameters
        ----------
        fine_tuning_job_id : str
            The ID of the fine-tuning job to get checkpoints for.

        after : typing.Optional[str]
            Identifier for the last checkpoint ID from the previous pagination request.

        limit : typing.Optional[int]
            Number of checkpoints to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListFineTuningJobCheckpointsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fine_tuning/jobs/{encode_path_param(fine_tuning_job_id)}/checkpoints",
            method="GET",
            params={
                "after": after,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListFineTuningJobCheckpointsResponse,
                    parse_obj_as(
                        type_=ListFineTuningJobCheckpointsResponse,
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


class AsyncRawFineTuningClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_paginated_fine_tuning_jobs(
        self,
        *,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListPaginatedFineTuningJobsResponse]:
        """
        Parameters
        ----------
        after : typing.Optional[str]
            Identifier for the last job from the previous pagination request.

        limit : typing.Optional[int]
            Number of fine-tuning jobs to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListPaginatedFineTuningJobsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "fine_tuning/jobs",
            method="GET",
            params={
                "after": after,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPaginatedFineTuningJobsResponse,
                    parse_obj_as(
                        type_=ListPaginatedFineTuningJobsResponse,
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

    async def create_fine_tuning_job(
        self,
        *,
        model: CreateFineTuningJobRequestModel,
        training_file: str,
        hyperparameters: typing.Optional[CreateFineTuningJobRequestHyperparameters] = OMIT,
        suffix: typing.Optional[str] = OMIT,
        validation_file: typing.Optional[str] = OMIT,
        integrations: typing.Optional[typing.Sequence[CreateFineTuningJobRequestIntegrationsItem]] = OMIT,
        seed: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FineTuningJob]:
        """
        Parameters
        ----------
        model : CreateFineTuningJobRequestModel
            The name of the model to fine-tune. You can select one of the
            [supported models](/docs/guides/fine-tuning/what-models-can-be-fine-tuned).

        training_file : str
            The ID of an uploaded file that contains training data.

            See [upload file](/docs/api-reference/files/upload) for how to upload a file.

            Your dataset must be formatted as a JSONL file. Additionally, you must upload your file with the purpose `fine-tune`.

            See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.

        hyperparameters : typing.Optional[CreateFineTuningJobRequestHyperparameters]
            The hyperparameters used for the fine-tuning job.

        suffix : typing.Optional[str]
            A string of up to 18 characters that will be added to your fine-tuned model name.

            For example, a `suffix` of "custom-model-name" would produce a model name like `ft:gpt-3.5-turbo:openai:custom-model-name:7p4lURel`.

        validation_file : typing.Optional[str]
            The ID of an uploaded file that contains validation data.

            If you provide this file, the data is used to generate validation
            metrics periodically during fine-tuning. These metrics can be viewed in
            the fine-tuning results file.
            The same data should not be present in both train and validation files.

            Your dataset must be formatted as a JSONL file. You must upload your file with the purpose `fine-tune`.

            See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.

        integrations : typing.Optional[typing.Sequence[CreateFineTuningJobRequestIntegrationsItem]]
            A list of integrations to enable for your fine-tuning job.

        seed : typing.Optional[int]
            The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but may differ in rare cases.
            If a seed is not specified, one will be generated for you.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FineTuningJob]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "fine_tuning/jobs",
            method="POST",
            json={
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=CreateFineTuningJobRequestModel, direction="write"
                ),
                "training_file": training_file,
                "hyperparameters": convert_and_respect_annotation_metadata(
                    object_=hyperparameters, annotation=CreateFineTuningJobRequestHyperparameters, direction="write"
                ),
                "suffix": suffix,
                "validation_file": validation_file,
                "integrations": convert_and_respect_annotation_metadata(
                    object_=integrations,
                    annotation=typing.Optional[typing.Sequence[CreateFineTuningJobRequestIntegrationsItem]],
                    direction="write",
                ),
                "seed": seed,
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
                    FineTuningJob,
                    parse_obj_as(
                        type_=FineTuningJob,
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

    async def retrieve_fine_tuning_job(
        self, fine_tuning_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FineTuningJob]:
        """
        Parameters
        ----------
        fine_tuning_job_id : str
            The ID of the fine-tuning job.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FineTuningJob]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fine_tuning/jobs/{encode_path_param(fine_tuning_job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FineTuningJob,
                    parse_obj_as(
                        type_=FineTuningJob,
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

    async def list_fine_tuning_events(
        self,
        fine_tuning_job_id: str,
        *,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListFineTuningJobEventsResponse]:
        """
        Parameters
        ----------
        fine_tuning_job_id : str
            The ID of the fine-tuning job to get events for.

        after : typing.Optional[str]
            Identifier for the last event from the previous pagination request.

        limit : typing.Optional[int]
            Number of events to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListFineTuningJobEventsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fine_tuning/jobs/{encode_path_param(fine_tuning_job_id)}/events",
            method="GET",
            params={
                "after": after,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListFineTuningJobEventsResponse,
                    parse_obj_as(
                        type_=ListFineTuningJobEventsResponse,
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

    async def cancel_fine_tuning_job(
        self, fine_tuning_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FineTuningJob]:
        """
        Parameters
        ----------
        fine_tuning_job_id : str
            The ID of the fine-tuning job to cancel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FineTuningJob]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fine_tuning/jobs/{encode_path_param(fine_tuning_job_id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FineTuningJob,
                    parse_obj_as(
                        type_=FineTuningJob,
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

    async def list_fine_tuning_job_checkpoints(
        self,
        fine_tuning_job_id: str,
        *,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListFineTuningJobCheckpointsResponse]:
        """
        Parameters
        ----------
        fine_tuning_job_id : str
            The ID of the fine-tuning job to get checkpoints for.

        after : typing.Optional[str]
            Identifier for the last checkpoint ID from the previous pagination request.

        limit : typing.Optional[int]
            Number of checkpoints to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListFineTuningJobCheckpointsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fine_tuning/jobs/{encode_path_param(fine_tuning_job_id)}/checkpoints",
            method="GET",
            params={
                "after": after,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListFineTuningJobCheckpointsResponse,
                    parse_obj_as(
                        type_=ListFineTuningJobCheckpointsResponse,
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
