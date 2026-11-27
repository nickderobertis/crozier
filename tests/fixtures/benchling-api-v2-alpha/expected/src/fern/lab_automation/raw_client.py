

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.connection_files_paginated_list import ConnectionFilesPaginatedList
from .types.list_connect_files_request_data_type import ListConnectFilesRequestDataType
from pydantic import ValidationError


class RawLabAutomationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_connect_files(
        self,
        *,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        created_at_lte: typing.Optional[str] = None,
        created_at_gte: typing.Optional[str] = None,
        modified_at_lt: typing.Optional[str] = None,
        modified_at_gt: typing.Optional[str] = None,
        modified_at_lte: typing.Optional[str] = None,
        modified_at_gte: typing.Optional[str] = None,
        filename_includes: typing.Optional[str] = None,
        connection_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        connection_schema_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        data_type: typing.Optional[ListConnectFilesRequestDataType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConnectionFilesPaginatedList]:
        """
        List Benchling Connect files

        Parameters
        ----------
        page_size : typing.Optional[int]
            Number of results to return. Defaults to 50, maximum of 100.

        next_token : typing.Optional[str]
            Token for pagination

        created_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created before the specified time. e.g. < 2017-04-30.

        created_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created after the specified time. e.g. > 2017-04-30.

        created_at_lte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created on or before the specified time. e.g. <= 2017-04-30.

        created_at_gte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created on or after the specified time. e.g. >= 2017-04-30.

        modified_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified before the specified time. e.g. < 2017-04-30.

        modified_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified after the specified time. e.g. > 2017-04-30.

        modified_at_lte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or before the specified time. e.g. <= 2017-04-30.

        modified_at_gte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or after the specified time. e.g. >= 2017-04-30.

        filename_includes : typing.Optional[str]
            Name substring of a file. Restricts results to those with names that include the provided substring.

        connection_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Comma-separated list of connection IDs. Restricts results to those created by the given connections.

        connection_schema_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Comma-separated list of connection schema IDs. Restricts results to those created by connections with the given connection schemas.

        data_type : typing.Optional[ListConnectFilesRequestDataType]
            File data type. Restricts results to those with the specified data type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConnectionFilesPaginatedList]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "benchling-connect/connection-files",
            method="GET",
            params={
                "pageSize": page_size,
                "nextToken": next_token,
                "createdAt.lt": created_at_lt,
                "createdAt.gt": created_at_gt,
                "createdAt.lte": created_at_lte,
                "createdAt.gte": created_at_gte,
                "modifiedAt.lt": modified_at_lt,
                "modifiedAt.gt": modified_at_gt,
                "modifiedAt.lte": modified_at_lte,
                "modifiedAt.gte": modified_at_gte,
                "filenameIncludes": filename_includes,
                "connectionIds": connection_ids,
                "connectionSchemaIds": connection_schema_ids,
                "dataType": data_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConnectionFilesPaginatedList,
                    parse_obj_as(
                        type_=ConnectionFilesPaginatedList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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


class AsyncRawLabAutomationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_connect_files(
        self,
        *,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        created_at_lte: typing.Optional[str] = None,
        created_at_gte: typing.Optional[str] = None,
        modified_at_lt: typing.Optional[str] = None,
        modified_at_gt: typing.Optional[str] = None,
        modified_at_lte: typing.Optional[str] = None,
        modified_at_gte: typing.Optional[str] = None,
        filename_includes: typing.Optional[str] = None,
        connection_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        connection_schema_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        data_type: typing.Optional[ListConnectFilesRequestDataType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConnectionFilesPaginatedList]:
        """
        List Benchling Connect files

        Parameters
        ----------
        page_size : typing.Optional[int]
            Number of results to return. Defaults to 50, maximum of 100.

        next_token : typing.Optional[str]
            Token for pagination

        created_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created before the specified time. e.g. < 2017-04-30.

        created_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created after the specified time. e.g. > 2017-04-30.

        created_at_lte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created on or before the specified time. e.g. <= 2017-04-30.

        created_at_gte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created on or after the specified time. e.g. >= 2017-04-30.

        modified_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified before the specified time. e.g. < 2017-04-30.

        modified_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified after the specified time. e.g. > 2017-04-30.

        modified_at_lte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or before the specified time. e.g. <= 2017-04-30.

        modified_at_gte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or after the specified time. e.g. >= 2017-04-30.

        filename_includes : typing.Optional[str]
            Name substring of a file. Restricts results to those with names that include the provided substring.

        connection_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Comma-separated list of connection IDs. Restricts results to those created by the given connections.

        connection_schema_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Comma-separated list of connection schema IDs. Restricts results to those created by connections with the given connection schemas.

        data_type : typing.Optional[ListConnectFilesRequestDataType]
            File data type. Restricts results to those with the specified data type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConnectionFilesPaginatedList]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "benchling-connect/connection-files",
            method="GET",
            params={
                "pageSize": page_size,
                "nextToken": next_token,
                "createdAt.lt": created_at_lt,
                "createdAt.gt": created_at_gt,
                "createdAt.lte": created_at_lte,
                "createdAt.gte": created_at_gte,
                "modifiedAt.lt": modified_at_lt,
                "modifiedAt.gt": modified_at_gt,
                "modifiedAt.lte": modified_at_lte,
                "modifiedAt.gte": modified_at_gte,
                "filenameIncludes": filename_includes,
                "connectionIds": connection_ids,
                "connectionSchemaIds": connection_schema_ids,
                "dataType": data_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConnectionFilesPaginatedList,
                    parse_obj_as(
                        type_=ConnectionFilesPaginatedList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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
