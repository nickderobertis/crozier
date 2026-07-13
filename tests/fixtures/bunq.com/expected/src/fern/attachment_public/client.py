

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.attachment_public import AttachmentPublic
from ..types.attachment_public_create import AttachmentPublicCreate
from ..types.attachment_public_read import AttachmentPublicRead
from .raw_client import AsyncRawAttachmentPublicClient, RawAttachmentPublicClient


OMIT = typing.cast(typing.Any, ...)


class AttachmentPublicClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAttachmentPublicClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAttachmentPublicClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAttachmentPublicClient
        """
        return self._raw_client

    def create_attachment_public(
        self, *, request: AttachmentPublic, request_options: typing.Optional[RequestOptions] = None
    ) -> AttachmentPublicCreate:
        """
        Create a new public attachment. Create a POST request with a payload that contains a binary representation of the file, without any JSON wrapping. Make sure you define the MIME type (i.e. image/jpeg, or image/png) in the Content-Type header. You are required to provide a description of the attachment using the X-Bunq-Attachment-Description header.

        Parameters
        ----------
        request : AttachmentPublic

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachmentPublicCreate
            This call is used to upload an attachment that can be referenced to as an avatar (through the Avatar endpoint) or in a tab sent. Attachments supported are png, jpg and gif.

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
        client.attachment_public.create_attachment_public(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.create_attachment_public(request=request, request_options=request_options)
        return _response.data

    def read_attachment_public(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AttachmentPublicRead:
        """
        Get a specific attachment's metadata through its UUID. The Content-Type header of the response will describe the MIME type of the attachment file.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachmentPublicRead
            This call is used to upload an attachment that can be referenced to as an avatar (through the Avatar endpoint) or in a tab sent. Attachments supported are png, jpg and gif.

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
        client.attachment_public.read_attachment_public(
            item_id=1,
        )
        """
        _response = self._raw_client.read_attachment_public(item_id, request_options=request_options)
        return _response.data


class AsyncAttachmentPublicClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAttachmentPublicClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAttachmentPublicClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAttachmentPublicClient
        """
        return self._raw_client

    async def create_attachment_public(
        self, *, request: AttachmentPublic, request_options: typing.Optional[RequestOptions] = None
    ) -> AttachmentPublicCreate:
        """
        Create a new public attachment. Create a POST request with a payload that contains a binary representation of the file, without any JSON wrapping. Make sure you define the MIME type (i.e. image/jpeg, or image/png) in the Content-Type header. You are required to provide a description of the attachment using the X-Bunq-Attachment-Description header.

        Parameters
        ----------
        request : AttachmentPublic

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachmentPublicCreate
            This call is used to upload an attachment that can be referenced to as an avatar (through the Avatar endpoint) or in a tab sent. Attachments supported are png, jpg and gif.

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
            await client.attachment_public.create_attachment_public(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_attachment_public(request=request, request_options=request_options)
        return _response.data

    async def read_attachment_public(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AttachmentPublicRead:
        """
        Get a specific attachment's metadata through its UUID. The Content-Type header of the response will describe the MIME type of the attachment file.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachmentPublicRead
            This call is used to upload an attachment that can be referenced to as an avatar (through the Avatar endpoint) or in a tab sent. Attachments supported are png, jpg and gif.

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
            await client.attachment_public.read_attachment_public(
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_attachment_public(item_id, request_options=request_options)
        return _response.data
