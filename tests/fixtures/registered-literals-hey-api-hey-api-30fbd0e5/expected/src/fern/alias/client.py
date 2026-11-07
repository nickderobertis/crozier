

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user import User
from ..types.val import Val
from .raw_client import AsyncRawAliasClient, RawAliasClient


class AliasClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAliasClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAliasClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAliasClient
        """
        return self._raw_client

    def username(self, username: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Get basic details about a user, given their username

        Parameters
        ----------
        username : str
            Username of the user who you are looking for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.alias.username(
            username="username",
        )
        """
        _response = self._raw_client.username(username, request_options=request_options)
        return _response.data

    def alias_val2(
        self, username: str, val_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Val:
        """
        Get a val

        Parameters
        ----------
        username : str
            Username of the user whose val you are looking for

        val_name : str
            Name of the val you're looking for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Val
            A Val

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.alias.alias_val2(
            username="username",
            val_name="val_name",
        )
        """
        _response = self._raw_client.alias_val2(username, val_name, request_options=request_options)
        return _response.data


class AsyncAliasClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAliasClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAliasClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAliasClient
        """
        return self._raw_client

    async def username(self, username: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Get basic details about a user, given their username

        Parameters
        ----------
        username : str
            Username of the user who you are looking for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.alias.username(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.username(username, request_options=request_options)
        return _response.data

    async def alias_val2(
        self, username: str, val_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Val:
        """
        Get a val

        Parameters
        ----------
        username : str
            Username of the user whose val you are looking for

        val_name : str
            Name of the val you're looking for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Val
            A Val

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.alias.alias_val2(
                username="username",
                val_name="val_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.alias_val2(username, val_name, request_options=request_options)
        return _response.data
