

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.introspection_request_token_type_hint import IntrospectionRequestTokenTypeHint
from ..types.introspection_response import IntrospectionResponse
from .raw_client import AsyncRawIntrospectionClient, RawIntrospectionClient


OMIT = typing.cast(typing.Any, ...)


class IntrospectionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIntrospectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIntrospectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIntrospectionClient
        """
        return self._raw_client

    def introspect_delegation_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[IntrospectionRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IntrospectionResponse:
        """
        MUST be called by the permission pipeline before any invocation of a tool whose
        `is_irreversible = True`, regardless of local cache state (FR-007).

        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[IntrospectionRequestTokenTypeHint]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IntrospectionResponse
            Introspection response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.introspection.introspect_delegation_token(
            token="token",
        )
        """
        _response = self._raw_client.introspect_delegation_token(
            token=token, token_type_hint=token_type_hint, request_options=request_options
        )
        return _response.data


class AsyncIntrospectionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIntrospectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIntrospectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIntrospectionClient
        """
        return self._raw_client

    async def introspect_delegation_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[IntrospectionRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IntrospectionResponse:
        """
        MUST be called by the permission pipeline before any invocation of a tool whose
        `is_irreversible = True`, regardless of local cache state (FR-007).

        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[IntrospectionRequestTokenTypeHint]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IntrospectionResponse
            Introspection response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.introspection.introspect_delegation_token(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.introspect_delegation_token(
            token=token, token_type_hint=token_type_hint, request_options=request_options
        )
        return _response.data
