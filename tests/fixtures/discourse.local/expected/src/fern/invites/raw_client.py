

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.create_invite_response import CreateInviteResponse


OMIT = typing.cast(typing.Any, ...)


class RawInvitesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_invite(
        self,
        *,
        api_key: str,
        api_username: str,
        custom_message: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        expires_at: typing.Optional[str] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        group_names: typing.Optional[str] = OMIT,
        max_redemptions_allowed: typing.Optional[int] = OMIT,
        skip_email: typing.Optional[bool] = OMIT,
        topic_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateInviteResponse]:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        custom_message : typing.Optional[str]
            optional, for email invites

        email : typing.Optional[str]
            required for email invites only

        expires_at : typing.Optional[str]
            optional, if not supplied, the invite_expiry_days site
            setting is used

        group_id : typing.Optional[int]
            optional, either this or `group_names`

        group_names : typing.Optional[str]
            optional, either this or `group_id`

        max_redemptions_allowed : typing.Optional[int]
            optional, for link invites

        skip_email : typing.Optional[bool]

        topic_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateInviteResponse]
            success response
        """
        _response = self._client_wrapper.httpx_client.request(
            "invites.json",
            method="POST",
            json={
                "custom_message": custom_message,
                "email": email,
                "expires_at": expires_at,
                "group_id": group_id,
                "group_names": group_names,
                "max_redemptions_allowed": max_redemptions_allowed,
                "skip_email": skip_email,
                "topic_id": topic_id,
            },
            headers={
                "content-type": "application/json",
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateInviteResponse,
                    parse_obj_as(
                        type_=CreateInviteResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawInvitesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_invite(
        self,
        *,
        api_key: str,
        api_username: str,
        custom_message: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        expires_at: typing.Optional[str] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        group_names: typing.Optional[str] = OMIT,
        max_redemptions_allowed: typing.Optional[int] = OMIT,
        skip_email: typing.Optional[bool] = OMIT,
        topic_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateInviteResponse]:
        """
        Parameters
        ----------
        api_key : str

        api_username : str

        custom_message : typing.Optional[str]
            optional, for email invites

        email : typing.Optional[str]
            required for email invites only

        expires_at : typing.Optional[str]
            optional, if not supplied, the invite_expiry_days site
            setting is used

        group_id : typing.Optional[int]
            optional, either this or `group_names`

        group_names : typing.Optional[str]
            optional, either this or `group_id`

        max_redemptions_allowed : typing.Optional[int]
            optional, for link invites

        skip_email : typing.Optional[bool]

        topic_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateInviteResponse]
            success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "invites.json",
            method="POST",
            json={
                "custom_message": custom_message,
                "email": email,
                "expires_at": expires_at,
                "group_id": group_id,
                "group_names": group_names,
                "max_redemptions_allowed": max_redemptions_allowed,
                "skip_email": skip_email,
                "topic_id": topic_id,
            },
            headers={
                "content-type": "application/json",
                "Api-Key": str(api_key) if api_key is not None else None,
                "Api-Username": str(api_username) if api_username is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateInviteResponse,
                    parse_obj_as(
                        type_=CreateInviteResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
