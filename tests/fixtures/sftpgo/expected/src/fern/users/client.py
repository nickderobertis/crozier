

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_response import ApiResponse
from ..types.filesystem_config import FilesystemConfig
from ..types.group_mapping import GroupMapping
from ..types.permission import Permission
from ..types.user import User
from ..types.user_filters import UserFilters
from ..types.virtual_folder import VirtualFolder
from .raw_client import AsyncRawUsersClient, RawUsersClient
from .types.get_users_request_order import GetUsersRequestOrder


OMIT = typing.cast(typing.Any, ...)


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsersClient
        """
        return self._raw_client

    def get_users(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetUsersRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[User]:
        """
        Returns an array with one or more users. For security reasons hashed passwords are omitted in the response

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetUsersRequestOrder]
            Ordering users by username. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[User]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.get_users()
        """
        _response = self._raw_client.get_users(offset=offset, limit=limit, order=order, request_options=request_options)
        return _response.data

    def add_user(
        self,
        *,
        confidential_data: typing.Optional[int] = None,
        id: typing.Optional[int] = OMIT,
        status: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        expiration_date: typing.Optional[int] = OMIT,
        password: typing.Optional[str] = OMIT,
        public_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        has_password: typing.Optional[bool] = OMIT,
        home_dir: typing.Optional[str] = OMIT,
        virtual_folders: typing.Optional[typing.Sequence[VirtualFolder]] = OMIT,
        uid: typing.Optional[int] = OMIT,
        gid: typing.Optional[int] = OMIT,
        max_sessions: typing.Optional[int] = OMIT,
        quota_size: typing.Optional[int] = OMIT,
        quota_files: typing.Optional[int] = OMIT,
        permissions: typing.Optional[typing.Dict[str, typing.Sequence[Permission]]] = OMIT,
        used_quota_size: typing.Optional[int] = OMIT,
        used_quota_files: typing.Optional[int] = OMIT,
        last_quota_update: typing.Optional[int] = OMIT,
        upload_bandwidth: typing.Optional[int] = OMIT,
        download_bandwidth: typing.Optional[int] = OMIT,
        upload_data_transfer: typing.Optional[int] = OMIT,
        download_data_transfer: typing.Optional[int] = OMIT,
        total_data_transfer: typing.Optional[int] = OMIT,
        used_upload_data_transfer: typing.Optional[int] = OMIT,
        used_download_data_transfer: typing.Optional[int] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_login: typing.Optional[int] = OMIT,
        first_download: typing.Optional[int] = OMIT,
        first_upload: typing.Optional[int] = OMIT,
        last_password_change: typing.Optional[int] = OMIT,
        filters: typing.Optional[UserFilters] = OMIT,
        filesystem: typing.Optional[FilesystemConfig] = OMIT,
        additional_info: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[GroupMapping]] = OMIT,
        oidc_custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        role: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Adds a new user.Recovery codes and TOTP configuration cannot be set using this API: each user must use the specific APIs

        Parameters
        ----------
        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the hash of the password and the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        id : typing.Optional[int]

        status : typing.Optional[int]
            status:
              * `0` user is disabled, login is not allowed
              * `1` user is enabled

        username : typing.Optional[str]
            username is unique

        email : typing.Optional[str]

        description : typing.Optional[str]
            optional description, for example the user full name

        expiration_date : typing.Optional[int]
            expiration date as unix timestamp in milliseconds. An expired account cannot login. 0 means no expiration

        password : typing.Optional[str]
            If the password has no known hashing algo prefix it will be stored, by default, using bcrypt, argon2id is supported too. You can send a password hashed as bcrypt ($2a$ prefix), argon2id, pbkdf2 or unix crypt and it will be stored as is. For security reasons this field is omitted when you search/get users

        public_keys : typing.Optional[typing.Sequence[str]]
            Public keys in OpenSSH format.

        has_password : typing.Optional[bool]
            Indicates whether the password is set

        home_dir : typing.Optional[str]
            path to the user home directory. The user cannot upload or download files outside this directory. SFTPGo tries to automatically create this folder if missing. Must be an absolute path

        virtual_folders : typing.Optional[typing.Sequence[VirtualFolder]]
            mapping between virtual SFTPGo paths and virtual folders

        uid : typing.Optional[int]
            if you run SFTPGo as root user, the created files and directories will be assigned to this uid. 0 means no change, the owner will be the user that runs SFTPGo. Ignored on windows

        gid : typing.Optional[int]
            if you run SFTPGo as root user, the created files and directories will be assigned to this gid. 0 means no change, the group will be the one of the user that runs SFTPGo. Ignored on windows

        max_sessions : typing.Optional[int]
            Maximum number of concurrent sessions and file transfers for the user. Under bursts of near-simultaneous connections, the count can briefly exceed the configured limit. 0 means unlimited

        quota_size : typing.Optional[int]
            Quota as size in bytes. 0 means unlimited. Please note that quota is updated if files are added/removed via SFTPGo otherwise a quota scan or a manual quota update is needed

        quota_files : typing.Optional[int]
            Quota as number of files. 0 means unlimited. Please note that quota is updated if files are added/removed via SFTPGo otherwise a quota scan or a manual quota update is needed

        permissions : typing.Optional[typing.Dict[str, typing.Sequence[Permission]]]
            hash map with directory as key and an array of permissions as value. Directories must be absolute paths, permissions for root directory ("/") are required

        used_quota_size : typing.Optional[int]

        used_quota_files : typing.Optional[int]

        last_quota_update : typing.Optional[int]
            Last quota update as unix timestamp in milliseconds

        upload_bandwidth : typing.Optional[int]
            Maximum upload bandwidth in KB/s per upload, 0 means unlimited

        download_bandwidth : typing.Optional[int]
            Maximum download bandwidth in KB/s per upload, 0 means unlimited

        upload_data_transfer : typing.Optional[int]
            Maximum data transfer allowed for uploads as MB. 0 means no limit

        download_data_transfer : typing.Optional[int]
            Maximum data transfer allowed for downloads as MB. 0 means no limit

        total_data_transfer : typing.Optional[int]
            Maximum total data transfer as MB. 0 means unlimited. You can set a total data transfer instead of the individual values for uploads and downloads

        used_upload_data_transfer : typing.Optional[int]
            Uploaded size, as bytes, since the last reset

        used_download_data_transfer : typing.Optional[int]
            Downloaded size, as bytes, since the last reset

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds. It will be 0 for users created before v2.2.0

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_login : typing.Optional[int]
            Last user login as unix timestamp in milliseconds. It is saved at most once every 10 minutes

        first_download : typing.Optional[int]
            first download time as unix timestamp in milliseconds

        first_upload : typing.Optional[int]
            first upload time as unix timestamp in milliseconds

        last_password_change : typing.Optional[int]
            last password change time as unix timestamp in milliseconds

        filters : typing.Optional[UserFilters]

        filesystem : typing.Optional[FilesystemConfig]

        additional_info : typing.Optional[str]
            Free form text field for external systems

        groups : typing.Optional[typing.Sequence[GroupMapping]]

        oidc_custom_fields : typing.Optional[typing.Dict[str, typing.Any]]
            This field is passed to the pre-login hook if custom OIDC token fields have been configured. Field values can be of any type (this is a free form object) and depend on the type of the configured OIDC token fields

        role : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.add_user()
        """
        _response = self._raw_client.add_user(
            confidential_data=confidential_data,
            id=id,
            status=status,
            username=username,
            email=email,
            description=description,
            expiration_date=expiration_date,
            password=password,
            public_keys=public_keys,
            has_password=has_password,
            home_dir=home_dir,
            virtual_folders=virtual_folders,
            uid=uid,
            gid=gid,
            max_sessions=max_sessions,
            quota_size=quota_size,
            quota_files=quota_files,
            permissions=permissions,
            used_quota_size=used_quota_size,
            used_quota_files=used_quota_files,
            last_quota_update=last_quota_update,
            upload_bandwidth=upload_bandwidth,
            download_bandwidth=download_bandwidth,
            upload_data_transfer=upload_data_transfer,
            download_data_transfer=download_data_transfer,
            total_data_transfer=total_data_transfer,
            used_upload_data_transfer=used_upload_data_transfer,
            used_download_data_transfer=used_download_data_transfer,
            created_at=created_at,
            updated_at=updated_at,
            last_login=last_login,
            first_download=first_download,
            first_upload=first_upload,
            last_password_change=last_password_change,
            filters=filters,
            filesystem=filesystem,
            additional_info=additional_info,
            groups=groups,
            oidc_custom_fields=oidc_custom_fields,
            role=role,
            request_options=request_options,
        )
        return _response.data

    def get_user_by_username(
        self,
        username: str,
        *,
        confidential_data: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Returns the user with the given username if it exists. For security reasons the hashed password is omitted in the response

        Parameters
        ----------
        username : str
            the username

        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the hash of the password and the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.get_user_by_username(
            username="username",
        )
        """
        _response = self._raw_client.get_user_by_username(
            username, confidential_data=confidential_data, request_options=request_options
        )
        return _response.data

    def update_user(
        self,
        username_: str,
        *,
        disconnect: typing.Optional[int] = None,
        id: typing.Optional[int] = OMIT,
        status: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        expiration_date: typing.Optional[int] = OMIT,
        password: typing.Optional[str] = OMIT,
        public_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        has_password: typing.Optional[bool] = OMIT,
        home_dir: typing.Optional[str] = OMIT,
        virtual_folders: typing.Optional[typing.Sequence[VirtualFolder]] = OMIT,
        uid: typing.Optional[int] = OMIT,
        gid: typing.Optional[int] = OMIT,
        max_sessions: typing.Optional[int] = OMIT,
        quota_size: typing.Optional[int] = OMIT,
        quota_files: typing.Optional[int] = OMIT,
        permissions: typing.Optional[typing.Dict[str, typing.Sequence[Permission]]] = OMIT,
        used_quota_size: typing.Optional[int] = OMIT,
        used_quota_files: typing.Optional[int] = OMIT,
        last_quota_update: typing.Optional[int] = OMIT,
        upload_bandwidth: typing.Optional[int] = OMIT,
        download_bandwidth: typing.Optional[int] = OMIT,
        upload_data_transfer: typing.Optional[int] = OMIT,
        download_data_transfer: typing.Optional[int] = OMIT,
        total_data_transfer: typing.Optional[int] = OMIT,
        used_upload_data_transfer: typing.Optional[int] = OMIT,
        used_download_data_transfer: typing.Optional[int] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_login: typing.Optional[int] = OMIT,
        first_download: typing.Optional[int] = OMIT,
        first_upload: typing.Optional[int] = OMIT,
        last_password_change: typing.Optional[int] = OMIT,
        filters: typing.Optional[UserFilters] = OMIT,
        filesystem: typing.Optional[FilesystemConfig] = OMIT,
        additional_info: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[GroupMapping]] = OMIT,
        oidc_custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        role: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing user and optionally disconnects it, if connected, to apply the new settings. The current password will be preserved if the password field is omitted in the request body. Recovery codes and TOTP configuration cannot be set/updated using this API: each user must use the specific APIs

        Parameters
        ----------
        username_ : str
            the username

        disconnect : typing.Optional[int]
            Disconnect:
              * `0` The user will not be disconnected and it will continue to use the old configuration until connected. This is the default
              * `1` The user will be disconnected after a successful update. It must login again and so it will be forced to use the new configuration

        id : typing.Optional[int]

        status : typing.Optional[int]
            status:
              * `0` user is disabled, login is not allowed
              * `1` user is enabled

        username : typing.Optional[str]
            username is unique

        email : typing.Optional[str]

        description : typing.Optional[str]
            optional description, for example the user full name

        expiration_date : typing.Optional[int]
            expiration date as unix timestamp in milliseconds. An expired account cannot login. 0 means no expiration

        password : typing.Optional[str]
            If the password has no known hashing algo prefix it will be stored, by default, using bcrypt, argon2id is supported too. You can send a password hashed as bcrypt ($2a$ prefix), argon2id, pbkdf2 or unix crypt and it will be stored as is. For security reasons this field is omitted when you search/get users

        public_keys : typing.Optional[typing.Sequence[str]]
            Public keys in OpenSSH format.

        has_password : typing.Optional[bool]
            Indicates whether the password is set

        home_dir : typing.Optional[str]
            path to the user home directory. The user cannot upload or download files outside this directory. SFTPGo tries to automatically create this folder if missing. Must be an absolute path

        virtual_folders : typing.Optional[typing.Sequence[VirtualFolder]]
            mapping between virtual SFTPGo paths and virtual folders

        uid : typing.Optional[int]
            if you run SFTPGo as root user, the created files and directories will be assigned to this uid. 0 means no change, the owner will be the user that runs SFTPGo. Ignored on windows

        gid : typing.Optional[int]
            if you run SFTPGo as root user, the created files and directories will be assigned to this gid. 0 means no change, the group will be the one of the user that runs SFTPGo. Ignored on windows

        max_sessions : typing.Optional[int]
            Maximum number of concurrent sessions and file transfers for the user. Under bursts of near-simultaneous connections, the count can briefly exceed the configured limit. 0 means unlimited

        quota_size : typing.Optional[int]
            Quota as size in bytes. 0 means unlimited. Please note that quota is updated if files are added/removed via SFTPGo otherwise a quota scan or a manual quota update is needed

        quota_files : typing.Optional[int]
            Quota as number of files. 0 means unlimited. Please note that quota is updated if files are added/removed via SFTPGo otherwise a quota scan or a manual quota update is needed

        permissions : typing.Optional[typing.Dict[str, typing.Sequence[Permission]]]
            hash map with directory as key and an array of permissions as value. Directories must be absolute paths, permissions for root directory ("/") are required

        used_quota_size : typing.Optional[int]

        used_quota_files : typing.Optional[int]

        last_quota_update : typing.Optional[int]
            Last quota update as unix timestamp in milliseconds

        upload_bandwidth : typing.Optional[int]
            Maximum upload bandwidth in KB/s per upload, 0 means unlimited

        download_bandwidth : typing.Optional[int]
            Maximum download bandwidth in KB/s per upload, 0 means unlimited

        upload_data_transfer : typing.Optional[int]
            Maximum data transfer allowed for uploads as MB. 0 means no limit

        download_data_transfer : typing.Optional[int]
            Maximum data transfer allowed for downloads as MB. 0 means no limit

        total_data_transfer : typing.Optional[int]
            Maximum total data transfer as MB. 0 means unlimited. You can set a total data transfer instead of the individual values for uploads and downloads

        used_upload_data_transfer : typing.Optional[int]
            Uploaded size, as bytes, since the last reset

        used_download_data_transfer : typing.Optional[int]
            Downloaded size, as bytes, since the last reset

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds. It will be 0 for users created before v2.2.0

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_login : typing.Optional[int]
            Last user login as unix timestamp in milliseconds. It is saved at most once every 10 minutes

        first_download : typing.Optional[int]
            first download time as unix timestamp in milliseconds

        first_upload : typing.Optional[int]
            first upload time as unix timestamp in milliseconds

        last_password_change : typing.Optional[int]
            last password change time as unix timestamp in milliseconds

        filters : typing.Optional[UserFilters]

        filesystem : typing.Optional[FilesystemConfig]

        additional_info : typing.Optional[str]
            Free form text field for external systems

        groups : typing.Optional[typing.Sequence[GroupMapping]]

        oidc_custom_fields : typing.Optional[typing.Dict[str, typing.Any]]
            This field is passed to the pre-login hook if custom OIDC token fields have been configured. Field values can be of any type (this is a free form object) and depend on the type of the configured OIDC token fields

        role : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.update_user(
            username_="username",
        )
        """
        _response = self._raw_client.update_user(
            username_,
            disconnect=disconnect,
            id=id,
            status=status,
            username=username,
            email=email,
            description=description,
            expiration_date=expiration_date,
            password=password,
            public_keys=public_keys,
            has_password=has_password,
            home_dir=home_dir,
            virtual_folders=virtual_folders,
            uid=uid,
            gid=gid,
            max_sessions=max_sessions,
            quota_size=quota_size,
            quota_files=quota_files,
            permissions=permissions,
            used_quota_size=used_quota_size,
            used_quota_files=used_quota_files,
            last_quota_update=last_quota_update,
            upload_bandwidth=upload_bandwidth,
            download_bandwidth=download_bandwidth,
            upload_data_transfer=upload_data_transfer,
            download_data_transfer=download_data_transfer,
            total_data_transfer=total_data_transfer,
            used_upload_data_transfer=used_upload_data_transfer,
            used_download_data_transfer=used_download_data_transfer,
            created_at=created_at,
            updated_at=updated_at,
            last_login=last_login,
            first_download=first_download,
            first_upload=first_upload,
            last_password_change=last_password_change,
            filters=filters,
            filesystem=filesystem,
            additional_info=additional_info,
            groups=groups,
            oidc_custom_fields=oidc_custom_fields,
            role=role,
            request_options=request_options,
        )
        return _response.data

    def delete_user(self, username: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Deletes an existing user

        Parameters
        ----------
        username : str
            the username

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.delete_user(
            username="username",
        )
        """
        _response = self._raw_client.delete_user(username, request_options=request_options)
        return _response.data

    def disable_user2fa(self, username: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Disables second factor authentication for the given user. This API must be used if the user loses access to their second factor auth device and has no recovery codes

        Parameters
        ----------
        username : str
            the username

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.disable_user2fa(
            username="username",
        )
        """
        _response = self._raw_client.disable_user2fa(username, request_options=request_options)
        return _response.data

    def user_forgot_password(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        You must configure an SMTP server. SFTPGo will send a code via email to reset the password if the specified user exists, has a valid email address and does not have the "reset-password-disabled" restriction. Requests that do not meet these conditions are silently ignored (a success response will be returned) to avoid disclosing existing users

        Parameters
        ----------
        username : str
            the username

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.user_forgot_password(
            username="username",
        )
        """
        _response = self._raw_client.user_forgot_password(username, request_options=request_options)
        return _response.data

    def user_reset_password(
        self,
        username: str,
        *,
        code: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Set a new password using the code received via email

        Parameters
        ----------
        username : str
            the username

        code : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.users.user_reset_password(
            username="username",
        )
        """
        _response = self._raw_client.user_reset_password(
            username, code=code, password=password, request_options=request_options
        )
        return _response.data


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsersClient
        """
        return self._raw_client

    async def get_users(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetUsersRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[User]:
        """
        Returns an array with one or more users. For security reasons hashed passwords are omitted in the response

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetUsersRequestOrder]
            Ordering users by username. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[User]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.users.get_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users(
            offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    async def add_user(
        self,
        *,
        confidential_data: typing.Optional[int] = None,
        id: typing.Optional[int] = OMIT,
        status: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        expiration_date: typing.Optional[int] = OMIT,
        password: typing.Optional[str] = OMIT,
        public_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        has_password: typing.Optional[bool] = OMIT,
        home_dir: typing.Optional[str] = OMIT,
        virtual_folders: typing.Optional[typing.Sequence[VirtualFolder]] = OMIT,
        uid: typing.Optional[int] = OMIT,
        gid: typing.Optional[int] = OMIT,
        max_sessions: typing.Optional[int] = OMIT,
        quota_size: typing.Optional[int] = OMIT,
        quota_files: typing.Optional[int] = OMIT,
        permissions: typing.Optional[typing.Dict[str, typing.Sequence[Permission]]] = OMIT,
        used_quota_size: typing.Optional[int] = OMIT,
        used_quota_files: typing.Optional[int] = OMIT,
        last_quota_update: typing.Optional[int] = OMIT,
        upload_bandwidth: typing.Optional[int] = OMIT,
        download_bandwidth: typing.Optional[int] = OMIT,
        upload_data_transfer: typing.Optional[int] = OMIT,
        download_data_transfer: typing.Optional[int] = OMIT,
        total_data_transfer: typing.Optional[int] = OMIT,
        used_upload_data_transfer: typing.Optional[int] = OMIT,
        used_download_data_transfer: typing.Optional[int] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_login: typing.Optional[int] = OMIT,
        first_download: typing.Optional[int] = OMIT,
        first_upload: typing.Optional[int] = OMIT,
        last_password_change: typing.Optional[int] = OMIT,
        filters: typing.Optional[UserFilters] = OMIT,
        filesystem: typing.Optional[FilesystemConfig] = OMIT,
        additional_info: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[GroupMapping]] = OMIT,
        oidc_custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        role: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Adds a new user.Recovery codes and TOTP configuration cannot be set using this API: each user must use the specific APIs

        Parameters
        ----------
        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the hash of the password and the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        id : typing.Optional[int]

        status : typing.Optional[int]
            status:
              * `0` user is disabled, login is not allowed
              * `1` user is enabled

        username : typing.Optional[str]
            username is unique

        email : typing.Optional[str]

        description : typing.Optional[str]
            optional description, for example the user full name

        expiration_date : typing.Optional[int]
            expiration date as unix timestamp in milliseconds. An expired account cannot login. 0 means no expiration

        password : typing.Optional[str]
            If the password has no known hashing algo prefix it will be stored, by default, using bcrypt, argon2id is supported too. You can send a password hashed as bcrypt ($2a$ prefix), argon2id, pbkdf2 or unix crypt and it will be stored as is. For security reasons this field is omitted when you search/get users

        public_keys : typing.Optional[typing.Sequence[str]]
            Public keys in OpenSSH format.

        has_password : typing.Optional[bool]
            Indicates whether the password is set

        home_dir : typing.Optional[str]
            path to the user home directory. The user cannot upload or download files outside this directory. SFTPGo tries to automatically create this folder if missing. Must be an absolute path

        virtual_folders : typing.Optional[typing.Sequence[VirtualFolder]]
            mapping between virtual SFTPGo paths and virtual folders

        uid : typing.Optional[int]
            if you run SFTPGo as root user, the created files and directories will be assigned to this uid. 0 means no change, the owner will be the user that runs SFTPGo. Ignored on windows

        gid : typing.Optional[int]
            if you run SFTPGo as root user, the created files and directories will be assigned to this gid. 0 means no change, the group will be the one of the user that runs SFTPGo. Ignored on windows

        max_sessions : typing.Optional[int]
            Maximum number of concurrent sessions and file transfers for the user. Under bursts of near-simultaneous connections, the count can briefly exceed the configured limit. 0 means unlimited

        quota_size : typing.Optional[int]
            Quota as size in bytes. 0 means unlimited. Please note that quota is updated if files are added/removed via SFTPGo otherwise a quota scan or a manual quota update is needed

        quota_files : typing.Optional[int]
            Quota as number of files. 0 means unlimited. Please note that quota is updated if files are added/removed via SFTPGo otherwise a quota scan or a manual quota update is needed

        permissions : typing.Optional[typing.Dict[str, typing.Sequence[Permission]]]
            hash map with directory as key and an array of permissions as value. Directories must be absolute paths, permissions for root directory ("/") are required

        used_quota_size : typing.Optional[int]

        used_quota_files : typing.Optional[int]

        last_quota_update : typing.Optional[int]
            Last quota update as unix timestamp in milliseconds

        upload_bandwidth : typing.Optional[int]
            Maximum upload bandwidth in KB/s per upload, 0 means unlimited

        download_bandwidth : typing.Optional[int]
            Maximum download bandwidth in KB/s per upload, 0 means unlimited

        upload_data_transfer : typing.Optional[int]
            Maximum data transfer allowed for uploads as MB. 0 means no limit

        download_data_transfer : typing.Optional[int]
            Maximum data transfer allowed for downloads as MB. 0 means no limit

        total_data_transfer : typing.Optional[int]
            Maximum total data transfer as MB. 0 means unlimited. You can set a total data transfer instead of the individual values for uploads and downloads

        used_upload_data_transfer : typing.Optional[int]
            Uploaded size, as bytes, since the last reset

        used_download_data_transfer : typing.Optional[int]
            Downloaded size, as bytes, since the last reset

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds. It will be 0 for users created before v2.2.0

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_login : typing.Optional[int]
            Last user login as unix timestamp in milliseconds. It is saved at most once every 10 minutes

        first_download : typing.Optional[int]
            first download time as unix timestamp in milliseconds

        first_upload : typing.Optional[int]
            first upload time as unix timestamp in milliseconds

        last_password_change : typing.Optional[int]
            last password change time as unix timestamp in milliseconds

        filters : typing.Optional[UserFilters]

        filesystem : typing.Optional[FilesystemConfig]

        additional_info : typing.Optional[str]
            Free form text field for external systems

        groups : typing.Optional[typing.Sequence[GroupMapping]]

        oidc_custom_fields : typing.Optional[typing.Dict[str, typing.Any]]
            This field is passed to the pre-login hook if custom OIDC token fields have been configured. Field values can be of any type (this is a free form object) and depend on the type of the configured OIDC token fields

        role : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.users.add_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.add_user(
            confidential_data=confidential_data,
            id=id,
            status=status,
            username=username,
            email=email,
            description=description,
            expiration_date=expiration_date,
            password=password,
            public_keys=public_keys,
            has_password=has_password,
            home_dir=home_dir,
            virtual_folders=virtual_folders,
            uid=uid,
            gid=gid,
            max_sessions=max_sessions,
            quota_size=quota_size,
            quota_files=quota_files,
            permissions=permissions,
            used_quota_size=used_quota_size,
            used_quota_files=used_quota_files,
            last_quota_update=last_quota_update,
            upload_bandwidth=upload_bandwidth,
            download_bandwidth=download_bandwidth,
            upload_data_transfer=upload_data_transfer,
            download_data_transfer=download_data_transfer,
            total_data_transfer=total_data_transfer,
            used_upload_data_transfer=used_upload_data_transfer,
            used_download_data_transfer=used_download_data_transfer,
            created_at=created_at,
            updated_at=updated_at,
            last_login=last_login,
            first_download=first_download,
            first_upload=first_upload,
            last_password_change=last_password_change,
            filters=filters,
            filesystem=filesystem,
            additional_info=additional_info,
            groups=groups,
            oidc_custom_fields=oidc_custom_fields,
            role=role,
            request_options=request_options,
        )
        return _response.data

    async def get_user_by_username(
        self,
        username: str,
        *,
        confidential_data: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Returns the user with the given username if it exists. For security reasons the hashed password is omitted in the response

        Parameters
        ----------
        username : str
            the username

        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the hash of the password and the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.users.get_user_by_username(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_by_username(
            username, confidential_data=confidential_data, request_options=request_options
        )
        return _response.data

    async def update_user(
        self,
        username_: str,
        *,
        disconnect: typing.Optional[int] = None,
        id: typing.Optional[int] = OMIT,
        status: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        expiration_date: typing.Optional[int] = OMIT,
        password: typing.Optional[str] = OMIT,
        public_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        has_password: typing.Optional[bool] = OMIT,
        home_dir: typing.Optional[str] = OMIT,
        virtual_folders: typing.Optional[typing.Sequence[VirtualFolder]] = OMIT,
        uid: typing.Optional[int] = OMIT,
        gid: typing.Optional[int] = OMIT,
        max_sessions: typing.Optional[int] = OMIT,
        quota_size: typing.Optional[int] = OMIT,
        quota_files: typing.Optional[int] = OMIT,
        permissions: typing.Optional[typing.Dict[str, typing.Sequence[Permission]]] = OMIT,
        used_quota_size: typing.Optional[int] = OMIT,
        used_quota_files: typing.Optional[int] = OMIT,
        last_quota_update: typing.Optional[int] = OMIT,
        upload_bandwidth: typing.Optional[int] = OMIT,
        download_bandwidth: typing.Optional[int] = OMIT,
        upload_data_transfer: typing.Optional[int] = OMIT,
        download_data_transfer: typing.Optional[int] = OMIT,
        total_data_transfer: typing.Optional[int] = OMIT,
        used_upload_data_transfer: typing.Optional[int] = OMIT,
        used_download_data_transfer: typing.Optional[int] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_login: typing.Optional[int] = OMIT,
        first_download: typing.Optional[int] = OMIT,
        first_upload: typing.Optional[int] = OMIT,
        last_password_change: typing.Optional[int] = OMIT,
        filters: typing.Optional[UserFilters] = OMIT,
        filesystem: typing.Optional[FilesystemConfig] = OMIT,
        additional_info: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[GroupMapping]] = OMIT,
        oidc_custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        role: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing user and optionally disconnects it, if connected, to apply the new settings. The current password will be preserved if the password field is omitted in the request body. Recovery codes and TOTP configuration cannot be set/updated using this API: each user must use the specific APIs

        Parameters
        ----------
        username_ : str
            the username

        disconnect : typing.Optional[int]
            Disconnect:
              * `0` The user will not be disconnected and it will continue to use the old configuration until connected. This is the default
              * `1` The user will be disconnected after a successful update. It must login again and so it will be forced to use the new configuration

        id : typing.Optional[int]

        status : typing.Optional[int]
            status:
              * `0` user is disabled, login is not allowed
              * `1` user is enabled

        username : typing.Optional[str]
            username is unique

        email : typing.Optional[str]

        description : typing.Optional[str]
            optional description, for example the user full name

        expiration_date : typing.Optional[int]
            expiration date as unix timestamp in milliseconds. An expired account cannot login. 0 means no expiration

        password : typing.Optional[str]
            If the password has no known hashing algo prefix it will be stored, by default, using bcrypt, argon2id is supported too. You can send a password hashed as bcrypt ($2a$ prefix), argon2id, pbkdf2 or unix crypt and it will be stored as is. For security reasons this field is omitted when you search/get users

        public_keys : typing.Optional[typing.Sequence[str]]
            Public keys in OpenSSH format.

        has_password : typing.Optional[bool]
            Indicates whether the password is set

        home_dir : typing.Optional[str]
            path to the user home directory. The user cannot upload or download files outside this directory. SFTPGo tries to automatically create this folder if missing. Must be an absolute path

        virtual_folders : typing.Optional[typing.Sequence[VirtualFolder]]
            mapping between virtual SFTPGo paths and virtual folders

        uid : typing.Optional[int]
            if you run SFTPGo as root user, the created files and directories will be assigned to this uid. 0 means no change, the owner will be the user that runs SFTPGo. Ignored on windows

        gid : typing.Optional[int]
            if you run SFTPGo as root user, the created files and directories will be assigned to this gid. 0 means no change, the group will be the one of the user that runs SFTPGo. Ignored on windows

        max_sessions : typing.Optional[int]
            Maximum number of concurrent sessions and file transfers for the user. Under bursts of near-simultaneous connections, the count can briefly exceed the configured limit. 0 means unlimited

        quota_size : typing.Optional[int]
            Quota as size in bytes. 0 means unlimited. Please note that quota is updated if files are added/removed via SFTPGo otherwise a quota scan or a manual quota update is needed

        quota_files : typing.Optional[int]
            Quota as number of files. 0 means unlimited. Please note that quota is updated if files are added/removed via SFTPGo otherwise a quota scan or a manual quota update is needed

        permissions : typing.Optional[typing.Dict[str, typing.Sequence[Permission]]]
            hash map with directory as key and an array of permissions as value. Directories must be absolute paths, permissions for root directory ("/") are required

        used_quota_size : typing.Optional[int]

        used_quota_files : typing.Optional[int]

        last_quota_update : typing.Optional[int]
            Last quota update as unix timestamp in milliseconds

        upload_bandwidth : typing.Optional[int]
            Maximum upload bandwidth in KB/s per upload, 0 means unlimited

        download_bandwidth : typing.Optional[int]
            Maximum download bandwidth in KB/s per upload, 0 means unlimited

        upload_data_transfer : typing.Optional[int]
            Maximum data transfer allowed for uploads as MB. 0 means no limit

        download_data_transfer : typing.Optional[int]
            Maximum data transfer allowed for downloads as MB. 0 means no limit

        total_data_transfer : typing.Optional[int]
            Maximum total data transfer as MB. 0 means unlimited. You can set a total data transfer instead of the individual values for uploads and downloads

        used_upload_data_transfer : typing.Optional[int]
            Uploaded size, as bytes, since the last reset

        used_download_data_transfer : typing.Optional[int]
            Downloaded size, as bytes, since the last reset

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds. It will be 0 for users created before v2.2.0

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_login : typing.Optional[int]
            Last user login as unix timestamp in milliseconds. It is saved at most once every 10 minutes

        first_download : typing.Optional[int]
            first download time as unix timestamp in milliseconds

        first_upload : typing.Optional[int]
            first upload time as unix timestamp in milliseconds

        last_password_change : typing.Optional[int]
            last password change time as unix timestamp in milliseconds

        filters : typing.Optional[UserFilters]

        filesystem : typing.Optional[FilesystemConfig]

        additional_info : typing.Optional[str]
            Free form text field for external systems

        groups : typing.Optional[typing.Sequence[GroupMapping]]

        oidc_custom_fields : typing.Optional[typing.Dict[str, typing.Any]]
            This field is passed to the pre-login hook if custom OIDC token fields have been configured. Field values can be of any type (this is a free form object) and depend on the type of the configured OIDC token fields

        role : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.users.update_user(
                username_="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user(
            username_,
            disconnect=disconnect,
            id=id,
            status=status,
            username=username,
            email=email,
            description=description,
            expiration_date=expiration_date,
            password=password,
            public_keys=public_keys,
            has_password=has_password,
            home_dir=home_dir,
            virtual_folders=virtual_folders,
            uid=uid,
            gid=gid,
            max_sessions=max_sessions,
            quota_size=quota_size,
            quota_files=quota_files,
            permissions=permissions,
            used_quota_size=used_quota_size,
            used_quota_files=used_quota_files,
            last_quota_update=last_quota_update,
            upload_bandwidth=upload_bandwidth,
            download_bandwidth=download_bandwidth,
            upload_data_transfer=upload_data_transfer,
            download_data_transfer=download_data_transfer,
            total_data_transfer=total_data_transfer,
            used_upload_data_transfer=used_upload_data_transfer,
            used_download_data_transfer=used_download_data_transfer,
            created_at=created_at,
            updated_at=updated_at,
            last_login=last_login,
            first_download=first_download,
            first_upload=first_upload,
            last_password_change=last_password_change,
            filters=filters,
            filesystem=filesystem,
            additional_info=additional_info,
            groups=groups,
            oidc_custom_fields=oidc_custom_fields,
            role=role,
            request_options=request_options,
        )
        return _response.data

    async def delete_user(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Deletes an existing user

        Parameters
        ----------
        username : str
            the username

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.users.delete_user(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user(username, request_options=request_options)
        return _response.data

    async def disable_user2fa(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Disables second factor authentication for the given user. This API must be used if the user loses access to their second factor auth device and has no recovery codes

        Parameters
        ----------
        username : str
            the username

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.users.disable_user2fa(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disable_user2fa(username, request_options=request_options)
        return _response.data

    async def user_forgot_password(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        You must configure an SMTP server. SFTPGo will send a code via email to reset the password if the specified user exists, has a valid email address and does not have the "reset-password-disabled" restriction. Requests that do not meet these conditions are silently ignored (a success response will be returned) to avoid disclosing existing users

        Parameters
        ----------
        username : str
            the username

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.users.user_forgot_password(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.user_forgot_password(username, request_options=request_options)
        return _response.data

    async def user_reset_password(
        self,
        username: str,
        *,
        code: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Set a new password using the code received via email

        Parameters
        ----------
        username : str
            the username

        code : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.users.user_reset_password(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.user_reset_password(
            username, code=code, password=password, request_options=request_options
        )
        return _response.data
