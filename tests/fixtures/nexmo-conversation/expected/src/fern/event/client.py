

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.event_body import EventBody
from ..types.event_retrieved import EventRetrieved
from ..types.event_type import EventType
from ..types.member_id import MemberId
from .raw_client import AsyncRawEventClient, RawEventClient
from .types.create_event_response import CreateEventResponse


OMIT = typing.cast(typing.Any, ...)


class EventClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEventClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEventClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEventClient
        """
        return self._raw_client

    def get_events(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[EventRetrieved]:
        """
        This endpoint is **DEPRECATED**. Please use [/v0.2/events](/api/conversation.v2#get-events).

        Parameters
        ----------
        conversation_id : str
            Conversation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EventRetrieved]
            Retrieve Events Response Payload Object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event.get_events(
            conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
        )
        """
        _response = self._raw_client.get_events(conversation_id, request_options=request_options)
        return _response.data

    def create_event(
        self,
        conversation_id: str,
        *,
        from_: MemberId,
        type: EventType,
        body: typing.Optional[EventBody] = OMIT,
        to: typing.Optional[MemberId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateEventResponse:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        from_ : MemberId

        type : EventType

        body : typing.Optional[EventBody]

        to : typing.Optional[MemberId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateEventResponse
            Create New Event Response Payload Object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event.create_event(
            conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
            from_="MEM-63f61863-4a51-4f6b-86e1-46edebio0391",
            type="text",
        )
        """
        _response = self._raw_client.create_event(
            conversation_id, from_=from_, type=type, body=body, to=to, request_options=request_options
        )
        return _response.data

    def get_event(
        self, conversation_id: str, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EventRetrieved:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        event_id : str
            Event ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventRetrieved
            Retrieve an event Content Payload

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event.get_event(
            conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
            event_id="event_id",
        )
        """
        _response = self._raw_client.get_event(conversation_id, event_id, request_options=request_options)
        return _response.data

    def delete_event(
        self, conversation_id: str, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        event_id : str
            Event ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Success response with empty JSON

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event.delete_event(
            conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
            event_id="event_id",
        )
        """
        _response = self._raw_client.delete_event(conversation_id, event_id, request_options=request_options)
        return _response.data


class AsyncEventClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEventClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEventClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEventClient
        """
        return self._raw_client

    async def get_events(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[EventRetrieved]:
        """
        This endpoint is **DEPRECATED**. Please use [/v0.2/events](/api/conversation.v2#get-events).

        Parameters
        ----------
        conversation_id : str
            Conversation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EventRetrieved]
            Retrieve Events Response Payload Object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event.get_events(
                conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_events(conversation_id, request_options=request_options)
        return _response.data

    async def create_event(
        self,
        conversation_id: str,
        *,
        from_: MemberId,
        type: EventType,
        body: typing.Optional[EventBody] = OMIT,
        to: typing.Optional[MemberId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateEventResponse:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        from_ : MemberId

        type : EventType

        body : typing.Optional[EventBody]

        to : typing.Optional[MemberId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateEventResponse
            Create New Event Response Payload Object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event.create_event(
                conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
                from_="MEM-63f61863-4a51-4f6b-86e1-46edebio0391",
                type="text",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_event(
            conversation_id, from_=from_, type=type, body=body, to=to, request_options=request_options
        )
        return _response.data

    async def get_event(
        self, conversation_id: str, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EventRetrieved:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        event_id : str
            Event ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventRetrieved
            Retrieve an event Content Payload

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event.get_event(
                conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
                event_id="event_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_event(conversation_id, event_id, request_options=request_options)
        return _response.data

    async def delete_event(
        self, conversation_id: str, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        event_id : str
            Event ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Success response with empty JSON

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event.delete_event(
                conversation_id="CON-f972836a-550f-45fa-956c-12a2ab5b7d22",
                event_id="event_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_event(conversation_id, event_id, request_options=request_options)
        return _response.data
