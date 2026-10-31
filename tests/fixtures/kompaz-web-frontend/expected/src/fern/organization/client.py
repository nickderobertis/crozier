

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.organization_resource import OrganizationResource
from .raw_client import AsyncRawOrganizationClient, RawOrganizationClient
from .types.organization_index_response import OrganizationIndexResponse


OMIT = typing.cast(typing.Any, ...)


class OrganizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganizationClient
        """
        return self._raw_client

    def index(
        self,
        *,
        search: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationIndexResponse:
        """
        Parameters
        ----------
        search : typing.Optional[str]

        page_number : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationIndexResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.organization.index()
        """
        _response = self._raw_client.index(
            search=search, page_number=page_number, page_size=page_size, request_options=request_options
        )
        return _response.data

    def store(self, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> OrganizationResource:
        """
        Parameters
        ----------
        name : str

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
        client.organization.store(
            name="name",
        )
        """
        _response = self._raw_client.store(name=name, request_options=request_options)
        return _response.data

    def show(
        self, organization: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganizationResource:
        """
        Parameters
        ----------
        organization : str
            The organization ID

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
        client.organization.show(
            organization="organization",
        )
        """
        _response = self._raw_client.show(organization, request_options=request_options)
        return _response.data

    def update(
        self, organization: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganizationResource:
        """
        Parameters
        ----------
        organization : str
            The organization ID

        name : str

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
        client.organization.update(
            organization="organization",
            name="name",
        )
        """
        _response = self._raw_client.update(organization, name=name, request_options=request_options)
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
        client.organization.destroy(
            organization="organization",
        )
        """
        _response = self._raw_client.destroy(organization, request_options=request_options)
        return _response.data


class AsyncOrganizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganizationClient
        """
        return self._raw_client

    async def index(
        self,
        *,
        search: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationIndexResponse:
        """
        Parameters
        ----------
        search : typing.Optional[str]

        page_number : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationIndexResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.organization.index()


        asyncio.run(main())
        """
        _response = await self._raw_client.index(
            search=search, page_number=page_number, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def store(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganizationResource:
        """
        Parameters
        ----------
        name : str

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
            await client.organization.store(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.store(name=name, request_options=request_options)
        return _response.data

    async def show(
        self, organization: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganizationResource:
        """
        Parameters
        ----------
        organization : str
            The organization ID

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
            await client.organization.show(
                organization="organization",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.show(organization, request_options=request_options)
        return _response.data

    async def update(
        self, organization: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganizationResource:
        """
        Parameters
        ----------
        organization : str
            The organization ID

        name : str

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
            await client.organization.update(
                organization="organization",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(organization, name=name, request_options=request_options)
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
            await client.organization.destroy(
                organization="organization",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.destroy(organization, request_options=request_options)
        return _response.data
