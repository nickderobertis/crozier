

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import (
    AsyncRawNonUeN2MessageNotificationIndividualSubscriptionDocumentClient,
    RawNonUeN2MessageNotificationIndividualSubscriptionDocumentClient,
)


class NonUeN2MessageNotificationIndividualSubscriptionDocumentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNonUeN2MessageNotificationIndividualSubscriptionDocumentClient(
            client_wrapper=client_wrapper
        )

    @property
    def with_raw_response(self) -> RawNonUeN2MessageNotificationIndividualSubscriptionDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNonUeN2MessageNotificationIndividualSubscriptionDocumentClient
        """
        return self._raw_client

    def non_ue_n2info_un_subscribe(
        self, n2notify_subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        n2notify_subscription_id : str
            N2 info Subscription Identifier

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
        client.non_ue_n2message_notification_individual_subscription_document.non_ue_n2info_un_subscribe(
            n2notify_subscription_id="n2NotifySubscriptionId",
        )
        """
        _response = self._raw_client.non_ue_n2info_un_subscribe(
            n2notify_subscription_id, request_options=request_options
        )
        return _response.data


class AsyncNonUeN2MessageNotificationIndividualSubscriptionDocumentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNonUeN2MessageNotificationIndividualSubscriptionDocumentClient(
            client_wrapper=client_wrapper
        )

    @property
    def with_raw_response(self) -> AsyncRawNonUeN2MessageNotificationIndividualSubscriptionDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNonUeN2MessageNotificationIndividualSubscriptionDocumentClient
        """
        return self._raw_client

    async def non_ue_n2info_un_subscribe(
        self, n2notify_subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        n2notify_subscription_id : str
            N2 info Subscription Identifier

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
            await client.non_ue_n2message_notification_individual_subscription_document.non_ue_n2info_un_subscribe(
                n2notify_subscription_id="n2NotifySubscriptionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.non_ue_n2info_un_subscribe(
            n2notify_subscription_id, request_options=request_options
        )
        return _response.data
