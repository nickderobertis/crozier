

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_suppression_response import CreateSuppressionResponse
from ..types.paginated_suppressions_response import PaginatedSuppressionsResponse
from ..types.success_response import SuccessResponse
from .raw_client import AsyncRawSuppressionsClient, RawSuppressionsClient


OMIT = typing.cast(typing.Any, ...)


class SuppressionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSuppressionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSuppressionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSuppressionsClient
        """
        return self._raw_client

    def get_suppressions(
        self,
        account_id: str,
        *,
        domain: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        from_time: typing.Optional[dt.datetime] = None,
        to_time: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedSuppressionsResponse:
        """
        Returns a list of suppressions for the account

        **Query Parameters:**
        - `domain`: Filter by domain (optional)
        - `email`: Filter by email (optional)
        - `from_time`: Filter suppressions created after this time (RFC3339 format, optional)
        - `to_time`: Filter suppressions created before this time (RFC3339 format, optional)
        - `limit`: Maximum number of items to return (1-100, default: 100)
        - `after`: Pagination cursor for the next page
        - `before`: Pagination cursor for the previous page

        Parameters
        ----------
        account_id : str
            Account ID

        domain : typing.Optional[str]
            Filter by domain

        email : typing.Optional[str]
            Email address

        from_time : typing.Optional[dt.datetime]
            Filter suppressions created after this time (RFC3339 format)

        to_time : typing.Optional[dt.datetime]
            Filter suppressions created before this time (RFC3339 format)

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page. Provide the value provided in `previous_cursor` from the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedSuppressionsResponse
            List of suppressions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.suppressions.get_suppressions(
            account_id="account_id",
        )
        """
        _response = self._raw_client.get_suppressions(
            account_id,
            domain=domain,
            email=email,
            from_time=from_time,
            to_time=to_time,
            limit=limit,
            after=after,
            before=before,
            request_options=request_options,
        )
        return _response.data

    def create_suppression(
        self,
        account_id: str,
        *,
        email: str,
        expires_at: dt.datetime,
        idempotency_key: typing.Optional[str] = None,
        domain: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSuppressionResponse:
        """
        Creates a new suppression for an email address

        **Validation Requirements:**
        - `email` must be a valid email address
        - `expires_at` must be in RFC3339 format
        - `domain` is optional - if not provided, applies to all account domains

        Parameters
        ----------
        account_id : str
            Account ID

        email : str
            Email address to suppress

        expires_at : dt.datetime
            When the suppression expires (RFC3339 format)

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        domain : typing.Optional[str]
            Domain for which to suppress the email

        reason : typing.Optional[str]
            Reason for suppression

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSuppressionResponse
            Suppression created successfully

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.suppressions.create_suppression(
            account_id="account_id",
            idempotency_key="user-12345-create-domain-20240101",
            email="user@example.com",
            domain="example.com",
            reason="User requested removal",
            expires_at=datetime.datetime.fromisoformat(
                "2024-12-25 10:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.create_suppression(
            account_id,
            email=email,
            expires_at=expires_at,
            idempotency_key=idempotency_key,
            domain=domain,
            reason=reason,
            request_options=request_options,
        )
        return _response.data

    def delete_suppression(
        self,
        account_id: str,
        *,
        email: str,
        domain: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
        """
        Deletes suppressions for an email address

        **Query Parameters:**
        - `email`: Required email address to delete from suppression list
        - `domain`: Optional domain filter to delete suppressions for specific domain only

        Parameters
        ----------
        account_id : str
            Account ID

        email : str
            Email address

        domain : typing.Optional[str]
            Optional domain filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Suppression deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.suppressions.delete_suppression(
            account_id="account_id",
            email="email",
        )
        """
        _response = self._raw_client.delete_suppression(
            account_id, email=email, domain=domain, request_options=request_options
        )
        return _response.data

    def delete_all_suppressions(
        self,
        account_id: str,
        *,
        domain: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
        """
        Deletes all suppressions for the account

        **Query Parameters:**
        - `domain`: Optional domain filter to delete suppressions for specific domain only

        Parameters
        ----------
        account_id : str
            Account ID

        domain : typing.Optional[str]
            Optional domain filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            All suppressions deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.suppressions.delete_all_suppressions(
            account_id="account_id",
        )
        """
        _response = self._raw_client.delete_all_suppressions(account_id, domain=domain, request_options=request_options)
        return _response.data


class AsyncSuppressionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSuppressionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSuppressionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSuppressionsClient
        """
        return self._raw_client

    async def get_suppressions(
        self,
        account_id: str,
        *,
        domain: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        from_time: typing.Optional[dt.datetime] = None,
        to_time: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedSuppressionsResponse:
        """
        Returns a list of suppressions for the account

        **Query Parameters:**
        - `domain`: Filter by domain (optional)
        - `email`: Filter by email (optional)
        - `from_time`: Filter suppressions created after this time (RFC3339 format, optional)
        - `to_time`: Filter suppressions created before this time (RFC3339 format, optional)
        - `limit`: Maximum number of items to return (1-100, default: 100)
        - `after`: Pagination cursor for the next page
        - `before`: Pagination cursor for the previous page

        Parameters
        ----------
        account_id : str
            Account ID

        domain : typing.Optional[str]
            Filter by domain

        email : typing.Optional[str]
            Email address

        from_time : typing.Optional[dt.datetime]
            Filter suppressions created after this time (RFC3339 format)

        to_time : typing.Optional[dt.datetime]
            Filter suppressions created before this time (RFC3339 format)

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page. Provide the value provided in `previous_cursor` from the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedSuppressionsResponse
            List of suppressions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.suppressions.get_suppressions(
                account_id="account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_suppressions(
            account_id,
            domain=domain,
            email=email,
            from_time=from_time,
            to_time=to_time,
            limit=limit,
            after=after,
            before=before,
            request_options=request_options,
        )
        return _response.data

    async def create_suppression(
        self,
        account_id: str,
        *,
        email: str,
        expires_at: dt.datetime,
        idempotency_key: typing.Optional[str] = None,
        domain: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSuppressionResponse:
        """
        Creates a new suppression for an email address

        **Validation Requirements:**
        - `email` must be a valid email address
        - `expires_at` must be in RFC3339 format
        - `domain` is optional - if not provided, applies to all account domains

        Parameters
        ----------
        account_id : str
            Account ID

        email : str
            Email address to suppress

        expires_at : dt.datetime
            When the suppression expires (RFC3339 format)

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        domain : typing.Optional[str]
            Domain for which to suppress the email

        reason : typing.Optional[str]
            Reason for suppression

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSuppressionResponse
            Suppression created successfully

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.suppressions.create_suppression(
                account_id="account_id",
                idempotency_key="user-12345-create-domain-20240101",
                email="user@example.com",
                domain="example.com",
                reason="User requested removal",
                expires_at=datetime.datetime.fromisoformat(
                    "2024-12-25 10:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_suppression(
            account_id,
            email=email,
            expires_at=expires_at,
            idempotency_key=idempotency_key,
            domain=domain,
            reason=reason,
            request_options=request_options,
        )
        return _response.data

    async def delete_suppression(
        self,
        account_id: str,
        *,
        email: str,
        domain: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
        """
        Deletes suppressions for an email address

        **Query Parameters:**
        - `email`: Required email address to delete from suppression list
        - `domain`: Optional domain filter to delete suppressions for specific domain only

        Parameters
        ----------
        account_id : str
            Account ID

        email : str
            Email address

        domain : typing.Optional[str]
            Optional domain filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Suppression deleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.suppressions.delete_suppression(
                account_id="account_id",
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_suppression(
            account_id, email=email, domain=domain, request_options=request_options
        )
        return _response.data

    async def delete_all_suppressions(
        self,
        account_id: str,
        *,
        domain: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuccessResponse:
        """
        Deletes all suppressions for the account

        **Query Parameters:**
        - `domain`: Optional domain filter to delete suppressions for specific domain only

        Parameters
        ----------
        account_id : str
            Account ID

        domain : typing.Optional[str]
            Optional domain filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            All suppressions deleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.suppressions.delete_all_suppressions(
                account_id="account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_all_suppressions(
            account_id, domain=domain, request_options=request_options
        )
        return _response.data
