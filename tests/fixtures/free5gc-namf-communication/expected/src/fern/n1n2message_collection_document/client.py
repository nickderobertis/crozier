

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.area_of_validity import AreaOfValidity
from ..types.arp import Arp
from ..types.n1message_container import N1MessageContainer
from ..types.n1n2message_transfer_rsp_data import N1N2MessageTransferRspData
from ..types.n2info_container import N2InfoContainer
from .raw_client import AsyncRawN1N2MessageCollectionDocumentClient, RawN1N2MessageCollectionDocumentClient


OMIT = typing.cast(typing.Any, ...)


class N1N2MessageCollectionDocumentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawN1N2MessageCollectionDocumentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawN1N2MessageCollectionDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawN1N2MessageCollectionDocumentClient
        """
        return self._raw_client

    def n1n2message_transfer(
        self,
        ue_context_id: str,
        *,
        n1message_container: typing.Optional[N1MessageContainer] = OMIT,
        n2info_container: typing.Optional[N2InfoContainer] = OMIT,
        skip_ind: typing.Optional[bool] = OMIT,
        last_msg_indication: typing.Optional[bool] = OMIT,
        pdu_session_id: typing.Optional[int] = OMIT,
        lcs_correlation_id: typing.Optional[str] = OMIT,
        ppi: typing.Optional[int] = OMIT,
        arp: typing.Optional[Arp] = OMIT,
        _5qi: typing.Optional[int] = OMIT,
        n1n2failure_txf_notif_uri: typing.Optional[str] = OMIT,
        smf_reallocation_ind: typing.Optional[bool] = OMIT,
        area_of_validity: typing.Optional[AreaOfValidity] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> N1N2MessageTransferRspData:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        n1message_container : typing.Optional[N1MessageContainer]

        n2info_container : typing.Optional[N2InfoContainer]

        skip_ind : typing.Optional[bool]

        last_msg_indication : typing.Optional[bool]

        pdu_session_id : typing.Optional[int]

        lcs_correlation_id : typing.Optional[str]

        ppi : typing.Optional[int]

        arp : typing.Optional[Arp]

        _5qi : typing.Optional[int]

        n1n2failure_txf_notif_uri : typing.Optional[str]

        smf_reallocation_ind : typing.Optional[bool]

        area_of_validity : typing.Optional[AreaOfValidity]

        supported_features : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        N1N2MessageTransferRspData
            N1N2 Message Transfer successfully initiated.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.n1n2message_collection_document.n1n2message_transfer(
            ue_context_id="ueContextId",
        )
        """
        _response = self._raw_client.n1n2message_transfer(
            ue_context_id,
            n1message_container=n1message_container,
            n2info_container=n2info_container,
            skip_ind=skip_ind,
            last_msg_indication=last_msg_indication,
            pdu_session_id=pdu_session_id,
            lcs_correlation_id=lcs_correlation_id,
            ppi=ppi,
            arp=arp,
            _5qi=_5qi,
            n1n2failure_txf_notif_uri=n1n2failure_txf_notif_uri,
            smf_reallocation_ind=smf_reallocation_ind,
            area_of_validity=area_of_validity,
            supported_features=supported_features,
            request_options=request_options,
        )
        return _response.data


class AsyncN1N2MessageCollectionDocumentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawN1N2MessageCollectionDocumentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawN1N2MessageCollectionDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawN1N2MessageCollectionDocumentClient
        """
        return self._raw_client

    async def n1n2message_transfer(
        self,
        ue_context_id: str,
        *,
        n1message_container: typing.Optional[N1MessageContainer] = OMIT,
        n2info_container: typing.Optional[N2InfoContainer] = OMIT,
        skip_ind: typing.Optional[bool] = OMIT,
        last_msg_indication: typing.Optional[bool] = OMIT,
        pdu_session_id: typing.Optional[int] = OMIT,
        lcs_correlation_id: typing.Optional[str] = OMIT,
        ppi: typing.Optional[int] = OMIT,
        arp: typing.Optional[Arp] = OMIT,
        _5qi: typing.Optional[int] = OMIT,
        n1n2failure_txf_notif_uri: typing.Optional[str] = OMIT,
        smf_reallocation_ind: typing.Optional[bool] = OMIT,
        area_of_validity: typing.Optional[AreaOfValidity] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> N1N2MessageTransferRspData:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        n1message_container : typing.Optional[N1MessageContainer]

        n2info_container : typing.Optional[N2InfoContainer]

        skip_ind : typing.Optional[bool]

        last_msg_indication : typing.Optional[bool]

        pdu_session_id : typing.Optional[int]

        lcs_correlation_id : typing.Optional[str]

        ppi : typing.Optional[int]

        arp : typing.Optional[Arp]

        _5qi : typing.Optional[int]

        n1n2failure_txf_notif_uri : typing.Optional[str]

        smf_reallocation_ind : typing.Optional[bool]

        area_of_validity : typing.Optional[AreaOfValidity]

        supported_features : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        N1N2MessageTransferRspData
            N1N2 Message Transfer successfully initiated.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.n1n2message_collection_document.n1n2message_transfer(
                ue_context_id="ueContextId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.n1n2message_transfer(
            ue_context_id,
            n1message_container=n1message_container,
            n2info_container=n2info_container,
            skip_ind=skip_ind,
            last_msg_indication=last_msg_indication,
            pdu_session_id=pdu_session_id,
            lcs_correlation_id=lcs_correlation_id,
            ppi=ppi,
            arp=arp,
            _5qi=_5qi,
            n1n2failure_txf_notif_uri=n1n2failure_txf_notif_uri,
            smf_reallocation_ind=smf_reallocation_ind,
            area_of_validity=area_of_validity,
            supported_features=supported_features,
            request_options=request_options,
        )
        return _response.data
