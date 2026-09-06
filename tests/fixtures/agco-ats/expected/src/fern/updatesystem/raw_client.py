

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.update_system_models_checkin_result import UpdateSystemModelsCheckinResult
from pydantic import ValidationError


class RawUpdatesystemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getcachedfiles(
        self, client_id: str, *, expired: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The ClientID of the Client

        expired : bool
            Only Expired Files (true|false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Clients/{encode_path_param(client_id)}/CachedFiles",
            method="GET",
            params={
                "Expired": expired,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def getcheckin(
        self,
        *,
        client_id: str,
        preview: bool,
        run_all_inventories: typing.Optional[bool] = None,
        transaction_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateSystemModelsCheckinResult]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID to check-in.  If this is a new client ID it will be added to Clients.

        preview : bool
            Get Pkgs w\\o updating Datetimes(true|false)

        run_all_inventories : typing.Optional[bool]
            Force return inventories. Defaults to false.

        transaction_id : typing.Optional[str]
            Optional. The 'NextTransactionID' from the previous check-in. Used to detect duplicate client IDs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSystemModelsCheckinResult]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/UpdateSystem",
            method="GET",
            params={
                "ClientID": client_id,
                "Preview": preview,
                "RunAllInventories": run_all_inventories,
                "transactionID": transaction_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsCheckinResult,
                    parse_obj_as(
                        type_=UpdateSystemModelsCheckinResult,
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


class AsyncRawUpdatesystemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getcachedfiles(
        self, client_id: str, *, expired: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The ClientID of the Client

        expired : bool
            Only Expired Files (true|false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Clients/{encode_path_param(client_id)}/CachedFiles",
            method="GET",
            params={
                "Expired": expired,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def getcheckin(
        self,
        *,
        client_id: str,
        preview: bool,
        run_all_inventories: typing.Optional[bool] = None,
        transaction_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateSystemModelsCheckinResult]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID to check-in.  If this is a new client ID it will be added to Clients.

        preview : bool
            Get Pkgs w\\o updating Datetimes(true|false)

        run_all_inventories : typing.Optional[bool]
            Force return inventories. Defaults to false.

        transaction_id : typing.Optional[str]
            Optional. The 'NextTransactionID' from the previous check-in. Used to detect duplicate client IDs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSystemModelsCheckinResult]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/UpdateSystem",
            method="GET",
            params={
                "ClientID": client_id,
                "Preview": preview,
                "RunAllInventories": run_all_inventories,
                "transactionID": transaction_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsCheckinResult,
                    parse_obj_as(
                        type_=UpdateSystemModelsCheckinResult,
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
