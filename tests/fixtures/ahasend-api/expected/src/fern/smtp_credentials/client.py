

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.created_smtp_credential import CreatedSmtpCredential
from ..types.paginated_smtp_credentials_response import PaginatedSmtpCredentialsResponse
from ..types.smtp_credential import SmtpCredential
from ..types.success_response import SuccessResponse
from .raw_client import AsyncRawSmtpCredentialsClient, RawSmtpCredentialsClient
from .types.create_smtp_credential_request_scope import CreateSmtpCredentialRequestScope


OMIT = typing.cast(typing.Any, ...)


class SmtpCredentialsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSmtpCredentialsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSmtpCredentialsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSmtpCredentialsClient
        """
        return self._raw_client

    def get_smtp_credentials(
        self,
        account_id: str,
        *,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedSmtpCredentialsResponse:
        """
        Returns a list of SMTP credentials for the account. The global read role
        sees all credentials; domain-scoped roles return credentials associated
        with at least one authorized domain.

        Parameters
        ----------
        account_id : str
            Account ID

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedSmtpCredentialsResponse
            List of SMTP credentials

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.smtp_credentials.get_smtp_credentials(
            account_id="account_id",
        )
        """
        _response = self._raw_client.get_smtp_credentials(
            account_id, limit=limit, after=after, before=before, request_options=request_options
        )
        return _response.data

    def create_smtp_credential(
        self,
        account_id: str,
        *,
        name: str,
        scope: CreateSmtpCredentialRequestScope,
        idempotency_key: typing.Optional[str] = None,
        sandbox: typing.Optional[bool] = OMIT,
        domains: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatedSmtpCredential:
        """
        Creates a new SMTP credential for SMTP authentication. A `scoped`
        credential requires at least one domain and the key must have write
        permission for every supplied domain. A `global` credential requires
        `smtp-credentials:write:all`; supplied domains are accepted but ignored,
        and the response contains `domains: []`. SMTP credentials have no
        update endpoint.

        Parameters
        ----------
        account_id : str
            Account ID

        name : str
            Credential name

        scope : CreateSmtpCredentialRequestScope
            Credential scope - "global" or "scoped"

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        sandbox : typing.Optional[bool]
            Whether this is a sandbox credential

        domains : typing.Optional[typing.Sequence[str]]
            For `scoped`, a non-empty array is required. For `global`, this may
            be omitted, null, empty, or non-empty; supplied values are accepted
            but ignored.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatedSmtpCredential
            SMTP credential created successfully

        Examples
        --------
        from fern.smtp_credentials import CreateSmtpCredentialRequestScope

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.smtp_credentials.create_smtp_credential(
            account_id="account_id",
            idempotency_key="user-12345-create-domain-20240101",
            name="Production SMTP",
            scope=CreateSmtpCredentialRequestScope.GLOBAL,
        )
        """
        _response = self._raw_client.create_smtp_credential(
            account_id,
            name=name,
            scope=scope,
            idempotency_key=idempotency_key,
            sandbox=sandbox,
            domains=domains,
            request_options=request_options,
        )
        return _response.data

    def get_smtp_credential(
        self, account_id: str, smtp_credential_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SmtpCredential:
        """
        Returns a specific SMTP credential by ID. Access requires the global
        read role or a read role matching at least one associated domain.

        Parameters
        ----------
        account_id : str
            Account ID

        smtp_credential_id : str
            SMTP Credential ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SmtpCredential
            SMTP credential details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.smtp_credentials.get_smtp_credential(
            account_id="account_id",
            smtp_credential_id="smtp_credential_id",
        )
        """
        _response = self._raw_client.get_smtp_credential(
            account_id, smtp_credential_id, request_options=request_options
        )
        return _response.data

    def delete_smtp_credential(
        self, account_id: str, smtp_credential_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Deletes an SMTP credential. Access requires the global delete role or a
        delete role matching at least one associated domain.

        Parameters
        ----------
        account_id : str
            Account ID

        smtp_credential_id : str
            SMTP Credential ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            SMTP credential deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.smtp_credentials.delete_smtp_credential(
            account_id="account_id",
            smtp_credential_id="smtp_credential_id",
        )
        """
        _response = self._raw_client.delete_smtp_credential(
            account_id, smtp_credential_id, request_options=request_options
        )
        return _response.data


class AsyncSmtpCredentialsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSmtpCredentialsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSmtpCredentialsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSmtpCredentialsClient
        """
        return self._raw_client

    async def get_smtp_credentials(
        self,
        account_id: str,
        *,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedSmtpCredentialsResponse:
        """
        Returns a list of SMTP credentials for the account. The global read role
        sees all credentials; domain-scoped roles return credentials associated
        with at least one authorized domain.

        Parameters
        ----------
        account_id : str
            Account ID

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedSmtpCredentialsResponse
            List of SMTP credentials

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.smtp_credentials.get_smtp_credentials(
                account_id="account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_smtp_credentials(
            account_id, limit=limit, after=after, before=before, request_options=request_options
        )
        return _response.data

    async def create_smtp_credential(
        self,
        account_id: str,
        *,
        name: str,
        scope: CreateSmtpCredentialRequestScope,
        idempotency_key: typing.Optional[str] = None,
        sandbox: typing.Optional[bool] = OMIT,
        domains: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatedSmtpCredential:
        """
        Creates a new SMTP credential for SMTP authentication. A `scoped`
        credential requires at least one domain and the key must have write
        permission for every supplied domain. A `global` credential requires
        `smtp-credentials:write:all`; supplied domains are accepted but ignored,
        and the response contains `domains: []`. SMTP credentials have no
        update endpoint.

        Parameters
        ----------
        account_id : str
            Account ID

        name : str
            Credential name

        scope : CreateSmtpCredentialRequestScope
            Credential scope - "global" or "scoped"

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        sandbox : typing.Optional[bool]
            Whether this is a sandbox credential

        domains : typing.Optional[typing.Sequence[str]]
            For `scoped`, a non-empty array is required. For `global`, this may
            be omitted, null, empty, or non-empty; supplied values are accepted
            but ignored.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatedSmtpCredential
            SMTP credential created successfully

        Examples
        --------
        import asyncio

        from fern.smtp_credentials import CreateSmtpCredentialRequestScope

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.smtp_credentials.create_smtp_credential(
                account_id="account_id",
                idempotency_key="user-12345-create-domain-20240101",
                name="Production SMTP",
                scope=CreateSmtpCredentialRequestScope.GLOBAL,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_smtp_credential(
            account_id,
            name=name,
            scope=scope,
            idempotency_key=idempotency_key,
            sandbox=sandbox,
            domains=domains,
            request_options=request_options,
        )
        return _response.data

    async def get_smtp_credential(
        self, account_id: str, smtp_credential_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SmtpCredential:
        """
        Returns a specific SMTP credential by ID. Access requires the global
        read role or a read role matching at least one associated domain.

        Parameters
        ----------
        account_id : str
            Account ID

        smtp_credential_id : str
            SMTP Credential ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SmtpCredential
            SMTP credential details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.smtp_credentials.get_smtp_credential(
                account_id="account_id",
                smtp_credential_id="smtp_credential_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_smtp_credential(
            account_id, smtp_credential_id, request_options=request_options
        )
        return _response.data

    async def delete_smtp_credential(
        self, account_id: str, smtp_credential_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Deletes an SMTP credential. Access requires the global delete role or a
        delete role matching at least one associated domain.

        Parameters
        ----------
        account_id : str
            Account ID

        smtp_credential_id : str
            SMTP Credential ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            SMTP credential deleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.smtp_credentials.delete_smtp_credential(
                account_id="account_id",
                smtp_credential_id="smtp_credential_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_smtp_credential(
            account_id, smtp_credential_id, request_options=request_options
        )
        return _response.data
