

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawN1N2IndividualSubscriptionDocumentClient, RawN1N2IndividualSubscriptionDocumentClient


class N1N2IndividualSubscriptionDocumentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawN1N2IndividualSubscriptionDocumentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawN1N2IndividualSubscriptionDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawN1N2IndividualSubscriptionDocumentClient
        """
        return self._raw_client

    def n1n2message_un_subscribe(
        self, ue_context_id: str, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        subscription_id : str
            Subscription Identifier

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
        client.n1n2individual_subscription_document.n1n2message_un_subscribe(
            ue_context_id="ueContextId",
            subscription_id="subscriptionId",
        )
        """
        _response = self._raw_client.n1n2message_un_subscribe(
            ue_context_id, subscription_id, request_options=request_options
        )
        return _response.data


class AsyncN1N2IndividualSubscriptionDocumentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawN1N2IndividualSubscriptionDocumentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawN1N2IndividualSubscriptionDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawN1N2IndividualSubscriptionDocumentClient
        """
        return self._raw_client

    async def n1n2message_un_subscribe(
        self, ue_context_id: str, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        subscription_id : str
            Subscription Identifier

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
            await client.n1n2individual_subscription_document.n1n2message_un_subscribe(
                ue_context_id="ueContextId",
                subscription_id="subscriptionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.n1n2message_un_subscribe(
            ue_context_id, subscription_id, request_options=request_options
        )
        return _response.data
