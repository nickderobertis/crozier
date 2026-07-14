

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .admin.client import AdminClient, AsyncAdminClient
    from .artifact_rules.client import ArtifactRulesClient, AsyncArtifactRulesClient
    from .artifact_type.client import ArtifactTypeClient, AsyncArtifactTypeClient
    from .artifacts.client import ArtifactsClient, AsyncArtifactsClient
    from .global_rules.client import AsyncGlobalRulesClient, GlobalRulesClient
    from .groups.client import AsyncGroupsClient, GroupsClient
    from .metadata.client import AsyncMetadataClient, MetadataClient
    from .search.client import AsyncSearchClient, SearchClient
    from .system.client import AsyncSystemClient, SystemClient
    from .users.client import AsyncUsersClient, UsersClient
    from .versions.client import AsyncVersionsClient, VersionsClient


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

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

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
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._artifact_type: typing.Optional[ArtifactTypeClient] = None
        self._admin: typing.Optional[AdminClient] = None
        self._global_rules: typing.Optional[GlobalRulesClient] = None
        self._groups: typing.Optional[GroupsClient] = None
        self._artifacts: typing.Optional[ArtifactsClient] = None
        self._metadata: typing.Optional[MetadataClient] = None
        self._artifact_rules: typing.Optional[ArtifactRulesClient] = None
        self._versions: typing.Optional[VersionsClient] = None
        self._search: typing.Optional[SearchClient] = None
        self._system: typing.Optional[SystemClient] = None
        self._users: typing.Optional[UsersClient] = None

    @property
    def artifact_type(self):
        if self._artifact_type is None:
            from .artifact_type.client import ArtifactTypeClient

            self._artifact_type = ArtifactTypeClient(client_wrapper=self._client_wrapper)
        return self._artifact_type

    @property
    def admin(self):
        if self._admin is None:
            from .admin.client import AdminClient

            self._admin = AdminClient(client_wrapper=self._client_wrapper)
        return self._admin

    @property
    def global_rules(self):
        if self._global_rules is None:
            from .global_rules.client import GlobalRulesClient

            self._global_rules = GlobalRulesClient(client_wrapper=self._client_wrapper)
        return self._global_rules

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import GroupsClient

            self._groups = GroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def artifacts(self):
        if self._artifacts is None:
            from .artifacts.client import ArtifactsClient

            self._artifacts = ArtifactsClient(client_wrapper=self._client_wrapper)
        return self._artifacts

    @property
    def metadata(self):
        if self._metadata is None:
            from .metadata.client import MetadataClient

            self._metadata = MetadataClient(client_wrapper=self._client_wrapper)
        return self._metadata

    @property
    def artifact_rules(self):
        if self._artifact_rules is None:
            from .artifact_rules.client import ArtifactRulesClient

            self._artifact_rules = ArtifactRulesClient(client_wrapper=self._client_wrapper)
        return self._artifact_rules

    @property
    def versions(self):
        if self._versions is None:
            from .versions.client import VersionsClient

            self._versions = VersionsClient(client_wrapper=self._client_wrapper)
        return self._versions

    @property
    def search(self):
        if self._search is None:
            from .search.client import SearchClient

            self._search = SearchClient(client_wrapper=self._client_wrapper)
        return self._search

    @property
    def system(self):
        if self._system is None:
            from .system.client import SystemClient

            self._system = SystemClient(client_wrapper=self._client_wrapper)
        return self._system

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users


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

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

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
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._artifact_type: typing.Optional[AsyncArtifactTypeClient] = None
        self._admin: typing.Optional[AsyncAdminClient] = None
        self._global_rules: typing.Optional[AsyncGlobalRulesClient] = None
        self._groups: typing.Optional[AsyncGroupsClient] = None
        self._artifacts: typing.Optional[AsyncArtifactsClient] = None
        self._metadata: typing.Optional[AsyncMetadataClient] = None
        self._artifact_rules: typing.Optional[AsyncArtifactRulesClient] = None
        self._versions: typing.Optional[AsyncVersionsClient] = None
        self._search: typing.Optional[AsyncSearchClient] = None
        self._system: typing.Optional[AsyncSystemClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None

    @property
    def artifact_type(self):
        if self._artifact_type is None:
            from .artifact_type.client import AsyncArtifactTypeClient

            self._artifact_type = AsyncArtifactTypeClient(client_wrapper=self._client_wrapper)
        return self._artifact_type

    @property
    def admin(self):
        if self._admin is None:
            from .admin.client import AsyncAdminClient

            self._admin = AsyncAdminClient(client_wrapper=self._client_wrapper)
        return self._admin

    @property
    def global_rules(self):
        if self._global_rules is None:
            from .global_rules.client import AsyncGlobalRulesClient

            self._global_rules = AsyncGlobalRulesClient(client_wrapper=self._client_wrapper)
        return self._global_rules

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import AsyncGroupsClient

            self._groups = AsyncGroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def artifacts(self):
        if self._artifacts is None:
            from .artifacts.client import AsyncArtifactsClient

            self._artifacts = AsyncArtifactsClient(client_wrapper=self._client_wrapper)
        return self._artifacts

    @property
    def metadata(self):
        if self._metadata is None:
            from .metadata.client import AsyncMetadataClient

            self._metadata = AsyncMetadataClient(client_wrapper=self._client_wrapper)
        return self._metadata

    @property
    def artifact_rules(self):
        if self._artifact_rules is None:
            from .artifact_rules.client import AsyncArtifactRulesClient

            self._artifact_rules = AsyncArtifactRulesClient(client_wrapper=self._client_wrapper)
        return self._artifact_rules

    @property
    def versions(self):
        if self._versions is None:
            from .versions.client import AsyncVersionsClient

            self._versions = AsyncVersionsClient(client_wrapper=self._client_wrapper)
        return self._versions

    @property
    def search(self):
        if self._search is None:
            from .search.client import AsyncSearchClient

            self._search = AsyncSearchClient(client_wrapper=self._client_wrapper)
        return self._search

    @property
    def system(self):
        if self._system is None:
            from .system.client import AsyncSystemClient

            self._system = AsyncSystemClient(client_wrapper=self._client_wrapper)
        return self._system

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
