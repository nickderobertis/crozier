

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .authorisation_server_certifications.client import (
        AsyncAuthorisationServerCertificationsClient,
        AuthorisationServerCertificationsClient,
    )
    from .authorisation_servers.client import AsyncAuthorisationServersClient, AuthorisationServersClient
    from .authorisation_servers_api_discovery_endpoints.client import (
        AsyncAuthorisationServersApiDiscoveryEndpointsClient,
        AuthorisationServersApiDiscoveryEndpointsClient,
    )
    from .authorisation_servers_api_resources.client import (
        AsyncAuthorisationServersApiResourcesClient,
        AuthorisationServersApiResourcesClient,
    )
    from .contacts.client import AsyncContactsClient, ContactsClient
    from .organisation_authority_claims.client import (
        AsyncOrganisationAuthorityClaimsClient,
        OrganisationAuthorityClaimsClient,
    )
    from .organisation_authority_claims_authorisations.client import (
        AsyncOrganisationAuthorityClaimsAuthorisationsClient,
        OrganisationAuthorityClaimsAuthorisationsClient,
    )
    from .organisation_authority_domain_claims.client import (
        AsyncOrganisationAuthorityDomainClaimsClient,
        OrganisationAuthorityDomainClaimsClient,
    )
    from .organisation_certificates.client import AsyncOrganisationCertificatesClient, OrganisationCertificatesClient
    from .organisation_domain_users.client import AsyncOrganisationDomainUsersClient, OrganisationDomainUsersClient
    from .organisations.client import AsyncOrganisationsClient, OrganisationsClient
    from .references_authorisation_domain.client import (
        AsyncReferencesAuthorisationDomainClient,
        ReferencesAuthorisationDomainClient,
    )
    from .references_authorisation_domain_role.client import (
        AsyncReferencesAuthorisationDomainRoleClient,
        ReferencesAuthorisationDomainRoleClient,
    )
    from .references_authorisation_domain_role_metadata.client import (
        AsyncReferencesAuthorisationDomainRoleMetadataClient,
        ReferencesAuthorisationDomainRoleMetadataClient,
    )
    from .references_authority.client import AsyncReferencesAuthorityClient, ReferencesAuthorityClient
    from .references_authority_authorisation_domain.client import (
        AsyncReferencesAuthorityAuthorisationDomainClient,
        ReferencesAuthorityAuthorisationDomainClient,
    )
    from .references_terms_and_conditions.client import (
        AsyncReferencesTermsAndConditionsClient,
        ReferencesTermsAndConditionsClient,
    )
    from .software_statement_assertions.client import (
        AsyncSoftwareStatementAssertionsClient,
        SoftwareStatementAssertionsClient,
    )
    from .software_statement_authority_claims.client import (
        AsyncSoftwareStatementAuthorityClaimsClient,
        SoftwareStatementAuthorityClaimsClient,
    )
    from .software_statement_certificates.client import (
        AsyncSoftwareStatementCertificatesClient,
        SoftwareStatementCertificatesClient,
    )
    from .software_statement_certifications.client import (
        AsyncSoftwareStatementCertificationsClient,
        SoftwareStatementCertificationsClient,
    )
    from .software_statement_metadata.client import (
        AsyncSoftwareStatementMetadataClient,
        SoftwareStatementMetadataClient,
    )
    from .software_statements_for_an_organisation.client import (
        AsyncSoftwareStatementsForAnOrganisationClient,
        SoftwareStatementsForAnOrganisationClient,
    )


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    fapi_auth_date : typing.Optional[str]
    fapi_customer_ip_address : typing.Optional[str]
    fapi_interaction_id : typing.Optional[str]
    customer_user_agent : typing.Optional[str]
    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

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
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        fapi_auth_date: typing.Optional[str] = None,
        fapi_customer_ip_address: typing.Optional[str] = None,
        fapi_interaction_id: typing.Optional[str] = None,
        customer_user_agent: typing.Optional[str] = None,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            fapi_auth_date=fapi_auth_date,
            fapi_customer_ip_address=fapi_customer_ip_address,
            fapi_interaction_id=fapi_interaction_id,
            customer_user_agent=customer_user_agent,
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._organisations: typing.Optional[OrganisationsClient] = None
        self._authorisation_servers: typing.Optional[AuthorisationServersClient] = None
        self._authorisation_servers_api_resources: typing.Optional[AuthorisationServersApiResourcesClient] = None
        self._authorisation_servers_api_discovery_endpoints: typing.Optional[
            AuthorisationServersApiDiscoveryEndpointsClient
        ] = None
        self._authorisation_server_certifications: typing.Optional[AuthorisationServerCertificationsClient] = None
        self._organisation_authority_claims: typing.Optional[OrganisationAuthorityClaimsClient] = None
        self._organisation_authority_claims_authorisations: typing.Optional[
            OrganisationAuthorityClaimsAuthorisationsClient
        ] = None
        self._organisation_authority_domain_claims: typing.Optional[OrganisationAuthorityDomainClaimsClient] = None
        self._organisation_certificates: typing.Optional[OrganisationCertificatesClient] = None
        self._contacts: typing.Optional[ContactsClient] = None
        self._software_statements_for_an_organisation: typing.Optional[SoftwareStatementsForAnOrganisationClient] = None
        self._software_statement_assertions: typing.Optional[SoftwareStatementAssertionsClient] = None
        self._software_statement_authority_claims: typing.Optional[SoftwareStatementAuthorityClaimsClient] = None
        self._software_statement_certificates: typing.Optional[SoftwareStatementCertificatesClient] = None
        self._software_statement_certifications: typing.Optional[SoftwareStatementCertificationsClient] = None
        self._software_statement_metadata: typing.Optional[SoftwareStatementMetadataClient] = None
        self._organisation_domain_users: typing.Optional[OrganisationDomainUsersClient] = None
        self._references_authorisation_domain_role: typing.Optional[ReferencesAuthorisationDomainRoleClient] = None
        self._references_authorisation_domain_role_metadata: typing.Optional[
            ReferencesAuthorisationDomainRoleMetadataClient
        ] = None
        self._references_authorisation_domain: typing.Optional[ReferencesAuthorisationDomainClient] = None
        self._references_authority: typing.Optional[ReferencesAuthorityClient] = None
        self._references_authority_authorisation_domain: typing.Optional[
            ReferencesAuthorityAuthorisationDomainClient
        ] = None
        self._references_terms_and_conditions: typing.Optional[ReferencesTermsAndConditionsClient] = None

    @property
    def organisations(self):
        if self._organisations is None:
            from .organisations.client import OrganisationsClient

            self._organisations = OrganisationsClient(client_wrapper=self._client_wrapper)
        return self._organisations

    @property
    def authorisation_servers(self):
        if self._authorisation_servers is None:
            from .authorisation_servers.client import AuthorisationServersClient

            self._authorisation_servers = AuthorisationServersClient(client_wrapper=self._client_wrapper)
        return self._authorisation_servers

    @property
    def authorisation_servers_api_resources(self):
        if self._authorisation_servers_api_resources is None:
            from .authorisation_servers_api_resources.client import AuthorisationServersApiResourcesClient

            self._authorisation_servers_api_resources = AuthorisationServersApiResourcesClient(
                client_wrapper=self._client_wrapper
            )
        return self._authorisation_servers_api_resources

    @property
    def authorisation_servers_api_discovery_endpoints(self):
        if self._authorisation_servers_api_discovery_endpoints is None:
            from .authorisation_servers_api_discovery_endpoints.client import (
                AuthorisationServersApiDiscoveryEndpointsClient,
            )

            self._authorisation_servers_api_discovery_endpoints = AuthorisationServersApiDiscoveryEndpointsClient(
                client_wrapper=self._client_wrapper
            )
        return self._authorisation_servers_api_discovery_endpoints

    @property
    def authorisation_server_certifications(self):
        if self._authorisation_server_certifications is None:
            from .authorisation_server_certifications.client import (
                AuthorisationServerCertificationsClient,
            )

            self._authorisation_server_certifications = AuthorisationServerCertificationsClient(
                client_wrapper=self._client_wrapper
            )
        return self._authorisation_server_certifications

    @property
    def organisation_authority_claims(self):
        if self._organisation_authority_claims is None:
            from .organisation_authority_claims.client import OrganisationAuthorityClaimsClient

            self._organisation_authority_claims = OrganisationAuthorityClaimsClient(client_wrapper=self._client_wrapper)
        return self._organisation_authority_claims

    @property
    def organisation_authority_claims_authorisations(self):
        if self._organisation_authority_claims_authorisations is None:
            from .organisation_authority_claims_authorisations.client import (
                OrganisationAuthorityClaimsAuthorisationsClient,
            )

            self._organisation_authority_claims_authorisations = OrganisationAuthorityClaimsAuthorisationsClient(
                client_wrapper=self._client_wrapper
            )
        return self._organisation_authority_claims_authorisations

    @property
    def organisation_authority_domain_claims(self):
        if self._organisation_authority_domain_claims is None:
            from .organisation_authority_domain_claims.client import (
                OrganisationAuthorityDomainClaimsClient,
            )

            self._organisation_authority_domain_claims = OrganisationAuthorityDomainClaimsClient(
                client_wrapper=self._client_wrapper
            )
        return self._organisation_authority_domain_claims

    @property
    def organisation_certificates(self):
        if self._organisation_certificates is None:
            from .organisation_certificates.client import OrganisationCertificatesClient

            self._organisation_certificates = OrganisationCertificatesClient(client_wrapper=self._client_wrapper)
        return self._organisation_certificates

    @property
    def contacts(self):
        if self._contacts is None:
            from .contacts.client import ContactsClient

            self._contacts = ContactsClient(client_wrapper=self._client_wrapper)
        return self._contacts

    @property
    def software_statements_for_an_organisation(self):
        if self._software_statements_for_an_organisation is None:
            from .software_statements_for_an_organisation.client import (
                SoftwareStatementsForAnOrganisationClient,
            )

            self._software_statements_for_an_organisation = SoftwareStatementsForAnOrganisationClient(
                client_wrapper=self._client_wrapper
            )
        return self._software_statements_for_an_organisation

    @property
    def software_statement_assertions(self):
        if self._software_statement_assertions is None:
            from .software_statement_assertions.client import SoftwareStatementAssertionsClient

            self._software_statement_assertions = SoftwareStatementAssertionsClient(client_wrapper=self._client_wrapper)
        return self._software_statement_assertions

    @property
    def software_statement_authority_claims(self):
        if self._software_statement_authority_claims is None:
            from .software_statement_authority_claims.client import SoftwareStatementAuthorityClaimsClient

            self._software_statement_authority_claims = SoftwareStatementAuthorityClaimsClient(
                client_wrapper=self._client_wrapper
            )
        return self._software_statement_authority_claims

    @property
    def software_statement_certificates(self):
        if self._software_statement_certificates is None:
            from .software_statement_certificates.client import SoftwareStatementCertificatesClient

            self._software_statement_certificates = SoftwareStatementCertificatesClient(
                client_wrapper=self._client_wrapper
            )
        return self._software_statement_certificates

    @property
    def software_statement_certifications(self):
        if self._software_statement_certifications is None:
            from .software_statement_certifications.client import SoftwareStatementCertificationsClient

            self._software_statement_certifications = SoftwareStatementCertificationsClient(
                client_wrapper=self._client_wrapper
            )
        return self._software_statement_certifications

    @property
    def software_statement_metadata(self):
        if self._software_statement_metadata is None:
            from .software_statement_metadata.client import SoftwareStatementMetadataClient

            self._software_statement_metadata = SoftwareStatementMetadataClient(client_wrapper=self._client_wrapper)
        return self._software_statement_metadata

    @property
    def organisation_domain_users(self):
        if self._organisation_domain_users is None:
            from .organisation_domain_users.client import OrganisationDomainUsersClient

            self._organisation_domain_users = OrganisationDomainUsersClient(client_wrapper=self._client_wrapper)
        return self._organisation_domain_users

    @property
    def references_authorisation_domain_role(self):
        if self._references_authorisation_domain_role is None:
            from .references_authorisation_domain_role.client import (
                ReferencesAuthorisationDomainRoleClient,
            )

            self._references_authorisation_domain_role = ReferencesAuthorisationDomainRoleClient(
                client_wrapper=self._client_wrapper
            )
        return self._references_authorisation_domain_role

    @property
    def references_authorisation_domain_role_metadata(self):
        if self._references_authorisation_domain_role_metadata is None:
            from .references_authorisation_domain_role_metadata.client import (
                ReferencesAuthorisationDomainRoleMetadataClient,
            )

            self._references_authorisation_domain_role_metadata = ReferencesAuthorisationDomainRoleMetadataClient(
                client_wrapper=self._client_wrapper
            )
        return self._references_authorisation_domain_role_metadata

    @property
    def references_authorisation_domain(self):
        if self._references_authorisation_domain is None:
            from .references_authorisation_domain.client import ReferencesAuthorisationDomainClient

            self._references_authorisation_domain = ReferencesAuthorisationDomainClient(
                client_wrapper=self._client_wrapper
            )
        return self._references_authorisation_domain

    @property
    def references_authority(self):
        if self._references_authority is None:
            from .references_authority.client import ReferencesAuthorityClient

            self._references_authority = ReferencesAuthorityClient(client_wrapper=self._client_wrapper)
        return self._references_authority

    @property
    def references_authority_authorisation_domain(self):
        if self._references_authority_authorisation_domain is None:
            from .references_authority_authorisation_domain.client import (
                ReferencesAuthorityAuthorisationDomainClient,
            )

            self._references_authority_authorisation_domain = ReferencesAuthorityAuthorisationDomainClient(
                client_wrapper=self._client_wrapper
            )
        return self._references_authority_authorisation_domain

    @property
    def references_terms_and_conditions(self):
        if self._references_terms_and_conditions is None:
            from .references_terms_and_conditions.client import ReferencesTermsAndConditionsClient

            self._references_terms_and_conditions = ReferencesTermsAndConditionsClient(
                client_wrapper=self._client_wrapper
            )
        return self._references_terms_and_conditions


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    fapi_auth_date : typing.Optional[str]
    fapi_customer_ip_address : typing.Optional[str]
    fapi_interaction_id : typing.Optional[str]
    customer_user_agent : typing.Optional[str]
    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        fapi_auth_date="YOUR_FAPI_AUTH_DATE",
        fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
        fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
        customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        fapi_auth_date: typing.Optional[str] = None,
        fapi_customer_ip_address: typing.Optional[str] = None,
        fapi_interaction_id: typing.Optional[str] = None,
        customer_user_agent: typing.Optional[str] = None,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            fapi_auth_date=fapi_auth_date,
            fapi_customer_ip_address=fapi_customer_ip_address,
            fapi_interaction_id=fapi_interaction_id,
            customer_user_agent=customer_user_agent,
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._organisations: typing.Optional[AsyncOrganisationsClient] = None
        self._authorisation_servers: typing.Optional[AsyncAuthorisationServersClient] = None
        self._authorisation_servers_api_resources: typing.Optional[AsyncAuthorisationServersApiResourcesClient] = None
        self._authorisation_servers_api_discovery_endpoints: typing.Optional[
            AsyncAuthorisationServersApiDiscoveryEndpointsClient
        ] = None
        self._authorisation_server_certifications: typing.Optional[AsyncAuthorisationServerCertificationsClient] = None
        self._organisation_authority_claims: typing.Optional[AsyncOrganisationAuthorityClaimsClient] = None
        self._organisation_authority_claims_authorisations: typing.Optional[
            AsyncOrganisationAuthorityClaimsAuthorisationsClient
        ] = None
        self._organisation_authority_domain_claims: typing.Optional[AsyncOrganisationAuthorityDomainClaimsClient] = None
        self._organisation_certificates: typing.Optional[AsyncOrganisationCertificatesClient] = None
        self._contacts: typing.Optional[AsyncContactsClient] = None
        self._software_statements_for_an_organisation: typing.Optional[
            AsyncSoftwareStatementsForAnOrganisationClient
        ] = None
        self._software_statement_assertions: typing.Optional[AsyncSoftwareStatementAssertionsClient] = None
        self._software_statement_authority_claims: typing.Optional[AsyncSoftwareStatementAuthorityClaimsClient] = None
        self._software_statement_certificates: typing.Optional[AsyncSoftwareStatementCertificatesClient] = None
        self._software_statement_certifications: typing.Optional[AsyncSoftwareStatementCertificationsClient] = None
        self._software_statement_metadata: typing.Optional[AsyncSoftwareStatementMetadataClient] = None
        self._organisation_domain_users: typing.Optional[AsyncOrganisationDomainUsersClient] = None
        self._references_authorisation_domain_role: typing.Optional[AsyncReferencesAuthorisationDomainRoleClient] = None
        self._references_authorisation_domain_role_metadata: typing.Optional[
            AsyncReferencesAuthorisationDomainRoleMetadataClient
        ] = None
        self._references_authorisation_domain: typing.Optional[AsyncReferencesAuthorisationDomainClient] = None
        self._references_authority: typing.Optional[AsyncReferencesAuthorityClient] = None
        self._references_authority_authorisation_domain: typing.Optional[
            AsyncReferencesAuthorityAuthorisationDomainClient
        ] = None
        self._references_terms_and_conditions: typing.Optional[AsyncReferencesTermsAndConditionsClient] = None

    @property
    def organisations(self):
        if self._organisations is None:
            from .organisations.client import AsyncOrganisationsClient

            self._organisations = AsyncOrganisationsClient(client_wrapper=self._client_wrapper)
        return self._organisations

    @property
    def authorisation_servers(self):
        if self._authorisation_servers is None:
            from .authorisation_servers.client import AsyncAuthorisationServersClient

            self._authorisation_servers = AsyncAuthorisationServersClient(client_wrapper=self._client_wrapper)
        return self._authorisation_servers

    @property
    def authorisation_servers_api_resources(self):
        if self._authorisation_servers_api_resources is None:
            from .authorisation_servers_api_resources.client import (
                AsyncAuthorisationServersApiResourcesClient,
            )

            self._authorisation_servers_api_resources = AsyncAuthorisationServersApiResourcesClient(
                client_wrapper=self._client_wrapper
            )
        return self._authorisation_servers_api_resources

    @property
    def authorisation_servers_api_discovery_endpoints(self):
        if self._authorisation_servers_api_discovery_endpoints is None:
            from .authorisation_servers_api_discovery_endpoints.client import (
                AsyncAuthorisationServersApiDiscoveryEndpointsClient,
            )

            self._authorisation_servers_api_discovery_endpoints = AsyncAuthorisationServersApiDiscoveryEndpointsClient(
                client_wrapper=self._client_wrapper
            )
        return self._authorisation_servers_api_discovery_endpoints

    @property
    def authorisation_server_certifications(self):
        if self._authorisation_server_certifications is None:
            from .authorisation_server_certifications.client import (
                AsyncAuthorisationServerCertificationsClient,
            )

            self._authorisation_server_certifications = AsyncAuthorisationServerCertificationsClient(
                client_wrapper=self._client_wrapper
            )
        return self._authorisation_server_certifications

    @property
    def organisation_authority_claims(self):
        if self._organisation_authority_claims is None:
            from .organisation_authority_claims.client import AsyncOrganisationAuthorityClaimsClient

            self._organisation_authority_claims = AsyncOrganisationAuthorityClaimsClient(
                client_wrapper=self._client_wrapper
            )
        return self._organisation_authority_claims

    @property
    def organisation_authority_claims_authorisations(self):
        if self._organisation_authority_claims_authorisations is None:
            from .organisation_authority_claims_authorisations.client import (
                AsyncOrganisationAuthorityClaimsAuthorisationsClient,
            )

            self._organisation_authority_claims_authorisations = AsyncOrganisationAuthorityClaimsAuthorisationsClient(
                client_wrapper=self._client_wrapper
            )
        return self._organisation_authority_claims_authorisations

    @property
    def organisation_authority_domain_claims(self):
        if self._organisation_authority_domain_claims is None:
            from .organisation_authority_domain_claims.client import (
                AsyncOrganisationAuthorityDomainClaimsClient,
            )

            self._organisation_authority_domain_claims = AsyncOrganisationAuthorityDomainClaimsClient(
                client_wrapper=self._client_wrapper
            )
        return self._organisation_authority_domain_claims

    @property
    def organisation_certificates(self):
        if self._organisation_certificates is None:
            from .organisation_certificates.client import AsyncOrganisationCertificatesClient

            self._organisation_certificates = AsyncOrganisationCertificatesClient(client_wrapper=self._client_wrapper)
        return self._organisation_certificates

    @property
    def contacts(self):
        if self._contacts is None:
            from .contacts.client import AsyncContactsClient

            self._contacts = AsyncContactsClient(client_wrapper=self._client_wrapper)
        return self._contacts

    @property
    def software_statements_for_an_organisation(self):
        if self._software_statements_for_an_organisation is None:
            from .software_statements_for_an_organisation.client import (
                AsyncSoftwareStatementsForAnOrganisationClient,
            )

            self._software_statements_for_an_organisation = AsyncSoftwareStatementsForAnOrganisationClient(
                client_wrapper=self._client_wrapper
            )
        return self._software_statements_for_an_organisation

    @property
    def software_statement_assertions(self):
        if self._software_statement_assertions is None:
            from .software_statement_assertions.client import AsyncSoftwareStatementAssertionsClient

            self._software_statement_assertions = AsyncSoftwareStatementAssertionsClient(
                client_wrapper=self._client_wrapper
            )
        return self._software_statement_assertions

    @property
    def software_statement_authority_claims(self):
        if self._software_statement_authority_claims is None:
            from .software_statement_authority_claims.client import (
                AsyncSoftwareStatementAuthorityClaimsClient,
            )

            self._software_statement_authority_claims = AsyncSoftwareStatementAuthorityClaimsClient(
                client_wrapper=self._client_wrapper
            )
        return self._software_statement_authority_claims

    @property
    def software_statement_certificates(self):
        if self._software_statement_certificates is None:
            from .software_statement_certificates.client import AsyncSoftwareStatementCertificatesClient

            self._software_statement_certificates = AsyncSoftwareStatementCertificatesClient(
                client_wrapper=self._client_wrapper
            )
        return self._software_statement_certificates

    @property
    def software_statement_certifications(self):
        if self._software_statement_certifications is None:
            from .software_statement_certifications.client import (
                AsyncSoftwareStatementCertificationsClient,
            )

            self._software_statement_certifications = AsyncSoftwareStatementCertificationsClient(
                client_wrapper=self._client_wrapper
            )
        return self._software_statement_certifications

    @property
    def software_statement_metadata(self):
        if self._software_statement_metadata is None:
            from .software_statement_metadata.client import AsyncSoftwareStatementMetadataClient

            self._software_statement_metadata = AsyncSoftwareStatementMetadataClient(
                client_wrapper=self._client_wrapper
            )
        return self._software_statement_metadata

    @property
    def organisation_domain_users(self):
        if self._organisation_domain_users is None:
            from .organisation_domain_users.client import AsyncOrganisationDomainUsersClient

            self._organisation_domain_users = AsyncOrganisationDomainUsersClient(client_wrapper=self._client_wrapper)
        return self._organisation_domain_users

    @property
    def references_authorisation_domain_role(self):
        if self._references_authorisation_domain_role is None:
            from .references_authorisation_domain_role.client import (
                AsyncReferencesAuthorisationDomainRoleClient,
            )

            self._references_authorisation_domain_role = AsyncReferencesAuthorisationDomainRoleClient(
                client_wrapper=self._client_wrapper
            )
        return self._references_authorisation_domain_role

    @property
    def references_authorisation_domain_role_metadata(self):
        if self._references_authorisation_domain_role_metadata is None:
            from .references_authorisation_domain_role_metadata.client import (
                AsyncReferencesAuthorisationDomainRoleMetadataClient,
            )

            self._references_authorisation_domain_role_metadata = AsyncReferencesAuthorisationDomainRoleMetadataClient(
                client_wrapper=self._client_wrapper
            )
        return self._references_authorisation_domain_role_metadata

    @property
    def references_authorisation_domain(self):
        if self._references_authorisation_domain is None:
            from .references_authorisation_domain.client import AsyncReferencesAuthorisationDomainClient

            self._references_authorisation_domain = AsyncReferencesAuthorisationDomainClient(
                client_wrapper=self._client_wrapper
            )
        return self._references_authorisation_domain

    @property
    def references_authority(self):
        if self._references_authority is None:
            from .references_authority.client import AsyncReferencesAuthorityClient

            self._references_authority = AsyncReferencesAuthorityClient(client_wrapper=self._client_wrapper)
        return self._references_authority

    @property
    def references_authority_authorisation_domain(self):
        if self._references_authority_authorisation_domain is None:
            from .references_authority_authorisation_domain.client import (
                AsyncReferencesAuthorityAuthorisationDomainClient,
            )

            self._references_authority_authorisation_domain = AsyncReferencesAuthorityAuthorisationDomainClient(
                client_wrapper=self._client_wrapper
            )
        return self._references_authority_authorisation_domain

    @property
    def references_terms_and_conditions(self):
        if self._references_terms_and_conditions is None:
            from .references_terms_and_conditions.client import AsyncReferencesTermsAndConditionsClient

            self._references_terms_and_conditions = AsyncReferencesTermsAndConditionsClient(
                client_wrapper=self._client_wrapper
            )
        return self._references_terms_and_conditions


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
