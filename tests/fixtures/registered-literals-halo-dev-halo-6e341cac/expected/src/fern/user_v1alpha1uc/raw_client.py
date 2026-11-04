

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.uc_user_vo import UcUserVo
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUserV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_my_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[UcUserVo]:
        """
        Get current user profile without password hash.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UcUserVo]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/uc.api.halo.run/v1alpha1/users/-",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UcUserVo,
                    parse_obj_as(
                        type_=UcUserVo,
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

    def change_my_password(
        self,
        *,
        password: str,
        old_password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UcUserVo]:
        """
        Set or change the password of the current user.

        Parameters
        ----------
        password : str
            new password of the current user

        old_password : typing.Optional[str]
            Old password. Required and verified only when the current user has a password; ignored otherwise.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UcUserVo]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/uc.api.halo.run/v1alpha1/users/-/password",
            method="PUT",
            json={
                "oldPassword": old_password,
                "password": password,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UcUserVo,
                    parse_obj_as(
                        type_=UcUserVo,
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


class AsyncRawUserV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_my_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UcUserVo]:
        """
        Get current user profile without password hash.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UcUserVo]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/uc.api.halo.run/v1alpha1/users/-",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UcUserVo,
                    parse_obj_as(
                        type_=UcUserVo,
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

    async def change_my_password(
        self,
        *,
        password: str,
        old_password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UcUserVo]:
        """
        Set or change the password of the current user.

        Parameters
        ----------
        password : str
            new password of the current user

        old_password : typing.Optional[str]
            Old password. Required and verified only when the current user has a password; ignored otherwise.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UcUserVo]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/uc.api.halo.run/v1alpha1/users/-/password",
            method="PUT",
            json={
                "oldPassword": old_password,
                "password": password,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UcUserVo,
                    parse_obj_as(
                        type_=UcUserVo,
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
