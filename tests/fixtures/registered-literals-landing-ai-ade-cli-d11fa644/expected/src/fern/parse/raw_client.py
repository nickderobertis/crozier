

import json
import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param, jsonable_encoder
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.error_response import ErrorResponse
from ..types.parse_response import ParseResponse
from .types.parse_create_job_request_options import ParseCreateJobRequestOptions
from .types.parse_create_job_request_service_tier import ParseCreateJobRequestServiceTier
from .types.parse_create_job_response import ParseCreateJobResponse
from .types.parse_get_job_response import ParseGetJobResponse
from .types.parse_list_jobs_response import ParseListJobsResponse
from .types.parse_run_sync_request_options import ParseRunSyncRequestOptions
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawParseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def run_sync(
        self,
        *,
        document: typing.Optional[core.File] = OMIT,
        document_url: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        options: typing.Optional[ParseRunSyncRequestOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ParseResponse]:
        """
        Parse a document and return the parse response inline.

        Parameters
        ----------
        document : typing.Optional[core.File]
            See core.File for more documentation

        document_url : typing.Optional[str]
            A publicly accessible URL to the file to parse. The file must be a PDF or image; see the list of [supported file types](https://docs.landing.ai/dpt3/file-types). Provide either `document` or `document_url`, not both.

        model : typing.Optional[str]
            The DPT-3 model snapshot to use for this request. Accepts a dated snapshot (for example, `dpt-3-pro-20260710`), the `dpt-3-pro-latest` alias, or the bare `dpt-3-pro` family name (equivalent to `dpt-3-pro-latest`). Defaults to the latest DPT-3 Pro snapshot.

        options : typing.Optional[ParseRunSyncRequestOptions]
            Optional object that customizes the parse. Use it to select which pages to process, adjust how content appears in the Markdown, or control how much detail the response includes. Sent as a JSON-serialized string in form data.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ParseResponse]
            The parse response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/parse",
            method="POST",
            data={
                "document_url": document_url,
                "model": model,
                "options": json.dumps(jsonable_encoder(options)) if options is not OMIT else OMIT,
            },
            files={
                **({"document": document} if document is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParseResponse,
                    parse_obj_as(
                        type_=ParseResponse,
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

    def list_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ParseListJobsResponse]:
        """
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
        HttpResponse[ParseListJobsResponse]
            The caller's jobs, newest first
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/parse/jobs",
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
                    ParseListJobsResponse,
                    parse_obj_as(
                        type_=ParseListJobsResponse,
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

    def create_job(
        self,
        *,
        document: typing.Optional[core.File] = OMIT,
        document_url: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        options: typing.Optional[ParseCreateJobRequestOptions] = OMIT,
        output_save_url: typing.Optional[str] = OMIT,
        service_tier: typing.Optional[ParseCreateJobRequestServiceTier] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ParseCreateJobResponse]:
        """
        Parse a document asynchronously. Returns a job ID; use it to poll for the job's status and retrieve the parse result once processing completes.

        Parameters
        ----------
        document : typing.Optional[core.File]
            See core.File for more documentation

        document_url : typing.Optional[str]
            A publicly accessible URL to the file to parse. The file must be a PDF or image; see the list of [supported file types](https://docs.landing.ai/dpt3/file-types). Provide either `document` or `document_url`, not both.

        model : typing.Optional[str]
            The DPT-3 model snapshot to use for this request. Accepts a dated snapshot (for example, `dpt-3-pro-20260710`), the `dpt-3-pro-latest` alias, or the bare `dpt-3-pro` family name (equivalent to `dpt-3-pro-latest`). Defaults to the latest DPT-3 Pro snapshot.

        options : typing.Optional[ParseCreateJobRequestOptions]
            Optional object that customizes the parse. Use it to select which pages to process, adjust how content appears in the Markdown, or control how much detail the response includes. Sent as a JSON-serialized string in form data.

        output_save_url : typing.Optional[str]
            Public URL the full response is delivered to; the API response then carries ``output_url`` instead of inline data.

        service_tier : typing.Optional[ParseCreateJobRequestServiceTier]
            Async service tier (``POST /jobs`` only). ``priority`` runs in the fast lane at the sync billing rate; absent → ``standard``.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ParseCreateJobResponse]
            Job created
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/parse/jobs",
            method="POST",
            data={
                "document_url": document_url,
                "model": model,
                "options": json.dumps(jsonable_encoder(options)) if options is not OMIT else OMIT,
                "output_save_url": output_save_url,
                "service_tier": service_tier,
            },
            files={
                **({"document": document} if document is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParseCreateJobResponse,
                    parse_obj_as(
                        type_=ParseCreateJobResponse,
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

    def get_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ParseGetJobResponse]:
        """
        Get the status of an async parse job. Once the job has ``completed``, ``result`` carries the parse response (or ``output_url`` when ``output_save_url`` was set). Partial success (some pages failed) is reported in ``result.metadata.failed_pages``.

        Parameters
        ----------
        job_id : str
            The identifier of the job to retrieve, as returned by the create-job request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ParseGetJobResponse]
            Job status / result
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/parse/jobs/{encode_path_param(job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParseGetJobResponse,
                    parse_obj_as(
                        type_=ParseGetJobResponse,
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


class AsyncRawParseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def run_sync(
        self,
        *,
        document: typing.Optional[core.File] = OMIT,
        document_url: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        options: typing.Optional[ParseRunSyncRequestOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ParseResponse]:
        """
        Parse a document and return the parse response inline.

        Parameters
        ----------
        document : typing.Optional[core.File]
            See core.File for more documentation

        document_url : typing.Optional[str]
            A publicly accessible URL to the file to parse. The file must be a PDF or image; see the list of [supported file types](https://docs.landing.ai/dpt3/file-types). Provide either `document` or `document_url`, not both.

        model : typing.Optional[str]
            The DPT-3 model snapshot to use for this request. Accepts a dated snapshot (for example, `dpt-3-pro-20260710`), the `dpt-3-pro-latest` alias, or the bare `dpt-3-pro` family name (equivalent to `dpt-3-pro-latest`). Defaults to the latest DPT-3 Pro snapshot.

        options : typing.Optional[ParseRunSyncRequestOptions]
            Optional object that customizes the parse. Use it to select which pages to process, adjust how content appears in the Markdown, or control how much detail the response includes. Sent as a JSON-serialized string in form data.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ParseResponse]
            The parse response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/parse",
            method="POST",
            data={
                "document_url": document_url,
                "model": model,
                "options": json.dumps(jsonable_encoder(options)) if options is not OMIT else OMIT,
            },
            files={
                **({"document": document} if document is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParseResponse,
                    parse_obj_as(
                        type_=ParseResponse,
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

    async def list_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ParseListJobsResponse]:
        """
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
        AsyncHttpResponse[ParseListJobsResponse]
            The caller's jobs, newest first
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/parse/jobs",
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
                    ParseListJobsResponse,
                    parse_obj_as(
                        type_=ParseListJobsResponse,
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

    async def create_job(
        self,
        *,
        document: typing.Optional[core.File] = OMIT,
        document_url: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        options: typing.Optional[ParseCreateJobRequestOptions] = OMIT,
        output_save_url: typing.Optional[str] = OMIT,
        service_tier: typing.Optional[ParseCreateJobRequestServiceTier] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ParseCreateJobResponse]:
        """
        Parse a document asynchronously. Returns a job ID; use it to poll for the job's status and retrieve the parse result once processing completes.

        Parameters
        ----------
        document : typing.Optional[core.File]
            See core.File for more documentation

        document_url : typing.Optional[str]
            A publicly accessible URL to the file to parse. The file must be a PDF or image; see the list of [supported file types](https://docs.landing.ai/dpt3/file-types). Provide either `document` or `document_url`, not both.

        model : typing.Optional[str]
            The DPT-3 model snapshot to use for this request. Accepts a dated snapshot (for example, `dpt-3-pro-20260710`), the `dpt-3-pro-latest` alias, or the bare `dpt-3-pro` family name (equivalent to `dpt-3-pro-latest`). Defaults to the latest DPT-3 Pro snapshot.

        options : typing.Optional[ParseCreateJobRequestOptions]
            Optional object that customizes the parse. Use it to select which pages to process, adjust how content appears in the Markdown, or control how much detail the response includes. Sent as a JSON-serialized string in form data.

        output_save_url : typing.Optional[str]
            Public URL the full response is delivered to; the API response then carries ``output_url`` instead of inline data.

        service_tier : typing.Optional[ParseCreateJobRequestServiceTier]
            Async service tier (``POST /jobs`` only). ``priority`` runs in the fast lane at the sync billing rate; absent → ``standard``.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ParseCreateJobResponse]
            Job created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/parse/jobs",
            method="POST",
            data={
                "document_url": document_url,
                "model": model,
                "options": json.dumps(jsonable_encoder(options)) if options is not OMIT else OMIT,
                "output_save_url": output_save_url,
                "service_tier": service_tier,
            },
            files={
                **({"document": document} if document is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParseCreateJobResponse,
                    parse_obj_as(
                        type_=ParseCreateJobResponse,
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

    async def get_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ParseGetJobResponse]:
        """
        Get the status of an async parse job. Once the job has ``completed``, ``result`` carries the parse response (or ``output_url`` when ``output_save_url`` was set). Partial success (some pages failed) is reported in ``result.metadata.failed_pages``.

        Parameters
        ----------
        job_id : str
            The identifier of the job to retrieve, as returned by the create-job request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ParseGetJobResponse]
            Job status / result
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/parse/jobs/{encode_path_param(job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParseGetJobResponse,
                    parse_obj_as(
                        type_=ParseGetJobResponse,
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
