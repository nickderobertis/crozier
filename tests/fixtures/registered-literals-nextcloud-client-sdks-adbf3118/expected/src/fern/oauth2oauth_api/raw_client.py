

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.oauth2oauth_api_get_token200response import Oauth2OauthApiGetToken200Response
from pydantic import ValidationError


class RawOauth2OauthApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_token(
        self,
        *,
        grant_type: str,
        code: str,
        refresh_token: str,
        client_id: str,
        client_secret: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Oauth2OauthApiGetToken200Response]:
        """
        Parameters
        ----------
        grant_type : str
            Token type that should be granted

        code : str
            Code of the flow

        refresh_token : str
            Refresh token

        client_id : str
            Client ID

        client_secret : str
            Client secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Oauth2OauthApiGetToken200Response]
            Token returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "index.php/apps/oauth2/api/v1/token",
            method="POST",
            params={
                "grant_type": grant_type,
                "code": code,
                "refresh_token": refresh_token,
                "client_id": client_id,
                "client_secret": client_secret,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Oauth2OauthApiGetToken200Response,
                    parse_obj_as(
                        type_=Oauth2OauthApiGetToken200Response,
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


class AsyncRawOauth2OauthApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_token(
        self,
        *,
        grant_type: str,
        code: str,
        refresh_token: str,
        client_id: str,
        client_secret: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Oauth2OauthApiGetToken200Response]:
        """
        Parameters
        ----------
        grant_type : str
            Token type that should be granted

        code : str
            Code of the flow

        refresh_token : str
            Refresh token

        client_id : str
            Client ID

        client_secret : str
            Client secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Oauth2OauthApiGetToken200Response]
            Token returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "index.php/apps/oauth2/api/v1/token",
            method="POST",
            params={
                "grant_type": grant_type,
                "code": code,
                "refresh_token": refresh_token,
                "client_id": client_id,
                "client_secret": client_secret,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Oauth2OauthApiGetToken200Response,
                    parse_obj_as(
                        type_=Oauth2OauthApiGetToken200Response,
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
