

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.core_hover_card_get_user200response import CoreHoverCardGetUser200Response
from pydantic import ValidationError


class RawCoreHoverCardClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreHoverCardGetUser200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreHoverCardGetUser200Response]
            User details returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/hovercard/v1/{encode_path_param(user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreHoverCardGetUser200Response,
                    parse_obj_as(
                        type_=CoreHoverCardGetUser200Response,
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


class AsyncRawCoreHoverCardClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreHoverCardGetUser200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreHoverCardGetUser200Response]
            User details returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/hovercard/v1/{encode_path_param(user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreHoverCardGetUser200Response,
                    parse_obj_as(
                        type_=CoreHoverCardGetUser200Response,
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
