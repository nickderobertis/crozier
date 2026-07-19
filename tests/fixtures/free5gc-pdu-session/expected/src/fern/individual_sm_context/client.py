

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.access_type import AccessType
from ..types.backup_amf_info import BackupAmfInfo
from ..types.cause import Cause
from ..types.eps_bearer_container import EpsBearerContainer
from ..types.eps_bearer_id import EpsBearerId
from ..types.eps_interworking_indication import EpsInterworkingIndication
from ..types.guami import Guami
from ..types.ho_state import HoState
from ..types.mme_capabilities import MmeCapabilities
from ..types.n2sm_info_type import N2SmInfoType
from ..types.ng_ap_cause import NgApCause
from ..types.plmn_id import PlmnId
from ..types.presence_state import PresenceState
from ..types.rat_type import RatType
from ..types.ref_to_binary_data import RefToBinaryData
from ..types.sm_context_retrieved_data import SmContextRetrievedData
from ..types.sm_context_updated_data import SmContextUpdatedData
from ..types.snssai import Snssai
from ..types.trace_data import TraceData
from ..types.up_cnx_state import UpCnxState
from ..types.user_location import UserLocation
from .raw_client import AsyncRawIndividualSmContextClient, RawIndividualSmContextClient


OMIT = typing.cast(typing.Any, ...)


class IndividualSmContextClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIndividualSmContextClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIndividualSmContextClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIndividualSmContextClient
        """
        return self._raw_client

    def retrieve_sm_context(
        self,
        sm_context_ref: str,
        *,
        target_mme_cap: typing.Optional[MmeCapabilities] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SmContextRetrievedData:
        """
        Parameters
        ----------
        sm_context_ref : str
            SM context reference

        target_mme_cap : typing.Optional[MmeCapabilities]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SmContextRetrievedData
            successful retrieval of an SM context

        Examples
        --------
        from fern import FernApi, MmeCapabilities

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.individual_sm_context.retrieve_sm_context(
            sm_context_ref="smContextRef",
            target_mme_cap=MmeCapabilities(
                non_ip_supported=False,
            ),
        )
        """
        _response = self._raw_client.retrieve_sm_context(
            sm_context_ref, target_mme_cap=target_mme_cap, request_options=request_options
        )
        return _response.data

    def update_sm_context(
        self,
        sm_context_ref: str,
        *,
        pei: typing.Optional[str] = OMIT,
        gpsi: typing.Optional[str] = OMIT,
        serving_nf_id: typing.Optional[str] = OMIT,
        guami: typing.Optional[Guami] = OMIT,
        serving_network: typing.Optional[PlmnId] = OMIT,
        backup_amf_info: typing.Optional[typing.Sequence[BackupAmfInfo]] = OMIT,
        an_type: typing.Optional[AccessType] = OMIT,
        rat_type: typing.Optional[RatType] = OMIT,
        presence_in_ladn: typing.Optional[PresenceState] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        up_cnx_state: typing.Optional[UpCnxState] = OMIT,
        ho_state: typing.Optional[HoState] = OMIT,
        to_be_switched: typing.Optional[bool] = OMIT,
        failed_to_be_switched: typing.Optional[bool] = OMIT,
        n1sm_msg: typing.Optional[RefToBinaryData] = OMIT,
        n2sm_info: typing.Optional[RefToBinaryData] = OMIT,
        n2sm_info_type: typing.Optional[N2SmInfoType] = OMIT,
        target_serving_nf_id: typing.Optional[str] = OMIT,
        sm_context_status_uri: typing.Optional[str] = OMIT,
        data_forwarding: typing.Optional[bool] = OMIT,
        eps_bearer_setup: typing.Optional[typing.Sequence[EpsBearerContainer]] = OMIT,
        revoke_ebi_list: typing.Optional[typing.Sequence[EpsBearerId]] = OMIT,
        release: typing.Optional[bool] = OMIT,
        cause: typing.Optional[Cause] = OMIT,
        ng_ap_cause: typing.Optional[NgApCause] = OMIT,
        _5g_mm_cause_value: typing.Optional[int] = OMIT,
        s_nssai: typing.Optional[Snssai] = OMIT,
        trace_data: typing.Optional[TraceData] = OMIT,
        eps_interworking_ind: typing.Optional[EpsInterworkingIndication] = OMIT,
        an_type_can_be_changed: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[SmContextUpdatedData]:
        """
        Parameters
        ----------
        sm_context_ref : str
            SM context reference

        pei : typing.Optional[str]

        gpsi : typing.Optional[str]

        serving_nf_id : typing.Optional[str]

        guami : typing.Optional[Guami]

        serving_network : typing.Optional[PlmnId]

        backup_amf_info : typing.Optional[typing.Sequence[BackupAmfInfo]]

        an_type : typing.Optional[AccessType]

        rat_type : typing.Optional[RatType]

        presence_in_ladn : typing.Optional[PresenceState]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        up_cnx_state : typing.Optional[UpCnxState]

        ho_state : typing.Optional[HoState]

        to_be_switched : typing.Optional[bool]

        failed_to_be_switched : typing.Optional[bool]

        n1sm_msg : typing.Optional[RefToBinaryData]

        n2sm_info : typing.Optional[RefToBinaryData]

        n2sm_info_type : typing.Optional[N2SmInfoType]

        target_serving_nf_id : typing.Optional[str]

        sm_context_status_uri : typing.Optional[str]

        data_forwarding : typing.Optional[bool]

        eps_bearer_setup : typing.Optional[typing.Sequence[EpsBearerContainer]]

        revoke_ebi_list : typing.Optional[typing.Sequence[EpsBearerId]]

        release : typing.Optional[bool]

        cause : typing.Optional[Cause]

        ng_ap_cause : typing.Optional[NgApCause]

        _5g_mm_cause_value : typing.Optional[int]

        s_nssai : typing.Optional[Snssai]

        trace_data : typing.Optional[TraceData]

        eps_interworking_ind : typing.Optional[EpsInterworkingIndication]

        an_type_can_be_changed : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[SmContextUpdatedData]
            successful update of an SM context with content in the response

        Examples
        --------
        import datetime

        from fern import (
            BackupAmfInfo,
            Ecgi,
            EutraLocation,
            FernApi,
            Guami,
            N3GaLocation,
            Ncgi,
            NgApCause,
            NrLocation,
            PlmnId,
            RefToBinaryData,
            Snssai,
            Tai,
            TraceData,
            TraceDepth,
            UserLocation,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.individual_sm_context.update_sm_context(
            sm_context_ref="smContextRef",
            pei="pei",
            gpsi="gpsi",
            serving_nf_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
            guami=Guami(
                plmn_id=PlmnId(
                    mcc="mcc",
                    mnc="mnc",
                ),
                amf_id="amfId",
            ),
            serving_network=PlmnId(
                mcc="mcc",
                mnc="mnc",
            ),
            backup_amf_info=[
                BackupAmfInfo(
                    backup_amf="backupAmf",
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
                ),
                BackupAmfInfo(
                    backup_amf="backupAmf",
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
                ),
            ],
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
            to_be_switched=False,
            failed_to_be_switched=True,
            n1sm_msg=RefToBinaryData(
                content_id="contentId",
            ),
            n2sm_info=RefToBinaryData(
                content_id="contentId",
            ),
            target_serving_nf_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
            sm_context_status_uri="smContextStatusUri",
            data_forwarding=False,
            eps_bearer_setup=["epsBearerSetup", "epsBearerSetup"],
            revoke_ebi_list=[1, 1],
            release=False,
            ng_ap_cause=NgApCause(
                group=0,
                value=0,
            ),
            f_5g_mm_cause_value=0,
            s_nssai=Snssai(
                sst=153,
                sd="sd",
            ),
            trace_data=TraceData(
                trace_ref="traceRef",
                trace_depth=TraceDepth.MINIMUM,
                ne_type_list="neTypeList",
                event_list="eventList",
                collection_entity_ipv4addr="198.51.100.1",
                collection_entity_ipv6addr="2001:db8:85a3::8a2e:370:7334",
                interface_list="interfaceList",
            ),
            an_type_can_be_changed=False,
        )
        """
        _response = self._raw_client.update_sm_context(
            sm_context_ref,
            pei=pei,
            gpsi=gpsi,
            serving_nf_id=serving_nf_id,
            guami=guami,
            serving_network=serving_network,
            backup_amf_info=backup_amf_info,
            an_type=an_type,
            rat_type=rat_type,
            presence_in_ladn=presence_in_ladn,
            ue_location=ue_location,
            ue_time_zone=ue_time_zone,
            add_ue_location=add_ue_location,
            up_cnx_state=up_cnx_state,
            ho_state=ho_state,
            to_be_switched=to_be_switched,
            failed_to_be_switched=failed_to_be_switched,
            n1sm_msg=n1sm_msg,
            n2sm_info=n2sm_info,
            n2sm_info_type=n2sm_info_type,
            target_serving_nf_id=target_serving_nf_id,
            sm_context_status_uri=sm_context_status_uri,
            data_forwarding=data_forwarding,
            eps_bearer_setup=eps_bearer_setup,
            revoke_ebi_list=revoke_ebi_list,
            release=release,
            cause=cause,
            ng_ap_cause=ng_ap_cause,
            _5g_mm_cause_value=_5g_mm_cause_value,
            s_nssai=s_nssai,
            trace_data=trace_data,
            eps_interworking_ind=eps_interworking_ind,
            an_type_can_be_changed=an_type_can_be_changed,
            request_options=request_options,
        )
        return _response.data

    def release_sm_context(
        self,
        sm_context_ref: str,
        *,
        cause: typing.Optional[Cause] = OMIT,
        ng_ap_cause: typing.Optional[NgApCause] = OMIT,
        _5g_mm_cause_value: typing.Optional[int] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        vsmf_release_only: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        sm_context_ref : str
            SM context reference

        cause : typing.Optional[Cause]

        ng_ap_cause : typing.Optional[NgApCause]

        _5g_mm_cause_value : typing.Optional[int]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        vsmf_release_only : typing.Optional[bool]

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
            Tai,
            UserLocation,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.individual_sm_context.release_sm_context(
            sm_context_ref="smContextRef",
            ng_ap_cause=NgApCause(
                group=0,
                value=0,
            ),
            f_5g_mm_cause_value=0,
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
            vsmf_release_only=False,
        )
        """
        _response = self._raw_client.release_sm_context(
            sm_context_ref,
            cause=cause,
            ng_ap_cause=ng_ap_cause,
            _5g_mm_cause_value=_5g_mm_cause_value,
            ue_location=ue_location,
            ue_time_zone=ue_time_zone,
            add_ue_location=add_ue_location,
            vsmf_release_only=vsmf_release_only,
            request_options=request_options,
        )
        return _response.data


class AsyncIndividualSmContextClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIndividualSmContextClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIndividualSmContextClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIndividualSmContextClient
        """
        return self._raw_client

    async def retrieve_sm_context(
        self,
        sm_context_ref: str,
        *,
        target_mme_cap: typing.Optional[MmeCapabilities] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SmContextRetrievedData:
        """
        Parameters
        ----------
        sm_context_ref : str
            SM context reference

        target_mme_cap : typing.Optional[MmeCapabilities]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SmContextRetrievedData
            successful retrieval of an SM context

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MmeCapabilities

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.individual_sm_context.retrieve_sm_context(
                sm_context_ref="smContextRef",
                target_mme_cap=MmeCapabilities(
                    non_ip_supported=False,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_sm_context(
            sm_context_ref, target_mme_cap=target_mme_cap, request_options=request_options
        )
        return _response.data

    async def update_sm_context(
        self,
        sm_context_ref: str,
        *,
        pei: typing.Optional[str] = OMIT,
        gpsi: typing.Optional[str] = OMIT,
        serving_nf_id: typing.Optional[str] = OMIT,
        guami: typing.Optional[Guami] = OMIT,
        serving_network: typing.Optional[PlmnId] = OMIT,
        backup_amf_info: typing.Optional[typing.Sequence[BackupAmfInfo]] = OMIT,
        an_type: typing.Optional[AccessType] = OMIT,
        rat_type: typing.Optional[RatType] = OMIT,
        presence_in_ladn: typing.Optional[PresenceState] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        up_cnx_state: typing.Optional[UpCnxState] = OMIT,
        ho_state: typing.Optional[HoState] = OMIT,
        to_be_switched: typing.Optional[bool] = OMIT,
        failed_to_be_switched: typing.Optional[bool] = OMIT,
        n1sm_msg: typing.Optional[RefToBinaryData] = OMIT,
        n2sm_info: typing.Optional[RefToBinaryData] = OMIT,
        n2sm_info_type: typing.Optional[N2SmInfoType] = OMIT,
        target_serving_nf_id: typing.Optional[str] = OMIT,
        sm_context_status_uri: typing.Optional[str] = OMIT,
        data_forwarding: typing.Optional[bool] = OMIT,
        eps_bearer_setup: typing.Optional[typing.Sequence[EpsBearerContainer]] = OMIT,
        revoke_ebi_list: typing.Optional[typing.Sequence[EpsBearerId]] = OMIT,
        release: typing.Optional[bool] = OMIT,
        cause: typing.Optional[Cause] = OMIT,
        ng_ap_cause: typing.Optional[NgApCause] = OMIT,
        _5g_mm_cause_value: typing.Optional[int] = OMIT,
        s_nssai: typing.Optional[Snssai] = OMIT,
        trace_data: typing.Optional[TraceData] = OMIT,
        eps_interworking_ind: typing.Optional[EpsInterworkingIndication] = OMIT,
        an_type_can_be_changed: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[SmContextUpdatedData]:
        """
        Parameters
        ----------
        sm_context_ref : str
            SM context reference

        pei : typing.Optional[str]

        gpsi : typing.Optional[str]

        serving_nf_id : typing.Optional[str]

        guami : typing.Optional[Guami]

        serving_network : typing.Optional[PlmnId]

        backup_amf_info : typing.Optional[typing.Sequence[BackupAmfInfo]]

        an_type : typing.Optional[AccessType]

        rat_type : typing.Optional[RatType]

        presence_in_ladn : typing.Optional[PresenceState]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        up_cnx_state : typing.Optional[UpCnxState]

        ho_state : typing.Optional[HoState]

        to_be_switched : typing.Optional[bool]

        failed_to_be_switched : typing.Optional[bool]

        n1sm_msg : typing.Optional[RefToBinaryData]

        n2sm_info : typing.Optional[RefToBinaryData]

        n2sm_info_type : typing.Optional[N2SmInfoType]

        target_serving_nf_id : typing.Optional[str]

        sm_context_status_uri : typing.Optional[str]

        data_forwarding : typing.Optional[bool]

        eps_bearer_setup : typing.Optional[typing.Sequence[EpsBearerContainer]]

        revoke_ebi_list : typing.Optional[typing.Sequence[EpsBearerId]]

        release : typing.Optional[bool]

        cause : typing.Optional[Cause]

        ng_ap_cause : typing.Optional[NgApCause]

        _5g_mm_cause_value : typing.Optional[int]

        s_nssai : typing.Optional[Snssai]

        trace_data : typing.Optional[TraceData]

        eps_interworking_ind : typing.Optional[EpsInterworkingIndication]

        an_type_can_be_changed : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[SmContextUpdatedData]
            successful update of an SM context with content in the response

        Examples
        --------
        import asyncio
        import datetime

        from fern import (
            AsyncFernApi,
            BackupAmfInfo,
            Ecgi,
            EutraLocation,
            Guami,
            N3GaLocation,
            Ncgi,
            NgApCause,
            NrLocation,
            PlmnId,
            RefToBinaryData,
            Snssai,
            Tai,
            TraceData,
            TraceDepth,
            UserLocation,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.individual_sm_context.update_sm_context(
                sm_context_ref="smContextRef",
                pei="pei",
                gpsi="gpsi",
                serving_nf_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
                guami=Guami(
                    plmn_id=PlmnId(
                        mcc="mcc",
                        mnc="mnc",
                    ),
                    amf_id="amfId",
                ),
                serving_network=PlmnId(
                    mcc="mcc",
                    mnc="mnc",
                ),
                backup_amf_info=[
                    BackupAmfInfo(
                        backup_amf="backupAmf",
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
                    ),
                    BackupAmfInfo(
                        backup_amf="backupAmf",
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
                    ),
                ],
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
                to_be_switched=False,
                failed_to_be_switched=True,
                n1sm_msg=RefToBinaryData(
                    content_id="contentId",
                ),
                n2sm_info=RefToBinaryData(
                    content_id="contentId",
                ),
                target_serving_nf_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
                sm_context_status_uri="smContextStatusUri",
                data_forwarding=False,
                eps_bearer_setup=["epsBearerSetup", "epsBearerSetup"],
                revoke_ebi_list=[1, 1],
                release=False,
                ng_ap_cause=NgApCause(
                    group=0,
                    value=0,
                ),
                f_5g_mm_cause_value=0,
                s_nssai=Snssai(
                    sst=153,
                    sd="sd",
                ),
                trace_data=TraceData(
                    trace_ref="traceRef",
                    trace_depth=TraceDepth.MINIMUM,
                    ne_type_list="neTypeList",
                    event_list="eventList",
                    collection_entity_ipv4addr="198.51.100.1",
                    collection_entity_ipv6addr="2001:db8:85a3::8a2e:370:7334",
                    interface_list="interfaceList",
                ),
                an_type_can_be_changed=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_sm_context(
            sm_context_ref,
            pei=pei,
            gpsi=gpsi,
            serving_nf_id=serving_nf_id,
            guami=guami,
            serving_network=serving_network,
            backup_amf_info=backup_amf_info,
            an_type=an_type,
            rat_type=rat_type,
            presence_in_ladn=presence_in_ladn,
            ue_location=ue_location,
            ue_time_zone=ue_time_zone,
            add_ue_location=add_ue_location,
            up_cnx_state=up_cnx_state,
            ho_state=ho_state,
            to_be_switched=to_be_switched,
            failed_to_be_switched=failed_to_be_switched,
            n1sm_msg=n1sm_msg,
            n2sm_info=n2sm_info,
            n2sm_info_type=n2sm_info_type,
            target_serving_nf_id=target_serving_nf_id,
            sm_context_status_uri=sm_context_status_uri,
            data_forwarding=data_forwarding,
            eps_bearer_setup=eps_bearer_setup,
            revoke_ebi_list=revoke_ebi_list,
            release=release,
            cause=cause,
            ng_ap_cause=ng_ap_cause,
            _5g_mm_cause_value=_5g_mm_cause_value,
            s_nssai=s_nssai,
            trace_data=trace_data,
            eps_interworking_ind=eps_interworking_ind,
            an_type_can_be_changed=an_type_can_be_changed,
            request_options=request_options,
        )
        return _response.data

    async def release_sm_context(
        self,
        sm_context_ref: str,
        *,
        cause: typing.Optional[Cause] = OMIT,
        ng_ap_cause: typing.Optional[NgApCause] = OMIT,
        _5g_mm_cause_value: typing.Optional[int] = OMIT,
        ue_location: typing.Optional[UserLocation] = OMIT,
        ue_time_zone: typing.Optional[str] = OMIT,
        add_ue_location: typing.Optional[UserLocation] = OMIT,
        vsmf_release_only: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        sm_context_ref : str
            SM context reference

        cause : typing.Optional[Cause]

        ng_ap_cause : typing.Optional[NgApCause]

        _5g_mm_cause_value : typing.Optional[int]

        ue_location : typing.Optional[UserLocation]

        ue_time_zone : typing.Optional[str]

        add_ue_location : typing.Optional[UserLocation]

        vsmf_release_only : typing.Optional[bool]

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
            Tai,
            UserLocation,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.individual_sm_context.release_sm_context(
                sm_context_ref="smContextRef",
                ng_ap_cause=NgApCause(
                    group=0,
                    value=0,
                ),
                f_5g_mm_cause_value=0,
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
                vsmf_release_only=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.release_sm_context(
            sm_context_ref,
            cause=cause,
            ng_ap_cause=ng_ap_cause,
            _5g_mm_cause_value=_5g_mm_cause_value,
            ue_location=ue_location,
            ue_time_zone=ue_time_zone,
            add_ue_location=add_ue_location,
            vsmf_release_only=vsmf_release_only,
            request_options=request_options,
        )
        return _response.data
