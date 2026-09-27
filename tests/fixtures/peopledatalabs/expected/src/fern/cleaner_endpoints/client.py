

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.company import Company
from ..types.location import Location
from ..types.school import School
from .raw_client import AsyncRawCleanerEndpointsClient, RawCleanerEndpointsClient


OMIT = typing.cast(typing.Any, ...)


class CleanerEndpointsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCleanerEndpointsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCleanerEndpointsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCleanerEndpointsClient
        """
        return self._raw_client

    def company_clean(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        website: typing.Optional[str] = OMIT,
        profile: typing.Optional[str] = OMIT,
        pretty: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Company:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            The name of the company

        website : typing.Optional[str]
            A website the company uses

        profile : typing.Optional[str]
            A social profile used by the company (e.g. LinkedIn/Facebook/Twitter)

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Company
            Company Found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.cleaner_endpoints.company_clean()
        """
        _response = self._raw_client.company_clean(
            name=name, website=website, profile=profile, pretty=pretty, request_options=request_options
        )
        return _response.data

    def school_clean(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        website: typing.Optional[str] = OMIT,
        profile: typing.Optional[str] = OMIT,
        pretty: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> School:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            The name of the school

        website : typing.Optional[str]
            A website the school uses

        profile : typing.Optional[str]
            A social profile used by the school (e.g. LinkedIn/Facebook/Twitter)

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        School
            School Found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.cleaner_endpoints.school_clean()
        """
        _response = self._raw_client.school_clean(
            name=name, website=website, profile=profile, pretty=pretty, request_options=request_options
        )
        return _response.data

    def location_clean(
        self,
        *,
        location: typing.Optional[str] = OMIT,
        pretty: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Location:
        """
        Parameters
        ----------
        location : typing.Optional[str]
            The raw location to process

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Location
            Location Found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.cleaner_endpoints.location_clean()
        """
        _response = self._raw_client.location_clean(location=location, pretty=pretty, request_options=request_options)
        return _response.data


class AsyncCleanerEndpointsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCleanerEndpointsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCleanerEndpointsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCleanerEndpointsClient
        """
        return self._raw_client

    async def company_clean(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        website: typing.Optional[str] = OMIT,
        profile: typing.Optional[str] = OMIT,
        pretty: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Company:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            The name of the company

        website : typing.Optional[str]
            A website the company uses

        profile : typing.Optional[str]
            A social profile used by the company (e.g. LinkedIn/Facebook/Twitter)

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Company
            Company Found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.cleaner_endpoints.company_clean()


        asyncio.run(main())
        """
        _response = await self._raw_client.company_clean(
            name=name, website=website, profile=profile, pretty=pretty, request_options=request_options
        )
        return _response.data

    async def school_clean(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        website: typing.Optional[str] = OMIT,
        profile: typing.Optional[str] = OMIT,
        pretty: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> School:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            The name of the school

        website : typing.Optional[str]
            A website the school uses

        profile : typing.Optional[str]
            A social profile used by the school (e.g. LinkedIn/Facebook/Twitter)

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        School
            School Found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.cleaner_endpoints.school_clean()


        asyncio.run(main())
        """
        _response = await self._raw_client.school_clean(
            name=name, website=website, profile=profile, pretty=pretty, request_options=request_options
        )
        return _response.data

    async def location_clean(
        self,
        *,
        location: typing.Optional[str] = OMIT,
        pretty: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Location:
        """
        Parameters
        ----------
        location : typing.Optional[str]
            The raw location to process

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Location
            Location Found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.cleaner_endpoints.location_clean()


        asyncio.run(main())
        """
        _response = await self._raw_client.location_clean(
            location=location, pretty=pretty, request_options=request_options
        )
        return _response.data
