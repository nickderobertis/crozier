

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.harbor_berth_assignment import HarborBerthAssignment
from ..types.harbor_event import HarborEvent
from ..types.harbor_voyage import HarborVoyage
from .raw_client import AsyncRawHarborClient, RawHarborClient
from .types.create_mooring_permit_request_vessel import CreateMooringPermitRequestVessel


OMIT = typing.cast(typing.Any, ...)


class HarborClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHarborClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHarborClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHarborClient
        """
        return self._raw_client

    def create_berth_assignment(
        self,
        harbor_id: str,
        *,
        harbor_berth_assignment_create_harbor_id: str,
        vessel_name: str,
        stay_hours: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HarborBerthAssignment:
        """
        Parameters
        ----------
        harbor_id : str

        harbor_berth_assignment_create_harbor_id : str

        vessel_name : str

        stay_hours : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HarborBerthAssignment
            The created berth assignment.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.harbor.create_berth_assignment(
            harbor_id="harbor_id",
            harbor_berth_assignment_create_harbor_id="harbor_id",
            vessel_name="vessel_name",
        )
        """
        _response = self._raw_client.create_berth_assignment(
            harbor_id,
            harbor_berth_assignment_create_harbor_id=harbor_berth_assignment_create_harbor_id,
            vessel_name=vessel_name,
            stay_hours=stay_hours,
            request_options=request_options,
        )
        return _response.data

    def create_voyage(
        self,
        harbor_id: str,
        *,
        harbor_voyage_create_harbor_id: str,
        route: str,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HarborVoyage:
        """
        Parameters
        ----------
        harbor_id : str

        harbor_voyage_create_harbor_id : str

        route : str

        tags : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HarborVoyage
            The created voyage.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.harbor.create_voyage(
            harbor_id="harbor_id",
            harbor_voyage_create_harbor_id="harbor_id",
            route="route",
        )
        """
        _response = self._raw_client.create_voyage(
            harbor_id,
            harbor_voyage_create_harbor_id=harbor_voyage_create_harbor_id,
            route=route,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    def create_mooring_permit(
        self,
        harbor_id: str,
        *,
        mooring_permit_harbor_id: str,
        vessel: typing.Optional[CreateMooringPermitRequestVessel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HarborEvent:
        """
        Parameters
        ----------
        harbor_id : str

        mooring_permit_harbor_id : str

        vessel : typing.Optional[CreateMooringPermitRequestVessel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HarborEvent
            The created permit's events.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.harbor.create_mooring_permit(
            harbor_id="harbor_id",
            mooring_permit_harbor_id="harbor_id",
        )
        """
        _response = self._raw_client.create_mooring_permit(
            harbor_id, mooring_permit_harbor_id=mooring_permit_harbor_id, vessel=vessel, request_options=request_options
        )
        return _response.data

    def create_log_entry(
        self,
        harbor_id: str,
        *,
        log_entry_harbor_id: str,
        body: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        harbor_id : str

        log_entry_harbor_id : str

        body : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.harbor.create_log_entry(
            harbor_id="harbor_id",
            log_entry_harbor_id="harbor_id",
            body="body",
        )
        """
        _response = self._raw_client.create_log_entry(
            harbor_id, log_entry_harbor_id=log_entry_harbor_id, body=body, request_options=request_options
        )
        return _response.data


class AsyncHarborClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHarborClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHarborClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHarborClient
        """
        return self._raw_client

    async def create_berth_assignment(
        self,
        harbor_id: str,
        *,
        harbor_berth_assignment_create_harbor_id: str,
        vessel_name: str,
        stay_hours: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HarborBerthAssignment:
        """
        Parameters
        ----------
        harbor_id : str

        harbor_berth_assignment_create_harbor_id : str

        vessel_name : str

        stay_hours : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HarborBerthAssignment
            The created berth assignment.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.harbor.create_berth_assignment(
                harbor_id="harbor_id",
                harbor_berth_assignment_create_harbor_id="harbor_id",
                vessel_name="vessel_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_berth_assignment(
            harbor_id,
            harbor_berth_assignment_create_harbor_id=harbor_berth_assignment_create_harbor_id,
            vessel_name=vessel_name,
            stay_hours=stay_hours,
            request_options=request_options,
        )
        return _response.data

    async def create_voyage(
        self,
        harbor_id: str,
        *,
        harbor_voyage_create_harbor_id: str,
        route: str,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HarborVoyage:
        """
        Parameters
        ----------
        harbor_id : str

        harbor_voyage_create_harbor_id : str

        route : str

        tags : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HarborVoyage
            The created voyage.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.harbor.create_voyage(
                harbor_id="harbor_id",
                harbor_voyage_create_harbor_id="harbor_id",
                route="route",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_voyage(
            harbor_id,
            harbor_voyage_create_harbor_id=harbor_voyage_create_harbor_id,
            route=route,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    async def create_mooring_permit(
        self,
        harbor_id: str,
        *,
        mooring_permit_harbor_id: str,
        vessel: typing.Optional[CreateMooringPermitRequestVessel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HarborEvent:
        """
        Parameters
        ----------
        harbor_id : str

        mooring_permit_harbor_id : str

        vessel : typing.Optional[CreateMooringPermitRequestVessel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HarborEvent
            The created permit's events.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.harbor.create_mooring_permit(
                harbor_id="harbor_id",
                mooring_permit_harbor_id="harbor_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_mooring_permit(
            harbor_id, mooring_permit_harbor_id=mooring_permit_harbor_id, vessel=vessel, request_options=request_options
        )
        return _response.data

    async def create_log_entry(
        self,
        harbor_id: str,
        *,
        log_entry_harbor_id: str,
        body: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        harbor_id : str

        log_entry_harbor_id : str

        body : str

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.harbor.create_log_entry(
                harbor_id="harbor_id",
                log_entry_harbor_id="harbor_id",
                body="body",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_log_entry(
            harbor_id, log_entry_harbor_id=log_entry_harbor_id, body=body, request_options=request_options
        )
        return _response.data
