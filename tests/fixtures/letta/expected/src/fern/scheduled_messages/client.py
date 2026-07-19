

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawScheduledMessagesClient, RawScheduledMessagesClient
from .types.scheduled_messages_delete_scheduled_message_request_body import (
    ScheduledMessagesDeleteScheduledMessageRequestBody,
)
from .types.scheduled_messages_delete_scheduled_message_response import ScheduledMessagesDeleteScheduledMessageResponse
from .types.scheduled_messages_list_scheduled_messages_response import ScheduledMessagesListScheduledMessagesResponse
from .types.scheduled_messages_retrieve_scheduled_message_response import (
    ScheduledMessagesRetrieveScheduledMessageResponse,
)
from .types.scheduled_messages_schedule_agent_message_request_include_return_message_types_item import (
    ScheduledMessagesScheduleAgentMessageRequestIncludeReturnMessageTypesItem,
)
from .types.scheduled_messages_schedule_agent_message_request_messages_item import (
    ScheduledMessagesScheduleAgentMessageRequestMessagesItem,
)
from .types.scheduled_messages_schedule_agent_message_request_schedule import (
    ScheduledMessagesScheduleAgentMessageRequestSchedule,
)
from .types.scheduled_messages_schedule_agent_message_response import ScheduledMessagesScheduleAgentMessageResponse


OMIT = typing.cast(typing.Any, ...)


class ScheduledMessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawScheduledMessagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawScheduledMessagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawScheduledMessagesClient
        """
        return self._raw_client

    def scheduled_messages_list_scheduled_messages(
        self,
        agent_id: str,
        *,
        limit: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduledMessagesListScheduledMessagesResponse:
        """
        List all scheduled messages for a specific agent.

        Parameters
        ----------
        agent_id : str

        limit : typing.Optional[str]

        after : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduledMessagesListScheduledMessagesResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.scheduled_messages.scheduled_messages_list_scheduled_messages(
            agent_id="agent_id",
        )
        """
        _response = self._raw_client.scheduled_messages_list_scheduled_messages(
            agent_id, limit=limit, after=after, request_options=request_options
        )
        return _response.data

    def scheduled_messages_schedule_agent_message(
        self,
        agent_id: str,
        *,
        messages: typing.Sequence[ScheduledMessagesScheduleAgentMessageRequestMessagesItem],
        schedule: ScheduledMessagesScheduleAgentMessageRequestSchedule,
        max_steps: typing.Optional[float] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        include_return_message_types: typing.Optional[
            typing.Sequence[ScheduledMessagesScheduleAgentMessageRequestIncludeReturnMessageTypesItem]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduledMessagesScheduleAgentMessageResponse:
        """
        Schedule a message to be sent by the agent at a specified time or on a recurring basis.

        Parameters
        ----------
        agent_id : str

        messages : typing.Sequence[ScheduledMessagesScheduleAgentMessageRequestMessagesItem]

        schedule : ScheduledMessagesScheduleAgentMessageRequestSchedule

        max_steps : typing.Optional[float]

        callback_url : typing.Optional[str]

        include_return_message_types : typing.Optional[typing.Sequence[ScheduledMessagesScheduleAgentMessageRequestIncludeReturnMessageTypesItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduledMessagesScheduleAgentMessageResponse
            201

        Examples
        --------
        from fern.scheduled_messages import (
            ScheduledMessagesScheduleAgentMessageRequestMessagesItem,
            ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem_Text,
            ScheduledMessagesScheduleAgentMessageRequestMessagesItemRole,
            ScheduledMessagesScheduleAgentMessageRequestSchedule_OneTime,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.scheduled_messages.scheduled_messages_schedule_agent_message(
            agent_id="agent_id",
            messages=[
                ScheduledMessagesScheduleAgentMessageRequestMessagesItem(
                    content=[
                        ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem_Text(
                            text="text",
                        )
                    ],
                    role=ScheduledMessagesScheduleAgentMessageRequestMessagesItemRole.USER,
                )
            ],
            schedule=ScheduledMessagesScheduleAgentMessageRequestSchedule_OneTime(
                scheduled_at=1.1,
            ),
        )
        """
        _response = self._raw_client.scheduled_messages_schedule_agent_message(
            agent_id,
            messages=messages,
            schedule=schedule,
            max_steps=max_steps,
            callback_url=callback_url,
            include_return_message_types=include_return_message_types,
            request_options=request_options,
        )
        return _response.data

    def scheduled_messages_retrieve_scheduled_message(
        self, agent_id: str, scheduled_message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ScheduledMessagesRetrieveScheduledMessageResponse:
        """
        Retrieve a scheduled message by its ID for a specific agent.

        Parameters
        ----------
        agent_id : str

        scheduled_message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduledMessagesRetrieveScheduledMessageResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.scheduled_messages.scheduled_messages_retrieve_scheduled_message(
            agent_id="agent_id",
            scheduled_message_id="scheduled_message_id",
        )
        """
        _response = self._raw_client.scheduled_messages_retrieve_scheduled_message(
            agent_id, scheduled_message_id, request_options=request_options
        )
        return _response.data

    def scheduled_messages_delete_scheduled_message(
        self,
        agent_id: str,
        scheduled_message_id: str,
        *,
        request: typing.Optional[ScheduledMessagesDeleteScheduledMessageRequestBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduledMessagesDeleteScheduledMessageResponse:
        """
        Delete a scheduled message by its ID for a specific agent.

        Parameters
        ----------
        agent_id : str

        scheduled_message_id : str

        request : typing.Optional[ScheduledMessagesDeleteScheduledMessageRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduledMessagesDeleteScheduledMessageResponse
            200

        Examples
        --------
        from fern.scheduled_messages import (
            ScheduledMessagesDeleteScheduledMessageRequestBody,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.scheduled_messages.scheduled_messages_delete_scheduled_message(
            agent_id="agent_id",
            scheduled_message_id="scheduled_message_id",
            request=ScheduledMessagesDeleteScheduledMessageRequestBody(),
        )
        """
        _response = self._raw_client.scheduled_messages_delete_scheduled_message(
            agent_id, scheduled_message_id, request=request, request_options=request_options
        )
        return _response.data


class AsyncScheduledMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawScheduledMessagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawScheduledMessagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawScheduledMessagesClient
        """
        return self._raw_client

    async def scheduled_messages_list_scheduled_messages(
        self,
        agent_id: str,
        *,
        limit: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduledMessagesListScheduledMessagesResponse:
        """
        List all scheduled messages for a specific agent.

        Parameters
        ----------
        agent_id : str

        limit : typing.Optional[str]

        after : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduledMessagesListScheduledMessagesResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.scheduled_messages.scheduled_messages_list_scheduled_messages(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.scheduled_messages_list_scheduled_messages(
            agent_id, limit=limit, after=after, request_options=request_options
        )
        return _response.data

    async def scheduled_messages_schedule_agent_message(
        self,
        agent_id: str,
        *,
        messages: typing.Sequence[ScheduledMessagesScheduleAgentMessageRequestMessagesItem],
        schedule: ScheduledMessagesScheduleAgentMessageRequestSchedule,
        max_steps: typing.Optional[float] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        include_return_message_types: typing.Optional[
            typing.Sequence[ScheduledMessagesScheduleAgentMessageRequestIncludeReturnMessageTypesItem]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduledMessagesScheduleAgentMessageResponse:
        """
        Schedule a message to be sent by the agent at a specified time or on a recurring basis.

        Parameters
        ----------
        agent_id : str

        messages : typing.Sequence[ScheduledMessagesScheduleAgentMessageRequestMessagesItem]

        schedule : ScheduledMessagesScheduleAgentMessageRequestSchedule

        max_steps : typing.Optional[float]

        callback_url : typing.Optional[str]

        include_return_message_types : typing.Optional[typing.Sequence[ScheduledMessagesScheduleAgentMessageRequestIncludeReturnMessageTypesItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduledMessagesScheduleAgentMessageResponse
            201

        Examples
        --------
        import asyncio

        from fern.scheduled_messages import (
            ScheduledMessagesScheduleAgentMessageRequestMessagesItem,
            ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem_Text,
            ScheduledMessagesScheduleAgentMessageRequestMessagesItemRole,
            ScheduledMessagesScheduleAgentMessageRequestSchedule_OneTime,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.scheduled_messages.scheduled_messages_schedule_agent_message(
                agent_id="agent_id",
                messages=[
                    ScheduledMessagesScheduleAgentMessageRequestMessagesItem(
                        content=[
                            ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem_Text(
                                text="text",
                            )
                        ],
                        role=ScheduledMessagesScheduleAgentMessageRequestMessagesItemRole.USER,
                    )
                ],
                schedule=ScheduledMessagesScheduleAgentMessageRequestSchedule_OneTime(
                    scheduled_at=1.1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.scheduled_messages_schedule_agent_message(
            agent_id,
            messages=messages,
            schedule=schedule,
            max_steps=max_steps,
            callback_url=callback_url,
            include_return_message_types=include_return_message_types,
            request_options=request_options,
        )
        return _response.data

    async def scheduled_messages_retrieve_scheduled_message(
        self, agent_id: str, scheduled_message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ScheduledMessagesRetrieveScheduledMessageResponse:
        """
        Retrieve a scheduled message by its ID for a specific agent.

        Parameters
        ----------
        agent_id : str

        scheduled_message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduledMessagesRetrieveScheduledMessageResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.scheduled_messages.scheduled_messages_retrieve_scheduled_message(
                agent_id="agent_id",
                scheduled_message_id="scheduled_message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.scheduled_messages_retrieve_scheduled_message(
            agent_id, scheduled_message_id, request_options=request_options
        )
        return _response.data

    async def scheduled_messages_delete_scheduled_message(
        self,
        agent_id: str,
        scheduled_message_id: str,
        *,
        request: typing.Optional[ScheduledMessagesDeleteScheduledMessageRequestBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduledMessagesDeleteScheduledMessageResponse:
        """
        Delete a scheduled message by its ID for a specific agent.

        Parameters
        ----------
        agent_id : str

        scheduled_message_id : str

        request : typing.Optional[ScheduledMessagesDeleteScheduledMessageRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduledMessagesDeleteScheduledMessageResponse
            200

        Examples
        --------
        import asyncio

        from fern.scheduled_messages import (
            ScheduledMessagesDeleteScheduledMessageRequestBody,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.scheduled_messages.scheduled_messages_delete_scheduled_message(
                agent_id="agent_id",
                scheduled_message_id="scheduled_message_id",
                request=ScheduledMessagesDeleteScheduledMessageRequestBody(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.scheduled_messages_delete_scheduled_message(
            agent_id, scheduled_message_id, request=request, request_options=request_options
        )
        return _response.data
