

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.authorisation_server_certification import AuthorisationServerCertification
from ..types.authorisation_server_certification_id import AuthorisationServerCertificationId
from ..types.authorisation_server_certifications import AuthorisationServerCertifications
from ..types.authorisation_server_id import AuthorisationServerId
from ..types.organisation_id import OrganisationId
from .raw_client import AsyncRawAuthorisationServerCertificationsClient, RawAuthorisationServerCertificationsClient


class AuthorisationServerCertificationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthorisationServerCertificationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthorisationServerCertificationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthorisationServerCertificationsClient
        """
        return self._raw_client

    def get_all_certifications_for_given_authorisation_server(
        self,
        organisation_id: OrganisationId,
        authorisation_server_id: AuthorisationServerId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationServerCertifications:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        authorisation_server_id : AuthorisationServerId
            The authorisation server Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorisationServerCertifications
            Authorisation Server certification for the given certification id

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
        client.authorisation_server_certifications.get_all_certifications_for_given_authorisation_server(
            organisation_id="OrganisationId",
            authorisation_server_id="AuthorisationServerId",
        )
        """
        _response = self._raw_client.get_all_certifications_for_given_authorisation_server(
            organisation_id, authorisation_server_id, request_options=request_options
        )
        return _response.data

    def get_a_certification_by_id(
        self,
        organisation_id: OrganisationId,
        authorisation_server_id: AuthorisationServerId,
        authorisation_server_certification_id: AuthorisationServerCertificationId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationServerCertification:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        authorisation_server_id : AuthorisationServerId
            The authorisation server Id

        authorisation_server_certification_id : AuthorisationServerCertificationId
            Auth server certification Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorisationServerCertification
            Authorisation Server certification for the given certification id

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
        client.authorisation_server_certifications.get_a_certification_by_id(
            organisation_id="OrganisationId",
            authorisation_server_id="AuthorisationServerId",
            authorisation_server_certification_id="AuthorisationServerCertificationId",
        )
        """
        _response = self._raw_client.get_a_certification_by_id(
            organisation_id,
            authorisation_server_id,
            authorisation_server_certification_id,
            request_options=request_options,
        )
        return _response.data


class AsyncAuthorisationServerCertificationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthorisationServerCertificationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthorisationServerCertificationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthorisationServerCertificationsClient
        """
        return self._raw_client

    async def get_all_certifications_for_given_authorisation_server(
        self,
        organisation_id: OrganisationId,
        authorisation_server_id: AuthorisationServerId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationServerCertifications:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        authorisation_server_id : AuthorisationServerId
            The authorisation server Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorisationServerCertifications
            Authorisation Server certification for the given certification id

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
            await client.authorisation_server_certifications.get_all_certifications_for_given_authorisation_server(
                organisation_id="OrganisationId",
                authorisation_server_id="AuthorisationServerId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_certifications_for_given_authorisation_server(
            organisation_id, authorisation_server_id, request_options=request_options
        )
        return _response.data

    async def get_a_certification_by_id(
        self,
        organisation_id: OrganisationId,
        authorisation_server_id: AuthorisationServerId,
        authorisation_server_certification_id: AuthorisationServerCertificationId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationServerCertification:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        authorisation_server_id : AuthorisationServerId
            The authorisation server Id

        authorisation_server_certification_id : AuthorisationServerCertificationId
            Auth server certification Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorisationServerCertification
            Authorisation Server certification for the given certification id

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
            await client.authorisation_server_certifications.get_a_certification_by_id(
                organisation_id="OrganisationId",
                authorisation_server_id="AuthorisationServerId",
                authorisation_server_certification_id="AuthorisationServerCertificationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_certification_by_id(
            organisation_id,
            authorisation_server_id,
            authorisation_server_certification_id,
            request_options=request_options,
        )
        return _response.data
