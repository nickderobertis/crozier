

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_paged_response_update_system_models_available_update_group_subscription import (
    ApiPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription,
)
from ..types.api_paged_response_update_system_models_update_group_subscription import (
    ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription,
)
from ..types.update_system_models_client import UpdateSystemModelsClient
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawClientsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateSystemModelsClient]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSystemModelsClient]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Clients/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsClient,
                    parse_obj_as(
                        type_=UpdateSystemModelsClient,
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

    def put(
        self,
        id: str,
        *,
        client_id: typing.Optional[str] = OMIT,
        last_checkin: typing.Optional[dt.datetime] = OMIT,
        tag: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        client_id : typing.Optional[str]
            Read Only. The id of the client

        last_checkin : typing.Optional[dt.datetime]
            Read Only. The time of the client's last checkin with the server.

        tag : typing.Optional[str]
            A description of the client that can be used for easy reference

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Clients/{encode_path_param(id)}",
            method="PUT",
            json={
                "ClientID": client_id,
                "LastCheckin": last_checkin,
                "Tag": tag,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getavailablesubscriptions(
        self,
        id: str,
        *,
        update_group_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Clients/{encode_path_param(id)}/AvailableUpdateGroupSubscriptions",
            method="GET",
            params={
                "UpdateGroupID": update_group_id,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription,
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

    def getsubscriptions(
        self,
        id: str,
        *,
        update_group_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Clients/{encode_path_param(id)}/UpdateGroupSubscriptions",
            method="GET",
            params={
                "UpdateGroupID": update_group_id,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription,
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


class AsyncRawClientsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateSystemModelsClient]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSystemModelsClient]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Clients/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsClient,
                    parse_obj_as(
                        type_=UpdateSystemModelsClient,
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

    async def put(
        self,
        id: str,
        *,
        client_id: typing.Optional[str] = OMIT,
        last_checkin: typing.Optional[dt.datetime] = OMIT,
        tag: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        client_id : typing.Optional[str]
            Read Only. The id of the client

        last_checkin : typing.Optional[dt.datetime]
            Read Only. The time of the client's last checkin with the server.

        tag : typing.Optional[str]
            A description of the client that can be used for easy reference

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Clients/{encode_path_param(id)}",
            method="PUT",
            json={
                "ClientID": client_id,
                "LastCheckin": last_checkin,
                "Tag": tag,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getavailablesubscriptions(
        self,
        id: str,
        *,
        update_group_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Clients/{encode_path_param(id)}/AvailableUpdateGroupSubscriptions",
            method="GET",
            params={
                "UpdateGroupID": update_group_id,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription,
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

    async def getsubscriptions(
        self,
        id: str,
        *,
        update_group_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Clients/{encode_path_param(id)}/UpdateGroupSubscriptions",
            method="GET",
            params={
                "UpdateGroupID": update_group_id,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription,
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
