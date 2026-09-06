

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_response import ApiResponse
from ..types.dir_entry import DirEntry
from ..types.mfa_protocols import MfaProtocols
from ..types.recovery_code import RecoveryCode
from ..types.secret import Secret
from ..types.share import Share
from ..types.share_scope import ShareScope
from ..types.totp_config import TotpConfig
from ..types.user_profile import UserProfile
from .raw_client import AsyncRawUserApIsClient, RawUserApIsClient
from .types.generate_user_totp_secret_response import GenerateUserTotpSecretResponse
from .types.get_user_shares_request_order import GetUserSharesRequestOrder


OMIT = typing.cast(typing.Any, ...)


class UserApIsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserApIsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserApIsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserApIsClient
        """
        return self._raw_client

    def change_user_password(
        self,
        *,
        current_password: typing.Optional[str] = OMIT,
        new_password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Changes the password for the logged in user

        Parameters
        ----------
        current_password : typing.Optional[str]

        new_password : typing.Optional[str]

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
        client.user_ap_is.change_user_password()
        """
        _response = self._raw_client.change_user_password(
            current_password=current_password, new_password=new_password, request_options=request_options
        )
        return _response.data

    def get_user_profile(self, *, request_options: typing.Optional[RequestOptions] = None) -> UserProfile:
        """
        Returns the profile for the logged in user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserProfile
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_ap_is.get_user_profile()
        """
        _response = self._raw_client.get_user_profile(request_options=request_options)
        return _response.data

    def update_user_profile(
        self,
        *,
        email: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        allow_api_key_auth: typing.Optional[bool] = OMIT,
        public_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Allows to update the profile for the logged in user

        Parameters
        ----------
        email : typing.Optional[str]

        description : typing.Optional[str]

        allow_api_key_auth : typing.Optional[bool]
            If enabled, you can impersonate this user, in REST API, using an API key. If disabled user credentials are required for impersonation

        public_keys : typing.Optional[typing.Sequence[str]]

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
        client.user_ap_is.update_user_profile()
        """
        _response = self._raw_client.update_user_profile(
            email=email,
            description=description,
            allow_api_key_auth=allow_api_key_auth,
            public_keys=public_keys,
            request_options=request_options,
        )
        return _response.data

    def get_user_recovery_codes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RecoveryCode]:
        """
        Returns the recovery codes for the logged in user. Recovery codes can be used if the user loses access to their second factor auth device. Recovery codes are returned unencrypted

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RecoveryCode]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_ap_is.get_user_recovery_codes()
        """
        _response = self._raw_client.get_user_recovery_codes(request_options=request_options)
        return _response.data

    def generate_user_recovery_codes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Generates new recovery codes for the logged in user. Generating new recovery codes you automatically invalidate old ones

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_ap_is.generate_user_recovery_codes()
        """
        _response = self._raw_client.generate_user_recovery_codes(request_options=request_options)
        return _response.data

    def get_user_totp_configs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TotpConfig]:
        """
        Returns the available TOTP configurations for the logged in user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TotpConfig]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_ap_is.get_user_totp_configs()
        """
        _response = self._raw_client.get_user_totp_configs(request_options=request_options)
        return _response.data

    def generate_user_totp_secret(
        self, *, config_name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> GenerateUserTotpSecretResponse:
        """
        Generates a new TOTP secret, including the QR code as png, using the specified configuration for the logged in user

        Parameters
        ----------
        config_name : typing.Optional[str]
            name of the configuration to use to generate the secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerateUserTotpSecretResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_ap_is.generate_user_totp_secret()
        """
        _response = self._raw_client.generate_user_totp_secret(config_name=config_name, request_options=request_options)
        return _response.data

    def validate_user_totp_secret(
        self,
        *,
        config_name: typing.Optional[str] = OMIT,
        passcode: typing.Optional[str] = OMIT,
        secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Checks if the given authentication code can be validated using the specified secret and config name

        Parameters
        ----------
        config_name : typing.Optional[str]
            name of the configuration to use to validate the passcode

        passcode : typing.Optional[str]
            passcode to validate

        secret : typing.Optional[str]
            secret to use to validate the passcode

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
        client.user_ap_is.validate_user_totp_secret()
        """
        _response = self._raw_client.validate_user_totp_secret(
            config_name=config_name, passcode=passcode, secret=secret, request_options=request_options
        )
        return _response.data

    def save_user_totp_config(
        self,
        *,
        protocols: typing.Optional[typing.Sequence[MfaProtocols]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        config_name: typing.Optional[str] = OMIT,
        secret: typing.Optional[Secret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Saves the specified TOTP config for the logged in user

        Parameters
        ----------
        protocols : typing.Optional[typing.Sequence[MfaProtocols]]
            TOTP will be required for the specified protocols. SSH protocol (SFTP/SCP/SSH commands) will ask for the TOTP passcode if the client uses keyboard interactive authentication. FTP has no standard way to support two factor authentication, if you enable the FTP support, you have to add the TOTP passcode after the password. For example if your password is "password" and your one time passcode is "123456" you have to use "password123456" as password. WebDAV is not supported since each single request must be authenticated and a passcode cannot be reused.

        enabled : typing.Optional[bool]

        config_name : typing.Optional[str]
            This name must be defined within the "totp" section of the SFTPGo configuration file. You will be unable to save a user/admin referencing a missing config_name

        secret : typing.Optional[Secret]

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
        client.user_ap_is.save_user_totp_config()
        """
        _response = self._raw_client.save_user_totp_config(
            protocols=protocols,
            enabled=enabled,
            config_name=config_name,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def get_user_shares(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetUserSharesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Share]:
        """
        Returns the share for the logged in user

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetUserSharesRequestOrder]
            Ordering shares by ID. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Share]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_ap_is.get_user_shares()
        """
        _response = self._raw_client.get_user_shares(
            offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    def add_share(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        scope: typing.Optional[ShareScope] = OMIT,
        paths: typing.Optional[typing.Sequence[str]] = OMIT,
        username: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_use_at: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        password: typing.Optional[str] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        used_tokens: typing.Optional[int] = OMIT,
        allow_from: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Adds a new share. The share id will be auto-generated

        Parameters
        ----------
        id : typing.Optional[str]
            auto-generated unique share identifier

        name : typing.Optional[str]

        description : typing.Optional[str]
            optional description

        scope : typing.Optional[ShareScope]

        paths : typing.Optional[typing.Sequence[str]]
            paths to files or directories, for share scope write this array must contain exactly one directory. Paths will not be validated on save so you can also create them after creating the share

        username : typing.Optional[str]

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_use_at : typing.Optional[int]
            last use time as unix timestamp in milliseconds

        expires_at : typing.Optional[int]
            optional share expiration, as unix timestamp in milliseconds. 0 means no expiration

        password : typing.Optional[str]
            optional password to protect the share. The special value "[**redacted**]" means that a password has been set, you can use this value if you want to preserve the current password when you update a share

        max_tokens : typing.Optional[int]
            maximum allowed access tokens. 0 means no limit

        used_tokens : typing.Optional[int]

        allow_from : typing.Optional[typing.Sequence[str]]
            Limit the share availability to these IP/Mask. IP/Mask must be in CIDR notation as defined in RFC 4632 and RFC 4291, for example "192.0.2.0/24" or "2001:db8::/32". An empty list means no restrictions

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
        client.user_ap_is.add_share()
        """
        _response = self._raw_client.add_share(
            id=id,
            name=name,
            description=description,
            scope=scope,
            paths=paths,
            username=username,
            created_at=created_at,
            updated_at=updated_at,
            last_use_at=last_use_at,
            expires_at=expires_at,
            password=password,
            max_tokens=max_tokens,
            used_tokens=used_tokens,
            allow_from=allow_from,
            request_options=request_options,
        )
        return _response.data

    def get_user_share_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Share:
        """
        Returns a share by id for the logged in user

        Parameters
        ----------
        id : str
            the share id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Share
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_ap_is.get_user_share_by_id(
            id="id",
        )
        """
        _response = self._raw_client.get_user_share_by_id(id, request_options=request_options)
        return _response.data

    def update_user_share(
        self,
        id_: str,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        scope: typing.Optional[ShareScope] = OMIT,
        paths: typing.Optional[typing.Sequence[str]] = OMIT,
        username: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_use_at: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        password: typing.Optional[str] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        used_tokens: typing.Optional[int] = OMIT,
        allow_from: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing share belonging to the logged in user

        Parameters
        ----------
        id_ : str
            the share id

        id : typing.Optional[str]
            auto-generated unique share identifier

        name : typing.Optional[str]

        description : typing.Optional[str]
            optional description

        scope : typing.Optional[ShareScope]

        paths : typing.Optional[typing.Sequence[str]]
            paths to files or directories, for share scope write this array must contain exactly one directory. Paths will not be validated on save so you can also create them after creating the share

        username : typing.Optional[str]

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_use_at : typing.Optional[int]
            last use time as unix timestamp in milliseconds

        expires_at : typing.Optional[int]
            optional share expiration, as unix timestamp in milliseconds. 0 means no expiration

        password : typing.Optional[str]
            optional password to protect the share. The special value "[**redacted**]" means that a password has been set, you can use this value if you want to preserve the current password when you update a share

        max_tokens : typing.Optional[int]
            maximum allowed access tokens. 0 means no limit

        used_tokens : typing.Optional[int]

        allow_from : typing.Optional[typing.Sequence[str]]
            Limit the share availability to these IP/Mask. IP/Mask must be in CIDR notation as defined in RFC 4632 and RFC 4291, for example "192.0.2.0/24" or "2001:db8::/32". An empty list means no restrictions

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
        client.user_ap_is.update_user_share(
            id_="id",
        )
        """
        _response = self._raw_client.update_user_share(
            id_,
            id=id,
            name=name,
            description=description,
            scope=scope,
            paths=paths,
            username=username,
            created_at=created_at,
            updated_at=updated_at,
            last_use_at=last_use_at,
            expires_at=expires_at,
            password=password,
            max_tokens=max_tokens,
            used_tokens=used_tokens,
            allow_from=allow_from,
            request_options=request_options,
        )
        return _response.data

    def delete_user_share(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Deletes an existing share belonging to the logged in user

        Parameters
        ----------
        id : str
            the share id

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
        client.user_ap_is.delete_user_share(
            id="id",
        )
        """
        _response = self._raw_client.delete_user_share(id, request_options=request_options)
        return _response.data

    def copy_a_file_or_a_directory(
        self, *, path: str, target: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Parameters
        ----------
        path : str
            Path to the file/folder to copy. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"

        target : str
            New name. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"

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
        client.user_ap_is.copy_a_file_or_a_directory(
            path="path",
            target="target",
        )
        """
        _response = self._raw_client.copy_a_file_or_a_directory(
            path=path, target=target, request_options=request_options
        )
        return _response.data

    def move_rename_a_file_or_a_directory(
        self, *, path: str, target: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Parameters
        ----------
        path : str
            Path to the file/folder to rename. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"

        target : str
            New name. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"

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
        client.user_ap_is.move_rename_a_file_or_a_directory(
            path="path",
            target="target",
        )
        """
        _response = self._raw_client.move_rename_a_file_or_a_directory(
            path=path, target=target, request_options=request_options
        )
        return _response.data

    def get_user_dir_contents(
        self, *, path: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DirEntry]:
        """
        Returns the contents of the specified directory for the logged in user

        Parameters
        ----------
        path : typing.Optional[str]
            Path to the folder to read. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir". If empty or missing the user's start directory is assumed. If relative, the user's start directory is used as the base

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DirEntry]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_ap_is.get_user_dir_contents()
        """
        _response = self._raw_client.get_user_dir_contents(path=path, request_options=request_options)
        return _response.data

    def create_user_dir(
        self,
        *,
        path: str,
        mkdir_parents: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Create a directory for the logged in user

        Parameters
        ----------
        path : str
            Path to the folder to create. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"

        mkdir_parents : typing.Optional[bool]
            Create parent directories if they do not exist?

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
        client.user_ap_is.create_user_dir(
            path="path",
        )
        """
        _response = self._raw_client.create_user_dir(
            path=path, mkdir_parents=mkdir_parents, request_options=request_options
        )
        return _response.data

    def delete_user_dir(self, *, path: str, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Delete a directory and any children it contains for the logged in user

        Parameters
        ----------
        path : str
            Path to the folder to delete. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"

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
        client.user_ap_is.delete_user_dir(
            path="path",
        )
        """
        _response = self._raw_client.delete_user_dir(path=path, request_options=request_options)
        return _response.data

    def rename_user_dir(
        self, *, path: str, target: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Rename a directory for the logged in user. The rename is allowed for empty directory or for non empty local directories, with no virtual folders inside

        Parameters
        ----------
        path : str
            Path to the folder to rename. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"

        target : str
            New name. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"

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
        client.user_ap_is.rename_user_dir(
            path="path",
            target="target",
        )
        """
        _response = self._raw_client.rename_user_dir(path=path, target=target, request_options=request_options)
        return _response.data

    def download_user_file(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Returns the file contents as response body

        Parameters
        ----------
        path : str
            Path to the file to download. It must be URL encoded, for example the path "my dir/àdir/file.txt" must be sent as "my%20dir%2F%C3%A0dir%2Ffile.txt"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_ap_is.download_user_file(
            path="path",
        )
        """
        with self._raw_client.download_user_file(path=path, request_options=request_options) as r:
            yield from r.data

    def create_user_files(
        self,
        *,
        path: typing.Optional[str] = None,
        mkdir_parents: typing.Optional[bool] = None,
        filenames: typing.Optional[typing.List[core.File]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Upload one or more files for the logged in user

        Parameters
        ----------
        path : typing.Optional[str]
            Parent directory for the uploaded files. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir". If empty or missing the root path is assumed. If a file with the same name already exists, it will be overwritten

        mkdir_parents : typing.Optional[bool]
            Create parent directories if they do not exist?

        filenames : typing.Optional[typing.List[core.File]]
            See core.File for more documentation

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
        client.user_ap_is.create_user_files()
        """
        _response = self._raw_client.create_user_files(
            path=path, mkdir_parents=mkdir_parents, filenames=filenames, request_options=request_options
        )
        return _response.data

    def delete_user_file(self, *, path: str, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Delete a file for the logged in user.

        Parameters
        ----------
        path : str
            Path to the file to delete. It must be URL encoded

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
        client.user_ap_is.delete_user_file(
            path="path",
        )
        """
        _response = self._raw_client.delete_user_file(path=path, request_options=request_options)
        return _response.data

    def rename_user_file(
        self, *, path: str, target: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Rename a file for the logged in user. Deprecated, use "file-actions/move"

        Parameters
        ----------
        path : str
            Path to the file to rename. It must be URL encoded

        target : str
            New name. It must be URL encoded

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
        client.user_ap_is.rename_user_file(
            path="path",
            target="target",
        )
        """
        _response = self._raw_client.rename_user_file(path=path, target=target, request_options=request_options)
        return _response.data

    def create_user_file(
        self,
        *,
        path: str,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        mkdir_parents: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Upload a single file for the logged in user to an existing directory. This API does not use multipart/form-data and so no temporary files are created server side but only a single file can be uploaded as POST body

        Parameters
        ----------
        path : str
            Full file path. It must be path encoded, for example the path "my dir/àdir/file.txt" must be sent as "my%20dir%2F%C3%A0dir%2Ffile.txt". The parent directory must exist. If a file with the same name already exists, it will be overwritten

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        mkdir_parents : typing.Optional[bool]
            Create parent directories if they do not exist?

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation
        """
        _response = self._raw_client.create_user_file(
            path=path, request=request, mkdir_parents=mkdir_parents, request_options=request_options
        )
        return _response.data

    def setprops_user_file(
        self,
        *,
        path: str,
        modification_time: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Set supported metadata attributes for the specified file or directory

        Parameters
        ----------
        path : str
            Full file/directory path. It must be URL encoded, for example the path "my dir/àdir/file.txt" must be sent as "my%20dir%2F%C3%A0dir%2Ffile.txt"

        modification_time : typing.Optional[int]
            File modification time as unix timestamp in milliseconds

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
        client.user_ap_is.setprops_user_file(
            path="path",
        )
        """
        _response = self._raw_client.setprops_user_file(
            path=path, modification_time=modification_time, request_options=request_options
        )
        return _response.data

    def streamzip(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        A zip file, containing the specified files and folders, will be generated on the fly and returned as response body. Only folders and regular files will be included in the zip

        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.user_ap_is.streamzip(
            request=["string", "string"],
        )
        """
        with self._raw_client.streamzip(request=request, request_options=request_options) as r:
            yield from r.data


class AsyncUserApIsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserApIsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserApIsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserApIsClient
        """
        return self._raw_client

    async def change_user_password(
        self,
        *,
        current_password: typing.Optional[str] = OMIT,
        new_password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Changes the password for the logged in user

        Parameters
        ----------
        current_password : typing.Optional[str]

        new_password : typing.Optional[str]

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
            await client.user_ap_is.change_user_password()


        asyncio.run(main())
        """
        _response = await self._raw_client.change_user_password(
            current_password=current_password, new_password=new_password, request_options=request_options
        )
        return _response.data

    async def get_user_profile(self, *, request_options: typing.Optional[RequestOptions] = None) -> UserProfile:
        """
        Returns the profile for the logged in user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserProfile
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
            await client.user_ap_is.get_user_profile()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_profile(request_options=request_options)
        return _response.data

    async def update_user_profile(
        self,
        *,
        email: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        allow_api_key_auth: typing.Optional[bool] = OMIT,
        public_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Allows to update the profile for the logged in user

        Parameters
        ----------
        email : typing.Optional[str]

        description : typing.Optional[str]

        allow_api_key_auth : typing.Optional[bool]
            If enabled, you can impersonate this user, in REST API, using an API key. If disabled user credentials are required for impersonation

        public_keys : typing.Optional[typing.Sequence[str]]

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
            await client.user_ap_is.update_user_profile()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user_profile(
            email=email,
            description=description,
            allow_api_key_auth=allow_api_key_auth,
            public_keys=public_keys,
            request_options=request_options,
        )
        return _response.data

    async def get_user_recovery_codes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RecoveryCode]:
        """
        Returns the recovery codes for the logged in user. Recovery codes can be used if the user loses access to their second factor auth device. Recovery codes are returned unencrypted

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RecoveryCode]
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
            await client.user_ap_is.get_user_recovery_codes()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_recovery_codes(request_options=request_options)
        return _response.data

    async def generate_user_recovery_codes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Generates new recovery codes for the logged in user. Generating new recovery codes you automatically invalidate old ones

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
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
            await client.user_ap_is.generate_user_recovery_codes()


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_user_recovery_codes(request_options=request_options)
        return _response.data

    async def get_user_totp_configs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TotpConfig]:
        """
        Returns the available TOTP configurations for the logged in user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TotpConfig]
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
            await client.user_ap_is.get_user_totp_configs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_totp_configs(request_options=request_options)
        return _response.data

    async def generate_user_totp_secret(
        self, *, config_name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> GenerateUserTotpSecretResponse:
        """
        Generates a new TOTP secret, including the QR code as png, using the specified configuration for the logged in user

        Parameters
        ----------
        config_name : typing.Optional[str]
            name of the configuration to use to generate the secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerateUserTotpSecretResponse
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
            await client.user_ap_is.generate_user_totp_secret()


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_user_totp_secret(
            config_name=config_name, request_options=request_options
        )
        return _response.data

    async def validate_user_totp_secret(
        self,
        *,
        config_name: typing.Optional[str] = OMIT,
        passcode: typing.Optional[str] = OMIT,
        secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Checks if the given authentication code can be validated using the specified secret and config name

        Parameters
        ----------
        config_name : typing.Optional[str]
            name of the configuration to use to validate the passcode

        passcode : typing.Optional[str]
            passcode to validate

        secret : typing.Optional[str]
            secret to use to validate the passcode

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
            await client.user_ap_is.validate_user_totp_secret()


        asyncio.run(main())
        """
        _response = await self._raw_client.validate_user_totp_secret(
            config_name=config_name, passcode=passcode, secret=secret, request_options=request_options
        )
        return _response.data

    async def save_user_totp_config(
        self,
        *,
        protocols: typing.Optional[typing.Sequence[MfaProtocols]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        config_name: typing.Optional[str] = OMIT,
        secret: typing.Optional[Secret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Saves the specified TOTP config for the logged in user

        Parameters
        ----------
        protocols : typing.Optional[typing.Sequence[MfaProtocols]]
            TOTP will be required for the specified protocols. SSH protocol (SFTP/SCP/SSH commands) will ask for the TOTP passcode if the client uses keyboard interactive authentication. FTP has no standard way to support two factor authentication, if you enable the FTP support, you have to add the TOTP passcode after the password. For example if your password is "password" and your one time passcode is "123456" you have to use "password123456" as password. WebDAV is not supported since each single request must be authenticated and a passcode cannot be reused.

        enabled : typing.Optional[bool]

        config_name : typing.Optional[str]
            This name must be defined within the "totp" section of the SFTPGo configuration file. You will be unable to save a user/admin referencing a missing config_name

        secret : typing.Optional[Secret]

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
            await client.user_ap_is.save_user_totp_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.save_user_totp_config(
            protocols=protocols,
            enabled=enabled,
            config_name=config_name,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def get_user_shares(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetUserSharesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Share]:
        """
        Returns the share for the logged in user

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetUserSharesRequestOrder]
            Ordering shares by ID. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Share]
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
            await client.user_ap_is.get_user_shares()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_shares(
            offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    async def add_share(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        scope: typing.Optional[ShareScope] = OMIT,
        paths: typing.Optional[typing.Sequence[str]] = OMIT,
        username: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_use_at: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        password: typing.Optional[str] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        used_tokens: typing.Optional[int] = OMIT,
        allow_from: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Adds a new share. The share id will be auto-generated

        Parameters
        ----------
        id : typing.Optional[str]
            auto-generated unique share identifier

        name : typing.Optional[str]

        description : typing.Optional[str]
            optional description

        scope : typing.Optional[ShareScope]

        paths : typing.Optional[typing.Sequence[str]]
            paths to files or directories, for share scope write this array must contain exactly one directory. Paths will not be validated on save so you can also create them after creating the share

        username : typing.Optional[str]

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_use_at : typing.Optional[int]
            last use time as unix timestamp in milliseconds

        expires_at : typing.Optional[int]
            optional share expiration, as unix timestamp in milliseconds. 0 means no expiration

        password : typing.Optional[str]
            optional password to protect the share. The special value "[**redacted**]" means that a password has been set, you can use this value if you want to preserve the current password when you update a share

        max_tokens : typing.Optional[int]
            maximum allowed access tokens. 0 means no limit

        used_tokens : typing.Optional[int]

        allow_from : typing.Optional[typing.Sequence[str]]
            Limit the share availability to these IP/Mask. IP/Mask must be in CIDR notation as defined in RFC 4632 and RFC 4291, for example "192.0.2.0/24" or "2001:db8::/32". An empty list means no restrictions

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
            await client.user_ap_is.add_share()


        asyncio.run(main())
        """
        _response = await self._raw_client.add_share(
            id=id,
            name=name,
            description=description,
            scope=scope,
            paths=paths,
            username=username,
            created_at=created_at,
            updated_at=updated_at,
            last_use_at=last_use_at,
            expires_at=expires_at,
            password=password,
            max_tokens=max_tokens,
            used_tokens=used_tokens,
            allow_from=allow_from,
            request_options=request_options,
        )
        return _response.data

    async def get_user_share_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Share:
        """
        Returns a share by id for the logged in user

        Parameters
        ----------
        id : str
            the share id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Share
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
            await client.user_ap_is.get_user_share_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_share_by_id(id, request_options=request_options)
        return _response.data

    async def update_user_share(
        self,
        id_: str,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        scope: typing.Optional[ShareScope] = OMIT,
        paths: typing.Optional[typing.Sequence[str]] = OMIT,
        username: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_use_at: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[int] = OMIT,
        password: typing.Optional[str] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        used_tokens: typing.Optional[int] = OMIT,
        allow_from: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing share belonging to the logged in user

        Parameters
        ----------
        id_ : str
            the share id

        id : typing.Optional[str]
            auto-generated unique share identifier

        name : typing.Optional[str]

        description : typing.Optional[str]
            optional description

        scope : typing.Optional[ShareScope]

        paths : typing.Optional[typing.Sequence[str]]
            paths to files or directories, for share scope write this array must contain exactly one directory. Paths will not be validated on save so you can also create them after creating the share

        username : typing.Optional[str]

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_use_at : typing.Optional[int]
            last use time as unix timestamp in milliseconds

        expires_at : typing.Optional[int]
            optional share expiration, as unix timestamp in milliseconds. 0 means no expiration

        password : typing.Optional[str]
            optional password to protect the share. The special value "[**redacted**]" means that a password has been set, you can use this value if you want to preserve the current password when you update a share

        max_tokens : typing.Optional[int]
            maximum allowed access tokens. 0 means no limit

        used_tokens : typing.Optional[int]

        allow_from : typing.Optional[typing.Sequence[str]]
            Limit the share availability to these IP/Mask. IP/Mask must be in CIDR notation as defined in RFC 4632 and RFC 4291, for example "192.0.2.0/24" or "2001:db8::/32". An empty list means no restrictions

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
            await client.user_ap_is.update_user_share(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_user_share(
            id_,
            id=id,
            name=name,
            description=description,
            scope=scope,
            paths=paths,
            username=username,
            created_at=created_at,
            updated_at=updated_at,
            last_use_at=last_use_at,
            expires_at=expires_at,
            password=password,
            max_tokens=max_tokens,
            used_tokens=used_tokens,
            allow_from=allow_from,
            request_options=request_options,
        )
        return _response.data

    async def delete_user_share(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Deletes an existing share belonging to the logged in user

        Parameters
        ----------
        id : str
            the share id

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
            await client.user_ap_is.delete_user_share(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user_share(id, request_options=request_options)
        return _response.data

    async def copy_a_file_or_a_directory(
        self, *, path: str, target: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Parameters
        ----------
        path : str
            Path to the file/folder to copy. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"

        target : str
            New name. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"

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
            await client.user_ap_is.copy_a_file_or_a_directory(
                path="path",
                target="target",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.copy_a_file_or_a_directory(
            path=path, target=target, request_options=request_options
        )
        return _response.data

    async def move_rename_a_file_or_a_directory(
        self, *, path: str, target: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Parameters
        ----------
        path : str
            Path to the file/folder to rename. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"

        target : str
            New name. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"

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
            await client.user_ap_is.move_rename_a_file_or_a_directory(
                path="path",
                target="target",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.move_rename_a_file_or_a_directory(
            path=path, target=target, request_options=request_options
        )
        return _response.data

    async def get_user_dir_contents(
        self, *, path: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DirEntry]:
        """
        Returns the contents of the specified directory for the logged in user

        Parameters
        ----------
        path : typing.Optional[str]
            Path to the folder to read. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir". If empty or missing the user's start directory is assumed. If relative, the user's start directory is used as the base

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DirEntry]
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
            await client.user_ap_is.get_user_dir_contents()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user_dir_contents(path=path, request_options=request_options)
        return _response.data

    async def create_user_dir(
        self,
        *,
        path: str,
        mkdir_parents: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Create a directory for the logged in user

        Parameters
        ----------
        path : str
            Path to the folder to create. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"

        mkdir_parents : typing.Optional[bool]
            Create parent directories if they do not exist?

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
            await client.user_ap_is.create_user_dir(
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_user_dir(
            path=path, mkdir_parents=mkdir_parents, request_options=request_options
        )
        return _response.data

    async def delete_user_dir(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Delete a directory and any children it contains for the logged in user

        Parameters
        ----------
        path : str
            Path to the folder to delete. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"

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
            await client.user_ap_is.delete_user_dir(
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user_dir(path=path, request_options=request_options)
        return _response.data

    async def rename_user_dir(
        self, *, path: str, target: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Rename a directory for the logged in user. The rename is allowed for empty directory or for non empty local directories, with no virtual folders inside

        Parameters
        ----------
        path : str
            Path to the folder to rename. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"

        target : str
            New name. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"

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
            await client.user_ap_is.rename_user_dir(
                path="path",
                target="target",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rename_user_dir(path=path, target=target, request_options=request_options)
        return _response.data

    async def download_user_file(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Returns the file contents as response body

        Parameters
        ----------
        path : str
            Path to the file to download. It must be URL encoded, for example the path "my dir/àdir/file.txt" must be sent as "my%20dir%2F%C3%A0dir%2Ffile.txt"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
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
            await client.user_ap_is.download_user_file(
                path="path",
            )


        asyncio.run(main())
        """
        async with self._raw_client.download_user_file(path=path, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def create_user_files(
        self,
        *,
        path: typing.Optional[str] = None,
        mkdir_parents: typing.Optional[bool] = None,
        filenames: typing.Optional[typing.List[core.File]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Upload one or more files for the logged in user

        Parameters
        ----------
        path : typing.Optional[str]
            Parent directory for the uploaded files. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir". If empty or missing the root path is assumed. If a file with the same name already exists, it will be overwritten

        mkdir_parents : typing.Optional[bool]
            Create parent directories if they do not exist?

        filenames : typing.Optional[typing.List[core.File]]
            See core.File for more documentation

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
            await client.user_ap_is.create_user_files()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_user_files(
            path=path, mkdir_parents=mkdir_parents, filenames=filenames, request_options=request_options
        )
        return _response.data

    async def delete_user_file(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Delete a file for the logged in user.

        Parameters
        ----------
        path : str
            Path to the file to delete. It must be URL encoded

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
            await client.user_ap_is.delete_user_file(
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user_file(path=path, request_options=request_options)
        return _response.data

    async def rename_user_file(
        self, *, path: str, target: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Rename a file for the logged in user. Deprecated, use "file-actions/move"

        Parameters
        ----------
        path : str
            Path to the file to rename. It must be URL encoded

        target : str
            New name. It must be URL encoded

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
            await client.user_ap_is.rename_user_file(
                path="path",
                target="target",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rename_user_file(path=path, target=target, request_options=request_options)
        return _response.data

    async def create_user_file(
        self,
        *,
        path: str,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        mkdir_parents: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Upload a single file for the logged in user to an existing directory. This API does not use multipart/form-data and so no temporary files are created server side but only a single file can be uploaded as POST body

        Parameters
        ----------
        path : str
            Full file path. It must be path encoded, for example the path "my dir/àdir/file.txt" must be sent as "my%20dir%2F%C3%A0dir%2Ffile.txt". The parent directory must exist. If a file with the same name already exists, it will be overwritten

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        mkdir_parents : typing.Optional[bool]
            Create parent directories if they do not exist?

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation
        """
        _response = await self._raw_client.create_user_file(
            path=path, request=request, mkdir_parents=mkdir_parents, request_options=request_options
        )
        return _response.data

    async def setprops_user_file(
        self,
        *,
        path: str,
        modification_time: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Set supported metadata attributes for the specified file or directory

        Parameters
        ----------
        path : str
            Full file/directory path. It must be URL encoded, for example the path "my dir/àdir/file.txt" must be sent as "my%20dir%2F%C3%A0dir%2Ffile.txt"

        modification_time : typing.Optional[int]
            File modification time as unix timestamp in milliseconds

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
            await client.user_ap_is.setprops_user_file(
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.setprops_user_file(
            path=path, modification_time=modification_time, request_options=request_options
        )
        return _response.data

    async def streamzip(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        A zip file, containing the specified files and folders, will be generated on the fly and returned as response body. Only folders and regular files will be included in the zip

        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
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
            await client.user_ap_is.streamzip(
                request=["string", "string"],
            )


        asyncio.run(main())
        """
        async with self._raw_client.streamzip(request=request, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
