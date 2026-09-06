

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.organisation_authority_domain_claim import OrganisationAuthorityDomainClaim
from ..types.organisation_authority_domain_claim_id import OrganisationAuthorityDomainClaimId
from ..types.organisation_authority_domain_claims_page import OrganisationAuthorityDomainClaimsPage
from ..types.organisation_id import OrganisationId
from .raw_client import AsyncRawOrganisationAuthorityDomainClaimsClient, RawOrganisationAuthorityDomainClaimsClient


class OrganisationAuthorityDomainClaimsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganisationAuthorityDomainClaimsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganisationAuthorityDomainClaimsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganisationAuthorityDomainClaimsClient
        """
        return self._raw_client

    def get_the_authority_domain_claims_for_the_given_organisation(
        self,
        organisation_id: OrganisationId,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganisationAuthorityDomainClaimsPage:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        page : typing.Optional[int]
            The page number to return of the result set

        size : typing.Optional[int]
            The size of the pages to return

        sort : typing.Optional[str]
            The field name to sort

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganisationAuthorityDomainClaimsPage
            All data of an organisation's authority domain claims

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )
        client.organisation_authority_domain_claims.get_the_authority_domain_claims_for_the_given_organisation(
            organisation_id="OrganisationId",
        )
        """
        _response = self._raw_client.get_the_authority_domain_claims_for_the_given_organisation(
            organisation_id, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    def get_an_authority_domain_claim_by_id(
        self,
        organisation_id: OrganisationId,
        organisation_authority_domain_claim_id: OrganisationAuthorityDomainClaimId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganisationAuthorityDomainClaim:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        organisation_authority_domain_claim_id : OrganisationAuthorityDomainClaimId
            Organisation Authority Domain Claim Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganisationAuthorityDomainClaim
            All authority to domain mappings data

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )
        client.organisation_authority_domain_claims.get_an_authority_domain_claim_by_id(
            organisation_id="OrganisationId",
            organisation_authority_domain_claim_id="OrganisationAuthorityDomainClaimId",
        )
        """
        _response = self._raw_client.get_an_authority_domain_claim_by_id(
            organisation_id, organisation_authority_domain_claim_id, request_options=request_options
        )
        return _response.data


class AsyncOrganisationAuthorityDomainClaimsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganisationAuthorityDomainClaimsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganisationAuthorityDomainClaimsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganisationAuthorityDomainClaimsClient
        """
        return self._raw_client

    async def get_the_authority_domain_claims_for_the_given_organisation(
        self,
        organisation_id: OrganisationId,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganisationAuthorityDomainClaimsPage:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        page : typing.Optional[int]
            The page number to return of the result set

        size : typing.Optional[int]
            The size of the pages to return

        sort : typing.Optional[str]
            The field name to sort

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganisationAuthorityDomainClaimsPage
            All data of an organisation's authority domain claims

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organisation_authority_domain_claims.get_the_authority_domain_claims_for_the_given_organisation(
                organisation_id="OrganisationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_the_authority_domain_claims_for_the_given_organisation(
            organisation_id, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    async def get_an_authority_domain_claim_by_id(
        self,
        organisation_id: OrganisationId,
        organisation_authority_domain_claim_id: OrganisationAuthorityDomainClaimId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganisationAuthorityDomainClaim:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        organisation_authority_domain_claim_id : OrganisationAuthorityDomainClaimId
            Organisation Authority Domain Claim Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganisationAuthorityDomainClaim
            All authority to domain mappings data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organisation_authority_domain_claims.get_an_authority_domain_claim_by_id(
                organisation_id="OrganisationId",
                organisation_authority_domain_claim_id="OrganisationAuthorityDomainClaimId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_an_authority_domain_claim_by_id(
            organisation_id, organisation_authority_domain_claim_id, request_options=request_options
        )
        return _response.data
