

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_key import ApiKey
from ..types.paginated_api_keys_response import PaginatedApiKeysResponse
from ..types.paginated_sub_accounts_response import PaginatedSubAccountsResponse
from ..types.sub_account import SubAccount
from ..types.sub_account_usage_response import SubAccountUsageResponse
from ..types.success_response import SuccessResponse
from ..types.update_api_key_request import UpdateApiKeyRequest
from ..types.update_sub_account_request import UpdateSubAccountRequest
from .raw_client import AsyncRawSubAccountsClient, RawSubAccountsClient
from .types.create_sub_account_api_key_response import CreateSubAccountApiKeyResponse


OMIT = typing.cast(typing.Any, ...)


class SubAccountsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSubAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSubAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSubAccountsClient
        """
        return self._raw_client

    def list_sub_accounts(
        self,
        account_id: str,
        *,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedSubAccountsResponse:
        """
        Returns a cursor-paginated list of sub accounts under the parent account. Soft-deleted sub accounts are not included; usage billed for sub accounts deleted during the current period is reported by the usage endpoint's `removed_sub_accounts` aggregate.

        Parameters
        ----------
        account_id : str
            Parent account ID

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value from `next_cursor` in the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page. Provide the value from `previous_cursor` in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedSubAccountsResponse
            List of sub accounts

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sub_accounts.list_sub_accounts(
            account_id="account_id",
        )
        """
        _response = self._raw_client.list_sub_accounts(
            account_id, limit=limit, after=after, before=before, request_options=request_options
        )
        return _response.data

    def create_sub_account(
        self,
        account_id: str,
        *,
        name: str,
        website: str,
        idempotency_key: typing.Optional[str] = None,
        monthly_credit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubAccount:
        """
        Creates a new sub account under the parent account

        Parameters
        ----------
        account_id : str
            Parent account ID

        name : str
            Human-readable name for the sub account; leading and trailing whitespace is trimmed and the result must not be blank

        website : str
            Account website domain

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        monthly_credit : typing.Optional[int]
            Optional monthly cap; 0 means no cap

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubAccount
            Sub account created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sub_accounts.create_sub_account(
            account_id="account_id",
            idempotency_key="user-12345-create-domain-20240101",
            name="Acme Subsidiary",
            website="acme.example.com",
            monthly_credit=0,
        )
        """
        _response = self._raw_client.create_sub_account(
            account_id,
            name=name,
            website=website,
            idempotency_key=idempotency_key,
            monthly_credit=monthly_credit,
            request_options=request_options,
        )
        return _response.data

    def get_sub_accounts_usage(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SubAccountUsageResponse:
        """
        Returns current billing-period usage and proportional allocated cost for the parent and active sub accounts

        Parameters
        ----------
        account_id : str
            Parent account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubAccountUsageResponse
            Sub-account usage breakdown

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sub_accounts.get_sub_accounts_usage(
            account_id="account_id",
        )
        """
        _response = self._raw_client.get_sub_accounts_usage(account_id, request_options=request_options)
        return _response.data

    def get_sub_account(
        self, account_id: str, sub_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SubAccount:
        """
        Returns a specific sub account under the parent account

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubAccount
            Sub account details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sub_accounts.get_sub_account(
            account_id="account_id",
            sub_account_id="sub_account_id",
        )
        """
        _response = self._raw_client.get_sub_account(account_id, sub_account_id, request_options=request_options)
        return _response.data

    def update_sub_account(
        self,
        account_id: str,
        sub_account_id: str,
        *,
        request: UpdateSubAccountRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubAccount:
        """
        Updates a sub account's editable settings

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        request : UpdateSubAccountRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubAccount
            Sub account updated successfully

        Examples
        --------
        from fern import FernApi, UpdateSubAccountRequestName

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sub_accounts.update_sub_account(
            account_id="account_id",
            sub_account_id="sub_account_id",
            request=UpdateSubAccountRequestName(
                name="name",
            ),
        )
        """
        _response = self._raw_client.update_sub_account(
            account_id, sub_account_id, request=request, request_options=request_options
        )
        return _response.data

    def delete_sub_account(
        self, account_id: str, sub_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Soft-deletes a sub account under the parent account

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Sub account deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sub_accounts.delete_sub_account(
            account_id="account_id",
            sub_account_id="sub_account_id",
        )
        """
        _response = self._raw_client.delete_sub_account(account_id, sub_account_id, request_options=request_options)
        return _response.data

    def suspend_sub_account(
        self,
        account_id: str,
        sub_account_id: str,
        *,
        reason: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubAccount:
        """
        Suspends a sub account under the parent account

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        reason : str
            Reason shown on the sub account suspension record

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubAccount
            Sub account suspended successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sub_accounts.suspend_sub_account(
            account_id="account_id",
            sub_account_id="sub_account_id",
            reason="Customer requested temporary pause",
        )
        """
        _response = self._raw_client.suspend_sub_account(
            account_id, sub_account_id, reason=reason, request_options=request_options
        )
        return _response.data

    def unsuspend_sub_account(
        self, account_id: str, sub_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SubAccount:
        """
        Unsuspends a sub account under the parent account

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubAccount
            Sub account unsuspended successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sub_accounts.unsuspend_sub_account(
            account_id="account_id",
            sub_account_id="sub_account_id",
        )
        """
        _response = self._raw_client.unsuspend_sub_account(account_id, sub_account_id, request_options=request_options)
        return _response.data

    def list_sub_account_api_keys(
        self,
        account_id: str,
        sub_account_id: str,
        *,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedApiKeysResponse:
        """
        Returns a cursor-paginated list of API keys owned by a sub account. The `secret_key` field is omitted from list responses.

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value from `next_cursor` in the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page. Provide the value from `previous_cursor` in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedApiKeysResponse
            List of sub-account API keys

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sub_accounts.list_sub_account_api_keys(
            account_id="account_id",
            sub_account_id="sub_account_id",
        )
        """
        _response = self._raw_client.list_sub_account_api_keys(
            account_id, sub_account_id, limit=limit, after=after, before=before, request_options=request_options
        )
        return _response.data

    def create_sub_account_api_key(
        self,
        account_id: str,
        sub_account_id: str,
        *,
        label: str,
        scopes: typing.Sequence[str],
        idempotency_key: typing.Optional[str] = None,
        ip_allow_list: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSubAccountApiKeyResponse:
        """
        Creates an API key owned by the sub account. Parent credentials must belong to the parent account and include `sub-account-api-keys:write`; sub-account credentials cannot manage nested API keys. The returned `secret_key` authenticates as the child account and should be stored immediately.

        Bootstrap example:
        1. Create the sub account with `POST /v2/accounts/{account_id}/sub-accounts` and a unique `Idempotency-Key`.
        2. Create the bootstrap child API key with this endpoint and a different unique `Idempotency-Key`.
        3. Store the one-time `secret_key` from the `201` response. Exact idempotent replays within 5 minutes return the same `secret_key`.
        4. Use that child secret with the child `sub_account_id` as the `account_id` on ordinary v2 routes.

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        label : str
            Human-readable label for the API key; must not be empty

        scopes : typing.Sequence[str]
            Array of scope strings to grant to this API key

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        ip_allow_list : typing.Optional[typing.Sequence[str]]
            Optional list of source IPs allowed to authenticate with this key. Each entry is a CIDR block (e.g. `203.0.113.0/24`) or a bare IPv4/IPv6 address (stored as a `/32` or `/128`). Entries are canonicalized (host bits are masked) and de-duplicated. The allow-all prefixes `0.0.0.0/0` and `::/0` are rejected, and at most 100 entries are allowed after de-duplication. Omit the field or pass an empty array to leave the key usable from any IP.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSubAccountApiKeyResponse
            Sub-account API key created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sub_accounts.create_sub_account_api_key(
            account_id="account_id",
            sub_account_id="sub_account_id",
            idempotency_key="user-12345-create-domain-20240101",
            label="Bootstrap key",
            scopes=["messages:send:all", "domains:read"],
        )
        """
        _response = self._raw_client.create_sub_account_api_key(
            account_id,
            sub_account_id,
            label=label,
            scopes=scopes,
            idempotency_key=idempotency_key,
            ip_allow_list=ip_allow_list,
            request_options=request_options,
        )
        return _response.data

    def get_sub_account_api_key(
        self,
        account_id: str,
        sub_account_id: str,
        key_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKey:
        """
        Returns a specific API key owned by a sub account. The `secret_key` field is omitted from read responses.

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        key_id : str
            API key ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Sub-account API key details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sub_accounts.get_sub_account_api_key(
            account_id="account_id",
            sub_account_id="sub_account_id",
            key_id="key_id",
        )
        """
        _response = self._raw_client.get_sub_account_api_key(
            account_id, sub_account_id, key_id, request_options=request_options
        )
        return _response.data

    def update_sub_account_api_key(
        self,
        account_id: str,
        sub_account_id: str,
        key_id: str,
        *,
        request: UpdateApiKeyRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKey:
        """
        Updates the label and scopes for an API key owned by a sub account. Updated scopes are validated against the child account.

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        key_id : str
            API key ID

        request : UpdateApiKeyRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Sub-account API key updated successfully

        Examples
        --------
        from fern import FernApi, UpdateApiKeyRequestLabel

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sub_accounts.update_sub_account_api_key(
            account_id="account_id",
            sub_account_id="sub_account_id",
            key_id="key_id",
            request=UpdateApiKeyRequestLabel(
                label="Updated bootstrap key",
            ),
        )
        """
        _response = self._raw_client.update_sub_account_api_key(
            account_id, sub_account_id, key_id, request=request, request_options=request_options
        )
        return _response.data

    def delete_sub_account_api_key(
        self,
        account_id: str,
        sub_account_id: str,
        key_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
        """
        Deletes an API key owned by a sub account.

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        key_id : str
            API key ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Sub-account API key deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sub_accounts.delete_sub_account_api_key(
            account_id="account_id",
            sub_account_id="sub_account_id",
            key_id="key_id",
        )
        """
        _response = self._raw_client.delete_sub_account_api_key(
            account_id, sub_account_id, key_id, request_options=request_options
        )
        return _response.data


class AsyncSubAccountsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSubAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSubAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSubAccountsClient
        """
        return self._raw_client

    async def list_sub_accounts(
        self,
        account_id: str,
        *,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedSubAccountsResponse:
        """
        Returns a cursor-paginated list of sub accounts under the parent account. Soft-deleted sub accounts are not included; usage billed for sub accounts deleted during the current period is reported by the usage endpoint's `removed_sub_accounts` aggregate.

        Parameters
        ----------
        account_id : str
            Parent account ID

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value from `next_cursor` in the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page. Provide the value from `previous_cursor` in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedSubAccountsResponse
            List of sub accounts

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sub_accounts.list_sub_accounts(
                account_id="account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_sub_accounts(
            account_id, limit=limit, after=after, before=before, request_options=request_options
        )
        return _response.data

    async def create_sub_account(
        self,
        account_id: str,
        *,
        name: str,
        website: str,
        idempotency_key: typing.Optional[str] = None,
        monthly_credit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubAccount:
        """
        Creates a new sub account under the parent account

        Parameters
        ----------
        account_id : str
            Parent account ID

        name : str
            Human-readable name for the sub account; leading and trailing whitespace is trimmed and the result must not be blank

        website : str
            Account website domain

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        monthly_credit : typing.Optional[int]
            Optional monthly cap; 0 means no cap

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubAccount
            Sub account created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sub_accounts.create_sub_account(
                account_id="account_id",
                idempotency_key="user-12345-create-domain-20240101",
                name="Acme Subsidiary",
                website="acme.example.com",
                monthly_credit=0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_sub_account(
            account_id,
            name=name,
            website=website,
            idempotency_key=idempotency_key,
            monthly_credit=monthly_credit,
            request_options=request_options,
        )
        return _response.data

    async def get_sub_accounts_usage(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SubAccountUsageResponse:
        """
        Returns current billing-period usage and proportional allocated cost for the parent and active sub accounts

        Parameters
        ----------
        account_id : str
            Parent account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubAccountUsageResponse
            Sub-account usage breakdown

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sub_accounts.get_sub_accounts_usage(
                account_id="account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sub_accounts_usage(account_id, request_options=request_options)
        return _response.data

    async def get_sub_account(
        self, account_id: str, sub_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SubAccount:
        """
        Returns a specific sub account under the parent account

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubAccount
            Sub account details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sub_accounts.get_sub_account(
                account_id="account_id",
                sub_account_id="sub_account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sub_account(account_id, sub_account_id, request_options=request_options)
        return _response.data

    async def update_sub_account(
        self,
        account_id: str,
        sub_account_id: str,
        *,
        request: UpdateSubAccountRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubAccount:
        """
        Updates a sub account's editable settings

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        request : UpdateSubAccountRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubAccount
            Sub account updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, UpdateSubAccountRequestName

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sub_accounts.update_sub_account(
                account_id="account_id",
                sub_account_id="sub_account_id",
                request=UpdateSubAccountRequestName(
                    name="name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_sub_account(
            account_id, sub_account_id, request=request, request_options=request_options
        )
        return _response.data

    async def delete_sub_account(
        self, account_id: str, sub_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Soft-deletes a sub account under the parent account

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Sub account deleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sub_accounts.delete_sub_account(
                account_id="account_id",
                sub_account_id="sub_account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_sub_account(
            account_id, sub_account_id, request_options=request_options
        )
        return _response.data

    async def suspend_sub_account(
        self,
        account_id: str,
        sub_account_id: str,
        *,
        reason: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubAccount:
        """
        Suspends a sub account under the parent account

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        reason : str
            Reason shown on the sub account suspension record

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubAccount
            Sub account suspended successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sub_accounts.suspend_sub_account(
                account_id="account_id",
                sub_account_id="sub_account_id",
                reason="Customer requested temporary pause",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.suspend_sub_account(
            account_id, sub_account_id, reason=reason, request_options=request_options
        )
        return _response.data

    async def unsuspend_sub_account(
        self, account_id: str, sub_account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SubAccount:
        """
        Unsuspends a sub account under the parent account

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubAccount
            Sub account unsuspended successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sub_accounts.unsuspend_sub_account(
                account_id="account_id",
                sub_account_id="sub_account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unsuspend_sub_account(
            account_id, sub_account_id, request_options=request_options
        )
        return _response.data

    async def list_sub_account_api_keys(
        self,
        account_id: str,
        sub_account_id: str,
        *,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedApiKeysResponse:
        """
        Returns a cursor-paginated list of API keys owned by a sub account. The `secret_key` field is omitted from list responses.

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value from `next_cursor` in the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page. Provide the value from `previous_cursor` in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedApiKeysResponse
            List of sub-account API keys

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sub_accounts.list_sub_account_api_keys(
                account_id="account_id",
                sub_account_id="sub_account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_sub_account_api_keys(
            account_id, sub_account_id, limit=limit, after=after, before=before, request_options=request_options
        )
        return _response.data

    async def create_sub_account_api_key(
        self,
        account_id: str,
        sub_account_id: str,
        *,
        label: str,
        scopes: typing.Sequence[str],
        idempotency_key: typing.Optional[str] = None,
        ip_allow_list: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSubAccountApiKeyResponse:
        """
        Creates an API key owned by the sub account. Parent credentials must belong to the parent account and include `sub-account-api-keys:write`; sub-account credentials cannot manage nested API keys. The returned `secret_key` authenticates as the child account and should be stored immediately.

        Bootstrap example:
        1. Create the sub account with `POST /v2/accounts/{account_id}/sub-accounts` and a unique `Idempotency-Key`.
        2. Create the bootstrap child API key with this endpoint and a different unique `Idempotency-Key`.
        3. Store the one-time `secret_key` from the `201` response. Exact idempotent replays within 5 minutes return the same `secret_key`.
        4. Use that child secret with the child `sub_account_id` as the `account_id` on ordinary v2 routes.

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        label : str
            Human-readable label for the API key; must not be empty

        scopes : typing.Sequence[str]
            Array of scope strings to grant to this API key

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        ip_allow_list : typing.Optional[typing.Sequence[str]]
            Optional list of source IPs allowed to authenticate with this key. Each entry is a CIDR block (e.g. `203.0.113.0/24`) or a bare IPv4/IPv6 address (stored as a `/32` or `/128`). Entries are canonicalized (host bits are masked) and de-duplicated. The allow-all prefixes `0.0.0.0/0` and `::/0` are rejected, and at most 100 entries are allowed after de-duplication. Omit the field or pass an empty array to leave the key usable from any IP.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSubAccountApiKeyResponse
            Sub-account API key created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sub_accounts.create_sub_account_api_key(
                account_id="account_id",
                sub_account_id="sub_account_id",
                idempotency_key="user-12345-create-domain-20240101",
                label="Bootstrap key",
                scopes=["messages:send:all", "domains:read"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_sub_account_api_key(
            account_id,
            sub_account_id,
            label=label,
            scopes=scopes,
            idempotency_key=idempotency_key,
            ip_allow_list=ip_allow_list,
            request_options=request_options,
        )
        return _response.data

    async def get_sub_account_api_key(
        self,
        account_id: str,
        sub_account_id: str,
        key_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKey:
        """
        Returns a specific API key owned by a sub account. The `secret_key` field is omitted from read responses.

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        key_id : str
            API key ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Sub-account API key details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sub_accounts.get_sub_account_api_key(
                account_id="account_id",
                sub_account_id="sub_account_id",
                key_id="key_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sub_account_api_key(
            account_id, sub_account_id, key_id, request_options=request_options
        )
        return _response.data

    async def update_sub_account_api_key(
        self,
        account_id: str,
        sub_account_id: str,
        key_id: str,
        *,
        request: UpdateApiKeyRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKey:
        """
        Updates the label and scopes for an API key owned by a sub account. Updated scopes are validated against the child account.

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        key_id : str
            API key ID

        request : UpdateApiKeyRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            Sub-account API key updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, UpdateApiKeyRequestLabel

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sub_accounts.update_sub_account_api_key(
                account_id="account_id",
                sub_account_id="sub_account_id",
                key_id="key_id",
                request=UpdateApiKeyRequestLabel(
                    label="Updated bootstrap key",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_sub_account_api_key(
            account_id, sub_account_id, key_id, request=request, request_options=request_options
        )
        return _response.data

    async def delete_sub_account_api_key(
        self,
        account_id: str,
        sub_account_id: str,
        key_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
        """
        Deletes an API key owned by a sub account.

        Parameters
        ----------
        account_id : str
            Parent account ID

        sub_account_id : str
            Sub account ID

        key_id : str
            API key ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Sub-account API key deleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sub_accounts.delete_sub_account_api_key(
                account_id="account_id",
                sub_account_id="sub_account_id",
                key_id="key_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_sub_account_api_key(
            account_id, sub_account_id, key_id, request_options=request_options
        )
        return _response.data
