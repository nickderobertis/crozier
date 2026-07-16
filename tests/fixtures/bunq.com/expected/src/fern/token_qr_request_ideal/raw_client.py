

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.token_qr_request_ideal_create import TokenQrRequestIdealCreate
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTokenQrRequestIdealClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_token_qr_request_ideal_for_user(
        self, user_id: int, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TokenQrRequestIdealCreate]:
        """
        Create a request from an ideal transaction.

        Parameters
        ----------
        user_id : int


        token : str
            The token passed from a site or read from a QR code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TokenQrRequestIdealCreate]
            Using this call you create a request for payment from an external token provided with an ideal transaction. Make sure your iDEAL payments are compliant with the iDEAL standards, by following the following manual: https:/www.bunq.com/terms-idealstandards. It's very important to keep these points in mind when you are using the endpoint to make iDEAL payments from your application.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/token-qr-request-ideal",
            method="POST",
            json={
                "token": token,
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
                    TokenQrRequestIdealCreate,
                    parse_obj_as(
                        type_=TokenQrRequestIdealCreate,
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


class AsyncRawTokenQrRequestIdealClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_token_qr_request_ideal_for_user(
        self, user_id: int, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TokenQrRequestIdealCreate]:
        """
        Create a request from an ideal transaction.

        Parameters
        ----------
        user_id : int


        token : str
            The token passed from a site or read from a QR code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TokenQrRequestIdealCreate]
            Using this call you create a request for payment from an external token provided with an ideal transaction. Make sure your iDEAL payments are compliant with the iDEAL standards, by following the following manual: https:/www.bunq.com/terms-idealstandards. It's very important to keep these points in mind when you are using the endpoint to make iDEAL payments from your application.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/token-qr-request-ideal",
            method="POST",
            json={
                "token": token,
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
                    TokenQrRequestIdealCreate,
                    parse_obj_as(
                        type_=TokenQrRequestIdealCreate,
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
