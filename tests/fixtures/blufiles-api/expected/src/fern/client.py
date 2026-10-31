

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.config import Config
from .types.delete_me_tokens_request_id import DeleteMeTokensRequestId
from .types.filtered_admin_user import FilteredAdminUser
from .types.filtered_collection import FilteredCollection
from .types.filtered_file import FilteredFile
from .types.filtered_file_upload import FilteredFileUpload
from .types.filtered_folder import FilteredFolder
from .types.filtered_paste import FilteredPaste
from .types.filtered_share import FilteredShare
from .types.filtered_token import FilteredToken
from .types.get_admin_usage_response import GetAdminUsageResponse
from .types.get_me_response import GetMeResponse
from .types.get_usage_stats_response import GetUsageStatsResponse
from .types.patch_admin_config_request_disable_registration import PatchAdminConfigRequestDisableRegistration
from .types.patch_admin_config_request_total import PatchAdminConfigRequestTotal
from .types.patch_admin_config_request_user import PatchAdminConfigRequestUser
from .types.patch_admin_users_id_request_type import PatchAdminUsersIdRequestType
from .types.patch_me_tokens_response import PatchMeTokensResponse
from .types.post_auth_login_response import PostAuthLoginResponse
from .types.post_auth_register_response import PostAuthRegisterResponse
from .types.post_me_tokens_response import PostMeTokensResponse
from .types.post_search_response import PostSearchResponse
from .types.post_share_request_type import PostShareRequestType


OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

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
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
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
            base_url=base_url,
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

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def get_admin_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> Config:
        """
        Returns the current server configuration. Requires an admin session token.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Config
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_admin_config()
        """
        _response = self._raw_client.get_admin_config(request_options=request_options)
        return _response.data

    def patch_admin_config(
        self,
        *,
        max_users: float,
        disable_registration: PatchAdminConfigRequestDisableRegistration,
        total: PatchAdminConfigRequestTotal,
        user: PatchAdminConfigRequestUser,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Applies partial updates to the server configuration. Requires an admin session token.

        Parameters
        ----------
        max_users : float

        disable_registration : PatchAdminConfigRequestDisableRegistration

        total : PatchAdminConfigRequestTotal

        user : PatchAdminConfigRequestUser

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import (
            FernApi,
            PatchAdminConfigRequestDisableRegistrationOne,
            PatchAdminConfigRequestTotal,
            PatchAdminConfigRequestUser,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.patch_admin_config(
            max_users=1.1,
            disable_registration=PatchAdminConfigRequestDisableRegistrationOne.AFTER_FIRST_USER,
            total=PatchAdminConfigRequestTotal(
                max_files=1.1,
                max_folders=1.1,
                max_pastes=1.1,
                max_collections=1.1,
                max_shares=1.1,
                max_storage=1.1,
            ),
            user=PatchAdminConfigRequestUser(
                max_files=1.1,
                max_folders=1.1,
                max_pastes=1.1,
                max_collections=1.1,
                max_shares=1.1,
                max_tokens=1.1,
                max_storage=1.1,
            ),
        )
        """
        _response = self._raw_client.patch_admin_config(
            max_users=max_users,
            disable_registration=disable_registration,
            total=total,
            user=user,
            request_options=request_options,
        )
        return _response.data

    def get_admin_usage(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetAdminUsageResponse:
        """
        Returns server-wide usage counters for storage, files, folders, pastes, collections,
        and shares alongside their configured limits. Requires an admin session token.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAdminUsageResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_admin_usage()
        """
        _response = self._raw_client.get_admin_usage(request_options=request_options)
        return _response.data

    def post_auth_login(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostAuthLoginResponse:
        """
        Authenticates with a username and password and returns a session token.

        Parameters
        ----------
        username : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthLoginResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_auth_login(
            username="username",
            password="password",
        )
        """
        _response = self._raw_client.post_auth_login(
            username=username, password=password, request_options=request_options
        )
        return _response.data

    def post_auth_register(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostAuthRegisterResponse:
        """
        Creates a new user account and returns a session token. May be disabled by server configuration.

        Parameters
        ----------
        username : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthRegisterResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_auth_register(
            username="username",
            password="password",
        )
        """
        _response = self._raw_client.post_auth_register(
            username=username, password=password, request_options=request_options
        )
        return _response.data

    def get_collection_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilteredCollection:
        """
        Returns a collection by ID. Accessible via a valid share link or as the owner.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredCollection
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_collection_id(
            id="id",
        )
        """
        _response = self._raw_client.get_collection_id(id, request_options=request_options)
        return _response.data

    def delete_collection_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes a collection. The files inside are not deleted.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_collection_id(
            id="id",
        )
        """
        _response = self._raw_client.delete_collection_id(id, request_options=request_options)
        return _response.data

    def patch_collection_id(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        file_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the name or file membership of a collection.

        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        file_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.patch_collection_id(
            id="id",
        )
        """
        _response = self._raw_client.patch_collection_id(
            id, name=name, file_ids=file_ids, request_options=request_options
        )
        return _response.data

    def get_collection(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FilteredCollection]:
        """
        Returns all collections owned by the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FilteredCollection]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_collection()
        """
        _response = self._raw_client.get_collection(request_options=request_options)
        return _response.data

    def post_collection(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FilteredCollection:
        """
        Creates a new empty collection for grouping files.

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredCollection
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_collection(
            name="name",
        )
        """
        _response = self._raw_client.post_collection(name=name, request_options=request_options)
        return _response.data

    def post_file(self, *, request_options: typing.Optional[RequestOptions] = None) -> FilteredFile:
        """
        Creates a new file record. Supply either an `uploadId` from a completed chunked upload
        or raw `data` bytes for small files. Optionally creates a share link in the same request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredFile
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_file()
        """
        _response = self._raw_client.post_file(request_options=request_options)
        return _response.data

    def get_folder_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> FilteredFolder:
        """
        Returns a folder and its contents by ID. Accessible via a valid share link or as the owner.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredFolder
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_folder_id(
            id="id",
        )
        """
        _response = self._raw_client.get_folder_id(id, request_options=request_options)
        return _response.data

    def delete_folder_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes a folder and all files inside it.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_folder_id(
            id="id",
        )
        """
        _response = self._raw_client.delete_folder_id(id, request_options=request_options)
        return _response.data

    def patch_folder_id(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the name or parent folder of an existing folder.

        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        parent_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.patch_folder_id(
            id="id",
        )
        """
        _response = self._raw_client.patch_folder_id(
            id, name=name, parent_id=parent_id, request_options=request_options
        )
        return _response.data

    def get_folder(self, *, request_options: typing.Optional[RequestOptions] = None) -> FilteredFolder:
        """
        Returns the authenticated user's root folder.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredFolder
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_folder()
        """
        _response = self._raw_client.get_folder(request_options=request_options)
        return _response.data

    def post_folder(
        self,
        *,
        name: str,
        parent_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilteredFolder:
        """
        Create a new folder under an optional parent.

        Parameters
        ----------
        name : str

        parent_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredFolder
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_folder(
            name="name",
        )
        """
        _response = self._raw_client.post_folder(name=name, parent_id=parent_id, request_options=request_options)
        return _response.data

    def delete_me_collections(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes all collections owned by the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_me_collections()
        """
        _response = self._raw_client.delete_me_collections(request_options=request_options)
        return _response.data

    def delete_me_files(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes all files and folders owned by the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_me_files()
        """
        _response = self._raw_client.delete_me_files(request_options=request_options)
        return _response.data

    def get_me(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetMeResponse:
        """
        Returns the authenticated user's ID, username, and role.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMeResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_me()
        """
        _response = self._raw_client.get_me(request_options=request_options)
        return _response.data

    def delete_me(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes the authenticated user's account and all associated data.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_me()
        """
        _response = self._raw_client.delete_me(request_options=request_options)
        return _response.data

    def patch_me(self, *, username: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Updates the authenticated user's username.

        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.patch_me(
            username="username",
        )
        """
        _response = self._raw_client.patch_me(username=username, request_options=request_options)
        return _response.data

    def post_me_logout(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Invalidates the current session token.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_me_logout()
        """
        _response = self._raw_client.post_me_logout(request_options=request_options)
        return _response.data

    def patch_me_password(
        self, *, current_password: str, new_password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Updates the authenticated user's password after verifying the current one.

        Parameters
        ----------
        current_password : str

        new_password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.patch_me_password(
            current_password="currentPassword",
            new_password="newPassword",
        )
        """
        _response = self._raw_client.patch_me_password(
            current_password=current_password, new_password=new_password, request_options=request_options
        )
        return _response.data

    def delete_me_pastes(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes all pastes owned by the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_me_pastes()
        """
        _response = self._raw_client.delete_me_pastes(request_options=request_options)
        return _response.data

    def delete_me_shares(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes all share links owned by the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_me_shares()
        """
        _response = self._raw_client.delete_me_shares(request_options=request_options)
        return _response.data

    def get_me_tokens(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[FilteredToken]:
        """
        Returns all API tokens for the authenticated user, sorted with the current token first.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FilteredToken]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_me_tokens()
        """
        _response = self._raw_client.get_me_tokens(request_options=request_options)
        return _response.data

    def post_me_tokens(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostMeTokensResponse:
        """
        Creates a new named uploader API token for programmatic access.

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostMeTokensResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_me_tokens(
            name="name",
        )
        """
        _response = self._raw_client.post_me_tokens(name=name, request_options=request_options)
        return _response.data

    def delete_me_tokens(
        self, *, id: DeleteMeTokensRequestId, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a specific token by ID, all tokens, or all tokens except the current session.

        Parameters
        ----------
        id : DeleteMeTokensRequestId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import DeleteMeTokensRequestIdZero, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_me_tokens(
            id=DeleteMeTokensRequestIdZero.ALL,
        )
        """
        _response = self._raw_client.delete_me_tokens(id=id, request_options=request_options)
        return _response.data

    def patch_me_tokens(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PatchMeTokensResponse:
        """
        Regenerates a token by ID. Only applicable to uploader tokens.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchMeTokensResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.patch_me_tokens(
            id="id",
        )
        """
        _response = self._raw_client.patch_me_tokens(id=id, request_options=request_options)
        return _response.data

    def get_paste_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> FilteredPaste:
        """
        Returns a paste including its full content.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredPaste
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_paste_id(
            id="id",
        )
        """
        _response = self._raw_client.get_paste_id(id, request_options=request_options)
        return _response.data

    def delete_paste_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes a paste.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_paste_id(
            id="id",
        )
        """
        _response = self._raw_client.delete_paste_id(id, request_options=request_options)
        return _response.data

    def patch_paste_id(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        content: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilteredPaste:
        """
        Updates the name, content, or syntax type of a paste.

        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        content : typing.Optional[str]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredPaste
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.patch_paste_id(
            id="id",
        )
        """
        _response = self._raw_client.patch_paste_id(
            id, name=name, content=content, type=type, request_options=request_options
        )
        return _response.data

    def get_paste(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[FilteredPaste]:
        """
        Returns all pastes owned by the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FilteredPaste]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_paste()
        """
        _response = self._raw_client.get_paste(request_options=request_options)
        return _response.data

    def post_paste(
        self,
        *,
        name: str,
        content: str,
        type: str,
        share: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilteredPaste:
        """
        Creates a new text paste. Optionally creates a share link in the same request.

        Parameters
        ----------
        name : str

        content : str

        type : str

        share : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredPaste
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_paste(
            name="name",
            content="content",
            type="type",
        )
        """
        _response = self._raw_client.post_paste(
            name=name, content=content, type=type, share=share, request_options=request_options
        )
        return _response.data

    def post_search(
        self,
        *,
        query: str,
        folder_id: typing.Optional[str] = OMIT,
        recursive: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostSearchResponse:
        """
        Searches for files and folders using a query and optional folder ID

        Parameters
        ----------
        query : str

        folder_id : typing.Optional[str]

        recursive : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostSearchResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_search(
            query="query",
        )
        """
        _response = self._raw_client.post_search(
            query=query, folder_id=folder_id, recursive=recursive, request_options=request_options
        )
        return _response.data

    def get_share(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[FilteredShare]:
        """
        Returns all share links owned by the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FilteredShare]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_share()
        """
        _response = self._raw_client.get_share(request_options=request_options)
        return _response.data

    def post_share(
        self,
        *,
        type: PostShareRequestType,
        id: str,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilteredShare:
        """
        Creates a public share link for a file, folder, collection, or paste.

        Parameters
        ----------
        type : PostShareRequestType

        id : str

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredShare
            OK

        Examples
        --------
        from fern import FernApi, PostShareRequestType

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_share(
            type=PostShareRequestType.FILE,
            id="id",
        )
        """
        _response = self._raw_client.post_share(type=type, id=id, password=password, request_options=request_options)
        return _response.data

    def post_uploads(
        self, *, total_bytes: float, request_options: typing.Optional[RequestOptions] = None
    ) -> FilteredFileUpload:
        """
        Initialises a multi-part file upload session and returns an upload ID.
        Use the upload ID to push data chunks, then finalise by creating a file.

        Parameters
        ----------
        total_bytes : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredFileUpload
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_uploads(
            total_bytes=1.1,
        )
        """
        _response = self._raw_client.post_uploads(total_bytes=total_bytes, request_options=request_options)
        return _response.data

    def get_usage_largest(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FilteredFile]:
        """
        Returns the authenticated user's top 10 files sorted by size descending.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FilteredFile]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_usage_largest()
        """
        _response = self._raw_client.get_usage_largest(request_options=request_options)
        return _response.data

    def get_usage_stats(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetUsageStatsResponse:
        """
        Returns the authenticated user's current usage counters for storage, files, folders,
        pastes, collections, shares, and tokens alongside their configured per-user limits.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUsageStatsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_usage_stats()
        """
        _response = self._raw_client.get_usage_stats(request_options=request_options)
        return _response.data

    def get_admin_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FilteredAdminUser]:
        """
        Returns all registered users including their storage usage. Requires an admin session token.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FilteredAdminUser]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_admin_users()
        """
        _response = self._raw_client.get_admin_users(request_options=request_options)
        return _response.data

    def post_admin_users(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Creates a new user account. Requires an admin session token.

        Parameters
        ----------
        username : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_admin_users(
            username="username",
            password="password",
        )
        """
        _response = self._raw_client.post_admin_users(
            username=username, password=password, request_options=request_options
        )
        return _response.data

    def get_file_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> FilteredFile:
        """
        Returns metadata for a file by ID. Accessible via a valid share link or as the owner.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredFile
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_file_id(
            id="id",
        )
        """
        _response = self._raw_client.get_file_id(id, request_options=request_options)
        return _response.data

    def delete_file_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes a file and its stored content.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_file_id(
            id="id",
        )
        """
        _response = self._raw_client.delete_file_id(id, request_options=request_options)
        return _response.data

    def patch_file_id(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the name or parent folder of a file.

        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        folder_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.patch_file_id(
            id="id",
        )
        """
        _response = self._raw_client.patch_file_id(id, name=name, folder_id=folder_id, request_options=request_options)
        return _response.data

    def get_file_id_raw(
        self, id: str, *, share_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Streams the raw file content with the appropriate Content-Type header.
        Accessible via a valid share link or as the owner.

        Parameters
        ----------
        id : str

        share_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_file_id_raw(
            id="id",
        )
        """
        _response = self._raw_client.get_file_id_raw(id, share_id=share_id, request_options=request_options)
        return _response.data

    def get_share_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> FilteredShare:
        """
        Returns share metadata and increments the view counter. Publicly accessible.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredShare
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_share_id(
            id="id",
        )
        """
        _response = self._raw_client.get_share_id(id, request_options=request_options)
        return _response.data

    def delete_share_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Revokes a share link, making the shared resource inaccessible to anonymous users.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_share_id(
            id="id",
        )
        """
        _response = self._raw_client.delete_share_id(id, request_options=request_options)
        return _response.data

    def patch_share_id(
        self, id: str, *, password: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Allows the owner of a share to update its password.

        Parameters
        ----------
        id : str

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.patch_share_id(
            id="id",
        )
        """
        _response = self._raw_client.patch_share_id(id, password=password, request_options=request_options)
        return _response.data

    def post_uploads_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilteredFileUpload:
        """
        Appends a raw binary chunk to an in-progress upload session.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredFileUpload
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.post_uploads_id(
            id="id",
        )
        """
        _response = self._raw_client.post_uploads_id(id, request_options=request_options)
        return _response.data

    def delete_uploads_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Cancels and deletes an in-progress upload session.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_uploads_id(
            id="id",
        )
        """
        _response = self._raw_client.delete_uploads_id(id, request_options=request_options)
        return _response.data

    def get_admin_users_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilteredAdminUser:
        """
        Get info about a specific user and their storage usage/limits. Requires an admin session token.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredAdminUser
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_admin_users_id(
            id="id",
        )
        """
        _response = self._raw_client.get_admin_users_id(id, request_options=request_options)
        return _response.data

    def delete_admin_users_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes a user account and all associated data. Requires an admin session token.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_admin_users_id(
            id="id",
        )
        """
        _response = self._raw_client.delete_admin_users_id(id, request_options=request_options)
        return _response.data

    def patch_admin_users_id(
        self,
        id: str,
        *,
        type: typing.Optional[PatchAdminUsersIdRequestType] = OMIT,
        storage_limit: typing.Optional[float] = OMIT,
        file_limit: typing.Optional[float] = OMIT,
        folder_limit: typing.Optional[float] = OMIT,
        paste_limit: typing.Optional[float] = OMIT,
        collection_limit: typing.Optional[float] = OMIT,
        share_limit: typing.Optional[float] = OMIT,
        token_limit: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the role of a specific user. Requires an admin session token.

        Parameters
        ----------
        id : str

        type : typing.Optional[PatchAdminUsersIdRequestType]

        storage_limit : typing.Optional[float]

        file_limit : typing.Optional[float]

        folder_limit : typing.Optional[float]

        paste_limit : typing.Optional[float]

        collection_limit : typing.Optional[float]

        share_limit : typing.Optional[float]

        token_limit : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.patch_admin_users_id(
            id="id",
        )
        """
        _response = self._raw_client.patch_admin_users_id(
            id,
            type=type,
            storage_limit=storage_limit,
            file_limit=file_limit,
            folder_limit=folder_limit,
            paste_limit=paste_limit,
            collection_limit=collection_limit,
            share_limit=share_limit,
            token_limit=token_limit,
            request_options=request_options,
        )
        return _response.data


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
    base_url : str
        The base url to use for requests from the client.

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
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
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
            base_url=base_url,
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

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def get_admin_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> Config:
        """
        Returns the current server configuration. Requires an admin session token.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Config
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_admin_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_admin_config(request_options=request_options)
        return _response.data

    async def patch_admin_config(
        self,
        *,
        max_users: float,
        disable_registration: PatchAdminConfigRequestDisableRegistration,
        total: PatchAdminConfigRequestTotal,
        user: PatchAdminConfigRequestUser,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Applies partial updates to the server configuration. Requires an admin session token.

        Parameters
        ----------
        max_users : float

        disable_registration : PatchAdminConfigRequestDisableRegistration

        total : PatchAdminConfigRequestTotal

        user : PatchAdminConfigRequestUser

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            PatchAdminConfigRequestDisableRegistrationOne,
            PatchAdminConfigRequestTotal,
            PatchAdminConfigRequestUser,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.patch_admin_config(
                max_users=1.1,
                disable_registration=PatchAdminConfigRequestDisableRegistrationOne.AFTER_FIRST_USER,
                total=PatchAdminConfigRequestTotal(
                    max_files=1.1,
                    max_folders=1.1,
                    max_pastes=1.1,
                    max_collections=1.1,
                    max_shares=1.1,
                    max_storage=1.1,
                ),
                user=PatchAdminConfigRequestUser(
                    max_files=1.1,
                    max_folders=1.1,
                    max_pastes=1.1,
                    max_collections=1.1,
                    max_shares=1.1,
                    max_tokens=1.1,
                    max_storage=1.1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_admin_config(
            max_users=max_users,
            disable_registration=disable_registration,
            total=total,
            user=user,
            request_options=request_options,
        )
        return _response.data

    async def get_admin_usage(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAdminUsageResponse:
        """
        Returns server-wide usage counters for storage, files, folders, pastes, collections,
        and shares alongside their configured limits. Requires an admin session token.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAdminUsageResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_admin_usage()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_admin_usage(request_options=request_options)
        return _response.data

    async def post_auth_login(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostAuthLoginResponse:
        """
        Authenticates with a username and password and returns a session token.

        Parameters
        ----------
        username : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthLoginResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_auth_login(
                username="username",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_auth_login(
            username=username, password=password, request_options=request_options
        )
        return _response.data

    async def post_auth_register(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostAuthRegisterResponse:
        """
        Creates a new user account and returns a session token. May be disabled by server configuration.

        Parameters
        ----------
        username : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthRegisterResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_auth_register(
                username="username",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_auth_register(
            username=username, password=password, request_options=request_options
        )
        return _response.data

    async def get_collection_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilteredCollection:
        """
        Returns a collection by ID. Accessible via a valid share link or as the owner.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredCollection
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_collection_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collection_id(id, request_options=request_options)
        return _response.data

    async def delete_collection_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes a collection. The files inside are not deleted.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_collection_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_collection_id(id, request_options=request_options)
        return _response.data

    async def patch_collection_id(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        file_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the name or file membership of a collection.

        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        file_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.patch_collection_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_collection_id(
            id, name=name, file_ids=file_ids, request_options=request_options
        )
        return _response.data

    async def get_collection(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FilteredCollection]:
        """
        Returns all collections owned by the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FilteredCollection]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_collection()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collection(request_options=request_options)
        return _response.data

    async def post_collection(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FilteredCollection:
        """
        Creates a new empty collection for grouping files.

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredCollection
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_collection(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_collection(name=name, request_options=request_options)
        return _response.data

    async def post_file(self, *, request_options: typing.Optional[RequestOptions] = None) -> FilteredFile:
        """
        Creates a new file record. Supply either an `uploadId` from a completed chunked upload
        or raw `data` bytes for small files. Optionally creates a share link in the same request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredFile
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_file()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_file(request_options=request_options)
        return _response.data

    async def get_folder_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilteredFolder:
        """
        Returns a folder and its contents by ID. Accessible via a valid share link or as the owner.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredFolder
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_folder_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_folder_id(id, request_options=request_options)
        return _response.data

    async def delete_folder_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes a folder and all files inside it.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_folder_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_folder_id(id, request_options=request_options)
        return _response.data

    async def patch_folder_id(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the name or parent folder of an existing folder.

        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        parent_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.patch_folder_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_folder_id(
            id, name=name, parent_id=parent_id, request_options=request_options
        )
        return _response.data

    async def get_folder(self, *, request_options: typing.Optional[RequestOptions] = None) -> FilteredFolder:
        """
        Returns the authenticated user's root folder.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredFolder
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_folder()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_folder(request_options=request_options)
        return _response.data

    async def post_folder(
        self,
        *,
        name: str,
        parent_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilteredFolder:
        """
        Create a new folder under an optional parent.

        Parameters
        ----------
        name : str

        parent_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredFolder
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_folder(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_folder(name=name, parent_id=parent_id, request_options=request_options)
        return _response.data

    async def delete_me_collections(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes all collections owned by the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_me_collections()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_me_collections(request_options=request_options)
        return _response.data

    async def delete_me_files(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes all files and folders owned by the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_me_files()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_me_files(request_options=request_options)
        return _response.data

    async def get_me(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetMeResponse:
        """
        Returns the authenticated user's ID, username, and role.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMeResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_me()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_me(request_options=request_options)
        return _response.data

    async def delete_me(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes the authenticated user's account and all associated data.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_me()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_me(request_options=request_options)
        return _response.data

    async def patch_me(self, *, username: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Updates the authenticated user's username.

        Parameters
        ----------
        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.patch_me(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_me(username=username, request_options=request_options)
        return _response.data

    async def post_me_logout(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Invalidates the current session token.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_me_logout()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_me_logout(request_options=request_options)
        return _response.data

    async def patch_me_password(
        self, *, current_password: str, new_password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Updates the authenticated user's password after verifying the current one.

        Parameters
        ----------
        current_password : str

        new_password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.patch_me_password(
                current_password="currentPassword",
                new_password="newPassword",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_me_password(
            current_password=current_password, new_password=new_password, request_options=request_options
        )
        return _response.data

    async def delete_me_pastes(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes all pastes owned by the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_me_pastes()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_me_pastes(request_options=request_options)
        return _response.data

    async def delete_me_shares(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes all share links owned by the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_me_shares()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_me_shares(request_options=request_options)
        return _response.data

    async def get_me_tokens(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FilteredToken]:
        """
        Returns all API tokens for the authenticated user, sorted with the current token first.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FilteredToken]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_me_tokens()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_me_tokens(request_options=request_options)
        return _response.data

    async def post_me_tokens(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostMeTokensResponse:
        """
        Creates a new named uploader API token for programmatic access.

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostMeTokensResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_me_tokens(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_me_tokens(name=name, request_options=request_options)
        return _response.data

    async def delete_me_tokens(
        self, *, id: DeleteMeTokensRequestId, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a specific token by ID, all tokens, or all tokens except the current session.

        Parameters
        ----------
        id : DeleteMeTokensRequestId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, DeleteMeTokensRequestIdZero

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_me_tokens(
                id=DeleteMeTokensRequestIdZero.ALL,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_me_tokens(id=id, request_options=request_options)
        return _response.data

    async def patch_me_tokens(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PatchMeTokensResponse:
        """
        Regenerates a token by ID. Only applicable to uploader tokens.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchMeTokensResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.patch_me_tokens(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_me_tokens(id=id, request_options=request_options)
        return _response.data

    async def get_paste_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> FilteredPaste:
        """
        Returns a paste including its full content.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredPaste
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_paste_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_paste_id(id, request_options=request_options)
        return _response.data

    async def delete_paste_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes a paste.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_paste_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_paste_id(id, request_options=request_options)
        return _response.data

    async def patch_paste_id(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        content: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilteredPaste:
        """
        Updates the name, content, or syntax type of a paste.

        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        content : typing.Optional[str]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredPaste
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.patch_paste_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_paste_id(
            id, name=name, content=content, type=type, request_options=request_options
        )
        return _response.data

    async def get_paste(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[FilteredPaste]:
        """
        Returns all pastes owned by the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FilteredPaste]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_paste()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_paste(request_options=request_options)
        return _response.data

    async def post_paste(
        self,
        *,
        name: str,
        content: str,
        type: str,
        share: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilteredPaste:
        """
        Creates a new text paste. Optionally creates a share link in the same request.

        Parameters
        ----------
        name : str

        content : str

        type : str

        share : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredPaste
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_paste(
                name="name",
                content="content",
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_paste(
            name=name, content=content, type=type, share=share, request_options=request_options
        )
        return _response.data

    async def post_search(
        self,
        *,
        query: str,
        folder_id: typing.Optional[str] = OMIT,
        recursive: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostSearchResponse:
        """
        Searches for files and folders using a query and optional folder ID

        Parameters
        ----------
        query : str

        folder_id : typing.Optional[str]

        recursive : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostSearchResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_search(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_search(
            query=query, folder_id=folder_id, recursive=recursive, request_options=request_options
        )
        return _response.data

    async def get_share(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[FilteredShare]:
        """
        Returns all share links owned by the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FilteredShare]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_share()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_share(request_options=request_options)
        return _response.data

    async def post_share(
        self,
        *,
        type: PostShareRequestType,
        id: str,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilteredShare:
        """
        Creates a public share link for a file, folder, collection, or paste.

        Parameters
        ----------
        type : PostShareRequestType

        id : str

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredShare
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PostShareRequestType

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_share(
                type=PostShareRequestType.FILE,
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_share(
            type=type, id=id, password=password, request_options=request_options
        )
        return _response.data

    async def post_uploads(
        self, *, total_bytes: float, request_options: typing.Optional[RequestOptions] = None
    ) -> FilteredFileUpload:
        """
        Initialises a multi-part file upload session and returns an upload ID.
        Use the upload ID to push data chunks, then finalise by creating a file.

        Parameters
        ----------
        total_bytes : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredFileUpload
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_uploads(
                total_bytes=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_uploads(total_bytes=total_bytes, request_options=request_options)
        return _response.data

    async def get_usage_largest(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FilteredFile]:
        """
        Returns the authenticated user's top 10 files sorted by size descending.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FilteredFile]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_usage_largest()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_usage_largest(request_options=request_options)
        return _response.data

    async def get_usage_stats(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUsageStatsResponse:
        """
        Returns the authenticated user's current usage counters for storage, files, folders,
        pastes, collections, shares, and tokens alongside their configured per-user limits.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUsageStatsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_usage_stats()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_usage_stats(request_options=request_options)
        return _response.data

    async def get_admin_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FilteredAdminUser]:
        """
        Returns all registered users including their storage usage. Requires an admin session token.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FilteredAdminUser]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_admin_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_admin_users(request_options=request_options)
        return _response.data

    async def post_admin_users(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Creates a new user account. Requires an admin session token.

        Parameters
        ----------
        username : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_admin_users(
                username="username",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_admin_users(
            username=username, password=password, request_options=request_options
        )
        return _response.data

    async def get_file_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> FilteredFile:
        """
        Returns metadata for a file by ID. Accessible via a valid share link or as the owner.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredFile
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_file_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_id(id, request_options=request_options)
        return _response.data

    async def delete_file_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes a file and its stored content.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_file_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file_id(id, request_options=request_options)
        return _response.data

    async def patch_file_id(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the name or parent folder of a file.

        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        folder_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.patch_file_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_file_id(
            id, name=name, folder_id=folder_id, request_options=request_options
        )
        return _response.data

    async def get_file_id_raw(
        self, id: str, *, share_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Streams the raw file content with the appropriate Content-Type header.
        Accessible via a valid share link or as the owner.

        Parameters
        ----------
        id : str

        share_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_file_id_raw(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_id_raw(id, share_id=share_id, request_options=request_options)
        return _response.data

    async def get_share_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> FilteredShare:
        """
        Returns share metadata and increments the view counter. Publicly accessible.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredShare
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_share_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_share_id(id, request_options=request_options)
        return _response.data

    async def delete_share_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Revokes a share link, making the shared resource inaccessible to anonymous users.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_share_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_share_id(id, request_options=request_options)
        return _response.data

    async def patch_share_id(
        self, id: str, *, password: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Allows the owner of a share to update its password.

        Parameters
        ----------
        id : str

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.patch_share_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_share_id(id, password=password, request_options=request_options)
        return _response.data

    async def post_uploads_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilteredFileUpload:
        """
        Appends a raw binary chunk to an in-progress upload session.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredFileUpload
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.post_uploads_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_uploads_id(id, request_options=request_options)
        return _response.data

    async def delete_uploads_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Cancels and deletes an in-progress upload session.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_uploads_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_uploads_id(id, request_options=request_options)
        return _response.data

    async def get_admin_users_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilteredAdminUser:
        """
        Get info about a specific user and their storage usage/limits. Requires an admin session token.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilteredAdminUser
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_admin_users_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_admin_users_id(id, request_options=request_options)
        return _response.data

    async def delete_admin_users_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes a user account and all associated data. Requires an admin session token.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_admin_users_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_admin_users_id(id, request_options=request_options)
        return _response.data

    async def patch_admin_users_id(
        self,
        id: str,
        *,
        type: typing.Optional[PatchAdminUsersIdRequestType] = OMIT,
        storage_limit: typing.Optional[float] = OMIT,
        file_limit: typing.Optional[float] = OMIT,
        folder_limit: typing.Optional[float] = OMIT,
        paste_limit: typing.Optional[float] = OMIT,
        collection_limit: typing.Optional[float] = OMIT,
        share_limit: typing.Optional[float] = OMIT,
        token_limit: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the role of a specific user. Requires an admin session token.

        Parameters
        ----------
        id : str

        type : typing.Optional[PatchAdminUsersIdRequestType]

        storage_limit : typing.Optional[float]

        file_limit : typing.Optional[float]

        folder_limit : typing.Optional[float]

        paste_limit : typing.Optional[float]

        collection_limit : typing.Optional[float]

        share_limit : typing.Optional[float]

        token_limit : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.patch_admin_users_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_admin_users_id(
            id,
            type=type,
            storage_limit=storage_limit,
            file_limit=file_limit,
            folder_limit=folder_limit,
            paste_limit=paste_limit,
            collection_limit=collection_limit,
            share_limit=share_limit,
            token_limit=token_limit,
            request_options=request_options,
        )
        return _response.data
