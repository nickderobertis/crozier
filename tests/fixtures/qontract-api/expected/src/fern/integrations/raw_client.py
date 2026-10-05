

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIntegrationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def github_owners(
        self,
        *,
        organizations: typing.Sequence[GithubOrgDesiredState],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GithubOwnersTaskResponse]:
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
        HttpResponse[GithubOwnersTaskResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/integrations/github-owners/reconcile",
            method="POST",
            json={
                "dry_run": dry_run,
                "organizations": convert_and_respect_annotation_metadata(
                    object_=organizations, annotation=typing.Sequence[GithubOrgDesiredState], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GithubOwnersTaskResponse,
                    parse_obj_as(
                        type_=GithubOwnersTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def github_owners_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GithubOwnersTaskResult]:
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
        HttpResponse[GithubOwnersTaskResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/github-owners/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GithubOwnersTaskResult,
                    parse_obj_as(
                        type_=GithubOwnersTaskResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def glitchtip_project_alerts(
        self,
        *,
        instances: typing.Sequence[GlitchtipInstance],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GlitchtipProjectAlertsTaskResponse]:
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
        HttpResponse[GlitchtipProjectAlertsTaskResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/integrations/glitchtip-project-alerts/reconcile",
            method="POST",
            json={
                "dry_run": dry_run,
                "instances": convert_and_respect_annotation_metadata(
                    object_=instances, annotation=typing.Sequence[GlitchtipInstance], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlitchtipProjectAlertsTaskResponse,
                    parse_obj_as(
                        type_=GlitchtipProjectAlertsTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def glitchtip_project_alerts_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GlitchtipProjectAlertsTaskResult]:
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
        HttpResponse[GlitchtipProjectAlertsTaskResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/glitchtip-project-alerts/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlitchtipProjectAlertsTaskResult,
                    parse_obj_as(
                        type_=GlitchtipProjectAlertsTaskResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def glitchtip(
        self,
        *,
        instances: typing.Sequence[GiInstance],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GlitchtipTaskResponse]:
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
        HttpResponse[GlitchtipTaskResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/integrations/glitchtip/reconcile",
            method="POST",
            json={
                "dry_run": dry_run,
                "instances": convert_and_respect_annotation_metadata(
                    object_=instances, annotation=typing.Sequence[GiInstance], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlitchtipTaskResponse,
                    parse_obj_as(
                        type_=GlitchtipTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def glitchtip_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GlitchtipTaskResult]:
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
        HttpResponse[GlitchtipTaskResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/glitchtip/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlitchtipTaskResult,
                    parse_obj_as(
                        type_=GlitchtipTaskResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def managed_sso_client(
        self,
        *,
        desired_clients: typing.Sequence[ManagedSsoClientDesiredState],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ManagedSsoClientTaskResponse]:
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
        HttpResponse[ManagedSsoClientTaskResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/integrations/managed-sso-client/reconcile",
            method="POST",
            json={
                "desired_clients": convert_and_respect_annotation_metadata(
                    object_=desired_clients, annotation=typing.Sequence[ManagedSsoClientDesiredState], direction="write"
                ),
                "dry_run": dry_run,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ManagedSsoClientTaskResponse,
                    parse_obj_as(
                        type_=ManagedSsoClientTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def managed_sso_client_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ManagedSsoClientTaskResult]:
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
        HttpResponse[ManagedSsoClientTaskResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/managed-sso-client/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ManagedSsoClientTaskResult,
                    parse_obj_as(
                        type_=ManagedSsoClientTaskResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def ocm_groups(
        self,
        *,
        clusters: typing.Sequence[OcmGroupsCluster],
        desired_state: typing.Sequence[OcmGroupUser],
        ocm_connection: OcmConnectionParams,
        ocm_environment: str,
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OcmGroupsTaskResponse]:
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
        HttpResponse[OcmGroupsTaskResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/integrations/ocm-groups/reconcile",
            method="POST",
            json={
                "clusters": convert_and_respect_annotation_metadata(
                    object_=clusters, annotation=typing.Sequence[OcmGroupsCluster], direction="write"
                ),
                "desired_state": convert_and_respect_annotation_metadata(
                    object_=desired_state, annotation=typing.Sequence[OcmGroupUser], direction="write"
                ),
                "dry_run": dry_run,
                "ocm_connection": convert_and_respect_annotation_metadata(
                    object_=ocm_connection, annotation=OcmConnectionParams, direction="write"
                ),
                "ocm_environment": ocm_environment,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OcmGroupsTaskResponse,
                    parse_obj_as(
                        type_=OcmGroupsTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def ocm_groups_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OcmGroupsTaskResult]:
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
        HttpResponse[OcmGroupsTaskResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/ocm-groups/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OcmGroupsTaskResult,
                    parse_obj_as(
                        type_=OcmGroupsTaskResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def ocm_oidc_idp(
        self,
        *,
        clusters: typing.Sequence[OcmOidcIdpCluster],
        ocm_connection: OcmConnectionParams,
        ocm_environment: str,
        vault_target: Secret,
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OcmOidcIdpTaskResponse]:
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
        HttpResponse[OcmOidcIdpTaskResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/integrations/ocm-oidc-idp/reconcile",
            method="POST",
            json={
                "clusters": convert_and_respect_annotation_metadata(
                    object_=clusters, annotation=typing.Sequence[OcmOidcIdpCluster], direction="write"
                ),
                "dry_run": dry_run,
                "ocm_connection": convert_and_respect_annotation_metadata(
                    object_=ocm_connection, annotation=OcmConnectionParams, direction="write"
                ),
                "ocm_environment": ocm_environment,
                "vault_target": convert_and_respect_annotation_metadata(
                    object_=vault_target, annotation=Secret, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OcmOidcIdpTaskResponse,
                    parse_obj_as(
                        type_=OcmOidcIdpTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def ocm_oidc_idp_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OcmOidcIdpTaskResult]:
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
        HttpResponse[OcmOidcIdpTaskResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/ocm-oidc-idp/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OcmOidcIdpTaskResult,
                    parse_obj_as(
                        type_=OcmOidcIdpTaskResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def openshift_namespaces(
        self,
        *,
        clusters: typing.Sequence[ClusterNamespaces],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OpenShiftNamespacesTaskResponse]:
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
        HttpResponse[OpenShiftNamespacesTaskResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/integrations/openshift-namespaces/reconcile",
            method="POST",
            json={
                "clusters": convert_and_respect_annotation_metadata(
                    object_=clusters, annotation=typing.Sequence[ClusterNamespaces], direction="write"
                ),
                "dry_run": dry_run,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenShiftNamespacesTaskResponse,
                    parse_obj_as(
                        type_=OpenShiftNamespacesTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def openshift_namespaces_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OpenShiftNamespacesTaskResult]:
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
        HttpResponse[OpenShiftNamespacesTaskResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/openshift-namespaces/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenShiftNamespacesTaskResult,
                    parse_obj_as(
                        type_=OpenShiftNamespacesTaskResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def quay_repos(
        self,
        *,
        orgs: typing.Sequence[QuayOrgConfig],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[QuayReposTaskResponse]:
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
        HttpResponse[QuayReposTaskResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/integrations/quay-repos/reconcile",
            method="POST",
            json={
                "dry_run": dry_run,
                "orgs": convert_and_respect_annotation_metadata(
                    object_=orgs, annotation=typing.Sequence[QuayOrgConfig], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QuayReposTaskResponse,
                    parse_obj_as(
                        type_=QuayReposTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def quay_repos_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[QuayReposTaskResult]:
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
        HttpResponse[QuayReposTaskResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/quay-repos/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QuayReposTaskResult,
                    parse_obj_as(
                        type_=QuayReposTaskResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def quay_robot_accounts(
        self,
        *,
        organizations: typing.Sequence[QuayOrgDesiredState],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[QuayRobotAccountsTaskResponse]:
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
        HttpResponse[QuayRobotAccountsTaskResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/integrations/quay-robot-accounts/reconcile",
            method="POST",
            json={
                "dry_run": dry_run,
                "organizations": convert_and_respect_annotation_metadata(
                    object_=organizations, annotation=typing.Sequence[QuayOrgDesiredState], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QuayRobotAccountsTaskResponse,
                    parse_obj_as(
                        type_=QuayRobotAccountsTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def quay_robot_accounts_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[QuayRobotAccountsTaskResult]:
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
        HttpResponse[QuayRobotAccountsTaskResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/quay-robot-accounts/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QuayRobotAccountsTaskResult,
                    parse_obj_as(
                        type_=QuayRobotAccountsTaskResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slack_usergroups(
        self,
        *,
        workspaces: typing.Sequence[SlackWorkspace],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SlackUsergroupsTaskResponse]:
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
        HttpResponse[SlackUsergroupsTaskResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/integrations/slack-usergroups/reconcile",
            method="POST",
            json={
                "dry_run": dry_run,
                "workspaces": convert_and_respect_annotation_metadata(
                    object_=workspaces, annotation=typing.Sequence[SlackWorkspace], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SlackUsergroupsTaskResponse,
                    parse_obj_as(
                        type_=SlackUsergroupsTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slack_usergroups_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SlackUsergroupsTaskResult]:
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
        HttpResponse[SlackUsergroupsTaskResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/slack-usergroups/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SlackUsergroupsTaskResult,
                    parse_obj_as(
                        type_=SlackUsergroupsTaskResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def sso_client(
        self,
        *,
        clusters: typing.Sequence[SsoClientCluster],
        keycloak_secrets: typing.Sequence[KeycloakInstanceSecret],
        ocm_environment: str,
        vault_target: Secret,
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SsoClientTaskResponse]:
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
        HttpResponse[SsoClientTaskResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/integrations/sso-client/reconcile",
            method="POST",
            json={
                "clusters": convert_and_respect_annotation_metadata(
                    object_=clusters, annotation=typing.Sequence[SsoClientCluster], direction="write"
                ),
                "dry_run": dry_run,
                "keycloak_secrets": convert_and_respect_annotation_metadata(
                    object_=keycloak_secrets, annotation=typing.Sequence[KeycloakInstanceSecret], direction="write"
                ),
                "ocm_environment": ocm_environment,
                "vault_target": convert_and_respect_annotation_metadata(
                    object_=vault_target, annotation=Secret, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SsoClientTaskResponse,
                    parse_obj_as(
                        type_=SsoClientTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def sso_client_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SsoClientTaskResult]:
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
        HttpResponse[SsoClientTaskResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/sso-client/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SsoClientTaskResult,
                    parse_obj_as(
                        type_=SsoClientTaskResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawIntegrationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def github_owners(
        self,
        *,
        organizations: typing.Sequence[GithubOrgDesiredState],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GithubOwnersTaskResponse]:
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
        AsyncHttpResponse[GithubOwnersTaskResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/integrations/github-owners/reconcile",
            method="POST",
            json={
                "dry_run": dry_run,
                "organizations": convert_and_respect_annotation_metadata(
                    object_=organizations, annotation=typing.Sequence[GithubOrgDesiredState], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GithubOwnersTaskResponse,
                    parse_obj_as(
                        type_=GithubOwnersTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def github_owners_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GithubOwnersTaskResult]:
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
        AsyncHttpResponse[GithubOwnersTaskResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/github-owners/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GithubOwnersTaskResult,
                    parse_obj_as(
                        type_=GithubOwnersTaskResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def glitchtip_project_alerts(
        self,
        *,
        instances: typing.Sequence[GlitchtipInstance],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GlitchtipProjectAlertsTaskResponse]:
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
        AsyncHttpResponse[GlitchtipProjectAlertsTaskResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/integrations/glitchtip-project-alerts/reconcile",
            method="POST",
            json={
                "dry_run": dry_run,
                "instances": convert_and_respect_annotation_metadata(
                    object_=instances, annotation=typing.Sequence[GlitchtipInstance], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlitchtipProjectAlertsTaskResponse,
                    parse_obj_as(
                        type_=GlitchtipProjectAlertsTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def glitchtip_project_alerts_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GlitchtipProjectAlertsTaskResult]:
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
        AsyncHttpResponse[GlitchtipProjectAlertsTaskResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/glitchtip-project-alerts/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlitchtipProjectAlertsTaskResult,
                    parse_obj_as(
                        type_=GlitchtipProjectAlertsTaskResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def glitchtip(
        self,
        *,
        instances: typing.Sequence[GiInstance],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GlitchtipTaskResponse]:
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
        AsyncHttpResponse[GlitchtipTaskResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/integrations/glitchtip/reconcile",
            method="POST",
            json={
                "dry_run": dry_run,
                "instances": convert_and_respect_annotation_metadata(
                    object_=instances, annotation=typing.Sequence[GiInstance], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlitchtipTaskResponse,
                    parse_obj_as(
                        type_=GlitchtipTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def glitchtip_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GlitchtipTaskResult]:
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
        AsyncHttpResponse[GlitchtipTaskResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/glitchtip/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlitchtipTaskResult,
                    parse_obj_as(
                        type_=GlitchtipTaskResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def managed_sso_client(
        self,
        *,
        desired_clients: typing.Sequence[ManagedSsoClientDesiredState],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ManagedSsoClientTaskResponse]:
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
        AsyncHttpResponse[ManagedSsoClientTaskResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/integrations/managed-sso-client/reconcile",
            method="POST",
            json={
                "desired_clients": convert_and_respect_annotation_metadata(
                    object_=desired_clients, annotation=typing.Sequence[ManagedSsoClientDesiredState], direction="write"
                ),
                "dry_run": dry_run,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ManagedSsoClientTaskResponse,
                    parse_obj_as(
                        type_=ManagedSsoClientTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def managed_sso_client_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ManagedSsoClientTaskResult]:
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
        AsyncHttpResponse[ManagedSsoClientTaskResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/managed-sso-client/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ManagedSsoClientTaskResult,
                    parse_obj_as(
                        type_=ManagedSsoClientTaskResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def ocm_groups(
        self,
        *,
        clusters: typing.Sequence[OcmGroupsCluster],
        desired_state: typing.Sequence[OcmGroupUser],
        ocm_connection: OcmConnectionParams,
        ocm_environment: str,
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OcmGroupsTaskResponse]:
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
        AsyncHttpResponse[OcmGroupsTaskResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/integrations/ocm-groups/reconcile",
            method="POST",
            json={
                "clusters": convert_and_respect_annotation_metadata(
                    object_=clusters, annotation=typing.Sequence[OcmGroupsCluster], direction="write"
                ),
                "desired_state": convert_and_respect_annotation_metadata(
                    object_=desired_state, annotation=typing.Sequence[OcmGroupUser], direction="write"
                ),
                "dry_run": dry_run,
                "ocm_connection": convert_and_respect_annotation_metadata(
                    object_=ocm_connection, annotation=OcmConnectionParams, direction="write"
                ),
                "ocm_environment": ocm_environment,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OcmGroupsTaskResponse,
                    parse_obj_as(
                        type_=OcmGroupsTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def ocm_groups_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OcmGroupsTaskResult]:
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
        AsyncHttpResponse[OcmGroupsTaskResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/ocm-groups/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OcmGroupsTaskResult,
                    parse_obj_as(
                        type_=OcmGroupsTaskResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def ocm_oidc_idp(
        self,
        *,
        clusters: typing.Sequence[OcmOidcIdpCluster],
        ocm_connection: OcmConnectionParams,
        ocm_environment: str,
        vault_target: Secret,
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OcmOidcIdpTaskResponse]:
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
        AsyncHttpResponse[OcmOidcIdpTaskResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/integrations/ocm-oidc-idp/reconcile",
            method="POST",
            json={
                "clusters": convert_and_respect_annotation_metadata(
                    object_=clusters, annotation=typing.Sequence[OcmOidcIdpCluster], direction="write"
                ),
                "dry_run": dry_run,
                "ocm_connection": convert_and_respect_annotation_metadata(
                    object_=ocm_connection, annotation=OcmConnectionParams, direction="write"
                ),
                "ocm_environment": ocm_environment,
                "vault_target": convert_and_respect_annotation_metadata(
                    object_=vault_target, annotation=Secret, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OcmOidcIdpTaskResponse,
                    parse_obj_as(
                        type_=OcmOidcIdpTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def ocm_oidc_idp_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OcmOidcIdpTaskResult]:
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
        AsyncHttpResponse[OcmOidcIdpTaskResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/ocm-oidc-idp/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OcmOidcIdpTaskResult,
                    parse_obj_as(
                        type_=OcmOidcIdpTaskResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def openshift_namespaces(
        self,
        *,
        clusters: typing.Sequence[ClusterNamespaces],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OpenShiftNamespacesTaskResponse]:
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
        AsyncHttpResponse[OpenShiftNamespacesTaskResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/integrations/openshift-namespaces/reconcile",
            method="POST",
            json={
                "clusters": convert_and_respect_annotation_metadata(
                    object_=clusters, annotation=typing.Sequence[ClusterNamespaces], direction="write"
                ),
                "dry_run": dry_run,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenShiftNamespacesTaskResponse,
                    parse_obj_as(
                        type_=OpenShiftNamespacesTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def openshift_namespaces_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OpenShiftNamespacesTaskResult]:
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
        AsyncHttpResponse[OpenShiftNamespacesTaskResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/openshift-namespaces/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenShiftNamespacesTaskResult,
                    parse_obj_as(
                        type_=OpenShiftNamespacesTaskResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def quay_repos(
        self,
        *,
        orgs: typing.Sequence[QuayOrgConfig],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[QuayReposTaskResponse]:
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
        AsyncHttpResponse[QuayReposTaskResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/integrations/quay-repos/reconcile",
            method="POST",
            json={
                "dry_run": dry_run,
                "orgs": convert_and_respect_annotation_metadata(
                    object_=orgs, annotation=typing.Sequence[QuayOrgConfig], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QuayReposTaskResponse,
                    parse_obj_as(
                        type_=QuayReposTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def quay_repos_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[QuayReposTaskResult]:
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
        AsyncHttpResponse[QuayReposTaskResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/quay-repos/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QuayReposTaskResult,
                    parse_obj_as(
                        type_=QuayReposTaskResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def quay_robot_accounts(
        self,
        *,
        organizations: typing.Sequence[QuayOrgDesiredState],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[QuayRobotAccountsTaskResponse]:
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
        AsyncHttpResponse[QuayRobotAccountsTaskResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/integrations/quay-robot-accounts/reconcile",
            method="POST",
            json={
                "dry_run": dry_run,
                "organizations": convert_and_respect_annotation_metadata(
                    object_=organizations, annotation=typing.Sequence[QuayOrgDesiredState], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QuayRobotAccountsTaskResponse,
                    parse_obj_as(
                        type_=QuayRobotAccountsTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def quay_robot_accounts_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[QuayRobotAccountsTaskResult]:
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
        AsyncHttpResponse[QuayRobotAccountsTaskResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/quay-robot-accounts/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QuayRobotAccountsTaskResult,
                    parse_obj_as(
                        type_=QuayRobotAccountsTaskResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slack_usergroups(
        self,
        *,
        workspaces: typing.Sequence[SlackWorkspace],
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SlackUsergroupsTaskResponse]:
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
        AsyncHttpResponse[SlackUsergroupsTaskResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/integrations/slack-usergroups/reconcile",
            method="POST",
            json={
                "dry_run": dry_run,
                "workspaces": convert_and_respect_annotation_metadata(
                    object_=workspaces, annotation=typing.Sequence[SlackWorkspace], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SlackUsergroupsTaskResponse,
                    parse_obj_as(
                        type_=SlackUsergroupsTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slack_usergroups_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SlackUsergroupsTaskResult]:
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
        AsyncHttpResponse[SlackUsergroupsTaskResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/slack-usergroups/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SlackUsergroupsTaskResult,
                    parse_obj_as(
                        type_=SlackUsergroupsTaskResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def sso_client(
        self,
        *,
        clusters: typing.Sequence[SsoClientCluster],
        keycloak_secrets: typing.Sequence[KeycloakInstanceSecret],
        ocm_environment: str,
        vault_target: Secret,
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SsoClientTaskResponse]:
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
        AsyncHttpResponse[SsoClientTaskResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/integrations/sso-client/reconcile",
            method="POST",
            json={
                "clusters": convert_and_respect_annotation_metadata(
                    object_=clusters, annotation=typing.Sequence[SsoClientCluster], direction="write"
                ),
                "dry_run": dry_run,
                "keycloak_secrets": convert_and_respect_annotation_metadata(
                    object_=keycloak_secrets, annotation=typing.Sequence[KeycloakInstanceSecret], direction="write"
                ),
                "ocm_environment": ocm_environment,
                "vault_target": convert_and_respect_annotation_metadata(
                    object_=vault_target, annotation=Secret, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SsoClientTaskResponse,
                    parse_obj_as(
                        type_=SsoClientTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def sso_client_task_status(
        self,
        task_id: str,
        *,
        timeout: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SsoClientTaskResult]:
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
        AsyncHttpResponse[SsoClientTaskResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/integrations/sso-client/reconcile/{encode_path_param(task_id)}",
            method="GET",
            params={
                "timeout": timeout,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SsoClientTaskResult,
                    parse_obj_as(
                        type_=SsoClientTaskResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
