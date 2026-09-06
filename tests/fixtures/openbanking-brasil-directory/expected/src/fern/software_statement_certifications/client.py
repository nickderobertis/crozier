

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.organisation_id import OrganisationId
from ..types.software_statement_certification import SoftwareStatementCertification
from ..types.software_statement_certification_id import SoftwareStatementCertificationId
from ..types.software_statement_certifications import SoftwareStatementCertifications
from ..types.software_statement_id import SoftwareStatementId
from .raw_client import AsyncRawSoftwareStatementCertificationsClient, RawSoftwareStatementCertificationsClient


class SoftwareStatementCertificationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSoftwareStatementCertificationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSoftwareStatementCertificationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSoftwareStatementCertificationsClient
        """
        return self._raw_client

    def get_all_certifications_for_given_software_statement(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoftwareStatementCertifications:
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
        SoftwareStatementCertifications
            Software Statement certification for the given certification id

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
        client.software_statement_certifications.get_all_certifications_for_given_software_statement(
            organisation_id="OrganisationId",
            software_statement_id="SoftwareStatementId",
        )
        """
        _response = self._raw_client.get_all_certifications_for_given_software_statement(
            organisation_id, software_statement_id, request_options=request_options
        )
        return _response.data

    def get_a_certification_by_id(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        software_statement_certification_id: SoftwareStatementCertificationId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoftwareStatementCertification:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        software_statement_id : SoftwareStatementId
            The software statement ID

        software_statement_certification_id : SoftwareStatementCertificationId
            Software Statement certification Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoftwareStatementCertification
            Software Statement certification for the given certification id

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
        client.software_statement_certifications.get_a_certification_by_id(
            organisation_id="OrganisationId",
            software_statement_id="SoftwareStatementId",
            software_statement_certification_id="SoftwareStatementCertificationId",
        )
        """
        _response = self._raw_client.get_a_certification_by_id(
            organisation_id, software_statement_id, software_statement_certification_id, request_options=request_options
        )
        return _response.data


class AsyncSoftwareStatementCertificationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSoftwareStatementCertificationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSoftwareStatementCertificationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSoftwareStatementCertificationsClient
        """
        return self._raw_client

    async def get_all_certifications_for_given_software_statement(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoftwareStatementCertifications:
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
        SoftwareStatementCertifications
            Software Statement certification for the given certification id

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
            await client.software_statement_certifications.get_all_certifications_for_given_software_statement(
                organisation_id="OrganisationId",
                software_statement_id="SoftwareStatementId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_certifications_for_given_software_statement(
            organisation_id, software_statement_id, request_options=request_options
        )
        return _response.data

    async def get_a_certification_by_id(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        software_statement_certification_id: SoftwareStatementCertificationId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoftwareStatementCertification:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        software_statement_id : SoftwareStatementId
            The software statement ID

        software_statement_certification_id : SoftwareStatementCertificationId
            Software Statement certification Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoftwareStatementCertification
            Software Statement certification for the given certification id

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
            await client.software_statement_certifications.get_a_certification_by_id(
                organisation_id="OrganisationId",
                software_statement_id="SoftwareStatementId",
                software_statement_certification_id="SoftwareStatementCertificationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_certification_by_id(
            organisation_id, software_statement_id, software_statement_certification_id, request_options=request_options
        )
        return _response.data
