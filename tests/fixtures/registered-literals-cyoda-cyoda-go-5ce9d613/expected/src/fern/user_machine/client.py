

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.delete_technical_user200response_dto import DeleteTechnicalUser200ResponseDto
from ..types.technical_user_credentials_dto import TechnicalUserCredentialsDto
from ..types.technical_user_dto import TechnicalUserDto
from ..types.token_response_dto import TokenResponseDto
from .raw_client import AsyncRawUserMachineClient, RawUserMachineClient
from .types.get_technical_user_token_request_grant_type import GetTechnicalUserTokenRequestGrantType
from .types.get_technical_user_token_request_subject_token_type import GetTechnicalUserTokenRequestSubjectTokenType


OMIT = typing.cast(typing.Any, ...)


class UserMachineClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserMachineClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserMachineClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserMachineClient
        """
        return self._raw_client

    def list_technical_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TechnicalUserDto]:
        """
        Retrieves a list of all active machine-to-machine (M2M) clients (OAuth 2.0 clients) to the current legal entity.
        These users authenticate via client credentials and act on behalf of applications, not humans.

        Returns the client IDs of all M2M clients that are currently active
        and available for authentication.

        **Authorization Required:** SUPER_USER role

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TechnicalUserDto]
            List of M2M clients returned successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user_machine.list_technical_users()
        """
        _response = self._raw_client.list_technical_users(request_options=request_options)
        return _response.data

    def create_technical_user(
        self, *, with_admin_role: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> TechnicalUserCredentialsDto:
        """
        Creates a new machine-to-machine (M2M) client for API authentication via OAuth 2.0.

        The created user will have M2M role permissions, necessary for getting the bearer token.

        When `withAdminRole` is set to `true`, the M2M client will additionally receive the ADMIN role,
        granting it full access to all ADMIN-level endpoints (e.g., trusted key registration).
        This requires the `cyoda.security.web.jwt.m2m.admin-role-enabled` feature flag to be enabled;
        otherwise, a 401 Unauthorized response is returned.

        **Authorization Required:** SUPER_USER role

        Parameters
        ----------
        with_admin_role : typing.Optional[str]
            When true, the created M2M client will additionally receive the ADMIN role. Requires the M2M admin role feature flag to be enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TechnicalUserCredentialsDto
            M2M client created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user_machine.create_technical_user()
        """
        _response = self._raw_client.create_technical_user(
            with_admin_role=with_admin_role, request_options=request_options
        )
        return _response.data

    def delete_technical_user(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteTechnicalUser200ResponseDto:
        """
        Deletes a M2M client and invalidates all associated credentials.

        This operation cannot be undone without a support ticket. Any applications using this client's
        credentials will immediately lose access and must be reconfigured with new credentials.

        **Authorization Required:** SUPER_USER role

        Parameters
        ----------
        client_id : str
            The client ID of the M2M client to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTechnicalUser200ResponseDto
            M2M client deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user_machine.delete_technical_user(
            client_id="clientId",
        )
        """
        _response = self._raw_client.delete_technical_user(client_id, request_options=request_options)
        return _response.data

    def reset_technical_user_secret(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TechnicalUserCredentialsDto:
        """
        Generates a new client secret for an existing M2M client.

        This operation invalidates the current client secret and generates a new one.
        Any applications using the old secret will need to be updated with the new credentials.

        **Authorization Required:** SUPER_USER role

        Parameters
        ----------
        client_id : str
            The client ID of the M2M client whose secret should be reset

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TechnicalUserCredentialsDto
            Client secret reset successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user_machine.reset_technical_user_secret(
            client_id="clientId",
        )
        """
        _response = self._raw_client.reset_technical_user_secret(client_id, request_options=request_options)
        return _response.data

    def get_technical_user_token(
        self,
        *,
        grant_type: typing.Optional[GetTechnicalUserTokenRequestGrantType] = OMIT,
        subject_token: typing.Optional[str] = OMIT,
        subject_token_type: typing.Optional[GetTechnicalUserTokenRequestSubjectTokenType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokenResponseDto:
        """
        Authenticates a M2M client and returns an access token.

        Supports two grant types:

        1. **client_credentials** — Standard OAuth 2.0 Client Credentials Grant for M2M authentication.
        2. **urn:ietf:params:oauth:grant-type:token-exchange** — RFC 8693 Token Exchange.
           The M2M client acts on behalf of a user by presenting the user's JWT as `subject_token`.

        In both cases the M2M client authenticates via HTTP Basic Authentication
        (client_id and client_secret in the Authorization header).

        **Note:** This endpoint does not require an existing access token, as it serves as the authentication entry point.

        Parameters
        ----------
        grant_type : typing.Optional[GetTechnicalUserTokenRequestGrantType]
            The OAuth 2.0 grant type

        subject_token : typing.Optional[str]
            The subject token to exchange

        subject_token_type : typing.Optional[GetTechnicalUserTokenRequestSubjectTokenType]
            The type of the subject token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponseDto
            Access token issued successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user_machine.get_technical_user_token()
        """
        _response = self._raw_client.get_technical_user_token(
            grant_type=grant_type,
            subject_token=subject_token,
            subject_token_type=subject_token_type,
            request_options=request_options,
        )
        return _response.data


class AsyncUserMachineClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserMachineClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserMachineClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserMachineClient
        """
        return self._raw_client

    async def list_technical_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TechnicalUserDto]:
        """
        Retrieves a list of all active machine-to-machine (M2M) clients (OAuth 2.0 clients) to the current legal entity.
        These users authenticate via client credentials and act on behalf of applications, not humans.

        Returns the client IDs of all M2M clients that are currently active
        and available for authentication.

        **Authorization Required:** SUPER_USER role

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TechnicalUserDto]
            List of M2M clients returned successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user_machine.list_technical_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_technical_users(request_options=request_options)
        return _response.data

    async def create_technical_user(
        self, *, with_admin_role: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> TechnicalUserCredentialsDto:
        """
        Creates a new machine-to-machine (M2M) client for API authentication via OAuth 2.0.

        The created user will have M2M role permissions, necessary for getting the bearer token.

        When `withAdminRole` is set to `true`, the M2M client will additionally receive the ADMIN role,
        granting it full access to all ADMIN-level endpoints (e.g., trusted key registration).
        This requires the `cyoda.security.web.jwt.m2m.admin-role-enabled` feature flag to be enabled;
        otherwise, a 401 Unauthorized response is returned.

        **Authorization Required:** SUPER_USER role

        Parameters
        ----------
        with_admin_role : typing.Optional[str]
            When true, the created M2M client will additionally receive the ADMIN role. Requires the M2M admin role feature flag to be enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TechnicalUserCredentialsDto
            M2M client created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user_machine.create_technical_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_technical_user(
            with_admin_role=with_admin_role, request_options=request_options
        )
        return _response.data

    async def delete_technical_user(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteTechnicalUser200ResponseDto:
        """
        Deletes a M2M client and invalidates all associated credentials.

        This operation cannot be undone without a support ticket. Any applications using this client's
        credentials will immediately lose access and must be reconfigured with new credentials.

        **Authorization Required:** SUPER_USER role

        Parameters
        ----------
        client_id : str
            The client ID of the M2M client to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTechnicalUser200ResponseDto
            M2M client deleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user_machine.delete_technical_user(
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_technical_user(client_id, request_options=request_options)
        return _response.data

    async def reset_technical_user_secret(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TechnicalUserCredentialsDto:
        """
        Generates a new client secret for an existing M2M client.

        This operation invalidates the current client secret and generates a new one.
        Any applications using the old secret will need to be updated with the new credentials.

        **Authorization Required:** SUPER_USER role

        Parameters
        ----------
        client_id : str
            The client ID of the M2M client whose secret should be reset

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TechnicalUserCredentialsDto
            Client secret reset successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user_machine.reset_technical_user_secret(
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reset_technical_user_secret(client_id, request_options=request_options)
        return _response.data

    async def get_technical_user_token(
        self,
        *,
        grant_type: typing.Optional[GetTechnicalUserTokenRequestGrantType] = OMIT,
        subject_token: typing.Optional[str] = OMIT,
        subject_token_type: typing.Optional[GetTechnicalUserTokenRequestSubjectTokenType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokenResponseDto:
        """
        Authenticates a M2M client and returns an access token.

        Supports two grant types:

        1. **client_credentials** — Standard OAuth 2.0 Client Credentials Grant for M2M authentication.
        2. **urn:ietf:params:oauth:grant-type:token-exchange** — RFC 8693 Token Exchange.
           The M2M client acts on behalf of a user by presenting the user's JWT as `subject_token`.

        In both cases the M2M client authenticates via HTTP Basic Authentication
        (client_id and client_secret in the Authorization header).

        **Note:** This endpoint does not require an existing access token, as it serves as the authentication entry point.

        Parameters
        ----------
        grant_type : typing.Optional[GetTechnicalUserTokenRequestGrantType]
            The OAuth 2.0 grant type

        subject_token : typing.Optional[str]
            The subject token to exchange

        subject_token_type : typing.Optional[GetTechnicalUserTokenRequestSubjectTokenType]
            The type of the subject token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponseDto
            Access token issued successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user_machine.get_technical_user_token()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_technical_user_token(
            grant_type=grant_type,
            subject_token=subject_token,
            subject_token_type=subject_token_type,
            request_options=request_options,
        )
        return _response.data
