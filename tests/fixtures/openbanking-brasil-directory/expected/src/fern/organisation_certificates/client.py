

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.certificate_or_key import CertificateOrKey
from ..types.certificate_or_key_id import CertificateOrKeyId
from ..types.certificates_or_keys import CertificatesOrKeys
from ..types.organisation_certificate_type import OrganisationCertificateType
from ..types.organisation_id import OrganisationId
from .raw_client import AsyncRawOrganisationCertificatesClient, RawOrganisationCertificatesClient


class OrganisationCertificatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganisationCertificatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganisationCertificatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganisationCertificatesClient
        """
        return self._raw_client

    def get_the_certificates_for_the_given_organisation(
        self, organisation_id: OrganisationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CertificatesOrKeys:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

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
        client.organisation_certificates.get_the_certificates_for_the_given_organisation(
            organisation_id="OrganisationId",
        )
        """
        _response = self._raw_client.get_the_certificates_for_the_given_organisation(
            organisation_id, request_options=request_options
        )
        return _response.data

    def retrieve_a_certificate_with_the_given_certificate_or_key_id(
        self,
        organisation_id: OrganisationId,
        certificate_or_key_id: CertificateOrKeyId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CertificateOrKey:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

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
        from fern import FernApi

        client = FernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )
        client.organisation_certificates.retrieve_a_certificate_with_the_given_certificate_or_key_id(
            organisation_id="OrganisationId",
            certificate_or_key_id="CertificateOrKeyId",
        )
        """
        _response = self._raw_client.retrieve_a_certificate_with_the_given_certificate_or_key_id(
            organisation_id, certificate_or_key_id, request_options=request_options
        )
        return _response.data

    def get_the_certificates_of_the_given_organisation_certificate_type_for_the_given_organisation(
        self,
        organisation_id: OrganisationId,
        organisation_certificate_type: OrganisationCertificateType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CertificatesOrKeys:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        organisation_certificate_type : OrganisationCertificateType
            The certificate type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CertificatesOrKeys
            All certificates for the org

        Examples
        --------
        from fern import FernApi, OrganisationCertificateType

        client = FernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )
        client.organisation_certificates.get_the_certificates_of_the_given_organisation_certificate_type_for_the_given_organisation(
            organisation_id="OrganisationId",
            organisation_certificate_type=OrganisationCertificateType.QWAC,
        )
        """
        _response = (
            self._raw_client.get_the_certificates_of_the_given_organisation_certificate_type_for_the_given_organisation(
                organisation_id, organisation_certificate_type, request_options=request_options
            )
        )
        return _response.data


class AsyncOrganisationCertificatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganisationCertificatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganisationCertificatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganisationCertificatesClient
        """
        return self._raw_client

    async def get_the_certificates_for_the_given_organisation(
        self, organisation_id: OrganisationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CertificatesOrKeys:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

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
            await client.organisation_certificates.get_the_certificates_for_the_given_organisation(
                organisation_id="OrganisationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_the_certificates_for_the_given_organisation(
            organisation_id, request_options=request_options
        )
        return _response.data

    async def retrieve_a_certificate_with_the_given_certificate_or_key_id(
        self,
        organisation_id: OrganisationId,
        certificate_or_key_id: CertificateOrKeyId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CertificateOrKey:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

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

        from fern import AsyncFernApi

        client = AsyncFernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organisation_certificates.retrieve_a_certificate_with_the_given_certificate_or_key_id(
                organisation_id="OrganisationId",
                certificate_or_key_id="CertificateOrKeyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_certificate_with_the_given_certificate_or_key_id(
            organisation_id, certificate_or_key_id, request_options=request_options
        )
        return _response.data

    async def get_the_certificates_of_the_given_organisation_certificate_type_for_the_given_organisation(
        self,
        organisation_id: OrganisationId,
        organisation_certificate_type: OrganisationCertificateType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CertificatesOrKeys:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        organisation_certificate_type : OrganisationCertificateType
            The certificate type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CertificatesOrKeys
            All certificates for the org

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OrganisationCertificateType

        client = AsyncFernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organisation_certificates.get_the_certificates_of_the_given_organisation_certificate_type_for_the_given_organisation(
                organisation_id="OrganisationId",
                organisation_certificate_type=OrganisationCertificateType.QWAC,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_the_certificates_of_the_given_organisation_certificate_type_for_the_given_organisation(
            organisation_id, organisation_certificate_type, request_options=request_options
        )
        return _response.data
