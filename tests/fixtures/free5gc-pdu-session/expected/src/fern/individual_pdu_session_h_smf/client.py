

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.access_type import AccessType
from ..types.cause import Cause
from ..types.eps_bearer_id import EpsBearerId
from ..types.eps_interworking_indication import EpsInterworkingIndication
from ..types.hsmf_updated_data import HsmfUpdatedData
from ..types.ng_ap_cause import NgApCause
from ..types.pdu_session_notify_item import PduSessionNotifyItem
from ..types.plmn_id import PlmnId
from ..types.qos_flow_item import QosFlowItem
from ..types.qos_flow_notify_item import QosFlowNotifyItem
from ..types.rat_type import RatType
from ..types.ref_to_binary_data import RefToBinaryData
from ..types.request_indication import RequestIndication
from ..types.secondary_rat_usage_report import SecondaryRatUsageReport
from ..types.tunnel_info import TunnelInfo
from ..types.user_location import UserLocation
from .raw_client import AsyncRawIndividualPduSessionHSmfClient, RawIndividualPduSessionHSmfClient


OMIT = typing.cast(typing.Any, ...)


class IndividualPduSessionHSmfClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIndividualPduSessionHSmfClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIndividualPduSessionHSmfClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIndividualPduSessionHSmfClient
        """
        return self._raw_client

    def update_pdu_session(
        self,
        pdu_session_ref: str,
        *,
        request_indication: RequestIndication,
        pei: typing.Optional[str] = OMIT,
        vcn_tunnel_info: typing.Optional[TunnelInfo] = OMIT,
        serving_network: typing.Optional[PlmnId] = OMIT,
        an_type: typing.Optional[AccessType] = OMIT,
        rat_type: typing.Optional[RatType] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        pause_charging: typing.Optional[bool] = OMIT,
        pti: typing.Optional[int] = OMIT,
        n1sm_info_from_ue: typing.Optional[RefToBinaryData] = OMIT,
        unknown_n1sm_info: typing.Optional[RefToBinaryData] = OMIT,
        qos_flows_rel_notify_list: typing.Optional[typing.Sequence[QosFlowItem]] = OMIT,
        qos_flows_notify_list: typing.Optional[typing.Sequence[QosFlowNotifyItem]] = OMIT,
        notify_list: typing.Optional[typing.Sequence[PduSessionNotifyItem]] = OMIT,
        eps_bearer_id: typing.Optional[typing.Sequence[EpsBearerId]] = OMIT,
        ho_preparation_indication: typing.Optional[bool] = OMIT,
        revoke_ebi_list: typing.Optional[typing.Sequence[EpsBearerId]] = OMIT,
        cause: typing.Optional[Cause] = OMIT,
        ng_ap_cause: typing.Optional[NgApCause] = OMIT,
        _5g_mm_cause_value: typing.Optional[int] = OMIT,
        always_on_requested: typing.Optional[bool] = OMIT,
        eps_interworking_ind: typing.Optional[EpsInterworkingIndication] = OMIT,
        secondary_rat_usage_report: typing.Optional[typing.Sequence[SecondaryRatUsageReport]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[HsmfUpdatedData]:
        """
        Parameters
        ----------
        pdu_session_ref : str
            PDU session reference

        request_indication : RequestIndication

        pei : typing.Optional[str]

        vcn_tunnel_info : typing.Optional[TunnelInfo]

        serving_network : typing.Optional[PlmnId]

        an_type : typing.Optional[AccessType]

        rat_type : typing.Optional[RatType]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        pause_charging : typing.Optional[bool]

        pti : typing.Optional[int]

        n1sm_info_from_ue : typing.Optional[RefToBinaryData]

        unknown_n1sm_info : typing.Optional[RefToBinaryData]

        qos_flows_rel_notify_list : typing.Optional[typing.Sequence[QosFlowItem]]

        qos_flows_notify_list : typing.Optional[typing.Sequence[QosFlowNotifyItem]]

        notify_list : typing.Optional[typing.Sequence[PduSessionNotifyItem]]

        eps_bearer_id : typing.Optional[typing.Sequence[EpsBearerId]]

        ho_preparation_indication : typing.Optional[bool]

        revoke_ebi_list : typing.Optional[typing.Sequence[EpsBearerId]]

        cause : typing.Optional[Cause]

        ng_ap_cause : typing.Optional[NgApCause]

        _5g_mm_cause_value : typing.Optional[int]

        always_on_requested : typing.Optional[bool]

        eps_interworking_ind : typing.Optional[EpsInterworkingIndication]

        secondary_rat_usage_report : typing.Optional[typing.Sequence[SecondaryRatUsageReport]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[HsmfUpdatedData]
            successful update of a PDU session with content in the response

        Examples
        --------
        import datetime

        from fern import (
            Ecgi,
            EutraLocation,
            FernApi,
            N3GaLocation,
            Ncgi,
            NgApCause,
            NotificationCause,
            NrLocation,
            PduSessionNotifyItem,
            PlmnId,
            QosFlowItem,
            QosFlowNotifyItem,
            QosFlowUsageReport,
            RatType,
            RefToBinaryData,
            RequestIndication,
            SecondaryRatUsageReport,
            Tai,
            TunnelInfo,
            UserLocation,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.individual_pdu_session_h_smf.update_pdu_session(
            pdu_session_ref="pduSessionRef",
            request_indication=RequestIndication.UE_REQ_PDU_SES_MOD,
            pei="pei",
            vcn_tunnel_info=TunnelInfo(
                ipv4addr="198.51.100.1",
                ipv6addr="2001:db8:85a3::8a2e:370:7334",
                gtp_teid="gtpTeid",
            ),
            serving_network=PlmnId(
                mcc="mcc",
                mnc="mnc",
            ),
            ue_location=UserLocation(
                eutra_location=EutraLocation(
                    tai=Tai(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        tac="tac",
                    ),
                    ecgi=Ecgi(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        eutra_cell_id="eutraCellId",
                    ),
                    age_of_location_information=2624,
                    ue_location_timestamp=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    geographical_information="geographicalInformation",
                    geodetic_information="geodeticInformation",
                    global_ngenb_id={
                        "gNbId": {"bitLength": 28, "gNBValue": "gNBValue"},
                        "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                        "n3IwfId": "n3IwfId",
                        "ngeNbId": "ngeNbId",
                    },
                ),
                nr_location=NrLocation(
                    tai=Tai(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        tac="tac",
                    ),
                    ncgi=Ncgi(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        nr_cell_id="nrCellId",
                    ),
                    age_of_location_information=4803,
                    ue_location_timestamp=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    geographical_information="geographicalInformation",
                    geodetic_information="geodeticInformation",
                    global_gnb_id={
                        "gNbId": {"bitLength": 28, "gNBValue": "gNBValue"},
                        "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                        "n3IwfId": "n3IwfId",
                        "ngeNbId": "ngeNbId",
                    },
                ),
                n3ga_location=N3GaLocation(
                    n3gpp_tai=Tai(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        tac="tac",
                    ),
                    n3iwf_id="n3IwfId",
                    ue_ipv4addr="198.51.100.1",
                    ue_ipv6addr="2001:db8:85a3::8a2e:370:7334",
                    port_number=0,
                ),
            ),
            ue_time_zone="ueTimeZone",
            add_ue_location=UserLocation(
                eutra_location=EutraLocation(
                    tai=Tai(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        tac="tac",
                    ),
                    ecgi=Ecgi(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        eutra_cell_id="eutraCellId",
                    ),
                    age_of_location_information=2624,
                    ue_location_timestamp=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    geographical_information="geographicalInformation",
                    geodetic_information="geodeticInformation",
                    global_ngenb_id={
                        "gNbId": {"bitLength": 28, "gNBValue": "gNBValue"},
                        "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                        "n3IwfId": "n3IwfId",
                        "ngeNbId": "ngeNbId",
                    },
                ),
                nr_location=NrLocation(
                    tai=Tai(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        tac="tac",
                    ),
                    ncgi=Ncgi(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        nr_cell_id="nrCellId",
                    ),
                    age_of_location_information=4803,
                    ue_location_timestamp=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    geographical_information="geographicalInformation",
                    geodetic_information="geodeticInformation",
                    global_gnb_id={
                        "gNbId": {"bitLength": 28, "gNBValue": "gNBValue"},
                        "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                        "n3IwfId": "n3IwfId",
                        "ngeNbId": "ngeNbId",
                    },
                ),
                n3ga_location=N3GaLocation(
                    n3gpp_tai=Tai(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        tac="tac",
                    ),
                    n3iwf_id="n3IwfId",
                    ue_ipv4addr="198.51.100.1",
                    ue_ipv6addr="2001:db8:85a3::8a2e:370:7334",
                    port_number=0,
                ),
            ),
            pause_charging=True,
            pti=20,
            n1sm_info_from_ue=RefToBinaryData(
                content_id="contentId",
            ),
            unknown_n1sm_info=RefToBinaryData(
                content_id="contentId",
            ),
            qos_flows_rel_notify_list=[
                QosFlowItem(
                    qfi=5,
                ),
                QosFlowItem(
                    qfi=5,
                ),
            ],
            qos_flows_notify_list=[
                QosFlowNotifyItem(
                    qfi=37,
                    notification_cause=NotificationCause.QOS_FULFILLED,
                ),
                QosFlowNotifyItem(
                    qfi=37,
                    notification_cause=NotificationCause.QOS_FULFILLED,
                ),
            ],
            notify_list=[
                PduSessionNotifyItem(
                    notification_cause=NotificationCause.QOS_FULFILLED,
                ),
                PduSessionNotifyItem(
                    notification_cause=NotificationCause.QOS_FULFILLED,
                ),
            ],
            eps_bearer_id=[1, 1],
            ho_preparation_indication=True,
            revoke_ebi_list=[1, 1],
            ng_ap_cause=NgApCause(
                group=0,
                value=0,
            ),
            f_5g_mm_cause_value=0,
            always_on_requested=False,
            secondary_rat_usage_report=[
                SecondaryRatUsageReport(
                    secondary_rat_type=RatType.NR,
                    qos_flows_usage_data=[
                        QosFlowUsageReport(
                            qfi=37,
                            start_time_stamp=datetime.datetime.fromisoformat(
                                "2024-01-15 09:30:00+00:00",
                            ),
                            end_time_stamp=datetime.datetime.fromisoformat(
                                "2024-01-15 09:30:00+00:00",
                            ),
                            downlink_volume=1,
                            uplink_volume=5,
                        ),
                        QosFlowUsageReport(
                            qfi=37,
                            start_time_stamp=datetime.datetime.fromisoformat(
                                "2024-01-15 09:30:00+00:00",
                            ),
                            end_time_stamp=datetime.datetime.fromisoformat(
                                "2024-01-15 09:30:00+00:00",
                            ),
                            downlink_volume=1,
                            uplink_volume=5,
                        ),
                    ],
                ),
                SecondaryRatUsageReport(
                    secondary_rat_type=RatType.NR,
                    qos_flows_usage_data=[
                        QosFlowUsageReport(
                            qfi=37,
                            start_time_stamp=datetime.datetime.fromisoformat(
                                "2024-01-15 09:30:00+00:00",
                            ),
                            end_time_stamp=datetime.datetime.fromisoformat(
                                "2024-01-15 09:30:00+00:00",
                            ),
                            downlink_volume=1,
                            uplink_volume=5,
                        ),
                        QosFlowUsageReport(
                            qfi=37,
                            start_time_stamp=datetime.datetime.fromisoformat(
                                "2024-01-15 09:30:00+00:00",
                            ),
                            end_time_stamp=datetime.datetime.fromisoformat(
                                "2024-01-15 09:30:00+00:00",
                            ),
                            downlink_volume=1,
                            uplink_volume=5,
                        ),
                    ],
                ),
            ],
        )
        """
        _response = self._raw_client.update_pdu_session(
            pdu_session_ref,
            request_indication=request_indication,
            pei=pei,
            vcn_tunnel_info=vcn_tunnel_info,
            serving_network=serving_network,
            an_type=an_type,
            rat_type=rat_type,
            ue_location=ue_location,
            ue_time_zone=ue_time_zone,
            add_ue_location=add_ue_location,
            pause_charging=pause_charging,
            pti=pti,
            n1sm_info_from_ue=n1sm_info_from_ue,
            unknown_n1sm_info=unknown_n1sm_info,
            qos_flows_rel_notify_list=qos_flows_rel_notify_list,
            qos_flows_notify_list=qos_flows_notify_list,
            notify_list=notify_list,
            eps_bearer_id=eps_bearer_id,
            ho_preparation_indication=ho_preparation_indication,
            revoke_ebi_list=revoke_ebi_list,
            cause=cause,
            ng_ap_cause=ng_ap_cause,
            _5g_mm_cause_value=_5g_mm_cause_value,
            always_on_requested=always_on_requested,
            eps_interworking_ind=eps_interworking_ind,
            secondary_rat_usage_report=secondary_rat_usage_report,
            request_options=request_options,
        )
        return _response.data

    def release_pdu_session(
        self,
        pdu_session_ref: str,
        *,
        cause: typing.Optional[Cause] = OMIT,
        ng_ap_cause: typing.Optional[NgApCause] = OMIT,
        _5g_mm_cause_value: typing.Optional[int] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        secondary_rat_usage_report: typing.Optional[typing.Sequence[SecondaryRatUsageReport]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        pdu_session_ref : str
            PDU session reference

        cause : typing.Optional[Cause]

        ng_ap_cause : typing.Optional[NgApCause]

        _5g_mm_cause_value : typing.Optional[int]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        secondary_rat_usage_report : typing.Optional[typing.Sequence[SecondaryRatUsageReport]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from fern import (
            Ecgi,
            EutraLocation,
            FernApi,
            N3GaLocation,
            Ncgi,
            NgApCause,
            NrLocation,
            PlmnId,
            QosFlowUsageReport,
            RatType,
            SecondaryRatUsageReport,
            Tai,
            UserLocation,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.individual_pdu_session_h_smf.release_pdu_session(
            pdu_session_ref="pduSessionRef",
            ng_ap_cause=NgApCause(
                group=0,
                value=0,
            ),
            _5g_mm_cause_value=0,
            ue_location=UserLocation(
                eutra_location=EutraLocation(
                    tai=Tai(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        tac="tac",
                    ),
                    ecgi=Ecgi(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        eutra_cell_id="eutraCellId",
                    ),
                    age_of_location_information=2624,
                    ue_location_timestamp=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    geographical_information="geographicalInformation",
                    geodetic_information="geodeticInformation",
                    global_ngenb_id={
                        "gNbId": {"bitLength": 28, "gNBValue": "gNBValue"},
                        "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                        "n3IwfId": "n3IwfId",
                        "ngeNbId": "ngeNbId",
                    },
                ),
                nr_location=NrLocation(
                    tai=Tai(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        tac="tac",
                    ),
                    ncgi=Ncgi(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        nr_cell_id="nrCellId",
                    ),
                    age_of_location_information=4803,
                    ue_location_timestamp=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    geographical_information="geographicalInformation",
                    geodetic_information="geodeticInformation",
                    global_gnb_id={
                        "gNbId": {"bitLength": 28, "gNBValue": "gNBValue"},
                        "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                        "n3IwfId": "n3IwfId",
                        "ngeNbId": "ngeNbId",
                    },
                ),
                n3ga_location=N3GaLocation(
                    n3gpp_tai=Tai(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        tac="tac",
                    ),
                    n3iwf_id="n3IwfId",
                    ue_ipv4addr="198.51.100.1",
                    ue_ipv6addr="2001:db8:85a3::8a2e:370:7334",
                    port_number=0,
                ),
            ),
            ue_time_zone="ueTimeZone",
            add_ue_location=UserLocation(
                eutra_location=EutraLocation(
                    tai=Tai(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        tac="tac",
                    ),
                    ecgi=Ecgi(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        eutra_cell_id="eutraCellId",
                    ),
                    age_of_location_information=2624,
                    ue_location_timestamp=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    geographical_information="geographicalInformation",
                    geodetic_information="geodeticInformation",
                    global_ngenb_id={
                        "gNbId": {"bitLength": 28, "gNBValue": "gNBValue"},
                        "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                        "n3IwfId": "n3IwfId",
                        "ngeNbId": "ngeNbId",
                    },
                ),
                nr_location=NrLocation(
                    tai=Tai(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        tac="tac",
                    ),
                    ncgi=Ncgi(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        nr_cell_id="nrCellId",
                    ),
                    age_of_location_information=4803,
                    ue_location_timestamp=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    geographical_information="geographicalInformation",
                    geodetic_information="geodeticInformation",
                    global_gnb_id={
                        "gNbId": {"bitLength": 28, "gNBValue": "gNBValue"},
                        "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                        "n3IwfId": "n3IwfId",
                        "ngeNbId": "ngeNbId",
                    },
                ),
                n3ga_location=N3GaLocation(
                    n3gpp_tai=Tai(
                        plmn_id=PlmnId(
                            mcc="mcc",
                            mnc="mnc",
                        ),
                        tac="tac",
                    ),
                    n3iwf_id="n3IwfId",
                    ue_ipv4addr="198.51.100.1",
                    ue_ipv6addr="2001:db8:85a3::8a2e:370:7334",
                    port_number=0,
                ),
            ),
            secondary_rat_usage_report=[
                SecondaryRatUsageReport(
                    secondary_rat_type=RatType.NR,
                    qos_flows_usage_data=[
                        QosFlowUsageReport(
                            qfi=37,
                            start_time_stamp=datetime.datetime.fromisoformat(
                                "2024-01-15 09:30:00+00:00",
                            ),
                            end_time_stamp=datetime.datetime.fromisoformat(
                                "2024-01-15 09:30:00+00:00",
                            ),
                            downlink_volume=1,
                            uplink_volume=5,
                        ),
                        QosFlowUsageReport(
                            qfi=37,
                            start_time_stamp=datetime.datetime.fromisoformat(
                                "2024-01-15 09:30:00+00:00",
                            ),
                            end_time_stamp=datetime.datetime.fromisoformat(
                                "2024-01-15 09:30:00+00:00",
                            ),
                            downlink_volume=1,
                            uplink_volume=5,
                        ),
                    ],
                ),
                SecondaryRatUsageReport(
                    secondary_rat_type=RatType.NR,
                    qos_flows_usage_data=[
                        QosFlowUsageReport(
                            qfi=37,
                            start_time_stamp=datetime.datetime.fromisoformat(
                                "2024-01-15 09:30:00+00:00",
                            ),
                            end_time_stamp=datetime.datetime.fromisoformat(
                                "2024-01-15 09:30:00+00:00",
                            ),
                            downlink_volume=1,
                            uplink_volume=5,
                        ),
                        QosFlowUsageReport(
                            qfi=37,
                            start_time_stamp=datetime.datetime.fromisoformat(
                                "2024-01-15 09:30:00+00:00",
                            ),
                            end_time_stamp=datetime.datetime.fromisoformat(
                                "2024-01-15 09:30:00+00:00",
                            ),
                            downlink_volume=1,
                            uplink_volume=5,
                        ),
                    ],
                ),
            ],
        )
        """
        _response = self._raw_client.release_pdu_session(
            pdu_session_ref,
            cause=cause,
            ng_ap_cause=ng_ap_cause,
            _5g_mm_cause_value=_5g_mm_cause_value,
            ue_location=ue_location,
            ue_time_zone=ue_time_zone,
            add_ue_location=add_ue_location,
            secondary_rat_usage_report=secondary_rat_usage_report,
            request_options=request_options,
        )
        return _response.data


class AsyncIndividualPduSessionHSmfClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIndividualPduSessionHSmfClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIndividualPduSessionHSmfClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIndividualPduSessionHSmfClient
        """
        return self._raw_client

    async def update_pdu_session(
        self,
        pdu_session_ref: str,
        *,
        request_indication: RequestIndication,
        pei: typing.Optional[str] = OMIT,
        vcn_tunnel_info: typing.Optional[TunnelInfo] = OMIT,
        serving_network: typing.Optional[PlmnId] = OMIT,
        an_type: typing.Optional[AccessType] = OMIT,
        rat_type: typing.Optional[RatType] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        pause_charging: typing.Optional[bool] = OMIT,
        pti: typing.Optional[int] = OMIT,
        n1sm_info_from_ue: typing.Optional[RefToBinaryData] = OMIT,
        unknown_n1sm_info: typing.Optional[RefToBinaryData] = OMIT,
        qos_flows_rel_notify_list: typing.Optional[typing.Sequence[QosFlowItem]] = OMIT,
        qos_flows_notify_list: typing.Optional[typing.Sequence[QosFlowNotifyItem]] = OMIT,
        notify_list: typing.Optional[typing.Sequence[PduSessionNotifyItem]] = OMIT,
        eps_bearer_id: typing.Optional[typing.Sequence[EpsBearerId]] = OMIT,
        ho_preparation_indication: typing.Optional[bool] = OMIT,
        revoke_ebi_list: typing.Optional[typing.Sequence[EpsBearerId]] = OMIT,
        cause: typing.Optional[Cause] = OMIT,
        ng_ap_cause: typing.Optional[NgApCause] = OMIT,
        _5g_mm_cause_value: typing.Optional[int] = OMIT,
        always_on_requested: typing.Optional[bool] = OMIT,
        eps_interworking_ind: typing.Optional[EpsInterworkingIndication] = OMIT,
        secondary_rat_usage_report: typing.Optional[typing.Sequence[SecondaryRatUsageReport]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[HsmfUpdatedData]:
        """
        Parameters
        ----------
        pdu_session_ref : str
            PDU session reference

        request_indication : RequestIndication

        pei : typing.Optional[str]

        vcn_tunnel_info : typing.Optional[TunnelInfo]

        serving_network : typing.Optional[PlmnId]

        an_type : typing.Optional[AccessType]

        rat_type : typing.Optional[RatType]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        pause_charging : typing.Optional[bool]

        pti : typing.Optional[int]

        n1sm_info_from_ue : typing.Optional[RefToBinaryData]

        unknown_n1sm_info : typing.Optional[RefToBinaryData]

        qos_flows_rel_notify_list : typing.Optional[typing.Sequence[QosFlowItem]]

        qos_flows_notify_list : typing.Optional[typing.Sequence[QosFlowNotifyItem]]

        notify_list : typing.Optional[typing.Sequence[PduSessionNotifyItem]]

        eps_bearer_id : typing.Optional[typing.Sequence[EpsBearerId]]

        ho_preparation_indication : typing.Optional[bool]

        revoke_ebi_list : typing.Optional[typing.Sequence[EpsBearerId]]

        cause : typing.Optional[Cause]

        ng_ap_cause : typing.Optional[NgApCause]

        _5g_mm_cause_value : typing.Optional[int]

        always_on_requested : typing.Optional[bool]

        eps_interworking_ind : typing.Optional[EpsInterworkingIndication]

        secondary_rat_usage_report : typing.Optional[typing.Sequence[SecondaryRatUsageReport]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[HsmfUpdatedData]
            successful update of a PDU session with content in the response

        Examples
        --------
        import asyncio
        import datetime

        from fern import (
            AsyncFernApi,
            Ecgi,
            EutraLocation,
            N3GaLocation,
            Ncgi,
            NgApCause,
            NotificationCause,
            NrLocation,
            PduSessionNotifyItem,
            PlmnId,
            QosFlowItem,
            QosFlowNotifyItem,
            QosFlowUsageReport,
            RatType,
            RefToBinaryData,
            RequestIndication,
            SecondaryRatUsageReport,
            Tai,
            TunnelInfo,
            UserLocation,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.individual_pdu_session_h_smf.update_pdu_session(
                pdu_session_ref="pduSessionRef",
                request_indication=RequestIndication.UE_REQ_PDU_SES_MOD,
                pei="pei",
                vcn_tunnel_info=TunnelInfo(
                    ipv4addr="198.51.100.1",
                    ipv6addr="2001:db8:85a3::8a2e:370:7334",
                    gtp_teid="gtpTeid",
                ),
                serving_network=PlmnId(
                    mcc="mcc",
                    mnc="mnc",
                ),
                ue_location=UserLocation(
                    eutra_location=EutraLocation(
                        tai=Tai(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            tac="tac",
                        ),
                        ecgi=Ecgi(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            eutra_cell_id="eutraCellId",
                        ),
                        age_of_location_information=2624,
                        ue_location_timestamp=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                        geographical_information="geographicalInformation",
                        geodetic_information="geodeticInformation",
                        global_ngenb_id={
                            "gNbId": {"bitLength": 28, "gNBValue": "gNBValue"},
                            "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                            "n3IwfId": "n3IwfId",
                            "ngeNbId": "ngeNbId",
                        },
                    ),
                    nr_location=NrLocation(
                        tai=Tai(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            tac="tac",
                        ),
                        ncgi=Ncgi(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            nr_cell_id="nrCellId",
                        ),
                        age_of_location_information=4803,
                        ue_location_timestamp=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                        geographical_information="geographicalInformation",
                        geodetic_information="geodeticInformation",
                        global_gnb_id={
                            "gNbId": {"bitLength": 28, "gNBValue": "gNBValue"},
                            "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                            "n3IwfId": "n3IwfId",
                            "ngeNbId": "ngeNbId",
                        },
                    ),
                    n3ga_location=N3GaLocation(
                        n3gpp_tai=Tai(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            tac="tac",
                        ),
                        n3iwf_id="n3IwfId",
                        ue_ipv4addr="198.51.100.1",
                        ue_ipv6addr="2001:db8:85a3::8a2e:370:7334",
                        port_number=0,
                    ),
                ),
                ue_time_zone="ueTimeZone",
                add_ue_location=UserLocation(
                    eutra_location=EutraLocation(
                        tai=Tai(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            tac="tac",
                        ),
                        ecgi=Ecgi(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            eutra_cell_id="eutraCellId",
                        ),
                        age_of_location_information=2624,
                        ue_location_timestamp=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                        geographical_information="geographicalInformation",
                        geodetic_information="geodeticInformation",
                        global_ngenb_id={
                            "gNbId": {"bitLength": 28, "gNBValue": "gNBValue"},
                            "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                            "n3IwfId": "n3IwfId",
                            "ngeNbId": "ngeNbId",
                        },
                    ),
                    nr_location=NrLocation(
                        tai=Tai(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            tac="tac",
                        ),
                        ncgi=Ncgi(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            nr_cell_id="nrCellId",
                        ),
                        age_of_location_information=4803,
                        ue_location_timestamp=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                        geographical_information="geographicalInformation",
                        geodetic_information="geodeticInformation",
                        global_gnb_id={
                            "gNbId": {"bitLength": 28, "gNBValue": "gNBValue"},
                            "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                            "n3IwfId": "n3IwfId",
                            "ngeNbId": "ngeNbId",
                        },
                    ),
                    n3ga_location=N3GaLocation(
                        n3gpp_tai=Tai(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            tac="tac",
                        ),
                        n3iwf_id="n3IwfId",
                        ue_ipv4addr="198.51.100.1",
                        ue_ipv6addr="2001:db8:85a3::8a2e:370:7334",
                        port_number=0,
                    ),
                ),
                pause_charging=True,
                pti=20,
                n1sm_info_from_ue=RefToBinaryData(
                    content_id="contentId",
                ),
                unknown_n1sm_info=RefToBinaryData(
                    content_id="contentId",
                ),
                qos_flows_rel_notify_list=[
                    QosFlowItem(
                        qfi=5,
                    ),
                    QosFlowItem(
                        qfi=5,
                    ),
                ],
                qos_flows_notify_list=[
                    QosFlowNotifyItem(
                        qfi=37,
                        notification_cause=NotificationCause.QOS_FULFILLED,
                    ),
                    QosFlowNotifyItem(
                        qfi=37,
                        notification_cause=NotificationCause.QOS_FULFILLED,
                    ),
                ],
                notify_list=[
                    PduSessionNotifyItem(
                        notification_cause=NotificationCause.QOS_FULFILLED,
                    ),
                    PduSessionNotifyItem(
                        notification_cause=NotificationCause.QOS_FULFILLED,
                    ),
                ],
                eps_bearer_id=[1, 1],
                ho_preparation_indication=True,
                revoke_ebi_list=[1, 1],
                ng_ap_cause=NgApCause(
                    group=0,
                    value=0,
                ),
                f_5g_mm_cause_value=0,
                always_on_requested=False,
                secondary_rat_usage_report=[
                    SecondaryRatUsageReport(
                        secondary_rat_type=RatType.NR,
                        qos_flows_usage_data=[
                            QosFlowUsageReport(
                                qfi=37,
                                start_time_stamp=datetime.datetime.fromisoformat(
                                    "2024-01-15 09:30:00+00:00",
                                ),
                                end_time_stamp=datetime.datetime.fromisoformat(
                                    "2024-01-15 09:30:00+00:00",
                                ),
                                downlink_volume=1,
                                uplink_volume=5,
                            ),
                            QosFlowUsageReport(
                                qfi=37,
                                start_time_stamp=datetime.datetime.fromisoformat(
                                    "2024-01-15 09:30:00+00:00",
                                ),
                                end_time_stamp=datetime.datetime.fromisoformat(
                                    "2024-01-15 09:30:00+00:00",
                                ),
                                downlink_volume=1,
                                uplink_volume=5,
                            ),
                        ],
                    ),
                    SecondaryRatUsageReport(
                        secondary_rat_type=RatType.NR,
                        qos_flows_usage_data=[
                            QosFlowUsageReport(
                                qfi=37,
                                start_time_stamp=datetime.datetime.fromisoformat(
                                    "2024-01-15 09:30:00+00:00",
                                ),
                                end_time_stamp=datetime.datetime.fromisoformat(
                                    "2024-01-15 09:30:00+00:00",
                                ),
                                downlink_volume=1,
                                uplink_volume=5,
                            ),
                            QosFlowUsageReport(
                                qfi=37,
                                start_time_stamp=datetime.datetime.fromisoformat(
                                    "2024-01-15 09:30:00+00:00",
                                ),
                                end_time_stamp=datetime.datetime.fromisoformat(
                                    "2024-01-15 09:30:00+00:00",
                                ),
                                downlink_volume=1,
                                uplink_volume=5,
                            ),
                        ],
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_pdu_session(
            pdu_session_ref,
            request_indication=request_indication,
            pei=pei,
            vcn_tunnel_info=vcn_tunnel_info,
            serving_network=serving_network,
            an_type=an_type,
            rat_type=rat_type,
            ue_location=ue_location,
            ue_time_zone=ue_time_zone,
            add_ue_location=add_ue_location,
            pause_charging=pause_charging,
            pti=pti,
            n1sm_info_from_ue=n1sm_info_from_ue,
            unknown_n1sm_info=unknown_n1sm_info,
            qos_flows_rel_notify_list=qos_flows_rel_notify_list,
            qos_flows_notify_list=qos_flows_notify_list,
            notify_list=notify_list,
            eps_bearer_id=eps_bearer_id,
            ho_preparation_indication=ho_preparation_indication,
            revoke_ebi_list=revoke_ebi_list,
            cause=cause,
            ng_ap_cause=ng_ap_cause,
            _5g_mm_cause_value=_5g_mm_cause_value,
            always_on_requested=always_on_requested,
            eps_interworking_ind=eps_interworking_ind,
            secondary_rat_usage_report=secondary_rat_usage_report,
            request_options=request_options,
        )
        return _response.data

    async def release_pdu_session(
        self,
        pdu_session_ref: str,
        *,
        cause: typing.Optional[Cause] = OMIT,
        ng_ap_cause: typing.Optional[NgApCause] = OMIT,
        _5g_mm_cause_value: typing.Optional[int] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        secondary_rat_usage_report: typing.Optional[typing.Sequence[SecondaryRatUsageReport]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        pdu_session_ref : str
            PDU session reference

        cause : typing.Optional[Cause]

        ng_ap_cause : typing.Optional[NgApCause]

        _5g_mm_cause_value : typing.Optional[int]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        secondary_rat_usage_report : typing.Optional[typing.Sequence[SecondaryRatUsageReport]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from fern import (
            AsyncFernApi,
            Ecgi,
            EutraLocation,
            N3GaLocation,
            Ncgi,
            NgApCause,
            NrLocation,
            PlmnId,
            QosFlowUsageReport,
            RatType,
            SecondaryRatUsageReport,
            Tai,
            UserLocation,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.individual_pdu_session_h_smf.release_pdu_session(
                pdu_session_ref="pduSessionRef",
                ng_ap_cause=NgApCause(
                    group=0,
                    value=0,
                ),
                _5g_mm_cause_value=0,
                ue_location=UserLocation(
                    eutra_location=EutraLocation(
                        tai=Tai(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            tac="tac",
                        ),
                        ecgi=Ecgi(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            eutra_cell_id="eutraCellId",
                        ),
                        age_of_location_information=2624,
                        ue_location_timestamp=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                        geographical_information="geographicalInformation",
                        geodetic_information="geodeticInformation",
                        global_ngenb_id={
                            "gNbId": {"bitLength": 28, "gNBValue": "gNBValue"},
                            "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                            "n3IwfId": "n3IwfId",
                            "ngeNbId": "ngeNbId",
                        },
                    ),
                    nr_location=NrLocation(
                        tai=Tai(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            tac="tac",
                        ),
                        ncgi=Ncgi(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            nr_cell_id="nrCellId",
                        ),
                        age_of_location_information=4803,
                        ue_location_timestamp=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                        geographical_information="geographicalInformation",
                        geodetic_information="geodeticInformation",
                        global_gnb_id={
                            "gNbId": {"bitLength": 28, "gNBValue": "gNBValue"},
                            "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                            "n3IwfId": "n3IwfId",
                            "ngeNbId": "ngeNbId",
                        },
                    ),
                    n3ga_location=N3GaLocation(
                        n3gpp_tai=Tai(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            tac="tac",
                        ),
                        n3iwf_id="n3IwfId",
                        ue_ipv4addr="198.51.100.1",
                        ue_ipv6addr="2001:db8:85a3::8a2e:370:7334",
                        port_number=0,
                    ),
                ),
                ue_time_zone="ueTimeZone",
                add_ue_location=UserLocation(
                    eutra_location=EutraLocation(
                        tai=Tai(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            tac="tac",
                        ),
                        ecgi=Ecgi(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            eutra_cell_id="eutraCellId",
                        ),
                        age_of_location_information=2624,
                        ue_location_timestamp=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                        geographical_information="geographicalInformation",
                        geodetic_information="geodeticInformation",
                        global_ngenb_id={
                            "gNbId": {"bitLength": 28, "gNBValue": "gNBValue"},
                            "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                            "n3IwfId": "n3IwfId",
                            "ngeNbId": "ngeNbId",
                        },
                    ),
                    nr_location=NrLocation(
                        tai=Tai(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            tac="tac",
                        ),
                        ncgi=Ncgi(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            nr_cell_id="nrCellId",
                        ),
                        age_of_location_information=4803,
                        ue_location_timestamp=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                        geographical_information="geographicalInformation",
                        geodetic_information="geodeticInformation",
                        global_gnb_id={
                            "gNbId": {"bitLength": 28, "gNBValue": "gNBValue"},
                            "plmnId": {"mnc": "mnc", "mcc": "mcc"},
                            "n3IwfId": "n3IwfId",
                            "ngeNbId": "ngeNbId",
                        },
                    ),
                    n3ga_location=N3GaLocation(
                        n3gpp_tai=Tai(
                            plmn_id=PlmnId(
                                mcc="mcc",
                                mnc="mnc",
                            ),
                            tac="tac",
                        ),
                        n3iwf_id="n3IwfId",
                        ue_ipv4addr="198.51.100.1",
                        ue_ipv6addr="2001:db8:85a3::8a2e:370:7334",
                        port_number=0,
                    ),
                ),
                secondary_rat_usage_report=[
                    SecondaryRatUsageReport(
                        secondary_rat_type=RatType.NR,
                        qos_flows_usage_data=[
                            QosFlowUsageReport(
                                qfi=37,
                                start_time_stamp=datetime.datetime.fromisoformat(
                                    "2024-01-15 09:30:00+00:00",
                                ),
                                end_time_stamp=datetime.datetime.fromisoformat(
                                    "2024-01-15 09:30:00+00:00",
                                ),
                                downlink_volume=1,
                                uplink_volume=5,
                            ),
                            QosFlowUsageReport(
                                qfi=37,
                                start_time_stamp=datetime.datetime.fromisoformat(
                                    "2024-01-15 09:30:00+00:00",
                                ),
                                end_time_stamp=datetime.datetime.fromisoformat(
                                    "2024-01-15 09:30:00+00:00",
                                ),
                                downlink_volume=1,
                                uplink_volume=5,
                            ),
                        ],
                    ),
                    SecondaryRatUsageReport(
                        secondary_rat_type=RatType.NR,
                        qos_flows_usage_data=[
                            QosFlowUsageReport(
                                qfi=37,
                                start_time_stamp=datetime.datetime.fromisoformat(
                                    "2024-01-15 09:30:00+00:00",
                                ),
                                end_time_stamp=datetime.datetime.fromisoformat(
                                    "2024-01-15 09:30:00+00:00",
                                ),
                                downlink_volume=1,
                                uplink_volume=5,
                            ),
                            QosFlowUsageReport(
                                qfi=37,
                                start_time_stamp=datetime.datetime.fromisoformat(
                                    "2024-01-15 09:30:00+00:00",
                                ),
                                end_time_stamp=datetime.datetime.fromisoformat(
                                    "2024-01-15 09:30:00+00:00",
                                ),
                                downlink_volume=1,
                                uplink_volume=5,
                            ),
                        ],
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.release_pdu_session(
            pdu_session_ref,
            cause=cause,
            ng_ap_cause=ng_ap_cause,
            _5g_mm_cause_value=_5g_mm_cause_value,
            ue_location=ue_location,
            ue_time_zone=ue_time_zone,
            add_ue_location=add_ue_location,
            secondary_rat_usage_report=secondary_rat_usage_report,
            request_options=request_options,
        )
        return _response.data
