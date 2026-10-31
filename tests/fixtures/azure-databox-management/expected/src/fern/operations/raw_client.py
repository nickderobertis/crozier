

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.operation_list import OperationList
from pydantic import ValidationError


class RawOperationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OperationList]:
        """
        This method gets all the operations.

        Parameters
        ----------
        api_version : str
            The API Version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OperationList]
            The supported operations list.
        """
        _response = self._client_wrapper.httpx_client.request(
            "providers/Microsoft.DataBox/operations",
            method="GET",
            params={
                "api-version": api_version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OperationList,
                    parse_obj_as(
                        type_=OperationList,
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


class AsyncRawOperationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OperationList]:
        """
        This method gets all the operations.

        Parameters
        ----------
        api_version : str
            The API Version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OperationList]
            The supported operations list.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "providers/Microsoft.DataBox/operations",
            method="GET",
            params={
                "api-version": api_version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OperationList,
                    parse_obj_as(
                        type_=OperationList,
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
