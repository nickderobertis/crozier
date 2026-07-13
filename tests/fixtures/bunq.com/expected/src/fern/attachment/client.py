

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.attachment_monetary_account import AttachmentMonetaryAccount
from ..types.attachment_monetary_account_create import AttachmentMonetaryAccountCreate
from ..types.attachment_user_read import AttachmentUserRead
from .raw_client import AsyncRawAttachmentClient, RawAttachmentClient


OMIT = typing.cast(typing.Any, ...)


class AttachmentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAttachmentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAttachmentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAttachmentClient
        """
        return self._raw_client

    def read_attachment_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AttachmentUserRead:
        """
        Get a specific attachment. The header of the response contains the content-type of the attachment.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachmentUserRead
            This call is used to upload an attachment that is accessible only by a specific user. This can be used for example to upload passport scans or other documents. Attachments supported are png, jpg and gif.

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
        client.attachment.read_attachment_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_attachment_for_user(user_id, item_id, request_options=request_options)
        return _response.data

    def create_attachment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        request: AttachmentMonetaryAccount,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AttachmentMonetaryAccountCreate:
        """
        Create a new monetary account attachment. Create a POST request with a payload that contains the binary representation of the file, without any JSON wrapping. Make sure you define the MIME type (i.e. image/jpeg) in the Content-Type header. You are required to provide a description of the attachment using the X-Bunq-Attachment-Description header.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request : AttachmentMonetaryAccount

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachmentMonetaryAccountCreate
            This call is used to upload an attachment that can be referenced to in payment requests and payments sent from a specific monetary account. Attachments supported are png, jpg and gif.

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
        client.attachment.create_attachment_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            request={"key": "value"},
        )
        """
        _response = self._raw_client.create_attachment_for_user_monetary_account(
            user_id, monetary_account_id, request=request, request_options=request_options
        )
        return _response.data


class AsyncAttachmentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAttachmentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAttachmentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAttachmentClient
        """
        return self._raw_client

    async def read_attachment_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AttachmentUserRead:
        """
        Get a specific attachment. The header of the response contains the content-type of the attachment.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachmentUserRead
            This call is used to upload an attachment that is accessible only by a specific user. This can be used for example to upload passport scans or other documents. Attachments supported are png, jpg and gif.

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
            await client.attachment.read_attachment_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_attachment_for_user(user_id, item_id, request_options=request_options)
        return _response.data

    async def create_attachment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        request: AttachmentMonetaryAccount,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AttachmentMonetaryAccountCreate:
        """
        Create a new monetary account attachment. Create a POST request with a payload that contains the binary representation of the file, without any JSON wrapping. Make sure you define the MIME type (i.e. image/jpeg) in the Content-Type header. You are required to provide a description of the attachment using the X-Bunq-Attachment-Description header.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request : AttachmentMonetaryAccount

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachmentMonetaryAccountCreate
            This call is used to upload an attachment that can be referenced to in payment requests and payments sent from a specific monetary account. Attachments supported are png, jpg and gif.

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
            await client.attachment.create_attachment_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_attachment_for_user_monetary_account(
            user_id, monetary_account_id, request=request, request_options=request_options
        )
        return _response.data
