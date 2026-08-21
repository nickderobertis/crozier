

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMedicationClient, RawMedicationClient
from .types.get_medication_request_filter import GetMedicationRequestFilter
from .types.get_medication_response import GetMedicationResponse


class MedicationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMedicationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMedicationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMedicationClient
        """
        return self._raw_client

    def route_for_getting_filtered_medication_requests(
        self,
        *,
        filter: typing.Optional[GetMedicationRequestFilter] = None,
        value: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetMedicationResponse:
        """
        Parameters
        ----------
        filter : typing.Optional[GetMedicationRequestFilter]
            Pass the filter parameter you want to filter by

        value : typing.Optional[str]
            The value for the filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMedicationResponse
            Success response from medication API

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.medication.route_for_getting_filtered_medication_requests()
        """
        _response = self._raw_client.route_for_getting_filtered_medication_requests(
            filter=filter, value=value, request_options=request_options
        )
        return _response.data


class AsyncMedicationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMedicationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMedicationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMedicationClient
        """
        return self._raw_client

    async def route_for_getting_filtered_medication_requests(
        self,
        *,
        filter: typing.Optional[GetMedicationRequestFilter] = None,
        value: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetMedicationResponse:
        """
        Parameters
        ----------
        filter : typing.Optional[GetMedicationRequestFilter]
            Pass the filter parameter you want to filter by

        value : typing.Optional[str]
            The value for the filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMedicationResponse
            Success response from medication API

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.medication.route_for_getting_filtered_medication_requests()


        asyncio.run(main())
        """
        _response = await self._raw_client.route_for_getting_filtered_medication_requests(
            filter=filter, value=value, request_options=request_options
        )
        return _response.data
