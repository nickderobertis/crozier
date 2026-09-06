

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.organisation_id import OrganisationId
from ..types.software_authority_claim import SoftwareAuthorityClaim
from ..types.software_authority_claim_id import SoftwareAuthorityClaimId
from ..types.software_authority_claims import SoftwareAuthorityClaims
from ..types.software_statement_id import SoftwareStatementId
from .raw_client import AsyncRawSoftwareStatementAuthorityClaimsClient, RawSoftwareStatementAuthorityClaimsClient


class SoftwareStatementAuthorityClaimsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSoftwareStatementAuthorityClaimsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSoftwareStatementAuthorityClaimsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSoftwareStatementAuthorityClaimsClient
        """
        return self._raw_client

    def get_the_authority_claims_for_the_given_software_statement(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoftwareAuthorityClaims:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        software_statement_id : SoftwareStatementId
            The software statement ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoftwareAuthorityClaims
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
        client.software_statement_authority_claims.get_the_authority_claims_for_the_given_software_statement(
            organisation_id="OrganisationId",
            software_statement_id="SoftwareStatementId",
        )
        """
        _response = self._raw_client.get_the_authority_claims_for_the_given_software_statement(
            organisation_id, software_statement_id, request_options=request_options
        )
        return _response.data

    def get_an_authority_claim_by_id(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        software_authority_claim_id: SoftwareAuthorityClaimId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoftwareAuthorityClaim:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        software_statement_id : SoftwareStatementId
            The software statement ID

        software_authority_claim_id : SoftwareAuthorityClaimId
            The software statement's authority claim ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoftwareAuthorityClaim
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
        client.software_statement_authority_claims.get_an_authority_claim_by_id(
            organisation_id="OrganisationId",
            software_statement_id="SoftwareStatementId",
            software_authority_claim_id="SoftwareAuthorityClaimId",
        )
        """
        _response = self._raw_client.get_an_authority_claim_by_id(
            organisation_id, software_statement_id, software_authority_claim_id, request_options=request_options
        )
        return _response.data


class AsyncSoftwareStatementAuthorityClaimsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSoftwareStatementAuthorityClaimsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSoftwareStatementAuthorityClaimsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSoftwareStatementAuthorityClaimsClient
        """
        return self._raw_client

    async def get_the_authority_claims_for_the_given_software_statement(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoftwareAuthorityClaims:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        software_statement_id : SoftwareStatementId
            The software statement ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoftwareAuthorityClaims
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
            await client.software_statement_authority_claims.get_the_authority_claims_for_the_given_software_statement(
                organisation_id="OrganisationId",
                software_statement_id="SoftwareStatementId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_the_authority_claims_for_the_given_software_statement(
            organisation_id, software_statement_id, request_options=request_options
        )
        return _response.data

    async def get_an_authority_claim_by_id(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        software_authority_claim_id: SoftwareAuthorityClaimId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoftwareAuthorityClaim:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        software_statement_id : SoftwareStatementId
            The software statement ID

        software_authority_claim_id : SoftwareAuthorityClaimId
            The software statement's authority claim ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoftwareAuthorityClaim
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
            await client.software_statement_authority_claims.get_an_authority_claim_by_id(
                organisation_id="OrganisationId",
                software_statement_id="SoftwareStatementId",
                software_authority_claim_id="SoftwareAuthorityClaimId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_an_authority_claim_by_id(
            organisation_id, software_statement_id, software_authority_claim_id, request_options=request_options
        )
        return _response.data
