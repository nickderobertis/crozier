

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from ..types.extra_link_collection import ExtraLinkCollection
from ..types.task_instance import TaskInstance
from ..types.task_instance_collection import TaskInstanceCollection
from ..types.task_instance_reference import TaskInstanceReference
from ..types.task_state import TaskState
from ..types.update_task_instance_new_state import UpdateTaskInstanceNewState
from .types.get_log_response import GetLogResponse


OMIT = typing.cast(typing.Any, ...)


class RawTaskInstanceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_task_instances(
        self,
        dag_id: str,
        dag_run_id: str,
        *,
        execution_date_gte: typing.Optional[dt.datetime] = None,
        execution_date_lte: typing.Optional[dt.datetime] = None,
        start_date_gte: typing.Optional[dt.datetime] = None,
        start_date_lte: typing.Optional[dt.datetime] = None,
        end_date_gte: typing.Optional[dt.datetime] = None,
        end_date_lte: typing.Optional[dt.datetime] = None,
        duration_gte: typing.Optional[float] = None,
        duration_lte: typing.Optional[float] = None,
        state: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pool: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        queue: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaskInstanceCollection]:
        """
        This endpoint allows specifying `~` as the dag_id, dag_run_id to retrieve DAG runs for all DAGs and DAG runs.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        execution_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal to the specified date.

            This can be combined with execution_date_lte parameter to receive only the selected period.

        execution_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with execution_date_gte parameter to receive only the selected period.

        start_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        start_date_lte : typing.Optional[dt.datetime]
            Returns objects less or equal the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        end_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        end_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        duration_gte : typing.Optional[float]
            Returns objects greater than or equal to the specified values.

            This can be combined with duration_lte parameter to receive only the selected period.

        duration_lte : typing.Optional[float]
            Returns objects less than or equal to the specified values.

            This can be combined with duration_gte parameter to receive only the selected range.

        state : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        pool : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        queue : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskInstanceCollection]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances",
            method="GET",
            params={
                "execution_date_gte": serialize_datetime(execution_date_gte)
                if execution_date_gte is not None
                else None,
                "execution_date_lte": serialize_datetime(execution_date_lte)
                if execution_date_lte is not None
                else None,
                "start_date_gte": serialize_datetime(start_date_gte) if start_date_gte is not None else None,
                "start_date_lte": serialize_datetime(start_date_lte) if start_date_lte is not None else None,
                "end_date_gte": serialize_datetime(end_date_gte) if end_date_gte is not None else None,
                "end_date_lte": serialize_datetime(end_date_lte) if end_date_lte is not None else None,
                "duration_gte": duration_gte,
                "duration_lte": duration_lte,
                "state": state,
                "pool": pool,
                "queue": queue,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskInstanceCollection,
                    parse_obj_as(
                        type_=TaskInstanceCollection,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_task_instance(
        self, dag_id: str, dag_run_id: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TaskInstance]:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskInstance]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances/{jsonable_encoder(task_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskInstance,
                    parse_obj_as(
                        type_=TaskInstance,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def patch_task_instance(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        *,
        dry_run: typing.Optional[bool] = OMIT,
        new_state: typing.Optional[UpdateTaskInstanceNewState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaskInstanceReference]:
        """
        Updates the state for single task instance.
        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        dry_run : typing.Optional[bool]
            If set, don't actually run this operation. The response will contain the task instance
            planned to be affected, but won't be modified in any way.

        new_state : typing.Optional[UpdateTaskInstanceNewState]
            Expected new state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskInstanceReference]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances/{jsonable_encoder(task_id)}",
            method="PATCH",
            json={
                "dry_run": dry_run,
                "new_state": new_state,
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
                    TaskInstanceReference,
                    parse_obj_as(
                        type_=TaskInstanceReference,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_extra_links(
        self, dag_id: str, dag_run_id: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ExtraLinkCollection]:
        """
        List extra links for task instance.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExtraLinkCollection]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances/{jsonable_encoder(task_id)}/links",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtraLinkCollection,
                    parse_obj_as(
                        type_=ExtraLinkCollection,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_mapped_task_instances(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        execution_date_gte: typing.Optional[dt.datetime] = None,
        execution_date_lte: typing.Optional[dt.datetime] = None,
        start_date_gte: typing.Optional[dt.datetime] = None,
        start_date_lte: typing.Optional[dt.datetime] = None,
        end_date_gte: typing.Optional[dt.datetime] = None,
        end_date_lte: typing.Optional[dt.datetime] = None,
        duration_gte: typing.Optional[float] = None,
        duration_lte: typing.Optional[float] = None,
        state: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pool: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        queue: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaskInstanceCollection]:
        """
        Get details of all mapped task instances.

        *New in version 2.3.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        execution_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal to the specified date.

            This can be combined with execution_date_lte parameter to receive only the selected period.

        execution_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with execution_date_gte parameter to receive only the selected period.

        start_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        start_date_lte : typing.Optional[dt.datetime]
            Returns objects less or equal the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        end_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        end_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        duration_gte : typing.Optional[float]
            Returns objects greater than or equal to the specified values.

            This can be combined with duration_lte parameter to receive only the selected period.

        duration_lte : typing.Optional[float]
            Returns objects less than or equal to the specified values.

            This can be combined with duration_gte parameter to receive only the selected range.

        state : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        pool : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        queue : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskInstanceCollection]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances/{jsonable_encoder(task_id)}/listMapped",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "execution_date_gte": serialize_datetime(execution_date_gte)
                if execution_date_gte is not None
                else None,
                "execution_date_lte": serialize_datetime(execution_date_lte)
                if execution_date_lte is not None
                else None,
                "start_date_gte": serialize_datetime(start_date_gte) if start_date_gte is not None else None,
                "start_date_lte": serialize_datetime(start_date_lte) if start_date_lte is not None else None,
                "end_date_gte": serialize_datetime(end_date_gte) if end_date_gte is not None else None,
                "end_date_lte": serialize_datetime(end_date_lte) if end_date_lte is not None else None,
                "duration_gte": duration_gte,
                "duration_lte": duration_lte,
                "state": state,
                "pool": pool,
                "queue": queue,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskInstanceCollection,
                    parse_obj_as(
                        type_=TaskInstanceCollection,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_log(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        task_try_number: int,
        *,
        full_content: typing.Optional[bool] = None,
        map_index: typing.Optional[int] = None,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetLogResponse]:
        """
        Get logs for a specific task instance and its try number.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        task_try_number : int
            The task try number.

        full_content : typing.Optional[bool]
            A full content will be returned.
            By default, only the first fragment will be returned.

        map_index : typing.Optional[int]
            Filter on map index for mapped task.

        token : typing.Optional[str]
            A token that allows you to continue fetching logs.
            If passed, it will specify the location from which the download should be continued.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetLogResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances/{jsonable_encoder(task_id)}/logs/{jsonable_encoder(task_try_number)}",
            method="GET",
            params={
                "full_content": full_content,
                "map_index": map_index,
                "token": token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLogResponse,
                    parse_obj_as(
                        type_=GetLogResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def set_task_instance_note(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        *,
        note: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaskInstance]:
        """
        Update the manual user note of a non-mapped Task Instance.

        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        note : str
            The custom note to set for this Task Instance.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskInstance]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances/{jsonable_encoder(task_id)}/setNote",
            method="PATCH",
            json={
                "note": note,
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
                    TaskInstance,
                    parse_obj_as(
                        type_=TaskInstance,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_mapped_task_instance(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        map_index: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaskInstance]:
        """
        Get details of a mapped task instance.

        *New in version 2.3.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        map_index : int
            The map index.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskInstance]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances/{jsonable_encoder(task_id)}/{jsonable_encoder(map_index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskInstance,
                    parse_obj_as(
                        type_=TaskInstance,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def patch_mapped_task_instance(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        map_index: int,
        *,
        dry_run: typing.Optional[bool] = OMIT,
        new_state: typing.Optional[UpdateTaskInstanceNewState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaskInstanceReference]:
        """
        Updates the state for single mapped task instance.
        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        map_index : int
            The map index.

        dry_run : typing.Optional[bool]
            If set, don't actually run this operation. The response will contain the task instance
            planned to be affected, but won't be modified in any way.

        new_state : typing.Optional[UpdateTaskInstanceNewState]
            Expected new state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskInstanceReference]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances/{jsonable_encoder(task_id)}/{jsonable_encoder(map_index)}",
            method="PATCH",
            json={
                "dry_run": dry_run,
                "new_state": new_state,
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
                    TaskInstanceReference,
                    parse_obj_as(
                        type_=TaskInstanceReference,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def set_mapped_task_instance_note(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        map_index: int,
        *,
        note: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaskInstance]:
        """
        Update the manual user note of a mapped Task Instance.

        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        map_index : int
            The map index.

        note : str
            The custom note to set for this Task Instance.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskInstance]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances/{jsonable_encoder(task_id)}/{jsonable_encoder(map_index)}/setNote",
            method="PATCH",
            json={
                "note": note,
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
                    TaskInstance,
                    parse_obj_as(
                        type_=TaskInstance,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_task_instances_batch(
        self,
        *,
        dag_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        duration_gte: typing.Optional[float] = OMIT,
        duration_lte: typing.Optional[float] = OMIT,
        end_date_gte: typing.Optional[dt.datetime] = OMIT,
        end_date_lte: typing.Optional[dt.datetime] = OMIT,
        execution_date_gte: typing.Optional[dt.datetime] = OMIT,
        execution_date_lte: typing.Optional[dt.datetime] = OMIT,
        pool: typing.Optional[typing.Sequence[str]] = OMIT,
        queue: typing.Optional[typing.Sequence[str]] = OMIT,
        start_date_gte: typing.Optional[dt.datetime] = OMIT,
        start_date_lte: typing.Optional[dt.datetime] = OMIT,
        state: typing.Optional[typing.Sequence[TaskState]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaskInstanceCollection]:
        """
        List task instances from all DAGs and DAG runs.
        This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limits.

        Parameters
        ----------
        dag_ids : typing.Optional[typing.Sequence[str]]
            Return objects with specific DAG IDs.
            The value can be repeated to retrieve multiple matching values (OR condition).

        duration_gte : typing.Optional[float]
            Returns objects greater than or equal to the specified values.

            This can be combined with duration_lte parameter to receive only the selected period.

        duration_lte : typing.Optional[float]
            Returns objects less than or equal to the specified values.

            This can be combined with duration_gte parameter to receive only the selected range.

        end_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        end_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        execution_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal to the specified date.

            This can be combined with execution_date_lte parameter to receive only the selected period.

        execution_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with execution_date_gte parameter to receive only the selected period.

        pool : typing.Optional[typing.Sequence[str]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        queue : typing.Optional[typing.Sequence[str]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        start_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        start_date_lte : typing.Optional[dt.datetime]
            Returns objects less or equal the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        state : typing.Optional[typing.Sequence[TaskState]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskInstanceCollection]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "dags/~/dagRuns/~/taskInstances/list",
            method="POST",
            json={
                "dag_ids": dag_ids,
                "duration_gte": duration_gte,
                "duration_lte": duration_lte,
                "end_date_gte": end_date_gte,
                "end_date_lte": end_date_lte,
                "execution_date_gte": execution_date_gte,
                "execution_date_lte": execution_date_lte,
                "pool": pool,
                "queue": queue,
                "start_date_gte": start_date_gte,
                "start_date_lte": start_date_lte,
                "state": state,
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
                    TaskInstanceCollection,
                    parse_obj_as(
                        type_=TaskInstanceCollection,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTaskInstanceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_task_instances(
        self,
        dag_id: str,
        dag_run_id: str,
        *,
        execution_date_gte: typing.Optional[dt.datetime] = None,
        execution_date_lte: typing.Optional[dt.datetime] = None,
        start_date_gte: typing.Optional[dt.datetime] = None,
        start_date_lte: typing.Optional[dt.datetime] = None,
        end_date_gte: typing.Optional[dt.datetime] = None,
        end_date_lte: typing.Optional[dt.datetime] = None,
        duration_gte: typing.Optional[float] = None,
        duration_lte: typing.Optional[float] = None,
        state: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pool: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        queue: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaskInstanceCollection]:
        """
        This endpoint allows specifying `~` as the dag_id, dag_run_id to retrieve DAG runs for all DAGs and DAG runs.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        execution_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal to the specified date.

            This can be combined with execution_date_lte parameter to receive only the selected period.

        execution_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with execution_date_gte parameter to receive only the selected period.

        start_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        start_date_lte : typing.Optional[dt.datetime]
            Returns objects less or equal the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        end_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        end_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        duration_gte : typing.Optional[float]
            Returns objects greater than or equal to the specified values.

            This can be combined with duration_lte parameter to receive only the selected period.

        duration_lte : typing.Optional[float]
            Returns objects less than or equal to the specified values.

            This can be combined with duration_gte parameter to receive only the selected range.

        state : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        pool : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        queue : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskInstanceCollection]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances",
            method="GET",
            params={
                "execution_date_gte": serialize_datetime(execution_date_gte)
                if execution_date_gte is not None
                else None,
                "execution_date_lte": serialize_datetime(execution_date_lte)
                if execution_date_lte is not None
                else None,
                "start_date_gte": serialize_datetime(start_date_gte) if start_date_gte is not None else None,
                "start_date_lte": serialize_datetime(start_date_lte) if start_date_lte is not None else None,
                "end_date_gte": serialize_datetime(end_date_gte) if end_date_gte is not None else None,
                "end_date_lte": serialize_datetime(end_date_lte) if end_date_lte is not None else None,
                "duration_gte": duration_gte,
                "duration_lte": duration_lte,
                "state": state,
                "pool": pool,
                "queue": queue,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskInstanceCollection,
                    parse_obj_as(
                        type_=TaskInstanceCollection,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_task_instance(
        self, dag_id: str, dag_run_id: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TaskInstance]:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskInstance]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances/{jsonable_encoder(task_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskInstance,
                    parse_obj_as(
                        type_=TaskInstance,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def patch_task_instance(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        *,
        dry_run: typing.Optional[bool] = OMIT,
        new_state: typing.Optional[UpdateTaskInstanceNewState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaskInstanceReference]:
        """
        Updates the state for single task instance.
        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        dry_run : typing.Optional[bool]
            If set, don't actually run this operation. The response will contain the task instance
            planned to be affected, but won't be modified in any way.

        new_state : typing.Optional[UpdateTaskInstanceNewState]
            Expected new state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskInstanceReference]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances/{jsonable_encoder(task_id)}",
            method="PATCH",
            json={
                "dry_run": dry_run,
                "new_state": new_state,
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
                    TaskInstanceReference,
                    parse_obj_as(
                        type_=TaskInstanceReference,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_extra_links(
        self, dag_id: str, dag_run_id: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ExtraLinkCollection]:
        """
        List extra links for task instance.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExtraLinkCollection]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances/{jsonable_encoder(task_id)}/links",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtraLinkCollection,
                    parse_obj_as(
                        type_=ExtraLinkCollection,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_mapped_task_instances(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        execution_date_gte: typing.Optional[dt.datetime] = None,
        execution_date_lte: typing.Optional[dt.datetime] = None,
        start_date_gte: typing.Optional[dt.datetime] = None,
        start_date_lte: typing.Optional[dt.datetime] = None,
        end_date_gte: typing.Optional[dt.datetime] = None,
        end_date_lte: typing.Optional[dt.datetime] = None,
        duration_gte: typing.Optional[float] = None,
        duration_lte: typing.Optional[float] = None,
        state: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pool: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        queue: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaskInstanceCollection]:
        """
        Get details of all mapped task instances.

        *New in version 2.3.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        execution_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal to the specified date.

            This can be combined with execution_date_lte parameter to receive only the selected period.

        execution_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with execution_date_gte parameter to receive only the selected period.

        start_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        start_date_lte : typing.Optional[dt.datetime]
            Returns objects less or equal the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        end_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        end_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        duration_gte : typing.Optional[float]
            Returns objects greater than or equal to the specified values.

            This can be combined with duration_lte parameter to receive only the selected period.

        duration_lte : typing.Optional[float]
            Returns objects less than or equal to the specified values.

            This can be combined with duration_gte parameter to receive only the selected range.

        state : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        pool : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        queue : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskInstanceCollection]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances/{jsonable_encoder(task_id)}/listMapped",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "execution_date_gte": serialize_datetime(execution_date_gte)
                if execution_date_gte is not None
                else None,
                "execution_date_lte": serialize_datetime(execution_date_lte)
                if execution_date_lte is not None
                else None,
                "start_date_gte": serialize_datetime(start_date_gte) if start_date_gte is not None else None,
                "start_date_lte": serialize_datetime(start_date_lte) if start_date_lte is not None else None,
                "end_date_gte": serialize_datetime(end_date_gte) if end_date_gte is not None else None,
                "end_date_lte": serialize_datetime(end_date_lte) if end_date_lte is not None else None,
                "duration_gte": duration_gte,
                "duration_lte": duration_lte,
                "state": state,
                "pool": pool,
                "queue": queue,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskInstanceCollection,
                    parse_obj_as(
                        type_=TaskInstanceCollection,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_log(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        task_try_number: int,
        *,
        full_content: typing.Optional[bool] = None,
        map_index: typing.Optional[int] = None,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetLogResponse]:
        """
        Get logs for a specific task instance and its try number.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        task_try_number : int
            The task try number.

        full_content : typing.Optional[bool]
            A full content will be returned.
            By default, only the first fragment will be returned.

        map_index : typing.Optional[int]
            Filter on map index for mapped task.

        token : typing.Optional[str]
            A token that allows you to continue fetching logs.
            If passed, it will specify the location from which the download should be continued.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetLogResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances/{jsonable_encoder(task_id)}/logs/{jsonable_encoder(task_try_number)}",
            method="GET",
            params={
                "full_content": full_content,
                "map_index": map_index,
                "token": token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLogResponse,
                    parse_obj_as(
                        type_=GetLogResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def set_task_instance_note(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        *,
        note: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaskInstance]:
        """
        Update the manual user note of a non-mapped Task Instance.

        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        note : str
            The custom note to set for this Task Instance.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskInstance]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances/{jsonable_encoder(task_id)}/setNote",
            method="PATCH",
            json={
                "note": note,
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
                    TaskInstance,
                    parse_obj_as(
                        type_=TaskInstance,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_mapped_task_instance(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        map_index: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaskInstance]:
        """
        Get details of a mapped task instance.

        *New in version 2.3.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        map_index : int
            The map index.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskInstance]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances/{jsonable_encoder(task_id)}/{jsonable_encoder(map_index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskInstance,
                    parse_obj_as(
                        type_=TaskInstance,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def patch_mapped_task_instance(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        map_index: int,
        *,
        dry_run: typing.Optional[bool] = OMIT,
        new_state: typing.Optional[UpdateTaskInstanceNewState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaskInstanceReference]:
        """
        Updates the state for single mapped task instance.
        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        map_index : int
            The map index.

        dry_run : typing.Optional[bool]
            If set, don't actually run this operation. The response will contain the task instance
            planned to be affected, but won't be modified in any way.

        new_state : typing.Optional[UpdateTaskInstanceNewState]
            Expected new state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskInstanceReference]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances/{jsonable_encoder(task_id)}/{jsonable_encoder(map_index)}",
            method="PATCH",
            json={
                "dry_run": dry_run,
                "new_state": new_state,
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
                    TaskInstanceReference,
                    parse_obj_as(
                        type_=TaskInstanceReference,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def set_mapped_task_instance_note(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        map_index: int,
        *,
        note: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaskInstance]:
        """
        Update the manual user note of a mapped Task Instance.

        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        map_index : int
            The map index.

        note : str
            The custom note to set for this Task Instance.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskInstance]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{jsonable_encoder(dag_id)}/dagRuns/{jsonable_encoder(dag_run_id)}/taskInstances/{jsonable_encoder(task_id)}/{jsonable_encoder(map_index)}/setNote",
            method="PATCH",
            json={
                "note": note,
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
                    TaskInstance,
                    parse_obj_as(
                        type_=TaskInstance,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_task_instances_batch(
        self,
        *,
        dag_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        duration_gte: typing.Optional[float] = OMIT,
        duration_lte: typing.Optional[float] = OMIT,
        end_date_gte: typing.Optional[dt.datetime] = OMIT,
        end_date_lte: typing.Optional[dt.datetime] = OMIT,
        execution_date_gte: typing.Optional[dt.datetime] = OMIT,
        execution_date_lte: typing.Optional[dt.datetime] = OMIT,
        pool: typing.Optional[typing.Sequence[str]] = OMIT,
        queue: typing.Optional[typing.Sequence[str]] = OMIT,
        start_date_gte: typing.Optional[dt.datetime] = OMIT,
        start_date_lte: typing.Optional[dt.datetime] = OMIT,
        state: typing.Optional[typing.Sequence[TaskState]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaskInstanceCollection]:
        """
        List task instances from all DAGs and DAG runs.
        This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limits.

        Parameters
        ----------
        dag_ids : typing.Optional[typing.Sequence[str]]
            Return objects with specific DAG IDs.
            The value can be repeated to retrieve multiple matching values (OR condition).

        duration_gte : typing.Optional[float]
            Returns objects greater than or equal to the specified values.

            This can be combined with duration_lte parameter to receive only the selected period.

        duration_lte : typing.Optional[float]
            Returns objects less than or equal to the specified values.

            This can be combined with duration_gte parameter to receive only the selected range.

        end_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        end_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        execution_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal to the specified date.

            This can be combined with execution_date_lte parameter to receive only the selected period.

        execution_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with execution_date_gte parameter to receive only the selected period.

        pool : typing.Optional[typing.Sequence[str]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        queue : typing.Optional[typing.Sequence[str]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        start_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        start_date_lte : typing.Optional[dt.datetime]
            Returns objects less or equal the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        state : typing.Optional[typing.Sequence[TaskState]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskInstanceCollection]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "dags/~/dagRuns/~/taskInstances/list",
            method="POST",
            json={
                "dag_ids": dag_ids,
                "duration_gte": duration_gte,
                "duration_lte": duration_lte,
                "end_date_gte": end_date_gte,
                "end_date_lte": end_date_lte,
                "execution_date_gte": execution_date_gte,
                "execution_date_lte": execution_date_lte,
                "pool": pool,
                "queue": queue,
                "start_date_gte": start_date_gte,
                "start_date_lte": start_date_lte,
                "state": state,
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
                    TaskInstanceCollection,
                    parse_obj_as(
                        type_=TaskInstanceCollection,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
