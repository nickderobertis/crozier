

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.organization_resource import OrganizationResource
from .raw_client import AsyncRawOrganizationlogoClient, RawOrganizationlogoClient


OMIT = typing.cast(typing.Any, ...)


class OrganizationlogoClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganizationlogoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganizationlogoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganizationlogoClient
        """
        return self._raw_client

    def show(self, organization: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Behind the bearer token like everything else here, because which organizations exist is not
        public. A browser cannot put a token on an `<img src>`, so a client fetches this and hands
        the response to the element as an object URL.

        Parameters
        ----------
        organization : str
            The organization ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.organizationlogo.show(
            organization="organization",
        )
        """
        _response = self._raw_client.show(organization, request_options=request_options)
        return _response.data

    def update(
        self, organization: str, *, logo: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganizationResource:
        """
        Parameters
        ----------
        organization : str
            The organization ID

        logo : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationResource
            `OrganizationResource`

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.organizationlogo.update(
            organization="organization",
        )
        """
        _response = self._raw_client.update(organization, logo=logo, request_options=request_options)
        return _response.data

    def destroy(self, organization: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        organization : str
            The organization ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.organizationlogo.destroy(
            organization="organization",
        )
        """
        _response = self._raw_client.destroy(organization, request_options=request_options)
        return _response.data


class AsyncOrganizationlogoClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganizationlogoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganizationlogoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganizationlogoClient
        """
        return self._raw_client

    async def show(self, organization: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Behind the bearer token like everything else here, because which organizations exist is not
        public. A browser cannot put a token on an `<img src>`, so a client fetches this and hands
        the response to the element as an object URL.

        Parameters
        ----------
        organization : str
            The organization ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.organizationlogo.show(
                organization="organization",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.show(organization, request_options=request_options)
        return _response.data

    async def update(
        self, organization: str, *, logo: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganizationResource:
        """
        Parameters
        ----------
        organization : str
            The organization ID

        logo : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationResource
            `OrganizationResource`

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.organizationlogo.update(
                organization="organization",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(organization, logo=logo, request_options=request_options)
        return _response.data

    async def destroy(self, organization: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        organization : str
            The organization ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.organizationlogo.destroy(
                organization="organization",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.destroy(organization, request_options=request_options)
        return _response.data
