

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.batch_job import BatchJob
from ..types.letta_batch_messages import LettaBatchMessages
from ..types.letta_batch_request import LettaBatchRequest
from ..types.letta_message_union import LettaMessageUnion
from .raw_client import AsyncRawMessagesClient, RawMessagesClient
from .types.list_all_messages_request_order import ListAllMessagesRequestOrder
from .types.list_batches_request_order import ListBatchesRequestOrder
from .types.list_batches_request_order_by import ListBatchesRequestOrderBy
from .types.list_messages_for_batch_request_order import ListMessagesForBatchRequestOrder
from .types.list_messages_for_batch_request_order_by import ListMessagesForBatchRequestOrderBy
from .types.search_all_messages_request_search_mode import SearchAllMessagesRequestSearchMode
from .types.search_all_messages_response_item import SearchAllMessagesResponseItem


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

    def list_all_messages(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAllMessagesRequestOrder] = None,
        conversation_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[LettaMessageUnion]:
        """
        List messages across all agents for the current user.

        Parameters
        ----------
        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListAllMessagesRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        conversation_id : typing.Optional[str]
            Conversation ID to filter messages by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LettaMessageUnion]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.messages.list_all_messages()
        """
        _response = self._raw_client.list_all_messages(
            before=before,
            after=after,
            limit=limit,
            order=order,
            conversation_id=conversation_id,
            request_options=request_options,
        )
        return _response.data

    def search_all_messages(
        self,
        *,
        query: str,
        search_mode: typing.Optional[SearchAllMessagesRequestSearchMode] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        conversation_id: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SearchAllMessagesResponseItem]:
        """
        Search messages across the organization with optional agent filtering.
        Returns messages with FTS/vector ranks and total RRF score.

        This is a cloud-only feature.

        Parameters
        ----------
        query : str
            Text query for full-text search

        search_mode : typing.Optional[SearchAllMessagesRequestSearchMode]
            Search mode to use

        agent_id : typing.Optional[str]
            Filter messages by agent ID

        conversation_id : typing.Optional[str]
            Filter messages by conversation ID

        limit : typing.Optional[int]
            Maximum number of results to return

        start_date : typing.Optional[dt.datetime]
            Filter messages created after this date

        end_date : typing.Optional[dt.datetime]
            Filter messages created on or before this date

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SearchAllMessagesResponseItem]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.messages.search_all_messages(
            query="query",
        )
        """
        _response = self._raw_client.search_all_messages(
            query=query,
            search_mode=search_mode,
            agent_id=agent_id,
            conversation_id=conversation_id,
            limit=limit,
            start_date=start_date,
            end_date=end_date,
            request_options=request_options,
        )
        return _response.data

    def list_batches(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListBatchesRequestOrder] = None,
        order_by: typing.Optional[ListBatchesRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[BatchJob]:
        """
        List all batch runs.

        Parameters
        ----------
        before : typing.Optional[str]
            Job ID cursor for pagination. Returns jobs that come before this job ID in the specified sort order

        after : typing.Optional[str]
            Job ID cursor for pagination. Returns jobs that come after this job ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of jobs to return

        order : typing.Optional[ListBatchesRequestOrder]
            Sort order for jobs by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListBatchesRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BatchJob]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.messages.list_batches()
        """
        _response = self._raw_client.list_batches(
            before=before, after=after, limit=limit, order=order, order_by=order_by, request_options=request_options
        )
        return _response.data

    def create_batch(
        self,
        *,
        requests: typing.Sequence[LettaBatchRequest],
        callback_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchJob:
        """
        Submit a batch of agent runs for asynchronous processing.

        Creates a job that will fan out messages to all listed agents and process them in parallel.
        The request will be rejected if it exceeds 256MB.

        Parameters
        ----------
        requests : typing.Sequence[LettaBatchRequest]
            List of requests to be processed in batch.

        callback_url : typing.Optional[str]
            Optional URL to call via POST when the batch completes. The callback payload will be a JSON object with the following fields: {'job_id': string, 'status': string, 'completed_at': string}. Where 'job_id' is the unique batch job identifier, 'status' is the final batch status (e.g., 'completed', 'failed'), and 'completed_at' is an ISO 8601 timestamp indicating when the batch job completed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchJob
            Successful Response

        Examples
        --------
        from fern import FernApi, LettaBatchRequest

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.messages.create_batch(
            requests=[
                LettaBatchRequest(
                    agent_id="agent_id",
                )
            ],
        )
        """
        _response = self._raw_client.create_batch(
            requests=requests, callback_url=callback_url, request_options=request_options
        )
        return _response.data

    def retrieve_batch(self, batch_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> BatchJob:
        """
        Retrieve the status and details of a batch run.

        Parameters
        ----------
        batch_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchJob
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.messages.retrieve_batch(
            batch_id="batch_id",
        )
        """
        _response = self._raw_client.retrieve_batch(batch_id, request_options=request_options)
        return _response.data

    def list_messages_for_batch(
        self,
        batch_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListMessagesForBatchRequestOrder] = None,
        order_by: typing.Optional[ListMessagesForBatchRequestOrderBy] = None,
        agent_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LettaBatchMessages:
        """
        Get response messages for a specific batch job.

        Parameters
        ----------
        batch_id : str

        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListMessagesForBatchRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListMessagesForBatchRequestOrderBy]
            Field to sort by

        agent_id : typing.Optional[str]
            Filter messages by agent ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LettaBatchMessages
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.messages.list_messages_for_batch(
            batch_id="batch_id",
        )
        """
        _response = self._raw_client.list_messages_for_batch(
            batch_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            agent_id=agent_id,
            request_options=request_options,
        )
        return _response.data

    def cancel_batch(self, batch_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Cancel a batch run.

        Parameters
        ----------
        batch_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.messages.cancel_batch(
            batch_id="batch_id",
        )
        """
        _response = self._raw_client.cancel_batch(batch_id, request_options=request_options)
        return _response.data

    def retrieve_message(
        self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LettaMessageUnion]:
        """
        Retrieve a message by ID.

        Parameters
        ----------
        message_id : str
            The ID of the message in the format 'message-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LettaMessageUnion]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.messages.retrieve_message(
            message_id="message-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.retrieve_message(message_id, request_options=request_options)
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

    async def list_all_messages(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAllMessagesRequestOrder] = None,
        conversation_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[LettaMessageUnion]:
        """
        List messages across all agents for the current user.

        Parameters
        ----------
        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListAllMessagesRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        conversation_id : typing.Optional[str]
            Conversation ID to filter messages by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LettaMessageUnion]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.messages.list_all_messages()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_messages(
            before=before,
            after=after,
            limit=limit,
            order=order,
            conversation_id=conversation_id,
            request_options=request_options,
        )
        return _response.data

    async def search_all_messages(
        self,
        *,
        query: str,
        search_mode: typing.Optional[SearchAllMessagesRequestSearchMode] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        conversation_id: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SearchAllMessagesResponseItem]:
        """
        Search messages across the organization with optional agent filtering.
        Returns messages with FTS/vector ranks and total RRF score.

        This is a cloud-only feature.

        Parameters
        ----------
        query : str
            Text query for full-text search

        search_mode : typing.Optional[SearchAllMessagesRequestSearchMode]
            Search mode to use

        agent_id : typing.Optional[str]
            Filter messages by agent ID

        conversation_id : typing.Optional[str]
            Filter messages by conversation ID

        limit : typing.Optional[int]
            Maximum number of results to return

        start_date : typing.Optional[dt.datetime]
            Filter messages created after this date

        end_date : typing.Optional[dt.datetime]
            Filter messages created on or before this date

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SearchAllMessagesResponseItem]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.messages.search_all_messages(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_all_messages(
            query=query,
            search_mode=search_mode,
            agent_id=agent_id,
            conversation_id=conversation_id,
            limit=limit,
            start_date=start_date,
            end_date=end_date,
            request_options=request_options,
        )
        return _response.data

    async def list_batches(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListBatchesRequestOrder] = None,
        order_by: typing.Optional[ListBatchesRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[BatchJob]:
        """
        List all batch runs.

        Parameters
        ----------
        before : typing.Optional[str]
            Job ID cursor for pagination. Returns jobs that come before this job ID in the specified sort order

        after : typing.Optional[str]
            Job ID cursor for pagination. Returns jobs that come after this job ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of jobs to return

        order : typing.Optional[ListBatchesRequestOrder]
            Sort order for jobs by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListBatchesRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BatchJob]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.messages.list_batches()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_batches(
            before=before, after=after, limit=limit, order=order, order_by=order_by, request_options=request_options
        )
        return _response.data

    async def create_batch(
        self,
        *,
        requests: typing.Sequence[LettaBatchRequest],
        callback_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchJob:
        """
        Submit a batch of agent runs for asynchronous processing.

        Creates a job that will fan out messages to all listed agents and process them in parallel.
        The request will be rejected if it exceeds 256MB.

        Parameters
        ----------
        requests : typing.Sequence[LettaBatchRequest]
            List of requests to be processed in batch.

        callback_url : typing.Optional[str]
            Optional URL to call via POST when the batch completes. The callback payload will be a JSON object with the following fields: {'job_id': string, 'status': string, 'completed_at': string}. Where 'job_id' is the unique batch job identifier, 'status' is the final batch status (e.g., 'completed', 'failed'), and 'completed_at' is an ISO 8601 timestamp indicating when the batch job completed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchJob
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LettaBatchRequest

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.messages.create_batch(
                requests=[
                    LettaBatchRequest(
                        agent_id="agent_id",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_batch(
            requests=requests, callback_url=callback_url, request_options=request_options
        )
        return _response.data

    async def retrieve_batch(
        self, batch_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BatchJob:
        """
        Retrieve the status and details of a batch run.

        Parameters
        ----------
        batch_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchJob
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.messages.retrieve_batch(
                batch_id="batch_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_batch(batch_id, request_options=request_options)
        return _response.data

    async def list_messages_for_batch(
        self,
        batch_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListMessagesForBatchRequestOrder] = None,
        order_by: typing.Optional[ListMessagesForBatchRequestOrderBy] = None,
        agent_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LettaBatchMessages:
        """
        Get response messages for a specific batch job.

        Parameters
        ----------
        batch_id : str

        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListMessagesForBatchRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListMessagesForBatchRequestOrderBy]
            Field to sort by

        agent_id : typing.Optional[str]
            Filter messages by agent ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LettaBatchMessages
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.messages.list_messages_for_batch(
                batch_id="batch_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_messages_for_batch(
            batch_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            agent_id=agent_id,
            request_options=request_options,
        )
        return _response.data

    async def cancel_batch(
        self, batch_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Cancel a batch run.

        Parameters
        ----------
        batch_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.messages.cancel_batch(
                batch_id="batch_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_batch(batch_id, request_options=request_options)
        return _response.data

    async def retrieve_message(
        self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LettaMessageUnion]:
        """
        Retrieve a message by ID.

        Parameters
        ----------
        message_id : str
            The ID of the message in the format 'message-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LettaMessageUnion]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.messages.retrieve_message(
                message_id="message-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_message(message_id, request_options=request_options)
        return _response.data
