

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.delegation_token import DelegationToken
from ..types.token_request_grant_type import TokenRequestGrantType
from .raw_client import AsyncRawTokenClient, RawTokenClient


OMIT = typing.cast(typing.Any, ...)


class TokenClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTokenClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTokenClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTokenClient
        """
        return self._raw_client

    def issue_delegation_token(
        self,
        *,
        grant_type: TokenRequestGrantType,
        code_verifier: str,
        device_code: typing.Optional[str] = OMIT,
        subject_token: typing.Optional[str] = OMIT,
        subject_token_type: typing.Optional[str] = OMIT,
        audience: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DelegationToken:
        """
        Issues a `DelegationToken` bound to a citizen authentication event.
        Supports two grant flows:
          - Device Authorization Grant per RFC 8628 (agent-first flows).
          - Token Exchange per RFC 8693 (ministry-to-ministry hand-off).
        PKCE per RFC 7636 is REQUIRED on all grant types. The issued token is a JWT
        per RFC 9068 with `aal_asserted` claim carrying NIST SP 800-63-4 AAL.

        Parameters
        ----------
        grant_type : TokenRequestGrantType
            Device grant (RFC 8628) or token exchange (RFC 8693).

        code_verifier : str
            PKCE code verifier (RFC 7636).

        device_code : typing.Optional[str]

        subject_token : typing.Optional[str]

        subject_token_type : typing.Optional[str]

        audience : typing.Optional[str]

        scope : typing.Optional[str]
            Space-separated scope string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DelegationToken
            Token issued.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.token.issue_delegation_token(
            grant_type="urn:ietf:params:oauth:grant-type:device_code",
            code_verifier="code_verifier",
        )
        """
        _response = self._raw_client.issue_delegation_token(
            grant_type=grant_type,
            code_verifier=code_verifier,
            device_code=device_code,
            subject_token=subject_token,
            subject_token_type=subject_token_type,
            audience=audience,
            scope=scope,
            request_options=request_options,
        )
        return _response.data


class AsyncTokenClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTokenClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTokenClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTokenClient
        """
        return self._raw_client

    async def issue_delegation_token(
        self,
        *,
        grant_type: TokenRequestGrantType,
        code_verifier: str,
        device_code: typing.Optional[str] = OMIT,
        subject_token: typing.Optional[str] = OMIT,
        subject_token_type: typing.Optional[str] = OMIT,
        audience: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DelegationToken:
        """
        Issues a `DelegationToken` bound to a citizen authentication event.
        Supports two grant flows:
          - Device Authorization Grant per RFC 8628 (agent-first flows).
          - Token Exchange per RFC 8693 (ministry-to-ministry hand-off).
        PKCE per RFC 7636 is REQUIRED on all grant types. The issued token is a JWT
        per RFC 9068 with `aal_asserted` claim carrying NIST SP 800-63-4 AAL.

        Parameters
        ----------
        grant_type : TokenRequestGrantType
            Device grant (RFC 8628) or token exchange (RFC 8693).

        code_verifier : str
            PKCE code verifier (RFC 7636).

        device_code : typing.Optional[str]

        subject_token : typing.Optional[str]

        subject_token_type : typing.Optional[str]

        audience : typing.Optional[str]

        scope : typing.Optional[str]
            Space-separated scope string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DelegationToken
            Token issued.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.token.issue_delegation_token(
                grant_type="urn:ietf:params:oauth:grant-type:device_code",
                code_verifier="code_verifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.issue_delegation_token(
            grant_type=grant_type,
            code_verifier=code_verifier,
            device_code=device_code,
            subject_token=subject_token,
            subject_token_type=subject_token_type,
            audience=audience,
            scope=scope,
            request_options=request_options,
        )
        return _response.data
