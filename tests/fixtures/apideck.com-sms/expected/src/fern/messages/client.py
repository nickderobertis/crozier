

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_message_response import CreateMessageResponse
from ..types.delete_message_response import DeleteMessageResponse
from ..types.get_message_response import GetMessageResponse
from ..types.get_messages_response import GetMessagesResponse
from ..types.message_direction import MessageDirection
from ..types.message_error import MessageError
from ..types.message_price import MessagePrice
from ..types.message_status import MessageStatus
from ..types.message_type import MessageType
from ..types.update_message_response import UpdateMessageResponse
from .raw_client import AsyncRawMessagesClient, RawMessagesClient


OMIT = typing.cast(typing.Any, ...)


class MessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMessagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMessagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMessagesClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetMessagesResponse:
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
        GetMessagesResponse
            Messages

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.messages.all_(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.all_(
            raw=raw, cursor=cursor, limit=limit, fields=fields, request_options=request_options
        )
        return _response.data

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
    ) -> CreateMessageResponse:
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
        CreateMessageResponse
            Messages

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.messages.add(
            body="Hi! How are you doing?",
            from_="+15017122661",
            to="+15017122662",
        )
        """
        _response = self._raw_client.add(
            body=body,
            from_=from_,
            to=to,
            raw=raw,
            created_at=created_at,
            created_by=created_by,
            direction=direction,
            error=error,
            id=id,
            messaging_service_id=messaging_service_id,
            number_of_media_files=number_of_media_files,
            number_of_units=number_of_units,
            price=price,
            reference=reference,
            scheduled_at=scheduled_at,
            sent_at=sent_at,
            status=status,
            subject=subject,
            type=type,
            updated_at=updated_at,
            updated_by=updated_by,
            webhook_url=webhook_url,
            request_options=request_options,
        )
        return _response.data

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetMessageResponse:
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
        GetMessageResponse
            Messages

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.messages.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteMessageResponse:
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
        DeleteMessageResponse
            Messages

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.messages.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

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
    ) -> UpdateMessageResponse:
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
        UpdateMessageResponse
            Messages

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.messages.update(
            id_="id",
            body="Hi! How are you doing?",
            from_="+15017122661",
            to="+15017122662",
        )
        """
        _response = self._raw_client.update(
            id_,
            body=body,
            from_=from_,
            to=to,
            raw=raw,
            created_at=created_at,
            created_by=created_by,
            direction=direction,
            error=error,
            id=id,
            messaging_service_id=messaging_service_id,
            number_of_media_files=number_of_media_files,
            number_of_units=number_of_units,
            price=price,
            reference=reference,
            scheduled_at=scheduled_at,
            sent_at=sent_at,
            status=status,
            subject=subject,
            type=type,
            updated_at=updated_at,
            updated_by=updated_by,
            webhook_url=webhook_url,
            request_options=request_options,
        )
        return _response.data


class AsyncMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMessagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMessagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMessagesClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetMessagesResponse:
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
        GetMessagesResponse
            Messages

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.messages.all_(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            raw=raw, cursor=cursor, limit=limit, fields=fields, request_options=request_options
        )
        return _response.data

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
    ) -> CreateMessageResponse:
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
        CreateMessageResponse
            Messages

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.messages.add(
                body="Hi! How are you doing?",
                from_="+15017122661",
                to="+15017122662",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            body=body,
            from_=from_,
            to=to,
            raw=raw,
            created_at=created_at,
            created_by=created_by,
            direction=direction,
            error=error,
            id=id,
            messaging_service_id=messaging_service_id,
            number_of_media_files=number_of_media_files,
            number_of_units=number_of_units,
            price=price,
            reference=reference,
            scheduled_at=scheduled_at,
            sent_at=sent_at,
            status=status,
            subject=subject,
            type=type,
            updated_at=updated_at,
            updated_by=updated_by,
            webhook_url=webhook_url,
            request_options=request_options,
        )
        return _response.data

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetMessageResponse:
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
        GetMessageResponse
            Messages

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.messages.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteMessageResponse:
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
        DeleteMessageResponse
            Messages

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.messages.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

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
    ) -> UpdateMessageResponse:
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
        UpdateMessageResponse
            Messages

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.messages.update(
                id_="id",
                body="Hi! How are you doing?",
                from_="+15017122661",
                to="+15017122662",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            body=body,
            from_=from_,
            to=to,
            raw=raw,
            created_at=created_at,
            created_by=created_by,
            direction=direction,
            error=error,
            id=id,
            messaging_service_id=messaging_service_id,
            number_of_media_files=number_of_media_files,
            number_of_units=number_of_units,
            price=price,
            reference=reference,
            scheduled_at=scheduled_at,
            sent_at=sent_at,
            status=status,
            subject=subject,
            type=type,
            updated_at=updated_at,
            updated_by=updated_by,
            webhook_url=webhook_url,
            request_options=request_options,
        )
        return _response.data
