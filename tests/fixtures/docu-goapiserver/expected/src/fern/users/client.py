

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user import User
from .raw_client import AsyncRawUsersClient, RawUsersClient


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsersClient
        """
        return self._raw_client

    def get_users_v3(
        self,
        *,
        company_id: str,
        email: typing.Optional[str] = None,
        updated_after: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[User]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Without email, returns users sorted by updated_at and optionally filters to updated_at strictly after updated_after. When email is supplied, returns zero or one matching user in an array; updated_after is ignored and not validated in that branch.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        email : typing.Optional[str]
            Exact email lookup; takes precedence over updated_after.

        updated_after : typing.Optional[dt.datetime]
            Only users whose non-null updated_at is strictly later than this RFC3339 timestamp; applies only without email.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[User]
            Successful response.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_users_v3(
            company_id="11111111-1111-4111-8111-111111111111",
            email="user@example.com",
            updated_after=datetime.datetime.fromisoformat(
                "2026-01-01 00:00:00+00:00",
            ),
        )
        """
        _response = self._raw_client.get_users_v3(
            company_id=company_id, email=email, updated_after=updated_after, request_options=request_options
        )
        return _response.data

    def get_users_id_v3(
        self, id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns 404 when the user does not exist for the company.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_users_id_v3(
            id="id",
            company_id="11111111-1111-4111-8111-111111111111",
        )
        """
        _response = self._raw_client.get_users_id_v3(id, company_id=company_id, request_options=request_options)
        return _response.data


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsersClient
        """
        return self._raw_client

    async def get_users_v3(
        self,
        *,
        company_id: str,
        email: typing.Optional[str] = None,
        updated_after: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[User]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Without email, returns users sorted by updated_at and optionally filters to updated_at strictly after updated_after. When email is supplied, returns zero or one matching user in an array; updated_after is ignored and not validated in that branch.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        email : typing.Optional[str]
            Exact email lookup; takes precedence over updated_after.

        updated_after : typing.Optional[dt.datetime]
            Only users whose non-null updated_at is strictly later than this RFC3339 timestamp; applies only without email.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[User]
            Successful response.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_users_v3(
                company_id="11111111-1111-4111-8111-111111111111",
                email="user@example.com",
                updated_after=datetime.datetime.fromisoformat(
                    "2026-01-01 00:00:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_v3(
            company_id=company_id, email=email, updated_after=updated_after, request_options=request_options
        )
        return _response.data

    async def get_users_id_v3(
        self, id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns 404 when the user does not exist for the company.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_users_id_v3(
                id="id",
                company_id="11111111-1111-4111-8111-111111111111",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_id_v3(id, company_id=company_id, request_options=request_options)
        return _response.data
