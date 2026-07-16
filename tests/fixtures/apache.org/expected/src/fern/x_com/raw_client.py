

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from ..types.x_com import XCom
from ..types.x_com_collection import XComCollection
from pydantic import ValidationError


class RawXComClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_xcom_entries(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[XComCollection]:
        """
        This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCOM entries for for all DAGs, DAG runs and task instances. XCom values won't be returned as they can be large. Use this endpoint to get a list of XCom entries and then fetch individual entry to get value.

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

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[XComCollection]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id)}/dagRuns/{encode_path_param(dag_run_id)}/taskInstances/{encode_path_param(task_id)}/xcomEntries",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    XComCollection,
                    parse_obj_as(
                        type_=XComCollection,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_xcom_entry(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        xcom_key: str,
        *,
        deserialize: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[XCom]:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        xcom_key : str
            The XCom key.

        deserialize : typing.Optional[bool]
            Whether to deserialize an XCom value when using a custom XCom backend.

            The XCom API endpoint calls `orm_deserialize_value` by default since an XCom may contain value
            that is potentially expensive to deserialize in the web server. Setting this to true overrides
            the consideration, and calls `deserialize_value` instead.

            This parameter is not meaningful when using the default XCom backend.

            *New in version 2.4.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[XCom]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id)}/dagRuns/{encode_path_param(dag_run_id)}/taskInstances/{encode_path_param(task_id)}/xcomEntries/{encode_path_param(xcom_key)}",
            method="GET",
            params={
                "deserialize": deserialize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    XCom,
                    parse_obj_as(
                        type_=XCom,
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


class AsyncRawXComClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_xcom_entries(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[XComCollection]:
        """
        This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCOM entries for for all DAGs, DAG runs and task instances. XCom values won't be returned as they can be large. Use this endpoint to get a list of XCom entries and then fetch individual entry to get value.

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

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[XComCollection]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id)}/dagRuns/{encode_path_param(dag_run_id)}/taskInstances/{encode_path_param(task_id)}/xcomEntries",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    XComCollection,
                    parse_obj_as(
                        type_=XComCollection,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_xcom_entry(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        xcom_key: str,
        *,
        deserialize: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[XCom]:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        xcom_key : str
            The XCom key.

        deserialize : typing.Optional[bool]
            Whether to deserialize an XCom value when using a custom XCom backend.

            The XCom API endpoint calls `orm_deserialize_value` by default since an XCom may contain value
            that is potentially expensive to deserialize in the web server. Setting this to true overrides
            the consideration, and calls `deserialize_value` instead.

            This parameter is not meaningful when using the default XCom backend.

            *New in version 2.4.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[XCom]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dags/{encode_path_param(dag_id)}/dagRuns/{encode_path_param(dag_run_id)}/taskInstances/{encode_path_param(task_id)}/xcomEntries/{encode_path_param(xcom_key)}",
            method="GET",
            params={
                "deserialize": deserialize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    XCom,
                    parse_obj_as(
                        type_=XCom,
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
