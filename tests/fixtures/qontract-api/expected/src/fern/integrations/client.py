

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cluster_namespaces import ClusterNamespaces
from ..types.gi_instance import GiInstance
from ..types.github_org_desired_state import GithubOrgDesiredState
from ..types.github_owners_task_response import GithubOwnersTaskResponse
from ..types.github_owners_task_result import GithubOwnersTaskResult
from ..types.glitchtip_instance import GlitchtipInstance
from ..types.glitchtip_project_alerts_task_response import GlitchtipProjectAlertsTaskResponse
from ..types.glitchtip_project_alerts_task_result import GlitchtipProjectAlertsTaskResult
from ..types.glitchtip_task_response import GlitchtipTaskResponse
from ..types.glitchtip_task_result import GlitchtipTaskResult
from ..types.keycloak_instance_secret import KeycloakInstanceSecret
from ..types.managed_sso_client_desired_state import ManagedSsoClientDesiredState
from ..types.managed_sso_client_task_response import ManagedSsoClientTaskResponse
from ..types.managed_sso_client_task_result import ManagedSsoClientTaskResult
from ..types.ocm_connection_params import OcmConnectionParams
from ..types.ocm_group_user import OcmGroupUser
from ..types.ocm_groups_cluster import OcmGroupsCluster
from ..types.ocm_groups_task_response import OcmGroupsTaskResponse
from ..types.ocm_groups_task_result import OcmGroupsTaskResult
from ..types.ocm_oidc_idp_cluster import OcmOidcIdpCluster
from ..types.ocm_oidc_idp_task_response import OcmOidcIdpTaskResponse
from ..types.ocm_oidc_idp_task_result import OcmOidcIdpTaskResult
from ..types.open_shift_namespaces_task_response import OpenShiftNamespacesTaskResponse
from ..types.open_shift_namespaces_task_result import OpenShiftNamespacesTaskResult
from ..types.quay_org_config import QuayOrgConfig
from ..types.quay_org_desired_state import QuayOrgDesiredState
from ..types.quay_repos_task_response import QuayReposTaskResponse
from ..types.quay_repos_task_result import QuayReposTaskResult
from ..types.quay_robot_accounts_task_response import QuayRobotAccountsTaskResponse
from ..types.quay_robot_accounts_task_result import QuayRobotAccountsTaskResult
from ..types.secret import Secret
from ..types.slack_usergroups_task_response import SlackUsergroupsTaskResponse
from ..types.slack_usergroups_task_result import SlackUsergroupsTaskResult
from ..types.slack_workspace import SlackWorkspace
from ..types.sso_client_cluster import SsoClientCluster
from ..types.sso_client_task_response import SsoClientTaskResponse
from ..types.sso_client_task_result import SsoClientTaskResult
from .raw_client import AsyncRawIntegrationsClient, RawIntegrationsClient


OMIT = typing.cast(typing.Any, ...)


class IntegrationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIntegrationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIntegrationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIntegrationsClient
        """
        return self._raw_client

    def github_owners(
        self,
        *,
        organizations: typing.Sequence[GithubOrgDesiredState],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GithubOwnersTaskResponse:
        """
        Queue a GitHub owners reconciliation task.

        This endpoint always queues a background task and returns immediately
        with a task_id. Use GET /reconcile/{task_id} to retrieve the result.

        Args:
            reconcile_request: Reconciliation request with desired owner state
            current_user: Authenticated user (from JWT token)
            request: FastAPI Request object (used to generate status_url)

        Returns:
            GithubOwnersTaskResponse with task_id and status_url

        Parameters
        ----------
        organizations : typing.Sequence[GithubOrgDesiredState]
            List of GitHub organizations with their desired owner membership

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GithubOwnersTaskResponse
            Successful Response

        Examples
        --------
        from fern import FernApi, GithubOrgDesiredState, Secret

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.github_owners(
            organizations=[
                GithubOrgDesiredState(
                    org_name="org_name",
                    owners=["owners"],
                    token=Secret(
                        path="path",
                        secret_manager_url="secret_manager_url",
                    ),
                )
            ],
        )
        """
        _response = self._raw_client.github_owners(
            organizations=organizations, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    def github_owners_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GithubOwnersTaskResult:
        """
        Retrieve the reconciliation result (blocking or non-blocking).

        **Non-blocking mode (default):** Returns immediate status (pending/success/failed)
        **Blocking mode (with timeout):** Waits up to timeout seconds, returns 408 if still pending

        Args:
            task_id: Task ID from POST /reconcile response
            current_user: Authenticated user (from JWT token)
            timeout: Maximum seconds to wait (default: None = non-blocking)

        Returns:
            GithubOwnersTaskResult with status, actions, applied_count, and errors

        Raises:
            HTTPException:
                - 404 Not Found: Task ID not found
                - 408 Request Timeout: Task still pending after timeout (blocking mode only)

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GithubOwnersTaskResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.github_owners_task_status(
            task_id="task_id",
        )
        """
        _response = self._raw_client.github_owners_task_status(
            task_id, timeout=timeout, request_options=request_options
        )
        return _response.data

    def glitchtip_project_alerts(
        self,
        *,
        instances: typing.Sequence[GlitchtipInstance],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GlitchtipProjectAlertsTaskResponse:
        """
        Queue Glitchtip project alerts reconciliation task.

        This endpoint always queues a background task and returns immediately
        with a task_id. Use GET /reconcile/{task_id} to retrieve the result.

        Args:
            reconcile_request: Reconciliation request with desired state
            current_user: Authenticated user (from JWT token)
            request: FastAPI Request object (used to generate status_url)

        Returns:
            GlitchtipProjectAlertsTaskResponse with task_id and status_url

        Parameters
        ----------
        instances : typing.Sequence[GlitchtipInstance]
            List of Glitchtip instances to reconcile

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlitchtipProjectAlertsTaskResponse
            Successful Response

        Examples
        --------
        from fern import FernApi, GlitchtipInstance, Secret

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.glitchtip_project_alerts(
            instances=[
                GlitchtipInstance(
                    console_url="console_url",
                    name="name",
                    token=Secret(
                        path="path",
                        secret_manager_url="secret_manager_url",
                    ),
                )
            ],
        )
        """
        _response = self._raw_client.glitchtip_project_alerts(
            instances=instances, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    def glitchtip_project_alerts_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GlitchtipProjectAlertsTaskResult:
        """
        Retrieve reconciliation result (blocking or non-blocking).

        **Non-blocking mode (default):** Returns immediate status (pending/success/failed)
        **Blocking mode (with timeout):** Waits up to timeout seconds, returns 408 if still pending

        Args:
            task_id: Task ID from POST /reconcile response
            current_user: Authenticated user (from JWT token)
            timeout: Maximum seconds to wait (default: None = non-blocking)

        Returns:
            GlitchtipProjectAlertsTaskResult with status, actions, applied_count, and errors

        Raises:
            HTTPException:
                - 404 Not Found: Task ID not found
                - 408 Request Timeout: Task still pending after timeout (blocking mode only)

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlitchtipProjectAlertsTaskResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.glitchtip_project_alerts_task_status(
            task_id="task_id",
        )
        """
        _response = self._raw_client.glitchtip_project_alerts_task_status(
            task_id, timeout=timeout, request_options=request_options
        )
        return _response.data

    def glitchtip(
        self,
        *,
        instances: typing.Sequence[GiInstance],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GlitchtipTaskResponse:
        """
        Queue Glitchtip reconciliation task.

        This endpoint always queues a background task and returns immediately
        with a task_id. Use GET /reconcile/{task_id} to retrieve the result.

        Args:
            reconcile_request: Reconciliation request with desired state
            current_user: Authenticated user (from JWT token)
            request: FastAPI Request object (used to generate status_url)

        Returns:
            GlitchtipTaskResponse with task_id and status_url

        Parameters
        ----------
        instances : typing.Sequence[GiInstance]
            List of Glitchtip instances to reconcile

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlitchtipTaskResponse
            Successful Response

        Examples
        --------
        from fern import FernApi, GiInstance, Secret

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.glitchtip(
            instances=[
                GiInstance(
                    automation_user_email=Secret(
                        path="path",
                        secret_manager_url="secret_manager_url",
                    ),
                    console_url="console_url",
                    name="name",
                    token=Secret(
                        path="path",
                        secret_manager_url="secret_manager_url",
                    ),
                )
            ],
        )
        """
        _response = self._raw_client.glitchtip(instances=instances, dry_run=dry_run, request_options=request_options)
        return _response.data

    def glitchtip_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GlitchtipTaskResult:
        """
        Retrieve reconciliation result (blocking or non-blocking).

        **Non-blocking mode (default):** Returns immediate status
        **Blocking mode (with timeout):** Waits up to timeout seconds

        Args:
            task_id: Task ID from POST /reconcile response
            current_user: Authenticated user (from JWT token)
            timeout: Maximum seconds to wait (default: None = non-blocking)

        Returns:
            GlitchtipTaskResult with status, actions, applied_count, and errors

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlitchtipTaskResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.glitchtip_task_status(
            task_id="task_id",
        )
        """
        _response = self._raw_client.glitchtip_task_status(task_id, timeout=timeout, request_options=request_options)
        return _response.data

    def managed_sso_client(
        self,
        *,
        desired_clients: typing.Sequence[ManagedSsoClientDesiredState],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ManagedSsoClientTaskResponse:
        """
        Queue a managed-sso-client reconciliation task.

        Parameters
        ----------
        desired_clients : typing.Sequence[ManagedSsoClientDesiredState]
            All tenant-declared managed SSO clients across app-interface

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ManagedSsoClientTaskResponse
            Successful Response

        Examples
        --------
        from fern import (
            FernApi,
            KeycloakInstanceRef,
            ManagedSsoClientDesiredState,
            Secret,
        )

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.managed_sso_client(
            desired_clients=[
                ManagedSsoClientDesiredState(
                    client_id="client_id",
                    keycloak_instance=KeycloakInstanceRef(
                        initial_access_token=Secret(
                            path="path",
                            secret_manager_url="secret_manager_url",
                        ),
                        url="url",
                    ),
                )
            ],
        )
        """
        _response = self._raw_client.managed_sso_client(
            desired_clients=desired_clients, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    def managed_sso_client_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ManagedSsoClientTaskResult:
        """
        Retrieve the reconciliation result (blocking or non-blocking).

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ManagedSsoClientTaskResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.managed_sso_client_task_status(
            task_id="task_id",
        )
        """
        _response = self._raw_client.managed_sso_client_task_status(
            task_id, timeout=timeout, request_options=request_options
        )
        return _response.data

    def ocm_groups(
        self,
        *,
        clusters: typing.Sequence[OcmGroupsCluster],
        desired_state: typing.Sequence[OcmGroupUser],
        ocm_connection: OcmConnectionParams,
        ocm_environment: str,
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OcmGroupsTaskResponse:
        """
        Queue OCM groups reconciliation task.

        This endpoint always queues a background task and returns immediately with a
        task_id. Use GET /reconcile/{task_id} to retrieve the result.

        Parameters
        ----------
        clusters : typing.Sequence[OcmGroupsCluster]
            Clusters with their managed groups

        desired_state : typing.Sequence[OcmGroupUser]
            Desired group memberships (from GraphQL roles)

        ocm_connection : OcmConnectionParams
            OCM connection details for cluster group CRUD

        ocm_environment : str
            OCM environment name (metric label only)

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OcmGroupsTaskResponse
            Successful Response

        Examples
        --------
        from fern import FernApi, OcmConnectionParams, OcmGroupsCluster, OcmGroupUser

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.ocm_groups(
            clusters=[
                OcmGroupsCluster(
                    cluster_id="cluster_id",
                    name="name",
                )
            ],
            desired_state=[
                OcmGroupUser(
                    cluster="cluster",
                    group="group",
                    user="user",
                )
            ],
            ocm_connection=OcmConnectionParams(
                access_token_client_id="access_token_client_id",
                access_token_url="access_token_url",
                ocm_url="ocm_url",
                path="path",
                secret_manager_url="secret_manager_url",
            ),
            ocm_environment="ocm_environment",
        )
        """
        _response = self._raw_client.ocm_groups(
            clusters=clusters,
            desired_state=desired_state,
            ocm_connection=ocm_connection,
            ocm_environment=ocm_environment,
            dry_run=dry_run,
            request_options=request_options,
        )
        return _response.data

    def ocm_groups_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OcmGroupsTaskResult:
        """
        Retrieve reconciliation result (blocking or non-blocking).

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OcmGroupsTaskResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.ocm_groups_task_status(
            task_id="task_id",
        )
        """
        _response = self._raw_client.ocm_groups_task_status(task_id, timeout=timeout, request_options=request_options)
        return _response.data

    def ocm_oidc_idp(
        self,
        *,
        clusters: typing.Sequence[OcmOidcIdpCluster],
        ocm_connection: OcmConnectionParams,
        ocm_environment: str,
        vault_target: Secret,
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OcmOidcIdpTaskResponse:
        """
        Queue OCM OIDC identity provider reconciliation task.

        This endpoint always queues a background task and returns immediately with a
        task_id. Use GET /reconcile/{task_id} to retrieve the result.

        Parameters
        ----------
        clusters : typing.Sequence[OcmOidcIdpCluster]
            All RHIDP-labeled clusters discovered for this environment

        ocm_connection : OcmConnectionParams
            OCM connection details, needed for identity provider CRUD

        ocm_environment : str
            OCM environment name (metric label only)

        vault_target : Secret
            Vault location sso_client stores per-cluster SSO client secrets under (field/version unused)

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OcmOidcIdpTaskResponse
            Successful Response

        Examples
        --------
        from fern import (
            FernApi,
            OcmConnectionParams,
            OcmOidcIdpAuth,
            OcmOidcIdpCluster,
            Secret,
        )

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.ocm_oidc_idp(
            clusters=[
                OcmOidcIdpCluster(
                    auth=OcmOidcIdpAuth(
                        enforced=True,
                        issuer="issuer",
                        name="name",
                        oidc_enabled=True,
                    ),
                    cluster_id="cluster_id",
                    name="name",
                    organization_id="organization_id",
                )
            ],
            ocm_connection=OcmConnectionParams(
                access_token_client_id="access_token_client_id",
                access_token_url="access_token_url",
                ocm_url="ocm_url",
                path="path",
                secret_manager_url="secret_manager_url",
            ),
            ocm_environment="ocm_environment",
            vault_target=Secret(
                path="path",
                secret_manager_url="secret_manager_url",
            ),
        )
        """
        _response = self._raw_client.ocm_oidc_idp(
            clusters=clusters,
            ocm_connection=ocm_connection,
            ocm_environment=ocm_environment,
            vault_target=vault_target,
            dry_run=dry_run,
            request_options=request_options,
        )
        return _response.data

    def ocm_oidc_idp_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OcmOidcIdpTaskResult:
        """
        Retrieve reconciliation result (blocking or non-blocking).

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OcmOidcIdpTaskResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.ocm_oidc_idp_task_status(
            task_id="task_id",
        )
        """
        _response = self._raw_client.ocm_oidc_idp_task_status(task_id, timeout=timeout, request_options=request_options)
        return _response.data

    def openshift_namespaces(
        self,
        *,
        clusters: typing.Sequence[ClusterNamespaces],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenShiftNamespacesTaskResponse:
        """
        Queue openshift-namespaces reconciliation task.

        Parameters
        ----------
        clusters : typing.Sequence[ClusterNamespaces]
            Clusters with desired namespaces

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenShiftNamespacesTaskResponse
            Successful Response

        Examples
        --------
        from fern import ClusterNamespaces, FernApi, Secret

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.openshift_namespaces(
            clusters=[
                ClusterNamespaces(
                    automation_token=Secret(
                        path="path",
                        secret_manager_url="secret_manager_url",
                    ),
                    cluster_name="cluster_name",
                    server_url="server_url",
                )
            ],
        )
        """
        _response = self._raw_client.openshift_namespaces(
            clusters=clusters, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    def openshift_namespaces_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenShiftNamespacesTaskResult:
        """
        Retrieve reconciliation result (blocking or non-blocking).

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenShiftNamespacesTaskResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.openshift_namespaces_task_status(
            task_id="task_id",
        )
        """
        _response = self._raw_client.openshift_namespaces_task_status(
            task_id, timeout=timeout, request_options=request_options
        )
        return _response.data

    def quay_repos(
        self,
        *,
        orgs: typing.Sequence[QuayOrgConfig],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QuayReposTaskResponse:
        """
        Queue Quay repos reconciliation task.

        Always queues a background task and returns immediately with a task_id.
        Use GET /reconcile/{task_id} to retrieve the result.

        Parameters
        ----------
        orgs : typing.Sequence[QuayOrgConfig]
            List of Quay organizations to reconcile

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QuayReposTaskResponse
            Successful Response

        Examples
        --------
        from fern import FernApi, QuayOrgConfig, Secret

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.quay_repos(
            orgs=[
                QuayOrgConfig(
                    automation_token=Secret(
                        path="path",
                        secret_manager_url="secret_manager_url",
                    ),
                    base_url="base_url",
                    instance="instance",
                    managed_repos=True,
                    org_name="org_name",
                )
            ],
        )
        """
        _response = self._raw_client.quay_repos(orgs=orgs, dry_run=dry_run, request_options=request_options)
        return _response.data

    def quay_repos_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QuayReposTaskResult:
        """
        Retrieve reconciliation result (blocking or non-blocking).

        Args:
            task_id: Task ID from POST /reconcile response
            timeout: Maximum seconds to wait (default: non-blocking)

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QuayReposTaskResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.quay_repos_task_status(
            task_id="task_id",
        )
        """
        _response = self._raw_client.quay_repos_task_status(task_id, timeout=timeout, request_options=request_options)
        return _response.data

    def quay_robot_accounts(
        self,
        *,
        organizations: typing.Sequence[QuayOrgDesiredState],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QuayRobotAccountsTaskResponse:
        """
        Queue a quay-robot-accounts reconciliation task.

        Parameters
        ----------
        organizations : typing.Sequence[QuayOrgDesiredState]
            Quay organizations with desired robot-account state

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QuayRobotAccountsTaskResponse
            Successful Response

        Examples
        --------
        from fern import FernApi, QuayOrgDesiredState, Secret

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.quay_robot_accounts(
            organizations=[
                QuayOrgDesiredState(
                    instance_name="instance_name",
                    instance_url="instance_url",
                    org_name="org_name",
                    token=Secret(
                        path="path",
                        secret_manager_url="secret_manager_url",
                    ),
                )
            ],
        )
        """
        _response = self._raw_client.quay_robot_accounts(
            organizations=organizations, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    def quay_robot_accounts_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QuayRobotAccountsTaskResult:
        """
        Retrieve the reconciliation result (blocking or non-blocking).

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QuayRobotAccountsTaskResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.quay_robot_accounts_task_status(
            task_id="task_id",
        )
        """
        _response = self._raw_client.quay_robot_accounts_task_status(
            task_id, timeout=timeout, request_options=request_options
        )
        return _response.data

    def slack_usergroups(
        self,
        *,
        workspaces: typing.Sequence[SlackWorkspace],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SlackUsergroupsTaskResponse:
        """
        Queue Slack usergroups reconciliation task.

        This endpoint always queues a background task and returns immediately
        with a task_id. Use GET /reconcile/{task_id} to retrieve the result.

        Args:
            reconcile_request: Reconciliation request with desired state
            current_user: Authenticated user (from JWT token)
            request: FastAPI Request object (used to generate status_url)

        Returns:
            SlackUsergroupsTaskResponse with task_id and status_url

        Parameters
        ----------
        workspaces : typing.Sequence[SlackWorkspace]
            List of Slack workspaces with their usergroups

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SlackUsergroupsTaskResponse
            Successful Response

        Examples
        --------
        from fern import (
            FernApi,
            Secret,
            SlackUsergroup,
            SlackUsergroupConfig,
            SlackWorkspace,
        )

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.slack_usergroups(
            workspaces=[
                SlackWorkspace(
                    managed_usergroups=["managed_usergroups"],
                    name="name",
                    token=Secret(
                        path="path",
                        secret_manager_url="secret_manager_url",
                    ),
                    usergroups=[
                        SlackUsergroup(
                            config=SlackUsergroupConfig(),
                            handle="handle",
                        )
                    ],
                )
            ],
        )
        """
        _response = self._raw_client.slack_usergroups(
            workspaces=workspaces, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    def slack_usergroups_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SlackUsergroupsTaskResult:
        """
        Retrieve reconciliation result (blocking or non-blocking).

        **Non-blocking mode (default):** Returns immediate status (pending/success/failed)
        **Blocking mode (with timeout):** Waits up to timeout seconds, returns 408 if still pending

        Args:
            task_id: Task ID from POST /reconcile response
            current_user: Authenticated user (from JWT token)
            timeout: Maximum seconds to wait (default: None = non-blocking)

        Returns:
            SlackUsergroupsTaskResult with status, actions, applied_count, and errors

        Raises:
            HTTPException:
                - 404 Not Found: Task ID not found
                - 408 Request Timeout: Task still pending after timeout (blocking mode only)

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SlackUsergroupsTaskResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.slack_usergroups_task_status(
            task_id="task_id",
        )
        """
        _response = self._raw_client.slack_usergroups_task_status(
            task_id, timeout=timeout, request_options=request_options
        )
        return _response.data

    def sso_client(
        self,
        *,
        clusters: typing.Sequence[SsoClientCluster],
        keycloak_secrets: typing.Sequence[KeycloakInstanceSecret],
        ocm_environment: str,
        vault_target: Secret,
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SsoClientTaskResponse:
        """
        Queue RHIDP SSO client reconciliation task.

        This endpoint always queues a background task and returns immediately with a
        task_id. Use GET /reconcile/{task_id} to retrieve the result.

        Parameters
        ----------
        clusters : typing.Sequence[SsoClientCluster]
            All RHIDP-labeled clusters discovered for this environment

        keycloak_secrets : typing.Sequence[KeycloakInstanceSecret]
            One entry per Keycloak instance (issuer URL + its Vault IAT secret reference)

        ocm_environment : str
            OCM environment name (metric label only)

        vault_target : Secret
            Vault location to store/list/delete SSO client secrets under (field/version unused)

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SsoClientTaskResponse
            Successful Response

        Examples
        --------
        from fern import (
            FernApi,
            KeycloakInstanceSecret,
            Secret,
            SsoClientAuth,
            SsoClientCluster,
        )

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.sso_client(
            clusters=[
                SsoClientCluster(
                    auth=SsoClientAuth(
                        issuer="issuer",
                        name="name",
                    ),
                    name="name",
                    organization_id="organization_id",
                    rhidp_enabled=True,
                )
            ],
            keycloak_secrets=[
                KeycloakInstanceSecret(
                    secret=Secret(
                        path="path",
                        secret_manager_url="secret_manager_url",
                    ),
                    url="url",
                )
            ],
            ocm_environment="ocm_environment",
            vault_target=Secret(
                path="path",
                secret_manager_url="secret_manager_url",
            ),
        )
        """
        _response = self._raw_client.sso_client(
            clusters=clusters,
            keycloak_secrets=keycloak_secrets,
            ocm_environment=ocm_environment,
            vault_target=vault_target,
            dry_run=dry_run,
            request_options=request_options,
        )
        return _response.data

    def sso_client_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SsoClientTaskResult:
        """
        Retrieve reconciliation result (blocking or non-blocking).

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SsoClientTaskResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.integrations.sso_client_task_status(
            task_id="task_id",
        )
        """
        _response = self._raw_client.sso_client_task_status(task_id, timeout=timeout, request_options=request_options)
        return _response.data


class AsyncIntegrationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIntegrationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIntegrationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIntegrationsClient
        """
        return self._raw_client

    async def github_owners(
        self,
        *,
        organizations: typing.Sequence[GithubOrgDesiredState],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GithubOwnersTaskResponse:
        """
        Queue a GitHub owners reconciliation task.

        This endpoint always queues a background task and returns immediately
        with a task_id. Use GET /reconcile/{task_id} to retrieve the result.

        Args:
            reconcile_request: Reconciliation request with desired owner state
            current_user: Authenticated user (from JWT token)
            request: FastAPI Request object (used to generate status_url)

        Returns:
            GithubOwnersTaskResponse with task_id and status_url

        Parameters
        ----------
        organizations : typing.Sequence[GithubOrgDesiredState]
            List of GitHub organizations with their desired owner membership

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GithubOwnersTaskResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GithubOrgDesiredState, Secret

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.github_owners(
                organizations=[
                    GithubOrgDesiredState(
                        org_name="org_name",
                        owners=["owners"],
                        token=Secret(
                            path="path",
                            secret_manager_url="secret_manager_url",
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.github_owners(
            organizations=organizations, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    async def github_owners_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GithubOwnersTaskResult:
        """
        Retrieve the reconciliation result (blocking or non-blocking).

        **Non-blocking mode (default):** Returns immediate status (pending/success/failed)
        **Blocking mode (with timeout):** Waits up to timeout seconds, returns 408 if still pending

        Args:
            task_id: Task ID from POST /reconcile response
            current_user: Authenticated user (from JWT token)
            timeout: Maximum seconds to wait (default: None = non-blocking)

        Returns:
            GithubOwnersTaskResult with status, actions, applied_count, and errors

        Raises:
            HTTPException:
                - 404 Not Found: Task ID not found
                - 408 Request Timeout: Task still pending after timeout (blocking mode only)

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GithubOwnersTaskResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.github_owners_task_status(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.github_owners_task_status(
            task_id, timeout=timeout, request_options=request_options
        )
        return _response.data

    async def glitchtip_project_alerts(
        self,
        *,
        instances: typing.Sequence[GlitchtipInstance],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GlitchtipProjectAlertsTaskResponse:
        """
        Queue Glitchtip project alerts reconciliation task.

        This endpoint always queues a background task and returns immediately
        with a task_id. Use GET /reconcile/{task_id} to retrieve the result.

        Args:
            reconcile_request: Reconciliation request with desired state
            current_user: Authenticated user (from JWT token)
            request: FastAPI Request object (used to generate status_url)

        Returns:
            GlitchtipProjectAlertsTaskResponse with task_id and status_url

        Parameters
        ----------
        instances : typing.Sequence[GlitchtipInstance]
            List of Glitchtip instances to reconcile

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlitchtipProjectAlertsTaskResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GlitchtipInstance, Secret

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.glitchtip_project_alerts(
                instances=[
                    GlitchtipInstance(
                        console_url="console_url",
                        name="name",
                        token=Secret(
                            path="path",
                            secret_manager_url="secret_manager_url",
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.glitchtip_project_alerts(
            instances=instances, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    async def glitchtip_project_alerts_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GlitchtipProjectAlertsTaskResult:
        """
        Retrieve reconciliation result (blocking or non-blocking).

        **Non-blocking mode (default):** Returns immediate status (pending/success/failed)
        **Blocking mode (with timeout):** Waits up to timeout seconds, returns 408 if still pending

        Args:
            task_id: Task ID from POST /reconcile response
            current_user: Authenticated user (from JWT token)
            timeout: Maximum seconds to wait (default: None = non-blocking)

        Returns:
            GlitchtipProjectAlertsTaskResult with status, actions, applied_count, and errors

        Raises:
            HTTPException:
                - 404 Not Found: Task ID not found
                - 408 Request Timeout: Task still pending after timeout (blocking mode only)

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlitchtipProjectAlertsTaskResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.glitchtip_project_alerts_task_status(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.glitchtip_project_alerts_task_status(
            task_id, timeout=timeout, request_options=request_options
        )
        return _response.data

    async def glitchtip(
        self,
        *,
        instances: typing.Sequence[GiInstance],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GlitchtipTaskResponse:
        """
        Queue Glitchtip reconciliation task.

        This endpoint always queues a background task and returns immediately
        with a task_id. Use GET /reconcile/{task_id} to retrieve the result.

        Args:
            reconcile_request: Reconciliation request with desired state
            current_user: Authenticated user (from JWT token)
            request: FastAPI Request object (used to generate status_url)

        Returns:
            GlitchtipTaskResponse with task_id and status_url

        Parameters
        ----------
        instances : typing.Sequence[GiInstance]
            List of Glitchtip instances to reconcile

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlitchtipTaskResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GiInstance, Secret

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.glitchtip(
                instances=[
                    GiInstance(
                        automation_user_email=Secret(
                            path="path",
                            secret_manager_url="secret_manager_url",
                        ),
                        console_url="console_url",
                        name="name",
                        token=Secret(
                            path="path",
                            secret_manager_url="secret_manager_url",
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.glitchtip(
            instances=instances, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    async def glitchtip_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GlitchtipTaskResult:
        """
        Retrieve reconciliation result (blocking or non-blocking).

        **Non-blocking mode (default):** Returns immediate status
        **Blocking mode (with timeout):** Waits up to timeout seconds

        Args:
            task_id: Task ID from POST /reconcile response
            current_user: Authenticated user (from JWT token)
            timeout: Maximum seconds to wait (default: None = non-blocking)

        Returns:
            GlitchtipTaskResult with status, actions, applied_count, and errors

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlitchtipTaskResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.glitchtip_task_status(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.glitchtip_task_status(
            task_id, timeout=timeout, request_options=request_options
        )
        return _response.data

    async def managed_sso_client(
        self,
        *,
        desired_clients: typing.Sequence[ManagedSsoClientDesiredState],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ManagedSsoClientTaskResponse:
        """
        Queue a managed-sso-client reconciliation task.

        Parameters
        ----------
        desired_clients : typing.Sequence[ManagedSsoClientDesiredState]
            All tenant-declared managed SSO clients across app-interface

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ManagedSsoClientTaskResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            KeycloakInstanceRef,
            ManagedSsoClientDesiredState,
            Secret,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.managed_sso_client(
                desired_clients=[
                    ManagedSsoClientDesiredState(
                        client_id="client_id",
                        keycloak_instance=KeycloakInstanceRef(
                            initial_access_token=Secret(
                                path="path",
                                secret_manager_url="secret_manager_url",
                            ),
                            url="url",
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.managed_sso_client(
            desired_clients=desired_clients, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    async def managed_sso_client_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ManagedSsoClientTaskResult:
        """
        Retrieve the reconciliation result (blocking or non-blocking).

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ManagedSsoClientTaskResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.managed_sso_client_task_status(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.managed_sso_client_task_status(
            task_id, timeout=timeout, request_options=request_options
        )
        return _response.data

    async def ocm_groups(
        self,
        *,
        clusters: typing.Sequence[OcmGroupsCluster],
        desired_state: typing.Sequence[OcmGroupUser],
        ocm_connection: OcmConnectionParams,
        ocm_environment: str,
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OcmGroupsTaskResponse:
        """
        Queue OCM groups reconciliation task.

        This endpoint always queues a background task and returns immediately with a
        task_id. Use GET /reconcile/{task_id} to retrieve the result.

        Parameters
        ----------
        clusters : typing.Sequence[OcmGroupsCluster]
            Clusters with their managed groups

        desired_state : typing.Sequence[OcmGroupUser]
            Desired group memberships (from GraphQL roles)

        ocm_connection : OcmConnectionParams
            OCM connection details for cluster group CRUD

        ocm_environment : str
            OCM environment name (metric label only)

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OcmGroupsTaskResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            OcmConnectionParams,
            OcmGroupsCluster,
            OcmGroupUser,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.ocm_groups(
                clusters=[
                    OcmGroupsCluster(
                        cluster_id="cluster_id",
                        name="name",
                    )
                ],
                desired_state=[
                    OcmGroupUser(
                        cluster="cluster",
                        group="group",
                        user="user",
                    )
                ],
                ocm_connection=OcmConnectionParams(
                    access_token_client_id="access_token_client_id",
                    access_token_url="access_token_url",
                    ocm_url="ocm_url",
                    path="path",
                    secret_manager_url="secret_manager_url",
                ),
                ocm_environment="ocm_environment",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ocm_groups(
            clusters=clusters,
            desired_state=desired_state,
            ocm_connection=ocm_connection,
            ocm_environment=ocm_environment,
            dry_run=dry_run,
            request_options=request_options,
        )
        return _response.data

    async def ocm_groups_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OcmGroupsTaskResult:
        """
        Retrieve reconciliation result (blocking or non-blocking).

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OcmGroupsTaskResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.ocm_groups_task_status(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ocm_groups_task_status(
            task_id, timeout=timeout, request_options=request_options
        )
        return _response.data

    async def ocm_oidc_idp(
        self,
        *,
        clusters: typing.Sequence[OcmOidcIdpCluster],
        ocm_connection: OcmConnectionParams,
        ocm_environment: str,
        vault_target: Secret,
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OcmOidcIdpTaskResponse:
        """
        Queue OCM OIDC identity provider reconciliation task.

        This endpoint always queues a background task and returns immediately with a
        task_id. Use GET /reconcile/{task_id} to retrieve the result.

        Parameters
        ----------
        clusters : typing.Sequence[OcmOidcIdpCluster]
            All RHIDP-labeled clusters discovered for this environment

        ocm_connection : OcmConnectionParams
            OCM connection details, needed for identity provider CRUD

        ocm_environment : str
            OCM environment name (metric label only)

        vault_target : Secret
            Vault location sso_client stores per-cluster SSO client secrets under (field/version unused)

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OcmOidcIdpTaskResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            OcmConnectionParams,
            OcmOidcIdpAuth,
            OcmOidcIdpCluster,
            Secret,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.ocm_oidc_idp(
                clusters=[
                    OcmOidcIdpCluster(
                        auth=OcmOidcIdpAuth(
                            enforced=True,
                            issuer="issuer",
                            name="name",
                            oidc_enabled=True,
                        ),
                        cluster_id="cluster_id",
                        name="name",
                        organization_id="organization_id",
                    )
                ],
                ocm_connection=OcmConnectionParams(
                    access_token_client_id="access_token_client_id",
                    access_token_url="access_token_url",
                    ocm_url="ocm_url",
                    path="path",
                    secret_manager_url="secret_manager_url",
                ),
                ocm_environment="ocm_environment",
                vault_target=Secret(
                    path="path",
                    secret_manager_url="secret_manager_url",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ocm_oidc_idp(
            clusters=clusters,
            ocm_connection=ocm_connection,
            ocm_environment=ocm_environment,
            vault_target=vault_target,
            dry_run=dry_run,
            request_options=request_options,
        )
        return _response.data

    async def ocm_oidc_idp_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OcmOidcIdpTaskResult:
        """
        Retrieve reconciliation result (blocking or non-blocking).

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OcmOidcIdpTaskResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.ocm_oidc_idp_task_status(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ocm_oidc_idp_task_status(
            task_id, timeout=timeout, request_options=request_options
        )
        return _response.data

    async def openshift_namespaces(
        self,
        *,
        clusters: typing.Sequence[ClusterNamespaces],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenShiftNamespacesTaskResponse:
        """
        Queue openshift-namespaces reconciliation task.

        Parameters
        ----------
        clusters : typing.Sequence[ClusterNamespaces]
            Clusters with desired namespaces

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenShiftNamespacesTaskResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ClusterNamespaces, Secret

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.openshift_namespaces(
                clusters=[
                    ClusterNamespaces(
                        automation_token=Secret(
                            path="path",
                            secret_manager_url="secret_manager_url",
                        ),
                        cluster_name="cluster_name",
                        server_url="server_url",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.openshift_namespaces(
            clusters=clusters, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    async def openshift_namespaces_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenShiftNamespacesTaskResult:
        """
        Retrieve reconciliation result (blocking or non-blocking).

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenShiftNamespacesTaskResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.openshift_namespaces_task_status(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.openshift_namespaces_task_status(
            task_id, timeout=timeout, request_options=request_options
        )
        return _response.data

    async def quay_repos(
        self,
        *,
        orgs: typing.Sequence[QuayOrgConfig],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QuayReposTaskResponse:
        """
        Queue Quay repos reconciliation task.

        Always queues a background task and returns immediately with a task_id.
        Use GET /reconcile/{task_id} to retrieve the result.

        Parameters
        ----------
        orgs : typing.Sequence[QuayOrgConfig]
            List of Quay organizations to reconcile

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QuayReposTaskResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, QuayOrgConfig, Secret

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.quay_repos(
                orgs=[
                    QuayOrgConfig(
                        automation_token=Secret(
                            path="path",
                            secret_manager_url="secret_manager_url",
                        ),
                        base_url="base_url",
                        instance="instance",
                        managed_repos=True,
                        org_name="org_name",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.quay_repos(orgs=orgs, dry_run=dry_run, request_options=request_options)
        return _response.data

    async def quay_repos_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QuayReposTaskResult:
        """
        Retrieve reconciliation result (blocking or non-blocking).

        Args:
            task_id: Task ID from POST /reconcile response
            timeout: Maximum seconds to wait (default: non-blocking)

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QuayReposTaskResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.quay_repos_task_status(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.quay_repos_task_status(
            task_id, timeout=timeout, request_options=request_options
        )
        return _response.data

    async def quay_robot_accounts(
        self,
        *,
        organizations: typing.Sequence[QuayOrgDesiredState],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QuayRobotAccountsTaskResponse:
        """
        Queue a quay-robot-accounts reconciliation task.

        Parameters
        ----------
        organizations : typing.Sequence[QuayOrgDesiredState]
            Quay organizations with desired robot-account state

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QuayRobotAccountsTaskResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, QuayOrgDesiredState, Secret

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.quay_robot_accounts(
                organizations=[
                    QuayOrgDesiredState(
                        instance_name="instance_name",
                        instance_url="instance_url",
                        org_name="org_name",
                        token=Secret(
                            path="path",
                            secret_manager_url="secret_manager_url",
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.quay_robot_accounts(
            organizations=organizations, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    async def quay_robot_accounts_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QuayRobotAccountsTaskResult:
        """
        Retrieve the reconciliation result (blocking or non-blocking).

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QuayRobotAccountsTaskResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.quay_robot_accounts_task_status(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.quay_robot_accounts_task_status(
            task_id, timeout=timeout, request_options=request_options
        )
        return _response.data

    async def slack_usergroups(
        self,
        *,
        workspaces: typing.Sequence[SlackWorkspace],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SlackUsergroupsTaskResponse:
        """
        Queue Slack usergroups reconciliation task.

        This endpoint always queues a background task and returns immediately
        with a task_id. Use GET /reconcile/{task_id} to retrieve the result.

        Args:
            reconcile_request: Reconciliation request with desired state
            current_user: Authenticated user (from JWT token)
            request: FastAPI Request object (used to generate status_url)

        Returns:
            SlackUsergroupsTaskResponse with task_id and status_url

        Parameters
        ----------
        workspaces : typing.Sequence[SlackWorkspace]
            List of Slack workspaces with their usergroups

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SlackUsergroupsTaskResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            Secret,
            SlackUsergroup,
            SlackUsergroupConfig,
            SlackWorkspace,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.slack_usergroups(
                workspaces=[
                    SlackWorkspace(
                        managed_usergroups=["managed_usergroups"],
                        name="name",
                        token=Secret(
                            path="path",
                            secret_manager_url="secret_manager_url",
                        ),
                        usergroups=[
                            SlackUsergroup(
                                config=SlackUsergroupConfig(),
                                handle="handle",
                            )
                        ],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slack_usergroups(
            workspaces=workspaces, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    async def slack_usergroups_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SlackUsergroupsTaskResult:
        """
        Retrieve reconciliation result (blocking or non-blocking).

        **Non-blocking mode (default):** Returns immediate status (pending/success/failed)
        **Blocking mode (with timeout):** Waits up to timeout seconds, returns 408 if still pending

        Args:
            task_id: Task ID from POST /reconcile response
            current_user: Authenticated user (from JWT token)
            timeout: Maximum seconds to wait (default: None = non-blocking)

        Returns:
            SlackUsergroupsTaskResult with status, actions, applied_count, and errors

        Raises:
            HTTPException:
                - 404 Not Found: Task ID not found
                - 408 Request Timeout: Task still pending after timeout (blocking mode only)

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SlackUsergroupsTaskResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.slack_usergroups_task_status(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slack_usergroups_task_status(
            task_id, timeout=timeout, request_options=request_options
        )
        return _response.data

    async def sso_client(
        self,
        *,
        clusters: typing.Sequence[SsoClientCluster],
        keycloak_secrets: typing.Sequence[KeycloakInstanceSecret],
        ocm_environment: str,
        vault_target: Secret,
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SsoClientTaskResponse:
        """
        Queue RHIDP SSO client reconciliation task.

        This endpoint always queues a background task and returns immediately with a
        task_id. Use GET /reconcile/{task_id} to retrieve the result.

        Parameters
        ----------
        clusters : typing.Sequence[SsoClientCluster]
            All RHIDP-labeled clusters discovered for this environment

        keycloak_secrets : typing.Sequence[KeycloakInstanceSecret]
            One entry per Keycloak instance (issuer URL + its Vault IAT secret reference)

        ocm_environment : str
            OCM environment name (metric label only)

        vault_target : Secret
            Vault location to store/list/delete SSO client secrets under (field/version unused)

        dry_run : typing.Optional[bool]
            If True, only calculate actions without executing. Default: True (safety first!)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SsoClientTaskResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            KeycloakInstanceSecret,
            Secret,
            SsoClientAuth,
            SsoClientCluster,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.sso_client(
                clusters=[
                    SsoClientCluster(
                        auth=SsoClientAuth(
                            issuer="issuer",
                            name="name",
                        ),
                        name="name",
                        organization_id="organization_id",
                        rhidp_enabled=True,
                    )
                ],
                keycloak_secrets=[
                    KeycloakInstanceSecret(
                        secret=Secret(
                            path="path",
                            secret_manager_url="secret_manager_url",
                        ),
                        url="url",
                    )
                ],
                ocm_environment="ocm_environment",
                vault_target=Secret(
                    path="path",
                    secret_manager_url="secret_manager_url",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sso_client(
            clusters=clusters,
            keycloak_secrets=keycloak_secrets,
            ocm_environment=ocm_environment,
            vault_target=vault_target,
            dry_run=dry_run,
            request_options=request_options,
        )
        return _response.data

    async def sso_client_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SsoClientTaskResult:
        """
        Retrieve reconciliation result (blocking or non-blocking).

        Parameters
        ----------
        task_id : str

        timeout : typing.Optional[int]
            Optional: Block up to N seconds for completion. Omit for immediate status check.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SsoClientTaskResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.integrations.sso_client_task_status(
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sso_client_task_status(
            task_id, timeout=timeout, request_options=request_options
        )
        return _response.data
