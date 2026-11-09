

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.edge_message_dto import EdgeMessageDto
from ..types.entity_transaction_response import EntityTransactionResponse
from .raw_client import AsyncRawEdgeMessageClient, RawEdgeMessageClient


OMIT = typing.cast(typing.Any, ...)


class EdgeMessageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEdgeMessageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEdgeMessageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEdgeMessageClient
        """
        return self._raw_client

    def delete_messages(
        self,
        *,
        request: str,
        transaction_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Deletes multiple stored edge messages using their unique identifiers, including the associated payload blobs. Messages are deleted in batches according to the specified transaction size.

        Parameters
        ----------
        request : str

        transaction_size : typing.Optional[int]
            Number of messages to delete per transaction batch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Messages successfully deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.edge_message.delete_messages(
            request="string",
        )
        """
        _response = self._raw_client.delete_messages(
            request=request, transaction_size=transaction_size, request_options=request_options
        )
        return _response.data

    def new_message(
        self,
        subject: str,
        *,
        request: str,
        transaction_timeout_millis: typing.Optional[int] = None,
        message_id: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        recipient: typing.Optional[str] = None,
        reply_to: typing.Optional[str] = None,
        correlation_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Creates and stores a new edge message with the provided payload and AMQP-aligned headers. The message is processed according to the specified parsing configuration and stored with a unique identifier.

        Parameters
        ----------
        subject : str
            Message subject identifier

        request : str

        transaction_timeout_millis : typing.Optional[int]
            Maximum time in milliseconds to wait for transaction completion

        message_id : typing.Optional[str]
            Custom message identifier

        user_id : typing.Optional[str]
            ID of the message sender

        recipient : typing.Optional[str]
            Intended message recipient

        reply_to : typing.Optional[str]
            Reply-to address for responses

        correlation_id : typing.Optional[str]
            Correlation ID for message tracking

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Message successfully created and stored

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.edge_message.new_message(
            subject="subject",
            request="string",
        )
        """
        _response = self._raw_client.new_message(
            subject,
            request=request,
            transaction_timeout_millis=transaction_timeout_millis,
            message_id=message_id,
            user_id=user_id,
            recipient=recipient,
            reply_to=reply_to,
            correlation_id=correlation_id,
            request_options=request_options,
        )
        return _response.data

    def get_message(
        self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EdgeMessageDto:
        """
        Fetches a stored edge message using its unique identifier, including all message metadata and payload

        Parameters
        ----------
        message_id : str
            Unique identifier of the message to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EdgeMessageDto
            Message successfully retrieved

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.edge_message.get_message(
            message_id="825ba31c-0b5b-11f0-91f5-667325248341",
        )
        """
        _response = self._raw_client.get_message(message_id, request_options=request_options)
        return _response.data

    def delete_message(
        self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntityTransactionResponse:
        """
        Deletes a stored edge message using its unique identifier, including the associated payload blob

        Parameters
        ----------
        message_id : str
            Unique identifier of the message to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityTransactionResponse
            Message successfully deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.edge_message.delete_message(
            message_id="825ba31c-0b5b-11f0-91f5-667325248341",
        )
        """
        _response = self._raw_client.delete_message(message_id, request_options=request_options)
        return _response.data


class AsyncEdgeMessageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEdgeMessageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEdgeMessageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEdgeMessageClient
        """
        return self._raw_client

    async def delete_messages(
        self,
        *,
        request: str,
        transaction_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Deletes multiple stored edge messages using their unique identifiers, including the associated payload blobs. Messages are deleted in batches according to the specified transaction size.

        Parameters
        ----------
        request : str

        transaction_size : typing.Optional[int]
            Number of messages to delete per transaction batch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Messages successfully deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.edge_message.delete_messages(
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_messages(
            request=request, transaction_size=transaction_size, request_options=request_options
        )
        return _response.data

    async def new_message(
        self,
        subject: str,
        *,
        request: str,
        transaction_timeout_millis: typing.Optional[int] = None,
        message_id: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        recipient: typing.Optional[str] = None,
        reply_to: typing.Optional[str] = None,
        correlation_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Creates and stores a new edge message with the provided payload and AMQP-aligned headers. The message is processed according to the specified parsing configuration and stored with a unique identifier.

        Parameters
        ----------
        subject : str
            Message subject identifier

        request : str

        transaction_timeout_millis : typing.Optional[int]
            Maximum time in milliseconds to wait for transaction completion

        message_id : typing.Optional[str]
            Custom message identifier

        user_id : typing.Optional[str]
            ID of the message sender

        recipient : typing.Optional[str]
            Intended message recipient

        reply_to : typing.Optional[str]
            Reply-to address for responses

        correlation_id : typing.Optional[str]
            Correlation ID for message tracking

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Message successfully created and stored

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.edge_message.new_message(
                subject="subject",
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.new_message(
            subject,
            request=request,
            transaction_timeout_millis=transaction_timeout_millis,
            message_id=message_id,
            user_id=user_id,
            recipient=recipient,
            reply_to=reply_to,
            correlation_id=correlation_id,
            request_options=request_options,
        )
        return _response.data

    async def get_message(
        self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EdgeMessageDto:
        """
        Fetches a stored edge message using its unique identifier, including all message metadata and payload

        Parameters
        ----------
        message_id : str
            Unique identifier of the message to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EdgeMessageDto
            Message successfully retrieved

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.edge_message.get_message(
                message_id="825ba31c-0b5b-11f0-91f5-667325248341",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_message(message_id, request_options=request_options)
        return _response.data

    async def delete_message(
        self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntityTransactionResponse:
        """
        Deletes a stored edge message using its unique identifier, including the associated payload blob

        Parameters
        ----------
        message_id : str
            Unique identifier of the message to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityTransactionResponse
            Message successfully deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.edge_message.delete_message(
                message_id="825ba31c-0b5b-11f0-91f5-667325248341",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_message(message_id, request_options=request_options)
        return _response.data
