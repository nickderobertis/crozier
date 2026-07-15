

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_response import ApiResponse
from .raw_client import AsyncRawQueuesClient, RawQueuesClient


OMIT = typing.cast(typing.Any, ...)


class QueuesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawQueuesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawQueuesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawQueuesClient
        """
        return self._raw_client

    def get_list_of_queues(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.queues.get_list_of_queues()
        """
        _response = self._raw_client.get_list_of_queues(request_options=request_options)
        return _response.data

    def create_queue(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.queues.create_queue()
        """
        _response = self._raw_client.create_queue(request_options=request_options)
        return _response.data

    def delete_queue(
        self,
        queue_name: str,
        *,
        confirm: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """


        Parameters
        ----------
        queue_name : str

        confirm : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.queues.delete_queue(
            queue_name="queueName",
        )
        """
        _response = self._raw_client.delete_queue(queue_name, confirm=confirm, request_options=request_options)
        return _response.data

    def get_queue_config(
        self, queue_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """


        Parameters
        ----------
        queue_name : str
            Name of Queue

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.queues.get_queue_config(
            queue_name="queueName",
        )
        """
        _response = self._raw_client.get_queue_config(queue_name, request_options=request_options)
        return _response.data

    def update_queue_config(
        self, queue_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """


        Parameters
        ----------
        queue_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.queues.update_queue_config(
            queue_name="queueName",
        )
        """
        _response = self._raw_client.update_queue_config(queue_name, request_options=request_options)
        return _response.data

    def get_message_data(
        self, queue_name: str, queue_message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """


        Parameters
        ----------
        queue_name : str
            Name of Queue

        queue_message_id : str
            ID of Queue Message for which data is to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.queues.get_message_data(
            queue_name="queueName",
            queue_message_id="queueMessageId",
        )
        """
        _response = self._raw_client.get_message_data(queue_name, queue_message_id, request_options=request_options)
        return _response.data

    def get_next_messages(
        self,
        queue_name: str,
        *,
        count: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """


        Parameters
        ----------
        queue_name : str
            Name of Queue

        count : typing.Optional[str]
            Number of messages to get

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.queues.get_next_messages(
            queue_name="queueName",
        )
        """
        _response = self._raw_client.get_next_messages(queue_name, count=count, request_options=request_options)
        return _response.data

    def send_message_binary(
        self,
        queue_name: str,
        *,
        content_type: str,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        regions: typing.Optional[str] = None,
        delay: typing.Optional[str] = None,
        expiration: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """


        Parameters
        ----------
        queue_name : str
            Name of Queue

        content_type : str
            Content type of the data to be sent with Queue Message

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        regions : typing.Optional[str]
            Regions to which message is to be sent

        delay : typing.Optional[str]

        expiration : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation
        """
        _response = self._raw_client.send_message_binary(
            queue_name,
            content_type=content_type,
            request=request,
            regions=regions,
            delay=delay,
            expiration=expiration,
            request_options=request_options,
        )
        return _response.data

    def ack_message(
        self, queue_name: str, queue_message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """


        Parameters
        ----------
        queue_name : str
            Name of Queue

        queue_message_id : str
            ID of Queue Message to be acknowledged

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.queues.ack_message(
            queue_name="queueName",
            queue_message_id="queueMessageId",
        )
        """
        _response = self._raw_client.ack_message(queue_name, queue_message_id, request_options=request_options)
        return _response.data


class AsyncQueuesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawQueuesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawQueuesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawQueuesClient
        """
        return self._raw_client

    async def get_list_of_queues(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.queues.get_list_of_queues()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_list_of_queues(request_options=request_options)
        return _response.data

    async def create_queue(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.queues.create_queue()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_queue(request_options=request_options)
        return _response.data

    async def delete_queue(
        self,
        queue_name: str,
        *,
        confirm: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """


        Parameters
        ----------
        queue_name : str

        confirm : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.queues.delete_queue(
                queue_name="queueName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_queue(queue_name, confirm=confirm, request_options=request_options)
        return _response.data

    async def get_queue_config(
        self, queue_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """


        Parameters
        ----------
        queue_name : str
            Name of Queue

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.queues.get_queue_config(
                queue_name="queueName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_queue_config(queue_name, request_options=request_options)
        return _response.data

    async def update_queue_config(
        self, queue_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """


        Parameters
        ----------
        queue_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.queues.update_queue_config(
                queue_name="queueName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_queue_config(queue_name, request_options=request_options)
        return _response.data

    async def get_message_data(
        self, queue_name: str, queue_message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """


        Parameters
        ----------
        queue_name : str
            Name of Queue

        queue_message_id : str
            ID of Queue Message for which data is to be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.queues.get_message_data(
                queue_name="queueName",
                queue_message_id="queueMessageId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_message_data(
            queue_name, queue_message_id, request_options=request_options
        )
        return _response.data

    async def get_next_messages(
        self,
        queue_name: str,
        *,
        count: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """


        Parameters
        ----------
        queue_name : str
            Name of Queue

        count : typing.Optional[str]
            Number of messages to get

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.queues.get_next_messages(
                queue_name="queueName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_next_messages(queue_name, count=count, request_options=request_options)
        return _response.data

    async def send_message_binary(
        self,
        queue_name: str,
        *,
        content_type: str,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        regions: typing.Optional[str] = None,
        delay: typing.Optional[str] = None,
        expiration: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """


        Parameters
        ----------
        queue_name : str
            Name of Queue

        content_type : str
            Content type of the data to be sent with Queue Message

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        regions : typing.Optional[str]
            Regions to which message is to be sent

        delay : typing.Optional[str]

        expiration : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation
        """
        _response = await self._raw_client.send_message_binary(
            queue_name,
            content_type=content_type,
            request=request,
            regions=regions,
            delay=delay,
            expiration=expiration,
            request_options=request_options,
        )
        return _response.data

    async def ack_message(
        self, queue_name: str, queue_message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """


        Parameters
        ----------
        queue_name : str
            Name of Queue

        queue_message_id : str
            ID of Queue Message to be acknowledged

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.queues.ack_message(
                queue_name="queueName",
                queue_message_id="queueMessageId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ack_message(queue_name, queue_message_id, request_options=request_options)
        return _response.data
