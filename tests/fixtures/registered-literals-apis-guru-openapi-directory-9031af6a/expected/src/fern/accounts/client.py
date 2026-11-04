

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAccountsClient, RawAccountsClient
from .types.add_user_to_account_request_account import AddUserToAccountRequestAccount
from .types.add_user_to_account_request_users_item import AddUserToAccountRequestUsersItem
from .types.add_user_to_account_response import AddUserToAccountResponse
from .types.delete_account_request_identification import DeleteAccountRequestIdentification
from .types.delete_account_response import DeleteAccountResponse
from .types.remove_user_from_account_request_account import RemoveUserFromAccountRequestAccount
from .types.remove_user_from_account_request_users_item import RemoveUserFromAccountRequestUsersItem
from .types.remove_user_from_account_response import RemoveUserFromAccountResponse
from .types.upsert_account_request_identification import UpsertAccountRequestIdentification
from .types.upsert_account_request_properties_value import UpsertAccountRequestPropertiesValue
from .types.upsert_account_response import UpsertAccountResponse


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

    def delete_account(
        self,
        *,
        identification: DeleteAccountRequestIdentification,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteAccountResponse:
        """
        Endpoint used to delete an account.

        Parameters
        ----------
        identification : DeleteAccountRequestIdentification
            Account identification requires an accountId, domain or both

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAccountResponse
            Accepted

        Examples
        --------
        from fern.accounts import DeleteAccountRequestIdentification

        from fern import FernApi

        client = FernApi()
        client.accounts.delete_account(
            identification=DeleteAccountRequestIdentification(),
        )
        """
        _response = self._raw_client.delete_account(identification=identification, request_options=request_options)
        return _response.data

    def upsert_account(
        self,
        *,
        identification: UpsertAccountRequestIdentification,
        properties: typing.Optional[typing.Dict[str, UpsertAccountRequestPropertiesValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpsertAccountResponse:
        """
        Endpoint used to create or update an account.

        Parameters
        ----------
        identification : UpsertAccountRequestIdentification
            Account identification requires an accountId, domain or both

        properties : typing.Optional[typing.Dict[str, UpsertAccountRequestPropertiesValue]]
            The properties being set, possible values are strings, booleans, numbers and datetimes (ISO 8601)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpsertAccountResponse
            Account will be created

        Examples
        --------
        from fern.accounts import UpsertAccountRequestIdentification

        from fern import FernApi

        client = FernApi()
        client.accounts.upsert_account(
            identification=UpsertAccountRequestIdentification(),
        )
        """
        _response = self._raw_client.upsert_account(
            identification=identification, properties=properties, request_options=request_options
        )
        return _response.data

    def add_user_to_account(
        self,
        *,
        account: AddUserToAccountRequestAccount,
        users: typing.Sequence[AddUserToAccountRequestUsersItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddUserToAccountResponse:
        """
        You can add up to 100 users to an account.

        Parameters
        ----------
        account : AddUserToAccountRequestAccount
            Account identification requires an accountId, domain or both

        users : typing.Sequence[AddUserToAccountRequestUsersItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddUserToAccountResponse
            Object was created

        Examples
        --------
        from fern.accounts import (
            AddUserToAccountRequestAccount,
            AddUserToAccountRequestUsersItem,
            AddUserToAccountRequestUsersItemIdentification,
        )

        from fern import FernApi

        client = FernApi()
        client.accounts.add_user_to_account(
            account=AddUserToAccountRequestAccount(),
            users=[
                AddUserToAccountRequestUsersItem(
                    identification=AddUserToAccountRequestUsersItemIdentification(),
                )
            ],
        )
        """
        _response = self._raw_client.add_user_to_account(account=account, users=users, request_options=request_options)
        return _response.data

    def remove_user_from_account(
        self,
        *,
        account: RemoveUserFromAccountRequestAccount,
        users: typing.Sequence[RemoveUserFromAccountRequestUsersItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RemoveUserFromAccountResponse:
        """
        You can remove up to 100 users from an account.

        When removing a user, the user will still be stored in journy.io, but marked as "removed".

        Parameters
        ----------
        account : RemoveUserFromAccountRequestAccount
            Account identification requires an accountId, domain or both

        users : typing.Sequence[RemoveUserFromAccountRequestUsersItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoveUserFromAccountResponse
            No content

        Examples
        --------
        from fern.accounts import (
            RemoveUserFromAccountRequestAccount,
            RemoveUserFromAccountRequestUsersItem,
            RemoveUserFromAccountRequestUsersItemIdentification,
        )

        from fern import FernApi

        client = FernApi()
        client.accounts.remove_user_from_account(
            account=RemoveUserFromAccountRequestAccount(),
            users=[
                RemoveUserFromAccountRequestUsersItem(
                    identification=RemoveUserFromAccountRequestUsersItemIdentification(),
                )
            ],
        )
        """
        _response = self._raw_client.remove_user_from_account(
            account=account, users=users, request_options=request_options
        )
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

    async def delete_account(
        self,
        *,
        identification: DeleteAccountRequestIdentification,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteAccountResponse:
        """
        Endpoint used to delete an account.

        Parameters
        ----------
        identification : DeleteAccountRequestIdentification
            Account identification requires an accountId, domain or both

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAccountResponse
            Accepted

        Examples
        --------
        import asyncio

        from fern.accounts import DeleteAccountRequestIdentification

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounts.delete_account(
                identification=DeleteAccountRequestIdentification(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_account(
            identification=identification, request_options=request_options
        )
        return _response.data

    async def upsert_account(
        self,
        *,
        identification: UpsertAccountRequestIdentification,
        properties: typing.Optional[typing.Dict[str, UpsertAccountRequestPropertiesValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpsertAccountResponse:
        """
        Endpoint used to create or update an account.

        Parameters
        ----------
        identification : UpsertAccountRequestIdentification
            Account identification requires an accountId, domain or both

        properties : typing.Optional[typing.Dict[str, UpsertAccountRequestPropertiesValue]]
            The properties being set, possible values are strings, booleans, numbers and datetimes (ISO 8601)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpsertAccountResponse
            Account will be created

        Examples
        --------
        import asyncio

        from fern.accounts import UpsertAccountRequestIdentification

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounts.upsert_account(
                identification=UpsertAccountRequestIdentification(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert_account(
            identification=identification, properties=properties, request_options=request_options
        )
        return _response.data

    async def add_user_to_account(
        self,
        *,
        account: AddUserToAccountRequestAccount,
        users: typing.Sequence[AddUserToAccountRequestUsersItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddUserToAccountResponse:
        """
        You can add up to 100 users to an account.

        Parameters
        ----------
        account : AddUserToAccountRequestAccount
            Account identification requires an accountId, domain or both

        users : typing.Sequence[AddUserToAccountRequestUsersItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddUserToAccountResponse
            Object was created

        Examples
        --------
        import asyncio

        from fern.accounts import (
            AddUserToAccountRequestAccount,
            AddUserToAccountRequestUsersItem,
            AddUserToAccountRequestUsersItemIdentification,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounts.add_user_to_account(
                account=AddUserToAccountRequestAccount(),
                users=[
                    AddUserToAccountRequestUsersItem(
                        identification=AddUserToAccountRequestUsersItemIdentification(),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_user_to_account(
            account=account, users=users, request_options=request_options
        )
        return _response.data

    async def remove_user_from_account(
        self,
        *,
        account: RemoveUserFromAccountRequestAccount,
        users: typing.Sequence[RemoveUserFromAccountRequestUsersItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RemoveUserFromAccountResponse:
        """
        You can remove up to 100 users from an account.

        When removing a user, the user will still be stored in journy.io, but marked as "removed".

        Parameters
        ----------
        account : RemoveUserFromAccountRequestAccount
            Account identification requires an accountId, domain or both

        users : typing.Sequence[RemoveUserFromAccountRequestUsersItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoveUserFromAccountResponse
            No content

        Examples
        --------
        import asyncio

        from fern.accounts import (
            RemoveUserFromAccountRequestAccount,
            RemoveUserFromAccountRequestUsersItem,
            RemoveUserFromAccountRequestUsersItemIdentification,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.accounts.remove_user_from_account(
                account=RemoveUserFromAccountRequestAccount(),
                users=[
                    RemoveUserFromAccountRequestUsersItem(
                        identification=RemoveUserFromAccountRequestUsersItemIdentification(),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_user_from_account(
            account=account, users=users, request_options=request_options
        )
        return _response.data
