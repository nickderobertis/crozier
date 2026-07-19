# Reference
## SmContextsCollection
<details><summary><code>client.sm_contexts_collection.<a href="src/fern/sm_contexts_collection/client.py">post_sm_contexts</a>(...) -> SmContextCreatedData</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sm_contexts_collection.post_sm_contexts(
    binary_data_n1sm_message="example_binaryDataN1SmMessage",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**json_data:** `typing.Optional[SmContextCreateData]` 
    
</dd>
</dl>

<dl>
<dd>

**binary_data_n1sm_message:** `typing.Optional[core.File]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## IndividualSmContext
<details><summary><code>client.individual_sm_context.<a href="src/fern/individual_sm_context/client.py">retrieve_sm_context</a>(...) -> SmContextRetrievedData</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, MmeCapabilities
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.individual_sm_context.retrieve_sm_context(
    sm_context_ref="smContextRef",
    target_mme_cap=MmeCapabilities(
        non_ip_supported=False,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sm_context_ref:** `str` — SM context reference
    
</dd>
</dl>

<dl>
<dd>

**target_mme_cap:** `typing.Optional[MmeCapabilities]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.individual_sm_context.<a href="src/fern/individual_sm_context/client.py">update_sm_context</a>(...) -> typing.Optional[SmContextUpdatedData]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Guami, PlmnId, BackupAmfInfo, UserLocation, EutraLocation, Tai, Ecgi, NrLocation, Ncgi, N3GaLocation, RefToBinaryData, NgApCause, Snssai, TraceData, TraceDepth
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
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
                )
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
                )
            ],
        )
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_ngenb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_gnb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_ngenb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_gnb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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
    eps_bearer_setup=[
        "epsBearerSetup",
        "epsBearerSetup"
    ],
    revoke_ebi_list=[
        1,
        1
    ],
    release=False,
    ng_ap_cause=NgApCause(
        group=0,
        value=0,
    ),
    f_value=0,
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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sm_context_ref:** `str` — SM context reference
    
</dd>
</dl>

<dl>
<dd>

