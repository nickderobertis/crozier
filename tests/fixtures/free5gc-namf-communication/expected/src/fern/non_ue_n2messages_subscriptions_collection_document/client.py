

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.access_type import AccessType
from ..types.global_ran_node_id import GlobalRanNodeId
from ..types.n2information_class import N2InformationClass
from ..types.non_ue_n2info_subscription_created_data import NonUeN2InfoSubscriptionCreatedData
from .raw_client import (
    AsyncRawNonUeN2MessagesSubscriptionsCollectionDocumentClient,
    RawNonUeN2MessagesSubscriptionsCollectionDocumentClient,
)


OMIT = typing.cast(typing.Any, ...)


class NonUeN2MessagesSubscriptionsCollectionDocumentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNonUeN2MessagesSubscriptionsCollectionDocumentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNonUeN2MessagesSubscriptionsCollectionDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNonUeN2MessagesSubscriptionsCollectionDocumentClient
        """
        return self._raw_client

    def non_ue_n2info_subscribe(
        self,
        *,
        n2information_class: N2InformationClass,
        n2notify_callback_uri: str,
        global_ran_node_list: typing.Optional[typing.Sequence[GlobalRanNodeId]] = OMIT,
        an_type_list: typing.Optional[typing.Sequence[AccessType]] = OMIT,
        nf_id: typing.Optional[str] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NonUeN2InfoSubscriptionCreatedData:
        """
        Parameters
        ----------
        n2information_class : N2InformationClass

        n2notify_callback_uri : str

        global_ran_node_list : typing.Optional[typing.Sequence[GlobalRanNodeId]]

        an_type_list : typing.Optional[typing.Sequence[AccessType]]

        nf_id : typing.Optional[str]

        supported_features : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NonUeN2InfoSubscriptionCreatedData
            Non UE N2 Info Subscription successfully created.

        Examples
        --------
        from fern import AccessType, FernApi, N2InformationClass

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.non_ue_n2messages_subscriptions_collection_document.non_ue_n2info_subscribe(
            global_ran_node_list=[
                {
                    "gNbId": {"bitLength": 24, "gNBValue": "gNBValue"},
                    "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                    "n3IwfId": "n3IwfId",
                    "ngeNbId": "ngeNbId",
                },
                {
                    "gNbId": {"bitLength": 24, "gNBValue": "gNBValue"},
                    "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                    "n3IwfId": "n3IwfId",
                    "ngeNbId": "ngeNbId",
                },
            ],
            an_type_list=[AccessType.THREE_GPP_ACCESS, AccessType.THREE_GPP_ACCESS],
            n2information_class=N2InformationClass.SM,
            n2notify_callback_uri="n2NotifyCallbackUri",
            nf_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
            supported_features="supportedFeatures",
        )
        """
        _response = self._raw_client.non_ue_n2info_subscribe(
            n2information_class=n2information_class,
            n2notify_callback_uri=n2notify_callback_uri,
            global_ran_node_list=global_ran_node_list,
            an_type_list=an_type_list,
            nf_id=nf_id,
            supported_features=supported_features,
            request_options=request_options,
        )
        return _response.data


class AsyncNonUeN2MessagesSubscriptionsCollectionDocumentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNonUeN2MessagesSubscriptionsCollectionDocumentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNonUeN2MessagesSubscriptionsCollectionDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNonUeN2MessagesSubscriptionsCollectionDocumentClient
        """
        return self._raw_client

    async def non_ue_n2info_subscribe(
        self,
        *,
        n2information_class: N2InformationClass,
        n2notify_callback_uri: str,
        global_ran_node_list: typing.Optional[typing.Sequence[GlobalRanNodeId]] = OMIT,
        an_type_list: typing.Optional[typing.Sequence[AccessType]] = OMIT,
        nf_id: typing.Optional[str] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NonUeN2InfoSubscriptionCreatedData:
        """
        Parameters
        ----------
        n2information_class : N2InformationClass

        n2notify_callback_uri : str

        global_ran_node_list : typing.Optional[typing.Sequence[GlobalRanNodeId]]

        an_type_list : typing.Optional[typing.Sequence[AccessType]]

        nf_id : typing.Optional[str]

        supported_features : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NonUeN2InfoSubscriptionCreatedData
            Non UE N2 Info Subscription successfully created.

        Examples
        --------
        import asyncio

        from fern import AccessType, AsyncFernApi, N2InformationClass

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.non_ue_n2messages_subscriptions_collection_document.non_ue_n2info_subscribe(
                global_ran_node_list=[
                    {
                        "gNbId": {"bitLength": 24, "gNBValue": "gNBValue"},
                        "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                        "n3IwfId": "n3IwfId",
                        "ngeNbId": "ngeNbId",
                    },
                    {
                        "gNbId": {"bitLength": 24, "gNBValue": "gNBValue"},
                        "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                        "n3IwfId": "n3IwfId",
                        "ngeNbId": "ngeNbId",
                    },
                ],
                an_type_list=[AccessType.THREE_GPP_ACCESS, AccessType.THREE_GPP_ACCESS],
                n2information_class=N2InformationClass.SM,
                n2notify_callback_uri="n2NotifyCallbackUri",
                nf_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
                supported_features="supportedFeatures",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.non_ue_n2info_subscribe(
            n2information_class=n2information_class,
            n2notify_callback_uri=n2notify_callback_uri,
            global_ran_node_list=global_ran_node_list,
            an_type_list=an_type_list,
            nf_id=nf_id,
            supported_features=supported_features,
            request_options=request_options,
        )
        return _response.data
