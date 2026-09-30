

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.attachment_response import AttachmentResponse
from .raw_client import AsyncRawAttachmentsClient, RawAttachmentsClient


OMIT = typing.cast(typing.Any, ...)


class AttachmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAttachmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAttachmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAttachmentsClient
        """
        return self._raw_client

    def create_attachment(
        self, *, attachment: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> AttachmentResponse:
        """
        Parameters
        ----------
        attachment : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachmentResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.attachments.create_attachment()
        """
        _response = self._raw_client.create_attachment(attachment=attachment, request_options=request_options)
        return _response.data

    def get_attachment(
        self, attachment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AttachmentResponse:
        """
        Parameters
        ----------
        attachment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachmentResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.attachments.get_attachment(
            attachment_id="attachment_id",
        )
        """
        _response = self._raw_client.get_attachment(attachment_id, request_options=request_options)
        return _response.data


class AsyncAttachmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAttachmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAttachmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAttachmentsClient
        """
        return self._raw_client

    async def create_attachment(
        self, *, attachment: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> AttachmentResponse:
        """
        Parameters
        ----------
        attachment : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachmentResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.attachments.create_attachment()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_attachment(attachment=attachment, request_options=request_options)
        return _response.data

    async def get_attachment(
        self, attachment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AttachmentResponse:
        """
        Parameters
        ----------
        attachment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachmentResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.attachments.get_attachment(
                attachment_id="attachment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_attachment(attachment_id, request_options=request_options)
        return _response.data
