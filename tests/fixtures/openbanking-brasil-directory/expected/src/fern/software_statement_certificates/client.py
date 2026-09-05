

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.certificate_or_key import CertificateOrKey
from ..types.certificate_or_key_id import CertificateOrKeyId
from ..types.certificates_or_keys import CertificatesOrKeys
from ..types.organisation_id import OrganisationId
from ..types.software_statement_certificate_or_key_type import SoftwareStatementCertificateOrKeyType
from ..types.software_statement_id import SoftwareStatementId
from .raw_client import AsyncRawSoftwareStatementCertificatesClient, RawSoftwareStatementCertificatesClient
from .types.amend_certificate_request_revoke_reason import AmendCertificateRequestRevokeReason


OMIT = typing.cast(typing.Any, ...)


class SoftwareStatementCertificatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSoftwareStatementCertificatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSoftwareStatementCertificatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSoftwareStatementCertificatesClient
        """
        return self._raw_client

    def get_certificates_for_the_given_software_statement(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CertificatesOrKeys:
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
        CertificatesOrKeys
            All certificates for the org

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
        client.software_statement_certificates.get_certificates_for_the_given_software_statement(
            organisation_id="OrganisationId",
            software_statement_id="SoftwareStatementId",
        )
        """
        _response = self._raw_client.get_certificates_for_the_given_software_statement(
            organisation_id, software_statement_id, request_options=request_options
        )
        return _response.data

    def get_the_certificate_of_the_given_type_and_id_for_the_given_software_statement(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        software_statement_certificate_or_key_type: SoftwareStatementCertificateOrKeyType,
        certificate_or_key_id: CertificateOrKeyId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CertificateOrKey:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        software_statement_id : SoftwareStatementId
            The software statement ID

        software_statement_certificate_or_key_type : SoftwareStatementCertificateOrKeyType
            The certificate or key type that can be associated with a software statement

        certificate_or_key_id : CertificateOrKeyId
            The certificate or key Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CertificateOrKey
            A certificate object

        Examples
        --------
        from fern import FernApi, SoftwareStatementCertificateOrKeyType

        client = FernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )
        client.software_statement_certificates.get_the_certificate_of_the_given_type_and_id_for_the_given_software_statement(
            organisation_id="OrganisationId",
            software_statement_id="SoftwareStatementId",
            software_statement_certificate_or_key_type=SoftwareStatementCertificateOrKeyType.RTSTRANSPORT,
            certificate_or_key_id="CertificateOrKeyId",
        )
        """
        _response = self._raw_client.get_the_certificate_of_the_given_type_and_id_for_the_given_software_statement(
            organisation_id,
            software_statement_id,
            software_statement_certificate_or_key_type,
            certificate_or_key_id,
            request_options=request_options,
        )
        return _response.data

    def update_a_software_statement_certificate_with_the_given_certificate_or_key_id_eg_revoke_reason(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        software_statement_certificate_or_key_type: SoftwareStatementCertificateOrKeyType,
        certificate_or_key_id: CertificateOrKeyId,
        *,
        revoke_reason: AmendCertificateRequestRevokeReason,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        software_statement_id : SoftwareStatementId
            The software statement ID

        software_statement_certificate_or_key_type : SoftwareStatementCertificateOrKeyType
            The certificate or key type that can be associated with a software statement

        certificate_or_key_id : CertificateOrKeyId
            The certificate or key Id

        revoke_reason : AmendCertificateRequestRevokeReason
            Specify a reason for revokation of the certificate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.software_statement_certificates import (
            AmendCertificateRequestRevokeReason,
        )

        from fern import FernApi, SoftwareStatementCertificateOrKeyType

        client = FernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )
        client.software_statement_certificates.update_a_software_statement_certificate_with_the_given_certificate_or_key_id_eg_revoke_reason(
            organisation_id="OrganisationId",
            software_statement_id="SoftwareStatementId",
            software_statement_certificate_or_key_type=SoftwareStatementCertificateOrKeyType.RTSTRANSPORT,
            certificate_or_key_id="CertificateOrKeyId",
            revoke_reason=AmendCertificateRequestRevokeReason.UNSPECIFIED,
        )
        """
        _response = self._raw_client.update_a_software_statement_certificate_with_the_given_certificate_or_key_id_eg_revoke_reason(
            organisation_id,
            software_statement_id,
            software_statement_certificate_or_key_type,
            certificate_or_key_id,
            revoke_reason=revoke_reason,
            request_options=request_options,
        )
        return _response.data


class AsyncSoftwareStatementCertificatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSoftwareStatementCertificatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSoftwareStatementCertificatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSoftwareStatementCertificatesClient
        """
        return self._raw_client

    async def get_certificates_for_the_given_software_statement(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CertificatesOrKeys:
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
        CertificatesOrKeys
            All certificates for the org

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
            await client.software_statement_certificates.get_certificates_for_the_given_software_statement(
                organisation_id="OrganisationId",
                software_statement_id="SoftwareStatementId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_certificates_for_the_given_software_statement(
            organisation_id, software_statement_id, request_options=request_options
        )
        return _response.data

    async def get_the_certificate_of_the_given_type_and_id_for_the_given_software_statement(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        software_statement_certificate_or_key_type: SoftwareStatementCertificateOrKeyType,
        certificate_or_key_id: CertificateOrKeyId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CertificateOrKey:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        software_statement_id : SoftwareStatementId
            The software statement ID

        software_statement_certificate_or_key_type : SoftwareStatementCertificateOrKeyType
            The certificate or key type that can be associated with a software statement

        certificate_or_key_id : CertificateOrKeyId
            The certificate or key Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CertificateOrKey
            A certificate object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SoftwareStatementCertificateOrKeyType

        client = AsyncFernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.software_statement_certificates.get_the_certificate_of_the_given_type_and_id_for_the_given_software_statement(
                organisation_id="OrganisationId",
                software_statement_id="SoftwareStatementId",
                software_statement_certificate_or_key_type=SoftwareStatementCertificateOrKeyType.RTSTRANSPORT,
                certificate_or_key_id="CertificateOrKeyId",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.get_the_certificate_of_the_given_type_and_id_for_the_given_software_statement(
                organisation_id,
                software_statement_id,
                software_statement_certificate_or_key_type,
                certificate_or_key_id,
                request_options=request_options,
            )
        )
        return _response.data

    async def update_a_software_statement_certificate_with_the_given_certificate_or_key_id_eg_revoke_reason(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        software_statement_certificate_or_key_type: SoftwareStatementCertificateOrKeyType,
        certificate_or_key_id: CertificateOrKeyId,
        *,
        revoke_reason: AmendCertificateRequestRevokeReason,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        software_statement_id : SoftwareStatementId
            The software statement ID

        software_statement_certificate_or_key_type : SoftwareStatementCertificateOrKeyType
            The certificate or key type that can be associated with a software statement

        certificate_or_key_id : CertificateOrKeyId
            The certificate or key Id

        revoke_reason : AmendCertificateRequestRevokeReason
            Specify a reason for revokation of the certificate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.software_statement_certificates import (
            AmendCertificateRequestRevokeReason,
        )

        from fern import AsyncFernApi, SoftwareStatementCertificateOrKeyType

        client = AsyncFernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.software_statement_certificates.update_a_software_statement_certificate_with_the_given_certificate_or_key_id_eg_revoke_reason(
                organisation_id="OrganisationId",
                software_statement_id="SoftwareStatementId",
                software_statement_certificate_or_key_type=SoftwareStatementCertificateOrKeyType.RTSTRANSPORT,
                certificate_or_key_id="CertificateOrKeyId",
                revoke_reason=AmendCertificateRequestRevokeReason.UNSPECIFIED,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_a_software_statement_certificate_with_the_given_certificate_or_key_id_eg_revoke_reason(
            organisation_id,
            software_statement_id,
            software_statement_certificate_or_key_type,
            certificate_or_key_id,
            revoke_reason=revoke_reason,
            request_options=request_options,
        )
        return _response.data
