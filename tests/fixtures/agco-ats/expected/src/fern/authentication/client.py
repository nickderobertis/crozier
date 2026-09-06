

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_models_authenticated_user import ApiModelsAuthenticatedUser
from .raw_client import AsyncRawAuthenticationClient, RawAuthenticationClient
from .types.api_models_credentials_bearer_action import ApiModelsCredentialsBearerAction
from .types.api_models_credentials_mac_action import ApiModelsCredentialsMacAction
from .types.api_models_token_options_bearer_action import ApiModelsTokenOptionsBearerAction
from .types.api_models_token_options_mac_action import ApiModelsTokenOptionsMacAction


OMIT = typing.cast(typing.Any, ...)


class AuthenticationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthenticationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthenticationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthenticationClient
        """
        return self._raw_client

    def putmanagetokens(
        self,
        user_id: int,
        *,
        bearer_action: typing.Optional[ApiModelsTokenOptionsBearerAction] = OMIT,
        mac_action: typing.Optional[ApiModelsTokenOptionsMacAction] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        user_id : int

        bearer_action : typing.Optional[ApiModelsTokenOptionsBearerAction]
            The action to perform on the bearer token. Optional. Defaults to ‘None’.

        mac_action : typing.Optional[ApiModelsTokenOptionsMacAction]
            The action to perform on the MAC token. Optional. Defaults to ‘None’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authentication.putmanagetokens(
            user_id=1,
        )
        """
        _response = self._raw_client.putmanagetokens(
            user_id, bearer_action=bearer_action, mac_action=mac_action, request_options=request_options
        )
        return _response.data

    def default(
        self,
        *,
        password: str,
        username: str,
        bearer_action: typing.Optional[ApiModelsCredentialsBearerAction] = OMIT,
        mac_action: typing.Optional[ApiModelsCredentialsMacAction] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiModelsAuthenticatedUser:
        """
        No Documentation Found.

        Parameters
        ----------
        password : str
            A secret word or phrase that must be used to gain admission

        username : str
            A unique ID a user needs to login with

        bearer_action : typing.Optional[ApiModelsCredentialsBearerAction]
            The action to perform on the bearer token. Optional. Defaults to ‘None’.

        mac_action : typing.Optional[ApiModelsCredentialsMacAction]
            The action to perform on the MAC token. Optional. Defaults to ‘None’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiModelsAuthenticatedUser
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authentication.default(
            password="password",
            username="username",
        )
        """
        _response = self._raw_client.default(
            password=password,
            username=username,
            bearer_action=bearer_action,
            mac_action=mac_action,
            request_options=request_options,
        )
        return _response.data

    def isalive(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

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

        client = FernApi()
        client.authentication.isalive()
        """
        _response = self._raw_client.isalive(request_options=request_options)
        return _response.data

    def requestpasswordreset(
        self, *, parameter_name: str, url: str, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        parameter_name : str
            The query string parameter name to use for supplying the password reset token

        url : str
            The URL to direct the user to reset the password.

        username : str
            The username to reset the password for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authentication.requestpasswordreset(
            parameter_name="ParameterName",
            url="Url",
            username="Username",
        )
        """
        _response = self._raw_client.requestpasswordreset(
            parameter_name=parameter_name, url=url, username=username, request_options=request_options
        )
        return _response.data

    def resetpasword(
        self, *, new_password: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        new_password : str
            The new password

        token : str
            The password reset token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authentication.resetpasword(
            new_password="NewPassword",
            token="Token",
        )
        """
        _response = self._raw_client.resetpasword(
            new_password=new_password, token=token, request_options=request_options
        )
        return _response.data


class AsyncAuthenticationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthenticationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthenticationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthenticationClient
        """
        return self._raw_client

    async def putmanagetokens(
        self,
        user_id: int,
        *,
        bearer_action: typing.Optional[ApiModelsTokenOptionsBearerAction] = OMIT,
        mac_action: typing.Optional[ApiModelsTokenOptionsMacAction] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        user_id : int

        bearer_action : typing.Optional[ApiModelsTokenOptionsBearerAction]
            The action to perform on the bearer token. Optional. Defaults to ‘None’.

        mac_action : typing.Optional[ApiModelsTokenOptionsMacAction]
            The action to perform on the MAC token. Optional. Defaults to ‘None’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.authentication.putmanagetokens(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putmanagetokens(
            user_id, bearer_action=bearer_action, mac_action=mac_action, request_options=request_options
        )
        return _response.data

    async def default(
        self,
        *,
        password: str,
        username: str,
        bearer_action: typing.Optional[ApiModelsCredentialsBearerAction] = OMIT,
        mac_action: typing.Optional[ApiModelsCredentialsMacAction] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiModelsAuthenticatedUser:
        """
        No Documentation Found.

        Parameters
        ----------
        password : str
            A secret word or phrase that must be used to gain admission

        username : str
            A unique ID a user needs to login with

        bearer_action : typing.Optional[ApiModelsCredentialsBearerAction]
            The action to perform on the bearer token. Optional. Defaults to ‘None’.

        mac_action : typing.Optional[ApiModelsCredentialsMacAction]
            The action to perform on the MAC token. Optional. Defaults to ‘None’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiModelsAuthenticatedUser
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.authentication.default(
                password="password",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.default(
            password=password,
            username=username,
            bearer_action=bearer_action,
            mac_action=mac_action,
            request_options=request_options,
        )
        return _response.data

    async def isalive(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

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

        client = AsyncFernApi()


        async def main() -> None:
            await client.authentication.isalive()


        asyncio.run(main())
        """
        _response = await self._raw_client.isalive(request_options=request_options)
        return _response.data

    async def requestpasswordreset(
        self, *, parameter_name: str, url: str, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        parameter_name : str
            The query string parameter name to use for supplying the password reset token

        url : str
            The URL to direct the user to reset the password.

        username : str
            The username to reset the password for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.authentication.requestpasswordreset(
                parameter_name="ParameterName",
                url="Url",
                username="Username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.requestpasswordreset(
            parameter_name=parameter_name, url=url, username=username, request_options=request_options
        )
        return _response.data

    async def resetpasword(
        self, *, new_password: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        new_password : str
            The new password

        token : str
            The password reset token

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.authentication.resetpasword(
                new_password="NewPassword",
                token="Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resetpasword(
            new_password=new_password, token=token, request_options=request_options
        )
        return _response.data