**request:** `SmContextUpdateData` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.individual_sm_context.<a href="src/fern/individual_sm_context/client.py">release_sm_context</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, NgApCause, UserLocation, EutraLocation, Tai, PlmnId, Ecgi, NrLocation, Ncgi, N3GaLocation
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.individual_sm_context.release_sm_context(
    sm_context_ref="smContextRef",
    ng_ap_cause=NgApCause(
        group=0,
        value=0,
    ),
    f_value=0,
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_ngenb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_gnb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_ngenb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_gnb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sm_context_ref:** `str` — SM context reference
    
</dd>
</dl>

<dl>
<dd>

**request:** `SmContextReleaseData` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PduSessionsCollection
<details><summary><code>client.pdu_sessions_collection.<a href="src/fern/pdu_sessions_collection/client.py">post_pdu_sessions</a>(...) -> PduSessionCreatedData</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Snssai, PlmnId, TunnelInfo, AccessType, UserLocation, EutraLocation, Tai, Ecgi, NrLocation, Ncgi, N3GaLocation, RefToBinaryData, RoamingChargingProfile, Trigger, TriggerType, TriggerCategory
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
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
    eps_bearer_id=[
        1,
        1
    ],
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_ngenb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_gnb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_ngenb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_gnb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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
    recovery_time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
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
            )
        ],
    ),
    charging_id="chargingId",
    old_pdu_session_id=153,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PduSessionCreateData` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## IndividualPduSessionHSmf
<details><summary><code>client.individual_pdu_session_h_smf.<a href="src/fern/individual_pdu_session_h_smf/client.py">update_pdu_session</a>(...) -> typing.Optional[HsmfUpdatedData]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, RequestIndication, TunnelInfo, PlmnId, UserLocation, EutraLocation, Tai, Ecgi, NrLocation, Ncgi, N3GaLocation, RefToBinaryData, QosFlowItem, QosFlowNotifyItem, NotificationCause, PduSessionNotifyItem, NgApCause, SecondaryRatUsageReport, RatType, QosFlowUsageReport
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_ngenb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_gnb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_ngenb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_gnb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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
        )
    ],
    qos_flows_notify_list=[
        QosFlowNotifyItem(
            qfi=37,
            notification_cause=NotificationCause.QOS_FULFILLED,
        ),
        QosFlowNotifyItem(
            qfi=37,
            notification_cause=NotificationCause.QOS_FULFILLED,
        )
    ],
    notify_list=[
        PduSessionNotifyItem(
            notification_cause=NotificationCause.QOS_FULFILLED,
        ),
        PduSessionNotifyItem(
            notification_cause=NotificationCause.QOS_FULFILLED,
        )
    ],
    eps_bearer_id=[
        1,
        1
    ],
    ho_preparation_indication=True,
    revoke_ebi_list=[
        1,
        1
    ],
    ng_ap_cause=NgApCause(
        group=0,
        value=0,
    ),
    f_value=0,
    always_on_requested=False,
    secondary_rat_usage_report=[
        SecondaryRatUsageReport(
            secondary_rat_type=RatType.NR,
            qos_flows_usage_data=[
                QosFlowUsageReport(
                    qfi=37,
                    start_time_stamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
                    end_time_stamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
                    downlink_volume=1,
                    uplink_volume=5,
                ),
                QosFlowUsageReport(
                    qfi=37,
                    start_time_stamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
                    end_time_stamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
                    downlink_volume=1,
                    uplink_volume=5,
                )
            ],
        ),
        SecondaryRatUsageReport(
            secondary_rat_type=RatType.NR,
            qos_flows_usage_data=[
                QosFlowUsageReport(
                    qfi=37,
                    start_time_stamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
                    end_time_stamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
                    downlink_volume=1,
                    uplink_volume=5,
                ),
                QosFlowUsageReport(
                    qfi=37,
                    start_time_stamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
                    end_time_stamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
                    downlink_volume=1,
                    uplink_volume=5,
                )
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pdu_session_ref:** `str` — PDU session reference
    
</dd>
</dl>

<dl>
<dd>

**request:** `HsmfUpdateData` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.individual_pdu_session_h_smf.<a href="src/fern/individual_pdu_session_h_smf/client.py">release_pdu_session</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, NgApCause, UserLocation, EutraLocation, Tai, PlmnId, Ecgi, NrLocation, Ncgi, N3GaLocation, SecondaryRatUsageReport, RatType, QosFlowUsageReport
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.individual_pdu_session_h_smf.release_pdu_session(
    pdu_session_ref="pduSessionRef",
    ng_ap_cause=NgApCause(
        group=0,
        value=0,
    ),
    f_value=0,
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_ngenb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_gnb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_ngenb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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
            ue_location_timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            geographical_information="geographicalInformation",
            geodetic_information="geodeticInformation",
            global_gnb_id={"gNbId": {"bitLength": 28, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
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
                    start_time_stamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
                    end_time_stamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
                    downlink_volume=1,
                    uplink_volume=5,
                ),
                QosFlowUsageReport(
                    qfi=37,
                    start_time_stamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
                    end_time_stamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
                    downlink_volume=1,
                    uplink_volume=5,
                )
            ],
        ),
        SecondaryRatUsageReport(
            secondary_rat_type=RatType.NR,
            qos_flows_usage_data=[
                QosFlowUsageReport(
                    qfi=37,
                    start_time_stamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
                    end_time_stamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
                    downlink_volume=1,
                    uplink_volume=5,
                ),
                QosFlowUsageReport(
                    qfi=37,
                    start_time_stamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
                    end_time_stamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
                    downlink_volume=1,
                    uplink_volume=5,
                )
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pdu_session_ref:** `str` — PDU session reference
    
</dd>
</dl>

<dl>
<dd>

**cause:** `typing.Optional[Cause]` 
    
</dd>
</dl>

<dl>
<dd>

**ng_ap_cause:** `typing.Optional[NgApCause]` 
    
</dd>
</dl>

<dl>
<dd>

**5g_mm_cause_value:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**ue_location:** `typing.Optional[UserLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**ue_time_zone:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**add_ue_location:** `typing.Optional[UserLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**secondary_rat_usage_report:** `typing.Optional[typing.List[SecondaryRatUsageReport]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

