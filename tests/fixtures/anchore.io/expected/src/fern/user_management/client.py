

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.access_credential_type import AccessCredentialType
from ..types.account import Account
from ..types.account_list import AccountList
from ..types.account_status import AccountStatus
from ..types.account_status_state import AccountStatusState
from ..types.credential_list import CredentialList
from ..types.user import User
from .raw_client import AsyncRawUserManagementClient, RawUserManagementClient
from .types.delete_user_credential_request_credential_type import DeleteUserCredentialRequestCredentialType
from .types.list_accounts_request_state import ListAccountsRequestState


OMIT = typing.cast(typing.Any, ...)


class UserManagementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserManagementClient
        """
        return self._raw_client

    def list_accounts(
        self,
        *,
        state: typing.Optional[ListAccountsRequestState] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountList:
        """
        Parameters
        ----------
        state : typing.Optional[ListAccountsRequestState]
            Filter accounts by state

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountList
            Accound summary listing

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.user_management.list_accounts()
        """
        _response = self._raw_client.list_accounts(state=state, request_options=request_options)
        return _response.data

    def create_account(
        self, *, name: str, email: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> Account:
        """
        Parameters
        ----------
        name : str
            The account name to use. This will identify the account and must be globally unique in the system.

        email : typing.Optional[str]
            An optional email to associate with the account for contact purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Account
            Account Record

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.user_management.create_account(
            name="name",
        )
        """
        _response = self._raw_client.create_account(name=name, email=email, request_options=request_options)
        return _response.data

    def get_account(self, accountname: str, *, request_options: typing.Optional[RequestOptions] = None) -> Account:
        """
        Parameters
        ----------
        accountname : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Account
            Get user information

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.user_management.get_account(
            accountname="accountname",
        )
        """
        _response = self._raw_client.get_account(accountname, request_options=request_options)
        return _response.data

    def delete_account(self, accountname: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        accountname : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.user_management.delete_account(
            accountname="accountname",
        )
        """
        _response = self._raw_client.delete_account(accountname, request_options=request_options)
        return _response.data

    def update_account_state(
        self,
        accountname: str,
        *,
        state: typing.Optional[AccountStatusState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountStatus:
        """
        Parameters
        ----------
        accountname : str

        state : typing.Optional[AccountStatusState]
            The status of the account

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountStatus
            Updated state of the account

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.user_management.update_account_state(
            accountname="accountname",
        )
        """
        _response = self._raw_client.update_account_state(accountname, state=state, request_options=request_options)
        return _response.data

    def list_users(
        self, accountname: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[User]:
        """
        Parameters
        ----------
        accountname : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[User]
            User listing

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.user_management.list_users(
            accountname="accountname",
        )
        """
        _response = self._raw_client.list_users(accountname, request_options=request_options)
        return _response.data

    def create_user(
        self, accountname: str, *, password: str, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Parameters
        ----------
        accountname : str

        password : str
            The initial password for the user, must be at least 6 characters, up to 128

        username : str
            The username to create

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Credential summary

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.user_management.create_user(
            accountname="accountname",
            password="password",
            username="username",
        )
        """
        _response = self._raw_client.create_user(
            accountname, password=password, username=username, request_options=request_options
        )
        return _response.data

    def get_account_user(
        self, accountname: str, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Parameters
        ----------
        accountname : str

        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User record

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.user_management.get_account_user(
            accountname="accountname",
            username="username",
        )
        """
        _response = self._raw_client.get_account_user(accountname, username, request_options=request_options)
        return _response.data

    def delete_user(
        self, accountname: str, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        accountname : str

        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.user_management.delete_user(
            accountname="accountname",
            username="username",
        )
        """
        _response = self._raw_client.delete_user(accountname, username, request_options=request_options)
        return _response.data

    def list_user_credentials(
        self, accountname: str, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CredentialList:
        """
        Parameters
        ----------
        accountname : str

        username : str

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
        client.user_management.list_user_credentials(
            accountname="accountname",
            username="username",
        )
        """
        _response = self._raw_client.list_user_credentials(accountname, username, request_options=request_options)
        return _response.data

    def create_user_credential(
        self,
        accountname: str,
        username: str,
        *,
        type: AccessCredentialType,
        value: str,
        created_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Parameters
        ----------
        accountname : str

        username : str

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
        client.user_management.create_user_credential(
            accountname="accountname",
            username="username",
            type=AccessCredentialType.PASSWORD,
            value="value",
        )
        """
        _response = self._raw_client.create_user_credential(
            accountname, username, type=type, value=value, created_at=created_at, request_options=request_options
        )
        return _response.data

    def delete_user_credential(
        self,
        accountname: str,
        username: str,
        *,
        credential_type: DeleteUserCredentialRequestCredentialType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        accountname : str

        username : str

        credential_type : DeleteUserCredentialRequestCredentialType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.user_management import DeleteUserCredentialRequestCredentialType

        from fern import FernApi

        client = FernApi()
        client.user_management.delete_user_credential(
            accountname="accountname",
            username="username",
            credential_type=DeleteUserCredentialRequestCredentialType.PASSWORD,
        )
        """
        _response = self._raw_client.delete_user_credential(
            accountname, username, credential_type=credential_type, request_options=request_options
        )
        return _response.data


class AsyncUserManagementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserManagementClient
        """
        return self._raw_client

    async def list_accounts(
        self,
        *,
        state: typing.Optional[ListAccountsRequestState] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountList:
        """
        Parameters
        ----------
        state : typing.Optional[ListAccountsRequestState]
            Filter accounts by state

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountList
            Accound summary listing

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.user_management.list_accounts()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_accounts(state=state, request_options=request_options)
        return _response.data

    async def create_account(
        self, *, name: str, email: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> Account:
        """
        Parameters
        ----------
        name : str
            The account name to use. This will identify the account and must be globally unique in the system.

        email : typing.Optional[str]
            An optional email to associate with the account for contact purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Account
            Account Record

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.user_management.create_account(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_account(name=name, email=email, request_options=request_options)
        return _response.data

    async def get_account(
        self, accountname: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Account:
        """
        Parameters
        ----------
        accountname : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Account
            Get user information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.user_management.get_account(
                accountname="accountname",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_account(accountname, request_options=request_options)
        return _response.data

    async def delete_account(
        self, accountname: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        accountname : str

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
            await client.user_management.delete_account(
                accountname="accountname",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_account(accountname, request_options=request_options)
        return _response.data

    async def update_account_state(
        self,
        accountname: str,
        *,
        state: typing.Optional[AccountStatusState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountStatus:
        """
        Parameters
        ----------
        accountname : str

        state : typing.Optional[AccountStatusState]
            The status of the account

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountStatus
            Updated state of the account

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.user_management.update_account_state(
                accountname="accountname",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_account_state(
            accountname, state=state, request_options=request_options
        )
        return _response.data

    async def list_users(
        self, accountname: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[User]:
        """
        Parameters
        ----------
        accountname : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[User]
            User listing

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.user_management.list_users(
                accountname="accountname",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_users(accountname, request_options=request_options)
        return _response.data

    async def create_user(
        self, accountname: str, *, password: str, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Parameters
        ----------
        accountname : str

        password : str
            The initial password for the user, must be at least 6 characters, up to 128

        username : str
            The username to create

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Credential summary

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.user_management.create_user(
                accountname="accountname",
                password="password",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_user(
            accountname, password=password, username=username, request_options=request_options
        )
        return _response.data

    async def get_account_user(
        self, accountname: str, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Parameters
        ----------
        accountname : str

        username : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User record

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.user_management.get_account_user(
                accountname="accountname",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_account_user(accountname, username, request_options=request_options)
        return _response.data

    async def delete_user(
        self, accountname: str, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        accountname : str

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

        client = AsyncFernApi()


        async def main() -> None:
            await client.user_management.delete_user(
                accountname="accountname",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user(accountname, username, request_options=request_options)
        return _response.data

    async def list_user_credentials(
        self, accountname: str, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CredentialList:
        """
        Parameters
        ----------
        accountname : str

        username : str

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
            await client.user_management.list_user_credentials(
                accountname="accountname",
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_user_credentials(accountname, username, request_options=request_options)
        return _response.data

    async def create_user_credential(
        self,
        accountname: str,
        username: str,
        *,
        type: AccessCredentialType,
        value: str,
        created_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Parameters
        ----------
        accountname : str

        username : str

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
            await client.user_management.create_user_credential(
                accountname="accountname",
                username="username",
                type=AccessCredentialType.PASSWORD,
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_user_credential(
            accountname, username, type=type, value=value, created_at=created_at, request_options=request_options
        )
        return _response.data

    async def delete_user_credential(
        self,
        accountname: str,
        username: str,
        *,
        credential_type: DeleteUserCredentialRequestCredentialType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        accountname : str

        username : str

        credential_type : DeleteUserCredentialRequestCredentialType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.user_management import DeleteUserCredentialRequestCredentialType

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.user_management.delete_user_credential(
                accountname="accountname",
                username="username",
                credential_type=DeleteUserCredentialRequestCredentialType.PASSWORD,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user_credential(
            accountname, username, credential_type=credential_type, request_options=request_options
        )
        return _response.data
