

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.chat_response import ChatResponse
from ..types.escalation_policy_users_response import EscalationPolicyUsersResponse
from ..types.file_sync_response import FileSyncResponse
from ..types.get_file_response import GetFileResponse
from ..types.github_org_members_response import GithubOrgMembersResponse
from ..types.ldap_direct_secret import LdapDirectSecret
from ..types.ldap_github_usernames_response import LdapGithubUsernamesResponse
from ..types.ldap_users_check_response import LdapUsersCheckResponse
from ..types.ocm_clusters_response import OcmClustersResponse
from ..types.repo_owners_response import RepoOwnersResponse
from ..types.schedule_users_response import ScheduleUsersResponse
from ..types.secret import Secret
from .raw_client import AsyncRawExternalClient, RawExternalClient
from .types.file_sync_request_file_operations_item import FileSyncRequestFileOperationsItem


OMIT = typing.cast(typing.Any, ...)


class ExternalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExternalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExternalClient
        """
        return self._raw_client

    def github_org_members(
        self,
        *,
        secret_manager_url: str,
        path: str,
        org_name: str,
        field: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GithubOrgMembersResponse:
        """
        Get all members of a GitHub organization.

        Lists every member of the organization (any role) using the GitHub API
        token resolved from Vault. Results are cached for performance (TTL
        configured in settings).

        Parameters
        ----------
        secret_manager_url : str
            Secret Manager URL

        path : str
            Path to the secret

        org_name : str
            GitHub organization name

        field : typing.Optional[str]
            Specific field within the secret

        version : typing.Optional[int]
            Version of the secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GithubOrgMembersResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.external.github_org_members(
            secret_manager_url="secret_manager_url",
            path="path",
            org_name="org_name",
        )
        """
        _response = self._raw_client.github_org_members(
            secret_manager_url=secret_manager_url,
            path=path,
            org_name=org_name,
            field=field,
            version=version,
            request_options=request_options,
        )
        return _response.data

    def ldap_github_usernames(
        self,
        *,
        logins: typing.Sequence[str],
        secret: LdapDirectSecret,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LdapGithubUsernamesResponse:
        """
        Resolve GitHub usernames to LDAP uids via the rhatSocialURL attribute.

        Maps each requested GitHub username to the app-interface org_username (LDAP
        uid) of the user whose rhatSocialURL points at that GitHub account. The
        full map is cached for performance; unresolved logins are omitted from the
        response.

        Args:
            request: GitHub usernames to resolve and the Vault secret reference
            cache: Cache dependency
            secret_manager: Secret manager dependency

        Returns:
            LdapGithubUsernamesResponse with resolved username -> org_username pairs

        Parameters
        ----------
        logins : typing.Sequence[str]
            GitHub usernames to resolve to LDAP uids

        secret : LdapDirectSecret
            Vault secret reference for LDAP credentials

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LdapGithubUsernamesResponse
            Successful Response

        Examples
        --------
        from fern import FernApi, LdapDirectSecret

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.external.ldap_github_usernames(
            logins=["logins"],
            secret=LdapDirectSecret(
                base_dn="base_dn",
                path="path",
                secret_manager_url="secret_manager_url",
                server_url="server_url",
            ),
        )
        """
        _response = self._raw_client.ldap_github_usernames(
            logins=logins, secret=secret, request_options=request_options
        )
        return _response.data

    def ldap_users_check(
        self,
        *,
        secret: LdapDirectSecret,
        usernames: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LdapUsersCheckResponse:
        """
        Check which usernames exist in LDAP (cached, FreeIPA-authenticated).

        Queries LDAP directly using FreeIPA service account credentials
        resolved from Vault. Results are cached for performance.

        Args:
            request: Request with usernames to check and Vault secret reference
            cache: Cache dependency
            secret_manager: Secret manager dependency

        Returns:
            LdapUsersCheckResponse with existence status per username

        Parameters
        ----------
        secret : LdapDirectSecret
            Vault secret reference for LDAP credentials

        usernames : typing.Sequence[str]
            Usernames to check

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LdapUsersCheckResponse
            Successful Response

        Examples
        --------
        from fern import FernApi, LdapDirectSecret

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.external.ldap_users_check(
            secret=LdapDirectSecret(
                base_dn="base_dn",
                path="path",
                secret_manager_url="secret_manager_url",
                server_url="server_url",
            ),
            usernames=["usernames"],
        )
        """
        _response = self._raw_client.ldap_users_check(
            secret=secret, usernames=usernames, request_options=request_options
        )
        return _response.data

    def ocm_clusters(
        self,
        *,
        secret_manager_url: str,
        path: str,
        ocm_url: str,
        access_token_url: str,
        access_token_client_id: str,
        label_key_prefix: str,
        field: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        org_ids: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OcmClustersResponse:
        """
        Discover OCM clusters with subscription/organization labels matching a prefix.

        Returns raw cluster info plus a flat dict of matching labels, merged with
        subscription-level labels winning over organization-level labels on key
        collisions. Label *interpretation* is left entirely to the caller. Results
        are cached (TTL configured in settings).

        Parameters
        ----------
        secret_manager_url : str
            Secret Manager URL

        path : str
            Path to the secret

        ocm_url : str
            OCM environment base URL

        access_token_url : str
            OAuth2 token endpoint (client-credentials grant)

        access_token_client_id : str
            OAuth2 client id

        label_key_prefix : str
            Subscription/organization label key prefix to search for (e.g. 'sre-capabilities.rhidp'); matched with a trailing '%' wildcard

        field : typing.Optional[str]
            Specific field within the secret

        version : typing.Optional[int]
            Version of the secret

        org_ids : typing.Optional[typing.Sequence[str]]
            Optional list of organization ids to restrict results to. Omit to include all matching organizations.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OcmClustersResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.external.ocm_clusters(
            secret_manager_url="secret_manager_url",
            path="path",
            ocm_url="ocm_url",
            access_token_url="access_token_url",
            access_token_client_id="access_token_client_id",
            label_key_prefix="label_key_prefix",
        )
        """
        _response = self._raw_client.ocm_clusters(
            secret_manager_url=secret_manager_url,
            path=path,
            ocm_url=ocm_url,
            access_token_url=access_token_url,
            access_token_client_id=access_token_client_id,
            label_key_prefix=label_key_prefix,
            field=field,
            version=version,
            org_ids=org_ids,
            request_options=request_options,
        )
        return _response.data

    def pagerduty_escalation_policy_users(
        self,
        policy_id: str,
        *,
        secret_manager_url: str,
        path: str,
        field: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EscalationPolicyUsersResponse:
        """
        Get users in a PagerDuty escalation policy.

        Fetches all users across all escalation rules in the policy.
        Results are cached for performance (TTL configured in settings).

        Args:
            policy_id: PagerDuty escalation policy ID
            instance: PagerDuty instance name

        Returns:
            EscalationPolicyUsersResponse with list of users

        Raises:
            HTTPException:
                - 500 Internal Server Error: If PagerDuty API call fails

        Example:
            GET /api/v1/external/pagerduty/escalation-policies/XYZ789/users?instance=app-sre
            Response:
            {
                "users": [
                    {"username": "jsmith"},
                    {"username": "mdoe"}
                ]
            }

        Parameters
        ----------
        policy_id : str

        secret_manager_url : str
            Secret Manager URL

        path : str
            Path to the secret

        field : typing.Optional[str]
            Specific field within the secret

        version : typing.Optional[int]
            Version of the secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EscalationPolicyUsersResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.external.pagerduty_escalation_policy_users(
            policy_id="policy_id",
            secret_manager_url="secret_manager_url",
            path="path",
        )
        """
        _response = self._raw_client.pagerduty_escalation_policy_users(
            policy_id,
            secret_manager_url=secret_manager_url,
            path=path,
            field=field,
            version=version,
            request_options=request_options,
        )
        return _response.data

    def pagerduty_schedule_users(
        self,
        schedule_id: str,
        *,
        secret_manager_url: str,
        path: str,
        field: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduleUsersResponse:
        """
        Get users currently on-call in a PagerDuty schedule.

        Fetches users from the specified schedule using a time window of now + 60 seconds.
        Results are cached for performance (TTL configured in settings).

        Args:
            schedule_id: PagerDuty schedule ID
            instance: PagerDuty instance name

        Returns:
            ScheduleUsersResponse with list of users

        Raises:
            HTTPException:
                - 500 Internal Server Error: If PagerDuty API call fails

        Example:
            GET /api/v1/external/pagerduty/schedules/ABC123/users?instance=app-sre
            Response:
            {
                "users": [
                    {"username": "jsmith"},
                    {"username": "mdoe"}
                ]
            }

        Parameters
        ----------
        schedule_id : str

        secret_manager_url : str
            Secret Manager URL

        path : str
            Path to the secret

        field : typing.Optional[str]
            Specific field within the secret

        version : typing.Optional[int]
            Version of the secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleUsersResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.external.pagerduty_schedule_users(
            schedule_id="schedule_id",
            secret_manager_url="secret_manager_url",
            path="path",
        )
        """
        _response = self._raw_client.pagerduty_schedule_users(
            schedule_id,
            secret_manager_url=secret_manager_url,
            path=path,
            field=field,
            version=version,
            request_options=request_options,
        )
        return _response.data

    def slack_chat_post_message(
        self,
        *,
        secret: Secret,
        text: str,
        workspace_name: str,
        channel: typing.Optional[str] = OMIT,
        icon_emoji: typing.Optional[str] = OMIT,
        icon_url: typing.Optional[str] = OMIT,
        thread_ts: typing.Optional[str] = OMIT,
        user: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChatResponse:
        """
        Post a message to a Slack channel or send a DM to a user.

        Exactly one of `channel` or `user` must be set in the request:
        - `channel`: post to a Slack channel by name
        - `user`: send a DM to a user by org_username

        Args:
            request: Chat request with channel/user, text, and credentials

        Returns:
            ChatResponse with ts, channel, and optional thread_ts

        Raises:
            HTTPException:
                - 404 Not Found: Channel or user not found
                - 502 Bad Gateway: If Slack API call fails

        Parameters
        ----------
        secret : Secret
            Secret reference for Slack bot token

        text : str
            Message text

        workspace_name : str
            Slack workspace name

        channel : typing.Optional[str]
            Channel name to post to (e.g., 'sd-app-sre-reconcile')

        icon_emoji : typing.Optional[str]
            Emoji to use as the message icon (e.g., ':robot_face:')

        icon_url : typing.Optional[str]
            URL to an image to use as the message icon

        thread_ts : typing.Optional[str]
            Optional thread timestamp for replies

        user : typing.Optional[str]
            org_username to send a DM to (e.g., 'jsmith@redhat.com')

        username : typing.Optional[str]
            Bot username to display

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChatResponse
            Successful Response

        Examples
        --------
        from fern import FernApi, Secret

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.external.slack_chat_post_message(
            secret=Secret(
                path="path",
                secret_manager_url="secret_manager_url",
            ),
            text="text",
            workspace_name="workspace_name",
        )
        """
        _response = self._raw_client.slack_chat_post_message(
            secret=secret,
            text=text,
            workspace_name=workspace_name,
            channel=channel,
            icon_emoji=icon_emoji,
            icon_url=icon_url,
            thread_ts=thread_ts,
            user=user,
            username=username,
            request_options=request_options,
        )
        return _response.data

    def vcs_file_sync(
        self,
        *,
        file_operations: typing.Sequence[FileSyncRequestFileOperationsItem],
        repo_url: str,
        target_branch: str,
        title: str,
        token: Secret,
        auto_merge: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileSyncResponse:
        """
        Reconcile file states in a VCS repository.

        Creates a merge request with the given file operations,
        deduplicating by MR title. Does not read current file state —
        relies on GitLab/GitHub for validation.

        Parameters
        ----------
        file_operations : typing.Sequence[FileSyncRequestFileOperationsItem]
            File operations to reconcile

        repo_url : str
            Repository URL (e.g., https://gitlab.com/group/project)

        target_branch : str
            Target branch name

        title : str
            Merge request title (used for deduplication)

        token : Secret
            Secret reference for VCS API token

        auto_merge : typing.Optional[bool]
            Whether to enable auto-merge

        description : typing.Optional[str]
            Merge request description

        labels : typing.Optional[typing.Sequence[str]]
            Labels to apply to the MR

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileSyncResponse
            Successful Response

        Examples
        --------
        from fern.external import FileSyncRequestFileOperationsItem_Create

        from fern import FernApi, Secret

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.external.vcs_file_sync(
            file_operations=[
                FileSyncRequestFileOperationsItem_Create(
                    commit_message="commit_message",
                    content="content",
                    path="path",
                )
            ],
            repo_url="repo_url",
            target_branch="target_branch",
            title="title",
            token=Secret(
                path="path",
                secret_manager_url="secret_manager_url",
            ),
        )
        """
        _response = self._raw_client.vcs_file_sync(
            file_operations=file_operations,
            repo_url=repo_url,
            target_branch=target_branch,
            title=title,
            token=token,
            auto_merge=auto_merge,
            description=description,
            labels=labels,
            request_options=request_options,
        )
        return _response.data

    def vcs_get_file(
        self,
        *,
        secret_manager_url: str,
        path: str,
        repo_url: str,
        file_path: str,
        ref: str,
        field: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetFileResponse:
        """
        Read a file from a VCS repository.

        Parameters
        ----------
        secret_manager_url : str
            Secret Manager URL

        path : str
            Path to the secret

        repo_url : str
            Repository URL (e.g., https://gitlab.com/group/project)

        file_path : str
            File path in the repository

        ref : str
            Git reference (branch, tag, SHA)

        field : typing.Optional[str]
            Specific field within the secret

        version : typing.Optional[int]
            Version of the secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFileResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.external.vcs_get_file(
            secret_manager_url="secret_manager_url",
            path="path",
            repo_url="repo_url",
            file_path="file_path",
            ref="ref",
        )
        """
        _response = self._raw_client.vcs_get_file(
            secret_manager_url=secret_manager_url,
            path=path,
            repo_url=repo_url,
            file_path=file_path,
            ref=ref,
            field=field,
            version=version,
            request_options=request_options,
        )
        return _response.data

    def vcs_repo_owners(
        self,
        *,
        secret_manager_url: str,
        path: str,
        repo_url: str,
        ref: str,
        field: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        owners_file: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RepoOwnersResponse:
        """
        Get OWNERS file data from a Git repository.

        Fetches OWNERS file approvers and reviewers from GitHub or GitLab repositories.
        Results are cached for performance (TTL configured in settings).

        Parameters
        ----------
        secret_manager_url : str
            Secret Manager URL

        path : str
            Path to the secret

        repo_url : str
            Repository URL (e.g., https://github.com/owner/repo)

        ref : str
            Git reference (branch, tag, commit SHA)

        field : typing.Optional[str]
            Specific field within the secret

        version : typing.Optional[int]
            Version of the secret

        owners_file : typing.Optional[str]
            Path to OWNERS file in the repository (e.g., /OWNERS or /path/to/OWNERS)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RepoOwnersResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.external.vcs_repo_owners(
            secret_manager_url="secret_manager_url",
            path="path",
            repo_url="repo_url",
            ref="ref",
        )
        """
        _response = self._raw_client.vcs_repo_owners(
            secret_manager_url=secret_manager_url,
            path=path,
            repo_url=repo_url,
            ref=ref,
            field=field,
            version=version,
            owners_file=owners_file,
            request_options=request_options,
        )
        return _response.data


class AsyncExternalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExternalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExternalClient
        """
        return self._raw_client

    async def github_org_members(
        self,
        *,
        secret_manager_url: str,
        path: str,
        org_name: str,
        field: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GithubOrgMembersResponse:
        """
        Get all members of a GitHub organization.

        Lists every member of the organization (any role) using the GitHub API
        token resolved from Vault. Results are cached for performance (TTL
        configured in settings).

        Parameters
        ----------
        secret_manager_url : str
            Secret Manager URL

        path : str
            Path to the secret

        org_name : str
            GitHub organization name

        field : typing.Optional[str]
            Specific field within the secret

        version : typing.Optional[int]
            Version of the secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GithubOrgMembersResponse
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
            await client.external.github_org_members(
                secret_manager_url="secret_manager_url",
                path="path",
                org_name="org_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.github_org_members(
            secret_manager_url=secret_manager_url,
            path=path,
            org_name=org_name,
            field=field,
            version=version,
            request_options=request_options,
        )
        return _response.data

    async def ldap_github_usernames(
        self,
        *,
        logins: typing.Sequence[str],
        secret: LdapDirectSecret,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LdapGithubUsernamesResponse:
        """
        Resolve GitHub usernames to LDAP uids via the rhatSocialURL attribute.

        Maps each requested GitHub username to the app-interface org_username (LDAP
        uid) of the user whose rhatSocialURL points at that GitHub account. The
        full map is cached for performance; unresolved logins are omitted from the
        response.

        Args:
            request: GitHub usernames to resolve and the Vault secret reference
            cache: Cache dependency
            secret_manager: Secret manager dependency

        Returns:
            LdapGithubUsernamesResponse with resolved username -> org_username pairs

        Parameters
        ----------
        logins : typing.Sequence[str]
            GitHub usernames to resolve to LDAP uids

        secret : LdapDirectSecret
            Vault secret reference for LDAP credentials

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LdapGithubUsernamesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LdapDirectSecret

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.external.ldap_github_usernames(
                logins=["logins"],
                secret=LdapDirectSecret(
                    base_dn="base_dn",
                    path="path",
                    secret_manager_url="secret_manager_url",
                    server_url="server_url",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ldap_github_usernames(
            logins=logins, secret=secret, request_options=request_options
        )
        return _response.data

    async def ldap_users_check(
        self,
        *,
        secret: LdapDirectSecret,
        usernames: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LdapUsersCheckResponse:
        """
        Check which usernames exist in LDAP (cached, FreeIPA-authenticated).

        Queries LDAP directly using FreeIPA service account credentials
        resolved from Vault. Results are cached for performance.

        Args:
            request: Request with usernames to check and Vault secret reference
            cache: Cache dependency
            secret_manager: Secret manager dependency

        Returns:
            LdapUsersCheckResponse with existence status per username

        Parameters
        ----------
        secret : LdapDirectSecret
            Vault secret reference for LDAP credentials

        usernames : typing.Sequence[str]
            Usernames to check

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LdapUsersCheckResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LdapDirectSecret

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.external.ldap_users_check(
                secret=LdapDirectSecret(
                    base_dn="base_dn",
                    path="path",
                    secret_manager_url="secret_manager_url",
                    server_url="server_url",
                ),
                usernames=["usernames"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ldap_users_check(
            secret=secret, usernames=usernames, request_options=request_options
        )
        return _response.data

    async def ocm_clusters(
        self,
        *,
        secret_manager_url: str,
        path: str,
        ocm_url: str,
        access_token_url: str,
        access_token_client_id: str,
        label_key_prefix: str,
        field: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        org_ids: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OcmClustersResponse:
        """
        Discover OCM clusters with subscription/organization labels matching a prefix.

        Returns raw cluster info plus a flat dict of matching labels, merged with
        subscription-level labels winning over organization-level labels on key
        collisions. Label *interpretation* is left entirely to the caller. Results
        are cached (TTL configured in settings).

        Parameters
        ----------
        secret_manager_url : str
            Secret Manager URL

        path : str
            Path to the secret

        ocm_url : str
            OCM environment base URL

        access_token_url : str
            OAuth2 token endpoint (client-credentials grant)

        access_token_client_id : str
            OAuth2 client id

        label_key_prefix : str
            Subscription/organization label key prefix to search for (e.g. 'sre-capabilities.rhidp'); matched with a trailing '%' wildcard

        field : typing.Optional[str]
            Specific field within the secret

        version : typing.Optional[int]
            Version of the secret

        org_ids : typing.Optional[typing.Sequence[str]]
            Optional list of organization ids to restrict results to. Omit to include all matching organizations.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OcmClustersResponse
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
            await client.external.ocm_clusters(
                secret_manager_url="secret_manager_url",
                path="path",
                ocm_url="ocm_url",
                access_token_url="access_token_url",
                access_token_client_id="access_token_client_id",
                label_key_prefix="label_key_prefix",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ocm_clusters(
            secret_manager_url=secret_manager_url,
            path=path,
            ocm_url=ocm_url,
            access_token_url=access_token_url,
            access_token_client_id=access_token_client_id,
            label_key_prefix=label_key_prefix,
            field=field,
            version=version,
            org_ids=org_ids,
            request_options=request_options,
        )
        return _response.data

    async def pagerduty_escalation_policy_users(
        self,
        policy_id: str,
        *,
        secret_manager_url: str,
        path: str,
        field: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EscalationPolicyUsersResponse:
        """
        Get users in a PagerDuty escalation policy.

        Fetches all users across all escalation rules in the policy.
        Results are cached for performance (TTL configured in settings).

        Args:
            policy_id: PagerDuty escalation policy ID
            instance: PagerDuty instance name

        Returns:
            EscalationPolicyUsersResponse with list of users

        Raises:
            HTTPException:
                - 500 Internal Server Error: If PagerDuty API call fails

        Example:
            GET /api/v1/external/pagerduty/escalation-policies/XYZ789/users?instance=app-sre
            Response:
            {
                "users": [
                    {"username": "jsmith"},
                    {"username": "mdoe"}
                ]
            }

        Parameters
        ----------
        policy_id : str

        secret_manager_url : str
            Secret Manager URL

        path : str
            Path to the secret

        field : typing.Optional[str]
            Specific field within the secret

        version : typing.Optional[int]
            Version of the secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EscalationPolicyUsersResponse
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
            await client.external.pagerduty_escalation_policy_users(
                policy_id="policy_id",
                secret_manager_url="secret_manager_url",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pagerduty_escalation_policy_users(
            policy_id,
            secret_manager_url=secret_manager_url,
            path=path,
            field=field,
            version=version,
            request_options=request_options,
        )
        return _response.data

    async def pagerduty_schedule_users(
        self,
        schedule_id: str,
        *,
        secret_manager_url: str,
        path: str,
        field: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScheduleUsersResponse:
        """
        Get users currently on-call in a PagerDuty schedule.

        Fetches users from the specified schedule using a time window of now + 60 seconds.
        Results are cached for performance (TTL configured in settings).

        Args:
            schedule_id: PagerDuty schedule ID
            instance: PagerDuty instance name

        Returns:
            ScheduleUsersResponse with list of users

        Raises:
            HTTPException:
                - 500 Internal Server Error: If PagerDuty API call fails

        Example:
            GET /api/v1/external/pagerduty/schedules/ABC123/users?instance=app-sre
            Response:
            {
                "users": [
                    {"username": "jsmith"},
                    {"username": "mdoe"}
                ]
            }

        Parameters
        ----------
        schedule_id : str

        secret_manager_url : str
            Secret Manager URL

        path : str
            Path to the secret

        field : typing.Optional[str]
            Specific field within the secret

        version : typing.Optional[int]
            Version of the secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleUsersResponse
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
            await client.external.pagerduty_schedule_users(
                schedule_id="schedule_id",
                secret_manager_url="secret_manager_url",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pagerduty_schedule_users(
            schedule_id,
            secret_manager_url=secret_manager_url,
            path=path,
            field=field,
            version=version,
            request_options=request_options,
        )
        return _response.data

    async def slack_chat_post_message(
        self,
        *,
        secret: Secret,
        text: str,
        workspace_name: str,
        channel: typing.Optional[str] = OMIT,
        icon_emoji: typing.Optional[str] = OMIT,
        icon_url: typing.Optional[str] = OMIT,
        thread_ts: typing.Optional[str] = OMIT,
        user: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChatResponse:
        """
        Post a message to a Slack channel or send a DM to a user.

        Exactly one of `channel` or `user` must be set in the request:
        - `channel`: post to a Slack channel by name
        - `user`: send a DM to a user by org_username

        Args:
            request: Chat request with channel/user, text, and credentials

        Returns:
            ChatResponse with ts, channel, and optional thread_ts

        Raises:
            HTTPException:
                - 404 Not Found: Channel or user not found
                - 502 Bad Gateway: If Slack API call fails

        Parameters
        ----------
        secret : Secret
            Secret reference for Slack bot token

        text : str
            Message text

        workspace_name : str
            Slack workspace name

        channel : typing.Optional[str]
            Channel name to post to (e.g., 'sd-app-sre-reconcile')

        icon_emoji : typing.Optional[str]
            Emoji to use as the message icon (e.g., ':robot_face:')

        icon_url : typing.Optional[str]
            URL to an image to use as the message icon

        thread_ts : typing.Optional[str]
            Optional thread timestamp for replies

        user : typing.Optional[str]
            org_username to send a DM to (e.g., 'jsmith@redhat.com')

        username : typing.Optional[str]
            Bot username to display

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChatResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Secret

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.external.slack_chat_post_message(
                secret=Secret(
                    path="path",
                    secret_manager_url="secret_manager_url",
                ),
                text="text",
                workspace_name="workspace_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slack_chat_post_message(
            secret=secret,
            text=text,
            workspace_name=workspace_name,
            channel=channel,
            icon_emoji=icon_emoji,
            icon_url=icon_url,
            thread_ts=thread_ts,
            user=user,
            username=username,
            request_options=request_options,
        )
        return _response.data

    async def vcs_file_sync(
        self,
        *,
        file_operations: typing.Sequence[FileSyncRequestFileOperationsItem],
        repo_url: str,
        target_branch: str,
        title: str,
        token: Secret,
        auto_merge: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileSyncResponse:
        """
        Reconcile file states in a VCS repository.

        Creates a merge request with the given file operations,
        deduplicating by MR title. Does not read current file state —
        relies on GitLab/GitHub for validation.

        Parameters
        ----------
        file_operations : typing.Sequence[FileSyncRequestFileOperationsItem]
            File operations to reconcile

        repo_url : str
            Repository URL (e.g., https://gitlab.com/group/project)

        target_branch : str
            Target branch name

        title : str
            Merge request title (used for deduplication)

        token : Secret
            Secret reference for VCS API token

        auto_merge : typing.Optional[bool]
            Whether to enable auto-merge

        description : typing.Optional[str]
            Merge request description

        labels : typing.Optional[typing.Sequence[str]]
            Labels to apply to the MR

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileSyncResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern.external import FileSyncRequestFileOperationsItem_Create

        from fern import AsyncFernApi, Secret

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.external.vcs_file_sync(
                file_operations=[
                    FileSyncRequestFileOperationsItem_Create(
                        commit_message="commit_message",
                        content="content",
                        path="path",
                    )
                ],
                repo_url="repo_url",
                target_branch="target_branch",
                title="title",
                token=Secret(
                    path="path",
                    secret_manager_url="secret_manager_url",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vcs_file_sync(
            file_operations=file_operations,
            repo_url=repo_url,
            target_branch=target_branch,
            title=title,
            token=token,
            auto_merge=auto_merge,
            description=description,
            labels=labels,
            request_options=request_options,
        )
        return _response.data

    async def vcs_get_file(
        self,
        *,
        secret_manager_url: str,
        path: str,
        repo_url: str,
        file_path: str,
        ref: str,
        field: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetFileResponse:
        """
        Read a file from a VCS repository.

        Parameters
        ----------
        secret_manager_url : str
            Secret Manager URL

        path : str
            Path to the secret

        repo_url : str
            Repository URL (e.g., https://gitlab.com/group/project)

        file_path : str
            File path in the repository

        ref : str
            Git reference (branch, tag, SHA)

        field : typing.Optional[str]
            Specific field within the secret

        version : typing.Optional[int]
            Version of the secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFileResponse
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
            await client.external.vcs_get_file(
                secret_manager_url="secret_manager_url",
                path="path",
                repo_url="repo_url",
                file_path="file_path",
                ref="ref",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vcs_get_file(
            secret_manager_url=secret_manager_url,
            path=path,
            repo_url=repo_url,
            file_path=file_path,
            ref=ref,
            field=field,
            version=version,
            request_options=request_options,
        )
        return _response.data

    async def vcs_repo_owners(
        self,
        *,
        secret_manager_url: str,
        path: str,
        repo_url: str,
        ref: str,
        field: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        owners_file: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RepoOwnersResponse:
        """
        Get OWNERS file data from a Git repository.

        Fetches OWNERS file approvers and reviewers from GitHub or GitLab repositories.
        Results are cached for performance (TTL configured in settings).

        Parameters
        ----------
        secret_manager_url : str
            Secret Manager URL

        path : str
            Path to the secret

        repo_url : str
            Repository URL (e.g., https://github.com/owner/repo)

        ref : str
            Git reference (branch, tag, commit SHA)

        field : typing.Optional[str]
            Specific field within the secret

        version : typing.Optional[int]
            Version of the secret

        owners_file : typing.Optional[str]
            Path to OWNERS file in the repository (e.g., /OWNERS or /path/to/OWNERS)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RepoOwnersResponse
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
            await client.external.vcs_repo_owners(
                secret_manager_url="secret_manager_url",
                path="path",
                repo_url="repo_url",
                ref="ref",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vcs_repo_owners(
            secret_manager_url=secret_manager_url,
            path=path,
            repo_url=repo_url,
            ref=ref,
            field=field,
            version=version,
            owners_file=owners_file,
            request_options=request_options,
        )
        return _response.data
