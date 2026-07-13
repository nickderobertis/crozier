

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.avatar_create import AvatarCreate
from ..types.avatar_read import AvatarRead
from ..types.image import Image
from .raw_client import AsyncRawAvatarClient, RawAvatarClient


OMIT = typing.cast(typing.Any, ...)


class AvatarClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAvatarClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAvatarClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAvatarClient
        """
        return self._raw_client

    def create_avatar(
        self,
        *,
        anchor_uuid: typing.Optional[str] = OMIT,
        image: typing.Optional[typing.Sequence[Image]] = OMIT,
        style: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AvatarCreate:
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
        AvatarCreate
            Avatars are public images used to represent you or your company. Avatars are used to represent users, monetary accounts and cash registers. Avatars cannot be deleted, only replaced. Avatars can be updated after uploading the image you would like to use through AttachmentPublic. Using the attachment_public_uuid which is returned you can update your Avatar. Avatars used for cash registers and company accounts will be reviewed by bunq.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.avatar.create_avatar()
        """
        _response = self._raw_client.create_avatar(
            anchor_uuid=anchor_uuid, image=image, style=style, uuid_=uuid_, request_options=request_options
        )
        return _response.data

    def read_avatar(self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> AvatarRead:
        """
        Avatars are public images used to represent you or your company. Avatars are used to represent users, monetary accounts and cash registers. Avatars cannot be deleted, only replaced. Avatars can be updated after uploading the image you would like to use through AttachmentPublic. Using the attachment_public_uuid which is returned you can update your Avatar. Avatars used for cash registers and company accounts will be reviewed by bunq.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AvatarRead
            Avatars are public images used to represent you or your company. Avatars are used to represent users, monetary accounts and cash registers. Avatars cannot be deleted, only replaced. Avatars can be updated after uploading the image you would like to use through AttachmentPublic. Using the attachment_public_uuid which is returned you can update your Avatar. Avatars used for cash registers and company accounts will be reviewed by bunq.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.avatar.read_avatar(
            item_id=1,
        )
        """
        _response = self._raw_client.read_avatar(item_id, request_options=request_options)
        return _response.data


class AsyncAvatarClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAvatarClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAvatarClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAvatarClient
        """
        return self._raw_client

    async def create_avatar(
        self,
        *,
        anchor_uuid: typing.Optional[str] = OMIT,
        image: typing.Optional[typing.Sequence[Image]] = OMIT,
        style: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AvatarCreate:
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
        AvatarCreate
            Avatars are public images used to represent you or your company. Avatars are used to represent users, monetary accounts and cash registers. Avatars cannot be deleted, only replaced. Avatars can be updated after uploading the image you would like to use through AttachmentPublic. Using the attachment_public_uuid which is returned you can update your Avatar. Avatars used for cash registers and company accounts will be reviewed by bunq.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.avatar.create_avatar()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_avatar(
            anchor_uuid=anchor_uuid, image=image, style=style, uuid_=uuid_, request_options=request_options
        )
        return _response.data

    async def read_avatar(self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> AvatarRead:
        """
        Avatars are public images used to represent you or your company. Avatars are used to represent users, monetary accounts and cash registers. Avatars cannot be deleted, only replaced. Avatars can be updated after uploading the image you would like to use through AttachmentPublic. Using the attachment_public_uuid which is returned you can update your Avatar. Avatars used for cash registers and company accounts will be reviewed by bunq.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AvatarRead
            Avatars are public images used to represent you or your company. Avatars are used to represent users, monetary accounts and cash registers. Avatars cannot be deleted, only replaced. Avatars can be updated after uploading the image you would like to use through AttachmentPublic. Using the attachment_public_uuid which is returned you can update your Avatar. Avatars used for cash registers and company accounts will be reviewed by bunq.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.avatar.read_avatar(
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_avatar(item_id, request_options=request_options)
        return _response.data
