

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.job import Job
from .types.list_jobs_request_order import ListJobsRequestOrder
from .types.list_jobs_request_order_by import ListJobsRequestOrderBy
from pydantic import ValidationError


class RawJobsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_jobs(
        self,
        *,
        source_id: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListJobsRequestOrder] = None,
        order_by: typing.Optional[ListJobsRequestOrderBy] = None,
        active: typing.Optional[bool] = None,
        ascending: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Job]]:
        """
        List all jobs.

        Parameters
        ----------
        source_id : typing.Optional[str]
            Deprecated: Use `folder_id` parameter instead. Only list jobs associated with the source.

        before : typing.Optional[str]
            Job ID cursor for pagination. Returns jobs that come before this job ID in the specified sort order

        after : typing.Optional[str]
            Job ID cursor for pagination. Returns jobs that come after this job ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of jobs to return

        order : typing.Optional[ListJobsRequestOrder]
            Sort order for jobs by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListJobsRequestOrderBy]
            Field to sort by

        active : typing.Optional[bool]
            Filter for active jobs.

        ascending : typing.Optional[bool]
            Whether to sort jobs oldest to newest (True, default) or newest to oldest (False). Deprecated in favor of order field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Job]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/jobs/",
            method="GET",
            params={
                "source_id": source_id,
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "active": active,
                "ascending": ascending,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Job],
                    parse_obj_as(
                        type_=typing.List[Job],
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

    def list_active_jobs(
        self,
        *,
        source_id: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        ascending: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Job]]:
        """
        List all active jobs.

        Parameters
        ----------
        source_id : typing.Optional[str]
            Deprecated: Use `folder_id` parameter instead. Only list jobs associated with the source.

        before : typing.Optional[str]
            Cursor for pagination

        after : typing.Optional[str]
            Cursor for pagination

        limit : typing.Optional[int]
            Limit for pagination

        ascending : typing.Optional[bool]
            Whether to sort jobs oldest to newest (True, default) or newest to oldest (False)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Job]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/jobs/active",
            method="GET",
            params={
                "source_id": source_id,
                "before": before,
                "after": after,
                "limit": limit,
                "ascending": ascending,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Job],
                    parse_obj_as(
                        type_=typing.List[Job],
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

    def retrieve_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Job]:
        """
        Get the status of a job.

        Parameters
        ----------
        job_id : str
            The ID of the job in the format 'job-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Job]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/jobs/{encode_path_param(job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Job,
                    parse_obj_as(
                        type_=Job,
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

    def delete_job(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Job]:
        """
        Delete a job by its job_id.

        Parameters
        ----------
        job_id : str
            The ID of the job in the format 'job-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Job]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/jobs/{encode_path_param(job_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Job,
                    parse_obj_as(
                        type_=Job,
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

    def cancel_job(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Job]:
        """
        Cancel a job by its job_id.

        This endpoint marks a job as cancelled, which will cause any associated
        agent execution to terminate as soon as possible.

        Parameters
        ----------
        job_id : str
            The ID of the job in the format 'job-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Job]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/jobs/{encode_path_param(job_id)}/cancel",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Job,
                    parse_obj_as(
                        type_=Job,
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


class AsyncRawJobsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_jobs(
        self,
        *,
        source_id: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListJobsRequestOrder] = None,
        order_by: typing.Optional[ListJobsRequestOrderBy] = None,
        active: typing.Optional[bool] = None,
        ascending: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Job]]:
        """
        List all jobs.

        Parameters
        ----------
        source_id : typing.Optional[str]
            Deprecated: Use `folder_id` parameter instead. Only list jobs associated with the source.

        before : typing.Optional[str]
            Job ID cursor for pagination. Returns jobs that come before this job ID in the specified sort order

        after : typing.Optional[str]
            Job ID cursor for pagination. Returns jobs that come after this job ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of jobs to return

        order : typing.Optional[ListJobsRequestOrder]
            Sort order for jobs by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListJobsRequestOrderBy]
            Field to sort by

        active : typing.Optional[bool]
            Filter for active jobs.

        ascending : typing.Optional[bool]
            Whether to sort jobs oldest to newest (True, default) or newest to oldest (False). Deprecated in favor of order field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Job]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/jobs/",
            method="GET",
            params={
                "source_id": source_id,
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "active": active,
                "ascending": ascending,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Job],
                    parse_obj_as(
                        type_=typing.List[Job],
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

    async def list_active_jobs(
        self,
        *,
        source_id: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        ascending: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Job]]:
        """
        List all active jobs.

        Parameters
        ----------
        source_id : typing.Optional[str]
            Deprecated: Use `folder_id` parameter instead. Only list jobs associated with the source.

        before : typing.Optional[str]
            Cursor for pagination

        after : typing.Optional[str]
            Cursor for pagination

        limit : typing.Optional[int]
            Limit for pagination

        ascending : typing.Optional[bool]
            Whether to sort jobs oldest to newest (True, default) or newest to oldest (False)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Job]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/jobs/active",
            method="GET",
            params={
                "source_id": source_id,
                "before": before,
                "after": after,
                "limit": limit,
                "ascending": ascending,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Job],
                    parse_obj_as(
                        type_=typing.List[Job],
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

    async def retrieve_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Job]:
        """
        Get the status of a job.

        Parameters
        ----------
        job_id : str
            The ID of the job in the format 'job-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Job]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/jobs/{encode_path_param(job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Job,
                    parse_obj_as(
                        type_=Job,
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

    async def delete_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Job]:
        """
        Delete a job by its job_id.

        Parameters
        ----------
        job_id : str
            The ID of the job in the format 'job-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Job]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/jobs/{encode_path_param(job_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Job,
                    parse_obj_as(
                        type_=Job,
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

    async def cancel_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Job]:
        """
        Cancel a job by its job_id.

        This endpoint marks a job as cancelled, which will cause any associated
        agent execution to terminate as soon as possible.

        Parameters
        ----------
        job_id : str
            The ID of the job in the format 'job-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Job]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/jobs/{encode_path_param(job_id)}/cancel",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Job,
                    parse_obj_as(
                        type_=Job,
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
