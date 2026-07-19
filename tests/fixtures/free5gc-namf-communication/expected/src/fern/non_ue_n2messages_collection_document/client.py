

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ecgi import Ecgi
from ..types.global_ran_node_id import GlobalRanNodeId
from ..types.n2info_container import N2InfoContainer
from ..types.n2information_transfer_rsp_data import N2InformationTransferRspData
from ..types.ncgi import Ncgi
from ..types.rat_selector import RatSelector
from ..types.tai import Tai
from .raw_client import AsyncRawNonUeN2MessagesCollectionDocumentClient, RawNonUeN2MessagesCollectionDocumentClient


OMIT = typing.cast(typing.Any, ...)


class NonUeN2MessagesCollectionDocumentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNonUeN2MessagesCollectionDocumentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNonUeN2MessagesCollectionDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNonUeN2MessagesCollectionDocumentClient
        """
        return self._raw_client

    def non_ue_n2message_transfer(
        self,
        *,
        n2information: N2InfoContainer,
        tai_list: typing.Optional[typing.Sequence[Tai]] = OMIT,
        rat_selector: typing.Optional[RatSelector] = OMIT,
        ecgi_list: typing.Optional[typing.Sequence[Ecgi]] = OMIT,
        ncgi_list: typing.Optional[typing.Sequence[Ncgi]] = OMIT,
        global_ran_node_list: typing.Optional[typing.Sequence[GlobalRanNodeId]] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> N2InformationTransferRspData:
        """
        Parameters
        ----------
        n2information : N2InfoContainer

        tai_list : typing.Optional[typing.Sequence[Tai]]

        rat_selector : typing.Optional[RatSelector]

        ecgi_list : typing.Optional[typing.Sequence[Ecgi]]

        ncgi_list : typing.Optional[typing.Sequence[Ncgi]]

        global_ran_node_list : typing.Optional[typing.Sequence[GlobalRanNodeId]]

        supported_features : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        N2InformationTransferRspData
            Non UE N2 Message Transfer successfully initiated.

        Examples
        --------
        from fern import FernApi, N2InfoContainer, N2InformationClass

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.non_ue_n2messages_collection_document.non_ue_n2message_transfer(
            n2information=N2InfoContainer(
                n2information_class=N2InformationClass.SM,
            ),
        )
        """
        _response = self._raw_client.non_ue_n2message_transfer(
            n2information=n2information,
            tai_list=tai_list,
            rat_selector=rat_selector,
            ecgi_list=ecgi_list,
            ncgi_list=ncgi_list,
            global_ran_node_list=global_ran_node_list,
            supported_features=supported_features,
            request_options=request_options,
        )
        return _response.data


class AsyncNonUeN2MessagesCollectionDocumentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNonUeN2MessagesCollectionDocumentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNonUeN2MessagesCollectionDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNonUeN2MessagesCollectionDocumentClient
        """
        return self._raw_client

    async def non_ue_n2message_transfer(
        self,
        *,
        n2information: N2InfoContainer,
        tai_list: typing.Optional[typing.Sequence[Tai]] = OMIT,
        rat_selector: typing.Optional[RatSelector] = OMIT,
        ecgi_list: typing.Optional[typing.Sequence[Ecgi]] = OMIT,
        ncgi_list: typing.Optional[typing.Sequence[Ncgi]] = OMIT,
        global_ran_node_list: typing.Optional[typing.Sequence[GlobalRanNodeId]] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> N2InformationTransferRspData:
        """
        Parameters
        ----------
        n2information : N2InfoContainer

        tai_list : typing.Optional[typing.Sequence[Tai]]

        rat_selector : typing.Optional[RatSelector]

        ecgi_list : typing.Optional[typing.Sequence[Ecgi]]

        ncgi_list : typing.Optional[typing.Sequence[Ncgi]]

        global_ran_node_list : typing.Optional[typing.Sequence[GlobalRanNodeId]]

        supported_features : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        N2InformationTransferRspData
            Non UE N2 Message Transfer successfully initiated.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, N2InfoContainer, N2InformationClass

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.non_ue_n2messages_collection_document.non_ue_n2message_transfer(
                n2information=N2InfoContainer(
                    n2information_class=N2InformationClass.SM,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.non_ue_n2message_transfer(
            n2information=n2information,
            tai_list=tai_list,
            rat_selector=rat_selector,
            ecgi_list=ecgi_list,
            ncgi_list=ncgi_list,
            global_ran_node_list=global_ran_node_list,
            supported_features=supported_features,
            request_options=request_options,
        )
        return _response.data
