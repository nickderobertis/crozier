

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
from ..errors.not_found_error import NotFoundError
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
from .types.file_sync_request_file_operations_item import FileSyncRequestFileOperationsItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawExternalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def github_org_members(
        self,
        *,
        secret_manager_url: str,
        path: str,
        org_name: str,
        field: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GithubOrgMembersResponse]:
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
        HttpResponse[GithubOrgMembersResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/external/github-org/members",
            method="GET",
            params={
                "secret_manager_url": secret_manager_url,
                "path": path,
                "field": field,
                "version": version,
                "org_name": org_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GithubOrgMembersResponse,
                    parse_obj_as(
                        type_=GithubOrgMembersResponse,
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

    def ldap_github_usernames(
        self,
        *,
        logins: typing.Sequence[str],
        secret: LdapDirectSecret,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LdapGithubUsernamesResponse]:
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
        HttpResponse[LdapGithubUsernamesResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/external/ldap/github-usernames",
            method="POST",
            json={
                "logins": logins,
                "secret": convert_and_respect_annotation_metadata(
                    object_=secret, annotation=LdapDirectSecret, direction="write"
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
                    LdapGithubUsernamesResponse,
                    parse_obj_as(
                        type_=LdapGithubUsernamesResponse,
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

    def ldap_users_check(
        self,
        *,
        secret: LdapDirectSecret,
        usernames: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LdapUsersCheckResponse]:
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
        HttpResponse[LdapUsersCheckResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/external/ldap/users/check",
            method="POST",
            json={
                "secret": convert_and_respect_annotation_metadata(
                    object_=secret, annotation=LdapDirectSecret, direction="write"
                ),
                "usernames": usernames,
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
                    LdapUsersCheckResponse,
                    parse_obj_as(
                        type_=LdapUsersCheckResponse,
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
    ) -> HttpResponse[OcmClustersResponse]:
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
        HttpResponse[OcmClustersResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/external/ocm/clusters",
            method="GET",
            params={
                "secret_manager_url": secret_manager_url,
                "path": path,
                "field": field,
                "version": version,
                "ocm_url": ocm_url,
                "access_token_url": access_token_url,
                "access_token_client_id": access_token_client_id,
                "label_key_prefix": label_key_prefix,
                "org_ids": org_ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OcmClustersResponse,
                    parse_obj_as(
                        type_=OcmClustersResponse,
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

    def pagerduty_escalation_policy_users(
        self,
        policy_id: str,
        *,
        secret_manager_url: str,
        path: str,
        field: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EscalationPolicyUsersResponse]:
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
        HttpResponse[EscalationPolicyUsersResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/external/pagerduty/escalation-policies/{encode_path_param(policy_id)}/users",
            method="GET",
            params={
                "secret_manager_url": secret_manager_url,
                "path": path,
                "field": field,
                "version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EscalationPolicyUsersResponse,
                    parse_obj_as(
                        type_=EscalationPolicyUsersResponse,
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

    def pagerduty_schedule_users(
        self,
        schedule_id: str,
        *,
        secret_manager_url: str,
        path: str,
        field: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ScheduleUsersResponse]:
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
        HttpResponse[ScheduleUsersResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/external/pagerduty/schedules/{encode_path_param(schedule_id)}/users",
            method="GET",
            params={
                "secret_manager_url": secret_manager_url,
                "path": path,
                "field": field,
                "version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScheduleUsersResponse,
                    parse_obj_as(
                        type_=ScheduleUsersResponse,
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
    ) -> HttpResponse[ChatResponse]:
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
        HttpResponse[ChatResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/external/slack/chat",
            method="POST",
            json={
                "channel": channel,
                "icon_emoji": icon_emoji,
                "icon_url": icon_url,
                "secret": convert_and_respect_annotation_metadata(object_=secret, annotation=Secret, direction="write"),
                "text": text,
                "thread_ts": thread_ts,
                "user": user,
                "username": username,
                "workspace_name": workspace_name,
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
                    ChatResponse,
                    parse_obj_as(
                        type_=ChatResponse,
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
    ) -> HttpResponse[FileSyncResponse]:
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
        HttpResponse[FileSyncResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/external/vcs/file-sync",
            method="POST",
            json={
                "auto_merge": auto_merge,
                "description": description,
                "file_operations": convert_and_respect_annotation_metadata(
                    object_=file_operations,
                    annotation=typing.Sequence[FileSyncRequestFileOperationsItem],
                    direction="write",
                ),
                "labels": labels,
                "repo_url": repo_url,
                "target_branch": target_branch,
                "title": title,
                "token": convert_and_respect_annotation_metadata(object_=token, annotation=Secret, direction="write"),
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
                    FileSyncResponse,
                    parse_obj_as(
                        type_=FileSyncResponse,
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
    ) -> HttpResponse[GetFileResponse]:
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
        HttpResponse[GetFileResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/external/vcs/repos/file",
            method="GET",
            params={
                "secret_manager_url": secret_manager_url,
                "path": path,
                "field": field,
                "version": version,
                "repo_url": repo_url,
                "file_path": file_path,
                "ref": ref,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFileResponse,
                    parse_obj_as(
                        type_=GetFileResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[RepoOwnersResponse]:
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
        HttpResponse[RepoOwnersResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/external/vcs/repos/owners",
            method="GET",
            params={
                "secret_manager_url": secret_manager_url,
                "path": path,
                "field": field,
                "version": version,
                "repo_url": repo_url,
                "owners_file": owners_file,
                "ref": ref,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RepoOwnersResponse,
                    parse_obj_as(
                        type_=RepoOwnersResponse,
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


class AsyncRawExternalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def github_org_members(
        self,
        *,
        secret_manager_url: str,
        path: str,
        org_name: str,
        field: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GithubOrgMembersResponse]:
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
        AsyncHttpResponse[GithubOrgMembersResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/external/github-org/members",
            method="GET",
            params={
                "secret_manager_url": secret_manager_url,
                "path": path,
                "field": field,
                "version": version,
                "org_name": org_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GithubOrgMembersResponse,
                    parse_obj_as(
                        type_=GithubOrgMembersResponse,
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

    async def ldap_github_usernames(
        self,
        *,
        logins: typing.Sequence[str],
        secret: LdapDirectSecret,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LdapGithubUsernamesResponse]:
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
        AsyncHttpResponse[LdapGithubUsernamesResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/external/ldap/github-usernames",
            method="POST",
            json={
                "logins": logins,
                "secret": convert_and_respect_annotation_metadata(
                    object_=secret, annotation=LdapDirectSecret, direction="write"
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
                    LdapGithubUsernamesResponse,
                    parse_obj_as(
                        type_=LdapGithubUsernamesResponse,
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

    async def ldap_users_check(
        self,
        *,
        secret: LdapDirectSecret,
        usernames: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LdapUsersCheckResponse]:
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
        AsyncHttpResponse[LdapUsersCheckResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/external/ldap/users/check",
            method="POST",
            json={
                "secret": convert_and_respect_annotation_metadata(
                    object_=secret, annotation=LdapDirectSecret, direction="write"
                ),
                "usernames": usernames,
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
                    LdapUsersCheckResponse,
                    parse_obj_as(
                        type_=LdapUsersCheckResponse,
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
    ) -> AsyncHttpResponse[OcmClustersResponse]:
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
        AsyncHttpResponse[OcmClustersResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/external/ocm/clusters",
            method="GET",
            params={
                "secret_manager_url": secret_manager_url,
                "path": path,
                "field": field,
                "version": version,
                "ocm_url": ocm_url,
                "access_token_url": access_token_url,
                "access_token_client_id": access_token_client_id,
                "label_key_prefix": label_key_prefix,
                "org_ids": org_ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OcmClustersResponse,
                    parse_obj_as(
                        type_=OcmClustersResponse,
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

    async def pagerduty_escalation_policy_users(
        self,
        policy_id: str,
        *,
        secret_manager_url: str,
        path: str,
        field: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EscalationPolicyUsersResponse]:
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
        AsyncHttpResponse[EscalationPolicyUsersResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/external/pagerduty/escalation-policies/{encode_path_param(policy_id)}/users",
            method="GET",
            params={
                "secret_manager_url": secret_manager_url,
                "path": path,
                "field": field,
                "version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EscalationPolicyUsersResponse,
                    parse_obj_as(
                        type_=EscalationPolicyUsersResponse,
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

    async def pagerduty_schedule_users(
        self,
        schedule_id: str,
        *,
        secret_manager_url: str,
        path: str,
        field: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ScheduleUsersResponse]:
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
        AsyncHttpResponse[ScheduleUsersResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/external/pagerduty/schedules/{encode_path_param(schedule_id)}/users",
            method="GET",
            params={
                "secret_manager_url": secret_manager_url,
                "path": path,
                "field": field,
                "version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScheduleUsersResponse,
                    parse_obj_as(
                        type_=ScheduleUsersResponse,
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
    ) -> AsyncHttpResponse[ChatResponse]:
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
        AsyncHttpResponse[ChatResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/external/slack/chat",
            method="POST",
            json={
                "channel": channel,
                "icon_emoji": icon_emoji,
                "icon_url": icon_url,
                "secret": convert_and_respect_annotation_metadata(object_=secret, annotation=Secret, direction="write"),
                "text": text,
                "thread_ts": thread_ts,
                "user": user,
                "username": username,
                "workspace_name": workspace_name,
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
                    ChatResponse,
                    parse_obj_as(
                        type_=ChatResponse,
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
    ) -> AsyncHttpResponse[FileSyncResponse]:
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
        AsyncHttpResponse[FileSyncResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/external/vcs/file-sync",
            method="POST",
            json={
                "auto_merge": auto_merge,
                "description": description,
                "file_operations": convert_and_respect_annotation_metadata(
                    object_=file_operations,
                    annotation=typing.Sequence[FileSyncRequestFileOperationsItem],
                    direction="write",
                ),
                "labels": labels,
                "repo_url": repo_url,
                "target_branch": target_branch,
                "title": title,
                "token": convert_and_respect_annotation_metadata(object_=token, annotation=Secret, direction="write"),
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
                    FileSyncResponse,
                    parse_obj_as(
                        type_=FileSyncResponse,
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
    ) -> AsyncHttpResponse[GetFileResponse]:
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
        AsyncHttpResponse[GetFileResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/external/vcs/repos/file",
            method="GET",
            params={
                "secret_manager_url": secret_manager_url,
                "path": path,
                "field": field,
                "version": version,
                "repo_url": repo_url,
                "file_path": file_path,
                "ref": ref,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFileResponse,
                    parse_obj_as(
                        type_=GetFileResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[RepoOwnersResponse]:
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
        AsyncHttpResponse[RepoOwnersResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/external/vcs/repos/owners",
            method="GET",
            params={
                "secret_manager_url": secret_manager_url,
                "path": path,
                "field": field,
                "version": version,
                "repo_url": repo_url,
                "owners_file": owners_file,
                "ref": ref,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RepoOwnersResponse,
                    parse_obj_as(
                        type_=RepoOwnersResponse,
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
