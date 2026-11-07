

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.internal_server_error import InternalServerError
from ..types.internal_server_error_body import InternalServerErrorBody
from .types.emails_send_request_attachments_item import EmailsSendRequestAttachmentsItem
from .types.emails_send_request_bcc import EmailsSendRequestBcc
from .types.emails_send_request_cc import EmailsSendRequestCc
from .types.emails_send_request_from import EmailsSendRequestFrom
from .types.emails_send_request_reply_to_list import EmailsSendRequestReplyToList
from .types.emails_send_request_to import EmailsSendRequestTo
from .types.emails_send_response import EmailsSendResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEmailsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[EmailsSendResponse]:
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
        HttpResponse[EmailsSendResponse]
            Email accepted to be sent
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/email",
            method="POST",
            json={
                "subject": subject,
                "from": convert_and_respect_annotation_metadata(
                    object_=from_, annotation=EmailsSendRequestFrom, direction="write"
                ),
                "headers": headers,
                "to": convert_and_respect_annotation_metadata(
                    object_=to, annotation=EmailsSendRequestTo, direction="write"
                ),
                "cc": convert_and_respect_annotation_metadata(
                    object_=cc, annotation=EmailsSendRequestCc, direction="write"
                ),
                "bcc": convert_and_respect_annotation_metadata(
                    object_=bcc, annotation=EmailsSendRequestBcc, direction="write"
                ),
                "text": text,
                "html": html,
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments, annotation=typing.Sequence[EmailsSendRequestAttachmentsItem], direction="write"
                ),
                "replyToList": convert_and_respect_annotation_metadata(
                    object_=reply_to_list, annotation=EmailsSendRequestReplyToList, direction="write"
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
                    EmailsSendResponse,
                    parse_obj_as(
                        type_=EmailsSendResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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


class AsyncRawEmailsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[EmailsSendResponse]:
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
        AsyncHttpResponse[EmailsSendResponse]
            Email accepted to be sent
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/email",
            method="POST",
            json={
                "subject": subject,
                "from": convert_and_respect_annotation_metadata(
                    object_=from_, annotation=EmailsSendRequestFrom, direction="write"
                ),
                "headers": headers,
                "to": convert_and_respect_annotation_metadata(
                    object_=to, annotation=EmailsSendRequestTo, direction="write"
                ),
                "cc": convert_and_respect_annotation_metadata(
                    object_=cc, annotation=EmailsSendRequestCc, direction="write"
                ),
                "bcc": convert_and_respect_annotation_metadata(
                    object_=bcc, annotation=EmailsSendRequestBcc, direction="write"
                ),
                "text": text,
                "html": html,
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments, annotation=typing.Sequence[EmailsSendRequestAttachmentsItem], direction="write"
                ),
                "replyToList": convert_and_respect_annotation_metadata(
                    object_=reply_to_list, annotation=EmailsSendRequestReplyToList, direction="write"
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
                    EmailsSendResponse,
                    parse_obj_as(
                        type_=EmailsSendResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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
