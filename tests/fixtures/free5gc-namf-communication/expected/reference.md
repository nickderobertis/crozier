# Reference
## IndividualUeContextDocument
<details><summary><code>client.individual_ue_context_document.<a href="src/fern/individual_ue_context_document/client.py">create_ue_context</a>(...) -> UeContextCreatedData</code></summary>
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

client.individual_ue_context_document.create_ue_context(
    ue_context_id="ueContextId",
    binary_data_n1message="example_binaryDataN1Message",
    binary_data_n2information="example_binaryDataN2Information",
    binary_data_n2information_ext1="example_binaryDataN2InformationExt1",
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

**ue_context_id:** `str` — UE Context Identifier
    
</dd>
</dl>

<dl>
<dd>

**json_data:** `typing.Optional[UeContextCreateData]` 
    
</dd>
</dl>

<dl>
<dd>

**binary_data_n1message:** `typing.Optional[core.File]` 
    
</dd>
</dl>

<dl>
<dd>

**binary_data_n2information:** `typing.Optional[core.File]` 
    
</dd>
</dl>

<dl>
<dd>

**binary_data_n2information_ext1:** `typing.Optional[core.File]` 
    
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

<details><summary><code>client.individual_ue_context_document.<a href="src/fern/individual_ue_context_document/client.py">release_ue_context</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, NgApCause
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.individual_ue_context_document.release_ue_context(
    ue_context_id="ueContextId",
    ngap_cause=NgApCause(
        group=0,
        value=0,
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

**ue_context_id:** `str` — UE Context Identifier
    
</dd>
</dl>

<dl>
<dd>

**ngap_cause:** `NgApCause` 
    
</dd>
</dl>

<dl>
<dd>

**supi:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**unauthenticated_supi:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.individual_ue_context_document.<a href="src/fern/individual_ue_context_document/client.py">ebi_assignment</a>(...) -> AssignedEbiData</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Arp, PreemptionCapability, PreemptionVulnerability
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
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
        )
    ],
    released_ebi_list=[
        1,
        1
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

**ue_context_id:** `str` — UE Context Identifier
    
</dd>
</dl>

<dl>
<dd>

**pdu_session_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**arp_list:** `typing.Optional[typing.List[Arp]]` 
    
</dd>
</dl>

<dl>
<dd>

**released_ebi_list:** `typing.Optional[typing.List[EpsBearerId]]` 
    
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

<details><summary><code>client.individual_ue_context_document.<a href="src/fern/individual_ue_context_document/client.py">ue_context_transfer</a>(...) -> UeContextTransferRspData</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TransferReason, AccessType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.individual_ue_context_document.ue_context_transfer(
    ue_context_id="ueContextId",
    reason=TransferReason.INIT_REG,
    access_type=AccessType.THREE_GPP_ACCESS,
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

**ue_context_id:** `str` — UE Context Identifier
    
</dd>
</dl>

<dl>
<dd>

**request:** `UeContextTransferReqData` 
    
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

<details><summary><code>client.individual_ue_context_document.<a href="src/fern/individual_ue_context_document/client.py">registration_status_update</a>(...) -> UeRegStatusUpdateRspData</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, UeContextTransferStatus
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.individual_ue_context_document.registration_status_update(
    ue_context_id="ueContextId",
    transfer_status=UeContextTransferStatus.TRANSFERRED,
    to_release_session_list=[
        1,
        1
    ],
    pcf_reselected_ind=True,
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

**ue_context_id:** `str` — UE Context Identifier
    
</dd>
</dl>

<dl>
<dd>

**transfer_status:** `UeContextTransferStatus` 
    
</dd>
</dl>

<dl>
<dd>

**to_release_session_list:** `typing.Optional[typing.List[PduSessionId]]` 
    
</dd>
</dl>

<dl>
<dd>

**pcf_reselected_ind:** `typing.Optional[bool]` 
    
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

## N1N2MessageCollectionDocument
<details><summary><code>client.n1n2message_collection_document.<a href="src/fern/n1n2message_collection_document/client.py">n1n2message_transfer</a>(...) -> N1N2MessageTransferRspData</code></summary>
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

client.n1n2message_collection_document.n1n2message_transfer(
    ue_context_id="ueContextId",
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

**ue_context_id:** `str` — UE Context Identifier
    
</dd>
</dl>

<dl>
<dd>

**request:** `N1N2MessageTransferReqData` 
    
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

## N1N2SubscriptionsCollectionForIndividualUeContextsDocument
<details><summary><code>client.n1n2subscriptions_collection_for_individual_ue_contexts_document.<a href="src/fern/n1n2subscriptions_collection_for_individual_ue_contexts_document/client.py">n1n2message_subscribe</a>(...) -> UeN1N2InfoSubscriptionCreatedData</code></summary>
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

client.n1n2subscriptions_collection_for_individual_ue_contexts_document.n1n2message_subscribe(
    ue_context_id="ueContextId",
    n2notify_callback_uri="n2NotifyCallbackUri",
    n1notify_callback_uri="n1NotifyCallbackUri",
    nf_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    supported_features="supportedFeatures",
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

**ue_context_id:** `str` — UE Context Identifier
    
</dd>
</dl>

<dl>
<dd>

**n2information_class:** `typing.Optional[N2InformationClass]` 
    
</dd>
</dl>

<dl>
<dd>

**n2notify_callback_uri:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**n1message_class:** `typing.Optional[N1MessageClass]` 
    
</dd>
</dl>

<dl>
<dd>

**n1notify_callback_uri:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**nf_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**supported_features:** `typing.Optional[str]` 
    
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

## N1N2IndividualSubscriptionDocument
<details><summary><code>client.n1n2individual_subscription_document.<a href="src/fern/n1n2individual_subscription_document/client.py">n1n2message_un_subscribe</a>(...)</code></summary>
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

client.n1n2individual_subscription_document.n1n2message_un_subscribe(
    ue_context_id="ueContextId",
    subscription_id="subscriptionId",
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

**ue_context_id:** `str` — UE Context Identifier
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `str` — Subscription Identifier
    
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

## NonUeN2MessagesCollectionDocument
<details><summary><code>client.non_ue_n2messages_collection_document.<a href="src/fern/non_ue_n2messages_collection_document/client.py">non_ue_n2message_transfer</a>(...) -> N2InformationTransferRspData</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, N2InfoContainer, N2InformationClass
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.non_ue_n2messages_collection_document.non_ue_n2message_transfer(
    n2information=N2InfoContainer(
        n2information_class=N2InformationClass.SM,
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

**request:** `N2InformationTransferReqData` 
    
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

## NonUeN2MessagesSubscriptionsCollectionDocument
<details><summary><code>client.non_ue_n2messages_subscriptions_collection_document.<a href="src/fern/non_ue_n2messages_subscriptions_collection_document/client.py">non_ue_n2info_subscribe</a>(...) -> NonUeN2InfoSubscriptionCreatedData</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AccessType, N2InformationClass
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.non_ue_n2messages_subscriptions_collection_document.non_ue_n2info_subscribe(
    global_ran_node_list=[
        {"gNbId": {"bitLength": 24, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"},
        {"gNbId": {"bitLength": 24, "gNBValue": "gNBValue"}, "plmnId": {"mnc": "mnc", "mcc": "mcc"}, "n3IwfId": "n3IwfId", "ngeNbId": "ngeNbId"}
    ],
    an_type_list=[
        AccessType.THREE_GPP_ACCESS,
        AccessType.THREE_GPP_ACCESS
    ],
    n2information_class=N2InformationClass.SM,
    n2notify_callback_uri="n2NotifyCallbackUri",
    nf_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    supported_features="supportedFeatures",
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

**n2information_class:** `N2InformationClass` 
    
</dd>
</dl>

<dl>
<dd>

**n2notify_callback_uri:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**global_ran_node_list:** `typing.Optional[typing.List[GlobalRanNodeId]]` 
    
</dd>
</dl>

<dl>
<dd>

**an_type_list:** `typing.Optional[typing.List[AccessType]]` 
    
</dd>
</dl>

<dl>
<dd>

**nf_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**supported_features:** `typing.Optional[str]` 
    
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

## NonUeN2MessageNotificationIndividualSubscriptionDocument
<details><summary><code>client.non_ue_n2message_notification_individual_subscription_document.<a href="src/fern/non_ue_n2message_notification_individual_subscription_document/client.py">non_ue_n2info_un_subscribe</a>(...)</code></summary>
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

client.non_ue_n2message_notification_individual_subscription_document.non_ue_n2info_un_subscribe(
    n2notify_subscription_id="n2NotifySubscriptionId",
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

**n2notify_subscription_id:** `str` — N2 info Subscription Identifier
    
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

## SubscriptionsCollectionDocument
<details><summary><code>client.subscriptions_collection_document.<a href="src/fern/subscriptions_collection_document/client.py">amf_status_change_subscribe</a>(...) -> SubscriptionData</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Guami, PlmnId
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
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

**request:** `SubscriptionData` 
    
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

## IndividualSubscriptionDocument
<details><summary><code>client.individual_subscription_document.<a href="src/fern/individual_subscription_document/client.py">amf_status_change_subscribe_modfy</a>(...) -> SubscriptionData</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Guami, PlmnId
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
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

**subscription_id:** `str` — AMF Status Change Subscription Identifier
    
</dd>
</dl>

<dl>
<dd>

**request:** `SubscriptionData` 
    
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

<details><summary><code>client.individual_subscription_document.<a href="src/fern/individual_subscription_document/client.py">amf_status_change_un_subscribe</a>(...)</code></summary>
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

client.individual_subscription_document.amf_status_change_un_subscribe(
    subscription_id="subscriptionId",
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

**subscription_id:** `str` — AMF Status Change Subscription Identifier
    
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

