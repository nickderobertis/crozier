

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.access_type import AccessType
from ..types.arp import Arp
from ..types.assigned_ebi_data import AssignedEbiData
from ..types.eps_bearer_id import EpsBearerId
from ..types.n1message_container import N1MessageContainer
from ..types.ng_ap_cause import NgApCause
from ..types.pdu_session_id import PduSessionId
from ..types.plmn_id import PlmnId
from ..types.transfer_reason import TransferReason
from ..types.ue_context_create_data import UeContextCreateData
from ..types.ue_context_created_data import UeContextCreatedData
from ..types.ue_context_transfer_rsp_data import UeContextTransferRspData
from ..types.ue_context_transfer_status import UeContextTransferStatus
from ..types.ue_reg_status_update_rsp_data import UeRegStatusUpdateRspData
from .raw_client import AsyncRawIndividualUeContextDocumentClient, RawIndividualUeContextDocumentClient


OMIT = typing.cast(typing.Any, ...)


class IndividualUeContextDocumentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIndividualUeContextDocumentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIndividualUeContextDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIndividualUeContextDocumentClient
        """
        return self._raw_client

    def create_ue_context(
        self,
        ue_context_id: str,
        *,
        json_data: typing.Optional[UeContextCreateData] = OMIT,
        binary_data_n1message: typing.Optional[core.File] = OMIT,
        binary_data_n2information: typing.Optional[core.File] = OMIT,
        binary_data_n2information_ext1: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UeContextCreatedData:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        json_data : typing.Optional[UeContextCreateData]

        binary_data_n1message : typing.Optional[core.File]
            See core.File for more documentation

        binary_data_n2information : typing.Optional[core.File]
            See core.File for more documentation

        binary_data_n2information_ext1 : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UeContextCreatedData
            UE context successfully created.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.individual_ue_context_document.create_ue_context(
            ue_context_id="ueContextId",
        )
        """
        _response = self._raw_client.create_ue_context(
            ue_context_id,
            json_data=json_data,
            binary_data_n1message=binary_data_n1message,
            binary_data_n2information=binary_data_n2information,
            binary_data_n2information_ext1=binary_data_n2information_ext1,
            request_options=request_options,
        )
        return _response.data

    def release_ue_context(
        self,
        ue_context_id: str,
        *,
        ngap_cause: NgApCause,
        supi: typing.Optional[str] = OMIT,
        unauthenticated_supi: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        ngap_cause : NgApCause

        supi : typing.Optional[str]

        unauthenticated_supi : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, NgApCause

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.individual_ue_context_document.release_ue_context(
            ue_context_id="ueContextId",
            ngap_cause=NgApCause(
                group=0,
                value=0,
            ),
        )
        """
        _response = self._raw_client.release_ue_context(
            ue_context_id,
            ngap_cause=ngap_cause,
            supi=supi,
            unauthenticated_supi=unauthenticated_supi,
            request_options=request_options,
        )
        return _response.data

    def ebi_assignment(
        self,
        ue_context_id: str,
        *,
        pdu_session_id: int,
        arp_list: typing.Optional[typing.Sequence[Arp]] = OMIT,
        released_ebi_list: typing.Optional[typing.Sequence[EpsBearerId]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssignedEbiData:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        pdu_session_id : int

        arp_list : typing.Optional[typing.Sequence[Arp]]

        released_ebi_list : typing.Optional[typing.Sequence[EpsBearerId]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssignedEbiData
            EBI Assignment successfully performed.

        Examples
        --------
        from fern import Arp, FernApi, PreemptionCapability, PreemptionVulnerability

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.individual_ue_context_document.ebi_assignment(
            ue_context_id="ueContextId",
            pdu_session_id=20,
            arp_list=[
                Arp(
                    priority_level=10,
                    preempt_cap=PreemptionCapability.NOT_PREEMPT,
                    preempt_vuln=PreemptionVulnerability.NOT_PREEMPTABLE,
                ),
                Arp(
                    priority_level=10,
                    preempt_cap=PreemptionCapability.NOT_PREEMPT,
                    preempt_vuln=PreemptionVulnerability.NOT_PREEMPTABLE,
                ),
            ],
            released_ebi_list=[1, 1],
        )
        """
        _response = self._raw_client.ebi_assignment(
            ue_context_id,
            pdu_session_id=pdu_session_id,
            arp_list=arp_list,
            released_ebi_list=released_ebi_list,
            request_options=request_options,
        )
        return _response.data

    def ue_context_transfer(
        self,
        ue_context_id: str,
        *,
        reason: TransferReason,
        access_type: AccessType,
        plmn_id: typing.Optional[PlmnId] = OMIT,
        reg_request: typing.Optional[N1MessageContainer] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UeContextTransferRspData:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        reason : TransferReason

        access_type : AccessType

        plmn_id : typing.Optional[PlmnId]

        reg_request : typing.Optional[N1MessageContainer]

        supported_features : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UeContextTransferRspData
            UE context transfer successfully initiated.

        Examples
        --------
        from fern import AccessType, FernApi, TransferReason

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.individual_ue_context_document.ue_context_transfer(
            ue_context_id="ueContextId",
            reason=TransferReason.INIT_REG,
            access_type=AccessType.THREE_GPP_ACCESS,
        )
        """
        _response = self._raw_client.ue_context_transfer(
            ue_context_id,
            reason=reason,
            access_type=access_type,
            plmn_id=plmn_id,
            reg_request=reg_request,
            supported_features=supported_features,
            request_options=request_options,
        )
        return _response.data

    def registration_status_update(
        self,
        ue_context_id: str,
        *,
        transfer_status: UeContextTransferStatus,
        to_release_session_list: typing.Optional[typing.Sequence[PduSessionId]] = OMIT,
        pcf_reselected_ind: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UeRegStatusUpdateRspData:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        transfer_status : UeContextTransferStatus

        to_release_session_list : typing.Optional[typing.Sequence[PduSessionId]]

        pcf_reselected_ind : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UeRegStatusUpdateRspData
            UE context transfer status successfully updated.

        Examples
        --------
        from fern import FernApi, UeContextTransferStatus

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.individual_ue_context_document.registration_status_update(
            ue_context_id="ueContextId",
            transfer_status=UeContextTransferStatus.TRANSFERRED,
            to_release_session_list=[1, 1],
            pcf_reselected_ind=True,
        )
        """
        _response = self._raw_client.registration_status_update(
            ue_context_id,
            transfer_status=transfer_status,
            to_release_session_list=to_release_session_list,
            pcf_reselected_ind=pcf_reselected_ind,
            request_options=request_options,
        )
        return _response.data


class AsyncIndividualUeContextDocumentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIndividualUeContextDocumentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIndividualUeContextDocumentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIndividualUeContextDocumentClient
        """
        return self._raw_client

    async def create_ue_context(
        self,
        ue_context_id: str,
        *,
        json_data: typing.Optional[UeContextCreateData] = OMIT,
        binary_data_n1message: typing.Optional[core.File] = OMIT,
        binary_data_n2information: typing.Optional[core.File] = OMIT,
        binary_data_n2information_ext1: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UeContextCreatedData:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        json_data : typing.Optional[UeContextCreateData]

        binary_data_n1message : typing.Optional[core.File]
            See core.File for more documentation

        binary_data_n2information : typing.Optional[core.File]
            See core.File for more documentation

        binary_data_n2information_ext1 : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UeContextCreatedData
            UE context successfully created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.individual_ue_context_document.create_ue_context(
                ue_context_id="ueContextId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_ue_context(
            ue_context_id,
            json_data=json_data,
            binary_data_n1message=binary_data_n1message,
            binary_data_n2information=binary_data_n2information,
            binary_data_n2information_ext1=binary_data_n2information_ext1,
            request_options=request_options,
        )
        return _response.data

    async def release_ue_context(
        self,
        ue_context_id: str,
        *,
        ngap_cause: NgApCause,
        supi: typing.Optional[str] = OMIT,
        unauthenticated_supi: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        ngap_cause : NgApCause

        supi : typing.Optional[str]

        unauthenticated_supi : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, NgApCause

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.individual_ue_context_document.release_ue_context(
                ue_context_id="ueContextId",
                ngap_cause=NgApCause(
                    group=0,
                    value=0,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.release_ue_context(
            ue_context_id,
            ngap_cause=ngap_cause,
            supi=supi,
            unauthenticated_supi=unauthenticated_supi,
            request_options=request_options,
        )
        return _response.data

    async def ebi_assignment(
        self,
        ue_context_id: str,
        *,
        pdu_session_id: int,
        arp_list: typing.Optional[typing.Sequence[Arp]] = OMIT,
        released_ebi_list: typing.Optional[typing.Sequence[EpsBearerId]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssignedEbiData:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        pdu_session_id : int

        arp_list : typing.Optional[typing.Sequence[Arp]]

        released_ebi_list : typing.Optional[typing.Sequence[EpsBearerId]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssignedEbiData
            EBI Assignment successfully performed.

        Examples
        --------
        import asyncio

        from fern import (
            Arp,
            AsyncFernApi,
            PreemptionCapability,
            PreemptionVulnerability,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.individual_ue_context_document.ebi_assignment(
                ue_context_id="ueContextId",
                pdu_session_id=20,
                arp_list=[
                    Arp(
                        priority_level=10,
                        preempt_cap=PreemptionCapability.NOT_PREEMPT,
                        preempt_vuln=PreemptionVulnerability.NOT_PREEMPTABLE,
                    ),
                    Arp(
                        priority_level=10,
                        preempt_cap=PreemptionCapability.NOT_PREEMPT,
                        preempt_vuln=PreemptionVulnerability.NOT_PREEMPTABLE,
                    ),
                ],
                released_ebi_list=[1, 1],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ebi_assignment(
            ue_context_id,
            pdu_session_id=pdu_session_id,
            arp_list=arp_list,
            released_ebi_list=released_ebi_list,
            request_options=request_options,
        )
        return _response.data

    async def ue_context_transfer(
        self,
        ue_context_id: str,
        *,
        reason: TransferReason,
        access_type: AccessType,
        plmn_id: typing.Optional[PlmnId] = OMIT,
        reg_request: typing.Optional[N1MessageContainer] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UeContextTransferRspData:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        reason : TransferReason

        access_type : AccessType

        plmn_id : typing.Optional[PlmnId]

        reg_request : typing.Optional[N1MessageContainer]

        supported_features : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UeContextTransferRspData
            UE context transfer successfully initiated.

        Examples
        --------
        import asyncio

        from fern import AccessType, AsyncFernApi, TransferReason

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.individual_ue_context_document.ue_context_transfer(
                ue_context_id="ueContextId",
                reason=TransferReason.INIT_REG,
                access_type=AccessType.THREE_GPP_ACCESS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ue_context_transfer(
            ue_context_id,
            reason=reason,
            access_type=access_type,
            plmn_id=plmn_id,
            reg_request=reg_request,
            supported_features=supported_features,
            request_options=request_options,
        )
        return _response.data

    async def registration_status_update(
        self,
        ue_context_id: str,
        *,
        transfer_status: UeContextTransferStatus,
        to_release_session_list: typing.Optional[typing.Sequence[PduSessionId]] = OMIT,
        pcf_reselected_ind: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UeRegStatusUpdateRspData:
        """
        Parameters
        ----------
        ue_context_id : str
            UE Context Identifier

        transfer_status : UeContextTransferStatus

        to_release_session_list : typing.Optional[typing.Sequence[PduSessionId]]

        pcf_reselected_ind : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UeRegStatusUpdateRspData
            UE context transfer status successfully updated.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, UeContextTransferStatus

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.individual_ue_context_document.registration_status_update(
                ue_context_id="ueContextId",
                transfer_status=UeContextTransferStatus.TRANSFERRED,
                to_release_session_list=[1, 1],
                pcf_reselected_ind=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.registration_status_update(
            ue_context_id,
            transfer_status=transfer_status,
            to_release_session_list=to_release_session_list,
            pcf_reselected_ind=pcf_reselected_ind,
            request_options=request_options,
        )
        return _response.data
