

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.channel import Channel
from ..types.knocker_id import KnockerId
from ..types.media import Media
from ..types.member_action import MemberAction
from ..types.member_id import MemberId
from ..types.member_id_inviting import MemberIdInviting
from ..types.user_id import UserId
from .types.create_member_response import CreateMemberResponse
from .types.get_member_response import GetMemberResponse
from .types.get_members_response_item import GetMembersResponseItem
from .types.update_member_response import UpdateMemberResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMemberClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_members(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[GetMembersResponseItem]]:
        """
        This endpoint is **DEPRECATED**. Please use [/v0.2/members](/api/conversation.v2#get-members).

        Parameters
        ----------
        conversation_id : str
            Conversation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetMembersResponseItem]]
            Members List Object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/members",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetMembersResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetMembersResponseItem],
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

    def create_member(
        self,
        conversation_id: str,
        *,
        channel: Channel,
        user_id: UserId,
        action: typing.Optional[MemberAction] = OMIT,
        knocking_id: typing.Optional[KnockerId] = OMIT,
        media: typing.Optional[Media] = OMIT,
        member_id: typing.Optional[MemberId] = OMIT,
        member_id_inviting: typing.Optional[MemberIdInviting] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateMemberResponse]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        channel : Channel

        user_id : UserId

        action : typing.Optional[MemberAction]

        knocking_id : typing.Optional[KnockerId]

        media : typing.Optional[Media]

        member_id : typing.Optional[MemberId]

        member_id_inviting : typing.Optional[MemberIdInviting]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateMemberResponse]
            Create or invite Member in invite state
        """
        _response = self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/members",
            method="POST",
            json={
                "action": action,
                "channel": convert_and_respect_annotation_metadata(
                    object_=channel, annotation=Channel, direction="write"
                ),
                "knocking_id": knocking_id,
                "media": convert_and_respect_annotation_metadata(object_=media, annotation=Media, direction="write"),
                "member_id": member_id,
                "member_id_inviting": member_id_inviting,
                "user_id": user_id,
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
                    CreateMemberResponse,
                    parse_obj_as(
                        type_=CreateMemberResponse,
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

    def get_member(
        self, conversation_id: str, member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetMemberResponse]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        member_id : str
            Member ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMemberResponse]
            Retrieve member payload
        """
        _response = self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/members/{encode_path_param(member_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMemberResponse,
                    parse_obj_as(
                        type_=GetMemberResponse,
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

    def update_member(
        self,
        conversation_id: str,
        member_id: str,
        *,
        action: typing.Optional[MemberAction] = OMIT,
        channel: typing.Optional[Channel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateMemberResponse]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        member_id : str
            Member ID

        action : typing.Optional[MemberAction]

        channel : typing.Optional[Channel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateMemberResponse]
            Member retrieved
        """
        _response = self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/members/{encode_path_param(member_id)}",
            method="PUT",
            json={
                "action": action,
                "channel": convert_and_respect_annotation_metadata(
                    object_=channel, annotation=Channel, direction="write"
                ),
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
                    UpdateMemberResponse,
                    parse_obj_as(
                        type_=UpdateMemberResponse,
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

    def delete_member(
        self, conversation_id: str, member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        member_id : str
            Member ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Success response with empty JSON
        """
        _response = self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/members/{encode_path_param(member_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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


class AsyncRawMemberClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_members(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[GetMembersResponseItem]]:
        """
        This endpoint is **DEPRECATED**. Please use [/v0.2/members](/api/conversation.v2#get-members).

        Parameters
        ----------
        conversation_id : str
            Conversation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetMembersResponseItem]]
            Members List Object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/members",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetMembersResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetMembersResponseItem],
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

    async def create_member(
        self,
        conversation_id: str,
        *,
        channel: Channel,
        user_id: UserId,
        action: typing.Optional[MemberAction] = OMIT,
        knocking_id: typing.Optional[KnockerId] = OMIT,
        media: typing.Optional[Media] = OMIT,
        member_id: typing.Optional[MemberId] = OMIT,
        member_id_inviting: typing.Optional[MemberIdInviting] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateMemberResponse]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        channel : Channel

        user_id : UserId

        action : typing.Optional[MemberAction]

        knocking_id : typing.Optional[KnockerId]

        media : typing.Optional[Media]

        member_id : typing.Optional[MemberId]

        member_id_inviting : typing.Optional[MemberIdInviting]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateMemberResponse]
            Create or invite Member in invite state
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/members",
            method="POST",
            json={
                "action": action,
                "channel": convert_and_respect_annotation_metadata(
                    object_=channel, annotation=Channel, direction="write"
                ),
                "knocking_id": knocking_id,
                "media": convert_and_respect_annotation_metadata(object_=media, annotation=Media, direction="write"),
                "member_id": member_id,
                "member_id_inviting": member_id_inviting,
                "user_id": user_id,
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
                    CreateMemberResponse,
                    parse_obj_as(
                        type_=CreateMemberResponse,
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

    async def get_member(
        self, conversation_id: str, member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMemberResponse]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        member_id : str
            Member ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMemberResponse]
            Retrieve member payload
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/members/{encode_path_param(member_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMemberResponse,
                    parse_obj_as(
                        type_=GetMemberResponse,
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

    async def update_member(
        self,
        conversation_id: str,
        member_id: str,
        *,
        action: typing.Optional[MemberAction] = OMIT,
        channel: typing.Optional[Channel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateMemberResponse]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        member_id : str
            Member ID

        action : typing.Optional[MemberAction]

        channel : typing.Optional[Channel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateMemberResponse]
            Member retrieved
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/members/{encode_path_param(member_id)}",
            method="PUT",
            json={
                "action": action,
                "channel": convert_and_respect_annotation_metadata(
                    object_=channel, annotation=Channel, direction="write"
                ),
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
                    UpdateMemberResponse,
                    parse_obj_as(
                        type_=UpdateMemberResponse,
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

    async def delete_member(
        self, conversation_id: str, member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        member_id : str
            Member ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Success response with empty JSON
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/members/{encode_path_param(member_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
