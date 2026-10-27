

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
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.conversation_member import ConversationMember
from ..types.conversation_member_input_roles_item import ConversationMemberInputRolesItem
from ..types.error import Error
from .types.list_channel_members_response import ListChannelMembersResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawChannelMembersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_channel_members(
        self,
        team_id: str,
        channel_id: str,
        *,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListChannelMembersResponse]:
        """
        Retrieve a list of members in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        filter : typing.Optional[str]
            OData filter query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListChannelMembersResponse]
            Successfully retrieved channel members
        """
        _response = self._client_wrapper.httpx_client.request(
            f"teams/{encode_path_param(team_id)}/channels/{encode_path_param(channel_id)}/members",
            method="GET",
            params={
                "$top": top,
                "$skip": skip,
                "$filter": filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListChannelMembersResponse,
                    parse_obj_as(
                        type_=ListChannelMembersResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def add_channel_member(
        self,
        team_id: str,
        channel_id: str,
        *,
        odata_type: str,
        user_odata_bind: str,
        roles: typing.Optional[typing.Sequence[ConversationMemberInputRolesItem]] = OMIT,
        visible_history_start_date_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConversationMember]:
        """
        Add a member to a private channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        odata_type : str

        user_odata_bind : str

        roles : typing.Optional[typing.Sequence[ConversationMemberInputRolesItem]]

        visible_history_start_date_time : typing.Optional[dt.datetime]
            Timestamp from which the member can see messages

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConversationMember]
            Member added successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"teams/{encode_path_param(team_id)}/channels/{encode_path_param(channel_id)}/members",
            method="POST",
            json={
                "@odata.type": odata_type,
                "user@odata.bind": user_odata_bind,
                "roles": roles,
                "visibleHistoryStartDateTime": visible_history_start_date_time,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConversationMember,
                    parse_obj_as(
                        type_=ConversationMember,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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


class AsyncRawChannelMembersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_channel_members(
        self,
        team_id: str,
        channel_id: str,
        *,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListChannelMembersResponse]:
        """
        Retrieve a list of members in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        filter : typing.Optional[str]
            OData filter query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListChannelMembersResponse]
            Successfully retrieved channel members
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"teams/{encode_path_param(team_id)}/channels/{encode_path_param(channel_id)}/members",
            method="GET",
            params={
                "$top": top,
                "$skip": skip,
                "$filter": filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListChannelMembersResponse,
                    parse_obj_as(
                        type_=ListChannelMembersResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def add_channel_member(
        self,
        team_id: str,
        channel_id: str,
        *,
        odata_type: str,
        user_odata_bind: str,
        roles: typing.Optional[typing.Sequence[ConversationMemberInputRolesItem]] = OMIT,
        visible_history_start_date_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConversationMember]:
        """
        Add a member to a private channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        odata_type : str

        user_odata_bind : str

        roles : typing.Optional[typing.Sequence[ConversationMemberInputRolesItem]]

        visible_history_start_date_time : typing.Optional[dt.datetime]
            Timestamp from which the member can see messages

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConversationMember]
            Member added successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"teams/{encode_path_param(team_id)}/channels/{encode_path_param(channel_id)}/members",
            method="POST",
            json={
                "@odata.type": odata_type,
                "user@odata.bind": user_odata_bind,
                "roles": roles,
                "visibleHistoryStartDateTime": visible_history_start_date_time,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConversationMember,
                    parse_obj_as(
                        type_=ConversationMember,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
