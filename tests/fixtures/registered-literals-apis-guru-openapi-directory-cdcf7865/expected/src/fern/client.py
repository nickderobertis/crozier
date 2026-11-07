

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .addons.client import AddonsClient, AsyncAddonsClient
    from .base.client import AsyncBaseClient, BaseClient
    from .citations.client import AsyncCitationsClient, CitationsClient
    from .collections.client import AsyncCollectionsClient, CollectionsClient
    from .comments.client import AsyncCommentsClient, CommentsClient
    from .draft_registrations.client import AsyncDraftRegistrationsClient, DraftRegistrationsClient
    from .files.client import AsyncFilesClient, FilesClient
    from .institutions.client import AsyncInstitutionsClient, InstitutionsClient
    from .licenses.client import AsyncLicensesClient, LicensesClient
    from .logs.client import AsyncLogsClient, LogsClient
    from .nodes.client import AsyncNodesClient, NodesClient
    from .preprint_providers.client import AsyncPreprintProvidersClient, PreprintProvidersClient
    from .preprints.client import AsyncPreprintsClient, PreprintsClient
    from .registration_schema_blocks.client import AsyncRegistrationSchemaBlocksClient, RegistrationSchemaBlocksClient
    from .registration_schemas.client import AsyncRegistrationSchemasClient, RegistrationSchemasClient
    from .registrations.client import AsyncRegistrationsClient, RegistrationsClient
    from .schema_response_actions.client import AsyncSchemaResponseActionsClient, SchemaResponseActionsClient
    from .schema_responses.client import AsyncSchemaResponsesClient, SchemaResponsesClient
    from .taxonomies.client import AsyncTaxonomiesClient, TaxonomiesClient
    from .users.client import AsyncUsersClient, UsersClient
    from .view_only_links.client import AsyncViewOnlyLinksClient, ViewOnlyLinksClient
    from .wikis.client import AsyncWikisClient, WikisClient


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

    client = FernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
        self._base: typing.Optional[BaseClient] = None
        self._logs: typing.Optional[LogsClient] = None
        self._addons: typing.Optional[AddonsClient] = None
        self._citations: typing.Optional[CitationsClient] = None
        self._collections: typing.Optional[CollectionsClient] = None
        self._comments: typing.Optional[CommentsClient] = None
        self._draft_registrations: typing.Optional[DraftRegistrationsClient] = None
        self._files: typing.Optional[FilesClient] = None
        self._institutions: typing.Optional[InstitutionsClient] = None
        self._licenses: typing.Optional[LicensesClient] = None
        self._nodes: typing.Optional[NodesClient] = None
        self._preprint_providers: typing.Optional[PreprintProvidersClient] = None
        self._preprints: typing.Optional[PreprintsClient] = None
        self._registrations: typing.Optional[RegistrationsClient] = None
        self._schema_responses: typing.Optional[SchemaResponsesClient] = None
        self._schema_response_actions: typing.Optional[SchemaResponseActionsClient] = None
        self._registration_schema_blocks: typing.Optional[RegistrationSchemaBlocksClient] = None
        self._registration_schemas: typing.Optional[RegistrationSchemasClient] = None
        self._taxonomies: typing.Optional[TaxonomiesClient] = None
        self._users: typing.Optional[UsersClient] = None
        self._view_only_links: typing.Optional[ViewOnlyLinksClient] = None
        self._wikis: typing.Optional[WikisClient] = None

    @property
    def base(self):
        if self._base is None:
            from .base.client import BaseClient

            self._base = BaseClient(client_wrapper=self._client_wrapper)
        return self._base

    @property
    def logs(self):
        if self._logs is None:
            from .logs.client import LogsClient

            self._logs = LogsClient(client_wrapper=self._client_wrapper)
        return self._logs

    @property
    def addons(self):
        if self._addons is None:
            from .addons.client import AddonsClient

            self._addons = AddonsClient(client_wrapper=self._client_wrapper)
        return self._addons

    @property
    def citations(self):
        if self._citations is None:
            from .citations.client import CitationsClient

            self._citations = CitationsClient(client_wrapper=self._client_wrapper)
        return self._citations

    @property
    def collections(self):
        if self._collections is None:
            from .collections.client import CollectionsClient

            self._collections = CollectionsClient(client_wrapper=self._client_wrapper)
        return self._collections

    @property
    def comments(self):
        if self._comments is None:
            from .comments.client import CommentsClient

            self._comments = CommentsClient(client_wrapper=self._client_wrapper)
        return self._comments

    @property
    def draft_registrations(self):
        if self._draft_registrations is None:
            from .draft_registrations.client import DraftRegistrationsClient

            self._draft_registrations = DraftRegistrationsClient(client_wrapper=self._client_wrapper)
        return self._draft_registrations

    @property
    def files(self):
        if self._files is None:
            from .files.client import FilesClient

            self._files = FilesClient(client_wrapper=self._client_wrapper)
        return self._files

    @property
    def institutions(self):
        if self._institutions is None:
            from .institutions.client import InstitutionsClient

            self._institutions = InstitutionsClient(client_wrapper=self._client_wrapper)
        return self._institutions

    @property
    def licenses(self):
        if self._licenses is None:
            from .licenses.client import LicensesClient

            self._licenses = LicensesClient(client_wrapper=self._client_wrapper)
        return self._licenses

    @property
    def nodes(self):
        if self._nodes is None:
            from .nodes.client import NodesClient

            self._nodes = NodesClient(client_wrapper=self._client_wrapper)
        return self._nodes

    @property
    def preprint_providers(self):
        if self._preprint_providers is None:
            from .preprint_providers.client import PreprintProvidersClient

            self._preprint_providers = PreprintProvidersClient(client_wrapper=self._client_wrapper)
        return self._preprint_providers

    @property
    def preprints(self):
        if self._preprints is None:
            from .preprints.client import PreprintsClient

            self._preprints = PreprintsClient(client_wrapper=self._client_wrapper)
        return self._preprints

    @property
    def registrations(self):
        if self._registrations is None:
            from .registrations.client import RegistrationsClient

            self._registrations = RegistrationsClient(client_wrapper=self._client_wrapper)
        return self._registrations

    @property
    def schema_responses(self):
        if self._schema_responses is None:
            from .schema_responses.client import SchemaResponsesClient

            self._schema_responses = SchemaResponsesClient(client_wrapper=self._client_wrapper)
        return self._schema_responses

    @property
    def schema_response_actions(self):
        if self._schema_response_actions is None:
            from .schema_response_actions.client import SchemaResponseActionsClient

            self._schema_response_actions = SchemaResponseActionsClient(client_wrapper=self._client_wrapper)
        return self._schema_response_actions

    @property
    def registration_schema_blocks(self):
        if self._registration_schema_blocks is None:
            from .registration_schema_blocks.client import RegistrationSchemaBlocksClient

            self._registration_schema_blocks = RegistrationSchemaBlocksClient(client_wrapper=self._client_wrapper)
        return self._registration_schema_blocks

    @property
    def registration_schemas(self):
        if self._registration_schemas is None:
            from .registration_schemas.client import RegistrationSchemasClient

            self._registration_schemas = RegistrationSchemasClient(client_wrapper=self._client_wrapper)
        return self._registration_schemas

    @property
    def taxonomies(self):
        if self._taxonomies is None:
            from .taxonomies.client import TaxonomiesClient

            self._taxonomies = TaxonomiesClient(client_wrapper=self._client_wrapper)
        return self._taxonomies

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def view_only_links(self):
        if self._view_only_links is None:
            from .view_only_links.client import ViewOnlyLinksClient

            self._view_only_links = ViewOnlyLinksClient(client_wrapper=self._client_wrapper)
        return self._view_only_links

    @property
    def wikis(self):
        if self._wikis is None:
            from .wikis.client import WikisClient

            self._wikis = WikisClient(client_wrapper=self._client_wrapper)
        return self._wikis


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

    client = AsyncFernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
        self._base: typing.Optional[AsyncBaseClient] = None
        self._logs: typing.Optional[AsyncLogsClient] = None
        self._addons: typing.Optional[AsyncAddonsClient] = None
        self._citations: typing.Optional[AsyncCitationsClient] = None
        self._collections: typing.Optional[AsyncCollectionsClient] = None
        self._comments: typing.Optional[AsyncCommentsClient] = None
        self._draft_registrations: typing.Optional[AsyncDraftRegistrationsClient] = None
        self._files: typing.Optional[AsyncFilesClient] = None
        self._institutions: typing.Optional[AsyncInstitutionsClient] = None
        self._licenses: typing.Optional[AsyncLicensesClient] = None
        self._nodes: typing.Optional[AsyncNodesClient] = None
        self._preprint_providers: typing.Optional[AsyncPreprintProvidersClient] = None
        self._preprints: typing.Optional[AsyncPreprintsClient] = None
        self._registrations: typing.Optional[AsyncRegistrationsClient] = None
        self._schema_responses: typing.Optional[AsyncSchemaResponsesClient] = None
        self._schema_response_actions: typing.Optional[AsyncSchemaResponseActionsClient] = None
        self._registration_schema_blocks: typing.Optional[AsyncRegistrationSchemaBlocksClient] = None
        self._registration_schemas: typing.Optional[AsyncRegistrationSchemasClient] = None
        self._taxonomies: typing.Optional[AsyncTaxonomiesClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None
        self._view_only_links: typing.Optional[AsyncViewOnlyLinksClient] = None
        self._wikis: typing.Optional[AsyncWikisClient] = None

    @property
    def base(self):
        if self._base is None:
            from .base.client import AsyncBaseClient

            self._base = AsyncBaseClient(client_wrapper=self._client_wrapper)
        return self._base

    @property
    def logs(self):
        if self._logs is None:
            from .logs.client import AsyncLogsClient

            self._logs = AsyncLogsClient(client_wrapper=self._client_wrapper)
        return self._logs

    @property
    def addons(self):
        if self._addons is None:
            from .addons.client import AsyncAddonsClient

            self._addons = AsyncAddonsClient(client_wrapper=self._client_wrapper)
        return self._addons

    @property
    def citations(self):
        if self._citations is None:
            from .citations.client import AsyncCitationsClient

            self._citations = AsyncCitationsClient(client_wrapper=self._client_wrapper)
        return self._citations

    @property
    def collections(self):
        if self._collections is None:
            from .collections.client import AsyncCollectionsClient

            self._collections = AsyncCollectionsClient(client_wrapper=self._client_wrapper)
        return self._collections

    @property
    def comments(self):
        if self._comments is None:
            from .comments.client import AsyncCommentsClient

            self._comments = AsyncCommentsClient(client_wrapper=self._client_wrapper)
        return self._comments

    @property
    def draft_registrations(self):
        if self._draft_registrations is None:
            from .draft_registrations.client import AsyncDraftRegistrationsClient

            self._draft_registrations = AsyncDraftRegistrationsClient(client_wrapper=self._client_wrapper)
        return self._draft_registrations

    @property
    def files(self):
        if self._files is None:
            from .files.client import AsyncFilesClient

            self._files = AsyncFilesClient(client_wrapper=self._client_wrapper)
        return self._files

    @property
    def institutions(self):
        if self._institutions is None:
            from .institutions.client import AsyncInstitutionsClient

            self._institutions = AsyncInstitutionsClient(client_wrapper=self._client_wrapper)
        return self._institutions

    @property
    def licenses(self):
        if self._licenses is None:
            from .licenses.client import AsyncLicensesClient

            self._licenses = AsyncLicensesClient(client_wrapper=self._client_wrapper)
        return self._licenses

    @property
    def nodes(self):
        if self._nodes is None:
            from .nodes.client import AsyncNodesClient

            self._nodes = AsyncNodesClient(client_wrapper=self._client_wrapper)
        return self._nodes

    @property
    def preprint_providers(self):
        if self._preprint_providers is None:
            from .preprint_providers.client import AsyncPreprintProvidersClient

            self._preprint_providers = AsyncPreprintProvidersClient(client_wrapper=self._client_wrapper)
        return self._preprint_providers

    @property
    def preprints(self):
        if self._preprints is None:
            from .preprints.client import AsyncPreprintsClient

            self._preprints = AsyncPreprintsClient(client_wrapper=self._client_wrapper)
        return self._preprints

    @property
    def registrations(self):
        if self._registrations is None:
            from .registrations.client import AsyncRegistrationsClient

            self._registrations = AsyncRegistrationsClient(client_wrapper=self._client_wrapper)
        return self._registrations

    @property
    def schema_responses(self):
        if self._schema_responses is None:
            from .schema_responses.client import AsyncSchemaResponsesClient

            self._schema_responses = AsyncSchemaResponsesClient(client_wrapper=self._client_wrapper)
        return self._schema_responses

    @property
    def schema_response_actions(self):
        if self._schema_response_actions is None:
            from .schema_response_actions.client import AsyncSchemaResponseActionsClient

            self._schema_response_actions = AsyncSchemaResponseActionsClient(client_wrapper=self._client_wrapper)
        return self._schema_response_actions

    @property
    def registration_schema_blocks(self):
        if self._registration_schema_blocks is None:
            from .registration_schema_blocks.client import AsyncRegistrationSchemaBlocksClient

            self._registration_schema_blocks = AsyncRegistrationSchemaBlocksClient(client_wrapper=self._client_wrapper)
        return self._registration_schema_blocks

    @property
    def registration_schemas(self):
        if self._registration_schemas is None:
            from .registration_schemas.client import AsyncRegistrationSchemasClient

            self._registration_schemas = AsyncRegistrationSchemasClient(client_wrapper=self._client_wrapper)
        return self._registration_schemas

    @property
    def taxonomies(self):
        if self._taxonomies is None:
            from .taxonomies.client import AsyncTaxonomiesClient

            self._taxonomies = AsyncTaxonomiesClient(client_wrapper=self._client_wrapper)
        return self._taxonomies

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def view_only_links(self):
        if self._view_only_links is None:
            from .view_only_links.client import AsyncViewOnlyLinksClient

            self._view_only_links = AsyncViewOnlyLinksClient(client_wrapper=self._client_wrapper)
        return self._view_only_links

    @property
    def wikis(self):
        if self._wikis is None:
            from .wikis.client import AsyncWikisClient

            self._wikis = AsyncWikisClient(client_wrapper=self._client_wrapper)
        return self._wikis


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
