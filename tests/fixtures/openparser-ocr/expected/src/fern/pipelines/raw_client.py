

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
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.delete_extraction_pipeline_response import DeleteExtractionPipelineResponse
from ..types.error_response import ErrorResponse
from ..types.extraction_pipeline import ExtractionPipeline
from ..types.extraction_pipeline_id import ExtractionPipelineId
from ..types.extraction_pipeline_list_response import ExtractionPipelineListResponse
from .types.create_extraction_pipeline_request_grounding import CreateExtractionPipelineRequestGrounding
from .types.create_extraction_pipeline_request_llm_options import CreateExtractionPipelineRequestLlmOptions
from .types.update_extraction_pipeline_request_grounding import UpdateExtractionPipelineRequestGrounding
from .types.update_extraction_pipeline_request_llm_options import UpdateExtractionPipelineRequestLlmOptions
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPipelinesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_extraction_pipelines(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ExtractionPipelineListResponse]:
        """
        Return active (non-deleted) pipelines for the authenticated tenant, newest updates first.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExtractionPipelineListResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "pipelines",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtractionPipelineListResponse,
                    parse_obj_as(
                        type_=ExtractionPipelineListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def create_extraction_pipeline(
        self,
        *,
        name: str,
        ocr_model: str,
        llm_model: str,
        schema: typing.Dict[str, typing.Any],
        slug: typing.Optional[str] = OMIT,
        ocr_options: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        llm_options: typing.Optional[CreateExtractionPipelineRequestLlmOptions] = OMIT,
        repair_attempts: typing.Optional[int] = OMIT,
        grounding: typing.Optional[CreateExtractionPipelineRequestGrounding] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExtractionPipeline]:
        """
        Persist a tenant-scoped extraction configuration (OCR model, LLM model, schema,
        repair/grounding/reasoning). Validated with the same admission gates as extract.
        Playground tokens and `ocr:full` keys are both accepted.

        Parameters
        ----------
        name : str

        ocr_model : str

        llm_model : str

        schema : typing.Dict[str, typing.Any]
            JSON Schema object describing fields to extract. Root must be an object schema with
            explicit `properties` and at least one named property. Admission applies the same
            strict structured-output normalization as extract.

        slug : typing.Optional[str]

        ocr_options : typing.Optional[typing.Dict[str, typing.Any]]

        llm_options : typing.Optional[CreateExtractionPipelineRequestLlmOptions]

        repair_attempts : typing.Optional[int]

        grounding : typing.Optional[CreateExtractionPipelineRequestGrounding]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExtractionPipeline]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "pipelines",
            method="POST",
            json={
                "name": name,
                "slug": slug,
                "ocr_model": ocr_model,
                "ocr_options": ocr_options,
                "llm_model": llm_model,
                "llm_options": convert_and_respect_annotation_metadata(
                    object_=llm_options, annotation=CreateExtractionPipelineRequestLlmOptions, direction="write"
                ),
                "schema": schema,
                "repair_attempts": repair_attempts,
                "grounding": grounding,
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
                    ExtractionPipeline,
                    parse_obj_as(
                        type_=ExtractionPipeline,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_extraction_pipeline(
        self, id: ExtractionPipelineId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ExtractionPipeline]:
        """
        Return one active pipeline. Missing, deleted, and cross-tenant ids return
        `404 pipeline_not_found`.

        Parameters
        ----------
        id : ExtractionPipelineId
            Tenant-scoped saved extraction pipeline identifier (`oppl_…`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExtractionPipeline]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtractionPipeline,
                    parse_obj_as(
                        type_=ExtractionPipeline,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def delete_extraction_pipeline(
        self, id: ExtractionPipelineId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteExtractionPipelineResponse]:
        """
        Marks the pipeline deleted. Subsequent extract admits with that id return
        `404 pipeline_not_found`. Historical jobs retain snapshotted config.

        Parameters
        ----------
        id : ExtractionPipelineId
            Tenant-scoped saved extraction pipeline identifier (`oppl_…`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteExtractionPipelineResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteExtractionPipelineResponse,
                    parse_obj_as(
                        type_=DeleteExtractionPipelineResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def update_extraction_pipeline(
        self,
        id: ExtractionPipelineId,
        *,
        name: typing.Optional[str] = OMIT,
        slug: typing.Optional[str] = OMIT,
        ocr_model: typing.Optional[str] = OMIT,
        ocr_options: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        llm_model: typing.Optional[str] = OMIT,
        llm_options: typing.Optional[UpdateExtractionPipelineRequestLlmOptions] = OMIT,
        schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        repair_attempts: typing.Optional[int] = OMIT,
        grounding: typing.Optional[UpdateExtractionPipelineRequestGrounding] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExtractionPipeline]:
        """
        Patch one or more fields, re-validate the effective merged config, and atomically
        increment `version`. In-flight and completed jobs keep their admit-time snapshots.

        Parameters
        ----------
        id : ExtractionPipelineId
            Tenant-scoped saved extraction pipeline identifier (`oppl_…`).

        name : typing.Optional[str]

        slug : typing.Optional[str]

        ocr_model : typing.Optional[str]

        ocr_options : typing.Optional[typing.Dict[str, typing.Any]]

        llm_model : typing.Optional[str]

        llm_options : typing.Optional[UpdateExtractionPipelineRequestLlmOptions]

        schema : typing.Optional[typing.Dict[str, typing.Any]]
            Replacement extraction schema. Root must be an object schema with explicit `properties`
            and at least one named property. Merged pipeline config is re-validated on every update.

        repair_attempts : typing.Optional[int]

        grounding : typing.Optional[UpdateExtractionPipelineRequestGrounding]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExtractionPipeline]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}",
            method="PATCH",
            json={
                "name": name,
                "slug": slug,
                "ocr_model": ocr_model,
                "ocr_options": ocr_options,
                "llm_model": llm_model,
                "llm_options": convert_and_respect_annotation_metadata(
                    object_=llm_options,
                    annotation=typing.Optional[UpdateExtractionPipelineRequestLlmOptions],
                    direction="write",
                ),
                "schema": schema,
                "repair_attempts": repair_attempts,
                "grounding": grounding,
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
                    ExtractionPipeline,
                    parse_obj_as(
                        type_=ExtractionPipeline,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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


class AsyncRawPipelinesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_extraction_pipelines(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ExtractionPipelineListResponse]:
        """
        Return active (non-deleted) pipelines for the authenticated tenant, newest updates first.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExtractionPipelineListResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pipelines",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtractionPipelineListResponse,
                    parse_obj_as(
                        type_=ExtractionPipelineListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def create_extraction_pipeline(
        self,
        *,
        name: str,
        ocr_model: str,
        llm_model: str,
        schema: typing.Dict[str, typing.Any],
        slug: typing.Optional[str] = OMIT,
        ocr_options: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        llm_options: typing.Optional[CreateExtractionPipelineRequestLlmOptions] = OMIT,
        repair_attempts: typing.Optional[int] = OMIT,
        grounding: typing.Optional[CreateExtractionPipelineRequestGrounding] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExtractionPipeline]:
        """
        Persist a tenant-scoped extraction configuration (OCR model, LLM model, schema,
        repair/grounding/reasoning). Validated with the same admission gates as extract.
        Playground tokens and `ocr:full` keys are both accepted.

        Parameters
        ----------
        name : str

        ocr_model : str

        llm_model : str

        schema : typing.Dict[str, typing.Any]
            JSON Schema object describing fields to extract. Root must be an object schema with
            explicit `properties` and at least one named property. Admission applies the same
            strict structured-output normalization as extract.

        slug : typing.Optional[str]

        ocr_options : typing.Optional[typing.Dict[str, typing.Any]]

        llm_options : typing.Optional[CreateExtractionPipelineRequestLlmOptions]

        repair_attempts : typing.Optional[int]

        grounding : typing.Optional[CreateExtractionPipelineRequestGrounding]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExtractionPipeline]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pipelines",
            method="POST",
            json={
                "name": name,
                "slug": slug,
                "ocr_model": ocr_model,
                "ocr_options": ocr_options,
                "llm_model": llm_model,
                "llm_options": convert_and_respect_annotation_metadata(
                    object_=llm_options, annotation=CreateExtractionPipelineRequestLlmOptions, direction="write"
                ),
                "schema": schema,
                "repair_attempts": repair_attempts,
                "grounding": grounding,
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
                    ExtractionPipeline,
                    parse_obj_as(
                        type_=ExtractionPipeline,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_extraction_pipeline(
        self, id: ExtractionPipelineId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ExtractionPipeline]:
        """
        Return one active pipeline. Missing, deleted, and cross-tenant ids return
        `404 pipeline_not_found`.

        Parameters
        ----------
        id : ExtractionPipelineId
            Tenant-scoped saved extraction pipeline identifier (`oppl_…`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExtractionPipeline]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtractionPipeline,
                    parse_obj_as(
                        type_=ExtractionPipeline,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def delete_extraction_pipeline(
        self, id: ExtractionPipelineId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteExtractionPipelineResponse]:
        """
        Marks the pipeline deleted. Subsequent extract admits with that id return
        `404 pipeline_not_found`. Historical jobs retain snapshotted config.

        Parameters
        ----------
        id : ExtractionPipelineId
            Tenant-scoped saved extraction pipeline identifier (`oppl_…`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteExtractionPipelineResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteExtractionPipelineResponse,
                    parse_obj_as(
                        type_=DeleteExtractionPipelineResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def update_extraction_pipeline(
        self,
        id: ExtractionPipelineId,
        *,
        name: typing.Optional[str] = OMIT,
        slug: typing.Optional[str] = OMIT,
        ocr_model: typing.Optional[str] = OMIT,
        ocr_options: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        llm_model: typing.Optional[str] = OMIT,
        llm_options: typing.Optional[UpdateExtractionPipelineRequestLlmOptions] = OMIT,
        schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        repair_attempts: typing.Optional[int] = OMIT,
        grounding: typing.Optional[UpdateExtractionPipelineRequestGrounding] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExtractionPipeline]:
        """
        Patch one or more fields, re-validate the effective merged config, and atomically
        increment `version`. In-flight and completed jobs keep their admit-time snapshots.

        Parameters
        ----------
        id : ExtractionPipelineId
            Tenant-scoped saved extraction pipeline identifier (`oppl_…`).

        name : typing.Optional[str]

        slug : typing.Optional[str]

        ocr_model : typing.Optional[str]

        ocr_options : typing.Optional[typing.Dict[str, typing.Any]]

        llm_model : typing.Optional[str]

        llm_options : typing.Optional[UpdateExtractionPipelineRequestLlmOptions]

        schema : typing.Optional[typing.Dict[str, typing.Any]]
            Replacement extraction schema. Root must be an object schema with explicit `properties`
            and at least one named property. Merged pipeline config is re-validated on every update.

        repair_attempts : typing.Optional[int]

        grounding : typing.Optional[UpdateExtractionPipelineRequestGrounding]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExtractionPipeline]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}",
            method="PATCH",
            json={
                "name": name,
                "slug": slug,
                "ocr_model": ocr_model,
                "ocr_options": ocr_options,
                "llm_model": llm_model,
                "llm_options": convert_and_respect_annotation_metadata(
                    object_=llm_options,
                    annotation=typing.Optional[UpdateExtractionPipelineRequestLlmOptions],
                    direction="write",
                ),
                "schema": schema,
                "repair_attempts": repair_attempts,
                "grounding": grounding,
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
                    ExtractionPipeline,
                    parse_obj_as(
                        type_=ExtractionPipeline,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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
