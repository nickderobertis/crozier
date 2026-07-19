

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.n1message_class import N1MessageClass
from ..types.n2information_class import N2InformationClass
from ..types.ue_n1n2info_subscription_created_data import UeN1N2InfoSubscriptionCreatedData
from .raw_client import (
    AsyncRawN1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient,
    RawN1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient,
)


OMIT = typing.cast(typing.Any, ...)


class N1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawN1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient(
            client_wrapper=client_wrapper
        )

    @property
    def with_raw_response(self) -> RawN1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawN1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient
        """
        return self._raw_client

    def n1n2message_subscribe(
        self,
        ue_context_id: str,
        *,
        n2information_class: typing.Optional[N2InformationClass] = OMIT,
        n2notify_callback_uri: typing.Optional[str] = OMIT,
        n1message_class: typing.Optional[N1MessageClass] = OMIT,
        n1notify_callback_uri: typing.Optional[str] = OMIT,
        nf_id: typing.Optional[str] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UeN1N2InfoSubscriptionCreatedData:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        n2information_class : typing.Optional[N2InformationClass]

        n2notify_callback_uri : typing.Optional[str]

        n1message_class : typing.Optional[N1MessageClass]

        n1notify_callback_uri : typing.Optional[str]

        nf_id : typing.Optional[str]

        supported_features : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UeN1N2InfoSubscriptionCreatedData
            N1N2 Message Subscription successfully created.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.n1n2subscriptions_collection_for_individual_ue_contexts_document.n1n2message_subscribe(
            ue_context_id="ueContextId",
            n2notify_callback_uri="n2NotifyCallbackUri",
            n1notify_callback_uri="n1NotifyCallbackUri",
            nf_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
            supported_features="supportedFeatures",
        )
        """
        _response = self._raw_client.n1n2message_subscribe(
            ue_context_id,
            n2information_class=n2information_class,
            n2notify_callback_uri=n2notify_callback_uri,
            n1message_class=n1message_class,
            n1notify_callback_uri=n1notify_callback_uri,
            nf_id=nf_id,
            supported_features=supported_features,
            request_options=request_options,
        )
        return _response.data


class AsyncN1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawN1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient(
            client_wrapper=client_wrapper
        )

    @property
    def with_raw_response(self) -> AsyncRawN1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawN1N2SubscriptionsCollectionForIndividualUeContextsDocumentClient
        """
        return self._raw_client

    async def n1n2message_subscribe(
        self,
        ue_context_id: str,
        *,
        n2information_class: typing.Optional[N2InformationClass] = OMIT,
        n2notify_callback_uri: typing.Optional[str] = OMIT,
        n1message_class: typing.Optional[N1MessageClass] = OMIT,
        n1notify_callback_uri: typing.Optional[str] = OMIT,
        nf_id: typing.Optional[str] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UeN1N2InfoSubscriptionCreatedData:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        n2information_class : typing.Optional[N2InformationClass]

        n2notify_callback_uri : typing.Optional[str]

        n1message_class : typing.Optional[N1MessageClass]

        n1notify_callback_uri : typing.Optional[str]

        nf_id : typing.Optional[str]

        supported_features : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UeN1N2InfoSubscriptionCreatedData
            N1N2 Message Subscription successfully created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.n1n2subscriptions_collection_for_individual_ue_contexts_document.n1n2message_subscribe(
                ue_context_id="ueContextId",
                n2notify_callback_uri="n2NotifyCallbackUri",
                n1notify_callback_uri="n1NotifyCallbackUri",
                nf_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
                supported_features="supportedFeatures",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.n1n2message_subscribe(
            ue_context_id,
            n2information_class=n2information_class,
            n2notify_callback_uri=n2notify_callback_uri,
            n1message_class=n1message_class,
            n1notify_callback_uri=n1notify_callback_uri,
            nf_id=nf_id,
            supported_features=supported_features,
            request_options=request_options,
        )
        return _response.data
