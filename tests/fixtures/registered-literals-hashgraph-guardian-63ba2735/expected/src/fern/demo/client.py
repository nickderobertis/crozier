

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.hedera_account import HederaAccount
from ..types.registered_users_dto import RegisteredUsersDto
from ..types.task import Task
from .raw_client import AsyncRawDemoClient, RawDemoClient


class DemoClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDemoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDemoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDemoClient
        """
        return self._raw_client

    def demo_api_registered_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RegisteredUsersDto:
        """
        Returns list of registered users.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisteredUsersDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.demo.demo_api_registered_users()
        """
        _response = self._raw_client.demo_api_registered_users(request_options=request_options)
        return _response.data

    def get_demo_random_key(self, *, request_options: typing.Optional[RequestOptions] = None) -> HederaAccount:
        """
        Generates a new Hedera account with a random private key.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HederaAccount
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.demo.get_demo_random_key()
        """
        _response = self._raw_client.get_demo_random_key(request_options=request_options)
        return _response.data

    def generates_a_new_hedera_account_with_a_random_private_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Generates a new Hedera account with a random private key.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.demo.generates_a_new_hedera_account_with_a_random_private_key()
        """
        _response = self._raw_client.generates_a_new_hedera_account_with_a_random_private_key(
            request_options=request_options
        )
        return _response.data


class AsyncDemoClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDemoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDemoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDemoClient
        """
        return self._raw_client

    async def demo_api_registered_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RegisteredUsersDto:
        """
        Returns list of registered users.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisteredUsersDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.demo.demo_api_registered_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.demo_api_registered_users(request_options=request_options)
        return _response.data

    async def get_demo_random_key(self, *, request_options: typing.Optional[RequestOptions] = None) -> HederaAccount:
        """
        Generates a new Hedera account with a random private key.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HederaAccount
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.demo.get_demo_random_key()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_demo_random_key(request_options=request_options)
        return _response.data

    async def generates_a_new_hedera_account_with_a_random_private_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Generates a new Hedera account with a random private key.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.demo.generates_a_new_hedera_account_with_a_random_private_key()


        asyncio.run(main())
        """
        _response = await self._raw_client.generates_a_new_hedera_account_with_a_random_private_key(
            request_options=request_options
        )
        return _response.data
