

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.access_credential_type import AccessCredentialType
from ..types.account import Account
from ..types.credential_list import CredentialList
from ..types.user import User
from .raw_client import AsyncRawIdentityClient, RawIdentityClient


OMIT = typing.cast(typing.Any, ...)


class IdentityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIdentityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIdentityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIdentityClient
        """
        return self._raw_client

    def get_users_account(self, *, request_options: typing.Optional[RequestOptions] = None) -> Account:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Account
            User details for caller's user

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.identity.get_users_account()
        """
        _response = self._raw_client.get_users_account(request_options=request_options)
        return _response.data

    def get_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User details for caller's user

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.identity.get_user()
        """
        _response = self._raw_client.get_user(request_options=request_options)
        return _response.data

    def get_credentials(self, *, request_options: typing.Optional[RequestOptions] = None) -> CredentialList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CredentialList
            User credential listing

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.identity.get_credentials()
        """
        _response = self._raw_client.get_credentials(request_options=request_options)
        return _response.data

    def add_credential(
        self,
        *,
        type: AccessCredentialType,
        value: str,
        created_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Parameters
        ----------
        type : AccessCredentialType
            The type of credential

        value : str
            The credential value (e.g. the password)

        created_at : typing.Optional[str]
            The timestamp of creation of the credential

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Add a credential, overwritting if already exists

        Examples
        --------
        from fern import AccessCredentialType, FernApi

        client = FernApi()
        client.identity.add_credential(
            type=AccessCredentialType.PASSWORD,
            value="value",
        )
        """
        _response = self._raw_client.add_credential(
            type=type, value=value, created_at=created_at, request_options=request_options
        )
        return _response.data


class AsyncIdentityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIdentityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIdentityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIdentityClient
        """
        return self._raw_client

    async def get_users_account(self, *, request_options: typing.Optional[RequestOptions] = None) -> Account:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Account
            User details for caller's user

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.identity.get_users_account()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_account(request_options=request_options)
        return _response.data

    async def get_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User details for caller's user

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.identity.get_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user(request_options=request_options)
        return _response.data

    async def get_credentials(self, *, request_options: typing.Optional[RequestOptions] = None) -> CredentialList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CredentialList
            User credential listing

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.identity.get_credentials()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_credentials(request_options=request_options)
        return _response.data

    async def add_credential(
        self,
        *,
        type: AccessCredentialType,
        value: str,
        created_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Parameters
        ----------
        type : AccessCredentialType
            The type of credential

        value : str
            The credential value (e.g. the password)

        created_at : typing.Optional[str]
            The timestamp of creation of the credential

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Add a credential, overwritting if already exists

        Examples
        --------
        import asyncio

        from fern import AccessCredentialType, AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.identity.add_credential(
                type=AccessCredentialType.PASSWORD,
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_credential(
            type=type, value=value, created_at=created_at, request_options=request_options
        )
        return _response.data
