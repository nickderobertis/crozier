

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.endpoint_get_conversations_id import EndpointGetConversationsId
from ..types.endpoint_get_conversations_id_messages import EndpointGetConversationsIdMessages
from ..types.endpoint_get_conversations_id_statuses import EndpointGetConversationsIdStatuses
from ..types.endpoint_get_conversations_statuses import EndpointGetConversationsStatuses
from ..types.endpoint_patch_conversations_id_statuses import EndpointPatchConversationsIdStatuses
from ..types.endpoint_post_conversations_id_messages import EndpointPostConversationsIdMessages
from ..types.endpoint_post_conversations_id_schedules import EndpointPostConversationsIdSchedules
from ..types.endpoint_post_conversations_id_searches import EndpointPostConversationsIdSearches
from ..types.endpoint_post_conversations_schedules import EndpointPostConversationsSchedules
from ..types.endpoint_post_conversations_searches import EndpointPostConversationsSearches
from .raw_client import AsyncRawConversationsClient, RawConversationsClient
from .types.get_conversations_statuses_request_filter import GetConversationsStatusesRequestFilter
from .types.post_conversations_id_messages_request_metadata0privacy import (
    PostConversationsIdMessagesRequestMetadata0Privacy,
)
from .types.post_conversations_id_messages_request_metadata1privacy import (
    PostConversationsIdMessagesRequestMetadata1Privacy,
)
from .types.post_conversations_id_messages_request_metadata2privacy import (
    PostConversationsIdMessagesRequestMetadata2Privacy,
)
from .types.post_conversations_id_schedules_request_sort import PostConversationsIdSchedulesRequestSort
from .types.post_conversations_schedules_request_sort import PostConversationsSchedulesRequestSort


OMIT = typing.cast(typing.Any, ...)


class ConversationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConversationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConversationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConversationsClient
        """
        return self._raw_client

    def post_conversations_schedules(
        self,
        *,
        date: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        roll_up: typing.Optional[bool] = OMIT,
        sort: typing.Optional[PostConversationsSchedulesRequestSort] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostConversationsSchedules:
        """
        Paginated report of information about messages contributed by conversation and date. Only conversations that exist within the current access token's bubble are considered in the calculations. Optionally roll up all conversations to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages.

        Parameters
        ----------
        date : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        roll_up : typing.Optional[bool]

        sort : typing.Optional[PostConversationsSchedulesRequestSort]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostConversationsSchedules
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversations.post_conversations_schedules()
        """
        _response = self._raw_client.post_conversations_schedules(
            date=date, limit=limit, offset=offset, roll_up=roll_up, sort=sort, request_options=request_options
        )
        return _response.data

    def post_conversations_searches(
        self,
        *,
        query: str,
        date: typing.Optional[str] = OMIT,
        gt_message_id: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostConversationsSearches:
        """
        Fetch messages authored from within the current bubble that match a query string passed in as a search parameter along with their relevancy score.

        Parameters
        ----------
        query : str

        date : typing.Optional[str]

        gt_message_id : typing.Optional[int]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostConversationsSearches
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversations.post_conversations_searches(
            query="query",
        )
        """
        _response = self._raw_client.post_conversations_searches(
            query=query,
            date=date,
            gt_message_id=gt_message_id,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def get_conversations_statuses(
        self,
        *,
        filter: typing.Optional[GetConversationsStatusesRequestFilter] = None,
        include_archived: typing.Optional[bool] = None,
        bubbled: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointGetConversationsStatuses:
        """
        Retrieve conversations that you are participating in with users who exists within the same bubble, along with your current relationship with the conversations. The user_a / user_b properties of the conversation are populated with as much data as is available if the user is not you. If the user is you, only the id field is populated. There is a separate status endpoint to retrieve relationship information for individual conversations. Optionally filter: 'new' to only show conversations with messages you haven't yet seen; 'introductions' to only show conversations where users have introduced themselves to you but nothing more; 'unreplied' to only show conversations where you have introduced yourself to other users but nothing more; 'notifications' to show all conversations where the other user was the last person to message. Optionally only show conversations engaging within the existing access token's bubble. This report is limited to your ~500-1000 most recently active conversations you've engaged in within current the access token's bubble.

        Parameters
        ----------
        filter : typing.Optional[GetConversationsStatusesRequestFilter]

        include_archived : typing.Optional[bool]

        bubbled : typing.Optional[bool]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetConversationsStatuses
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversations.get_conversations_statuses()
        """
        _response = self._raw_client.get_conversations_statuses(
            filter=filter,
            include_archived=include_archived,
            bubbled=bubbled,
            offset=offset,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def get_conversations_id(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetConversationsId:
        """
        Fetch an array of conversations. You can only retrieve conversations with users who exist within the current access token's bubble.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetConversationsId
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversations.get_conversations_id(
            id="ID",
        )
        """
        _response = self._raw_client.get_conversations_id(id, request_options=request_options)
        return _response.data

    def get_conversations_id_messages(
        self,
        id: int,
        *,
        gt_message_id: typing.Optional[int] = None,
        exclude_self: typing.Optional[bool] = None,
        date: typing.Optional[str] = None,
        bubbled: typing.Optional[bool] = None,
        record_seen: typing.Optional[bool] = None,
        timeout: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointGetConversationsIdMessages:
        """
        Retrieve the last {limit} messages in the conversation, provided the conversations exist within the current access token's bubble. If a timeout is 0 or greater, the batch is sorted oldest first. Otherwise, if timeout is a negative number, the transcript is paginated and sorted newest first. Specify a timeout for long polling (which delays the server sending back results for up to n seconds or until results are available, whichever comes first), or default to 0 for immediate results. Optionally record your status as online along with sharing the latest message you've seen with the other conversation participant. Optionally specify a gt_message_id to retrieve only messages with an ID greater than that specified (such as greater than the latest message ID received in the last poll). Optionally only poll for messages authored by the other person in the conversation, and echo messages authored by you when sending, for a perceived increase in performance. Optionally only retrieve messages that were posted from within the current access token's bubble. Optionally specify a date formatted as YYYY-MM-DD to retrieve a transcript of messages from a single day. When record_seen is set to true, the new message count for the conversation is reset to zero.

        Parameters
        ----------
        id : int

        gt_message_id : typing.Optional[int]

        exclude_self : typing.Optional[bool]

        date : typing.Optional[str]

        bubbled : typing.Optional[bool]

        record_seen : typing.Optional[bool]

        timeout : typing.Optional[int]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetConversationsIdMessages
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversations.get_conversations_id_messages(
            id=1,
        )
        """
        _response = self._raw_client.get_conversations_id_messages(
            id,
            gt_message_id=gt_message_id,
            exclude_self=exclude_self,
            date=date,
            bubbled=bubbled,
            record_seen=record_seen,
            timeout=timeout,
            offset=offset,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def post_conversations_id_messages(
        self,
        id: int,
        *,
        text_raw: str,
        bubbled: typing.Optional[bool] = OMIT,
        metadata0key: typing.Optional[str] = OMIT,
        metadata0privacy: typing.Optional[PostConversationsIdMessagesRequestMetadata0Privacy] = OMIT,
        metadata0values: typing.Optional[typing.List[str]] = OMIT,
        metadata1key: typing.Optional[str] = OMIT,
        metadata1privacy: typing.Optional[PostConversationsIdMessagesRequestMetadata1Privacy] = OMIT,
        metadata1values: typing.Optional[typing.List[str]] = OMIT,
        metadata2key: typing.Optional[str] = OMIT,
        metadata2privacy: typing.Optional[PostConversationsIdMessagesRequestMetadata2Privacy] = OMIT,
        metadata2values: typing.Optional[typing.List[str]] = OMIT,
        text_emoticons: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostConversationsIdMessages:
        """
        Post a message to a conversation that is with a user who exists within the current access token's bubble. Optionally specify whether emoticons should be parsed into smiley images. Optionally specify whether the message should be bubbled within the app. Additionally, optionally attach a single metadata key/value pair to the message upon submission.

        Parameters
        ----------
        id : int

        text_raw : str

        bubbled : typing.Optional[bool]

        metadata0key : typing.Optional[str]

        metadata0privacy : typing.Optional[PostConversationsIdMessagesRequestMetadata0Privacy]

        metadata0values : typing.Optional[typing.List[str]]

        metadata1key : typing.Optional[str]

        metadata1privacy : typing.Optional[PostConversationsIdMessagesRequestMetadata1Privacy]

        metadata1values : typing.Optional[typing.List[str]]

        metadata2key : typing.Optional[str]

        metadata2privacy : typing.Optional[PostConversationsIdMessagesRequestMetadata2Privacy]

        metadata2values : typing.Optional[typing.List[str]]

        text_emoticons : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostConversationsIdMessages
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversations.post_conversations_id_messages(
            id=1,
            text_raw="text_raw",
        )
        """
        _response = self._raw_client.post_conversations_id_messages(
            id,
            text_raw=text_raw,
            bubbled=bubbled,
            metadata0key=metadata0key,
            metadata0privacy=metadata0privacy,
            metadata0values=metadata0values,
            metadata1key=metadata1key,
            metadata1privacy=metadata1privacy,
            metadata1values=metadata1values,
            metadata2key=metadata2key,
            metadata2privacy=metadata2privacy,
            metadata2values=metadata2values,
            text_emoticons=text_emoticons,
            request_options=request_options,
        )
        return _response.data

    def post_conversations_id_schedules(
        self,
        id: typing.Sequence[int],
        *,
        date: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        roll_up: typing.Optional[bool] = OMIT,
        sort: typing.Optional[PostConversationsIdSchedulesRequestSort] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostConversationsIdSchedules:
        """
        Paginated report of information about messages contributed by conversation and date. Only conversations that exist within the current access token's bubble are considered in the calculations. Optionally roll up all conversations to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages within the conversation(s).

        Parameters
        ----------
        id : typing.Sequence[int]

        date : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        roll_up : typing.Optional[bool]

        sort : typing.Optional[PostConversationsIdSchedulesRequestSort]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostConversationsIdSchedules
            Valid Response
        """
        _response = self._raw_client.post_conversations_id_schedules(
            id, date=date, limit=limit, offset=offset, roll_up=roll_up, sort=sort, request_options=request_options
        )
        return _response.data

    def post_conversations_id_searches(
        self,
        id: typing.Sequence[int],
        *,
        query: str,
        date: typing.Optional[str] = OMIT,
        gt_message_id: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostConversationsIdSearches:
        """
        Fetch messages authored from within specified conversations that match a query string passed in as a search parameter along with their relevancy score.

        Parameters
        ----------
        id : typing.Sequence[int]

        query : str

        date : typing.Optional[str]

        gt_message_id : typing.Optional[int]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostConversationsIdSearches
            Valid Response
        """
        _response = self._raw_client.post_conversations_id_searches(
            id,
            query=query,
            date=date,
            gt_message_id=gt_message_id,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def get_conversations_id_statuses(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetConversationsIdStatuses:
        """
        Status information about your current relationship with one or more conversations you participating in, provided the conversations exist within the current access token's bubble.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetConversationsIdStatuses
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversations.get_conversations_id_statuses(
            id="ID",
        )
        """
        _response = self._raw_client.get_conversations_id_statuses(id, request_options=request_options)
        return _response.data

    def patch_conversations_id_statuses(
        self, id: int, *, archived_status: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointPatchConversationsIdStatuses:
        """
        Archive or unarchive a conversation that is with a user who exists within the same bubble.

        Parameters
        ----------
        id : int

        archived_status : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPatchConversationsIdStatuses
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.conversations.patch_conversations_id_statuses(
            id=1,
            archived_status=True,
        )
        """
        _response = self._raw_client.patch_conversations_id_statuses(
            id, archived_status=archived_status, request_options=request_options
        )
        return _response.data


class AsyncConversationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConversationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConversationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConversationsClient
        """
        return self._raw_client

    async def post_conversations_schedules(
        self,
        *,
        date: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        roll_up: typing.Optional[bool] = OMIT,
        sort: typing.Optional[PostConversationsSchedulesRequestSort] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostConversationsSchedules:
        """
        Paginated report of information about messages contributed by conversation and date. Only conversations that exist within the current access token's bubble are considered in the calculations. Optionally roll up all conversations to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages.

        Parameters
        ----------
        date : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        roll_up : typing.Optional[bool]

        sort : typing.Optional[PostConversationsSchedulesRequestSort]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostConversationsSchedules
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.post_conversations_schedules()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_conversations_schedules(
            date=date, limit=limit, offset=offset, roll_up=roll_up, sort=sort, request_options=request_options
        )
        return _response.data

    async def post_conversations_searches(
        self,
        *,
        query: str,
        date: typing.Optional[str] = OMIT,
        gt_message_id: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostConversationsSearches:
        """
        Fetch messages authored from within the current bubble that match a query string passed in as a search parameter along with their relevancy score.

        Parameters
        ----------
        query : str

        date : typing.Optional[str]

        gt_message_id : typing.Optional[int]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostConversationsSearches
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.post_conversations_searches(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_conversations_searches(
            query=query,
            date=date,
            gt_message_id=gt_message_id,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def get_conversations_statuses(
        self,
        *,
        filter: typing.Optional[GetConversationsStatusesRequestFilter] = None,
        include_archived: typing.Optional[bool] = None,
        bubbled: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointGetConversationsStatuses:
        """
        Retrieve conversations that you are participating in with users who exists within the same bubble, along with your current relationship with the conversations. The user_a / user_b properties of the conversation are populated with as much data as is available if the user is not you. If the user is you, only the id field is populated. There is a separate status endpoint to retrieve relationship information for individual conversations. Optionally filter: 'new' to only show conversations with messages you haven't yet seen; 'introductions' to only show conversations where users have introduced themselves to you but nothing more; 'unreplied' to only show conversations where you have introduced yourself to other users but nothing more; 'notifications' to show all conversations where the other user was the last person to message. Optionally only show conversations engaging within the existing access token's bubble. This report is limited to your ~500-1000 most recently active conversations you've engaged in within current the access token's bubble.

        Parameters
        ----------
        filter : typing.Optional[GetConversationsStatusesRequestFilter]

        include_archived : typing.Optional[bool]

        bubbled : typing.Optional[bool]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetConversationsStatuses
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.get_conversations_statuses()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_conversations_statuses(
            filter=filter,
            include_archived=include_archived,
            bubbled=bubbled,
            offset=offset,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def get_conversations_id(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetConversationsId:
        """
        Fetch an array of conversations. You can only retrieve conversations with users who exist within the current access token's bubble.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetConversationsId
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.get_conversations_id(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_conversations_id(id, request_options=request_options)
        return _response.data

    async def get_conversations_id_messages(
        self,
        id: int,
        *,
        gt_message_id: typing.Optional[int] = None,
        exclude_self: typing.Optional[bool] = None,
        date: typing.Optional[str] = None,
        bubbled: typing.Optional[bool] = None,
        record_seen: typing.Optional[bool] = None,
        timeout: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointGetConversationsIdMessages:
        """
        Retrieve the last {limit} messages in the conversation, provided the conversations exist within the current access token's bubble. If a timeout is 0 or greater, the batch is sorted oldest first. Otherwise, if timeout is a negative number, the transcript is paginated and sorted newest first. Specify a timeout for long polling (which delays the server sending back results for up to n seconds or until results are available, whichever comes first), or default to 0 for immediate results. Optionally record your status as online along with sharing the latest message you've seen with the other conversation participant. Optionally specify a gt_message_id to retrieve only messages with an ID greater than that specified (such as greater than the latest message ID received in the last poll). Optionally only poll for messages authored by the other person in the conversation, and echo messages authored by you when sending, for a perceived increase in performance. Optionally only retrieve messages that were posted from within the current access token's bubble. Optionally specify a date formatted as YYYY-MM-DD to retrieve a transcript of messages from a single day. When record_seen is set to true, the new message count for the conversation is reset to zero.

        Parameters
        ----------
        id : int

        gt_message_id : typing.Optional[int]

        exclude_self : typing.Optional[bool]

        date : typing.Optional[str]

        bubbled : typing.Optional[bool]

        record_seen : typing.Optional[bool]

        timeout : typing.Optional[int]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetConversationsIdMessages
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.get_conversations_id_messages(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_conversations_id_messages(
            id,
            gt_message_id=gt_message_id,
            exclude_self=exclude_self,
            date=date,
            bubbled=bubbled,
            record_seen=record_seen,
            timeout=timeout,
            offset=offset,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def post_conversations_id_messages(
        self,
        id: int,
        *,
        text_raw: str,
        bubbled: typing.Optional[bool] = OMIT,
        metadata0key: typing.Optional[str] = OMIT,
        metadata0privacy: typing.Optional[PostConversationsIdMessagesRequestMetadata0Privacy] = OMIT,
        metadata0values: typing.Optional[typing.List[str]] = OMIT,
        metadata1key: typing.Optional[str] = OMIT,
        metadata1privacy: typing.Optional[PostConversationsIdMessagesRequestMetadata1Privacy] = OMIT,
        metadata1values: typing.Optional[typing.List[str]] = OMIT,
        metadata2key: typing.Optional[str] = OMIT,
        metadata2privacy: typing.Optional[PostConversationsIdMessagesRequestMetadata2Privacy] = OMIT,
        metadata2values: typing.Optional[typing.List[str]] = OMIT,
        text_emoticons: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostConversationsIdMessages:
        """
        Post a message to a conversation that is with a user who exists within the current access token's bubble. Optionally specify whether emoticons should be parsed into smiley images. Optionally specify whether the message should be bubbled within the app. Additionally, optionally attach a single metadata key/value pair to the message upon submission.

        Parameters
        ----------
        id : int

        text_raw : str

        bubbled : typing.Optional[bool]

        metadata0key : typing.Optional[str]

        metadata0privacy : typing.Optional[PostConversationsIdMessagesRequestMetadata0Privacy]

        metadata0values : typing.Optional[typing.List[str]]

        metadata1key : typing.Optional[str]

        metadata1privacy : typing.Optional[PostConversationsIdMessagesRequestMetadata1Privacy]

        metadata1values : typing.Optional[typing.List[str]]

        metadata2key : typing.Optional[str]

        metadata2privacy : typing.Optional[PostConversationsIdMessagesRequestMetadata2Privacy]

        metadata2values : typing.Optional[typing.List[str]]

        text_emoticons : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostConversationsIdMessages
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.post_conversations_id_messages(
                id=1,
                text_raw="text_raw",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_conversations_id_messages(
            id,
            text_raw=text_raw,
            bubbled=bubbled,
            metadata0key=metadata0key,
            metadata0privacy=metadata0privacy,
            metadata0values=metadata0values,
            metadata1key=metadata1key,
            metadata1privacy=metadata1privacy,
            metadata1values=metadata1values,
            metadata2key=metadata2key,
            metadata2privacy=metadata2privacy,
            metadata2values=metadata2values,
            text_emoticons=text_emoticons,
            request_options=request_options,
        )
        return _response.data

    async def post_conversations_id_schedules(
        self,
        id: typing.Sequence[int],
        *,
        date: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        roll_up: typing.Optional[bool] = OMIT,
        sort: typing.Optional[PostConversationsIdSchedulesRequestSort] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostConversationsIdSchedules:
        """
        Paginated report of information about messages contributed by conversation and date. Only conversations that exist within the current access token's bubble are considered in the calculations. Optionally roll up all conversations to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages within the conversation(s).

        Parameters
        ----------
        id : typing.Sequence[int]

        date : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        roll_up : typing.Optional[bool]

        sort : typing.Optional[PostConversationsIdSchedulesRequestSort]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostConversationsIdSchedules
            Valid Response
        """
        _response = await self._raw_client.post_conversations_id_schedules(
            id, date=date, limit=limit, offset=offset, roll_up=roll_up, sort=sort, request_options=request_options
        )
        return _response.data

    async def post_conversations_id_searches(
        self,
        id: typing.Sequence[int],
        *,
        query: str,
        date: typing.Optional[str] = OMIT,
        gt_message_id: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostConversationsIdSearches:
        """
        Fetch messages authored from within specified conversations that match a query string passed in as a search parameter along with their relevancy score.

        Parameters
        ----------
        id : typing.Sequence[int]

        query : str

        date : typing.Optional[str]

        gt_message_id : typing.Optional[int]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostConversationsIdSearches
            Valid Response
        """
        _response = await self._raw_client.post_conversations_id_searches(
            id,
            query=query,
            date=date,
            gt_message_id=gt_message_id,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def get_conversations_id_statuses(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetConversationsIdStatuses:
        """
        Status information about your current relationship with one or more conversations you participating in, provided the conversations exist within the current access token's bubble.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetConversationsIdStatuses
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.get_conversations_id_statuses(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_conversations_id_statuses(id, request_options=request_options)
        return _response.data

    async def patch_conversations_id_statuses(
        self, id: int, *, archived_status: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointPatchConversationsIdStatuses:
        """
        Archive or unarchive a conversation that is with a user who exists within the same bubble.

        Parameters
        ----------
        id : int

        archived_status : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPatchConversationsIdStatuses
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.conversations.patch_conversations_id_statuses(
                id=1,
                archived_status=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_conversations_id_statuses(
            id, archived_status=archived_status, request_options=request_options
        )
        return _response.data
