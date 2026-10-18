

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.organization_project_claim_response_output import OrganizationProjectClaimResponseOutput
from ..types.organization_response_v1output import OrganizationResponseV1Output
from ..types.v1list_entitlements_response_output import V1ListEntitlementsResponseOutput
from ..types.v1organization_member_response_output import V1OrganizationMemberResponseOutput
from ..types.v1organization_slug_response_output import V1OrganizationSlugResponseOutput
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

    def v1list_all_organizations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OrganizationResponseV1Output]:
        """
        Returns a list of organizations that you currently belong to.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OrganizationResponseV1Output]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organizations.v1list_all_organizations()
        """
        _response = self._raw_client.v1list_all_organizations(request_options=request_options)
        return _response.data

    def v1create_an_organization(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganizationResponseV1Output:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationResponseV1Output


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organizations.v1create_an_organization(
            name="Acme",
        )
        """
        _response = self._raw_client.v1create_an_organization(name=name, request_options=request_options)
        return _response.data

    def v1get_organization_entitlements(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1ListEntitlementsResponseOutput:
        """
        Returns the entitlements available to the organization based on their plan and any overrides.

        Parameters
        ----------
        slug : str
            Organization slug

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1ListEntitlementsResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organizations.v1get_organization_entitlements(
            slug="tsrqponmlkjihgfedcba",
        )
        """
        _response = self._raw_client.v1get_organization_entitlements(slug, request_options=request_options)
        return _response.data

    def v1list_organization_members(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1OrganizationMemberResponseOutput]:
        """
        Parameters
        ----------
        slug : str
            Organization slug

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1OrganizationMemberResponseOutput]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organizations.v1list_organization_members(
            slug="tsrqponmlkjihgfedcba",
        )
        """
        _response = self._raw_client.v1list_organization_members(slug, request_options=request_options)
        return _response.data

    def v1get_an_organization(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1OrganizationSlugResponseOutput:
        """
        Parameters
        ----------
        slug : str
            Organization slug

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1OrganizationSlugResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organizations.v1get_an_organization(
            slug="tsrqponmlkjihgfedcba",
        )
        """
        _response = self._raw_client.v1get_an_organization(slug, request_options=request_options)
        return _response.data

    def v1get_organization_project_claim(
        self, slug: str, token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganizationProjectClaimResponseOutput:
        """
        Parameters
        ----------
        slug : str
            Organization slug

        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationProjectClaimResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organizations.v1get_organization_project_claim(
            slug="tsrqponmlkjihgfedcba",
            token="0123456789abcdef0123456789abcdef01234567",
        )
        """
        _response = self._raw_client.v1get_organization_project_claim(slug, token, request_options=request_options)
        return _response.data

    def v1claim_project_for_organization(
        self, slug: str, token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        slug : str
            Organization slug

        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organizations.v1claim_project_for_organization(
            slug="tsrqponmlkjihgfedcba",
            token="0123456789abcdef0123456789abcdef01234567",
        )
        """
        _response = self._raw_client.v1claim_project_for_organization(slug, token, request_options=request_options)
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

    async def v1list_all_organizations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OrganizationResponseV1Output]:
        """
        Returns a list of organizations that you currently belong to.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OrganizationResponseV1Output]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organizations.v1list_all_organizations()


        asyncio.run(main())
        """
        _response = await self._raw_client.v1list_all_organizations(request_options=request_options)
        return _response.data

    async def v1create_an_organization(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganizationResponseV1Output:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationResponseV1Output


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organizations.v1create_an_organization(
                name="Acme",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1create_an_organization(name=name, request_options=request_options)
        return _response.data

    async def v1get_organization_entitlements(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1ListEntitlementsResponseOutput:
        """
        Returns the entitlements available to the organization based on their plan and any overrides.

        Parameters
        ----------
        slug : str
            Organization slug

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1ListEntitlementsResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organizations.v1get_organization_entitlements(
                slug="tsrqponmlkjihgfedcba",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_organization_entitlements(slug, request_options=request_options)
        return _response.data

    async def v1list_organization_members(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1OrganizationMemberResponseOutput]:
        """
        Parameters
        ----------
        slug : str
            Organization slug

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1OrganizationMemberResponseOutput]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organizations.v1list_organization_members(
                slug="tsrqponmlkjihgfedcba",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1list_organization_members(slug, request_options=request_options)
        return _response.data

    async def v1get_an_organization(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1OrganizationSlugResponseOutput:
        """
        Parameters
        ----------
        slug : str
            Organization slug

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1OrganizationSlugResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organizations.v1get_an_organization(
                slug="tsrqponmlkjihgfedcba",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_an_organization(slug, request_options=request_options)
        return _response.data

    async def v1get_organization_project_claim(
        self, slug: str, token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganizationProjectClaimResponseOutput:
        """
        Parameters
        ----------
        slug : str
            Organization slug

        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationProjectClaimResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organizations.v1get_organization_project_claim(
                slug="tsrqponmlkjihgfedcba",
                token="0123456789abcdef0123456789abcdef01234567",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_organization_project_claim(
            slug, token, request_options=request_options
        )
        return _response.data

    async def v1claim_project_for_organization(
        self, slug: str, token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        slug : str
            Organization slug

        token : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organizations.v1claim_project_for_organization(
                slug="tsrqponmlkjihgfedcba",
                token="0123456789abcdef0123456789abcdef01234567",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1claim_project_for_organization(
            slug, token, request_options=request_options
        )
        return _response.data
