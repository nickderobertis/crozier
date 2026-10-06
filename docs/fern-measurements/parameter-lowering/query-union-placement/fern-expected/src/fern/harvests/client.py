

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_weighed_harvests_request_grade import ListWeighedHarvestsRequestGrade
from ..types.list_weighed_harvests_request_unit import ListWeighedHarvestsRequestUnit
from .raw_client import AsyncRawHarvestsClient, RawHarvestsClient
from .types.list_harvests_request_crate import ListHarvestsRequestCrate
from .types.list_harvests_request_ripeness import ListHarvestsRequestRipeness


class HarvestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHarvestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHarvestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHarvestsClient
        """
        return self._raw_client

    def list_harvests(
        self,
        *,
        ripeness: typing.Optional[ListHarvestsRequestRipeness] = None,
        crate: typing.Optional[ListHarvestsRequestCrate] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        ripeness : typing.Optional[ListHarvestsRequestRipeness]

        crate : typing.Optional[ListHarvestsRequestCrate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Harvests matching the filters.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.harvests.list_harvests()
        """
        _response = self._raw_client.list_harvests(ripeness=ripeness, crate=crate, request_options=request_options)
        return _response.data

    def list_weighed_harvests(
        self,
        *,
        unit: typing.Optional[ListWeighedHarvestsRequestUnit] = None,
        grade: typing.Optional[ListWeighedHarvestsRequestGrade] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        unit : typing.Optional[ListWeighedHarvestsRequestUnit]

        grade : typing.Optional[ListWeighedHarvestsRequestGrade]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Weighed harvests.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.harvests.list_weighed_harvests()
        """
        _response = self._raw_client.list_weighed_harvests(unit=unit, grade=grade, request_options=request_options)
        return _response.data


class AsyncHarvestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHarvestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHarvestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHarvestsClient
        """
        return self._raw_client

    async def list_harvests(
        self,
        *,
        ripeness: typing.Optional[ListHarvestsRequestRipeness] = None,
        crate: typing.Optional[ListHarvestsRequestCrate] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        ripeness : typing.Optional[ListHarvestsRequestRipeness]

        crate : typing.Optional[ListHarvestsRequestCrate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Harvests matching the filters.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.harvests.list_harvests()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_harvests(
            ripeness=ripeness, crate=crate, request_options=request_options
        )
        return _response.data

    async def list_weighed_harvests(
        self,
        *,
        unit: typing.Optional[ListWeighedHarvestsRequestUnit] = None,
        grade: typing.Optional[ListWeighedHarvestsRequestGrade] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        unit : typing.Optional[ListWeighedHarvestsRequestUnit]

        grade : typing.Optional[ListWeighedHarvestsRequestGrade]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Weighed harvests.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.harvests.list_weighed_harvests()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_weighed_harvests(
            unit=unit, grade=grade, request_options=request_options
        )
        return _response.data
