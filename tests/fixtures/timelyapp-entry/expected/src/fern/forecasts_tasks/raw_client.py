

import datetime as dt
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
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.v1forecast import V1Forecast
from ..types.v1forecast_summary import V1ForecastSummary
from .types.list_task_summaries_request_completed import ListTaskSummariesRequestCompleted
from .types.list_task_summaries_request_resource import ListTaskSummariesRequestResource
from .types.list_tasks_request_completed import ListTasksRequestCompleted
from .types.list_tasks_request_order import ListTasksRequestOrder
from .types.list_tasks_request_sort import ListTasksRequestSort
from .types.v1forecasts_create_forecast import V1ForecastsCreateForecast
from .types.v1forecasts_update_forecast import V1ForecastsUpdateForecast
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawForecastsTasksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_tasks(
        self,
        account_id: int,
        *,
        since: typing.Optional[dt.date] = None,
        upto: typing.Optional[dt.date] = None,
        completed: typing.Optional[ListTasksRequestCompleted] = None,
        user_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        forecast_ids: typing.Optional[str] = None,
        sort: typing.Optional[ListTasksRequestSort] = None,
        order: typing.Optional[ListTasksRequestOrder] = None,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[V1Forecast]]:
        """
        List all tasks in the account. Tasks are returned in a paginated format with optional filtering by date range, user, project, and completion status.

        Parameters
        ----------
        account_id : int
            Account ID

        since : typing.Optional[dt.date]
            Filter tasks from this date (inclusive)

        upto : typing.Optional[dt.date]
            Filter tasks up to this date (inclusive)

        completed : typing.Optional[ListTasksRequestCompleted]
            Filter by completion status

        user_ids : typing.Optional[str]
            Comma-separated list of user IDs to filter by

        project_ids : typing.Optional[str]
            Comma-separated list of project IDs, or "active"/"archived" to filter by project status

        forecast_ids : typing.Optional[str]
            Comma-separated list of task IDs to filter by

        sort : typing.Optional[ListTasksRequestSort]
            Field to sort by (default: updated_at)

        order : typing.Optional[ListTasksRequestOrder]
            Sort order (default: desc)

        per_page : typing.Optional[int]
            Number of results per page (max 5000)

        page : typing.Optional[int]
            Page number for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1Forecast]]
            Tasks list
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/forecasts",
            method="GET",
            params={
                "since": str(since) if since is not None else None,
                "upto": str(upto) if upto is not None else None,
                "completed": completed,
                "user_ids": user_ids,
                "project_ids": project_ids,
                "forecast_ids": forecast_ids,
                "sort": sort,
                "order": order,
                "per_page": per_page,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Forecast],
                    parse_obj_as(
                        type_=typing.List[V1Forecast],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    def create_task(
        self,
        account_id: int,
        *,
        forecast: V1ForecastsCreateForecast,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1Forecast]:
        """
        Create a new task. Requires the Planning feature to be enabled.

        Parameters
        ----------
        account_id : int
            Account ID

        forecast : V1ForecastsCreateForecast

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Forecast]
            Task created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/forecasts",
            method="POST",
            json={
                "forecast": convert_and_respect_annotation_metadata(
                    object_=forecast, annotation=V1ForecastsCreateForecast, direction="write"
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
                    V1Forecast,
                    parse_obj_as(
                        type_=V1Forecast,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def show_task(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1Forecast]:
        """
        Retrieve details for a specific task.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Task ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Forecast]
            Task details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/forecasts/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Forecast,
                    parse_obj_as(
                        type_=V1Forecast,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def delete_task(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete a task.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Task ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Task deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/forecasts/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def update_task(
        self,
        account_id: int,
        id: int,
        *,
        forecast: V1ForecastsUpdateForecast,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1Forecast]:
        """
        Update an existing task. Only the provided fields will be updated.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Task ID

        forecast : V1ForecastsUpdateForecast

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Forecast]
            Task updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/forecasts/{encode_path_param(id)}",
            method="PATCH",
            json={
                "forecast": convert_and_respect_annotation_metadata(
                    object_=forecast, annotation=V1ForecastsUpdateForecast, direction="write"
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
                    V1Forecast,
                    parse_obj_as(
                        type_=V1Forecast,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def list_task_summaries(
        self,
        account_id: int,
        resource: ListTaskSummariesRequestResource,
        *,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        completed: typing.Optional[ListTaskSummariesRequestCompleted] = None,
        user_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        forecast_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[V1ForecastSummary]]:
        """
        Get task summaries grouped by resource type (users or projects). Returns aggregate counts and duration totals.

        Parameters
        ----------
        account_id : int
            Account ID

        resource : ListTaskSummariesRequestResource
            Resource type to group summaries by

        since : typing.Optional[dt.date]
            Filter tasks from this date

        until : typing.Optional[dt.date]
            Filter tasks up to this date

        completed : typing.Optional[ListTaskSummariesRequestCompleted]
            Filter by completion status

        user_ids : typing.Optional[str]
            Comma-separated user IDs to filter by

        project_ids : typing.Optional[str]
            Comma-separated project IDs to filter by

        forecast_ids : typing.Optional[str]
            Comma-separated task IDs to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1ForecastSummary]]
            Task summaries
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/forecasts/{encode_path_param(resource)}/summary",
            method="GET",
            params={
                "since": str(since) if since is not None else None,
                "until": str(until) if until is not None else None,
                "completed": completed,
                "user_ids": user_ids,
                "project_ids": project_ids,
                "forecast_ids": forecast_ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1ForecastSummary],
                    parse_obj_as(
                        type_=typing.List[V1ForecastSummary],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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


class AsyncRawForecastsTasksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_tasks(
        self,
        account_id: int,
        *,
        since: typing.Optional[dt.date] = None,
        upto: typing.Optional[dt.date] = None,
        completed: typing.Optional[ListTasksRequestCompleted] = None,
        user_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        forecast_ids: typing.Optional[str] = None,
        sort: typing.Optional[ListTasksRequestSort] = None,
        order: typing.Optional[ListTasksRequestOrder] = None,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[V1Forecast]]:
        """
        List all tasks in the account. Tasks are returned in a paginated format with optional filtering by date range, user, project, and completion status.

        Parameters
        ----------
        account_id : int
            Account ID

        since : typing.Optional[dt.date]
            Filter tasks from this date (inclusive)

        upto : typing.Optional[dt.date]
            Filter tasks up to this date (inclusive)

        completed : typing.Optional[ListTasksRequestCompleted]
            Filter by completion status

        user_ids : typing.Optional[str]
            Comma-separated list of user IDs to filter by

        project_ids : typing.Optional[str]
            Comma-separated list of project IDs, or "active"/"archived" to filter by project status

        forecast_ids : typing.Optional[str]
            Comma-separated list of task IDs to filter by

        sort : typing.Optional[ListTasksRequestSort]
            Field to sort by (default: updated_at)

        order : typing.Optional[ListTasksRequestOrder]
            Sort order (default: desc)

        per_page : typing.Optional[int]
            Number of results per page (max 5000)

        page : typing.Optional[int]
            Page number for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1Forecast]]
            Tasks list
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/forecasts",
            method="GET",
            params={
                "since": str(since) if since is not None else None,
                "upto": str(upto) if upto is not None else None,
                "completed": completed,
                "user_ids": user_ids,
                "project_ids": project_ids,
                "forecast_ids": forecast_ids,
                "sort": sort,
                "order": order,
                "per_page": per_page,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Forecast],
                    parse_obj_as(
                        type_=typing.List[V1Forecast],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    async def create_task(
        self,
        account_id: int,
        *,
        forecast: V1ForecastsCreateForecast,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1Forecast]:
        """
        Create a new task. Requires the Planning feature to be enabled.

        Parameters
        ----------
        account_id : int
            Account ID

        forecast : V1ForecastsCreateForecast

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Forecast]
            Task created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/forecasts",
            method="POST",
            json={
                "forecast": convert_and_respect_annotation_metadata(
                    object_=forecast, annotation=V1ForecastsCreateForecast, direction="write"
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
                    V1Forecast,
                    parse_obj_as(
                        type_=V1Forecast,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def show_task(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1Forecast]:
        """
        Retrieve details for a specific task.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Task ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Forecast]
            Task details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/forecasts/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Forecast,
                    parse_obj_as(
                        type_=V1Forecast,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def delete_task(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete a task.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Task ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Task deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/forecasts/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def update_task(
        self,
        account_id: int,
        id: int,
        *,
        forecast: V1ForecastsUpdateForecast,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1Forecast]:
        """
        Update an existing task. Only the provided fields will be updated.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Task ID

        forecast : V1ForecastsUpdateForecast

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Forecast]
            Task updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/forecasts/{encode_path_param(id)}",
            method="PATCH",
            json={
                "forecast": convert_and_respect_annotation_metadata(
                    object_=forecast, annotation=V1ForecastsUpdateForecast, direction="write"
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
                    V1Forecast,
                    parse_obj_as(
                        type_=V1Forecast,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def list_task_summaries(
        self,
        account_id: int,
        resource: ListTaskSummariesRequestResource,
        *,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        completed: typing.Optional[ListTaskSummariesRequestCompleted] = None,
        user_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        forecast_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[V1ForecastSummary]]:
        """
        Get task summaries grouped by resource type (users or projects). Returns aggregate counts and duration totals.

        Parameters
        ----------
        account_id : int
            Account ID

        resource : ListTaskSummariesRequestResource
            Resource type to group summaries by

        since : typing.Optional[dt.date]
            Filter tasks from this date

        until : typing.Optional[dt.date]
            Filter tasks up to this date

        completed : typing.Optional[ListTaskSummariesRequestCompleted]
            Filter by completion status

        user_ids : typing.Optional[str]
            Comma-separated user IDs to filter by

        project_ids : typing.Optional[str]
            Comma-separated project IDs to filter by

        forecast_ids : typing.Optional[str]
            Comma-separated task IDs to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1ForecastSummary]]
            Task summaries
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/forecasts/{encode_path_param(resource)}/summary",
            method="GET",
            params={
                "since": str(since) if since is not None else None,
                "until": str(until) if until is not None else None,
                "completed": completed,
                "user_ids": user_ids,
                "project_ids": project_ids,
                "forecast_ids": forecast_ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1ForecastSummary],
                    parse_obj_as(
                        type_=typing.List[V1ForecastSummary],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
