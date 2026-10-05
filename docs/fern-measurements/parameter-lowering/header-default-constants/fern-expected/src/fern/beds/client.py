

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBedsClient, RawBedsClient
from .types.list_beds_request_x_vent_mode import ListBedsRequestXVentMode


class BedsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBedsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBedsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBedsClient
        """
        return self._raw_client

    def list_beds(
        self,
        *,
        section: str,
        lamp_watts: int,
        vent_mode: ListBedsRequestXVentMode,
        fan_speed: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        section : str

        lamp_watts : int

        vent_mode : ListBedsRequestXVentMode

        fan_speed : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Beds.

        Examples
        --------
        from fern.beds import ListBedsRequestXVentMode

        from fern import FernApi

        client = FernApi()
        client.beds.list_beds(
            lamp_watts=1,
            vent_mode=ListBedsRequestXVentMode.OPEN,
            section="section",
        )
        """
        _response = self._raw_client.list_beds(
            section=section,
            lamp_watts=lamp_watts,
            vent_mode=vent_mode,
            fan_speed=fan_speed,
            request_options=request_options,
        )
        return _response.data

    def get_bed(self, bed_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        bed_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            One bed.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.beds.get_bed(
            bed_id="bed_id",
        )
        """
        _response = self._raw_client.get_bed(bed_id, request_options=request_options)
        return _response.data


class AsyncBedsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBedsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBedsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBedsClient
        """
        return self._raw_client

    async def list_beds(
        self,
        *,
        section: str,
        lamp_watts: int,
        vent_mode: ListBedsRequestXVentMode,
        fan_speed: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        section : str

        lamp_watts : int

        vent_mode : ListBedsRequestXVentMode

        fan_speed : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Beds.

        Examples
        --------
        import asyncio

        from fern.beds import ListBedsRequestXVentMode

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.beds.list_beds(
                lamp_watts=1,
                vent_mode=ListBedsRequestXVentMode.OPEN,
                section="section",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_beds(
            section=section,
            lamp_watts=lamp_watts,
            vent_mode=vent_mode,
            fan_speed=fan_speed,
            request_options=request_options,
        )
        return _response.data

    async def get_bed(self, bed_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        bed_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            One bed.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.beds.get_bed(
                bed_id="bed_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bed(bed_id, request_options=request_options)
        return _response.data
