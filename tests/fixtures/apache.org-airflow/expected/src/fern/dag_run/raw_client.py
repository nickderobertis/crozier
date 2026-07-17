

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.dag_run import DagRun
from ..types.dag_run_collection import DagRunCollection
from ..types.dag_run_run_type import DagRunRunType
from ..types.dag_state import DagState
from ..types.dataset_event_collection import DatasetEventCollection
from ..types.error import Error
from .types.update_dag_run_state_state import UpdateDagRunStateState
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDagRunClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_dag_runs(
        self,
        dag_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        execution_date_gte: typing.Optional[dt.datetime] = None,
        execution_date_lte: typing.Optional[dt.datetime] = None,
        start_date_gte: typing.Optional[dt.datetime] = None,
        start_date_lte: typing.Optional[dt.datetime] = None,
        end_date_gte: typing.Optional[dt.datetime] = None,
        end_date_lte: typing.Optional[dt.datetime] = None,
        state: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DagRunCollection]:
        """
        This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

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

        state : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DagRunCollection]
            List of DAG runs.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id)}/dagRuns",
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
                "state": state,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DagRunCollection,
                    parse_obj_as(
                        type_=DagRunCollection,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_dag_run(
        self,
        dag_id_: str,
        *,
        conf: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        dag_id: typing.Optional[str] = OMIT,
        dag_run_id: typing.Optional[str] = OMIT,
        data_interval_end: typing.Optional[dt.datetime] = OMIT,
        data_interval_start: typing.Optional[dt.datetime] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        execution_date: typing.Optional[dt.datetime] = OMIT,
        external_trigger: typing.Optional[bool] = OMIT,
        last_scheduling_decision: typing.Optional[dt.datetime] = OMIT,
        logical_date: typing.Optional[dt.datetime] = OMIT,
        note: typing.Optional[str] = OMIT,
        run_type: typing.Optional[DagRunRunType] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        state: typing.Optional[DagState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DagRun]:
        """
        Parameters
        ----------
        dag_id_ : str
            The DAG ID.

        conf : typing.Optional[typing.Dict[str, typing.Any]]
            JSON object describing additional configuration parameters.

            The value of this field can be set only when creating the object. If you try to modify the
            field of an existing object, the request fails with an BAD_REQUEST error.

        dag_id : typing.Optional[str]

        dag_run_id : typing.Optional[str]
            Run ID.

            The value of this field can be set only when creating the object. If you try to modify the
            field of an existing object, the request fails with an BAD_REQUEST error.

            If not provided, a value will be generated based on execution_date.

            If the specified dag_run_id is in use, the creation request fails with an ALREADY_EXISTS error.

            This together with DAG_ID are a unique key.

        data_interval_end : typing.Optional[dt.datetime]

        data_interval_start : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        execution_date : typing.Optional[dt.datetime]
            The execution date. This is the same as logical_date, kept for backwards compatibility.
            If both this field and logical_date are provided but with different values, the request
            will fail with an BAD_REQUEST error.

            *Changed in version 2.2.0*&#58; Field becomes nullable.

            *Deprecated since version 2.2.0*&#58; Use 'logical_date' instead.

        external_trigger : typing.Optional[bool]

        last_scheduling_decision : typing.Optional[dt.datetime]

        logical_date : typing.Optional[dt.datetime]
            The logical date (previously called execution date). This is the time or interval covered by
            this DAG run, according to the DAG definition.

            The value of this field can be set only when creating the object. If you try to modify the
            field of an existing object, the request fails with an BAD_REQUEST error.

            This together with DAG_ID are a unique key.

            *New in version 2.2.0*

        note : typing.Optional[str]
            Contains manually entered notes by the user about the DagRun.

            *New in version 2.5.0*

        run_type : typing.Optional[DagRunRunType]

        start_date : typing.Optional[dt.datetime]
            The start time. The time when DAG run was actually created.

            *Changed in version 2.1.3*&#58; Field becomes nullable.

        state : typing.Optional[DagState]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DagRun]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id_)}/dagRuns",
            method="POST",
            json={
                "conf": conf,
                "dag_id": dag_id,
                "dag_run_id": dag_run_id,
                "data_interval_end": data_interval_end,
                "data_interval_start": data_interval_start,
                "end_date": end_date,
                "execution_date": execution_date,
                "external_trigger": external_trigger,
                "last_scheduling_decision": last_scheduling_decision,
                "logical_date": logical_date,
                "note": note,
                "run_type": run_type,
                "start_date": start_date,
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
                    DagRun,
                    parse_obj_as(
                        type_=DagRun,
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
            if _response.status_code == 409:
                raise ConflictError(
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_dag_run(
        self, dag_id: str, dag_run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DagRun]:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DagRun]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id)}/dagRuns/{encode_path_param(dag_run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DagRun,
                    parse_obj_as(
                        type_=DagRun,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_dag_run(
        self, dag_id: str, dag_run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id)}/dagRuns/{encode_path_param(dag_run_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_dag_run_state(
        self,
        dag_id: str,
        dag_run_id: str,
        *,
        state: typing.Optional[UpdateDagRunStateState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DagRun]:
        """
        Modify a DAG run.

        *New in version 2.2.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        state : typing.Optional[UpdateDagRunStateState]
            The state to set this DagRun

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DagRun]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id)}/dagRuns/{encode_path_param(dag_run_id)}",
            method="PATCH",
            json={
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
                    DagRun,
                    parse_obj_as(
                        type_=DagRun,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def clear_dag_run(
        self,
        dag_id: str,
        dag_run_id: str,
        *,
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DagRun]:
        """
        Clear a DAG run.

        *New in version 2.4.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        dry_run : typing.Optional[bool]
            If set, don't actually run this operation. The response will contain a list of task instances
            planned to be cleaned, but not modified in any way.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DagRun]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id)}/dagRuns/{encode_path_param(dag_run_id)}/clear",
            method="POST",
            json={
                "dry_run": dry_run,
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
                    DagRun,
                    parse_obj_as(
                        type_=DagRun,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def set_dag_run_note(
        self,
        dag_id: str,
        dag_run_id: str,
        *,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DagRun]:
        """
        Update the manual user note of a DagRun.

        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        note : typing.Optional[str]
            Custom notes left by users for this Dag Run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DagRun]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id)}/dagRuns/{encode_path_param(dag_run_id)}/setNote",
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
                    DagRun,
                    parse_obj_as(
                        type_=DagRun,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_upstream_dataset_events(
        self, dag_id: str, dag_run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DatasetEventCollection]:
        """
        Get datasets for a dag run.

        *New in version 2.4.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DatasetEventCollection]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id)}/dagRuns/{encode_path_param(dag_run_id)}/upstreamDatasetEvents",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DatasetEventCollection,
                    parse_obj_as(
                        type_=DatasetEventCollection,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_dag_runs_batch(
        self,
        *,
        dag_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        end_date_gte: typing.Optional[dt.datetime] = OMIT,
        end_date_lte: typing.Optional[dt.datetime] = OMIT,
        execution_date_gte: typing.Optional[dt.datetime] = OMIT,
        execution_date_lte: typing.Optional[dt.datetime] = OMIT,
        order_by: typing.Optional[str] = OMIT,
        page_limit: typing.Optional[int] = OMIT,
        page_offset: typing.Optional[int] = OMIT,
        start_date_gte: typing.Optional[dt.datetime] = OMIT,
        start_date_lte: typing.Optional[dt.datetime] = OMIT,
        states: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DagRunCollection]:
        """
        This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limit.

        Parameters
        ----------
        dag_ids : typing.Optional[typing.Sequence[str]]
            Return objects with specific DAG IDs.
            The value can be repeated to retrieve multiple matching values (OR condition).

        end_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with end_date_lte parameter to receive only the selected period.

        end_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with end_date_gte parameter to receive only the selected period.

        execution_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal to the specified date.

            This can be combined with execution_date_lte key to receive only the selected period.

        execution_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with execution_date_gte key to receive only the selected period.

        order_by : typing.Optional[str]
            The name of the field to order the results by. Prefix a field name
            with `-` to reverse the sort order.

            *New in version 2.1.0*

        page_limit : typing.Optional[int]
            The numbers of items to return.

        page_offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        start_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte key to receive only the selected period.

        start_date_lte : typing.Optional[dt.datetime]
            Returns objects less or equal the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period

        states : typing.Optional[typing.Sequence[str]]
            Return objects with specific states.
            The value can be repeated to retrieve multiple matching values (OR condition).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DagRunCollection]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "dags/~/dagRuns/list",
            method="POST",
            json={
                "dag_ids": dag_ids,
                "end_date_gte": end_date_gte,
                "end_date_lte": end_date_lte,
                "execution_date_gte": execution_date_gte,
                "execution_date_lte": execution_date_lte,
                "order_by": order_by,
                "page_limit": page_limit,
                "page_offset": page_offset,
                "start_date_gte": start_date_gte,
                "start_date_lte": start_date_lte,
                "states": states,
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
                    DagRunCollection,
                    parse_obj_as(
                        type_=DagRunCollection,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawDagRunClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_dag_runs(
        self,
        dag_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        execution_date_gte: typing.Optional[dt.datetime] = None,
        execution_date_lte: typing.Optional[dt.datetime] = None,
        start_date_gte: typing.Optional[dt.datetime] = None,
        start_date_lte: typing.Optional[dt.datetime] = None,
        end_date_gte: typing.Optional[dt.datetime] = None,
        end_date_lte: typing.Optional[dt.datetime] = None,
        state: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DagRunCollection]:
        """
        This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

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

        state : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DagRunCollection]
            List of DAG runs.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id)}/dagRuns",
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
                "state": state,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DagRunCollection,
                    parse_obj_as(
                        type_=DagRunCollection,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_dag_run(
        self,
        dag_id_: str,
        *,
        conf: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        dag_id: typing.Optional[str] = OMIT,
        dag_run_id: typing.Optional[str] = OMIT,
        data_interval_end: typing.Optional[dt.datetime] = OMIT,
        data_interval_start: typing.Optional[dt.datetime] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        execution_date: typing.Optional[dt.datetime] = OMIT,
        external_trigger: typing.Optional[bool] = OMIT,
        last_scheduling_decision: typing.Optional[dt.datetime] = OMIT,
        logical_date: typing.Optional[dt.datetime] = OMIT,
        note: typing.Optional[str] = OMIT,
        run_type: typing.Optional[DagRunRunType] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        state: typing.Optional[DagState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DagRun]:
        """
        Parameters
        ----------
        dag_id_ : str
            The DAG ID.

        conf : typing.Optional[typing.Dict[str, typing.Any]]
            JSON object describing additional configuration parameters.

            The value of this field can be set only when creating the object. If you try to modify the
            field of an existing object, the request fails with an BAD_REQUEST error.

        dag_id : typing.Optional[str]

        dag_run_id : typing.Optional[str]
            Run ID.

            The value of this field can be set only when creating the object. If you try to modify the
            field of an existing object, the request fails with an BAD_REQUEST error.

            If not provided, a value will be generated based on execution_date.

            If the specified dag_run_id is in use, the creation request fails with an ALREADY_EXISTS error.

            This together with DAG_ID are a unique key.

        data_interval_end : typing.Optional[dt.datetime]

        data_interval_start : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        execution_date : typing.Optional[dt.datetime]
            The execution date. This is the same as logical_date, kept for backwards compatibility.
            If both this field and logical_date are provided but with different values, the request
            will fail with an BAD_REQUEST error.

            *Changed in version 2.2.0*&#58; Field becomes nullable.

            *Deprecated since version 2.2.0*&#58; Use 'logical_date' instead.

        external_trigger : typing.Optional[bool]

        last_scheduling_decision : typing.Optional[dt.datetime]

        logical_date : typing.Optional[dt.datetime]
            The logical date (previously called execution date). This is the time or interval covered by
            this DAG run, according to the DAG definition.

            The value of this field can be set only when creating the object. If you try to modify the
            field of an existing object, the request fails with an BAD_REQUEST error.

            This together with DAG_ID are a unique key.

            *New in version 2.2.0*

        note : typing.Optional[str]
            Contains manually entered notes by the user about the DagRun.

            *New in version 2.5.0*

        run_type : typing.Optional[DagRunRunType]

        start_date : typing.Optional[dt.datetime]
            The start time. The time when DAG run was actually created.

            *Changed in version 2.1.3*&#58; Field becomes nullable.

        state : typing.Optional[DagState]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DagRun]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id_)}/dagRuns",
            method="POST",
            json={
                "conf": conf,
                "dag_id": dag_id,
                "dag_run_id": dag_run_id,
                "data_interval_end": data_interval_end,
                "data_interval_start": data_interval_start,
                "end_date": end_date,
                "execution_date": execution_date,
                "external_trigger": external_trigger,
                "last_scheduling_decision": last_scheduling_decision,
                "logical_date": logical_date,
                "note": note,
                "run_type": run_type,
                "start_date": start_date,
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
                    DagRun,
                    parse_obj_as(
                        type_=DagRun,
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
            if _response.status_code == 409:
                raise ConflictError(
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_dag_run(
        self, dag_id: str, dag_run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DagRun]:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DagRun]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id)}/dagRuns/{encode_path_param(dag_run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DagRun,
                    parse_obj_as(
                        type_=DagRun,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_dag_run(
        self, dag_id: str, dag_run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id)}/dagRuns/{encode_path_param(dag_run_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_dag_run_state(
        self,
        dag_id: str,
        dag_run_id: str,
        *,
        state: typing.Optional[UpdateDagRunStateState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DagRun]:
        """
        Modify a DAG run.

        *New in version 2.2.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        state : typing.Optional[UpdateDagRunStateState]
            The state to set this DagRun

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DagRun]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id)}/dagRuns/{encode_path_param(dag_run_id)}",
            method="PATCH",
            json={
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
                    DagRun,
                    parse_obj_as(
                        type_=DagRun,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def clear_dag_run(
        self,
        dag_id: str,
        dag_run_id: str,
        *,
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DagRun]:
        """
        Clear a DAG run.

        *New in version 2.4.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        dry_run : typing.Optional[bool]
            If set, don't actually run this operation. The response will contain a list of task instances
            planned to be cleaned, but not modified in any way.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DagRun]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id)}/dagRuns/{encode_path_param(dag_run_id)}/clear",
            method="POST",
            json={
                "dry_run": dry_run,
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
                    DagRun,
                    parse_obj_as(
                        type_=DagRun,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def set_dag_run_note(
        self,
        dag_id: str,
        dag_run_id: str,
        *,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DagRun]:
        """
        Update the manual user note of a DagRun.

        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        note : typing.Optional[str]
            Custom notes left by users for this Dag Run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DagRun]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id)}/dagRuns/{encode_path_param(dag_run_id)}/setNote",
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
                    DagRun,
                    parse_obj_as(
                        type_=DagRun,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_upstream_dataset_events(
        self, dag_id: str, dag_run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DatasetEventCollection]:
        """
        Get datasets for a dag run.

        *New in version 2.4.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DatasetEventCollection]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id)}/dagRuns/{encode_path_param(dag_run_id)}/upstreamDatasetEvents",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DatasetEventCollection,
                    parse_obj_as(
                        type_=DatasetEventCollection,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_dag_runs_batch(
        self,
        *,
        dag_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        end_date_gte: typing.Optional[dt.datetime] = OMIT,
        end_date_lte: typing.Optional[dt.datetime] = OMIT,
        execution_date_gte: typing.Optional[dt.datetime] = OMIT,
        execution_date_lte: typing.Optional[dt.datetime] = OMIT,
        order_by: typing.Optional[str] = OMIT,
        page_limit: typing.Optional[int] = OMIT,
        page_offset: typing.Optional[int] = OMIT,
        start_date_gte: typing.Optional[dt.datetime] = OMIT,
        start_date_lte: typing.Optional[dt.datetime] = OMIT,
        states: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DagRunCollection]:
        """
        This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limit.

        Parameters
        ----------
        dag_ids : typing.Optional[typing.Sequence[str]]
            Return objects with specific DAG IDs.
            The value can be repeated to retrieve multiple matching values (OR condition).

        end_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with end_date_lte parameter to receive only the selected period.

        end_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with end_date_gte parameter to receive only the selected period.

        execution_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal to the specified date.

            This can be combined with execution_date_lte key to receive only the selected period.

        execution_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with execution_date_gte key to receive only the selected period.

        order_by : typing.Optional[str]
            The name of the field to order the results by. Prefix a field name
            with `-` to reverse the sort order.

            *New in version 2.1.0*

        page_limit : typing.Optional[int]
            The numbers of items to return.

        page_offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        start_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte key to receive only the selected period.

        start_date_lte : typing.Optional[dt.datetime]
            Returns objects less or equal the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period

        states : typing.Optional[typing.Sequence[str]]
            Return objects with specific states.
            The value can be repeated to retrieve multiple matching values (OR condition).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DagRunCollection]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "dags/~/dagRuns/list",
            method="POST",
            json={
                "dag_ids": dag_ids,
                "end_date_gte": end_date_gte,
                "end_date_lte": end_date_lte,
                "execution_date_gte": execution_date_gte,
                "execution_date_lte": execution_date_lte,
                "order_by": order_by,
                "page_limit": page_limit,
                "page_offset": page_offset,
                "start_date_gte": start_date_gte,
                "start_date_lte": start_date_lte,
                "states": states,
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
                    DagRunCollection,
                    parse_obj_as(
                        type_=DagRunCollection,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
