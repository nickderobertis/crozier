

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.avatar_create import AvatarCreate
from ..types.avatar_read import AvatarRead
from ..types.image import Image


OMIT = typing.cast(typing.Any, ...)


class RawAvatarClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_avatar(
        self,
        *,
        anchor_uuid: typing.Optional[str] = OMIT,
        image: typing.Optional[typing.Sequence[Image]] = OMIT,
        style: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AvatarCreate]:
        """
        Avatars are public images used to represent you or your company. Avatars are used to represent users, monetary accounts and cash registers. Avatars cannot be deleted, only replaced. Avatars can be updated after uploading the image you would like to use through AttachmentPublic. Using the attachment_public_uuid which is returned you can update your Avatar. Avatars used for cash registers and company accounts will be reviewed by bunq.

        Parameters
        ----------
        anchor_uuid : typing.Optional[str]
            The public UUID of object this avatar is anchored to.

        image : typing.Optional[typing.Sequence[Image]]
            The actual image information of this avatar.

        style : typing.Optional[str]
            The style (if applicable) for this Avatar.

        uuid_ : typing.Optional[str]
            The public UUID of the avatar.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AvatarCreate]
            Avatars are public images used to represent you or your company. Avatars are used to represent users, monetary accounts and cash registers. Avatars cannot be deleted, only replaced. Avatars can be updated after uploading the image you would like to use through AttachmentPublic. Using the attachment_public_uuid which is returned you can update your Avatar. Avatars used for cash registers and company accounts will be reviewed by bunq.
        """
        _response = self._client_wrapper.httpx_client.request(
            "avatar",
            method="POST",
            json={
                "anchor_uuid": anchor_uuid,
                "image": convert_and_respect_annotation_metadata(
                    object_=image, annotation=typing.Sequence[Image], direction="write"
                ),
                "style": style,
                "uuid": uuid_,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AvatarCreate,
                    parse_obj_as(
                        type_=AvatarCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_avatar(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AvatarRead]:
        """
        Avatars are public images used to represent you or your company. Avatars are used to represent users, monetary accounts and cash registers. Avatars cannot be deleted, only replaced. Avatars can be updated after uploading the image you would like to use through AttachmentPublic. Using the attachment_public_uuid which is returned you can update your Avatar. Avatars used for cash registers and company accounts will be reviewed by bunq.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AvatarRead]
            Avatars are public images used to represent you or your company. Avatars are used to represent users, monetary accounts and cash registers. Avatars cannot be deleted, only replaced. Avatars can be updated after uploading the image you would like to use through AttachmentPublic. Using the attachment_public_uuid which is returned you can update your Avatar. Avatars used for cash registers and company accounts will be reviewed by bunq.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"avatar/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AvatarRead,
                    parse_obj_as(
                        type_=AvatarRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAvatarClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_avatar(
        self,
        *,
        anchor_uuid: typing.Optional[str] = OMIT,
        image: typing.Optional[typing.Sequence[Image]] = OMIT,
        style: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AvatarCreate]:
        """
        Avatars are public images used to represent you or your company. Avatars are used to represent users, monetary accounts and cash registers. Avatars cannot be deleted, only replaced. Avatars can be updated after uploading the image you would like to use through AttachmentPublic. Using the attachment_public_uuid which is returned you can update your Avatar. Avatars used for cash registers and company accounts will be reviewed by bunq.

        Parameters
        ----------
        anchor_uuid : typing.Optional[str]
            The public UUID of object this avatar is anchored to.

        image : typing.Optional[typing.Sequence[Image]]
            The actual image information of this avatar.

        style : typing.Optional[str]
            The style (if applicable) for this Avatar.

        uuid_ : typing.Optional[str]
            The public UUID of the avatar.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AvatarCreate]
            Avatars are public images used to represent you or your company. Avatars are used to represent users, monetary accounts and cash registers. Avatars cannot be deleted, only replaced. Avatars can be updated after uploading the image you would like to use through AttachmentPublic. Using the attachment_public_uuid which is returned you can update your Avatar. Avatars used for cash registers and company accounts will be reviewed by bunq.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "avatar",
            method="POST",
            json={
                "anchor_uuid": anchor_uuid,
                "image": convert_and_respect_annotation_metadata(
                    object_=image, annotation=typing.Sequence[Image], direction="write"
                ),
                "style": style,
                "uuid": uuid_,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AvatarCreate,
                    parse_obj_as(
                        type_=AvatarCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_avatar(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AvatarRead]:
        """
        Avatars are public images used to represent you or your company. Avatars are used to represent users, monetary accounts and cash registers. Avatars cannot be deleted, only replaced. Avatars can be updated after uploading the image you would like to use through AttachmentPublic. Using the attachment_public_uuid which is returned you can update your Avatar. Avatars used for cash registers and company accounts will be reviewed by bunq.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AvatarRead]
            Avatars are public images used to represent you or your company. Avatars are used to represent users, monetary accounts and cash registers. Avatars cannot be deleted, only replaced. Avatars can be updated after uploading the image you would like to use through AttachmentPublic. Using the attachment_public_uuid which is returned you can update your Avatar. Avatars used for cash registers and company accounts will be reviewed by bunq.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"avatar/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AvatarRead,
                    parse_obj_as(
                        type_=AvatarRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
