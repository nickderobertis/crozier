

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.guami import Guami
from ..types.subscription_data import SubscriptionData
from .raw_client import AsyncRawIndividualSubscriptionDocumentClient, RawIndividualSubscriptionDocumentClient


OMIT = typing.cast(typing.Any, ...)


class IndividualSubscriptionDocumentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIndividualSubscriptionDocumentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIndividualSubscriptionDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIndividualSubscriptionDocumentClient
        """
        return self._raw_client

    def amf_status_change_subscribe_modfy(
        self,
        subscription_id: str,
        *,
        amf_status_uri: str,
        guami_list: typing.Optional[typing.Sequence[Guami]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionData:
        """
        Parameters
        ----------
        subscription_id : str
            AMF Status Change Subscription Identifier

        amf_status_uri : str

        guami_list : typing.Optional[typing.Sequence[Guami]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionData
            N1N2 Message Subscription successfully updated.

        Examples
        --------
        from fern import FernApi, Guami, PlmnId

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.individual_subscription_document.amf_status_change_subscribe_modfy(
            subscription_id="subscriptionId",
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
        _response = self._raw_client.amf_status_change_subscribe_modfy(
            subscription_id, amf_status_uri=amf_status_uri, guami_list=guami_list, request_options=request_options
        )
        return _response.data

    def amf_status_change_un_subscribe(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str
            AMF Status Change Subscription Identifier

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
        client.individual_subscription_document.amf_status_change_un_subscribe(
            subscription_id="subscriptionId",
        )
        """
        _response = self._raw_client.amf_status_change_un_subscribe(subscription_id, request_options=request_options)
        return _response.data


class AsyncIndividualSubscriptionDocumentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIndividualSubscriptionDocumentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIndividualSubscriptionDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIndividualSubscriptionDocumentClient
        """
        return self._raw_client

    async def amf_status_change_subscribe_modfy(
        self,
        subscription_id: str,
        *,
        amf_status_uri: str,
        guami_list: typing.Optional[typing.Sequence[Guami]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionData:
        """
        Parameters
        ----------
        subscription_id : str
            AMF Status Change Subscription Identifier

        amf_status_uri : str

        guami_list : typing.Optional[typing.Sequence[Guami]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionData
            N1N2 Message Subscription successfully updated.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Guami, PlmnId

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.individual_subscription_document.amf_status_change_subscribe_modfy(
                subscription_id="subscriptionId",
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
        _response = await self._raw_client.amf_status_change_subscribe_modfy(
            subscription_id, amf_status_uri=amf_status_uri, guami_list=guami_list, request_options=request_options
        )
        return _response.data

    async def amf_status_change_un_subscribe(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str
            AMF Status Change Subscription Identifier

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
            await client.individual_subscription_document.amf_status_change_un_subscribe(
                subscription_id="subscriptionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.amf_status_change_un_subscribe(
            subscription_id, request_options=request_options
        )
        return _response.data
