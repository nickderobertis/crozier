

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.me_response import MeResponse

if typing.TYPE_CHECKING:
    from .client_api_display.client import AsyncClientApiDisplayClient, ClientApiDisplayClient
    from .client_api_file_upload.client import AsyncClientApiFileUploadClient, ClientApiFileUploadClient
    from .client_api_response.client import AsyncClientApiResponseClient, ClientApiResponseClient
    from .client_api_user.client import AsyncClientApiUserClient, ClientApiUserClient
    from .client_api_workspace.client import AsyncClientApiWorkspaceClient, ClientApiWorkspaceClient
    from .health.client import AsyncHealthClient, HealthClient
    from .management_api_contact_attribute_keys.client import (
        AsyncManagementApiContactAttributeKeysClient,
        ManagementApiContactAttributeKeysClient,
    )
    from .management_api_contacts.client import AsyncManagementApiContactsClient, ManagementApiContactsClient
    from .management_api_responses.client import AsyncManagementApiResponsesClient, ManagementApiResponsesClient
    from .management_api_surveys_contact_links.client import (
        AsyncManagementApiSurveysContactLinksClient,
        ManagementApiSurveysContactLinksClient,
    )
    from .management_api_webhooks.client import AsyncManagementApiWebhooksClient, ManagementApiWebhooksClient
    from .organizations_api_teams.client import AsyncOrganizationsApiTeamsClient, OrganizationsApiTeamsClient
    from .organizations_api_users.client import AsyncOrganizationsApiUsersClient, OrganizationsApiUsersClient
    from .organizations_api_workspace_teams.client import (
        AsyncOrganizationsApiWorkspaceTeamsClient,
        OrganizationsApiWorkspaceTeamsClient,
    )
    from .roles.client import AsyncRolesClient, RolesClient


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
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)
        self._client_api_response: typing.Optional[ClientApiResponseClient] = None
        self._client_api_display: typing.Optional[ClientApiDisplayClient] = None
        self._client_api_workspace: typing.Optional[ClientApiWorkspaceClient] = None
        self._client_api_user: typing.Optional[ClientApiUserClient] = None
        self._client_api_file_upload: typing.Optional[ClientApiFileUploadClient] = None
        self._health: typing.Optional[HealthClient] = None
        self._roles: typing.Optional[RolesClient] = None
        self._management_api_responses: typing.Optional[ManagementApiResponsesClient] = None
        self._management_api_contacts: typing.Optional[ManagementApiContactsClient] = None
        self._management_api_contact_attribute_keys: typing.Optional[ManagementApiContactAttributeKeysClient] = None
        self._management_api_surveys_contact_links: typing.Optional[ManagementApiSurveysContactLinksClient] = None
        self._management_api_webhooks: typing.Optional[ManagementApiWebhooksClient] = None
        self._organizations_api_teams: typing.Optional[OrganizationsApiTeamsClient] = None
        self._organizations_api_workspace_teams: typing.Optional[OrganizationsApiWorkspaceTeamsClient] = None
        self._organizations_api_users: typing.Optional[OrganizationsApiUsersClient] = None

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def me(self, *, request_options: typing.Optional[RequestOptions] = None) -> MeResponse:
        """
        Fetches the Workspaces and organizations associated with the API key.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MeResponse
            API key information retrieved successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.me()
        """
        _response = self._raw_client.me(request_options=request_options)
        return _response.data

    @property
    def client_api_response(self):
        if self._client_api_response is None:
            from .client_api_response.client import ClientApiResponseClient

            self._client_api_response = ClientApiResponseClient(client_wrapper=self._client_wrapper)
        return self._client_api_response

    @property
    def client_api_display(self):
        if self._client_api_display is None:
            from .client_api_display.client import ClientApiDisplayClient

            self._client_api_display = ClientApiDisplayClient(client_wrapper=self._client_wrapper)
        return self._client_api_display

    @property
    def client_api_workspace(self):
        if self._client_api_workspace is None:
            from .client_api_workspace.client import ClientApiWorkspaceClient

            self._client_api_workspace = ClientApiWorkspaceClient(client_wrapper=self._client_wrapper)
        return self._client_api_workspace

    @property
    def client_api_user(self):
        if self._client_api_user is None:
            from .client_api_user.client import ClientApiUserClient

            self._client_api_user = ClientApiUserClient(client_wrapper=self._client_wrapper)
        return self._client_api_user

    @property
    def client_api_file_upload(self):
        if self._client_api_file_upload is None:
            from .client_api_file_upload.client import ClientApiFileUploadClient

            self._client_api_file_upload = ClientApiFileUploadClient(client_wrapper=self._client_wrapper)
        return self._client_api_file_upload

    @property
    def health(self):
        if self._health is None:
            from .health.client import HealthClient

            self._health = HealthClient(client_wrapper=self._client_wrapper)
        return self._health

    @property
    def roles(self):
        if self._roles is None:
            from .roles.client import RolesClient

            self._roles = RolesClient(client_wrapper=self._client_wrapper)
        return self._roles

    @property
    def management_api_responses(self):
        if self._management_api_responses is None:
            from .management_api_responses.client import ManagementApiResponsesClient

            self._management_api_responses = ManagementApiResponsesClient(client_wrapper=self._client_wrapper)
        return self._management_api_responses

    @property
    def management_api_contacts(self):
        if self._management_api_contacts is None:
            from .management_api_contacts.client import ManagementApiContactsClient

            self._management_api_contacts = ManagementApiContactsClient(client_wrapper=self._client_wrapper)
        return self._management_api_contacts

    @property
    def management_api_contact_attribute_keys(self):
        if self._management_api_contact_attribute_keys is None:
            from .management_api_contact_attribute_keys.client import (
                ManagementApiContactAttributeKeysClient,
            )

            self._management_api_contact_attribute_keys = ManagementApiContactAttributeKeysClient(
                client_wrapper=self._client_wrapper
            )
        return self._management_api_contact_attribute_keys

    @property
    def management_api_surveys_contact_links(self):
        if self._management_api_surveys_contact_links is None:
            from .management_api_surveys_contact_links.client import (
                ManagementApiSurveysContactLinksClient,
            )

            self._management_api_surveys_contact_links = ManagementApiSurveysContactLinksClient(
                client_wrapper=self._client_wrapper
            )
        return self._management_api_surveys_contact_links

    @property
    def management_api_webhooks(self):
        if self._management_api_webhooks is None:
            from .management_api_webhooks.client import ManagementApiWebhooksClient

            self._management_api_webhooks = ManagementApiWebhooksClient(client_wrapper=self._client_wrapper)
        return self._management_api_webhooks

    @property
    def organizations_api_teams(self):
        if self._organizations_api_teams is None:
            from .organizations_api_teams.client import OrganizationsApiTeamsClient

            self._organizations_api_teams = OrganizationsApiTeamsClient(client_wrapper=self._client_wrapper)
        return self._organizations_api_teams

    @property
    def organizations_api_workspace_teams(self):
        if self._organizations_api_workspace_teams is None:
            from .organizations_api_workspace_teams.client import OrganizationsApiWorkspaceTeamsClient

            self._organizations_api_workspace_teams = OrganizationsApiWorkspaceTeamsClient(
                client_wrapper=self._client_wrapper
            )
        return self._organizations_api_workspace_teams

    @property
    def organizations_api_users(self):
        if self._organizations_api_users is None:
            from .organizations_api_users.client import OrganizationsApiUsersClient

            self._organizations_api_users = OrganizationsApiUsersClient(client_wrapper=self._client_wrapper)
        return self._organizations_api_users


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
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)
        self._client_api_response: typing.Optional[AsyncClientApiResponseClient] = None
        self._client_api_display: typing.Optional[AsyncClientApiDisplayClient] = None
        self._client_api_workspace: typing.Optional[AsyncClientApiWorkspaceClient] = None
        self._client_api_user: typing.Optional[AsyncClientApiUserClient] = None
        self._client_api_file_upload: typing.Optional[AsyncClientApiFileUploadClient] = None
        self._health: typing.Optional[AsyncHealthClient] = None
        self._roles: typing.Optional[AsyncRolesClient] = None
        self._management_api_responses: typing.Optional[AsyncManagementApiResponsesClient] = None
        self._management_api_contacts: typing.Optional[AsyncManagementApiContactsClient] = None
        self._management_api_contact_attribute_keys: typing.Optional[AsyncManagementApiContactAttributeKeysClient] = (
            None
        )
        self._management_api_surveys_contact_links: typing.Optional[AsyncManagementApiSurveysContactLinksClient] = None
        self._management_api_webhooks: typing.Optional[AsyncManagementApiWebhooksClient] = None
        self._organizations_api_teams: typing.Optional[AsyncOrganizationsApiTeamsClient] = None
        self._organizations_api_workspace_teams: typing.Optional[AsyncOrganizationsApiWorkspaceTeamsClient] = None
        self._organizations_api_users: typing.Optional[AsyncOrganizationsApiUsersClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def me(self, *, request_options: typing.Optional[RequestOptions] = None) -> MeResponse:
        """
        Fetches the Workspaces and organizations associated with the API key.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MeResponse
            API key information retrieved successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.me()


        asyncio.run(main())
        """
        _response = await self._raw_client.me(request_options=request_options)
        return _response.data

    @property
    def client_api_response(self):
        if self._client_api_response is None:
            from .client_api_response.client import AsyncClientApiResponseClient

            self._client_api_response = AsyncClientApiResponseClient(client_wrapper=self._client_wrapper)
        return self._client_api_response

    @property
    def client_api_display(self):
        if self._client_api_display is None:
            from .client_api_display.client import AsyncClientApiDisplayClient

            self._client_api_display = AsyncClientApiDisplayClient(client_wrapper=self._client_wrapper)
        return self._client_api_display

    @property
    def client_api_workspace(self):
        if self._client_api_workspace is None:
            from .client_api_workspace.client import AsyncClientApiWorkspaceClient

            self._client_api_workspace = AsyncClientApiWorkspaceClient(client_wrapper=self._client_wrapper)
        return self._client_api_workspace

    @property
    def client_api_user(self):
        if self._client_api_user is None:
            from .client_api_user.client import AsyncClientApiUserClient

            self._client_api_user = AsyncClientApiUserClient(client_wrapper=self._client_wrapper)
        return self._client_api_user

    @property
    def client_api_file_upload(self):
        if self._client_api_file_upload is None:
            from .client_api_file_upload.client import AsyncClientApiFileUploadClient

            self._client_api_file_upload = AsyncClientApiFileUploadClient(client_wrapper=self._client_wrapper)
        return self._client_api_file_upload

    @property
    def health(self):
        if self._health is None:
            from .health.client import AsyncHealthClient

            self._health = AsyncHealthClient(client_wrapper=self._client_wrapper)
        return self._health

    @property
    def roles(self):
        if self._roles is None:
            from .roles.client import AsyncRolesClient

            self._roles = AsyncRolesClient(client_wrapper=self._client_wrapper)
        return self._roles

    @property
    def management_api_responses(self):
        if self._management_api_responses is None:
            from .management_api_responses.client import AsyncManagementApiResponsesClient

            self._management_api_responses = AsyncManagementApiResponsesClient(client_wrapper=self._client_wrapper)
        return self._management_api_responses

    @property
    def management_api_contacts(self):
        if self._management_api_contacts is None:
            from .management_api_contacts.client import AsyncManagementApiContactsClient

            self._management_api_contacts = AsyncManagementApiContactsClient(client_wrapper=self._client_wrapper)
        return self._management_api_contacts

    @property
    def management_api_contact_attribute_keys(self):
        if self._management_api_contact_attribute_keys is None:
            from .management_api_contact_attribute_keys.client import (
                AsyncManagementApiContactAttributeKeysClient,
            )

            self._management_api_contact_attribute_keys = AsyncManagementApiContactAttributeKeysClient(
                client_wrapper=self._client_wrapper
            )
        return self._management_api_contact_attribute_keys

    @property
    def management_api_surveys_contact_links(self):
        if self._management_api_surveys_contact_links is None:
            from .management_api_surveys_contact_links.client import (
                AsyncManagementApiSurveysContactLinksClient,
            )

            self._management_api_surveys_contact_links = AsyncManagementApiSurveysContactLinksClient(
                client_wrapper=self._client_wrapper
            )
        return self._management_api_surveys_contact_links

    @property
    def management_api_webhooks(self):
        if self._management_api_webhooks is None:
            from .management_api_webhooks.client import AsyncManagementApiWebhooksClient

            self._management_api_webhooks = AsyncManagementApiWebhooksClient(client_wrapper=self._client_wrapper)
        return self._management_api_webhooks

    @property
    def organizations_api_teams(self):
        if self._organizations_api_teams is None:
            from .organizations_api_teams.client import AsyncOrganizationsApiTeamsClient

            self._organizations_api_teams = AsyncOrganizationsApiTeamsClient(client_wrapper=self._client_wrapper)
        return self._organizations_api_teams

    @property
    def organizations_api_workspace_teams(self):
        if self._organizations_api_workspace_teams is None:
            from .organizations_api_workspace_teams.client import (
                AsyncOrganizationsApiWorkspaceTeamsClient,
            )

            self._organizations_api_workspace_teams = AsyncOrganizationsApiWorkspaceTeamsClient(
                client_wrapper=self._client_wrapper
            )
        return self._organizations_api_workspace_teams

    @property
    def organizations_api_users(self):
        if self._organizations_api_users is None:
            from .organizations_api_users.client import AsyncOrganizationsApiUsersClient

            self._organizations_api_users = AsyncOrganizationsApiUsersClient(client_wrapper=self._client_wrapper)
        return self._organizations_api_users


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
