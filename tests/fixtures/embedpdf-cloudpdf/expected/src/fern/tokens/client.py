

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tokens_issue200response import TokensIssue200Response
from ..types.tokens_issue_request import TokensIssueRequest
from .raw_client import AsyncRawTokensClient, RawTokensClient


OMIT = typing.cast(typing.Any, ...)


class TokensClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTokensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTokensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTokensClient
        """
        return self._raw_client

    def issue(
        self, tenant_id: str, *, request: TokensIssueRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> TokensIssue200Response:
        """
        kind "tenant" requires the API token — authority mints only downward. Mounted only when the deployment can sign (HS256 mode); asymmetric deployments mint with their own private key.

        Parameters
        ----------
        tenant_id : str

        request : TokensIssueRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokensIssue200Response
            OK

        Examples
        --------
        from fern import FernApi, TokensIssueRequest_Doc

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tokens.issue(
            tenant_id="tenantId",
            request=TokensIssueRequest_Doc(
                sub="sub",
                doc_id="docId",
                scope=["scope"],
                expires_in=1,
            ),
        )
        """
        _response = self._raw_client.issue(tenant_id, request=request, request_options=request_options)
        return _response.data

    def revoke(
        self,
        tenant_id: str,
        jti: str,
        *,
        reason: typing.Optional[str] = OMIT,
        expires_at_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Mounted only when the deployment enables token revocation.

        Parameters
        ----------
        tenant_id : str

        jti : str

        reason : typing.Optional[str]

        expires_at_seconds : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tokens.revoke(
            tenant_id="tenantId",
            jti="jti",
        )
        """
        _response = self._raw_client.revoke(
            tenant_id, jti, reason=reason, expires_at_seconds=expires_at_seconds, request_options=request_options
        )
        return _response.data


class AsyncTokensClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTokensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTokensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTokensClient
        """
        return self._raw_client

    async def issue(
        self, tenant_id: str, *, request: TokensIssueRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> TokensIssue200Response:
        """
        kind "tenant" requires the API token — authority mints only downward. Mounted only when the deployment can sign (HS256 mode); asymmetric deployments mint with their own private key.

        Parameters
        ----------
        tenant_id : str

        request : TokensIssueRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokensIssue200Response
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TokensIssueRequest_Doc

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tokens.issue(
                tenant_id="tenantId",
                request=TokensIssueRequest_Doc(
                    sub="sub",
                    doc_id="docId",
                    scope=["scope"],
                    expires_in=1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.issue(tenant_id, request=request, request_options=request_options)
        return _response.data

    async def revoke(
        self,
        tenant_id: str,
        jti: str,
        *,
        reason: typing.Optional[str] = OMIT,
        expires_at_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Mounted only when the deployment enables token revocation.

        Parameters
        ----------
        tenant_id : str

        jti : str

        reason : typing.Optional[str]

        expires_at_seconds : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tokens.revoke(
                tenant_id="tenantId",
                jti="jti",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke(
            tenant_id, jti, reason=reason, expires_at_seconds=expires_at_seconds, request_options=request_options
        )
        return _response.data
