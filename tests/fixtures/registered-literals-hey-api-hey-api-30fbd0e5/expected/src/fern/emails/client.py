

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawEmailsClient, RawEmailsClient
from .types.emails_send_request_attachments_item import EmailsSendRequestAttachmentsItem
from .types.emails_send_request_bcc import EmailsSendRequestBcc
from .types.emails_send_request_cc import EmailsSendRequestCc
from .types.emails_send_request_from import EmailsSendRequestFrom
from .types.emails_send_request_reply_to_list import EmailsSendRequestReplyToList
from .types.emails_send_request_to import EmailsSendRequestTo
from .types.emails_send_response import EmailsSendResponse


OMIT = typing.cast(typing.Any, ...)


class EmailsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEmailsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEmailsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEmailsClient
        """
        return self._raw_client

    def send(
        self,
        *,
        subject: typing.Optional[str] = OMIT,
        from_: typing.Optional[EmailsSendRequestFrom] = OMIT,
        headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        to: typing.Optional[EmailsSendRequestTo] = OMIT,
        cc: typing.Optional[EmailsSendRequestCc] = OMIT,
        bcc: typing.Optional[EmailsSendRequestBcc] = OMIT,
        text: typing.Optional[str] = OMIT,
        html: typing.Optional[str] = OMIT,
        attachments: typing.Optional[typing.Sequence[EmailsSendRequestAttachmentsItem]] = OMIT,
        reply_to_list: typing.Optional[EmailsSendRequestReplyToList] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmailsSendResponse:
        """
        Send emails

        Parameters
        ----------
        subject : typing.Optional[str]
            The subject line of the email

        from_ : typing.Optional[EmailsSendRequestFrom]

        headers : typing.Optional[typing.Dict[str, str]]
            A set of headers to include the email that you send

        to : typing.Optional[EmailsSendRequestTo]
            A single email or list of emails for one of the address fields

        cc : typing.Optional[EmailsSendRequestCc]
            A single email or list of emails for one of the address fields

        bcc : typing.Optional[EmailsSendRequestBcc]
            A single email or list of emails for one of the address fields

        text : typing.Optional[str]
            Text content of the email, for email clients that may not support HTML

        html : typing.Optional[str]
            HTML content of the email. Can be specified alongside text

        attachments : typing.Optional[typing.Sequence[EmailsSendRequestAttachmentsItem]]
            A list of attachments to add to the email

        reply_to_list : typing.Optional[EmailsSendRequestReplyToList]
            A reply-to list of email addresses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmailsSendResponse
            Email accepted to be sent

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.emails.send(
            subject="An important message",
            text="Hello world",
            html="Hello <strong>world</strong>",
        )
        """
        _response = self._raw_client.send(
            subject=subject,
            from_=from_,
            headers=headers,
            to=to,
            cc=cc,
            bcc=bcc,
            text=text,
            html=html,
            attachments=attachments,
            reply_to_list=reply_to_list,
            request_options=request_options,
        )
        return _response.data


class AsyncEmailsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEmailsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEmailsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEmailsClient
        """
        return self._raw_client

    async def send(
        self,
        *,
        subject: typing.Optional[str] = OMIT,
        from_: typing.Optional[EmailsSendRequestFrom] = OMIT,
        headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        to: typing.Optional[EmailsSendRequestTo] = OMIT,
        cc: typing.Optional[EmailsSendRequestCc] = OMIT,
        bcc: typing.Optional[EmailsSendRequestBcc] = OMIT,
        text: typing.Optional[str] = OMIT,
        html: typing.Optional[str] = OMIT,
        attachments: typing.Optional[typing.Sequence[EmailsSendRequestAttachmentsItem]] = OMIT,
        reply_to_list: typing.Optional[EmailsSendRequestReplyToList] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmailsSendResponse:
        """
        Send emails

        Parameters
        ----------
        subject : typing.Optional[str]
            The subject line of the email

        from_ : typing.Optional[EmailsSendRequestFrom]

        headers : typing.Optional[typing.Dict[str, str]]
            A set of headers to include the email that you send

        to : typing.Optional[EmailsSendRequestTo]
            A single email or list of emails for one of the address fields

        cc : typing.Optional[EmailsSendRequestCc]
            A single email or list of emails for one of the address fields

        bcc : typing.Optional[EmailsSendRequestBcc]
            A single email or list of emails for one of the address fields

        text : typing.Optional[str]
            Text content of the email, for email clients that may not support HTML

        html : typing.Optional[str]
            HTML content of the email. Can be specified alongside text

        attachments : typing.Optional[typing.Sequence[EmailsSendRequestAttachmentsItem]]
            A list of attachments to add to the email

        reply_to_list : typing.Optional[EmailsSendRequestReplyToList]
            A reply-to list of email addresses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmailsSendResponse
            Email accepted to be sent

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.emails.send(
                subject="An important message",
                text="Hello world",
                html="Hello <strong>world</strong>",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send(
            subject=subject,
            from_=from_,
            headers=headers,
            to=to,
            cc=cc,
            bcc=bcc,
            text=text,
            html=html,
            attachments=attachments,
            reply_to_list=reply_to_list,
            request_options=request_options,
        )
        return _response.data
