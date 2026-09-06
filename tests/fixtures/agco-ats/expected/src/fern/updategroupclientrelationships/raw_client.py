

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
from ..types.api_paged_response_update_system_models_update_group_client_relationship import (
    ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship,
)
from ..types.update_system_models_update_group_client_relationship import (
    UpdateSystemModelsUpdateGroupClientRelationship,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUpdategroupclientrelationshipsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getsubscriptions(
        self,
        *,
        client_id: typing.Optional[str] = None,
        update_group_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : typing.Optional[str]
            Optional. Filter by Client ID

        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group ID

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        active : typing.Optional[bool]
            Optional. Filter by Active

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/UpdateGroupClientRelationships",
            method="GET",
            params={
                "ClientID": client_id,
                "UpdateGroupID": update_group_id,
                "limit": limit,
                "offset": offset,
                "Active": active,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship,
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

    def postsubscription(
        self,
        *,
        client_id: str,
        update_group_id: str,
        active: typing.Optional[bool] = OMIT,
        last_checkin: typing.Optional[dt.datetime] = OMIT,
        relationship_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            Read Only after creation. The client id of the subscriber.

        update_group_id : str
            Read Only after creation. The update group to subscribe to.

        active : typing.Optional[bool]
            The subscription status.  The status is active by default.

        last_checkin : typing.Optional[dt.datetime]
            ReadOnly. The timestamp of the last checkin.

        relationship_id : typing.Optional[str]
            Read Only after creation. The relationship id.  A relationship id will be assigned if not provided on creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/UpdateGroupClientRelationships",
            method="POST",
            json={
                "Active": active,
                "ClientID": client_id,
                "LastCheckin": last_checkin,
                "RelationshipID": relationship_id,
                "UpdateGroupID": update_group_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    def putsubscriptionbyclientidupdategroupid(
        self,
        *,
        client_id: str,
        update_group_id: str,
        active: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID.  This can be a client ID that has not been registered yet.

        update_group_id : str
            The Update Group ID

        active : bool
            Subscribe the client to the Update Group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/UpdateGroupClientRelationships",
            method="PUT",
            params={
                "ClientID": client_id,
                "UpdateGroupID": update_group_id,
                "Active": active,
            },
            request_options=request_options,
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

    def getsubscription(
        self, relationship_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateSystemModelsUpdateGroupClientRelationship]:
        """
        No Documentation Found.

        Parameters
        ----------
        relationship_id : str
            The RelationshipID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSystemModelsUpdateGroupClientRelationship]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroupClientRelationships/{encode_path_param(relationship_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsUpdateGroupClientRelationship,
                    parse_obj_as(
                        type_=UpdateSystemModelsUpdateGroupClientRelationship,
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

    def putsubscription(
        self,
        relationship_id_: str,
        *,
        client_id: str,
        update_group_id: str,
        active: typing.Optional[bool] = OMIT,
        last_checkin: typing.Optional[dt.datetime] = OMIT,
        relationship_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        relationship_id_ : str
            The relationship id of the UpdateGroupClientRelationship

        client_id : str
            Read Only after creation. The client id of the subscriber.

        update_group_id : str
            Read Only after creation. The update group to subscribe to.

        active : typing.Optional[bool]
            The subscription status.  The status is active by default.

        last_checkin : typing.Optional[dt.datetime]
            ReadOnly. The timestamp of the last checkin.

        relationship_id : typing.Optional[str]
            Read Only after creation. The relationship id.  A relationship id will be assigned if not provided on creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroupClientRelationships/{encode_path_param(relationship_id_)}",
            method="PUT",
            json={
                "Active": active,
                "ClientID": client_id,
                "LastCheckin": last_checkin,
                "RelationshipID": relationship_id,
                "UpdateGroupID": update_group_id,
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


class AsyncRawUpdategroupclientrelationshipsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getsubscriptions(
        self,
        *,
        client_id: typing.Optional[str] = None,
        update_group_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : typing.Optional[str]
            Optional. Filter by Client ID

        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group ID

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        active : typing.Optional[bool]
            Optional. Filter by Active

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/UpdateGroupClientRelationships",
            method="GET",
            params={
                "ClientID": client_id,
                "UpdateGroupID": update_group_id,
                "limit": limit,
                "offset": offset,
                "Active": active,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship,
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

    async def postsubscription(
        self,
        *,
        client_id: str,
        update_group_id: str,
        active: typing.Optional[bool] = OMIT,
        last_checkin: typing.Optional[dt.datetime] = OMIT,
        relationship_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            Read Only after creation. The client id of the subscriber.

        update_group_id : str
            Read Only after creation. The update group to subscribe to.

        active : typing.Optional[bool]
            The subscription status.  The status is active by default.

        last_checkin : typing.Optional[dt.datetime]
            ReadOnly. The timestamp of the last checkin.

        relationship_id : typing.Optional[str]
            Read Only after creation. The relationship id.  A relationship id will be assigned if not provided on creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/UpdateGroupClientRelationships",
            method="POST",
            json={
                "Active": active,
                "ClientID": client_id,
                "LastCheckin": last_checkin,
                "RelationshipID": relationship_id,
                "UpdateGroupID": update_group_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    async def putsubscriptionbyclientidupdategroupid(
        self,
        *,
        client_id: str,
        update_group_id: str,
        active: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID.  This can be a client ID that has not been registered yet.

        update_group_id : str
            The Update Group ID

        active : bool
            Subscribe the client to the Update Group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/UpdateGroupClientRelationships",
            method="PUT",
            params={
                "ClientID": client_id,
                "UpdateGroupID": update_group_id,
                "Active": active,
            },
            request_options=request_options,
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

    async def getsubscription(
        self, relationship_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateSystemModelsUpdateGroupClientRelationship]:
        """
        No Documentation Found.

        Parameters
        ----------
        relationship_id : str
            The RelationshipID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSystemModelsUpdateGroupClientRelationship]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroupClientRelationships/{encode_path_param(relationship_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsUpdateGroupClientRelationship,
                    parse_obj_as(
                        type_=UpdateSystemModelsUpdateGroupClientRelationship,
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

    async def putsubscription(
        self,
        relationship_id_: str,
        *,
        client_id: str,
        update_group_id: str,
        active: typing.Optional[bool] = OMIT,
        last_checkin: typing.Optional[dt.datetime] = OMIT,
        relationship_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        relationship_id_ : str
            The relationship id of the UpdateGroupClientRelationship

        client_id : str
            Read Only after creation. The client id of the subscriber.

        update_group_id : str
            Read Only after creation. The update group to subscribe to.

        active : typing.Optional[bool]
            The subscription status.  The status is active by default.

        last_checkin : typing.Optional[dt.datetime]
            ReadOnly. The timestamp of the last checkin.

        relationship_id : typing.Optional[str]
            Read Only after creation. The relationship id.  A relationship id will be assigned if not provided on creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroupClientRelationships/{encode_path_param(relationship_id_)}",
            method="PUT",
            json={
                "Active": active,
                "ClientID": client_id,
                "LastCheckin": last_checkin,
                "RelationshipID": relationship_id,
                "UpdateGroupID": update_group_id,
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
