

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.guami import Guami
from ..types.subscription_data import SubscriptionData
from .raw_client import AsyncRawSubscriptionsCollectionDocumentClient, RawSubscriptionsCollectionDocumentClient


OMIT = typing.cast(typing.Any, ...)


class SubscriptionsCollectionDocumentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSubscriptionsCollectionDocumentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSubscriptionsCollectionDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSubscriptionsCollectionDocumentClient
        """
        return self._raw_client

    def amf_status_change_subscribe(
        self,
        *,
        amf_status_uri: str,
        guami_list: typing.Optional[typing.Sequence[Guami]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionData:
        """
        Parameters
        ----------
        amf_status_uri : str

        guami_list : typing.Optional[typing.Sequence[Guami]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionData
            N1N2 Message Subscription successfully created.

        Examples
        --------
        from fern import FernApi, Guami, PlmnId

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.subscriptions_collection_document.amf_status_change_subscribe(
            amf_status_uri="amfStatusUri",
            guami_list=[
                Guami(
                    plmn_id=PlmnId(
                        mcc="mcc",
                        mnc="mnc",
                    ),
                    amf_id="amfId",
                ),
                Guami(
                    plmn_id=PlmnId(
                        mcc="mcc",
                        mnc="mnc",
                    ),
                    amf_id="amfId",
                ),
            ],
        )
        """
        _response = self._raw_client.amf_status_change_subscribe(
            amf_status_uri=amf_status_uri, guami_list=guami_list, request_options=request_options
        )
        return _response.data


class AsyncSubscriptionsCollectionDocumentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSubscriptionsCollectionDocumentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSubscriptionsCollectionDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSubscriptionsCollectionDocumentClient
        """
        return self._raw_client

    async def amf_status_change_subscribe(
        self,
        *,
        amf_status_uri: str,
        guami_list: typing.Optional[typing.Sequence[Guami]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionData:
        """
        Parameters
        ----------
        amf_status_uri : str

        guami_list : typing.Optional[typing.Sequence[Guami]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionData
            N1N2 Message Subscription successfully created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Guami, PlmnId

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.subscriptions_collection_document.amf_status_change_subscribe(
                amf_status_uri="amfStatusUri",
                guami_list=[
                    Guami(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        amf_id="amfId",
                    ),
                    Guami(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        amf_id="amfId",
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.amf_status_change_subscribe(
            amf_status_uri=amf_status_uri, guami_list=guami_list, request_options=request_options
        )
        return _response.data
