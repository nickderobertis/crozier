

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.error_response import ErrorResponse
from .types.v2ground_create_job_response import V2GroundCreateJobResponse
from .types.v2ground_get_job_response import V2GroundGetJobResponse
from .types.v2ground_list_jobs_response import V2GroundListJobsResponse
from .types.v2ground_run_sync_response import V2GroundRunSyncResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawGroundClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def v2ground_run_sync(
        self,
        *,
        extraction_metadata: typing.Dict[str, typing.Any],
        structure: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2GroundRunSyncResponse]:
        """
        Map extracted fields to the document blocks they were quoted from. Takes the extraction_metadata from an extract call and the structure tree from the parse call the markdown came from, and returns, for every extracted field, the overlapping blocks with their ids, page numbers, and bounding boxes. Runs synchronously and returns the result inline.

        Parameters
        ----------
        extraction_metadata : typing.Dict[str, typing.Any]
            The ``extraction_metadata`` object returned by ``POST /v2/extract`` (or the pipeline's extract step): a tree mirroring your extraction schema whose leaves are ``{value, ranges}`` objects, where ``ranges`` are ``{start, end}`` Unicode code point offsets into the parse markdown.

        structure : typing.Dict[str, typing.Any]
            The ``structure`` tree from the parse response the extraction was produced from. Every block in the tree carries its ``grounding`` (``{page, range, box}``) inline; block ids in the response resolve against this exact tree.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V2GroundRunSyncResponse]
            v2-ground result
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/ground",
            method="POST",
            json={
                "extraction_metadata": extraction_metadata,
                "structure": structure,
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
                    V2GroundRunSyncResponse,
                    parse_obj_as(
                        type_=V2GroundRunSyncResponse,
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

    def v2ground_list_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2GroundListJobsResponse]:
        """
        List your Ground jobs, newest first.

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
        HttpResponse[V2GroundListJobsResponse]
            The caller's jobs, newest first
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/ground/jobs",
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
                    V2GroundListJobsResponse,
                    parse_obj_as(
                        type_=V2GroundListJobsResponse,
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

    def v2ground_create_job(
        self,
        *,
        extraction_metadata: typing.Dict[str, typing.Any],
        structure: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V2GroundCreateJobResponse]:
        """
        Map extracted fields to the document blocks they were quoted from. Takes the extraction_metadata from an extract call and the structure tree from the parse call the markdown came from, and returns, for every extracted field, the overlapping blocks with their ids, page numbers, and bounding boxes. Runs asynchronously and returns a job ID; use it to poll for status and retrieve the result once processing completes.

        Parameters
        ----------
        extraction_metadata : typing.Dict[str, typing.Any]
            The ``extraction_metadata`` object returned by ``POST /v2/extract`` (or the pipeline's extract step): a tree mirroring your extraction schema whose leaves are ``{value, ranges}`` objects, where ``ranges`` are ``{start, end}`` Unicode code point offsets into the parse markdown.

        structure : typing.Dict[str, typing.Any]
            The ``structure`` tree from the parse response the extraction was produced from. Every block in the tree carries its ``grounding`` (``{page, range, box}``) inline; block ids in the response resolve against this exact tree.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V2GroundCreateJobResponse]
            Job created
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/ground/jobs",
            method="POST",
            json={
                "extraction_metadata": extraction_metadata,
                "structure": structure,
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
                    V2GroundCreateJobResponse,
                    parse_obj_as(
                        type_=V2GroundCreateJobResponse,
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

    def v2ground_get_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V2GroundGetJobResponse]:
        """
        Get the status of an async Ground job, including its result once the job has completed.

        Parameters
        ----------
        job_id : str
            The identifier of the job to retrieve, as returned by the create-job request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V2GroundGetJobResponse]
            Job status / result
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/ground/jobs/{encode_path_param(job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2GroundGetJobResponse,
                    parse_obj_as(
                        type_=V2GroundGetJobResponse,
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


class AsyncRawGroundClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def v2ground_run_sync(
        self,
        *,
        extraction_metadata: typing.Dict[str, typing.Any],
        structure: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2GroundRunSyncResponse]:
        """
        Map extracted fields to the document blocks they were quoted from. Takes the extraction_metadata from an extract call and the structure tree from the parse call the markdown came from, and returns, for every extracted field, the overlapping blocks with their ids, page numbers, and bounding boxes. Runs synchronously and returns the result inline.

        Parameters
        ----------
        extraction_metadata : typing.Dict[str, typing.Any]
            The ``extraction_metadata`` object returned by ``POST /v2/extract`` (or the pipeline's extract step): a tree mirroring your extraction schema whose leaves are ``{value, ranges}`` objects, where ``ranges`` are ``{start, end}`` Unicode code point offsets into the parse markdown.

        structure : typing.Dict[str, typing.Any]
            The ``structure`` tree from the parse response the extraction was produced from. Every block in the tree carries its ``grounding`` (``{page, range, box}``) inline; block ids in the response resolve against this exact tree.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V2GroundRunSyncResponse]
            v2-ground result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/ground",
            method="POST",
            json={
                "extraction_metadata": extraction_metadata,
                "structure": structure,
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
                    V2GroundRunSyncResponse,
                    parse_obj_as(
                        type_=V2GroundRunSyncResponse,
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

    async def v2ground_list_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2GroundListJobsResponse]:
        """
        List your Ground jobs, newest first.

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
        AsyncHttpResponse[V2GroundListJobsResponse]
            The caller's jobs, newest first
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/ground/jobs",
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
                    V2GroundListJobsResponse,
                    parse_obj_as(
                        type_=V2GroundListJobsResponse,
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

    async def v2ground_create_job(
        self,
        *,
        extraction_metadata: typing.Dict[str, typing.Any],
        structure: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V2GroundCreateJobResponse]:
        """
        Map extracted fields to the document blocks they were quoted from. Takes the extraction_metadata from an extract call and the structure tree from the parse call the markdown came from, and returns, for every extracted field, the overlapping blocks with their ids, page numbers, and bounding boxes. Runs asynchronously and returns a job ID; use it to poll for status and retrieve the result once processing completes.

        Parameters
        ----------
        extraction_metadata : typing.Dict[str, typing.Any]
            The ``extraction_metadata`` object returned by ``POST /v2/extract`` (or the pipeline's extract step): a tree mirroring your extraction schema whose leaves are ``{value, ranges}`` objects, where ``ranges`` are ``{start, end}`` Unicode code point offsets into the parse markdown.

        structure : typing.Dict[str, typing.Any]
            The ``structure`` tree from the parse response the extraction was produced from. Every block in the tree carries its ``grounding`` (``{page, range, box}``) inline; block ids in the response resolve against this exact tree.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V2GroundCreateJobResponse]
            Job created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/ground/jobs",
            method="POST",
            json={
                "extraction_metadata": extraction_metadata,
                "structure": structure,
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
                    V2GroundCreateJobResponse,
                    parse_obj_as(
                        type_=V2GroundCreateJobResponse,
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

    async def v2ground_get_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V2GroundGetJobResponse]:
        """
        Get the status of an async Ground job, including its result once the job has completed.

        Parameters
        ----------
        job_id : str
            The identifier of the job to retrieve, as returned by the create-job request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V2GroundGetJobResponse]
            Job status / result
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/ground/jobs/{encode_path_param(job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2GroundGetJobResponse,
                    parse_obj_as(
                        type_=V2GroundGetJobResponse,
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
