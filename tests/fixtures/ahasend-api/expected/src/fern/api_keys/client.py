

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_key import ApiKey
from ..types.paginated_api_keys_response import PaginatedApiKeysResponse
from ..types.success_response import SuccessResponse
from ..types.update_api_key_request import UpdateApiKeyRequest
from .raw_client import AsyncRawApiKeysClient, RawApiKeysClient
from .types.create_api_key_response import CreateApiKeyResponse


OMIT = typing.cast(typing.Any, ...)


class ApiKeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApiKeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApiKeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApiKeysClient
        """
        return self._raw_client

    def get_api_keys(
        self,
        account_id: str,
        *,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedApiKeysResponse:
        """
        Returns a list of API keys for the account

        Parameters
        ----------
        account_id : str
            Account ID

        limit : typing.Optional[int]
            Maximum number of items to return

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedApiKeysResponse
            List of API keys

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.api_keys.get_api_keys(
            account_id="account_id",
        )
        """
        _response = self._raw_client.get_api_keys(
            account_id, limit=limit, after=after, before=before, request_options=request_options
        )
        return _response.data

    def create_api_key(
        self,
        account_id: str,
        *,
        label: str,
        scopes: typing.Sequence[str],
        idempotency_key: typing.Optional[str] = None,
        ip_allow_list: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateApiKeyResponse:
        """
        Creates a new API key with the specified scopes

        Parameters
        ----------
        account_id : str
            Account ID

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
        CreateApiKeyResponse
            API key created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.api_keys.create_api_key(
            account_id="account_id",
            idempotency_key="user-12345-create-domain-20240101",
            label="Production API Key",
            scopes=["messages:send:all", "domains:read"],
            ip_allow_list=["203.0.113.0/24", "198.51.100.7"],
        )
        """
        _response = self._raw_client.create_api_key(
            account_id,
            label=label,
            scopes=scopes,
            idempotency_key=idempotency_key,
            ip_allow_list=ip_allow_list,
            request_options=request_options,
        )
        return _response.data

    def get_api_key(
        self, account_id: str, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKey:
        """
        Returns a specific API key by ID

        Parameters
        ----------
        account_id : str
            Account ID

        key_id : str
            API Key ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            API key details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.api_keys.get_api_key(
            account_id="account_id",
            key_id="key_id",
        )
        """
        _response = self._raw_client.get_api_key(account_id, key_id, request_options=request_options)
        return _response.data

    def update_api_key(
        self,
        account_id: str,
        key_id: str,
        *,
        request: UpdateApiKeyRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKey:
        """
        Updates an existing API key's label and scopes

        Parameters
        ----------
        account_id : str
            Account ID

        key_id : str
            API Key ID

        request : UpdateApiKeyRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            API key updated successfully

        Examples
        --------
        from fern import FernApi, UpdateApiKeyRequestLabel

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.api_keys.update_api_key(
            account_id="account_id",
            key_id="key_id",
            request=UpdateApiKeyRequestLabel(
                label="label",
            ),
        )
        """
        _response = self._raw_client.update_api_key(
            account_id, key_id, request=request, request_options=request_options
        )
        return _response.data

    def delete_api_key(
        self, account_id: str, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Deletes an API key

        Parameters
        ----------
        account_id : str
            Account ID

        key_id : str
            API Key ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            API key deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.api_keys.delete_api_key(
            account_id="account_id",
            key_id="key_id",
        )
        """
        _response = self._raw_client.delete_api_key(account_id, key_id, request_options=request_options)
        return _response.data


class AsyncApiKeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApiKeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApiKeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApiKeysClient
        """
        return self._raw_client

    async def get_api_keys(
        self,
        account_id: str,
        *,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedApiKeysResponse:
        """
        Returns a list of API keys for the account

        Parameters
        ----------
        account_id : str
            Account ID

        limit : typing.Optional[int]
            Maximum number of items to return

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedApiKeysResponse
            List of API keys

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.api_keys.get_api_keys(
                account_id="account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_keys(
            account_id, limit=limit, after=after, before=before, request_options=request_options
        )
        return _response.data

    async def create_api_key(
        self,
        account_id: str,
        *,
        label: str,
        scopes: typing.Sequence[str],
        idempotency_key: typing.Optional[str] = None,
        ip_allow_list: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateApiKeyResponse:
        """
        Creates a new API key with the specified scopes

        Parameters
        ----------
        account_id : str
            Account ID

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
        CreateApiKeyResponse
            API key created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.api_keys.create_api_key(
                account_id="account_id",
                idempotency_key="user-12345-create-domain-20240101",
                label="Production API Key",
                scopes=["messages:send:all", "domains:read"],
                ip_allow_list=["203.0.113.0/24", "198.51.100.7"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_api_key(
            account_id,
            label=label,
            scopes=scopes,
            idempotency_key=idempotency_key,
            ip_allow_list=ip_allow_list,
            request_options=request_options,
        )
        return _response.data

    async def get_api_key(
        self, account_id: str, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKey:
        """
        Returns a specific API key by ID

        Parameters
        ----------
        account_id : str
            Account ID

        key_id : str
            API Key ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            API key details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.api_keys.get_api_key(
                account_id="account_id",
                key_id="key_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_key(account_id, key_id, request_options=request_options)
        return _response.data

    async def update_api_key(
        self,
        account_id: str,
        key_id: str,
        *,
        request: UpdateApiKeyRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiKey:
        """
        Updates an existing API key's label and scopes

        Parameters
        ----------
        account_id : str
            Account ID

        key_id : str
            API Key ID

        request : UpdateApiKeyRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKey
            API key updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, UpdateApiKeyRequestLabel

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.api_keys.update_api_key(
                account_id="account_id",
                key_id="key_id",
                request=UpdateApiKeyRequestLabel(
                    label="label",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_api_key(
            account_id, key_id, request=request, request_options=request_options
        )
        return _response.data

    async def delete_api_key(
        self, account_id: str, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Deletes an API key

        Parameters
        ----------
        account_id : str
            Account ID

        key_id : str
            API Key ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            API key deleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.api_keys.delete_api_key(
                account_id="account_id",
                key_id="key_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_key(account_id, key_id, request_options=request_options)
        return _response.data
