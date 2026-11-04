

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.core_whats_new_dismiss200response import CoreWhatsNewDismiss200Response
from pydantic import ValidationError


class RawCoreProfileApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def set_visibility(
        self,
        target_user_id: str,
        *,
        param_id: str,
        visibility: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        target_user_id : str
            ID of the user

        param_id : str
            ID of the parameter

        visibility : str
            New visibility

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]
            Visibility updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/profile/{encode_path_param(target_user_id)}",
            method="PUT",
            params={
                "paramId": param_id,
                "visibility": visibility,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreWhatsNewDismiss200Response,
                    parse_obj_as(
                        type_=CoreWhatsNewDismiss200Response,
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


class AsyncRawCoreProfileApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def set_visibility(
        self,
        target_user_id: str,
        *,
        param_id: str,
        visibility: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        target_user_id : str
            ID of the user

        param_id : str
            ID of the parameter

        visibility : str
            New visibility

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]
            Visibility updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/profile/{encode_path_param(target_user_id)}",
            method="PUT",
            params={
                "paramId": param_id,
                "visibility": visibility,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreWhatsNewDismiss200Response,
                    parse_obj_as(
                        type_=CoreWhatsNewDismiss200Response,
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
