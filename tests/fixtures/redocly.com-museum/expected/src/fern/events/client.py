

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.event_dates import EventDates
from ..types.event_description import EventDescription
from ..types.event_id import EventId
from ..types.event_location import EventLocation
from ..types.event_name import EventName
from ..types.event_price import EventPrice
from ..types.special_event import SpecialEvent
from ..types.special_event_collection import SpecialEventCollection
from .raw_client import AsyncRawEventsClient, RawEventsClient


OMIT = typing.cast(typing.Any, ...)


class EventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEventsClient
        """
        return self._raw_client

    def list_special_events(
        self,
        *,
        start_date: typing.Optional[dt.date] = None,
        end_date: typing.Optional[dt.date] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SpecialEventCollection:
        """
        Return a list of upcoming special events at the museum.

        Parameters
        ----------
        start_date : typing.Optional[dt.date]
            Starting date to retrieve future operating hours from. Defaults to today's date.

        end_date : typing.Optional[dt.date]
            End of a date range to retrieve special events for. Defaults to 7 days after `startDate`.

        page : typing.Optional[int]
            Page number to retrieve.

        limit : typing.Optional[int]
            Number of days per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpecialEventCollection
            Success.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.events.list_special_events(
            start_date=datetime.date.fromisoformat(
                "2023-02-23",
            ),
            end_date=datetime.date.fromisoformat(
                "2023-04-18",
            ),
            page=2,
            limit=15,
        )
        """
        _response = self._raw_client.list_special_events(
            start_date=start_date, end_date=end_date, page=page, limit=limit, request_options=request_options
        )
        return _response.data

    def create_special_event(
        self,
        *,
        name: EventName,
        location: EventLocation,
        event_description: EventDescription,
        dates: EventDates,
        price: EventPrice,
        event_id: typing.Optional[EventId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SpecialEvent:
        """
        Creates a new special event for the museum.

        Parameters
        ----------
        name : EventName

        location : EventLocation

        event_description : EventDescription

        dates : EventDates

        price : EventPrice

        event_id : typing.Optional[EventId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpecialEvent
            Created.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.events.create_special_event(
            name="Mermaid Treasure Identification and Analysis",
            location="Under the seaaa 🦀 🎶 🌊.",
            event_description="Join us as we review and classify a rare collection of 20 thingamabobs, gadgets, gizmos, whoosits, and whatsits, kindly donated by Ariel.",
            dates=[
                datetime.date.fromisoformat(
                    "2023-09-05",
                ),
                datetime.date.fromisoformat(
                    "2023-09-08",
                ),
            ],
            price=0.0,
        )
        """
        _response = self._raw_client.create_special_event(
            name=name,
            location=location,
            event_description=event_description,
            dates=dates,
            price=price,
            event_id=event_id,
            request_options=request_options,
        )
        return _response.data

    def get_special_event(
        self, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SpecialEvent:
        """
        Get details about a special event.

        Parameters
        ----------
        event_id : str
            Identifier for a special event.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpecialEvent
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.events.get_special_event(
            event_id="dad4bce8-f5cb-4078-a211-995864315e39",
        )
        """
        _response = self._raw_client.get_special_event(event_id, request_options=request_options)
        return _response.data

    def delete_special_event(self, event_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a special event from the collection. Allows museum to cancel planned events.

        Parameters
        ----------
        event_id : str
            Identifier for a special event.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.events.delete_special_event(
            event_id="dad4bce8-f5cb-4078-a211-995864315e39",
        )
        """
        _response = self._raw_client.delete_special_event(event_id, request_options=request_options)
        return _response.data

    def update_special_event(
        self,
        event_id: str,
        *,
        name: typing.Optional[EventName] = OMIT,
        location: typing.Optional[EventLocation] = OMIT,
        event_description: typing.Optional[EventDescription] = OMIT,
        dates: typing.Optional[EventDates] = OMIT,
        price: typing.Optional[EventPrice] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SpecialEvent:
        """
        Update the details of a special event.

        Parameters
        ----------
        event_id : str
            Identifier for a special event.

        name : typing.Optional[EventName]

        location : typing.Optional[EventLocation]

        event_description : typing.Optional[EventDescription]

        dates : typing.Optional[EventDates]

        price : typing.Optional[EventPrice]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpecialEvent
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.events.update_special_event(
            event_id="dad4bce8-f5cb-4078-a211-995864315e39",
            location="On the beach.",
            price=15.0,
        )
        """
        _response = self._raw_client.update_special_event(
            event_id,
            name=name,
            location=location,
            event_description=event_description,
            dates=dates,
            price=price,
            request_options=request_options,
        )
        return _response.data


class AsyncEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEventsClient
        """
        return self._raw_client

    async def list_special_events(
        self,
        *,
        start_date: typing.Optional[dt.date] = None,
        end_date: typing.Optional[dt.date] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SpecialEventCollection:
        """
        Return a list of upcoming special events at the museum.

        Parameters
        ----------
        start_date : typing.Optional[dt.date]
            Starting date to retrieve future operating hours from. Defaults to today's date.

        end_date : typing.Optional[dt.date]
            End of a date range to retrieve special events for. Defaults to 7 days after `startDate`.

        page : typing.Optional[int]
            Page number to retrieve.

        limit : typing.Optional[int]
            Number of days per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpecialEventCollection
            Success.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.events.list_special_events(
                start_date=datetime.date.fromisoformat(
                    "2023-02-23",
                ),
                end_date=datetime.date.fromisoformat(
                    "2023-04-18",
                ),
                page=2,
                limit=15,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_special_events(
            start_date=start_date, end_date=end_date, page=page, limit=limit, request_options=request_options
        )
        return _response.data

    async def create_special_event(
        self,
        *,
        name: EventName,
        location: EventLocation,
        event_description: EventDescription,
        dates: EventDates,
        price: EventPrice,
        event_id: typing.Optional[EventId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SpecialEvent:
        """
        Creates a new special event for the museum.

        Parameters
        ----------
        name : EventName

        location : EventLocation

        event_description : EventDescription

        dates : EventDates

        price : EventPrice

        event_id : typing.Optional[EventId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpecialEvent
            Created.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.events.create_special_event(
                name="Mermaid Treasure Identification and Analysis",
                location="Under the seaaa 🦀 🎶 🌊.",
                event_description="Join us as we review and classify a rare collection of 20 thingamabobs, gadgets, gizmos, whoosits, and whatsits, kindly donated by Ariel.",
                dates=[
                    datetime.date.fromisoformat(
                        "2023-09-05",
                    ),
                    datetime.date.fromisoformat(
                        "2023-09-08",
                    ),
                ],
                price=0.0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_special_event(
            name=name,
            location=location,
            event_description=event_description,
            dates=dates,
            price=price,
            event_id=event_id,
            request_options=request_options,
        )
        return _response.data

    async def get_special_event(
        self, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SpecialEvent:
        """
        Get details about a special event.

        Parameters
        ----------
        event_id : str
            Identifier for a special event.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpecialEvent
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
            await client.events.get_special_event(
                event_id="dad4bce8-f5cb-4078-a211-995864315e39",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_special_event(event_id, request_options=request_options)
        return _response.data

    async def delete_special_event(
        self, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a special event from the collection. Allows museum to cancel planned events.

        Parameters
        ----------
        event_id : str
            Identifier for a special event.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.events.delete_special_event(
                event_id="dad4bce8-f5cb-4078-a211-995864315e39",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_special_event(event_id, request_options=request_options)
        return _response.data

    async def update_special_event(
        self,
        event_id: str,
        *,
        name: typing.Optional[EventName] = OMIT,
        location: typing.Optional[EventLocation] = OMIT,
        event_description: typing.Optional[EventDescription] = OMIT,
        dates: typing.Optional[EventDates] = OMIT,
        price: typing.Optional[EventPrice] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SpecialEvent:
        """
        Update the details of a special event.

        Parameters
        ----------
        event_id : str
            Identifier for a special event.

        name : typing.Optional[EventName]

        location : typing.Optional[EventLocation]

        event_description : typing.Optional[EventDescription]

        dates : typing.Optional[EventDates]

        price : typing.Optional[EventPrice]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpecialEvent
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
            await client.events.update_special_event(
                event_id="dad4bce8-f5cb-4078-a211-995864315e39",
                location="On the beach.",
                price=15.0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_special_event(
            event_id,
            name=name,
            location=location,
            event_description=event_description,
            dates=dates,
            price=price,
            request_options=request_options,
        )
        return _response.data
