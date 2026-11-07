

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error_envelope import ErrorEnvelope
from ..types.periodic_job import PeriodicJob
from ..types.periodic_job_catalog import PeriodicJobCatalog
from ..types.periodic_job_list import PeriodicJobList
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPeriodicJobsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_periodic_jobs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PeriodicJobList]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PeriodicJobList]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/periodic-jobs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PeriodicJobList,
                    parse_obj_as(
                        type_=PeriodicJobList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def create_periodic_job(
        self,
        *,
        id: str,
        kind: str,
        args: typing.Dict[str, typing.Any],
        queue: str,
        priority: int,
        max_attempts: int,
        tags: typing.Sequence[str],
        cron_expression: str,
        cron_timezone: str,
        paused: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PeriodicJob]:
        """
        Parameters
        ----------
        id : str

        kind : str

        args : typing.Dict[str, typing.Any]

        queue : str

        priority : int

        max_attempts : int

        tags : typing.Sequence[str]

        cron_expression : str

        cron_timezone : str

        paused : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PeriodicJob]
            The request has succeeded and a new resource has been created as a result.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/periodic-jobs",
            method="POST",
            json={
                "id": id,
                "kind": kind,
                "args": args,
                "queue": queue,
                "priority": priority,
                "maxAttempts": max_attempts,
                "tags": tags,
                "cronExpression": cron_expression,
                "cronTimezone": cron_timezone,
                "paused": paused,
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
                    PeriodicJob,
                    parse_obj_as(
                        type_=PeriodicJob,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def get_periodic_job_catalog(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PeriodicJobCatalog]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PeriodicJobCatalog]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/periodic-jobs/catalog",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PeriodicJobCatalog,
                    parse_obj_as(
                        type_=PeriodicJobCatalog,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def reset_periodic_jobs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PeriodicJobList]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PeriodicJobList]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/periodic-jobs/reset",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PeriodicJobList,
                    parse_obj_as(
                        type_=PeriodicJobList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def update_periodic_job(
        self,
        periodic_job_id: str,
        *,
        kind: str,
        args: typing.Dict[str, typing.Any],
        queue: str,
        priority: int,
        max_attempts: int,
        tags: typing.Sequence[str],
        cron_expression: str,
        cron_timezone: str,
        paused: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PeriodicJob]:
        """
        Parameters
        ----------
        periodic_job_id : str

        kind : str

        args : typing.Dict[str, typing.Any]

        queue : str

        priority : int

        max_attempts : int

        tags : typing.Sequence[str]

        cron_expression : str

        cron_timezone : str

        paused : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PeriodicJob]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/periodic-jobs/{encode_path_param(periodic_job_id)}",
            method="PUT",
            json={
                "kind": kind,
                "args": args,
                "queue": queue,
                "priority": priority,
                "maxAttempts": max_attempts,
                "tags": tags,
                "cronExpression": cron_expression,
                "cronTimezone": cron_timezone,
                "paused": paused,
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
                    PeriodicJob,
                    parse_obj_as(
                        type_=PeriodicJob,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def delete_periodic_job(
        self, periodic_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        periodic_job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/periodic-jobs/{encode_path_param(periodic_job_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def pause_periodic_job(
        self, periodic_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PeriodicJob]:
        """
        Parameters
        ----------
        periodic_job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PeriodicJob]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/periodic-jobs/{encode_path_param(periodic_job_id)}/pause",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PeriodicJob,
                    parse_obj_as(
                        type_=PeriodicJob,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    def resume_periodic_job(
        self, periodic_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PeriodicJob]:
        """
        Parameters
        ----------
        periodic_job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PeriodicJob]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/periodic-jobs/{encode_path_param(periodic_job_id)}/resume",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PeriodicJob,
                    parse_obj_as(
                        type_=PeriodicJob,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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


class AsyncRawPeriodicJobsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_periodic_jobs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PeriodicJobList]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PeriodicJobList]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/periodic-jobs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PeriodicJobList,
                    parse_obj_as(
                        type_=PeriodicJobList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def create_periodic_job(
        self,
        *,
        id: str,
        kind: str,
        args: typing.Dict[str, typing.Any],
        queue: str,
        priority: int,
        max_attempts: int,
        tags: typing.Sequence[str],
        cron_expression: str,
        cron_timezone: str,
        paused: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PeriodicJob]:
        """
        Parameters
        ----------
        id : str

        kind : str

        args : typing.Dict[str, typing.Any]

        queue : str

        priority : int

        max_attempts : int

        tags : typing.Sequence[str]

        cron_expression : str

        cron_timezone : str

        paused : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PeriodicJob]
            The request has succeeded and a new resource has been created as a result.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/periodic-jobs",
            method="POST",
            json={
                "id": id,
                "kind": kind,
                "args": args,
                "queue": queue,
                "priority": priority,
                "maxAttempts": max_attempts,
                "tags": tags,
                "cronExpression": cron_expression,
                "cronTimezone": cron_timezone,
                "paused": paused,
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
                    PeriodicJob,
                    parse_obj_as(
                        type_=PeriodicJob,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def get_periodic_job_catalog(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PeriodicJobCatalog]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PeriodicJobCatalog]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/periodic-jobs/catalog",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PeriodicJobCatalog,
                    parse_obj_as(
                        type_=PeriodicJobCatalog,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def reset_periodic_jobs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PeriodicJobList]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PeriodicJobList]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/periodic-jobs/reset",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PeriodicJobList,
                    parse_obj_as(
                        type_=PeriodicJobList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def update_periodic_job(
        self,
        periodic_job_id: str,
        *,
        kind: str,
        args: typing.Dict[str, typing.Any],
        queue: str,
        priority: int,
        max_attempts: int,
        tags: typing.Sequence[str],
        cron_expression: str,
        cron_timezone: str,
        paused: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PeriodicJob]:
        """
        Parameters
        ----------
        periodic_job_id : str

        kind : str

        args : typing.Dict[str, typing.Any]

        queue : str

        priority : int

        max_attempts : int

        tags : typing.Sequence[str]

        cron_expression : str

        cron_timezone : str

        paused : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PeriodicJob]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/periodic-jobs/{encode_path_param(periodic_job_id)}",
            method="PUT",
            json={
                "kind": kind,
                "args": args,
                "queue": queue,
                "priority": priority,
                "maxAttempts": max_attempts,
                "tags": tags,
                "cronExpression": cron_expression,
                "cronTimezone": cron_timezone,
                "paused": paused,
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
                    PeriodicJob,
                    parse_obj_as(
                        type_=PeriodicJob,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def delete_periodic_job(
        self, periodic_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        periodic_job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/periodic-jobs/{encode_path_param(periodic_job_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def pause_periodic_job(
        self, periodic_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PeriodicJob]:
        """
        Parameters
        ----------
        periodic_job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PeriodicJob]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/periodic-jobs/{encode_path_param(periodic_job_id)}/pause",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PeriodicJob,
                    parse_obj_as(
                        type_=PeriodicJob,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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

    async def resume_periodic_job(
        self, periodic_job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PeriodicJob]:
        """
        Parameters
        ----------
        periodic_job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PeriodicJob]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/periodic-jobs/{encode_path_param(periodic_job_id)}/resume",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PeriodicJob,
                    parse_obj_as(
                        type_=PeriodicJob,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorEnvelope,
                        parse_obj_as(
                            type_=ErrorEnvelope,
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
