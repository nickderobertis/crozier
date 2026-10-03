

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.organization import Organization
from ..types.paged_result_of_organization import PagedResultOfOrganization
from ..types.sort_direction import SortDirection
from .raw_client import AsyncRawOrganizationsClient, RawOrganizationsClient


OMIT = typing.cast(typing.Any, ...)


class OrganizationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganizationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganizationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganizationsClient
        """
        return self._raw_client

    def getorganizations(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        search_term: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagedResultOfOrganization:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        page_size : typing.Optional[int]

        search_term : typing.Optional[str]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagedResultOfOrganization


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations.getorganizations()
        """
        _response = self._raw_client.getorganizations(
            page=page,
            page_size=page_size,
            search_term=search_term,
            sort_by=sort_by,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    def createorganization(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Organization:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        email : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations.createorganization()
        """
        _response = self._raw_client.createorganization(name=name, email=email, request_options=request_options)
        return _response.data


class AsyncOrganizationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganizationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganizationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganizationsClient
        """
        return self._raw_client

    async def getorganizations(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        search_term: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagedResultOfOrganization:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        page_size : typing.Optional[int]

        search_term : typing.Optional[str]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagedResultOfOrganization


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations.getorganizations()


        asyncio.run(main())
        """
        _response = await self._raw_client.getorganizations(
            page=page,
            page_size=page_size,
            search_term=search_term,
            sort_by=sort_by,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    async def createorganization(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Organization:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        email : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations.createorganization()


        asyncio.run(main())
        """
        _response = await self._raw_client.createorganization(name=name, email=email, request_options=request_options)
        return _response.data
