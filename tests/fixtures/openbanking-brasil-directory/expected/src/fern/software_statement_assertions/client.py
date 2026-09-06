

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.organisation_id import OrganisationId
from ..types.software_statement_assertion import SoftwareStatementAssertion
from ..types.software_statement_id import SoftwareStatementId
from .raw_client import AsyncRawSoftwareStatementAssertionsClient, RawSoftwareStatementAssertionsClient


class SoftwareStatementAssertionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSoftwareStatementAssertionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSoftwareStatementAssertionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSoftwareStatementAssertionsClient
        """
        return self._raw_client

    def get_a_software_statement_assertion_for_the_given_software_statement_id(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoftwareStatementAssertion:
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
        SoftwareStatementAssertion
            OK

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
        client.software_statement_assertions.get_a_software_statement_assertion_for_the_given_software_statement_id(
            organisation_id="OrganisationId",
            software_statement_id="SoftwareStatementId",
        )
        """
        _response = self._raw_client.get_a_software_statement_assertion_for_the_given_software_statement_id(
            organisation_id, software_statement_id, request_options=request_options
        )
        return _response.data


class AsyncSoftwareStatementAssertionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSoftwareStatementAssertionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSoftwareStatementAssertionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSoftwareStatementAssertionsClient
        """
        return self._raw_client

    async def get_a_software_statement_assertion_for_the_given_software_statement_id(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoftwareStatementAssertion:
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
        SoftwareStatementAssertion
            OK

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
            await client.software_statement_assertions.get_a_software_statement_assertion_for_the_given_software_statement_id(
                organisation_id="OrganisationId",
                software_statement_id="SoftwareStatementId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_software_statement_assertion_for_the_given_software_statement_id(
            organisation_id, software_statement_id, request_options=request_options
        )
        return _response.data
