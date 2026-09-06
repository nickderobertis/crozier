

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.organisation_authority_claim import OrganisationAuthorityClaim
from ..types.organisation_authority_claim_id import OrganisationAuthorityClaimId
from ..types.organisation_authority_claims import OrganisationAuthorityClaims
from ..types.organisation_id import OrganisationId
from .raw_client import AsyncRawOrganisationAuthorityClaimsClient, RawOrganisationAuthorityClaimsClient


class OrganisationAuthorityClaimsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganisationAuthorityClaimsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganisationAuthorityClaimsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganisationAuthorityClaimsClient
        """
        return self._raw_client

    def get_the_authority_claims_for_the_given_organisation(
        self, organisation_id: OrganisationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganisationAuthorityClaims:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganisationAuthorityClaims
            All authority claims for the organisation

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
        client.organisation_authority_claims.get_the_authority_claims_for_the_given_organisation(
            organisation_id="OrganisationId",
        )
        """
        _response = self._raw_client.get_the_authority_claims_for_the_given_organisation(
            organisation_id, request_options=request_options
        )
        return _response.data

    def get_an_authority_claim_by_id(
        self,
        organisation_id: OrganisationId,
        organisation_authority_claim_id: OrganisationAuthorityClaimId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganisationAuthorityClaim:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        organisation_authority_claim_id : OrganisationAuthorityClaimId
            The Authority claims ID for an organisation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganisationAuthorityClaim
            Authority claim for the given Id

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
        client.organisation_authority_claims.get_an_authority_claim_by_id(
            organisation_id="OrganisationId",
            organisation_authority_claim_id="OrganisationAuthorityClaimId",
        )
        """
        _response = self._raw_client.get_an_authority_claim_by_id(
            organisation_id, organisation_authority_claim_id, request_options=request_options
        )
        return _response.data


class AsyncOrganisationAuthorityClaimsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganisationAuthorityClaimsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganisationAuthorityClaimsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganisationAuthorityClaimsClient
        """
        return self._raw_client

    async def get_the_authority_claims_for_the_given_organisation(
        self, organisation_id: OrganisationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganisationAuthorityClaims:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganisationAuthorityClaims
            All authority claims for the organisation

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
            await client.organisation_authority_claims.get_the_authority_claims_for_the_given_organisation(
                organisation_id="OrganisationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_the_authority_claims_for_the_given_organisation(
            organisation_id, request_options=request_options
        )
        return _response.data

    async def get_an_authority_claim_by_id(
        self,
        organisation_id: OrganisationId,
        organisation_authority_claim_id: OrganisationAuthorityClaimId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganisationAuthorityClaim:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        organisation_authority_claim_id : OrganisationAuthorityClaimId
            The Authority claims ID for an organisation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganisationAuthorityClaim
            Authority claim for the given Id

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
            await client.organisation_authority_claims.get_an_authority_claim_by_id(
                organisation_id="OrganisationId",
                organisation_authority_claim_id="OrganisationAuthorityClaimId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_an_authority_claim_by_id(
            organisation_id, organisation_authority_claim_id, request_options=request_options
        )
        return _response.data
