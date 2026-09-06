

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.notification_webhook_status_enum import NotificationWebhookStatusEnum
from ..types.organisation_id import OrganisationId
from ..types.sns_notification_webhook_uri import SnsNotificationWebhookUri
from ..types.software_statement import SoftwareStatement
from ..types.software_statement_id import SoftwareStatementId
from ..types.software_statement_request_mode import SoftwareStatementRequestMode
from ..types.software_statements import SoftwareStatements
from .raw_client import AsyncRawSoftwareStatementsForAnOrganisationClient, RawSoftwareStatementsForAnOrganisationClient
from .types.software_statement_update_request_status import SoftwareStatementUpdateRequestStatus


OMIT = typing.cast(typing.Any, ...)


class SoftwareStatementsForAnOrganisationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSoftwareStatementsForAnOrganisationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSoftwareStatementsForAnOrganisationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSoftwareStatementsForAnOrganisationClient
        """
        return self._raw_client

    def get_all_software_statements_for_the_given_organisation(
        self, organisation_id: OrganisationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SoftwareStatements:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoftwareStatements
            All software statements for the org

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
        client.software_statements_for_an_organisation.get_all_software_statements_for_the_given_organisation(
            organisation_id="OrganisationId",
        )
        """
        _response = self._raw_client.get_all_software_statements_for_the_given_organisation(
            organisation_id, request_options=request_options
        )
        return _response.data

    def get_a_software_statement(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoftwareStatement:
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
        SoftwareStatement
            Get the software statements with the given id

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
        client.software_statements_for_an_organisation.get_a_software_statement(
            organisation_id="OrganisationId",
            software_statement_id="SoftwareStatementId",
        )
        """
        _response = self._raw_client.get_a_software_statement(
            organisation_id, software_statement_id, request_options=request_options
        )
        return _response.data

    def update_a_software_statement_by_id(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        *,
        client_name: str,
        client_uri: str,
        logo_uri: str,
        redirect_uri: typing.Sequence[str],
        version: float,
        status: typing.Optional[SoftwareStatementUpdateRequestStatus] = OMIT,
        additional_software_metadata: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        environment: typing.Optional[str] = OMIT,
        mode: typing.Optional[SoftwareStatementRequestMode] = OMIT,
        notification_webhook: typing.Optional[SnsNotificationWebhookUri] = OMIT,
        notification_webhook_status: typing.Optional[NotificationWebhookStatusEnum] = OMIT,
        on_behalf_of: typing.Optional[str] = OMIT,
        policy_uri: typing.Optional[str] = OMIT,
        terms_of_service_uri: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoftwareStatement:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        software_statement_id : SoftwareStatementId
            The software statement ID

        client_name : str
            Software Statement client name

        client_uri : str
            The Software Statement compliant client URI

        logo_uri : str
            The Software Statement compliant logo URI

        redirect_uri : typing.Sequence[str]
            The Software Statement redirect URIs

        version : float
            Software Statement version as provided by the organisation's PTC

        status : typing.Optional[SoftwareStatementUpdateRequestStatus]
            Should this software statement be active or suspended?

        additional_software_metadata : typing.Optional[str]
            Extra metadata defined by the org admins to be loaded into the software statement and made avaiable during introspection

        description : typing.Optional[str]
            Software Statement description

        environment : typing.Optional[str]
            The additional check for software statement, this field can avoid environment checks.

        mode : typing.Optional[SoftwareStatementRequestMode]
            The additional check to see if the environment reflected above is live or test.

        notification_webhook : typing.Optional[SnsNotificationWebhookUri]

        notification_webhook_status : typing.Optional[NotificationWebhookStatusEnum]

        on_behalf_of : typing.Optional[str]
            A reference to fourth party organisation resource on the RTS Directory if the registering Org is acting on behalf of another

        policy_uri : typing.Optional[str]
            The Software Statement compliant policy URI

        terms_of_service_uri : typing.Optional[str]
            The Software Statement terms of service compliant URI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoftwareStatement
            Get the software statements with the given id

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
        client.software_statements_for_an_organisation.update_a_software_statement_by_id(
            organisation_id="OrganisationId",
            software_statement_id="SoftwareStatementId",
            client_name="ClientName",
            client_uri="ClientUri",
            logo_uri="LogoUri",
            redirect_uri=["RedirectUri"],
            version=1.1,
        )
        """
        _response = self._raw_client.update_a_software_statement_by_id(
            organisation_id,
            software_statement_id,
            client_name=client_name,
            client_uri=client_uri,
            logo_uri=logo_uri,
            redirect_uri=redirect_uri,
            version=version,
            status=status,
            additional_software_metadata=additional_software_metadata,
            description=description,
            environment=environment,
            mode=mode,
            notification_webhook=notification_webhook,
            notification_webhook_status=notification_webhook_status,
            on_behalf_of=on_behalf_of,
            policy_uri=policy_uri,
            terms_of_service_uri=terms_of_service_uri,
            request_options=request_options,
        )
        return _response.data

    def unlock_a_software_statement(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        *,
        unlock: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoftwareStatement:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        software_statement_id : SoftwareStatementId
            The software statement ID

        unlock : typing.Optional[bool]
            Unlock Software Statement

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoftwareStatement
            Get the software statements with the given id

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
        client.software_statements_for_an_organisation.unlock_a_software_statement(
            organisation_id="OrganisationId",
            software_statement_id="SoftwareStatementId",
        )
        """
        _response = self._raw_client.unlock_a_software_statement(
            organisation_id, software_statement_id, unlock=unlock, request_options=request_options
        )
        return _response.data


class AsyncSoftwareStatementsForAnOrganisationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSoftwareStatementsForAnOrganisationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSoftwareStatementsForAnOrganisationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSoftwareStatementsForAnOrganisationClient
        """
        return self._raw_client

    async def get_all_software_statements_for_the_given_organisation(
        self, organisation_id: OrganisationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SoftwareStatements:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoftwareStatements
            All software statements for the org

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
            await client.software_statements_for_an_organisation.get_all_software_statements_for_the_given_organisation(
                organisation_id="OrganisationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_software_statements_for_the_given_organisation(
            organisation_id, request_options=request_options
        )
        return _response.data

    async def get_a_software_statement(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoftwareStatement:
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
        SoftwareStatement
            Get the software statements with the given id

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
            await client.software_statements_for_an_organisation.get_a_software_statement(
                organisation_id="OrganisationId",
                software_statement_id="SoftwareStatementId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_software_statement(
            organisation_id, software_statement_id, request_options=request_options
        )
        return _response.data

    async def update_a_software_statement_by_id(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        *,
        client_name: str,
        client_uri: str,
        logo_uri: str,
        redirect_uri: typing.Sequence[str],
        version: float,
        status: typing.Optional[SoftwareStatementUpdateRequestStatus] = OMIT,
        additional_software_metadata: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        environment: typing.Optional[str] = OMIT,
        mode: typing.Optional[SoftwareStatementRequestMode] = OMIT,
        notification_webhook: typing.Optional[SnsNotificationWebhookUri] = OMIT,
        notification_webhook_status: typing.Optional[NotificationWebhookStatusEnum] = OMIT,
        on_behalf_of: typing.Optional[str] = OMIT,
        policy_uri: typing.Optional[str] = OMIT,
        terms_of_service_uri: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoftwareStatement:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        software_statement_id : SoftwareStatementId
            The software statement ID

        client_name : str
            Software Statement client name

        client_uri : str
            The Software Statement compliant client URI

        logo_uri : str
            The Software Statement compliant logo URI

        redirect_uri : typing.Sequence[str]
            The Software Statement redirect URIs

        version : float
            Software Statement version as provided by the organisation's PTC

        status : typing.Optional[SoftwareStatementUpdateRequestStatus]
            Should this software statement be active or suspended?

        additional_software_metadata : typing.Optional[str]
            Extra metadata defined by the org admins to be loaded into the software statement and made avaiable during introspection

        description : typing.Optional[str]
            Software Statement description

        environment : typing.Optional[str]
            The additional check for software statement, this field can avoid environment checks.

        mode : typing.Optional[SoftwareStatementRequestMode]
            The additional check to see if the environment reflected above is live or test.

        notification_webhook : typing.Optional[SnsNotificationWebhookUri]

        notification_webhook_status : typing.Optional[NotificationWebhookStatusEnum]

        on_behalf_of : typing.Optional[str]
            A reference to fourth party organisation resource on the RTS Directory if the registering Org is acting on behalf of another

        policy_uri : typing.Optional[str]
            The Software Statement compliant policy URI

        terms_of_service_uri : typing.Optional[str]
            The Software Statement terms of service compliant URI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoftwareStatement
            Get the software statements with the given id

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
            await client.software_statements_for_an_organisation.update_a_software_statement_by_id(
                organisation_id="OrganisationId",
                software_statement_id="SoftwareStatementId",
                client_name="ClientName",
                client_uri="ClientUri",
                logo_uri="LogoUri",
                redirect_uri=["RedirectUri"],
                version=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_a_software_statement_by_id(
            organisation_id,
            software_statement_id,
            client_name=client_name,
            client_uri=client_uri,
            logo_uri=logo_uri,
            redirect_uri=redirect_uri,
            version=version,
            status=status,
            additional_software_metadata=additional_software_metadata,
            description=description,
            environment=environment,
            mode=mode,
            notification_webhook=notification_webhook,
            notification_webhook_status=notification_webhook_status,
            on_behalf_of=on_behalf_of,
            policy_uri=policy_uri,
            terms_of_service_uri=terms_of_service_uri,
            request_options=request_options,
        )
        return _response.data

    async def unlock_a_software_statement(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        *,
        unlock: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoftwareStatement:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        software_statement_id : SoftwareStatementId
            The software statement ID

        unlock : typing.Optional[bool]
            Unlock Software Statement

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoftwareStatement
            Get the software statements with the given id

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
            await client.software_statements_for_an_organisation.unlock_a_software_statement(
                organisation_id="OrganisationId",
                software_statement_id="SoftwareStatementId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unlock_a_software_statement(
            organisation_id, software_statement_id, unlock=unlock, request_options=request_options
        )
        return _response.data
