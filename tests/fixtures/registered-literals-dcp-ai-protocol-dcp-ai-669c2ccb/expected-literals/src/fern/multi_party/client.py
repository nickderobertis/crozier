

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMultiPartyClient, RawMultiPartyClient
from .types.multi_party_authorize_request_authorization import MultiPartyAuthorizeRequestAuthorization
from .types.multi_party_authorize_response import MultiPartyAuthorizeResponse


OMIT = typing.cast(typing.Any, ...)


class MultiPartyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMultiPartyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMultiPartyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMultiPartyClient
        """
        return self._raw_client

    def multi_party_authorize(
        self,
        *,
        authorization: MultiPartyAuthorizeRequestAuthorization,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MultiPartyAuthorizeResponse:
        """
        Validates a multi-party authorization request. Requires at least the
        threshold number of authorizations including an owner signature.

        Parameters
        ----------
        authorization : MultiPartyAuthorizeRequestAuthorization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MultiPartyAuthorizeResponse
            Authorization verified

        Examples
        --------
        from fern.multi_party import (
            MultiPartyAuthorizeRequestAuthorization,
            MultiPartyAuthorizeRequestAuthorizationAuthorizationsItem,
        )

        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.multi_party.multi_party_authorize(
            authorization=MultiPartyAuthorizeRequestAuthorization(
                type="multi_party_authorization",
                operation="revoke_agent",
                authorizations=[
                    MultiPartyAuthorizeRequestAuthorizationAuthorizationsItem()
                ],
            ),
        )
        """
        _response = self._raw_client.multi_party_authorize(authorization=authorization, request_options=request_options)
        return _response.data


class AsyncMultiPartyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMultiPartyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMultiPartyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMultiPartyClient
        """
        return self._raw_client

    async def multi_party_authorize(
        self,
        *,
        authorization: MultiPartyAuthorizeRequestAuthorization,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MultiPartyAuthorizeResponse:
        """
        Validates a multi-party authorization request. Requires at least the
        threshold number of authorizations including an owner signature.

        Parameters
        ----------
        authorization : MultiPartyAuthorizeRequestAuthorization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MultiPartyAuthorizeResponse
            Authorization verified

        Examples
        --------
        import asyncio

        from fern.multi_party import (
            MultiPartyAuthorizeRequestAuthorization,
            MultiPartyAuthorizeRequestAuthorizationAuthorizationsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.multi_party.multi_party_authorize(
                authorization=MultiPartyAuthorizeRequestAuthorization(
                    type="multi_party_authorization",
                    operation="revoke_agent",
                    authorizations=[
                        MultiPartyAuthorizeRequestAuthorizationAuthorizationsItem()
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.multi_party_authorize(
            authorization=authorization, request_options=request_options
        )
        return _response.data
