

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.capability import Capability
from ..types.get_capability_grantees_endpoint_cursor_paged_result_of_output import (
    GetCapabilityGranteesEndpointCursorPagedResultOfOutput,
)
from ..types.get_customer_capabilities_endpoint_output import GetCustomerCapabilitiesEndpointOutput
from ..types.get_organization_capabilities_endpoint_output import GetOrganizationCapabilitiesEndpointOutput
from .raw_client import AsyncRawCapabilitiesClient, RawCapabilitiesClient


class CapabilitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCapabilitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCapabilitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCapabilitiesClient
        """
        return self._raw_client

    def lists_the_organizations_granted_a_capability_one_cursor_page_at_a_time(
        self,
        capability: Capability,
        *,
        cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCapabilityGranteesEndpointCursorPagedResultOfOutput:
        """
        Follow nextCursor to page.

        Parameters
        ----------
        capability : Capability
            The capability to inspect.

        cursor : typing.Optional[str]
            The opaque cursor from the previous page; omit for the first page.

        page_size : typing.Optional[int]
            The number of items per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCapabilityGranteesEndpointCursorPagedResultOfOutput
            OK

        Examples
        --------
        from fern import Capability, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.capabilities.lists_the_organizations_granted_a_capability_one_cursor_page_at_a_time(
            capability=Capability.SKIP_CONTENT_CHECK,
        )
        """
        _response = self._raw_client.lists_the_organizations_granted_a_capability_one_cursor_page_at_a_time(
            capability, cursor=cursor, page_size=page_size, request_options=request_options
        )
        return _response.data

    def lists_the_capabilities_a_customer_holds(
        self, customer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCustomerCapabilitiesEndpointOutput:
        """
        capabilities are granted to an organization, so these are the grants of the
         organization the customer is currently acting under — the same set enforced for them. A
         customer without an organization holds none.

        Parameters
        ----------
        customer_id : str
            The customer to inspect.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerCapabilitiesEndpointOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.capabilities.lists_the_capabilities_a_customer_holds(
            customer_id="customerId",
        )
        """
        _response = self._raw_client.lists_the_capabilities_a_customer_holds(
            customer_id, request_options=request_options
        )
        return _response.data

    def lists_the_capabilities_granted_to_an_organization(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetOrganizationCapabilitiesEndpointOutput:
        """
        Readable by the organization's own members, so a client can light up the product surfaces its
         grants entitle it to; platform staff read any organization.

        Parameters
        ----------
        organization_id : str
            The organization to inspect.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetOrganizationCapabilitiesEndpointOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.capabilities.lists_the_capabilities_granted_to_an_organization(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.lists_the_capabilities_granted_to_an_organization(
            organization_id, request_options=request_options
        )
        return _response.data

    def grants_a_capability_to_an_organization(
        self, organization_id: str, capability: Capability, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Idempotent: re-granting an existing grant is a no-op.

        Parameters
        ----------
        organization_id : str
            The organization to grant the capability to.

        capability : Capability
            The capability to grant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import Capability, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.capabilities.grants_a_capability_to_an_organization(
            organization_id="organizationId",
            capability=Capability.SKIP_CONTENT_CHECK,
        )
        """
        _response = self._raw_client.grants_a_capability_to_an_organization(
            organization_id, capability, request_options=request_options
        )
        return _response.data

    def revokes_an_organizations_capability_grant(
        self, organization_id: str, capability: Capability, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Idempotent: revoking a grant that does not exist is a no-op.

        Parameters
        ----------
        organization_id : str
            The organization to revoke the capability from.

        capability : Capability
            The capability to revoke.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import Capability, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.capabilities.revokes_an_organizations_capability_grant(
            organization_id="organizationId",
            capability=Capability.SKIP_CONTENT_CHECK,
        )
        """
        _response = self._raw_client.revokes_an_organizations_capability_grant(
            organization_id, capability, request_options=request_options
        )
        return _response.data


class AsyncCapabilitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCapabilitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCapabilitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCapabilitiesClient
        """
        return self._raw_client

    async def lists_the_organizations_granted_a_capability_one_cursor_page_at_a_time(
        self,
        capability: Capability,
        *,
        cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCapabilityGranteesEndpointCursorPagedResultOfOutput:
        """
        Follow nextCursor to page.

        Parameters
        ----------
        capability : Capability
            The capability to inspect.

        cursor : typing.Optional[str]
            The opaque cursor from the previous page; omit for the first page.

        page_size : typing.Optional[int]
            The number of items per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCapabilityGranteesEndpointCursorPagedResultOfOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Capability

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.capabilities.lists_the_organizations_granted_a_capability_one_cursor_page_at_a_time(
                capability=Capability.SKIP_CONTENT_CHECK,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.lists_the_organizations_granted_a_capability_one_cursor_page_at_a_time(
            capability, cursor=cursor, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def lists_the_capabilities_a_customer_holds(
        self, customer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCustomerCapabilitiesEndpointOutput:
        """
        capabilities are granted to an organization, so these are the grants of the
         organization the customer is currently acting under — the same set enforced for them. A
         customer without an organization holds none.

        Parameters
        ----------
        customer_id : str
            The customer to inspect.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomerCapabilitiesEndpointOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.capabilities.lists_the_capabilities_a_customer_holds(
                customer_id="customerId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.lists_the_capabilities_a_customer_holds(
            customer_id, request_options=request_options
        )
        return _response.data

    async def lists_the_capabilities_granted_to_an_organization(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetOrganizationCapabilitiesEndpointOutput:
        """
        Readable by the organization's own members, so a client can light up the product surfaces its
         grants entitle it to; platform staff read any organization.

        Parameters
        ----------
        organization_id : str
            The organization to inspect.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetOrganizationCapabilitiesEndpointOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.capabilities.lists_the_capabilities_granted_to_an_organization(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.lists_the_capabilities_granted_to_an_organization(
            organization_id, request_options=request_options
        )
        return _response.data

    async def grants_a_capability_to_an_organization(
        self, organization_id: str, capability: Capability, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Idempotent: re-granting an existing grant is a no-op.

        Parameters
        ----------
        organization_id : str
            The organization to grant the capability to.

        capability : Capability
            The capability to grant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Capability

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.capabilities.grants_a_capability_to_an_organization(
                organization_id="organizationId",
                capability=Capability.SKIP_CONTENT_CHECK,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.grants_a_capability_to_an_organization(
            organization_id, capability, request_options=request_options
        )
        return _response.data

    async def revokes_an_organizations_capability_grant(
        self, organization_id: str, capability: Capability, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Idempotent: revoking a grant that does not exist is a no-op.

        Parameters
        ----------
        organization_id : str
            The organization to revoke the capability from.

        capability : Capability
            The capability to revoke.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Capability

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.capabilities.revokes_an_organizations_capability_grant(
                organization_id="organizationId",
                capability=Capability.SKIP_CONTENT_CHECK,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revokes_an_organizations_capability_grant(
            organization_id, capability, request_options=request_options
        )
        return _response.data
