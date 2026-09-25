

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.json_success import JsonSuccess
from .raw_client import AsyncRawRemindersClient, RawRemindersClient
from .types.create_message_reminder_response import CreateMessageReminderResponse
from .types.get_reminders_response import GetRemindersResponse


OMIT = typing.cast(typing.Any, ...)


class RemindersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRemindersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRemindersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRemindersClient
        """
        return self._raw_client

    def get_reminders(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetRemindersResponse:
        """
        Fetch all [reminders](/help/schedule-a-reminder) for the
        current user.

        Reminders are messages the user has scheduled to be sent in the
        future to themself.

        **Changes**: New in Zulip 11.0 (feature level 399).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRemindersResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.reminders.get_reminders()
        """
        _response = self._raw_client.get_reminders(request_options=request_options)
        return _response.data

    def create_message_reminder(
        self,
        *,
        message_id: typing.Optional[int] = OMIT,
        scheduled_delivery_timestamp: typing.Optional[int] = OMIT,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateMessageReminderResponse:
        """
        Schedule a reminder to be sent to the current user at the specified time. The reminder will link the relevant message.

        **Changes**: New in Zulip 11.0 (feature level 381).

        Parameters
        ----------
        message_id : typing.Optional[int]
            The ID of the previously sent message to reference in the reminder message.

        scheduled_delivery_timestamp : typing.Optional[int]
            The UNIX timestamp for when the reminder will be sent,
            in UTC seconds.

        note : typing.Optional[str]
            A note associated with the reminder shown in the Notification Bot message.

            **Changes**: New in Zulip 11.0 (feature level 415).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateMessageReminderResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.reminders.create_message_reminder()
        """
        _response = self._raw_client.create_message_reminder(
            message_id=message_id,
            scheduled_delivery_timestamp=scheduled_delivery_timestamp,
            note=note,
            request_options=request_options,
        )
        return _response.data

    def delete_reminder(
        self, reminder_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Delete, and therefore cancel sending, a previously [scheduled
        reminder](/help/schedule-a-reminder).

        **Changes**: New in Zulip 11.0 (feature level 399).

        Parameters
        ----------
        reminder_id : int
            The ID of the reminder to delete.

            This is different from the unique ID that the message would have
            after being sent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.reminders.delete_reminder(
            reminder_id=1,
        )
        """
        _response = self._raw_client.delete_reminder(reminder_id, request_options=request_options)
        return _response.data


class AsyncRemindersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRemindersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRemindersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRemindersClient
        """
        return self._raw_client

    async def get_reminders(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetRemindersResponse:
        """
        Fetch all [reminders](/help/schedule-a-reminder) for the
        current user.

        Reminders are messages the user has scheduled to be sent in the
        future to themself.

        **Changes**: New in Zulip 11.0 (feature level 399).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRemindersResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.reminders.get_reminders()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_reminders(request_options=request_options)
        return _response.data

    async def create_message_reminder(
        self,
        *,
        message_id: typing.Optional[int] = OMIT,
        scheduled_delivery_timestamp: typing.Optional[int] = OMIT,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateMessageReminderResponse:
        """
        Schedule a reminder to be sent to the current user at the specified time. The reminder will link the relevant message.

        **Changes**: New in Zulip 11.0 (feature level 381).

        Parameters
        ----------
        message_id : typing.Optional[int]
            The ID of the previously sent message to reference in the reminder message.

        scheduled_delivery_timestamp : typing.Optional[int]
            The UNIX timestamp for when the reminder will be sent,
            in UTC seconds.

        note : typing.Optional[str]
            A note associated with the reminder shown in the Notification Bot message.

            **Changes**: New in Zulip 11.0 (feature level 415).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateMessageReminderResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.reminders.create_message_reminder()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_message_reminder(
            message_id=message_id,
            scheduled_delivery_timestamp=scheduled_delivery_timestamp,
            note=note,
            request_options=request_options,
        )
        return _response.data

    async def delete_reminder(
        self, reminder_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonSuccess:
        """
        Delete, and therefore cancel sending, a previously [scheduled
        reminder](/help/schedule-a-reminder).

        **Changes**: New in Zulip 11.0 (feature level 399).

        Parameters
        ----------
        reminder_id : int
            The ID of the reminder to delete.

            This is different from the unique ID that the message would have
            after being sent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonSuccess
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.reminders.delete_reminder(
                reminder_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_reminder(reminder_id, request_options=request_options)
        return _response.data
