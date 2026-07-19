

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.access_type import AccessType
from ..types.dnn_selection_mode import DnnSelectionMode
from ..types.eps_bearer_id import EpsBearerId
from ..types.eps_interworking_indication import EpsInterworkingIndication
from ..types.pdu_session_created_data import PduSessionCreatedData
from ..types.plmn_id import PlmnId
from ..types.rat_type import RatType
from ..types.ref_to_binary_data import RefToBinaryData
from ..types.request_type import RequestType
from ..types.roaming_charging_profile import RoamingChargingProfile
from ..types.snssai import Snssai
from ..types.tunnel_info import TunnelInfo
from ..types.user_location import UserLocation
from .raw_client import AsyncRawPduSessionsCollectionClient, RawPduSessionsCollectionClient


OMIT = typing.cast(typing.Any, ...)


class PduSessionsCollectionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPduSessionsCollectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPduSessionsCollectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPduSessionsCollectionClient
        """
        return self._raw_client

    def post_pdu_sessions(
        self,
        *,
        dnn: str,
        vsmf_id: str,
        serving_network: PlmnId,
        vsmf_pdu_session_uri: str,
        vcn_tunnel_info: TunnelInfo,
        an_type: AccessType,
        supi: typing.Optional[str] = OMIT,
        unauthenticated_supi: typing.Optional[bool] = OMIT,
        pei: typing.Optional[str] = OMIT,
        pdu_session_id: typing.Optional[int] = OMIT,
        s_nssai: typing.Optional[Snssai] = OMIT,
        request_type: typing.Optional[RequestType] = OMIT,
        eps_bearer_id: typing.Optional[typing.Sequence[EpsBearerId]] = OMIT,
        pgw_s8c_fteid: typing.Optional[str] = OMIT,
        rat_type: typing.Optional[RatType] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        gpsi: typing.Optional[str] = OMIT,
        n1sm_info_from_ue: typing.Optional[RefToBinaryData] = OMIT,
        unknown_n1sm_info: typing.Optional[RefToBinaryData] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        h_pcf_id: typing.Optional[str] = OMIT,
        ho_preparation_indication: typing.Optional[bool] = OMIT,
        sel_mode: typing.Optional[DnnSelectionMode] = OMIT,
        always_on_requested: typing.Optional[bool] = OMIT,
        udm_group_id: typing.Optional[str] = OMIT,
        routing_indicator: typing.Optional[str] = OMIT,
        eps_interworking_ind: typing.Optional[EpsInterworkingIndication] = OMIT,
        v_smf_service_instance_id: typing.Optional[str] = OMIT,
        recovery_time: typing.Optional[dt.datetime] = OMIT,
        roaming_charging_profile: typing.Optional[RoamingChargingProfile] = OMIT,
        charging_id: typing.Optional[str] = OMIT,
        old_pdu_session_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PduSessionCreatedData:
        """
        Parameters
        ----------
        dnn : str

        vsmf_id : str

        serving_network : PlmnId

        vsmf_pdu_session_uri : str

        vcn_tunnel_info : TunnelInfo

        an_type : AccessType

        supi : typing.Optional[str]

        unauthenticated_supi : typing.Optional[bool]

        pei : typing.Optional[str]

        pdu_session_id : typing.Optional[int]

        s_nssai : typing.Optional[Snssai]

        request_type : typing.Optional[RequestType]

        eps_bearer_id : typing.Optional[typing.Sequence[EpsBearerId]]

        pgw_s8c_fteid : typing.Optional[str]

        rat_type : typing.Optional[RatType]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        gpsi : typing.Optional[str]

        n1sm_info_from_ue : typing.Optional[RefToBinaryData]

        unknown_n1sm_info : typing.Optional[RefToBinaryData]

        supported_features : typing.Optional[str]

        h_pcf_id : typing.Optional[str]

        ho_preparation_indication : typing.Optional[bool]

        sel_mode : typing.Optional[DnnSelectionMode]

        always_on_requested : typing.Optional[bool]

        udm_group_id : typing.Optional[str]

        routing_indicator : typing.Optional[str]

        eps_interworking_ind : typing.Optional[EpsInterworkingIndication]

        v_smf_service_instance_id : typing.Optional[str]

        recovery_time : typing.Optional[dt.datetime]

        roaming_charging_profile : typing.Optional[RoamingChargingProfile]

        charging_id : typing.Optional[str]

        old_pdu_session_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PduSessionCreatedData
            successful creation of a PDU session

        Examples
        --------
        import datetime

        from fern import (
            AccessType,
            Ecgi,
            EutraLocation,
            FernApi,
            N3GaLocation,
            Ncgi,
            NrLocation,
            PlmnId,
            RefToBinaryData,
            RoamingChargingProfile,
            Snssai,
            Tai,
            Trigger,
            TriggerCategory,
            TriggerType,
            TunnelInfo,
            UserLocation,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pdu_sessions_collection.post_pdu_sessions(
            supi="supi",
            unauthenticated_supi=False,
            pei="pei",
            pdu_session_id=20,
            dnn="dnn",
            s_nssai=Snssai(
                sst=153,
                sd="sd",
            ),
            vsmf_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
            serving_network=PlmnId(
                mcc="mcc",
                mnc="mnc",
            ),
            eps_bearer_id=[1, 1],
            pgw_s8c_fteid="pgwS8cFteid",
            vsmf_pdu_session_uri="vsmfPduSessionUri",
            vcn_tunnel_info=TunnelInfo(
                ipv4addr="198.51.100.1",
                ipv6addr="2001:db8:85a3::8a2e:370:7334",
                gtp_teid="gtpTeid",
            ),
            an_type=AccessType.THREE_GPP_ACCESS,
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
            gpsi="gpsi",
            n1sm_info_from_ue=RefToBinaryData(
                content_id="contentId",
            ),
            unknown_n1sm_info=RefToBinaryData(
                content_id="contentId",
            ),
            supported_features="supportedFeatures",
            h_pcf_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
            ho_preparation_indication=True,
            always_on_requested=False,
            udm_group_id="udmGroupId",
            routing_indicator="routingIndicator",
            v_smf_service_instance_id="vSmfServiceInstanceId",
            recovery_time=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            roaming_charging_profile=RoamingChargingProfile(
                triggers=[
                    Trigger(
                        trigger_type=TriggerType.QUOTA_THRESHOLD,
                        trigger_category=TriggerCategory.IMMEDIATE_REPORT,
                        time_limit=1,
                        volume_limit=0,
                        max_number_ofccc=0,
                    ),
                    Trigger(
                        trigger_type=TriggerType.QUOTA_THRESHOLD,
                        trigger_category=TriggerCategory.IMMEDIATE_REPORT,
                        time_limit=1,
                        volume_limit=0,
                        max_number_ofccc=0,
                    ),
                ],
            ),
            charging_id="chargingId",
            old_pdu_session_id=153,
        )
        """
        _response = self._raw_client.post_pdu_sessions(
            dnn=dnn,
            vsmf_id=vsmf_id,
            serving_network=serving_network,
            vsmf_pdu_session_uri=vsmf_pdu_session_uri,
            vcn_tunnel_info=vcn_tunnel_info,
            an_type=an_type,
            supi=supi,
            unauthenticated_supi=unauthenticated_supi,
            pei=pei,
            pdu_session_id=pdu_session_id,
            s_nssai=s_nssai,
            request_type=request_type,
            eps_bearer_id=eps_bearer_id,
            pgw_s8c_fteid=pgw_s8c_fteid,
            rat_type=rat_type,
            ue_location=ue_location,
            ue_time_zone=ue_time_zone,
            add_ue_location=add_ue_location,
            gpsi=gpsi,
            n1sm_info_from_ue=n1sm_info_from_ue,
            unknown_n1sm_info=unknown_n1sm_info,
            supported_features=supported_features,
            h_pcf_id=h_pcf_id,
            ho_preparation_indication=ho_preparation_indication,
            sel_mode=sel_mode,
            always_on_requested=always_on_requested,
            udm_group_id=udm_group_id,
            routing_indicator=routing_indicator,
            eps_interworking_ind=eps_interworking_ind,
            v_smf_service_instance_id=v_smf_service_instance_id,
            recovery_time=recovery_time,
            roaming_charging_profile=roaming_charging_profile,
            charging_id=charging_id,
            old_pdu_session_id=old_pdu_session_id,
            request_options=request_options,
        )
        return _response.data


class AsyncPduSessionsCollectionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPduSessionsCollectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPduSessionsCollectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPduSessionsCollectionClient
        """
        return self._raw_client

    async def post_pdu_sessions(
        self,
        *,
        dnn: str,
        vsmf_id: str,
        serving_network: PlmnId,
        vsmf_pdu_session_uri: str,
        vcn_tunnel_info: TunnelInfo,
        an_type: AccessType,
        supi: typing.Optional[str] = OMIT,
        unauthenticated_supi: typing.Optional[bool] = OMIT,
        pei: typing.Optional[str] = OMIT,
        pdu_session_id: typing.Optional[int] = OMIT,
        s_nssai: typing.Optional[Snssai] = OMIT,
        request_type: typing.Optional[RequestType] = OMIT,
        eps_bearer_id: typing.Optional[typing.Sequence[EpsBearerId]] = OMIT,
        pgw_s8c_fteid: typing.Optional[str] = OMIT,
        rat_type: typing.Optional[RatType] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        gpsi: typing.Optional[str] = OMIT,
        n1sm_info_from_ue: typing.Optional[RefToBinaryData] = OMIT,
        unknown_n1sm_info: typing.Optional[RefToBinaryData] = OMIT,
        supported_features: typing.Optional[str] = OMIT,
        h_pcf_id: typing.Optional[str] = OMIT,
        ho_preparation_indication: typing.Optional[bool] = OMIT,
        sel_mode: typing.Optional[DnnSelectionMode] = OMIT,
        always_on_requested: typing.Optional[bool] = OMIT,
        udm_group_id: typing.Optional[str] = OMIT,
        routing_indicator: typing.Optional[str] = OMIT,
        eps_interworking_ind: typing.Optional[EpsInterworkingIndication] = OMIT,
        v_smf_service_instance_id: typing.Optional[str] = OMIT,
        recovery_time: typing.Optional[dt.datetime] = OMIT,
        roaming_charging_profile: typing.Optional[RoamingChargingProfile] = OMIT,
        charging_id: typing.Optional[str] = OMIT,
        old_pdu_session_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PduSessionCreatedData:
        """
        Parameters
        ----------
        dnn : str

        vsmf_id : str

        serving_network : PlmnId

        vsmf_pdu_session_uri : str

        vcn_tunnel_info : TunnelInfo

        an_type : AccessType

        supi : typing.Optional[str]

        unauthenticated_supi : typing.Optional[bool]

        pei : typing.Optional[str]

        pdu_session_id : typing.Optional[int]

        s_nssai : typing.Optional[Snssai]

        request_type : typing.Optional[RequestType]

        eps_bearer_id : typing.Optional[typing.Sequence[EpsBearerId]]

        pgw_s8c_fteid : typing.Optional[str]

        rat_type : typing.Optional[RatType]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        gpsi : typing.Optional[str]

        n1sm_info_from_ue : typing.Optional[RefToBinaryData]

        unknown_n1sm_info : typing.Optional[RefToBinaryData]

        supported_features : typing.Optional[str]

        h_pcf_id : typing.Optional[str]

        ho_preparation_indication : typing.Optional[bool]

        sel_mode : typing.Optional[DnnSelectionMode]

        always_on_requested : typing.Optional[bool]

        udm_group_id : typing.Optional[str]

        routing_indicator : typing.Optional[str]

        eps_interworking_ind : typing.Optional[EpsInterworkingIndication]

        v_smf_service_instance_id : typing.Optional[str]

        recovery_time : typing.Optional[dt.datetime]

        roaming_charging_profile : typing.Optional[RoamingChargingProfile]

        charging_id : typing.Optional[str]

        old_pdu_session_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PduSessionCreatedData
            successful creation of a PDU session

        Examples
        --------
        import asyncio
        import datetime

        from fern import (
            AccessType,
            AsyncFernApi,
            Ecgi,
            EutraLocation,
            N3GaLocation,
            Ncgi,
            NrLocation,
            PlmnId,
            RefToBinaryData,
            RoamingChargingProfile,
            Snssai,
            Tai,
            Trigger,
            TriggerCategory,
            TriggerType,
            TunnelInfo,
            UserLocation,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pdu_sessions_collection.post_pdu_sessions(
                supi="supi",
                unauthenticated_supi=False,
                pei="pei",
                pdu_session_id=20,
                dnn="dnn",
                s_nssai=Snssai(
                    sst=153,
                    sd="sd",
                ),
                vsmf_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
                serving_network=PlmnId(
                    mcc="mcc",
                    mnc="mnc",
                ),
                eps_bearer_id=[1, 1],
                pgw_s8c_fteid="pgwS8cFteid",
                vsmf_pdu_session_uri="vsmfPduSessionUri",
                vcn_tunnel_info=TunnelInfo(
                    ipv4addr="198.51.100.1",
                    ipv6addr="2001:db8:85a3::8a2e:370:7334",
                    gtp_teid="gtpTeid",
                ),
                an_type=AccessType.THREE_GPP_ACCESS,
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
                gpsi="gpsi",
                n1sm_info_from_ue=RefToBinaryData(
                    content_id="contentId",
                ),
                unknown_n1sm_info=RefToBinaryData(
                    content_id="contentId",
                ),
                supported_features="supportedFeatures",
                h_pcf_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
                ho_preparation_indication=True,
                always_on_requested=False,
                udm_group_id="udmGroupId",
                routing_indicator="routingIndicator",
                v_smf_service_instance_id="vSmfServiceInstanceId",
                recovery_time=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                roaming_charging_profile=RoamingChargingProfile(
                    triggers=[
                        Trigger(
                            trigger_type=TriggerType.QUOTA_THRESHOLD,
                            trigger_category=TriggerCategory.IMMEDIATE_REPORT,
                            time_limit=1,
                            volume_limit=0,
                            max_number_ofccc=0,
                        ),
                        Trigger(
                            trigger_type=TriggerType.QUOTA_THRESHOLD,
                            trigger_category=TriggerCategory.IMMEDIATE_REPORT,
                            time_limit=1,
                            volume_limit=0,
                            max_number_ofccc=0,
                        ),
                    ],
                ),
                charging_id="chargingId",
                old_pdu_session_id=153,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_pdu_sessions(
            dnn=dnn,
            vsmf_id=vsmf_id,
            serving_network=serving_network,
            vsmf_pdu_session_uri=vsmf_pdu_session_uri,
            vcn_tunnel_info=vcn_tunnel_info,
            an_type=an_type,
            supi=supi,
            unauthenticated_supi=unauthenticated_supi,
            pei=pei,
            pdu_session_id=pdu_session_id,
            s_nssai=s_nssai,
            request_type=request_type,
            eps_bearer_id=eps_bearer_id,
            pgw_s8c_fteid=pgw_s8c_fteid,
            rat_type=rat_type,
            ue_location=ue_location,
            ue_time_zone=ue_time_zone,
            add_ue_location=add_ue_location,
            gpsi=gpsi,
            n1sm_info_from_ue=n1sm_info_from_ue,
            unknown_n1sm_info=unknown_n1sm_info,
            supported_features=supported_features,
            h_pcf_id=h_pcf_id,
            ho_preparation_indication=ho_preparation_indication,
            sel_mode=sel_mode,
            always_on_requested=always_on_requested,
            udm_group_id=udm_group_id,
            routing_indicator=routing_indicator,
            eps_interworking_ind=eps_interworking_ind,
            v_smf_service_instance_id=v_smf_service_instance_id,
            recovery_time=recovery_time,
            roaming_charging_profile=roaming_charging_profile,
            charging_id=charging_id,
            old_pdu_session_id=old_pdu_session_id,
            request_options=request_options,
        )
        return _response.data
