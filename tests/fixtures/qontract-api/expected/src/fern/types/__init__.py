



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .access_type import AccessType
    from .chat_response import ChatResponse
    from .cluster_namespaces import ClusterNamespaces
    from .create_namespace_action import CreateNamespaceAction
    from .delete_namespace_action import DeleteNamespaceAction
    from .desired_namespace import DesiredNamespace
    from .escalation_policy_users_response import EscalationPolicyUsersResponse
    from .file_sync_create import FileSyncCreate
    from .file_sync_delete import FileSyncDelete
    from .file_sync_response import FileSyncResponse
    from .file_sync_status import FileSyncStatus
    from .file_sync_update import FileSyncUpdate
    from .get_file_response import GetFileResponse
    from .gi_instance import GiInstance
    from .gi_organization import GiOrganization
    from .gi_project import GiProject
    from .github_org_desired_state import GithubOrgDesiredState
    from .github_org_members_response import GithubOrgMembersResponse
    from .github_owner_action_add_owner import GithubOwnerActionAddOwner
    from .github_owners_task_response import GithubOwnersTaskResponse
    from .github_owners_task_result import GithubOwnersTaskResult
    from .github_owners_task_result_actions_item import (
        GithubOwnersTaskResultActionsItem,
        GithubOwnersTaskResultActionsItem_AddOwner,
    )
    from .github_owners_task_result_applied_actions_item import (
        GithubOwnersTaskResultAppliedActionsItem,
        GithubOwnersTaskResultAppliedActionsItem_AddOwner,
    )
    from .glitchtip_action_add_project_to_team import GlitchtipActionAddProjectToTeam
    from .glitchtip_action_add_user_to_team import GlitchtipActionAddUserToTeam
    from .glitchtip_action_create_organization import GlitchtipActionCreateOrganization
    from .glitchtip_action_create_project import GlitchtipActionCreateProject
    from .glitchtip_action_create_team import GlitchtipActionCreateTeam
    from .glitchtip_action_delete_organization import GlitchtipActionDeleteOrganization
    from .glitchtip_action_delete_project import GlitchtipActionDeleteProject
    from .glitchtip_action_delete_team import GlitchtipActionDeleteTeam
    from .glitchtip_action_delete_user import GlitchtipActionDeleteUser
    from .glitchtip_action_invite_user import GlitchtipActionInviteUser
    from .glitchtip_action_remove_project_from_team import GlitchtipActionRemoveProjectFromTeam
    from .glitchtip_action_remove_user_from_team import GlitchtipActionRemoveUserFromTeam
    from .glitchtip_action_update_project import GlitchtipActionUpdateProject
    from .glitchtip_action_update_user_role import GlitchtipActionUpdateUserRole
    from .glitchtip_alert_action_create import GlitchtipAlertActionCreate
    from .glitchtip_alert_action_delete import GlitchtipAlertActionDelete
    from .glitchtip_alert_action_update import GlitchtipAlertActionUpdate
    from .glitchtip_instance import GlitchtipInstance
    from .glitchtip_organization import GlitchtipOrganization
    from .glitchtip_project import GlitchtipProject
    from .glitchtip_project_alert import GlitchtipProjectAlert
    from .glitchtip_project_alert_recipient import GlitchtipProjectAlertRecipient
    from .glitchtip_project_alerts_task_response import GlitchtipProjectAlertsTaskResponse
    from .glitchtip_project_alerts_task_result import GlitchtipProjectAlertsTaskResult
    from .glitchtip_project_alerts_task_result_actions_item import (
        GlitchtipProjectAlertsTaskResultActionsItem,
        GlitchtipProjectAlertsTaskResultActionsItem_Create,
        GlitchtipProjectAlertsTaskResultActionsItem_Delete,
        GlitchtipProjectAlertsTaskResultActionsItem_Update,
    )
    from .glitchtip_project_alerts_task_result_applied_actions_item import (
        GlitchtipProjectAlertsTaskResultAppliedActionsItem,
        GlitchtipProjectAlertsTaskResultAppliedActionsItem_Create,
        GlitchtipProjectAlertsTaskResultAppliedActionsItem_Delete,
        GlitchtipProjectAlertsTaskResultAppliedActionsItem_Update,
    )
    from .glitchtip_task_response import GlitchtipTaskResponse
    from .glitchtip_task_result import GlitchtipTaskResult
    from .glitchtip_task_result_actions_item import (
        GlitchtipTaskResultActionsItem,
        GlitchtipTaskResultActionsItem_AddProjectToTeam,
        GlitchtipTaskResultActionsItem_AddUserToTeam,
        GlitchtipTaskResultActionsItem_CreateOrganization,
        GlitchtipTaskResultActionsItem_CreateProject,
        GlitchtipTaskResultActionsItem_CreateTeam,
        GlitchtipTaskResultActionsItem_DeleteOrganization,
        GlitchtipTaskResultActionsItem_DeleteProject,
        GlitchtipTaskResultActionsItem_DeleteTeam,
        GlitchtipTaskResultActionsItem_DeleteUser,
        GlitchtipTaskResultActionsItem_InviteUser,
        GlitchtipTaskResultActionsItem_RemoveProjectFromTeam,
        GlitchtipTaskResultActionsItem_RemoveUserFromTeam,
        GlitchtipTaskResultActionsItem_UpdateProject,
        GlitchtipTaskResultActionsItem_UpdateUserRole,
    )
    from .glitchtip_task_result_applied_actions_item import (
        GlitchtipTaskResultAppliedActionsItem,
        GlitchtipTaskResultAppliedActionsItem_AddProjectToTeam,
        GlitchtipTaskResultAppliedActionsItem_AddUserToTeam,
        GlitchtipTaskResultAppliedActionsItem_CreateOrganization,
        GlitchtipTaskResultAppliedActionsItem_CreateProject,
        GlitchtipTaskResultAppliedActionsItem_CreateTeam,
        GlitchtipTaskResultAppliedActionsItem_DeleteOrganization,
        GlitchtipTaskResultAppliedActionsItem_DeleteProject,
        GlitchtipTaskResultAppliedActionsItem_DeleteTeam,
        GlitchtipTaskResultAppliedActionsItem_DeleteUser,
        GlitchtipTaskResultAppliedActionsItem_InviteUser,
        GlitchtipTaskResultAppliedActionsItem_RemoveProjectFromTeam,
        GlitchtipTaskResultAppliedActionsItem_RemoveUserFromTeam,
        GlitchtipTaskResultAppliedActionsItem_UpdateProject,
        GlitchtipTaskResultAppliedActionsItem_UpdateUserRole,
    )
    from .glitchtip_team import GlitchtipTeam
    from .glitchtip_user import GlitchtipUser
    from .health_response import HealthResponse
    from .health_status import HealthStatus
    from .http_validation_error import HttpValidationError
    from .keycloak_instance_ref import KeycloakInstanceRef
    from .keycloak_instance_secret import KeycloakInstanceSecret
    from .ldap_direct_secret import LdapDirectSecret
    from .ldap_github_user import LdapGithubUser
    from .ldap_github_usernames_response import LdapGithubUsernamesResponse
    from .ldap_user_status import LdapUserStatus
    from .ldap_users_check_response import LdapUsersCheckResponse
    from .managed_sso_client_action_create import ManagedSsoClientActionCreate
    from .managed_sso_client_action_delete import ManagedSsoClientActionDelete
    from .managed_sso_client_action_move_tenant_secret import ManagedSsoClientActionMoveTenantSecret
    from .managed_sso_client_action_update import ManagedSsoClientActionUpdate
    from .managed_sso_client_desired_state import ManagedSsoClientDesiredState
    from .managed_sso_client_task_response import ManagedSsoClientTaskResponse
    from .managed_sso_client_task_result import ManagedSsoClientTaskResult
    from .managed_sso_client_task_result_actions_item import (
        ManagedSsoClientTaskResultActionsItem,
        ManagedSsoClientTaskResultActionsItem_Create,
        ManagedSsoClientTaskResultActionsItem_Delete,
        ManagedSsoClientTaskResultActionsItem_MoveTenantSecret,
        ManagedSsoClientTaskResultActionsItem_Update,
    )
    from .managed_sso_client_task_result_applied_actions_item import (
        ManagedSsoClientTaskResultAppliedActionsItem,
        ManagedSsoClientTaskResultAppliedActionsItem_Create,
        ManagedSsoClientTaskResultAppliedActionsItem_Delete,
        ManagedSsoClientTaskResultAppliedActionsItem_MoveTenantSecret,
        ManagedSsoClientTaskResultAppliedActionsItem_Update,
    )
    from .notification_add_user import NotificationAddUser
    from .notification_remove_user import NotificationRemoveUser
    from .ocm_cluster_info import OcmClusterInfo
    from .ocm_clusters_response import OcmClustersResponse
    from .ocm_connection_params import OcmConnectionParams
    from .ocm_group_user import OcmGroupUser
    from .ocm_groups_action_add_user import OcmGroupsActionAddUser
    from .ocm_groups_action_delete_user import OcmGroupsActionDeleteUser
    from .ocm_groups_cluster import OcmGroupsCluster
    from .ocm_groups_task_response import OcmGroupsTaskResponse
    from .ocm_groups_task_result import OcmGroupsTaskResult
    from .ocm_groups_task_result_actions_item import (
        OcmGroupsTaskResultActionsItem,
        OcmGroupsTaskResultActionsItem_AddUserToGroup,
        OcmGroupsTaskResultActionsItem_DeleteUserFromGroup,
    )
    from .ocm_groups_task_result_applied_actions_item import (
        OcmGroupsTaskResultAppliedActionsItem,
        OcmGroupsTaskResultAppliedActionsItem_AddUserToGroup,
        OcmGroupsTaskResultAppliedActionsItem_DeleteUserFromGroup,
    )
    from .ocm_oidc_idp_action_create import OcmOidcIdpActionCreate
    from .ocm_oidc_idp_action_delete import OcmOidcIdpActionDelete
    from .ocm_oidc_idp_action_update import OcmOidcIdpActionUpdate
    from .ocm_oidc_idp_auth import OcmOidcIdpAuth
    from .ocm_oidc_idp_cluster import OcmOidcIdpCluster
    from .ocm_oidc_idp_task_response import OcmOidcIdpTaskResponse
    from .ocm_oidc_idp_task_result import OcmOidcIdpTaskResult
    from .ocm_oidc_idp_task_result_actions_item import (
        OcmOidcIdpTaskResultActionsItem,
        OcmOidcIdpTaskResultActionsItem_Create,
        OcmOidcIdpTaskResultActionsItem_Delete,
        OcmOidcIdpTaskResultActionsItem_Update,
    )
    from .ocm_oidc_idp_task_result_applied_actions_item import (
        OcmOidcIdpTaskResultAppliedActionsItem,
        OcmOidcIdpTaskResultAppliedActionsItem_Create,
        OcmOidcIdpTaskResultAppliedActionsItem_Delete,
        OcmOidcIdpTaskResultAppliedActionsItem_Update,
    )
    from .oidc_desired_state import OidcDesiredState
    from .open_shift_namespaces_task_response import OpenShiftNamespacesTaskResponse
    from .open_shift_namespaces_task_result import OpenShiftNamespacesTaskResult
    from .open_shift_namespaces_task_result_actions_item import (
        OpenShiftNamespacesTaskResultActionsItem,
        OpenShiftNamespacesTaskResultActionsItem_CreateNamespace,
        OpenShiftNamespacesTaskResultActionsItem_DeleteNamespace,
    )
    from .open_shift_namespaces_task_result_applied_actions_item import (
        OpenShiftNamespacesTaskResultAppliedActionsItem,
        OpenShiftNamespacesTaskResultAppliedActionsItem_CreateNamespace,
        OpenShiftNamespacesTaskResultAppliedActionsItem_DeleteNamespace,
    )
    from .pager_duty_user import PagerDutyUser
    from .quay_org_config import QuayOrgConfig
    from .quay_org_desired_state import QuayOrgDesiredState
    from .quay_org_key import QuayOrgKey
    from .quay_repo_action_create import QuayRepoActionCreate
    from .quay_repo_action_delete import QuayRepoActionDelete
    from .quay_repo_action_update_description import QuayRepoActionUpdateDescription
    from .quay_repo_action_update_visibility import QuayRepoActionUpdateVisibility
    from .quay_repo_config import QuayRepoConfig
    from .quay_repo_permission import QuayRepoPermission
    from .quay_repos_task_response import QuayReposTaskResponse
    from .quay_repos_task_result import QuayReposTaskResult
    from .quay_repos_task_result_actions_item import (
        QuayReposTaskResultActionsItem,
        QuayReposTaskResultActionsItem_Create,
        QuayReposTaskResultActionsItem_Delete,
        QuayReposTaskResultActionsItem_UpdateDescription,
        QuayReposTaskResultActionsItem_UpdateVisibility,
    )
    from .quay_repos_task_result_applied_actions_item import (
        QuayReposTaskResultAppliedActionsItem,
        QuayReposTaskResultAppliedActionsItem_Create,
        QuayReposTaskResultAppliedActionsItem_Delete,
        QuayReposTaskResultAppliedActionsItem_UpdateDescription,
        QuayReposTaskResultAppliedActionsItem_UpdateVisibility,
    )
    from .quay_robot_accounts_task_response import QuayRobotAccountsTaskResponse
    from .quay_robot_accounts_task_result import QuayRobotAccountsTaskResult
    from .quay_robot_accounts_task_result_actions_item import (
        QuayRobotAccountsTaskResultActionsItem,
        QuayRobotAccountsTaskResultActionsItem_AddTeam,
        QuayRobotAccountsTaskResultActionsItem_Create,
        QuayRobotAccountsTaskResultActionsItem_Delete,
        QuayRobotAccountsTaskResultActionsItem_RemoveRepoPermission,
        QuayRobotAccountsTaskResultActionsItem_RemoveTeam,
        QuayRobotAccountsTaskResultActionsItem_SetRepoPermission,
    )
    from .quay_robot_accounts_task_result_applied_actions_item import (
        QuayRobotAccountsTaskResultAppliedActionsItem,
        QuayRobotAccountsTaskResultAppliedActionsItem_AddTeam,
        QuayRobotAccountsTaskResultAppliedActionsItem_Create,
        QuayRobotAccountsTaskResultAppliedActionsItem_Delete,
        QuayRobotAccountsTaskResultAppliedActionsItem_RemoveRepoPermission,
        QuayRobotAccountsTaskResultAppliedActionsItem_RemoveTeam,
        QuayRobotAccountsTaskResultAppliedActionsItem_SetRepoPermission,
    )
    from .quay_robot_action_add_team import QuayRobotActionAddTeam
    from .quay_robot_action_create import QuayRobotActionCreate
    from .quay_robot_action_delete import QuayRobotActionDelete
    from .quay_robot_action_remove_repo_permission import QuayRobotActionRemoveRepoPermission
    from .quay_robot_action_remove_team import QuayRobotActionRemoveTeam
    from .quay_robot_action_set_repo_permission import QuayRobotActionSetRepoPermission
    from .quay_robot_desired_state import QuayRobotDesiredState
    from .quay_robot_repository import QuayRobotRepository
    from .recipient_type import RecipientType
    from .repo_owners_response import RepoOwnersResponse
    from .schedule_users_response import ScheduleUsersResponse
    from .secret import Secret
    from .slack_usergroup import SlackUsergroup
    from .slack_usergroup_action_create import SlackUsergroupActionCreate
    from .slack_usergroup_action_update_metadata import SlackUsergroupActionUpdateMetadata
    from .slack_usergroup_action_update_users import SlackUsergroupActionUpdateUsers
    from .slack_usergroup_action_update_users_notifications_item import (
        SlackUsergroupActionUpdateUsersNotificationsItem,
        SlackUsergroupActionUpdateUsersNotificationsItem_AddUser,
        SlackUsergroupActionUpdateUsersNotificationsItem_RemoveUser,
    )
    from .slack_usergroup_config import SlackUsergroupConfig
    from .slack_usergroup_config_notifications_item import (
        SlackUsergroupConfigNotificationsItem,
        SlackUsergroupConfigNotificationsItem_AddUser,
        SlackUsergroupConfigNotificationsItem_RemoveUser,
    )
    from .slack_usergroups_task_response import SlackUsergroupsTaskResponse
    from .slack_usergroups_task_result import SlackUsergroupsTaskResult
    from .slack_usergroups_task_result_actions_item import (
        SlackUsergroupsTaskResultActionsItem,
        SlackUsergroupsTaskResultActionsItem_Create,
        SlackUsergroupsTaskResultActionsItem_UpdateMetadata,
        SlackUsergroupsTaskResultActionsItem_UpdateUsers,
    )
    from .slack_usergroups_task_result_applied_actions_item import (
        SlackUsergroupsTaskResultAppliedActionsItem,
        SlackUsergroupsTaskResultAppliedActionsItem_Create,
        SlackUsergroupsTaskResultAppliedActionsItem_UpdateMetadata,
        SlackUsergroupsTaskResultAppliedActionsItem_UpdateUsers,
    )
    from .slack_workspace import SlackWorkspace
    from .sso_client_action_create import SsoClientActionCreate
    from .sso_client_action_delete import SsoClientActionDelete
    from .sso_client_auth import SsoClientAuth
    from .sso_client_cluster import SsoClientCluster
    from .sso_client_task_response import SsoClientTaskResponse
    from .sso_client_task_result import SsoClientTaskResult
    from .sso_client_task_result_actions_item import (
        SsoClientTaskResultActionsItem,
        SsoClientTaskResultActionsItem_Create,
        SsoClientTaskResultActionsItem_Delete,
    )
    from .sso_client_task_result_applied_actions_item import (
        SsoClientTaskResultAppliedActionsItem,
        SsoClientTaskResultAppliedActionsItem_Create,
        SsoClientTaskResultAppliedActionsItem_Delete,
    )
    from .task_status import TaskStatus
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
    from .vcs_provider import VcsProvider
