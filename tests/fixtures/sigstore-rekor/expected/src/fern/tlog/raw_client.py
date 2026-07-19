

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.error import Error
from pydantic import ValidationError


class RawTlogClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_log_info(
        self, *, stable: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Error]:
        """
        Returns the current root hash and size of the merkle tree used to store the log entries.

        Parameters
        ----------
        stable : typing.Optional[bool]
            Whether to return a stable checkpoint for the active shard

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Error]
            An issue occurred while processing the request.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/log",
            method="GET",
            params={
                "stable": stable,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Error,
                    parse_obj_as(
                        type_=Error,
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

    def get_log_proof(
        self,
        *,
        first_size: typing.Optional[int] = None,
        last_size: typing.Optional[int] = None,
        tree_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Error]:
        """
        Returns a list of hashes for specified tree sizes that can be used to confirm the consistency of the transparency log

        Parameters
        ----------
        first_size : typing.Optional[int]
            The size of the tree that you wish to prove consistency from (1 means the beginning of the log) Defaults to 1 if not specified

        last_size : typing.Optional[int]
            The size of the tree that you wish to prove consistency to

        tree_id : typing.Optional[str]
            The tree ID of the tree that you wish to prove consistency for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Error]
            An issue occurred while processing the request.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/log/proof",
            method="GET",
            params={
                "firstSize": first_size,
                "lastSize": last_size,
                "treeID": tree_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Error,
                    parse_obj_as(
                        type_=Error,
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


class AsyncRawTlogClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_log_info(
        self, *, stable: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Error]:
        """
        Returns the current root hash and size of the merkle tree used to store the log entries.

        Parameters
        ----------
        stable : typing.Optional[bool]
            Whether to return a stable checkpoint for the active shard

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Error]
            An issue occurred while processing the request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/log",
            method="GET",
            params={
                "stable": stable,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Error,
                    parse_obj_as(
                        type_=Error,
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

    async def get_log_proof(
        self,
        *,
        first_size: typing.Optional[int] = None,
        last_size: typing.Optional[int] = None,
        tree_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Error]:
        """
        Returns a list of hashes for specified tree sizes that can be used to confirm the consistency of the transparency log

        Parameters
        ----------
        first_size : typing.Optional[int]
            The size of the tree that you wish to prove consistency from (1 means the beginning of the log) Defaults to 1 if not specified

        last_size : typing.Optional[int]
            The size of the tree that you wish to prove consistency to

        tree_id : typing.Optional[str]
            The tree ID of the tree that you wish to prove consistency for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Error]
            An issue occurred while processing the request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/log/proof",
            method="GET",
            params={
                "firstSize": first_size,
                "lastSize": last_size,
                "treeID": tree_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Error,
                    parse_obj_as(
                        type_=Error,
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
