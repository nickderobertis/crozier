

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
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.error_response import ErrorResponse
from ..types.v2extract_options import V2ExtractOptions
from .types.v2extract_create_job_request_service_tier import V2ExtractCreateJobRequestServiceTier
from .types.v2extract_create_job_response import V2ExtractCreateJobResponse
from .types.v2extract_get_job_response import V2ExtractGetJobResponse
from .types.v2extract_list_jobs_response import V2ExtractListJobsResponse
from .types.v2extract_run_sync_response import V2ExtractRunSyncResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawExtractClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def v2extract_run_sync(
        self,
        *,
        schema: typing.Dict[str, typing.Any],
        markdown: typing.Optional[str] = OMIT,
        markdown_url: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        options: typing.Optional[V2ExtractOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2ExtractRunSyncResponse]:
        """
        Extract structured data from a Markdown document according to a JSON schema, with character-span grounding into the source Markdown. Runs synchronously and returns the result inline.

        Parameters
        ----------
        schema : typing.Dict[str, typing.Any]
            JSON Schema describing the fields to extract. The schema must be an object type with a ``properties`` map of field names to their types and descriptions.

        markdown : typing.Optional[str]
            Markdown string to extract from, or a multipart FILE part carrying the markdown (large inputs — uploads are staged by the gateway). Can come from any source — LandingAI parse output, a third-party parser, or hand-authored text. When the markdown was produced by ``POST /v2/parse``, it ends with a ``<!-- doc_id=<id> -->`` comment that the service reads automatically and echoes as ``metadata.doc_id``.

        markdown_url : typing.Optional[str]
            URL to fetch the markdown from. Must be a public http(s) URL; private/loopback IPs are rejected at submit time.

        model : typing.Optional[str]
            The version of the model to use for extraction. Use ``extract-latest`` to use the latest version.

        options : typing.Optional[V2ExtractOptions]
            Extraction options (``strict``). Omit for defaults.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V2ExtractRunSyncResponse]
            v2-extract result
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/extract",
            method="POST",
            json={
                "schema": schema,
                "markdown": markdown,
                "markdown_url": markdown_url,
                "model": model,
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=typing.Optional[V2ExtractOptions], direction="write"
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
                    V2ExtractRunSyncResponse,
                    parse_obj_as(
                        type_=V2ExtractRunSyncResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def v2extract_list_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2ExtractListJobsResponse]:
        """
        List your Extract jobs, newest first.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (0-indexed).

        page_size : typing.Optional[int]
            Number of items per page.

        status : typing.Optional[str]
            Filter by job status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V2ExtractListJobsResponse]
            The caller's jobs, newest first
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/extract/jobs",
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2ExtractListJobsResponse,
                    parse_obj_as(
                        type_=V2ExtractListJobsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def v2extract_create_job(
        self,
        *,
        schema: typing.Dict[str, typing.Any],
        markdown: typing.Optional[str] = OMIT,
        markdown_url: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        options: typing.Optional[V2ExtractOptions] = OMIT,
        output_save_url: typing.Optional[str] = OMIT,
        service_tier: typing.Optional[V2ExtractCreateJobRequestServiceTier] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2ExtractCreateJobResponse]:
        """
        Extract structured data from a Markdown document according to a JSON schema, with character-span grounding into the source Markdown. Runs asynchronously and returns a job ID; use it to poll for status and retrieve the result once processing completes.

        Parameters
        ----------
        schema : typing.Dict[str, typing.Any]
            JSON Schema describing the fields to extract. The schema must be an object type with a ``properties`` map of field names to their types and descriptions.

        markdown : typing.Optional[str]
            Markdown string to extract from, or a multipart FILE part carrying the markdown (large inputs — uploads are staged by the gateway). Can come from any source — LandingAI parse output, a third-party parser, or hand-authored text. When the markdown was produced by ``POST /v2/parse``, it ends with a ``<!-- doc_id=<id> -->`` comment that the service reads automatically and echoes as ``metadata.doc_id``.

        markdown_url : typing.Optional[str]
            URL to fetch the markdown from. Must be a public http(s) URL; private/loopback IPs are rejected at submit time.

        model : typing.Optional[str]
            The version of the model to use for extraction. Use ``extract-latest`` to use the latest version.

        options : typing.Optional[V2ExtractOptions]
            Extraction options (``strict``). Omit for defaults.

        output_save_url : typing.Optional[str]
            URL to save the result to — e.g. a presigned S3 PUT URL. Async jobs only. When set, the finished result is delivered (HTTP PUT) to this URL and the completed job reports ``output_url`` instead of an inline ``result``. Must be a public http(s) URL; private/loopback IPs are rejected at submit time.

        service_tier : typing.Optional[V2ExtractCreateJobRequestServiceTier]
            Async service tier. ``priority`` runs in the fast lane at the sync billing rate; absent → ``standard``.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V2ExtractCreateJobResponse]
            Job created
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/extract/jobs",
            method="POST",
            json={
                "schema": schema,
                "markdown": markdown,
                "markdown_url": markdown_url,
                "model": model,
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=typing.Optional[V2ExtractOptions], direction="write"
                ),
                "output_save_url": output_save_url,
                "service_tier": service_tier,
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
                    V2ExtractCreateJobResponse,
                    parse_obj_as(
                        type_=V2ExtractCreateJobResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def v2extract_get_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V2ExtractGetJobResponse]:
        """
        Get the status of an async Extract job, including its result once the job has completed.

        Parameters
        ----------
        job_id : str
            The identifier of the job to retrieve, as returned by the create-job request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V2ExtractGetJobResponse]
            Job status / result
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/extract/jobs/{encode_path_param(job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2ExtractGetJobResponse,
                    parse_obj_as(
                        type_=V2ExtractGetJobResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawExtractClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def v2extract_run_sync(
        self,
        *,
        schema: typing.Dict[str, typing.Any],
        markdown: typing.Optional[str] = OMIT,
        markdown_url: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        options: typing.Optional[V2ExtractOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2ExtractRunSyncResponse]:
        """
        Extract structured data from a Markdown document according to a JSON schema, with character-span grounding into the source Markdown. Runs synchronously and returns the result inline.

        Parameters
        ----------
        schema : typing.Dict[str, typing.Any]
            JSON Schema describing the fields to extract. The schema must be an object type with a ``properties`` map of field names to their types and descriptions.

        markdown : typing.Optional[str]
            Markdown string to extract from, or a multipart FILE part carrying the markdown (large inputs — uploads are staged by the gateway). Can come from any source — LandingAI parse output, a third-party parser, or hand-authored text. When the markdown was produced by ``POST /v2/parse``, it ends with a ``<!-- doc_id=<id> -->`` comment that the service reads automatically and echoes as ``metadata.doc_id``.

        markdown_url : typing.Optional[str]
            URL to fetch the markdown from. Must be a public http(s) URL; private/loopback IPs are rejected at submit time.

        model : typing.Optional[str]
            The version of the model to use for extraction. Use ``extract-latest`` to use the latest version.

        options : typing.Optional[V2ExtractOptions]
            Extraction options (``strict``). Omit for defaults.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V2ExtractRunSyncResponse]
            v2-extract result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/extract",
            method="POST",
            json={
                "schema": schema,
                "markdown": markdown,
                "markdown_url": markdown_url,
                "model": model,
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=typing.Optional[V2ExtractOptions], direction="write"
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
                    V2ExtractRunSyncResponse,
                    parse_obj_as(
                        type_=V2ExtractRunSyncResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def v2extract_list_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2ExtractListJobsResponse]:
        """
        List your Extract jobs, newest first.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (0-indexed).

        page_size : typing.Optional[int]
            Number of items per page.

        status : typing.Optional[str]
            Filter by job status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V2ExtractListJobsResponse]
            The caller's jobs, newest first
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/extract/jobs",
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2ExtractListJobsResponse,
                    parse_obj_as(
                        type_=V2ExtractListJobsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def v2extract_create_job(
        self,
        *,
        schema: typing.Dict[str, typing.Any],
        markdown: typing.Optional[str] = OMIT,
        markdown_url: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        options: typing.Optional[V2ExtractOptions] = OMIT,
        output_save_url: typing.Optional[str] = OMIT,
        service_tier: typing.Optional[V2ExtractCreateJobRequestServiceTier] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2ExtractCreateJobResponse]:
        """
        Extract structured data from a Markdown document according to a JSON schema, with character-span grounding into the source Markdown. Runs asynchronously and returns a job ID; use it to poll for status and retrieve the result once processing completes.

        Parameters
        ----------
        schema : typing.Dict[str, typing.Any]
            JSON Schema describing the fields to extract. The schema must be an object type with a ``properties`` map of field names to their types and descriptions.

        markdown : typing.Optional[str]
            Markdown string to extract from, or a multipart FILE part carrying the markdown (large inputs — uploads are staged by the gateway). Can come from any source — LandingAI parse output, a third-party parser, or hand-authored text. When the markdown was produced by ``POST /v2/parse``, it ends with a ``<!-- doc_id=<id> -->`` comment that the service reads automatically and echoes as ``metadata.doc_id``.

        markdown_url : typing.Optional[str]
            URL to fetch the markdown from. Must be a public http(s) URL; private/loopback IPs are rejected at submit time.

        model : typing.Optional[str]
            The version of the model to use for extraction. Use ``extract-latest`` to use the latest version.

        options : typing.Optional[V2ExtractOptions]
            Extraction options (``strict``). Omit for defaults.

        output_save_url : typing.Optional[str]
            URL to save the result to — e.g. a presigned S3 PUT URL. Async jobs only. When set, the finished result is delivered (HTTP PUT) to this URL and the completed job reports ``output_url`` instead of an inline ``result``. Must be a public http(s) URL; private/loopback IPs are rejected at submit time.

        service_tier : typing.Optional[V2ExtractCreateJobRequestServiceTier]
            Async service tier. ``priority`` runs in the fast lane at the sync billing rate; absent → ``standard``.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V2ExtractCreateJobResponse]
            Job created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/extract/jobs",
            method="POST",
            json={
                "schema": schema,
                "markdown": markdown,
                "markdown_url": markdown_url,
                "model": model,
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=typing.Optional[V2ExtractOptions], direction="write"
                ),
                "output_save_url": output_save_url,
                "service_tier": service_tier,
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
                    V2ExtractCreateJobResponse,
                    parse_obj_as(
                        type_=V2ExtractCreateJobResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def v2extract_get_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V2ExtractGetJobResponse]:
        """
        Get the status of an async Extract job, including its result once the job has completed.

        Parameters
        ----------
        job_id : str
            The identifier of the job to retrieve, as returned by the create-job request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V2ExtractGetJobResponse]
            Job status / result
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/extract/jobs/{encode_path_param(job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2ExtractGetJobResponse,
                    parse_obj_as(
                        type_=V2ExtractGetJobResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
