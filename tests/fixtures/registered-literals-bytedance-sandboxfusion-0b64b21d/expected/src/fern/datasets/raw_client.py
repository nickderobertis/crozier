

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.eval_result_input import EvalResultInput
from ..types.eval_result_output import EvalResultOutput
from ..types.get_metrics_function_result import GetMetricsFunctionResult
from ..types.http_validation_error import HttpValidationError
from ..types.prompt import Prompt
from ..types.test_config import TestConfig
from .types.get_prompt_by_id_request_id import GetPromptByIdRequestId
from .types.list_ids_list_ids_post_response_item import ListIdsListIdsPostResponseItem
from .types.submit_request_id import SubmitRequestId
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDatasetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_datasets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        List all registered datasets

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "list_datasets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def list_ids(
        self,
        *,
        dataset: str,
        config: TestConfig,
        offset: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ListIdsListIdsPostResponseItem]]:
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
        HttpResponse[typing.List[ListIdsListIdsPostResponseItem]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "list_ids",
            method="POST",
            json={
                "dataset": dataset,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=TestConfig, direction="write"
                ),
                "offset": offset,
                "limit": limit,
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
                    typing.List[ListIdsListIdsPostResponseItem],
                    parse_obj_as(
                        type_=typing.List[ListIdsListIdsPostResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_prompt(
        self,
        *,
        dataset: str,
        config: TestConfig,
        offset: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Prompt]]:
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
        HttpResponse[typing.List[Prompt]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "get_prompts",
            method="POST",
            json={
                "dataset": dataset,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=TestConfig, direction="write"
                ),
                "offset": offset,
                "limit": limit,
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
                    typing.List[Prompt],
                    parse_obj_as(
                        type_=typing.List[Prompt],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_prompt_by_id(
        self,
        *,
        dataset: str,
        config: TestConfig,
        id: GetPromptByIdRequestId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Prompt]:
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
        HttpResponse[Prompt]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "get_prompt_by_id",
            method="POST",
            json={
                "dataset": dataset,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=TestConfig, direction="write"
                ),
                "id": convert_and_respect_annotation_metadata(
                    object_=id, annotation=GetPromptByIdRequestId, direction="write"
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
                    Prompt,
                    parse_obj_as(
                        type_=Prompt,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def submit(
        self,
        *,
        dataset: str,
        id: SubmitRequestId,
        completion: str,
        config: TestConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EvalResultOutput]:
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
        HttpResponse[EvalResultOutput]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "submit",
            method="POST",
            json={
                "dataset": dataset,
                "id": convert_and_respect_annotation_metadata(
                    object_=id, annotation=SubmitRequestId, direction="write"
                ),
                "completion": completion,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=TestConfig, direction="write"
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
                    EvalResultOutput,
                    parse_obj_as(
                        type_=EvalResultOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_metrics(
        self,
        *,
        dataset: str,
        config: TestConfig,
        results: typing.Sequence[EvalResultInput],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
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
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "get_metrics",
            method="POST",
            json={
                "dataset": dataset,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=TestConfig, direction="write"
                ),
                "results": convert_and_respect_annotation_metadata(
                    object_=results, annotation=typing.Sequence[EvalResultInput], direction="write"
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_metrics_function(
        self, *, dataset: str, config: TestConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetMetricsFunctionResult]:
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
        HttpResponse[GetMetricsFunctionResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "get_metrics_function",
            method="POST",
            json={
                "dataset": dataset,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=TestConfig, direction="write"
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
                    GetMetricsFunctionResult,
                    parse_obj_as(
                        type_=GetMetricsFunctionResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawDatasetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_datasets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        List all registered datasets

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "list_datasets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def list_ids(
        self,
        *,
        dataset: str,
        config: TestConfig,
        offset: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ListIdsListIdsPostResponseItem]]:
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
        AsyncHttpResponse[typing.List[ListIdsListIdsPostResponseItem]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "list_ids",
            method="POST",
            json={
                "dataset": dataset,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=TestConfig, direction="write"
                ),
                "offset": offset,
                "limit": limit,
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
                    typing.List[ListIdsListIdsPostResponseItem],
                    parse_obj_as(
                        type_=typing.List[ListIdsListIdsPostResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_prompt(
        self,
        *,
        dataset: str,
        config: TestConfig,
        offset: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Prompt]]:
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
        AsyncHttpResponse[typing.List[Prompt]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "get_prompts",
            method="POST",
            json={
                "dataset": dataset,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=TestConfig, direction="write"
                ),
                "offset": offset,
                "limit": limit,
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
                    typing.List[Prompt],
                    parse_obj_as(
                        type_=typing.List[Prompt],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_prompt_by_id(
        self,
        *,
        dataset: str,
        config: TestConfig,
        id: GetPromptByIdRequestId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Prompt]:
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
        AsyncHttpResponse[Prompt]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "get_prompt_by_id",
            method="POST",
            json={
                "dataset": dataset,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=TestConfig, direction="write"
                ),
                "id": convert_and_respect_annotation_metadata(
                    object_=id, annotation=GetPromptByIdRequestId, direction="write"
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
                    Prompt,
                    parse_obj_as(
                        type_=Prompt,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def submit(
        self,
        *,
        dataset: str,
        id: SubmitRequestId,
        completion: str,
        config: TestConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EvalResultOutput]:
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
        AsyncHttpResponse[EvalResultOutput]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "submit",
            method="POST",
            json={
                "dataset": dataset,
                "id": convert_and_respect_annotation_metadata(
                    object_=id, annotation=SubmitRequestId, direction="write"
                ),
                "completion": completion,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=TestConfig, direction="write"
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
                    EvalResultOutput,
                    parse_obj_as(
                        type_=EvalResultOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_metrics(
        self,
        *,
        dataset: str,
        config: TestConfig,
        results: typing.Sequence[EvalResultInput],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
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
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "get_metrics",
            method="POST",
            json={
                "dataset": dataset,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=TestConfig, direction="write"
                ),
                "results": convert_and_respect_annotation_metadata(
                    object_=results, annotation=typing.Sequence[EvalResultInput], direction="write"
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_metrics_function(
        self, *, dataset: str, config: TestConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMetricsFunctionResult]:
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
        AsyncHttpResponse[GetMetricsFunctionResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "get_metrics_function",
            method="POST",
            json={
                "dataset": dataset,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=TestConfig, direction="write"
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
                    GetMetricsFunctionResult,
                    parse_obj_as(
                        type_=GetMetricsFunctionResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
