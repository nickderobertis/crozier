

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.any_type import AnyType
from .types.begin_task_response import BeginTaskResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post(
        self,
        *,
        failure: str,
        profile_id: str,
        success: str,
        task_name: str,
        request: AnyType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BeginTaskResponse]:
        """
        Parameters
        ----------
        failure : str

        profile_id : str

        success : str

        task_name : str

        request : AnyType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BeginTaskResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            params={
                "failure": failure,
                "profileId": profile_id,
                "success": success,
                "taskName": task_name,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BeginTaskResponse,
                    parse_obj_as(
                        type_=BeginTaskResponse,
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post(
        self,
        *,
        failure: str,
        profile_id: str,
        success: str,
        task_name: str,
        request: AnyType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BeginTaskResponse]:
        """
        Parameters
        ----------
        failure : str

        profile_id : str

        success : str

        task_name : str

        request : AnyType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BeginTaskResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            params={
                "failure": failure,
                "profileId": profile_id,
                "success": success,
                "taskName": task_name,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BeginTaskResponse,
                    parse_obj_as(
                        type_=BeginTaskResponse,
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
