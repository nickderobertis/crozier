

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.connection import Connection
from ..types.connection_collection import ConnectionCollection
from ..types.connection_test import ConnectionTest
from ..types.error import Error


OMIT = typing.cast(typing.Any, ...)


class RawConnectionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_connections(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConnectionCollection]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConnectionCollection]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "connections",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConnectionCollection,
                    parse_obj_as(
                        type_=ConnectionCollection,
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

    def post_connection(
        self,
        *,
        extra: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        conn_type: typing.Optional[str] = OMIT,
        connection_id: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        login: typing.Optional[str] = OMIT,
        port: typing.Optional[int] = OMIT,
        schema: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Connection]:
        """
        Parameters
        ----------
        extra : typing.Optional[str]
            Other values that cannot be put into another field, e.g. RSA keys.

        password : typing.Optional[str]
            Password of the connection.

        conn_type : typing.Optional[str]
            The connection type.

        connection_id : typing.Optional[str]
            The connection ID.

        description : typing.Optional[str]
            The description of the connection.

        host : typing.Optional[str]
            Host of the connection.

        login : typing.Optional[str]
            Login of the connection.

        port : typing.Optional[int]
            Port of the connection.

        schema : typing.Optional[str]
            Schema of the connection.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Connection]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "connections",
            method="POST",
            json={
                "extra": extra,
                "password": password,
                "conn_type": conn_type,
                "connection_id": connection_id,
                "description": description,
                "host": host,
                "login": login,
                "port": port,
                "schema": schema,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Connection,
                    parse_obj_as(
                        type_=Connection,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def test_connection(
        self,
        *,
        extra: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        conn_type: typing.Optional[str] = OMIT,
        connection_id: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        login: typing.Optional[str] = OMIT,
        port: typing.Optional[int] = OMIT,
        schema: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConnectionTest]:
        """
        Test a connection.

        *New in version 2.2.0*

        Parameters
        ----------
        extra : typing.Optional[str]
            Other values that cannot be put into another field, e.g. RSA keys.

        password : typing.Optional[str]
            Password of the connection.

        conn_type : typing.Optional[str]
            The connection type.

        connection_id : typing.Optional[str]
            The connection ID.

        description : typing.Optional[str]
            The description of the connection.

        host : typing.Optional[str]
            Host of the connection.

        login : typing.Optional[str]
            Login of the connection.

        port : typing.Optional[int]
            Port of the connection.

        schema : typing.Optional[str]
            Schema of the connection.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConnectionTest]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "connections/test",
            method="POST",
            json={
                "extra": extra,
                "password": password,
                "conn_type": conn_type,
                "connection_id": connection_id,
                "description": description,
                "host": host,
                "login": login,
                "port": port,
                "schema": schema,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConnectionTest,
                    parse_obj_as(
                        type_=ConnectionTest,
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

    def get_connection(
        self, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Connection]:
        """
        Parameters
        ----------
        connection_id : str
            The connection ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Connection]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"connections/{jsonable_encoder(connection_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Connection,
                    parse_obj_as(
                        type_=Connection,
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

    def delete_connection(
        self, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        connection_id : str
            The connection ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"connections/{jsonable_encoder(connection_id)}",
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def patch_connection(
        self,
        connection_id_: str,
        *,
        update_mask: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        extra: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        conn_type: typing.Optional[str] = OMIT,
        connection_id: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        login: typing.Optional[str] = OMIT,
        port: typing.Optional[int] = OMIT,
        schema: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Connection]:
        """
        Parameters
        ----------
        connection_id_ : str
            The connection ID.

        update_mask : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The fields to update on the resource. If absent or empty, all modifiable fields are updated.
            A comma-separated list of fully qualified names of fields.

        extra : typing.Optional[str]
            Other values that cannot be put into another field, e.g. RSA keys.

        password : typing.Optional[str]
            Password of the connection.

        conn_type : typing.Optional[str]
            The connection type.

        connection_id : typing.Optional[str]
            The connection ID.

        description : typing.Optional[str]
            The description of the connection.

        host : typing.Optional[str]
            Host of the connection.

        login : typing.Optional[str]
            Login of the connection.

        port : typing.Optional[int]
            Port of the connection.

        schema : typing.Optional[str]
            Schema of the connection.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Connection]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"connections/{jsonable_encoder(connection_id_)}",
            method="PATCH",
            params={
                "update_mask": update_mask,
            },
            json={
                "extra": extra,
                "password": password,
                "conn_type": conn_type,
                "connection_id": connection_id,
                "description": description,
                "host": host,
                "login": login,
                "port": port,
                "schema": schema,
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
                    Connection,
                    parse_obj_as(
                        type_=Connection,
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


class AsyncRawConnectionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_connections(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConnectionCollection]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConnectionCollection]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "connections",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConnectionCollection,
                    parse_obj_as(
                        type_=ConnectionCollection,
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

    async def post_connection(
        self,
        *,
        extra: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        conn_type: typing.Optional[str] = OMIT,
        connection_id: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        login: typing.Optional[str] = OMIT,
        port: typing.Optional[int] = OMIT,
        schema: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Connection]:
        """
        Parameters
        ----------
        extra : typing.Optional[str]
            Other values that cannot be put into another field, e.g. RSA keys.

        password : typing.Optional[str]
            Password of the connection.

        conn_type : typing.Optional[str]
            The connection type.

        connection_id : typing.Optional[str]
            The connection ID.

        description : typing.Optional[str]
            The description of the connection.

        host : typing.Optional[str]
            Host of the connection.

        login : typing.Optional[str]
            Login of the connection.

        port : typing.Optional[int]
            Port of the connection.

        schema : typing.Optional[str]
            Schema of the connection.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Connection]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "connections",
            method="POST",
            json={
                "extra": extra,
                "password": password,
                "conn_type": conn_type,
                "connection_id": connection_id,
                "description": description,
                "host": host,
                "login": login,
                "port": port,
                "schema": schema,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Connection,
                    parse_obj_as(
                        type_=Connection,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def test_connection(
        self,
        *,
        extra: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        conn_type: typing.Optional[str] = OMIT,
        connection_id: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        login: typing.Optional[str] = OMIT,
        port: typing.Optional[int] = OMIT,
        schema: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConnectionTest]:
        """
        Test a connection.

        *New in version 2.2.0*

        Parameters
        ----------
        extra : typing.Optional[str]
            Other values that cannot be put into another field, e.g. RSA keys.

        password : typing.Optional[str]
            Password of the connection.

        conn_type : typing.Optional[str]
            The connection type.

        connection_id : typing.Optional[str]
            The connection ID.

        description : typing.Optional[str]
            The description of the connection.

        host : typing.Optional[str]
            Host of the connection.

        login : typing.Optional[str]
            Login of the connection.

        port : typing.Optional[int]
            Port of the connection.

        schema : typing.Optional[str]
            Schema of the connection.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConnectionTest]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "connections/test",
            method="POST",
            json={
                "extra": extra,
                "password": password,
                "conn_type": conn_type,
                "connection_id": connection_id,
                "description": description,
                "host": host,
                "login": login,
                "port": port,
                "schema": schema,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConnectionTest,
                    parse_obj_as(
                        type_=ConnectionTest,
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

    async def get_connection(
        self, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Connection]:
        """
        Parameters
        ----------
        connection_id : str
            The connection ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Connection]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"connections/{jsonable_encoder(connection_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Connection,
                    parse_obj_as(
                        type_=Connection,
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

    async def delete_connection(
        self, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        connection_id : str
            The connection ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"connections/{jsonable_encoder(connection_id)}",
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def patch_connection(
        self,
        connection_id_: str,
        *,
        update_mask: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        extra: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        conn_type: typing.Optional[str] = OMIT,
        connection_id: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        login: typing.Optional[str] = OMIT,
        port: typing.Optional[int] = OMIT,
        schema: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Connection]:
        """
        Parameters
        ----------
        connection_id_ : str
            The connection ID.

        update_mask : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The fields to update on the resource. If absent or empty, all modifiable fields are updated.
            A comma-separated list of fully qualified names of fields.

        extra : typing.Optional[str]
            Other values that cannot be put into another field, e.g. RSA keys.

        password : typing.Optional[str]
            Password of the connection.

        conn_type : typing.Optional[str]
            The connection type.

        connection_id : typing.Optional[str]
            The connection ID.

        description : typing.Optional[str]
            The description of the connection.

        host : typing.Optional[str]
            Host of the connection.

        login : typing.Optional[str]
            Login of the connection.

        port : typing.Optional[int]
            Port of the connection.

        schema : typing.Optional[str]
            Schema of the connection.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Connection]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"connections/{jsonable_encoder(connection_id_)}",
            method="PATCH",
            params={
                "update_mask": update_mask,
            },
            json={
                "extra": extra,
                "password": password,
                "conn_type": conn_type,
                "connection_id": connection_id,
                "description": description,
                "host": host,
                "login": login,
                "port": port,
                "schema": schema,
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
                    Connection,
                    parse_obj_as(
                        type_=Connection,
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
