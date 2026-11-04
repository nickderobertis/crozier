

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.result_set import ResultSet
from .types.sqlite_batch_request_mode import SqliteBatchRequestMode
from .types.sqlite_batch_request_statements_item import SqliteBatchRequestStatementsItem
from .types.sqlite_execute_request_statement import SqliteExecuteRequestStatement
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSqliteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def execute(
        self, *, statement: SqliteExecuteRequestStatement, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResultSet]:
        """
        Execute a single SQLite statement and return results

        Parameters
        ----------
        statement : SqliteExecuteRequestStatement

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResultSet]
            Result of executing an SQL statement.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sqlite/execute",
            method="POST",
            json={
                "statement": convert_and_respect_annotation_metadata(
                    object_=statement, annotation=SqliteExecuteRequestStatement, direction="write"
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
                    ResultSet,
                    parse_obj_as(
                        type_=ResultSet,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def batch(
        self,
        *,
        statements: typing.Sequence[SqliteBatchRequestStatementsItem],
        mode: typing.Optional[SqliteBatchRequestMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ResultSet]]:
        """
        Execute a batch of SQLite statements and return results for all of them

        Parameters
        ----------
        statements : typing.Sequence[SqliteBatchRequestStatementsItem]

        mode : typing.Optional[SqliteBatchRequestMode]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ResultSet]]
            Array of results from the statements executed
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sqlite/batch",
            method="POST",
            json={
                "statements": convert_and_respect_annotation_metadata(
                    object_=statements, annotation=typing.Sequence[SqliteBatchRequestStatementsItem], direction="write"
                ),
                "mode": mode,
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
                    typing.List[ResultSet],
                    parse_obj_as(
                        type_=typing.List[ResultSet],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSqliteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def execute(
        self, *, statement: SqliteExecuteRequestStatement, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResultSet]:
        """
        Execute a single SQLite statement and return results

        Parameters
        ----------
        statement : SqliteExecuteRequestStatement

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResultSet]
            Result of executing an SQL statement.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sqlite/execute",
            method="POST",
            json={
                "statement": convert_and_respect_annotation_metadata(
                    object_=statement, annotation=SqliteExecuteRequestStatement, direction="write"
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
                    ResultSet,
                    parse_obj_as(
                        type_=ResultSet,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def batch(
        self,
        *,
        statements: typing.Sequence[SqliteBatchRequestStatementsItem],
        mode: typing.Optional[SqliteBatchRequestMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ResultSet]]:
        """
        Execute a batch of SQLite statements and return results for all of them

        Parameters
        ----------
        statements : typing.Sequence[SqliteBatchRequestStatementsItem]

        mode : typing.Optional[SqliteBatchRequestMode]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ResultSet]]
            Array of results from the statements executed
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sqlite/batch",
            method="POST",
            json={
                "statements": convert_and_respect_annotation_metadata(
                    object_=statements, annotation=typing.Sequence[SqliteBatchRequestStatementsItem], direction="write"
                ),
                "mode": mode,
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
                    typing.List[ResultSet],
                    parse_obj_as(
                        type_=typing.List[ResultSet],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
