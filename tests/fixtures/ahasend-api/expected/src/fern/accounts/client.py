

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.account import Account
from ..types.account_members_response import AccountMembersResponse
from ..types.success_response import SuccessResponse
from ..types.user_account import UserAccount
from .raw_client import AsyncRawAccountsClient, RawAccountsClient
from .types.add_member_request_role import AddMemberRequestRole


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

    def get_account(self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Account:
        """
        Returns account information

        Parameters
        ----------
        account_id : str
            Account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Account
            Account details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounts.get_account(
            account_id="account_id",
        )
        """
        _response = self._raw_client.get_account(account_id, request_options=request_options)
        return _response.data

    def update_account(
        self,
        account_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        website: typing.Optional[str] = OMIT,
        about: typing.Optional[str] = OMIT,
        track_opens: typing.Optional[bool] = OMIT,
        track_clicks: typing.Optional[bool] = OMIT,
        reject_bad_recipients: typing.Optional[bool] = OMIT,
        reject_mistyped_recipients: typing.Optional[bool] = OMIT,
        message_metadata_retention: typing.Optional[int] = OMIT,
        message_data_retention: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Account:
        """
        Updates account settings

        **Validation Requirements:**
        - `name` must be maximum 255 characters
        - `website` must be a valid URL
        - `message_metadata_retention` must be between 1 and 30 days
        - `message_data_retention` must be between 0 and 30 days

        Parameters
        ----------
        account_id : str
            Account ID

        name : typing.Optional[str]
            Account name

        website : typing.Optional[str]
            Account website URL

        about : typing.Optional[str]
            Account description (used for account verification)

        track_opens : typing.Optional[bool]
            Default open tracking setting

        track_clicks : typing.Optional[bool]
            Default click tracking setting

        reject_bad_recipients : typing.Optional[bool]
            Whether to reject bad recipients

        reject_mistyped_recipients : typing.Optional[bool]
            Whether to reject mistyped recipients

        message_metadata_retention : typing.Optional[int]
            Default message metadata retention in days

        message_data_retention : typing.Optional[int]
            Default message data retention in days

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Account
            Account updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounts.update_account(
            account_id="account_id",
            name="Updated Company Name",
            website="https://example.com",
            track_opens=True,
        )
        """
        _response = self._raw_client.update_account(
            account_id,
            name=name,
            website=website,
            about=about,
            track_opens=track_opens,
            track_clicks=track_clicks,
            reject_bad_recipients=reject_bad_recipients,
            reject_mistyped_recipients=reject_mistyped_recipients,
            message_metadata_retention=message_metadata_retention,
            message_data_retention=message_data_retention,
            request_options=request_options,
        )
        return _response.data

    def get_account_members(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountMembersResponse:
        """
        Returns a list of account members

        Parameters
        ----------
        account_id : str
            Account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountMembersResponse
            List of account members

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounts.get_account_members(
            account_id="account_id",
        )
        """
        _response = self._raw_client.get_account_members(account_id, request_options=request_options)
        return _response.data

    def add_account_member(
        self,
        account_id: str,
        *,
        email: str,
        role: AddMemberRequestRole,
        idempotency_key: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserAccount:
        """
        Adds a new member to the account

        **Validation Requirements:**
        - `email` must be a valid email address
        - `role` must be one of: Administrator, Developer, Analyst, Billing Manager

        Parameters
        ----------
        account_id : str
            Account ID

        email : str
            Email address of the user to add

        role : AddMemberRequestRole
            Role to assign to the user

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        name : typing.Optional[str]
            Display name for the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserAccount
            Member added successfully

        Examples
        --------
        from fern.accounts import AddMemberRequestRole

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounts.add_account_member(
            account_id="account_id",
            idempotency_key="user-12345-create-domain-20240101",
            email="user@example.com",
            name="John Doe",
            role=AddMemberRequestRole.DEVELOPER,
        )
        """
        _response = self._raw_client.add_account_member(
            account_id,
            email=email,
            role=role,
            idempotency_key=idempotency_key,
            name=name,
            request_options=request_options,
        )
        return _response.data

    def remove_account_member(
        self, account_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Removes a member from the account

        **Restrictions:**
        - You cannot delete yourself
        - You cannot delete the account owner

        Parameters
        ----------
        account_id : str
            Account ID

        user_id : str
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Member removed successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounts.remove_account_member(
            account_id="account_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.remove_account_member(account_id, user_id, request_options=request_options)
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

    async def get_account(self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Account:
        """
        Returns account information

        Parameters
        ----------
        account_id : str
            Account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Account
            Account details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounts.get_account(
                account_id="account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_account(account_id, request_options=request_options)
        return _response.data

    async def update_account(
        self,
        account_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        website: typing.Optional[str] = OMIT,
        about: typing.Optional[str] = OMIT,
        track_opens: typing.Optional[bool] = OMIT,
        track_clicks: typing.Optional[bool] = OMIT,
        reject_bad_recipients: typing.Optional[bool] = OMIT,
        reject_mistyped_recipients: typing.Optional[bool] = OMIT,
        message_metadata_retention: typing.Optional[int] = OMIT,
        message_data_retention: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Account:
        """
        Updates account settings

        **Validation Requirements:**
        - `name` must be maximum 255 characters
        - `website` must be a valid URL
        - `message_metadata_retention` must be between 1 and 30 days
        - `message_data_retention` must be between 0 and 30 days

        Parameters
        ----------
        account_id : str
            Account ID

        name : typing.Optional[str]
            Account name

        website : typing.Optional[str]
            Account website URL

        about : typing.Optional[str]
            Account description (used for account verification)

        track_opens : typing.Optional[bool]
            Default open tracking setting

        track_clicks : typing.Optional[bool]
            Default click tracking setting

        reject_bad_recipients : typing.Optional[bool]
            Whether to reject bad recipients

        reject_mistyped_recipients : typing.Optional[bool]
            Whether to reject mistyped recipients

        message_metadata_retention : typing.Optional[int]
            Default message metadata retention in days

        message_data_retention : typing.Optional[int]
            Default message data retention in days

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Account
            Account updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounts.update_account(
                account_id="account_id",
                name="Updated Company Name",
                website="https://example.com",
                track_opens=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_account(
            account_id,
            name=name,
            website=website,
            about=about,
            track_opens=track_opens,
            track_clicks=track_clicks,
            reject_bad_recipients=reject_bad_recipients,
            reject_mistyped_recipients=reject_mistyped_recipients,
            message_metadata_retention=message_metadata_retention,
            message_data_retention=message_data_retention,
            request_options=request_options,
        )
        return _response.data

    async def get_account_members(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountMembersResponse:
        """
        Returns a list of account members

        Parameters
        ----------
        account_id : str
            Account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountMembersResponse
            List of account members

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounts.get_account_members(
                account_id="account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_account_members(account_id, request_options=request_options)
        return _response.data

    async def add_account_member(
        self,
        account_id: str,
        *,
        email: str,
        role: AddMemberRequestRole,
        idempotency_key: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserAccount:
        """
        Adds a new member to the account

        **Validation Requirements:**
        - `email` must be a valid email address
        - `role` must be one of: Administrator, Developer, Analyst, Billing Manager

        Parameters
        ----------
        account_id : str
            Account ID

        email : str
            Email address of the user to add

        role : AddMemberRequestRole
            Role to assign to the user

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        name : typing.Optional[str]
            Display name for the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserAccount
            Member added successfully

        Examples
        --------
        import asyncio

        from fern.accounts import AddMemberRequestRole

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounts.add_account_member(
                account_id="account_id",
                idempotency_key="user-12345-create-domain-20240101",
                email="user@example.com",
                name="John Doe",
                role=AddMemberRequestRole.DEVELOPER,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_account_member(
            account_id,
            email=email,
            role=role,
            idempotency_key=idempotency_key,
            name=name,
            request_options=request_options,
        )
        return _response.data

    async def remove_account_member(
        self, account_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Removes a member from the account

        **Restrictions:**
        - You cannot delete yourself
        - You cannot delete the account owner

        Parameters
        ----------
        account_id : str
            Account ID

        user_id : str
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Member removed successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounts.remove_account_member(
                account_id="account_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_account_member(account_id, user_id, request_options=request_options)
        return _response.data
