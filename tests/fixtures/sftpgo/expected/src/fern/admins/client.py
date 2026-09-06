

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.admin import Admin
from ..types.admin_filters import AdminFilters
from ..types.admin_group_mapping import AdminGroupMapping
from ..types.admin_permissions import AdminPermissions
from ..types.admin_profile import AdminProfile
from ..types.api_response import ApiResponse
from ..types.recovery_code import RecoveryCode
from ..types.secret import Secret
from ..types.totp_config import TotpConfig
from .raw_client import AsyncRawAdminsClient, RawAdminsClient
from .types.generate_admin_totp_secret_response import GenerateAdminTotpSecretResponse
from .types.get_admins_request_order import GetAdminsRequestOrder


OMIT = typing.cast(typing.Any, ...)


class AdminsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAdminsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAdminsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAdminsClient
        """
        return self._raw_client

    def change_admin_password(
        self,
        *,
        current_password: typing.Optional[str] = OMIT,
        new_password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Changes the password for the logged in admin

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
        client.admins.change_admin_password()
        """
        _response = self._raw_client.change_admin_password(
            current_password=current_password, new_password=new_password, request_options=request_options
        )
        return _response.data

    def get_admin_profile(self, *, request_options: typing.Optional[RequestOptions] = None) -> AdminProfile:
        """
        Returns the profile for the logged in admin

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdminProfile
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.admins.get_admin_profile()
        """
        _response = self._raw_client.get_admin_profile(request_options=request_options)
        return _response.data

    def update_admin_profile(
        self,
        *,
        email: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        allow_api_key_auth: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Allows to update the profile for the logged in admin

        Parameters
        ----------
        email : typing.Optional[str]

        description : typing.Optional[str]

        allow_api_key_auth : typing.Optional[bool]
            If enabled, you can impersonate this admin, in REST API, using an API key. If disabled admin credentials are required for impersonation

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
        client.admins.update_admin_profile()
        """
        _response = self._raw_client.update_admin_profile(
            email=email, description=description, allow_api_key_auth=allow_api_key_auth, request_options=request_options
        )
        return _response.data

    def get_admin_recovery_codes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RecoveryCode]:
        """
        Returns the recovery codes for the logged in admin. Recovery codes can be used if the admin loses access to their second factor auth device. Recovery codes are returned unencrypted

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
        client.admins.get_admin_recovery_codes()
        """
        _response = self._raw_client.get_admin_recovery_codes(request_options=request_options)
        return _response.data

    def generate_admin_recovery_codes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Generates new recovery codes for the logged in admin. Generating new recovery codes you automatically invalidate old ones

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
        client.admins.generate_admin_recovery_codes()
        """
        _response = self._raw_client.generate_admin_recovery_codes(request_options=request_options)
        return _response.data

    def get_admin_totp_configs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TotpConfig]:
        """
        Returns the available TOTP configurations for the logged in admin

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
        client.admins.get_admin_totp_configs()
        """
        _response = self._raw_client.get_admin_totp_configs(request_options=request_options)
        return _response.data

    def generate_admin_totp_secret(
        self, *, config_name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> GenerateAdminTotpSecretResponse:
        """
        Generates a new TOTP secret, including the QR code as png, using the specified configuration for the logged in admin

        Parameters
        ----------
        config_name : typing.Optional[str]
            name of the configuration to use to generate the secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerateAdminTotpSecretResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.admins.generate_admin_totp_secret()
        """
        _response = self._raw_client.generate_admin_totp_secret(
            config_name=config_name, request_options=request_options
        )
        return _response.data

    def validate_admin_totp_secret(
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
        client.admins.validate_admin_totp_secret()
        """
        _response = self._raw_client.validate_admin_totp_secret(
            config_name=config_name, passcode=passcode, secret=secret, request_options=request_options
        )
        return _response.data

    def save_admin_totp_config(
        self,
        *,
        enabled: typing.Optional[bool] = OMIT,
        config_name: typing.Optional[str] = OMIT,
        secret: typing.Optional[Secret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Saves the specified TOTP config for the logged in admin

        Parameters
        ----------
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
        client.admins.save_admin_totp_config()
        """
        _response = self._raw_client.save_admin_totp_config(
            enabled=enabled, config_name=config_name, secret=secret, request_options=request_options
        )
        return _response.data

    def get_admins(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetAdminsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Admin]:
        """
        Returns an array with one or more admins. For security reasons hashed passwords are omitted in the response

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetAdminsRequestOrder]
            Ordering admins by username. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Admin]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.admins.get_admins()
        """
        _response = self._raw_client.get_admins(
            offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    def add_admin(
        self,
        *,
        id: typing.Optional[int] = OMIT,
        status: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        permissions: typing.Optional[typing.Sequence[AdminPermissions]] = OMIT,
        filters: typing.Optional[AdminFilters] = OMIT,
        additional_info: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[AdminGroupMapping]] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_login: typing.Optional[int] = OMIT,
        role: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Admin:
        """
        Adds a new admin. Recovery codes and TOTP configuration cannot be set using this API: each admin must use the specific APIs

        Parameters
        ----------
        id : typing.Optional[int]

        status : typing.Optional[int]
            status:
              * `0` user is disabled, login is not allowed
              * `1` user is enabled

        username : typing.Optional[str]
            username is unique

        description : typing.Optional[str]
            optional description, for example the admin full name

        password : typing.Optional[str]
            Admin password. For security reasons this field is omitted when you search/get admins

        email : typing.Optional[str]

        permissions : typing.Optional[typing.Sequence[AdminPermissions]]

        filters : typing.Optional[AdminFilters]

        additional_info : typing.Optional[str]
            Free form text field

        groups : typing.Optional[typing.Sequence[AdminGroupMapping]]
            Groups automatically selected for new users created by this admin. The admin will still be able to choose different groups. These settings are only used for this admin UI and they will be ignored in REST API/hooks.

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds. It will be 0 for admins created before v2.2.0

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_login : typing.Optional[int]
            Last user login as unix timestamp in milliseconds. It is saved at most once every 10 minutes

        role : typing.Optional[str]
            If set the admin can only administer users with the same role. Role admins cannot have the "*" permission

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Admin
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.admins.add_admin()
        """
        _response = self._raw_client.add_admin(
            id=id,
            status=status,
            username=username,
            description=description,
            password=password,
            email=email,
            permissions=permissions,
            filters=filters,
            additional_info=additional_info,
            groups=groups,
            created_at=created_at,
            updated_at=updated_at,
            last_login=last_login,
            role=role,
            request_options=request_options,
        )
        return _response.data

    def get_admin_by_username(self, username: str, *, request_options: typing.Optional[RequestOptions] = None) -> Admin:
        """
        Returns the admin with the given username, if it exists. For security reasons the hashed password is omitted in the response

        Parameters
        ----------
        username : str
            the admin username

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Admin
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.admins.get_admin_by_username(
            username="username",
        )
        """
        _response = self._raw_client.get_admin_by_username(username, request_options=request_options)
        return _response.data

    def update_admin(
        self,
        username_: str,
        *,
        id: typing.Optional[int] = OMIT,
        status: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        permissions: typing.Optional[typing.Sequence[AdminPermissions]] = OMIT,
        filters: typing.Optional[AdminFilters] = OMIT,
        additional_info: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[AdminGroupMapping]] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_login: typing.Optional[int] = OMIT,
        role: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing admin. Recovery codes and TOTP configuration cannot be set/updated using this API: each admin must use the specific APIs. You are not allowed to update the admin impersonated using an API key

        Parameters
        ----------
        username_ : str
            the admin username

        id : typing.Optional[int]

        status : typing.Optional[int]
            status:
              * `0` user is disabled, login is not allowed
              * `1` user is enabled

        username : typing.Optional[str]
            username is unique

        description : typing.Optional[str]
            optional description, for example the admin full name

        password : typing.Optional[str]
            Admin password. For security reasons this field is omitted when you search/get admins

        email : typing.Optional[str]

        permissions : typing.Optional[typing.Sequence[AdminPermissions]]

        filters : typing.Optional[AdminFilters]

        additional_info : typing.Optional[str]
            Free form text field

        groups : typing.Optional[typing.Sequence[AdminGroupMapping]]
            Groups automatically selected for new users created by this admin. The admin will still be able to choose different groups. These settings are only used for this admin UI and they will be ignored in REST API/hooks.

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds. It will be 0 for admins created before v2.2.0

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_login : typing.Optional[int]
            Last user login as unix timestamp in milliseconds. It is saved at most once every 10 minutes

        role : typing.Optional[str]
            If set the admin can only administer users with the same role. Role admins cannot have the "*" permission

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
        client.admins.update_admin(
            username_="username",
        )
        """
        _response = self._raw_client.update_admin(
            username_,
            id=id,
            status=status,
            username=username,
            description=description,
            password=password,
            email=email,
            permissions=permissions,
            filters=filters,
            additional_info=additional_info,
            groups=groups,
            created_at=created_at,
            updated_at=updated_at,
            last_login=last_login,
            role=role,
            request_options=request_options,
        )
        return _response.data

    def delete_admin(self, username: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Deletes an existing admin

        Parameters
        ----------
        username : str
            the admin username

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
        client.admins.delete_admin(
            username="username",
        )
        """
        _response = self._raw_client.delete_admin(username, request_options=request_options)
        return _response.data

    def disable_admin2fa(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Disables second factor authentication for the given admin. This API must be used if the admin loses access to their second factor auth device and has no recovery codes

        Parameters
        ----------
        username : str
            the admin username

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
        client.admins.disable_admin2fa(
            username="username",
        )
        """
        _response = self._raw_client.disable_admin2fa(username, request_options=request_options)
        return _response.data

    def admin_forgot_password(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        You must set up an SMTP server. SFTPGo will send a code via email to reset the password if the specified admin exists and has a valid email address. Requests that do not meet these conditions are silently ignored (a success response will be returned) to avoid disclosing existing admins

        Parameters
        ----------
        username : str
            the admin username

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
        client.admins.admin_forgot_password(
            username="username",
        )
        """
        _response = self._raw_client.admin_forgot_password(username, request_options=request_options)
        return _response.data

    def admin_reset_password(
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
            the admin username

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
        client.admins.admin_reset_password(
            username="username",
        )
        """
        _response = self._raw_client.admin_reset_password(
            username, code=code, password=password, request_options=request_options
        )
        return _response.data


class AsyncAdminsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAdminsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAdminsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAdminsClient
        """
        return self._raw_client

    async def change_admin_password(
        self,
        *,
        current_password: typing.Optional[str] = OMIT,
        new_password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Changes the password for the logged in admin

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
            await client.admins.change_admin_password()


        asyncio.run(main())
        """
        _response = await self._raw_client.change_admin_password(
            current_password=current_password, new_password=new_password, request_options=request_options
        )
        return _response.data

    async def get_admin_profile(self, *, request_options: typing.Optional[RequestOptions] = None) -> AdminProfile:
        """
        Returns the profile for the logged in admin

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdminProfile
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
            await client.admins.get_admin_profile()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_admin_profile(request_options=request_options)
        return _response.data

    async def update_admin_profile(
        self,
        *,
        email: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        allow_api_key_auth: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Allows to update the profile for the logged in admin

        Parameters
        ----------
        email : typing.Optional[str]

        description : typing.Optional[str]

        allow_api_key_auth : typing.Optional[bool]
            If enabled, you can impersonate this admin, in REST API, using an API key. If disabled admin credentials are required for impersonation

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
            await client.admins.update_admin_profile()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_admin_profile(
            email=email, description=description, allow_api_key_auth=allow_api_key_auth, request_options=request_options
        )
        return _response.data

    async def get_admin_recovery_codes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RecoveryCode]:
        """
        Returns the recovery codes for the logged in admin. Recovery codes can be used if the admin loses access to their second factor auth device. Recovery codes are returned unencrypted

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
            await client.admins.get_admin_recovery_codes()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_admin_recovery_codes(request_options=request_options)
        return _response.data

    async def generate_admin_recovery_codes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Generates new recovery codes for the logged in admin. Generating new recovery codes you automatically invalidate old ones

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
            await client.admins.generate_admin_recovery_codes()


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_admin_recovery_codes(request_options=request_options)
        return _response.data

    async def get_admin_totp_configs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TotpConfig]:
        """
        Returns the available TOTP configurations for the logged in admin

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
            await client.admins.get_admin_totp_configs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_admin_totp_configs(request_options=request_options)
        return _response.data

    async def generate_admin_totp_secret(
        self, *, config_name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> GenerateAdminTotpSecretResponse:
        """
        Generates a new TOTP secret, including the QR code as png, using the specified configuration for the logged in admin

        Parameters
        ----------
        config_name : typing.Optional[str]
            name of the configuration to use to generate the secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerateAdminTotpSecretResponse
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
            await client.admins.generate_admin_totp_secret()


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_admin_totp_secret(
            config_name=config_name, request_options=request_options
        )
        return _response.data

    async def validate_admin_totp_secret(
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
            await client.admins.validate_admin_totp_secret()


        asyncio.run(main())
        """
        _response = await self._raw_client.validate_admin_totp_secret(
            config_name=config_name, passcode=passcode, secret=secret, request_options=request_options
        )
        return _response.data

    async def save_admin_totp_config(
        self,
        *,
        enabled: typing.Optional[bool] = OMIT,
        config_name: typing.Optional[str] = OMIT,
        secret: typing.Optional[Secret] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Saves the specified TOTP config for the logged in admin

        Parameters
        ----------
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
            await client.admins.save_admin_totp_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.save_admin_totp_config(
            enabled=enabled, config_name=config_name, secret=secret, request_options=request_options
        )
        return _response.data

    async def get_admins(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetAdminsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Admin]:
        """
        Returns an array with one or more admins. For security reasons hashed passwords are omitted in the response

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetAdminsRequestOrder]
            Ordering admins by username. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Admin]
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
            await client.admins.get_admins()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_admins(
            offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    async def add_admin(
        self,
        *,
        id: typing.Optional[int] = OMIT,
        status: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        permissions: typing.Optional[typing.Sequence[AdminPermissions]] = OMIT,
        filters: typing.Optional[AdminFilters] = OMIT,
        additional_info: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[AdminGroupMapping]] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_login: typing.Optional[int] = OMIT,
        role: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Admin:
        """
        Adds a new admin. Recovery codes and TOTP configuration cannot be set using this API: each admin must use the specific APIs

        Parameters
        ----------
        id : typing.Optional[int]

        status : typing.Optional[int]
            status:
              * `0` user is disabled, login is not allowed
              * `1` user is enabled

        username : typing.Optional[str]
            username is unique

        description : typing.Optional[str]
            optional description, for example the admin full name

        password : typing.Optional[str]
            Admin password. For security reasons this field is omitted when you search/get admins

        email : typing.Optional[str]

        permissions : typing.Optional[typing.Sequence[AdminPermissions]]

        filters : typing.Optional[AdminFilters]

        additional_info : typing.Optional[str]
            Free form text field

        groups : typing.Optional[typing.Sequence[AdminGroupMapping]]
            Groups automatically selected for new users created by this admin. The admin will still be able to choose different groups. These settings are only used for this admin UI and they will be ignored in REST API/hooks.

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds. It will be 0 for admins created before v2.2.0

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_login : typing.Optional[int]
            Last user login as unix timestamp in milliseconds. It is saved at most once every 10 minutes

        role : typing.Optional[str]
            If set the admin can only administer users with the same role. Role admins cannot have the "*" permission

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Admin
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
            await client.admins.add_admin()


        asyncio.run(main())
        """
        _response = await self._raw_client.add_admin(
            id=id,
            status=status,
            username=username,
            description=description,
            password=password,
            email=email,
            permissions=permissions,
            filters=filters,
            additional_info=additional_info,
            groups=groups,
            created_at=created_at,
            updated_at=updated_at,
            last_login=last_login,
            role=role,
            request_options=request_options,
        )
        return _response.data

    async def get_admin_by_username(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Admin:
        """
        Returns the admin with the given username, if it exists. For security reasons the hashed password is omitted in the response

        Parameters
        ----------
        username : str
            the admin username

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Admin
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
            await client.admins.get_admin_by_username(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_admin_by_username(username, request_options=request_options)
        return _response.data

    async def update_admin(
        self,
        username_: str,
        *,
        id: typing.Optional[int] = OMIT,
        status: typing.Optional[int] = OMIT,
        username: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        permissions: typing.Optional[typing.Sequence[AdminPermissions]] = OMIT,
        filters: typing.Optional[AdminFilters] = OMIT,
        additional_info: typing.Optional[str] = OMIT,
        groups: typing.Optional[typing.Sequence[AdminGroupMapping]] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        last_login: typing.Optional[int] = OMIT,
        role: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing admin. Recovery codes and TOTP configuration cannot be set/updated using this API: each admin must use the specific APIs. You are not allowed to update the admin impersonated using an API key

        Parameters
        ----------
        username_ : str
            the admin username

        id : typing.Optional[int]

        status : typing.Optional[int]
            status:
              * `0` user is disabled, login is not allowed
              * `1` user is enabled

        username : typing.Optional[str]
            username is unique

        description : typing.Optional[str]
            optional description, for example the admin full name

        password : typing.Optional[str]
            Admin password. For security reasons this field is omitted when you search/get admins

        email : typing.Optional[str]

        permissions : typing.Optional[typing.Sequence[AdminPermissions]]

        filters : typing.Optional[AdminFilters]

        additional_info : typing.Optional[str]
            Free form text field

        groups : typing.Optional[typing.Sequence[AdminGroupMapping]]
            Groups automatically selected for new users created by this admin. The admin will still be able to choose different groups. These settings are only used for this admin UI and they will be ignored in REST API/hooks.

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds. It will be 0 for admins created before v2.2.0

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        last_login : typing.Optional[int]
            Last user login as unix timestamp in milliseconds. It is saved at most once every 10 minutes

        role : typing.Optional[str]
            If set the admin can only administer users with the same role. Role admins cannot have the "*" permission

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
            await client.admins.update_admin(
                username_="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_admin(
            username_,
            id=id,
            status=status,
            username=username,
            description=description,
            password=password,
            email=email,
            permissions=permissions,
            filters=filters,
            additional_info=additional_info,
            groups=groups,
            created_at=created_at,
            updated_at=updated_at,
            last_login=last_login,
            role=role,
            request_options=request_options,
        )
        return _response.data

    async def delete_admin(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Deletes an existing admin

        Parameters
        ----------
        username : str
            the admin username

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
            await client.admins.delete_admin(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_admin(username, request_options=request_options)
        return _response.data

    async def disable_admin2fa(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Disables second factor authentication for the given admin. This API must be used if the admin loses access to their second factor auth device and has no recovery codes

        Parameters
        ----------
        username : str
            the admin username

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
            await client.admins.disable_admin2fa(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disable_admin2fa(username, request_options=request_options)
        return _response.data

    async def admin_forgot_password(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        You must set up an SMTP server. SFTPGo will send a code via email to reset the password if the specified admin exists and has a valid email address. Requests that do not meet these conditions are silently ignored (a success response will be returned) to avoid disclosing existing admins

        Parameters
        ----------
        username : str
            the admin username

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
            await client.admins.admin_forgot_password(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.admin_forgot_password(username, request_options=request_options)
        return _response.data

    async def admin_reset_password(
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
            the admin username

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
            await client.admins.admin_reset_password(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.admin_reset_password(
            username, code=code, password=password, request_options=request_options
        )
        return _response.data
