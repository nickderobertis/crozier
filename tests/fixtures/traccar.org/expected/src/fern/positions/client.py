

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.position import Position
from .raw_client import AsyncRawPositionsClient, RawPositionsClient


class PositionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPositionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPositionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPositionsClient
        """
        return self._raw_client

    def fetches_a_list_of_positions(
        self,
        *,
        device_id: typing.Optional[int] = None,
        from_: typing.Optional[dt.datetime] = None,
        to: typing.Optional[dt.datetime] = None,
        id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Position]:
        """
        We strongly recommend using [Traccar WebSocket API](https://www.traccar.org/traccar-api/) instead of periodically polling positions endpoint. Without any params, it returns a list of last known positions for all the user's Devices. _from_ and _to_ fields are not required with _id_.

        Parameters
        ----------
        device_id : typing.Optional[int]
            _deviceId_ is optional, but requires the _from_ and _to_ parameters when used

        from_ : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        id : typing.Optional[int]
            To fetch one or more positions. Multiple params can be passed like `id=31&id=42`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Position]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.positions.fetches_a_list_of_positions()
        """
        _response = self._raw_client.fetches_a_list_of_positions(
            device_id=device_id, from_=from_, to=to, id=id, request_options=request_options
        )
        return _response.data


class AsyncPositionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPositionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPositionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPositionsClient
        """
        return self._raw_client

    async def fetches_a_list_of_positions(
        self,
        *,
        device_id: typing.Optional[int] = None,
        from_: typing.Optional[dt.datetime] = None,
        to: typing.Optional[dt.datetime] = None,
        id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Position]:
        """
        We strongly recommend using [Traccar WebSocket API](https://www.traccar.org/traccar-api/) instead of periodically polling positions endpoint. Without any params, it returns a list of last known positions for all the user's Devices. _from_ and _to_ fields are not required with _id_.

        Parameters
        ----------
        device_id : typing.Optional[int]
            _deviceId_ is optional, but requires the _from_ and _to_ parameters when used

        from_ : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        id : typing.Optional[int]
            To fetch one or more positions. Multiple params can be passed like `id=31&id=42`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Position]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.positions.fetches_a_list_of_positions()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetches_a_list_of_positions(
            device_id=device_id, from_=from_, to=to, id=id, request_options=request_options
        )
        return _response.data