_dynamic_imports: typing.Dict[str, str] = {
    "AccessType": ".access_type",
    "ChatResponse": ".chat_response",
    "ClusterNamespaces": ".cluster_namespaces",
    "CreateNamespaceAction": ".create_namespace_action",
    "DeleteNamespaceAction": ".delete_namespace_action",
    "DesiredNamespace": ".desired_namespace",
    "EscalationPolicyUsersResponse": ".escalation_policy_users_response",
    "FileSyncCreate": ".file_sync_create",
    "FileSyncDelete": ".file_sync_delete",
    "FileSyncResponse": ".file_sync_response",
    "FileSyncStatus": ".file_sync_status",
    "FileSyncUpdate": ".file_sync_update",
    "GetFileResponse": ".get_file_response",
    "GiInstance": ".gi_instance",
    "GiOrganization": ".gi_organization",
    "GiProject": ".gi_project",
    "GithubOrgDesiredState": ".github_org_desired_state",
    "GithubOrgMembersResponse": ".github_org_members_response",
    "GithubOwnerActionAddOwner": ".github_owner_action_add_owner",
    "GithubOwnersTaskResponse": ".github_owners_task_response",
    "GithubOwnersTaskResult": ".github_owners_task_result",
    "GithubOwnersTaskResultActionsItem": ".github_owners_task_result_actions_item",
    "GithubOwnersTaskResultActionsItem_AddOwner": ".github_owners_task_result_actions_item",
    "GithubOwnersTaskResultAppliedActionsItem": ".github_owners_task_result_applied_actions_item",
    "GithubOwnersTaskResultAppliedActionsItem_AddOwner": ".github_owners_task_result_applied_actions_item",
    "GlitchtipActionAddProjectToTeam": ".glitchtip_action_add_project_to_team",
    "GlitchtipActionAddUserToTeam": ".glitchtip_action_add_user_to_team",
    "GlitchtipActionCreateOrganization": ".glitchtip_action_create_organization",
    "GlitchtipActionCreateProject": ".glitchtip_action_create_project",
    "GlitchtipActionCreateTeam": ".glitchtip_action_create_team",
    "GlitchtipActionDeleteOrganization": ".glitchtip_action_delete_organization",
    "GlitchtipActionDeleteProject": ".glitchtip_action_delete_project",
    "GlitchtipActionDeleteTeam": ".glitchtip_action_delete_team",
    "GlitchtipActionDeleteUser": ".glitchtip_action_delete_user",
    "GlitchtipActionInviteUser": ".glitchtip_action_invite_user",
    "GlitchtipActionRemoveProjectFromTeam": ".glitchtip_action_remove_project_from_team",
    "GlitchtipActionRemoveUserFromTeam": ".glitchtip_action_remove_user_from_team",
    "GlitchtipActionUpdateProject": ".glitchtip_action_update_project",
    "GlitchtipActionUpdateUserRole": ".glitchtip_action_update_user_role",
    "GlitchtipAlertActionCreate": ".glitchtip_alert_action_create",
    "GlitchtipAlertActionDelete": ".glitchtip_alert_action_delete",
    "GlitchtipAlertActionUpdate": ".glitchtip_alert_action_update",
    "GlitchtipInstance": ".glitchtip_instance",
    "GlitchtipOrganization": ".glitchtip_organization",
    "GlitchtipProject": ".glitchtip_project",
    "GlitchtipProjectAlert": ".glitchtip_project_alert",
    "GlitchtipProjectAlertRecipient": ".glitchtip_project_alert_recipient",
    "GlitchtipProjectAlertsTaskResponse": ".glitchtip_project_alerts_task_response",
    "GlitchtipProjectAlertsTaskResult": ".glitchtip_project_alerts_task_result",
    "GlitchtipProjectAlertsTaskResultActionsItem": ".glitchtip_project_alerts_task_result_actions_item",
    "GlitchtipProjectAlertsTaskResultActionsItem_Create": ".glitchtip_project_alerts_task_result_actions_item",
    "GlitchtipProjectAlertsTaskResultActionsItem_Delete": ".glitchtip_project_alerts_task_result_actions_item",
    "GlitchtipProjectAlertsTaskResultActionsItem_Update": ".glitchtip_project_alerts_task_result_actions_item",
    "GlitchtipProjectAlertsTaskResultAppliedActionsItem": ".glitchtip_project_alerts_task_result_applied_actions_item",
    "GlitchtipProjectAlertsTaskResultAppliedActionsItem_Create": ".glitchtip_project_alerts_task_result_applied_actions_item",
    "GlitchtipProjectAlertsTaskResultAppliedActionsItem_Delete": ".glitchtip_project_alerts_task_result_applied_actions_item",
    "GlitchtipProjectAlertsTaskResultAppliedActionsItem_Update": ".glitchtip_project_alerts_task_result_applied_actions_item",
    "GlitchtipTaskResponse": ".glitchtip_task_response",
    "GlitchtipTaskResult": ".glitchtip_task_result",
    "GlitchtipTaskResultActionsItem": ".glitchtip_task_result_actions_item",
    "GlitchtipTaskResultActionsItem_AddProjectToTeam": ".glitchtip_task_result_actions_item",
    "GlitchtipTaskResultActionsItem_AddUserToTeam": ".glitchtip_task_result_actions_item",
    "GlitchtipTaskResultActionsItem_CreateOrganization": ".glitchtip_task_result_actions_item",
    "GlitchtipTaskResultActionsItem_CreateProject": ".glitchtip_task_result_actions_item",
    "GlitchtipTaskResultActionsItem_CreateTeam": ".glitchtip_task_result_actions_item",
    "GlitchtipTaskResultActionsItem_DeleteOrganization": ".glitchtip_task_result_actions_item",
    "GlitchtipTaskResultActionsItem_DeleteProject": ".glitchtip_task_result_actions_item",
    "GlitchtipTaskResultActionsItem_DeleteTeam": ".glitchtip_task_result_actions_item",
    "GlitchtipTaskResultActionsItem_DeleteUser": ".glitchtip_task_result_actions_item",
    "GlitchtipTaskResultActionsItem_InviteUser": ".glitchtip_task_result_actions_item",
    "GlitchtipTaskResultActionsItem_RemoveProjectFromTeam": ".glitchtip_task_result_actions_item",
    "GlitchtipTaskResultActionsItem_RemoveUserFromTeam": ".glitchtip_task_result_actions_item",
    "GlitchtipTaskResultActionsItem_UpdateProject": ".glitchtip_task_result_actions_item",
    "GlitchtipTaskResultActionsItem_UpdateUserRole": ".glitchtip_task_result_actions_item",
    "GlitchtipTaskResultAppliedActionsItem": ".glitchtip_task_result_applied_actions_item",
    "GlitchtipTaskResultAppliedActionsItem_AddProjectToTeam": ".glitchtip_task_result_applied_actions_item",
    "GlitchtipTaskResultAppliedActionsItem_AddUserToTeam": ".glitchtip_task_result_applied_actions_item",
    "GlitchtipTaskResultAppliedActionsItem_CreateOrganization": ".glitchtip_task_result_applied_actions_item",
    "GlitchtipTaskResultAppliedActionsItem_CreateProject": ".glitchtip_task_result_applied_actions_item",
    "GlitchtipTaskResultAppliedActionsItem_CreateTeam": ".glitchtip_task_result_applied_actions_item",
    "GlitchtipTaskResultAppliedActionsItem_DeleteOrganization": ".glitchtip_task_result_applied_actions_item",
    "GlitchtipTaskResultAppliedActionsItem_DeleteProject": ".glitchtip_task_result_applied_actions_item",
    "GlitchtipTaskResultAppliedActionsItem_DeleteTeam": ".glitchtip_task_result_applied_actions_item",
    "GlitchtipTaskResultAppliedActionsItem_DeleteUser": ".glitchtip_task_result_applied_actions_item",
    "GlitchtipTaskResultAppliedActionsItem_InviteUser": ".glitchtip_task_result_applied_actions_item",
    "GlitchtipTaskResultAppliedActionsItem_RemoveProjectFromTeam": ".glitchtip_task_result_applied_actions_item",
    "GlitchtipTaskResultAppliedActionsItem_RemoveUserFromTeam": ".glitchtip_task_result_applied_actions_item",
    "GlitchtipTaskResultAppliedActionsItem_UpdateProject": ".glitchtip_task_result_applied_actions_item",
    "GlitchtipTaskResultAppliedActionsItem_UpdateUserRole": ".glitchtip_task_result_applied_actions_item",
    "GlitchtipTeam": ".glitchtip_team",
    "GlitchtipUser": ".glitchtip_user",
    "HealthResponse": ".health_response",
    "HealthStatus": ".health_status",
    "HttpValidationError": ".http_validation_error",
    "KeycloakInstanceRef": ".keycloak_instance_ref",
    "KeycloakInstanceSecret": ".keycloak_instance_secret",
    "LdapDirectSecret": ".ldap_direct_secret",
    "LdapGithubUser": ".ldap_github_user",
    "LdapGithubUsernamesResponse": ".ldap_github_usernames_response",
    "LdapUserStatus": ".ldap_user_status",
    "LdapUsersCheckResponse": ".ldap_users_check_response",
    "ManagedSsoClientActionCreate": ".managed_sso_client_action_create",
    "ManagedSsoClientActionDelete": ".managed_sso_client_action_delete",
    "ManagedSsoClientActionMoveTenantSecret": ".managed_sso_client_action_move_tenant_secret",
    "ManagedSsoClientActionUpdate": ".managed_sso_client_action_update",
    "ManagedSsoClientDesiredState": ".managed_sso_client_desired_state",
    "ManagedSsoClientTaskResponse": ".managed_sso_client_task_response",
    "ManagedSsoClientTaskResult": ".managed_sso_client_task_result",
    "ManagedSsoClientTaskResultActionsItem": ".managed_sso_client_task_result_actions_item",
    "ManagedSsoClientTaskResultActionsItem_Create": ".managed_sso_client_task_result_actions_item",
    "ManagedSsoClientTaskResultActionsItem_Delete": ".managed_sso_client_task_result_actions_item",
    "ManagedSsoClientTaskResultActionsItem_MoveTenantSecret": ".managed_sso_client_task_result_actions_item",
    "ManagedSsoClientTaskResultActionsItem_Update": ".managed_sso_client_task_result_actions_item",
    "ManagedSsoClientTaskResultAppliedActionsItem": ".managed_sso_client_task_result_applied_actions_item",
    "ManagedSsoClientTaskResultAppliedActionsItem_Create": ".managed_sso_client_task_result_applied_actions_item",
    "ManagedSsoClientTaskResultAppliedActionsItem_Delete": ".managed_sso_client_task_result_applied_actions_item",
    "ManagedSsoClientTaskResultAppliedActionsItem_MoveTenantSecret": ".managed_sso_client_task_result_applied_actions_item",
    "ManagedSsoClientTaskResultAppliedActionsItem_Update": ".managed_sso_client_task_result_applied_actions_item",
    "NotificationAddUser": ".notification_add_user",
    "NotificationRemoveUser": ".notification_remove_user",
    "OcmClusterInfo": ".ocm_cluster_info",
    "OcmClustersResponse": ".ocm_clusters_response",
    "OcmConnectionParams": ".ocm_connection_params",
    "OcmGroupUser": ".ocm_group_user",
    "OcmGroupsActionAddUser": ".ocm_groups_action_add_user",
    "OcmGroupsActionDeleteUser": ".ocm_groups_action_delete_user",
    "OcmGroupsCluster": ".ocm_groups_cluster",
    "OcmGroupsTaskResponse": ".ocm_groups_task_response",
    "OcmGroupsTaskResult": ".ocm_groups_task_result",
    "OcmGroupsTaskResultActionsItem": ".ocm_groups_task_result_actions_item",
    "OcmGroupsTaskResultActionsItem_AddUserToGroup": ".ocm_groups_task_result_actions_item",
    "OcmGroupsTaskResultActionsItem_DeleteUserFromGroup": ".ocm_groups_task_result_actions_item",
    "OcmGroupsTaskResultAppliedActionsItem": ".ocm_groups_task_result_applied_actions_item",
    "OcmGroupsTaskResultAppliedActionsItem_AddUserToGroup": ".ocm_groups_task_result_applied_actions_item",
    "OcmGroupsTaskResultAppliedActionsItem_DeleteUserFromGroup": ".ocm_groups_task_result_applied_actions_item",
    "OcmOidcIdpActionCreate": ".ocm_oidc_idp_action_create",
    "OcmOidcIdpActionDelete": ".ocm_oidc_idp_action_delete",
    "OcmOidcIdpActionUpdate": ".ocm_oidc_idp_action_update",
    "OcmOidcIdpAuth": ".ocm_oidc_idp_auth",
    "OcmOidcIdpCluster": ".ocm_oidc_idp_cluster",
    "OcmOidcIdpTaskResponse": ".ocm_oidc_idp_task_response",
    "OcmOidcIdpTaskResult": ".ocm_oidc_idp_task_result",
    "OcmOidcIdpTaskResultActionsItem": ".ocm_oidc_idp_task_result_actions_item",
    "OcmOidcIdpTaskResultActionsItem_Create": ".ocm_oidc_idp_task_result_actions_item",
    "OcmOidcIdpTaskResultActionsItem_Delete": ".ocm_oidc_idp_task_result_actions_item",
    "OcmOidcIdpTaskResultActionsItem_Update": ".ocm_oidc_idp_task_result_actions_item",
    "OcmOidcIdpTaskResultAppliedActionsItem": ".ocm_oidc_idp_task_result_applied_actions_item",
    "OcmOidcIdpTaskResultAppliedActionsItem_Create": ".ocm_oidc_idp_task_result_applied_actions_item",
    "OcmOidcIdpTaskResultAppliedActionsItem_Delete": ".ocm_oidc_idp_task_result_applied_actions_item",
    "OcmOidcIdpTaskResultAppliedActionsItem_Update": ".ocm_oidc_idp_task_result_applied_actions_item",
    "OidcDesiredState": ".oidc_desired_state",
    "OpenShiftNamespacesTaskResponse": ".open_shift_namespaces_task_response",
    "OpenShiftNamespacesTaskResult": ".open_shift_namespaces_task_result",
    "OpenShiftNamespacesTaskResultActionsItem": ".open_shift_namespaces_task_result_actions_item",
    "OpenShiftNamespacesTaskResultActionsItem_CreateNamespace": ".open_shift_namespaces_task_result_actions_item",
    "OpenShiftNamespacesTaskResultActionsItem_DeleteNamespace": ".open_shift_namespaces_task_result_actions_item",
    "OpenShiftNamespacesTaskResultAppliedActionsItem": ".open_shift_namespaces_task_result_applied_actions_item",
    "OpenShiftNamespacesTaskResultAppliedActionsItem_CreateNamespace": ".open_shift_namespaces_task_result_applied_actions_item",
    "OpenShiftNamespacesTaskResultAppliedActionsItem_DeleteNamespace": ".open_shift_namespaces_task_result_applied_actions_item",
    "PagerDutyUser": ".pager_duty_user",
    "QuayOrgConfig": ".quay_org_config",
    "QuayOrgDesiredState": ".quay_org_desired_state",
    "QuayOrgKey": ".quay_org_key",
    "QuayRepoActionCreate": ".quay_repo_action_create",
    "QuayRepoActionDelete": ".quay_repo_action_delete",
    "QuayRepoActionUpdateDescription": ".quay_repo_action_update_description",
    "QuayRepoActionUpdateVisibility": ".quay_repo_action_update_visibility",
    "QuayRepoConfig": ".quay_repo_config",
    "QuayRepoPermission": ".quay_repo_permission",
    "QuayReposTaskResponse": ".quay_repos_task_response",
    "QuayReposTaskResult": ".quay_repos_task_result",
    "QuayReposTaskResultActionsItem": ".quay_repos_task_result_actions_item",
    "QuayReposTaskResultActionsItem_Create": ".quay_repos_task_result_actions_item",
    "QuayReposTaskResultActionsItem_Delete": ".quay_repos_task_result_actions_item",
    "QuayReposTaskResultActionsItem_UpdateDescription": ".quay_repos_task_result_actions_item",
    "QuayReposTaskResultActionsItem_UpdateVisibility": ".quay_repos_task_result_actions_item",
    "QuayReposTaskResultAppliedActionsItem": ".quay_repos_task_result_applied_actions_item",
    "QuayReposTaskResultAppliedActionsItem_Create": ".quay_repos_task_result_applied_actions_item",
    "QuayReposTaskResultAppliedActionsItem_Delete": ".quay_repos_task_result_applied_actions_item",
    "QuayReposTaskResultAppliedActionsItem_UpdateDescription": ".quay_repos_task_result_applied_actions_item",
    "QuayReposTaskResultAppliedActionsItem_UpdateVisibility": ".quay_repos_task_result_applied_actions_item",
    "QuayRobotAccountsTaskResponse": ".quay_robot_accounts_task_response",
    "QuayRobotAccountsTaskResult": ".quay_robot_accounts_task_result",
    "QuayRobotAccountsTaskResultActionsItem": ".quay_robot_accounts_task_result_actions_item",
    "QuayRobotAccountsTaskResultActionsItem_AddTeam": ".quay_robot_accounts_task_result_actions_item",
    "QuayRobotAccountsTaskResultActionsItem_Create": ".quay_robot_accounts_task_result_actions_item",
    "QuayRobotAccountsTaskResultActionsItem_Delete": ".quay_robot_accounts_task_result_actions_item",
    "QuayRobotAccountsTaskResultActionsItem_RemoveRepoPermission": ".quay_robot_accounts_task_result_actions_item",
    "QuayRobotAccountsTaskResultActionsItem_RemoveTeam": ".quay_robot_accounts_task_result_actions_item",
    "QuayRobotAccountsTaskResultActionsItem_SetRepoPermission": ".quay_robot_accounts_task_result_actions_item",
    "QuayRobotAccountsTaskResultAppliedActionsItem": ".quay_robot_accounts_task_result_applied_actions_item",
    "QuayRobotAccountsTaskResultAppliedActionsItem_AddTeam": ".quay_robot_accounts_task_result_applied_actions_item",
    "QuayRobotAccountsTaskResultAppliedActionsItem_Create": ".quay_robot_accounts_task_result_applied_actions_item",
    "QuayRobotAccountsTaskResultAppliedActionsItem_Delete": ".quay_robot_accounts_task_result_applied_actions_item",
    "QuayRobotAccountsTaskResultAppliedActionsItem_RemoveRepoPermission": ".quay_robot_accounts_task_result_applied_actions_item",
    "QuayRobotAccountsTaskResultAppliedActionsItem_RemoveTeam": ".quay_robot_accounts_task_result_applied_actions_item",
    "QuayRobotAccountsTaskResultAppliedActionsItem_SetRepoPermission": ".quay_robot_accounts_task_result_applied_actions_item",
    "QuayRobotActionAddTeam": ".quay_robot_action_add_team",
    "QuayRobotActionCreate": ".quay_robot_action_create",
    "QuayRobotActionDelete": ".quay_robot_action_delete",
    "QuayRobotActionRemoveRepoPermission": ".quay_robot_action_remove_repo_permission",
    "QuayRobotActionRemoveTeam": ".quay_robot_action_remove_team",
    "QuayRobotActionSetRepoPermission": ".quay_robot_action_set_repo_permission",
    "QuayRobotDesiredState": ".quay_robot_desired_state",
    "QuayRobotRepository": ".quay_robot_repository",
    "RecipientType": ".recipient_type",
    "RepoOwnersResponse": ".repo_owners_response",
    "ScheduleUsersResponse": ".schedule_users_response",
    "Secret": ".secret",
    "SlackUsergroup": ".slack_usergroup",
    "SlackUsergroupActionCreate": ".slack_usergroup_action_create",
    "SlackUsergroupActionUpdateMetadata": ".slack_usergroup_action_update_metadata",
    "SlackUsergroupActionUpdateUsers": ".slack_usergroup_action_update_users",
    "SlackUsergroupActionUpdateUsersNotificationsItem": ".slack_usergroup_action_update_users_notifications_item",
    "SlackUsergroupActionUpdateUsersNotificationsItem_AddUser": ".slack_usergroup_action_update_users_notifications_item",
    "SlackUsergroupActionUpdateUsersNotificationsItem_RemoveUser": ".slack_usergroup_action_update_users_notifications_item",
    "SlackUsergroupConfig": ".slack_usergroup_config",
    "SlackUsergroupConfigNotificationsItem": ".slack_usergroup_config_notifications_item",
    "SlackUsergroupConfigNotificationsItem_AddUser": ".slack_usergroup_config_notifications_item",
    "SlackUsergroupConfigNotificationsItem_RemoveUser": ".slack_usergroup_config_notifications_item",
    "SlackUsergroupsTaskResponse": ".slack_usergroups_task_response",
    "SlackUsergroupsTaskResult": ".slack_usergroups_task_result",
    "SlackUsergroupsTaskResultActionsItem": ".slack_usergroups_task_result_actions_item",
    "SlackUsergroupsTaskResultActionsItem_Create": ".slack_usergroups_task_result_actions_item",
    "SlackUsergroupsTaskResultActionsItem_UpdateMetadata": ".slack_usergroups_task_result_actions_item",
    "SlackUsergroupsTaskResultActionsItem_UpdateUsers": ".slack_usergroups_task_result_actions_item",
    "SlackUsergroupsTaskResultAppliedActionsItem": ".slack_usergroups_task_result_applied_actions_item",
    "SlackUsergroupsTaskResultAppliedActionsItem_Create": ".slack_usergroups_task_result_applied_actions_item",
    "SlackUsergroupsTaskResultAppliedActionsItem_UpdateMetadata": ".slack_usergroups_task_result_applied_actions_item",
    "SlackUsergroupsTaskResultAppliedActionsItem_UpdateUsers": ".slack_usergroups_task_result_applied_actions_item",
    "SlackWorkspace": ".slack_workspace",
    "SsoClientActionCreate": ".sso_client_action_create",
    "SsoClientActionDelete": ".sso_client_action_delete",
    "SsoClientAuth": ".sso_client_auth",
    "SsoClientCluster": ".sso_client_cluster",
    "SsoClientTaskResponse": ".sso_client_task_response",
    "SsoClientTaskResult": ".sso_client_task_result",
    "SsoClientTaskResultActionsItem": ".sso_client_task_result_actions_item",
    "SsoClientTaskResultActionsItem_Create": ".sso_client_task_result_actions_item",
    "SsoClientTaskResultActionsItem_Delete": ".sso_client_task_result_actions_item",
    "SsoClientTaskResultAppliedActionsItem": ".sso_client_task_result_applied_actions_item",
    "SsoClientTaskResultAppliedActionsItem_Create": ".sso_client_task_result_applied_actions_item",
    "SsoClientTaskResultAppliedActionsItem_Delete": ".sso_client_task_result_applied_actions_item",
    "TaskStatus": ".task_status",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
    "VcsProvider": ".vcs_provider",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AccessType",
    "ChatResponse",
    "ClusterNamespaces",
    "CreateNamespaceAction",
    "DeleteNamespaceAction",
    "DesiredNamespace",
    "EscalationPolicyUsersResponse",
    "FileSyncCreate",
    "FileSyncDelete",
    "FileSyncResponse",
    "FileSyncStatus",
    "FileSyncUpdate",
    "GetFileResponse",
    "GiInstance",
    "GiOrganization",
    "GiProject",
    "GithubOrgDesiredState",
    "GithubOrgMembersResponse",
    "GithubOwnerActionAddOwner",
    "GithubOwnersTaskResponse",
    "GithubOwnersTaskResult",
    "GithubOwnersTaskResultActionsItem",
    "GithubOwnersTaskResultActionsItem_AddOwner",
    "GithubOwnersTaskResultAppliedActionsItem",
    "GithubOwnersTaskResultAppliedActionsItem_AddOwner",
    "GlitchtipActionAddProjectToTeam",
    "GlitchtipActionAddUserToTeam",
    "GlitchtipActionCreateOrganization",
    "GlitchtipActionCreateProject",
    "GlitchtipActionCreateTeam",
    "GlitchtipActionDeleteOrganization",
    "GlitchtipActionDeleteProject",
    "GlitchtipActionDeleteTeam",
    "GlitchtipActionDeleteUser",
    "GlitchtipActionInviteUser",
    "GlitchtipActionRemoveProjectFromTeam",
    "GlitchtipActionRemoveUserFromTeam",
    "GlitchtipActionUpdateProject",
    "GlitchtipActionUpdateUserRole",
    "GlitchtipAlertActionCreate",
    "GlitchtipAlertActionDelete",
    "GlitchtipAlertActionUpdate",
    "GlitchtipInstance",
    "GlitchtipOrganization",
    "GlitchtipProject",
    "GlitchtipProjectAlert",
    "GlitchtipProjectAlertRecipient",
    "GlitchtipProjectAlertsTaskResponse",
    "GlitchtipProjectAlertsTaskResult",
    "GlitchtipProjectAlertsTaskResultActionsItem",
    "GlitchtipProjectAlertsTaskResultActionsItem_Create",
    "GlitchtipProjectAlertsTaskResultActionsItem_Delete",
    "GlitchtipProjectAlertsTaskResultActionsItem_Update",
    "GlitchtipProjectAlertsTaskResultAppliedActionsItem",
    "GlitchtipProjectAlertsTaskResultAppliedActionsItem_Create",
    "GlitchtipProjectAlertsTaskResultAppliedActionsItem_Delete",
    "GlitchtipProjectAlertsTaskResultAppliedActionsItem_Update",
    "GlitchtipTaskResponse",
    "GlitchtipTaskResult",
    "GlitchtipTaskResultActionsItem",
    "GlitchtipTaskResultActionsItem_AddProjectToTeam",
    "GlitchtipTaskResultActionsItem_AddUserToTeam",
    "GlitchtipTaskResultActionsItem_CreateOrganization",
    "GlitchtipTaskResultActionsItem_CreateProject",
    "GlitchtipTaskResultActionsItem_CreateTeam",
    "GlitchtipTaskResultActionsItem_DeleteOrganization",
    "GlitchtipTaskResultActionsItem_DeleteProject",
    "GlitchtipTaskResultActionsItem_DeleteTeam",
    "GlitchtipTaskResultActionsItem_DeleteUser",
    "GlitchtipTaskResultActionsItem_InviteUser",
    "GlitchtipTaskResultActionsItem_RemoveProjectFromTeam",
    "GlitchtipTaskResultActionsItem_RemoveUserFromTeam",
    "GlitchtipTaskResultActionsItem_UpdateProject",
    "GlitchtipTaskResultActionsItem_UpdateUserRole",
    "GlitchtipTaskResultAppliedActionsItem",
    "GlitchtipTaskResultAppliedActionsItem_AddProjectToTeam",
    "GlitchtipTaskResultAppliedActionsItem_AddUserToTeam",
    "GlitchtipTaskResultAppliedActionsItem_CreateOrganization",
    "GlitchtipTaskResultAppliedActionsItem_CreateProject",
    "GlitchtipTaskResultAppliedActionsItem_CreateTeam",
    "GlitchtipTaskResultAppliedActionsItem_DeleteOrganization",
    "GlitchtipTaskResultAppliedActionsItem_DeleteProject",
    "GlitchtipTaskResultAppliedActionsItem_DeleteTeam",
    "GlitchtipTaskResultAppliedActionsItem_DeleteUser",
    "GlitchtipTaskResultAppliedActionsItem_InviteUser",
    "GlitchtipTaskResultAppliedActionsItem_RemoveProjectFromTeam",
    "GlitchtipTaskResultAppliedActionsItem_RemoveUserFromTeam",
    "GlitchtipTaskResultAppliedActionsItem_UpdateProject",
    "GlitchtipTaskResultAppliedActionsItem_UpdateUserRole",
    "GlitchtipTeam",
    "GlitchtipUser",
    "HealthResponse",
    "HealthStatus",
    "HttpValidationError",
    "KeycloakInstanceRef",
    "KeycloakInstanceSecret",
    "LdapDirectSecret",
    "LdapGithubUser",
    "LdapGithubUsernamesResponse",
    "LdapUserStatus",
    "LdapUsersCheckResponse",
    "ManagedSsoClientActionCreate",
    "ManagedSsoClientActionDelete",
    "ManagedSsoClientActionMoveTenantSecret",
    "ManagedSsoClientActionUpdate",
    "ManagedSsoClientDesiredState",
    "ManagedSsoClientTaskResponse",
    "ManagedSsoClientTaskResult",
    "ManagedSsoClientTaskResultActionsItem",
    "ManagedSsoClientTaskResultActionsItem_Create",
    "ManagedSsoClientTaskResultActionsItem_Delete",
    "ManagedSsoClientTaskResultActionsItem_MoveTenantSecret",
    "ManagedSsoClientTaskResultActionsItem_Update",
    "ManagedSsoClientTaskResultAppliedActionsItem",
    "ManagedSsoClientTaskResultAppliedActionsItem_Create",
    "ManagedSsoClientTaskResultAppliedActionsItem_Delete",
    "ManagedSsoClientTaskResultAppliedActionsItem_MoveTenantSecret",
    "ManagedSsoClientTaskResultAppliedActionsItem_Update",
    "NotificationAddUser",
    "NotificationRemoveUser",
    "OcmClusterInfo",
    "OcmClustersResponse",
    "OcmConnectionParams",
    "OcmGroupUser",
    "OcmGroupsActionAddUser",
    "OcmGroupsActionDeleteUser",
    "OcmGroupsCluster",
    "OcmGroupsTaskResponse",
    "OcmGroupsTaskResult",
    "OcmGroupsTaskResultActionsItem",
    "OcmGroupsTaskResultActionsItem_AddUserToGroup",
    "OcmGroupsTaskResultActionsItem_DeleteUserFromGroup",
    "OcmGroupsTaskResultAppliedActionsItem",
    "OcmGroupsTaskResultAppliedActionsItem_AddUserToGroup",
    "OcmGroupsTaskResultAppliedActionsItem_DeleteUserFromGroup",
    "OcmOidcIdpActionCreate",
    "OcmOidcIdpActionDelete",
    "OcmOidcIdpActionUpdate",
    "OcmOidcIdpAuth",
    "OcmOidcIdpCluster",
    "OcmOidcIdpTaskResponse",
    "OcmOidcIdpTaskResult",
    "OcmOidcIdpTaskResultActionsItem",
    "OcmOidcIdpTaskResultActionsItem_Create",
    "OcmOidcIdpTaskResultActionsItem_Delete",
    "OcmOidcIdpTaskResultActionsItem_Update",
    "OcmOidcIdpTaskResultAppliedActionsItem",
    "OcmOidcIdpTaskResultAppliedActionsItem_Create",
    "OcmOidcIdpTaskResultAppliedActionsItem_Delete",
    "OcmOidcIdpTaskResultAppliedActionsItem_Update",
    "OidcDesiredState",
    "OpenShiftNamespacesTaskResponse",
    "OpenShiftNamespacesTaskResult",
    "OpenShiftNamespacesTaskResultActionsItem",
    "OpenShiftNamespacesTaskResultActionsItem_CreateNamespace",
    "OpenShiftNamespacesTaskResultActionsItem_DeleteNamespace",
    "OpenShiftNamespacesTaskResultAppliedActionsItem",
    "OpenShiftNamespacesTaskResultAppliedActionsItem_CreateNamespace",
    "OpenShiftNamespacesTaskResultAppliedActionsItem_DeleteNamespace",
    "PagerDutyUser",
    "QuayOrgConfig",
    "QuayOrgDesiredState",
    "QuayOrgKey",
    "QuayRepoActionCreate",
    "QuayRepoActionDelete",
    "QuayRepoActionUpdateDescription",
    "QuayRepoActionUpdateVisibility",
    "QuayRepoConfig",
    "QuayRepoPermission",
    "QuayReposTaskResponse",
    "QuayReposTaskResult",
    "QuayReposTaskResultActionsItem",
    "QuayReposTaskResultActionsItem_Create",
    "QuayReposTaskResultActionsItem_Delete",
    "QuayReposTaskResultActionsItem_UpdateDescription",
    "QuayReposTaskResultActionsItem_UpdateVisibility",
    "QuayReposTaskResultAppliedActionsItem",
    "QuayReposTaskResultAppliedActionsItem_Create",
    "QuayReposTaskResultAppliedActionsItem_Delete",
    "QuayReposTaskResultAppliedActionsItem_UpdateDescription",
    "QuayReposTaskResultAppliedActionsItem_UpdateVisibility",
    "QuayRobotAccountsTaskResponse",
    "QuayRobotAccountsTaskResult",
    "QuayRobotAccountsTaskResultActionsItem",
    "QuayRobotAccountsTaskResultActionsItem_AddTeam",
    "QuayRobotAccountsTaskResultActionsItem_Create",
    "QuayRobotAccountsTaskResultActionsItem_Delete",
    "QuayRobotAccountsTaskResultActionsItem_RemoveRepoPermission",
    "QuayRobotAccountsTaskResultActionsItem_RemoveTeam",
    "QuayRobotAccountsTaskResultActionsItem_SetRepoPermission",
    "QuayRobotAccountsTaskResultAppliedActionsItem",
    "QuayRobotAccountsTaskResultAppliedActionsItem_AddTeam",
    "QuayRobotAccountsTaskResultAppliedActionsItem_Create",
    "QuayRobotAccountsTaskResultAppliedActionsItem_Delete",
    "QuayRobotAccountsTaskResultAppliedActionsItem_RemoveRepoPermission",
    "QuayRobotAccountsTaskResultAppliedActionsItem_RemoveTeam",
    "QuayRobotAccountsTaskResultAppliedActionsItem_SetRepoPermission",
    "QuayRobotActionAddTeam",
    "QuayRobotActionCreate",
    "QuayRobotActionDelete",
    "QuayRobotActionRemoveRepoPermission",
    "QuayRobotActionRemoveTeam",
    "QuayRobotActionSetRepoPermission",
    "QuayRobotDesiredState",
    "QuayRobotRepository",
    "RecipientType",
    "RepoOwnersResponse",
    "ScheduleUsersResponse",
    "Secret",
    "SlackUsergroup",
    "SlackUsergroupActionCreate",
    "SlackUsergroupActionUpdateMetadata",
    "SlackUsergroupActionUpdateUsers",
    "SlackUsergroupActionUpdateUsersNotificationsItem",
    "SlackUsergroupActionUpdateUsersNotificationsItem_AddUser",
    "SlackUsergroupActionUpdateUsersNotificationsItem_RemoveUser",
    "SlackUsergroupConfig",
    "SlackUsergroupConfigNotificationsItem",
    "SlackUsergroupConfigNotificationsItem_AddUser",
    "SlackUsergroupConfigNotificationsItem_RemoveUser",
    "SlackUsergroupsTaskResponse",
    "SlackUsergroupsTaskResult",
    "SlackUsergroupsTaskResultActionsItem",
    "SlackUsergroupsTaskResultActionsItem_Create",
    "SlackUsergroupsTaskResultActionsItem_UpdateMetadata",
    "SlackUsergroupsTaskResultActionsItem_UpdateUsers",
    "SlackUsergroupsTaskResultAppliedActionsItem",
    "SlackUsergroupsTaskResultAppliedActionsItem_Create",
    "SlackUsergroupsTaskResultAppliedActionsItem_UpdateMetadata",
    "SlackUsergroupsTaskResultAppliedActionsItem_UpdateUsers",
    "SlackWorkspace",
    "SsoClientActionCreate",
    "SsoClientActionDelete",
    "SsoClientAuth",
    "SsoClientCluster",
    "SsoClientTaskResponse",
    "SsoClientTaskResult",
    "SsoClientTaskResultActionsItem",
    "SsoClientTaskResultActionsItem_Create",
    "SsoClientTaskResultActionsItem_Delete",
    "SsoClientTaskResultAppliedActionsItem",
    "SsoClientTaskResultAppliedActionsItem_Create",
    "SsoClientTaskResultAppliedActionsItem_Delete",
    "TaskStatus",
    "ValidationError",
    "ValidationErrorLocItem",
    "VcsProvider",
]
