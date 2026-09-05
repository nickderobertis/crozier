

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.organisation_authorisation_id import OrganisationAuthorisationId
from ..types.organisation_authority_claim_authorisation import OrganisationAuthorityClaimAuthorisation
from ..types.organisation_authority_claim_authorisations import OrganisationAuthorityClaimAuthorisations
from ..types.organisation_authority_claim_id import OrganisationAuthorityClaimId
from ..types.organisation_id import OrganisationId
from .raw_client import (
    AsyncRawOrganisationAuthorityClaimsAuthorisationsClient,
    RawOrganisationAuthorityClaimsAuthorisationsClient,
)


class OrganisationAuthorityClaimsAuthorisationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganisationAuthorityClaimsAuthorisationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganisationAuthorityClaimsAuthorisationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganisationAuthorityClaimsAuthorisationsClient
        """
        return self._raw_client

    def get_an_authority_claims_authorisations(
        self,
        organisation_id: OrganisationId,
        organisation_authority_claim_id: OrganisationAuthorityClaimId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganisationAuthorityClaimAuthorisations:
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
        OrganisationAuthorityClaimAuthorisations
            Authorisations response

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
        client.organisation_authority_claims_authorisations.get_an_authority_claims_authorisations(
            organisation_id="OrganisationId",
            organisation_authority_claim_id="OrganisationAuthorityClaimId",
        )
        """
        _response = self._raw_client.get_an_authority_claims_authorisations(
            organisation_id, organisation_authority_claim_id, request_options=request_options
        )
        return _response.data

    def get_a_claim_authorisation(
        self,
        organisation_id: OrganisationId,
        organisation_authority_claim_id: OrganisationAuthorityClaimId,
        organisation_authorisation_id: OrganisationAuthorisationId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganisationAuthorityClaimAuthorisation:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        organisation_authority_claim_id : OrganisationAuthorityClaimId
            The Authority claims ID for an organisation

        organisation_authorisation_id : OrganisationAuthorisationId
            The authorisation ID for an organisation's authority claims

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganisationAuthorityClaimAuthorisation
            Authorisations response

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
        client.organisation_authority_claims_authorisations.get_a_claim_authorisation(
            organisation_id="OrganisationId",
            organisation_authority_claim_id="OrganisationAuthorityClaimId",
            organisation_authorisation_id="OrganisationAuthorisationId",
        )
        """
        _response = self._raw_client.get_a_claim_authorisation(
            organisation_id,
            organisation_authority_claim_id,
            organisation_authorisation_id,
            request_options=request_options,
        )
        return _response.data


class AsyncOrganisationAuthorityClaimsAuthorisationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganisationAuthorityClaimsAuthorisationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganisationAuthorityClaimsAuthorisationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganisationAuthorityClaimsAuthorisationsClient
        """
        return self._raw_client

    async def get_an_authority_claims_authorisations(
        self,
        organisation_id: OrganisationId,
        organisation_authority_claim_id: OrganisationAuthorityClaimId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganisationAuthorityClaimAuthorisations:
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
        OrganisationAuthorityClaimAuthorisations
            Authorisations response

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
            await client.organisation_authority_claims_authorisations.get_an_authority_claims_authorisations(
                organisation_id="OrganisationId",
                organisation_authority_claim_id="OrganisationAuthorityClaimId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_an_authority_claims_authorisations(
            organisation_id, organisation_authority_claim_id, request_options=request_options
        )
        return _response.data

    async def get_a_claim_authorisation(
        self,
        organisation_id: OrganisationId,
        organisation_authority_claim_id: OrganisationAuthorityClaimId,
        organisation_authorisation_id: OrganisationAuthorisationId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganisationAuthorityClaimAuthorisation:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        organisation_authority_claim_id : OrganisationAuthorityClaimId
            The Authority claims ID for an organisation

        organisation_authorisation_id : OrganisationAuthorisationId
            The authorisation ID for an organisation's authority claims

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganisationAuthorityClaimAuthorisation
            Authorisations response

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
            await client.organisation_authority_claims_authorisations.get_a_claim_authorisation(
                organisation_id="OrganisationId",
                organisation_authority_claim_id="OrganisationAuthorityClaimId",
                organisation_authorisation_id="OrganisationAuthorisationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_claim_authorisation(
            organisation_id,
            organisation_authority_claim_id,
            organisation_authorisation_id,
            request_options=request_options,
        )
        return _response.data
