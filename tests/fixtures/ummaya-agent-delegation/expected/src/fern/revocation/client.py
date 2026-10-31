

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.revocation_request_token_type_hint import RevocationRequestTokenTypeHint
from .raw_client import AsyncRawRevocationClient, RawRevocationClient


OMIT = typing.cast(typing.Any, ...)


class RevocationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRevocationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRevocationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRevocationClient
        """
        return self._raw_client

    def revoke_delegation_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[RevocationRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Revokes a token immediately. The spec declares a maximum propagation window
        (documented in the normative spec, not this skeleton) after which all downstream
        caches MUST reject the token.

        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[RevocationRequestTokenTypeHint]

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
        )
        client.revocation.revoke_delegation_token(
            token="token",
        )
        """
        _response = self._raw_client.revoke_delegation_token(
            token=token, token_type_hint=token_type_hint, request_options=request_options
        )
        return _response.data


class AsyncRevocationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRevocationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRevocationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRevocationClient
        """
        return self._raw_client

    async def revoke_delegation_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[RevocationRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Revokes a token immediately. The spec declares a maximum propagation window
        (documented in the normative spec, not this skeleton) after which all downstream
        caches MUST reject the token.

        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[RevocationRequestTokenTypeHint]

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
        )


        async def main() -> None:
            await client.revocation.revoke_delegation_token(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_delegation_token(
            token=token, token_type_hint=token_type_hint, request_options=request_options
        )
        return _response.data
