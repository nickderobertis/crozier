

import datetime as dt
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
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.bad_request_response import BadRequestResponse
from ..types.create_message_response import CreateMessageResponse
from ..types.delete_message_response import DeleteMessageResponse
from ..types.get_message_response import GetMessageResponse
from ..types.get_messages_response import GetMessagesResponse
from ..types.message_direction import MessageDirection
from ..types.message_error import MessageError
from ..types.message_price import MessagePrice
from ..types.message_status import MessageStatus
from ..types.message_type import MessageType
from ..types.not_found_response import NotFoundResponse
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unprocessable_response import UnprocessableResponse
from ..types.update_message_response import UpdateMessageResponse


OMIT = typing.cast(typing.Any, ...)


class RawMessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetMessagesResponse]:
        """
        List Messages

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMessagesResponse]
            Messages
        """
        _response = self._client_wrapper.httpx_client.request(
            "sms/messages",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMessagesResponse,
                    parse_obj_as(
                        type_=GetMessagesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add(
        self,
        *,
        body: str,
        from_: str,
        to: str,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        direction: typing.Optional[MessageDirection] = OMIT,
        error: typing.Optional[MessageError] = OMIT,
        id: typing.Optional[str] = OMIT,
        messaging_service_id: typing.Optional[str] = OMIT,
        number_of_media_files: typing.Optional[int] = OMIT,
        number_of_units: typing.Optional[int] = OMIT,
        price: typing.Optional[MessagePrice] = OMIT,
        reference: typing.Optional[str] = OMIT,
        scheduled_at: typing.Optional[dt.datetime] = OMIT,
        sent_at: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[MessageStatus] = OMIT,
        subject: typing.Optional[str] = OMIT,
        type: typing.Optional[MessageType] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        webhook_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateMessageResponse]:
        """
        Create Message

        Parameters
        ----------
        body : str
            The message text.

        from_ : str
            The phone number that initiated the message.

        to : str
            The phone number that received the message.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[dt.datetime]
            The date and time when the object was created.

        created_by : typing.Optional[str]
            The user who created the object.

        direction : typing.Optional[MessageDirection]
            The direction of the message.

        error : typing.Optional[MessageError]
            The error returned if your message status is failed or undelivered.

        id : typing.Optional[str]
            A unique identifier for an object.

        messaging_service_id : typing.Optional[str]
            The ID of the Messaging Service used with the message. In case of Plivo this links to the Powerpack ID.

        number_of_media_files : typing.Optional[int]
            The number of media files associated with the message.

        number_of_units : typing.Optional[int]
            The number of units that make up the complete message. Messages can be split up due to the constraints of the message size.

        price : typing.Optional[MessagePrice]
            Price of the message.

        reference : typing.Optional[str]
            A client reference.

        scheduled_at : typing.Optional[dt.datetime]
            The scheduled date and time of the message.

        sent_at : typing.Optional[dt.datetime]
            The date and time that the message was sent

        status : typing.Optional[MessageStatus]
            Status of the delivery of the message.

        subject : typing.Optional[str]

        type : typing.Optional[MessageType]
            Set to sms for SMS messages and mms for MMS messages.

        updated_at : typing.Optional[dt.datetime]
            The date and time when the object was last updated.

        updated_by : typing.Optional[str]
            The user who last updated the object.

        webhook_url : typing.Optional[str]
            Define a webhook to receive delivery notifications.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateMessageResponse]
            Messages
        """
        _response = self._client_wrapper.httpx_client.request(
            "sms/messages",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "body": body,
                "created_at": created_at,
                "created_by": created_by,
                "direction": direction,
                "error": convert_and_respect_annotation_metadata(
                    object_=error, annotation=MessageError, direction="write"
                ),
                "from": from_,
                "id": id,
                "messaging_service_id": messaging_service_id,
                "number_of_media_files": number_of_media_files,
                "number_of_units": number_of_units,
                "price": convert_and_respect_annotation_metadata(
                    object_=price, annotation=MessagePrice, direction="write"
                ),
                "reference": reference,
                "scheduled_at": scheduled_at,
                "sent_at": sent_at,
                "status": status,
                "subject": subject,
                "to": to,
                "type": type,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "webhook_url": webhook_url,
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
                    CreateMessageResponse,
                    parse_obj_as(
                        type_=CreateMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetMessageResponse]:
        """
        Get Message

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMessageResponse]
            Messages
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sms/messages/{jsonable_encoder(id)}",
            method="GET",
            params={
                "raw": raw,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMessageResponse,
                    parse_obj_as(
                        type_=GetMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteMessageResponse]:
        """
        Delete Message

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteMessageResponse]
            Messages
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sms/messages/{jsonable_encoder(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteMessageResponse,
                    parse_obj_as(
                        type_=DeleteMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update(
        self,
        id_: str,
        *,
        body: str,
        from_: str,
        to: str,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        direction: typing.Optional[MessageDirection] = OMIT,
        error: typing.Optional[MessageError] = OMIT,
        id: typing.Optional[str] = OMIT,
        messaging_service_id: typing.Optional[str] = OMIT,
        number_of_media_files: typing.Optional[int] = OMIT,
        number_of_units: typing.Optional[int] = OMIT,
        price: typing.Optional[MessagePrice] = OMIT,
        reference: typing.Optional[str] = OMIT,
        scheduled_at: typing.Optional[dt.datetime] = OMIT,
        sent_at: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[MessageStatus] = OMIT,
        subject: typing.Optional[str] = OMIT,
        type: typing.Optional[MessageType] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        webhook_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateMessageResponse]:
        """
        Update Message

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        body : str
            The message text.

        from_ : str
            The phone number that initiated the message.

        to : str
            The phone number that received the message.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[dt.datetime]
            The date and time when the object was created.

        created_by : typing.Optional[str]
            The user who created the object.

        direction : typing.Optional[MessageDirection]
            The direction of the message.

        error : typing.Optional[MessageError]
            The error returned if your message status is failed or undelivered.

        id : typing.Optional[str]
            A unique identifier for an object.

        messaging_service_id : typing.Optional[str]
            The ID of the Messaging Service used with the message. In case of Plivo this links to the Powerpack ID.

        number_of_media_files : typing.Optional[int]
            The number of media files associated with the message.

        number_of_units : typing.Optional[int]
            The number of units that make up the complete message. Messages can be split up due to the constraints of the message size.

        price : typing.Optional[MessagePrice]
            Price of the message.

        reference : typing.Optional[str]
            A client reference.

        scheduled_at : typing.Optional[dt.datetime]
            The scheduled date and time of the message.

        sent_at : typing.Optional[dt.datetime]
            The date and time that the message was sent

        status : typing.Optional[MessageStatus]
            Status of the delivery of the message.

        subject : typing.Optional[str]

        type : typing.Optional[MessageType]
            Set to sms for SMS messages and mms for MMS messages.

        updated_at : typing.Optional[dt.datetime]
            The date and time when the object was last updated.

        updated_by : typing.Optional[str]
            The user who last updated the object.

        webhook_url : typing.Optional[str]
            Define a webhook to receive delivery notifications.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateMessageResponse]
            Messages
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sms/messages/{jsonable_encoder(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "body": body,
                "created_at": created_at,
                "created_by": created_by,
                "direction": direction,
                "error": convert_and_respect_annotation_metadata(
                    object_=error, annotation=MessageError, direction="write"
                ),
                "from": from_,
                "id": id,
                "messaging_service_id": messaging_service_id,
                "number_of_media_files": number_of_media_files,
                "number_of_units": number_of_units,
                "price": convert_and_respect_annotation_metadata(
                    object_=price, annotation=MessagePrice, direction="write"
                ),
                "reference": reference,
                "scheduled_at": scheduled_at,
                "sent_at": sent_at,
                "status": status,
                "subject": subject,
                "to": to,
                "type": type,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "webhook_url": webhook_url,
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
                    UpdateMessageResponse,
                    parse_obj_as(
                        type_=UpdateMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetMessagesResponse]:
        """
        List Messages

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMessagesResponse]
            Messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sms/messages",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMessagesResponse,
                    parse_obj_as(
                        type_=GetMessagesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add(
        self,
        *,
        body: str,
        from_: str,
        to: str,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        direction: typing.Optional[MessageDirection] = OMIT,
        error: typing.Optional[MessageError] = OMIT,
        id: typing.Optional[str] = OMIT,
        messaging_service_id: typing.Optional[str] = OMIT,
        number_of_media_files: typing.Optional[int] = OMIT,
        number_of_units: typing.Optional[int] = OMIT,
        price: typing.Optional[MessagePrice] = OMIT,
        reference: typing.Optional[str] = OMIT,
        scheduled_at: typing.Optional[dt.datetime] = OMIT,
        sent_at: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[MessageStatus] = OMIT,
        subject: typing.Optional[str] = OMIT,
        type: typing.Optional[MessageType] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        webhook_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateMessageResponse]:
        """
        Create Message

        Parameters
        ----------
        body : str
            The message text.

        from_ : str
            The phone number that initiated the message.

        to : str
            The phone number that received the message.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[dt.datetime]
            The date and time when the object was created.

        created_by : typing.Optional[str]
            The user who created the object.

        direction : typing.Optional[MessageDirection]
            The direction of the message.

        error : typing.Optional[MessageError]
            The error returned if your message status is failed or undelivered.

        id : typing.Optional[str]
            A unique identifier for an object.

        messaging_service_id : typing.Optional[str]
            The ID of the Messaging Service used with the message. In case of Plivo this links to the Powerpack ID.

        number_of_media_files : typing.Optional[int]
            The number of media files associated with the message.

        number_of_units : typing.Optional[int]
            The number of units that make up the complete message. Messages can be split up due to the constraints of the message size.

        price : typing.Optional[MessagePrice]
            Price of the message.

        reference : typing.Optional[str]
            A client reference.

        scheduled_at : typing.Optional[dt.datetime]
            The scheduled date and time of the message.

        sent_at : typing.Optional[dt.datetime]
            The date and time that the message was sent

        status : typing.Optional[MessageStatus]
            Status of the delivery of the message.

        subject : typing.Optional[str]

        type : typing.Optional[MessageType]
            Set to sms for SMS messages and mms for MMS messages.

        updated_at : typing.Optional[dt.datetime]
            The date and time when the object was last updated.

        updated_by : typing.Optional[str]
            The user who last updated the object.

        webhook_url : typing.Optional[str]
            Define a webhook to receive delivery notifications.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateMessageResponse]
            Messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sms/messages",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "body": body,
                "created_at": created_at,
                "created_by": created_by,
                "direction": direction,
                "error": convert_and_respect_annotation_metadata(
                    object_=error, annotation=MessageError, direction="write"
                ),
                "from": from_,
                "id": id,
                "messaging_service_id": messaging_service_id,
                "number_of_media_files": number_of_media_files,
                "number_of_units": number_of_units,
                "price": convert_and_respect_annotation_metadata(
                    object_=price, annotation=MessagePrice, direction="write"
                ),
                "reference": reference,
                "scheduled_at": scheduled_at,
                "sent_at": sent_at,
                "status": status,
                "subject": subject,
                "to": to,
                "type": type,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "webhook_url": webhook_url,
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
                    CreateMessageResponse,
                    parse_obj_as(
                        type_=CreateMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetMessageResponse]:
        """
        Get Message

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMessageResponse]
            Messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sms/messages/{jsonable_encoder(id)}",
            method="GET",
            params={
                "raw": raw,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMessageResponse,
                    parse_obj_as(
                        type_=GetMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteMessageResponse]:
        """
        Delete Message

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteMessageResponse]
            Messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sms/messages/{jsonable_encoder(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteMessageResponse,
                    parse_obj_as(
                        type_=DeleteMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update(
        self,
        id_: str,
        *,
        body: str,
        from_: str,
        to: str,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        direction: typing.Optional[MessageDirection] = OMIT,
        error: typing.Optional[MessageError] = OMIT,
        id: typing.Optional[str] = OMIT,
        messaging_service_id: typing.Optional[str] = OMIT,
        number_of_media_files: typing.Optional[int] = OMIT,
        number_of_units: typing.Optional[int] = OMIT,
        price: typing.Optional[MessagePrice] = OMIT,
        reference: typing.Optional[str] = OMIT,
        scheduled_at: typing.Optional[dt.datetime] = OMIT,
        sent_at: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[MessageStatus] = OMIT,
        subject: typing.Optional[str] = OMIT,
        type: typing.Optional[MessageType] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        webhook_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateMessageResponse]:
        """
        Update Message

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        body : str
            The message text.

        from_ : str
            The phone number that initiated the message.

        to : str
            The phone number that received the message.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[dt.datetime]
            The date and time when the object was created.

        created_by : typing.Optional[str]
            The user who created the object.

        direction : typing.Optional[MessageDirection]
            The direction of the message.

        error : typing.Optional[MessageError]
            The error returned if your message status is failed or undelivered.

        id : typing.Optional[str]
            A unique identifier for an object.

        messaging_service_id : typing.Optional[str]
            The ID of the Messaging Service used with the message. In case of Plivo this links to the Powerpack ID.

        number_of_media_files : typing.Optional[int]
            The number of media files associated with the message.

        number_of_units : typing.Optional[int]
            The number of units that make up the complete message. Messages can be split up due to the constraints of the message size.

        price : typing.Optional[MessagePrice]
            Price of the message.

        reference : typing.Optional[str]
            A client reference.

        scheduled_at : typing.Optional[dt.datetime]
            The scheduled date and time of the message.

        sent_at : typing.Optional[dt.datetime]
            The date and time that the message was sent

        status : typing.Optional[MessageStatus]
            Status of the delivery of the message.

        subject : typing.Optional[str]

        type : typing.Optional[MessageType]
            Set to sms for SMS messages and mms for MMS messages.

        updated_at : typing.Optional[dt.datetime]
            The date and time when the object was last updated.

        updated_by : typing.Optional[str]
            The user who last updated the object.

        webhook_url : typing.Optional[str]
            Define a webhook to receive delivery notifications.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateMessageResponse]
            Messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sms/messages/{jsonable_encoder(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "body": body,
                "created_at": created_at,
                "created_by": created_by,
                "direction": direction,
                "error": convert_and_respect_annotation_metadata(
                    object_=error, annotation=MessageError, direction="write"
                ),
                "from": from_,
                "id": id,
                "messaging_service_id": messaging_service_id,
                "number_of_media_files": number_of_media_files,
                "number_of_units": number_of_units,
                "price": convert_and_respect_annotation_metadata(
                    object_=price, annotation=MessagePrice, direction="write"
                ),
                "reference": reference,
                "scheduled_at": scheduled_at,
                "sent_at": sent_at,
                "status": status,
                "subject": subject,
                "to": to,
                "type": type,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "webhook_url": webhook_url,
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
                    UpdateMessageResponse,
                    parse_obj_as(
                        type_=UpdateMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
