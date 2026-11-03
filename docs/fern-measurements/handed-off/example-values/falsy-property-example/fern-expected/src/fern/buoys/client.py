

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBuoysClient, RawBuoysClient
from .types.record_reading_response import RecordReadingResponse
from .types.register_buoy_response import RegisterBuoyResponse


OMIT = typing.cast(typing.Any, ...)


class BuoysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBuoysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBuoysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBuoysClient
        """
        return self._raw_client

    def register_buoy(
        self,
        *,
        survey_ref: str,
        label: str,
        depth_metres: int,
        harbour: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegisterBuoyResponse:
        """
        Parameters
        ----------
        survey_ref : str

        label : str

        depth_metres : int

        harbour : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterBuoyResponse
            Registered

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.buoys.register_buoy(
            survey_ref="X-Survey-Ref",
            label="label",
            depth_metres=1,
            harbour="harbour",
        )
        """
        _response = self._raw_client.register_buoy(
            survey_ref=survey_ref,
            label=label,
            depth_metres=depth_metres,
            harbour=harbour,
            request_options=request_options,
        )
        return _response.data

    def record_reading(
        self,
        buoy_id: str,
        *,
        berth: int,
        note: str,
        swell: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordReadingResponse:
        """
        Parameters
        ----------
        buoy_id : str

        berth : int

        note : str

        swell : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordReadingResponse
            Recorded

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.buoys.record_reading(
            buoy_id="buoyId",
            berth=1,
            note="",
            swell=0,
        )
        """
        _response = self._raw_client.record_reading(
            buoy_id, berth=berth, note=note, swell=swell, request_options=request_options
        )
        return _response.data


class AsyncBuoysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBuoysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBuoysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBuoysClient
        """
        return self._raw_client

    async def register_buoy(
        self,
        *,
        survey_ref: str,
        label: str,
        depth_metres: int,
        harbour: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegisterBuoyResponse:
        """
        Parameters
        ----------
        survey_ref : str

        label : str

        depth_metres : int

        harbour : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterBuoyResponse
            Registered

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.buoys.register_buoy(
                survey_ref="X-Survey-Ref",
                label="label",
                depth_metres=1,
                harbour="harbour",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_buoy(
            survey_ref=survey_ref,
            label=label,
            depth_metres=depth_metres,
            harbour=harbour,
            request_options=request_options,
        )
        return _response.data

    async def record_reading(
        self,
        buoy_id: str,
        *,
        berth: int,
        note: str,
        swell: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordReadingResponse:
        """
        Parameters
        ----------
        buoy_id : str

        berth : int

        note : str

        swell : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordReadingResponse
            Recorded

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.buoys.record_reading(
                buoy_id="buoyId",
                berth=1,
                note="",
                swell=0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_reading(
            buoy_id, berth=berth, note=note, swell=swell, request_options=request_options
        )
        return _response.data
