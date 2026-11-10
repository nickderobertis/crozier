

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.accounts_response_dto import AccountsResponseDto
from ..types.accounts_session_response_dto import AccountsSessionResponseDto
from ..types.aggregated_dto_item import AggregatedDtoItem
from ..types.balance_response_dto import BalanceResponseDto
from .raw_client import AsyncRawAccountsClient, RawAccountsClient


OMIT = typing.cast(typing.Any, ...)


class AccountsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountsClient
        """
        return self._raw_client

    def account_api_get_session(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountsSessionResponseDto:
        """
        Returns current user session.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountsSessionResponseDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounts.account_api_get_session()
        """
        _response = self._raw_client.account_api_get_session(request_options=request_options)
        return _response.data

    def account_api_register(
        self,
        *,
        username: str,
        password: str,
        password_confirmation: str,
        role: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountsResponseDto:
        """
        Object that contain username, password and role (optional) fields.

        Parameters
        ----------
        username : str

        password : str

        password_confirmation : str

        role : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountsResponseDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounts.account_api_register(
            username="username",
            password="password",
            password_confirmation="password_confirmation",
            role="role",
        )
        """
        _response = self._raw_client.account_api_register(
            username=username,
            password=password,
            password_confirmation=password_confirmation,
            role=role,
            request_options=request_options,
        )
        return _response.data

    def account_api_login(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountsSessionResponseDto:
        """
        Parameters
        ----------
        username : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountsSessionResponseDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounts.account_api_login(
            username="username",
            password="password",
        )
        """
        _response = self._raw_client.account_api_login(
            username=username, password=password, request_options=request_options
        )
        return _response.data

    def account_api_get_access_token(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns access token.

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
            token="YOUR_TOKEN",
        )
        client.accounts.account_api_get_access_token()
        """
        _response = self._raw_client.account_api_get_access_token(request_options=request_options)
        return _response.data

    def account_api_get_all_accounts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountsResponseDto:
        """
        Returns all users except those with roles Standard Registry and Auditor. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountsResponseDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounts.account_api_get_all_accounts()
        """
        _response = self._raw_client.account_api_get_all_accounts(request_options=request_options)
        return _response.data

    def account_api_get_standatd_registries(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountsResponseDto:
        """
        Returns all Standard Registries.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountsResponseDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounts.account_api_get_standatd_registries()
        """
        _response = self._raw_client.account_api_get_standatd_registries(request_options=request_options)
        return _response.data

    def account_api_get_aggregated_standard_registries(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AggregatedDtoItem]:
        """
        Returns all Standard Registries aggregated with polices and vcDocuments

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AggregatedDtoItem]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounts.account_api_get_aggregated_standard_registries()
        """
        _response = self._raw_client.account_api_get_aggregated_standard_registries(request_options=request_options)
        return _response.data

    def account_api_get_balance(self, *, request_options: typing.Optional[RequestOptions] = None) -> BalanceResponseDto:
        """
        Requests current Hedera account balance.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BalanceResponseDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounts.account_api_get_balance()
        """
        _response = self._raw_client.account_api_get_balance(request_options=request_options)
        return _response.data


class AsyncAccountsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountsClient
        """
        return self._raw_client

    async def account_api_get_session(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountsSessionResponseDto:
        """
        Returns current user session.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountsSessionResponseDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounts.account_api_get_session()


        asyncio.run(main())
        """
        _response = await self._raw_client.account_api_get_session(request_options=request_options)
        return _response.data

    async def account_api_register(
        self,
        *,
        username: str,
        password: str,
        password_confirmation: str,
        role: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountsResponseDto:
        """
        Object that contain username, password and role (optional) fields.

        Parameters
        ----------
        username : str

        password : str

        password_confirmation : str

        role : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountsResponseDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounts.account_api_register(
                username="username",
                password="password",
                password_confirmation="password_confirmation",
                role="role",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.account_api_register(
            username=username,
            password=password,
            password_confirmation=password_confirmation,
            role=role,
            request_options=request_options,
        )
        return _response.data

    async def account_api_login(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountsSessionResponseDto:
        """
        Parameters
        ----------
        username : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountsSessionResponseDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounts.account_api_login(
                username="username",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.account_api_login(
            username=username, password=password, request_options=request_options
        )
        return _response.data

    async def account_api_get_access_token(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns access token.

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounts.account_api_get_access_token()


        asyncio.run(main())
        """
        _response = await self._raw_client.account_api_get_access_token(request_options=request_options)
        return _response.data

    async def account_api_get_all_accounts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountsResponseDto:
        """
        Returns all users except those with roles Standard Registry and Auditor. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountsResponseDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounts.account_api_get_all_accounts()


        asyncio.run(main())
        """
        _response = await self._raw_client.account_api_get_all_accounts(request_options=request_options)
        return _response.data

    async def account_api_get_standatd_registries(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountsResponseDto:
        """
        Returns all Standard Registries.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountsResponseDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounts.account_api_get_standatd_registries()


        asyncio.run(main())
        """
        _response = await self._raw_client.account_api_get_standatd_registries(request_options=request_options)
        return _response.data

    async def account_api_get_aggregated_standard_registries(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AggregatedDtoItem]:
        """
        Returns all Standard Registries aggregated with polices and vcDocuments

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AggregatedDtoItem]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounts.account_api_get_aggregated_standard_registries()


        asyncio.run(main())
        """
        _response = await self._raw_client.account_api_get_aggregated_standard_registries(
            request_options=request_options
        )
        return _response.data

    async def account_api_get_balance(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BalanceResponseDto:
        """
        Requests current Hedera account balance.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BalanceResponseDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounts.account_api_get_balance()


        asyncio.run(main())
        """
        _response = await self._raw_client.account_api_get_balance(request_options=request_options)
        return _response.data
