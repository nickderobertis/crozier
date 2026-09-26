# Reference
## NpqApplications
<details><summary><code>client.npq_applications.<a href="src/fern/npq_applications/client.py">retrieve_multiple_npq_applications</a>(...) -> ApplicationsResponse</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.npq_applications.retrieve_multiple_npq_applications()

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

**filter:** `typing.Optional[ListApplicationsFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[PaginationFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[SortingOptions]` 
    
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

<details><summary><code>client.npq_applications.<a href="src/fern/npq_applications/client.py">retrieve_a_single_npq_application</a>(...) -> ApplicationResponse</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.npq_applications.retrieve_a_single_npq_application(
    id="d0b4a32e-a272-489e-b30a-cb17131457fc",
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

**id:** `IdAttribute` 
    
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

<details><summary><code>client.npq_applications.<a href="src/fern/npq_applications/client.py">accept_an_npq_application</a>(...) -> ApplicationResponse</code></summary>
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
from fern.npq_applications import ApplicationAcceptRequestData

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.npq_applications.accept_an_npq_application(
    id="id",
    data=ApplicationAcceptRequestData(
        type="type",
        attributes={"key": "value"},
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

**id:** `IdAttribute` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `ApplicationAcceptRequestData` — A NPQ application acceptance request data
    
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

<details><summary><code>client.npq_applications.<a href="src/fern/npq_applications/client.py">reject_an_npq_application</a>(...) -> ApplicationResponse</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.npq_applications.reject_an_npq_application(
    id="d0b4a32e-a272-489e-b30a-cb17131457fc",
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

**id:** `IdAttribute` 
    
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

<details><summary><code>client.npq_applications.<a href="src/fern/npq_applications/client.py">change_funded_place_value_of_an_npq_application</a>(...) -> ApplicationResponse</code></summary>
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
from fern.npq_applications import ApplicationChangeFundedPlaceRequestData, ApplicationChangeFundedPlaceRequestDataAttributes

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.npq_applications.change_funded_place_value_of_an_npq_application(
    id="d0b4a32e-a272-489e-b30a-cb17131457fc",
    data=ApplicationChangeFundedPlaceRequestData(
        type="npq-application-change-funded-place",
        attributes=ApplicationChangeFundedPlaceRequestDataAttributes(
            funded_place=True,
        ),
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

**id:** `IdAttribute` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `ApplicationChangeFundedPlaceRequestData` — A NPQ application change funded place request data
    
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

## ParticipantDeclarations
<details><summary><code>client.participant_declarations.<a href="src/fern/participant_declarations/client.py">retrieve_multiple_participant_declarations</a>(...) -> ParticipantDeclarationsResponse</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.participant_declarations.retrieve_multiple_participant_declarations()

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

**filter:** `typing.Optional[ListParticipantDeclarationsFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[PaginationFilter]` 
    
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

<details><summary><code>client.participant_declarations.<a href="src/fern/participant_declarations/client.py">declare_a_participant_has_reached_a_milestone</a>(...) -> ParticipantDeclarationResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ParticipantDeclarationStartedRequest, ParticipantDeclarationStartedRequestDeclarationType, ParticipantDeclarationStartedRequestCourseIdentifier
from fern.environment import FernApiEnvironment
from fern.participant_declarations import ParticipantDeclarationRequestData, ParticipantDeclarationRequestDataType
import datetime

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.participant_declarations.declare_a_participant_has_reached_a_milestone(
    data=ParticipantDeclarationRequestData(
        type=ParticipantDeclarationRequestDataType.PARTICIPANT_DECLARATION,
        attributes=ParticipantDeclarationStartedRequest(
            participant_id="db3a7848-7308-4879-942a-c4a70ced400a",
            declaration_type=ParticipantDeclarationStartedRequestDeclarationType.STARTED,
            declaration_date=datetime.datetime.fromisoformat("2021-05-31T02:21:32+00:00"),
            course_identifier=ParticipantDeclarationStartedRequestCourseIdentifier.NPQ_SENIOR_LEADERSHIP,
            delivery_partner_id="524df095-f9bf-4f9d-ba4c-772545a99e60",
        ),
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

**data:** `ParticipantDeclarationRequestData` — A participant declaration data request
    
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

<details><summary><code>client.participant_declarations.<a href="src/fern/participant_declarations/client.py">retrieve_a_single_participant_declarations</a>(...) -> ParticipantDeclarationResponse</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.participant_declarations.retrieve_a_single_participant_declarations(
    id="d0b4a32e-a272-489e-b30a-cb17131457fc",
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

**id:** `IdAttribute` 
    
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

<details><summary><code>client.participant_declarations.<a href="src/fern/participant_declarations/client.py">void_a_declaration</a>(...) -> ParticipantDeclarationResponse</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.participant_declarations.void_a_declaration(
    id="d0b4a32e-a272-489e-b30a-cb17131457fc",
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

**id:** `IdAttribute` 
    
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

<details><summary><code>client.participant_declarations.<a href="src/fern/participant_declarations/client.py">change_declaration_delivery_partner</a>(...) -> ParticipantDeclarationResponse</code></summary>
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
from fern.participant_declarations import ParticipantDeclarationChangeDeliveryPartnerRequestData, ParticipantDeclarationChangeDeliveryPartnerRequestDataType, ParticipantDeclarationChangeDeliveryPartnerRequestDataAttributes

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.participant_declarations.change_declaration_delivery_partner(
    id="d0b4a32e-a272-489e-b30a-cb17131457fc",
    data=ParticipantDeclarationChangeDeliveryPartnerRequestData(
        type=ParticipantDeclarationChangeDeliveryPartnerRequestDataType.PARTICIPANT_DECLARATION,
        attributes=ParticipantDeclarationChangeDeliveryPartnerRequestDataAttributes(
            delivery_partner_id="db3a7848-7308-4879-942a-c4a70ced400a",
            secondary_delivery_partner_id="f0de7abf-399b-4e68-83de-2c33b503810c",
        ),
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

**id:** `IdAttribute` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `ParticipantDeclarationChangeDeliveryPartnerRequestData` — A participant declaration change delivery partner request
    
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

## DeliveryPartners
<details><summary><code>client.delivery_partners.<a href="src/fern/delivery_partners/client.py">retrieve_multiple_delivery_partners</a>(...) -> DeliveryPartnersResponse</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.delivery_partners.retrieve_multiple_delivery_partners()

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

**filter:** `typing.Optional[ListDeliveryPartnersFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[PaginationFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[DeliveryPartnersSortingOptions]` 
    
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

## NpqParticipantOutcomes
<details><summary><code>client.npq_participant_outcomes.<a href="src/fern/npq_participant_outcomes/client.py">retrieve_multiple_npq_outcomes_for_all_participants</a>(...) -> ParticipantOutcomesResponse</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.npq_participant_outcomes.retrieve_multiple_npq_outcomes_for_all_participants()

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

**filter:** `typing.Optional[ListParticipantOutcomesFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[PaginationFilter]` 
    
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

<details><summary><code>client.npq_participant_outcomes.<a href="src/fern/npq_participant_outcomes/client.py">retrieve_multiple_npq_outcomes_for_a_single_participant</a>(...) -> ParticipantOutcomesResponse</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.npq_participant_outcomes.retrieve_multiple_npq_outcomes_for_a_single_participant(
    id="d0b4a32e-a272-489e-b30a-cb17131457fc",
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

**id:** `IdAttribute` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[PaginationFilter]` 
    
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

<details><summary><code>client.npq_participant_outcomes.<a href="src/fern/npq_participant_outcomes/client.py">submit_a_npq_outcome_for_a_single_participant</a>(...) -> ParticipantOutcomeResponse</code></summary>
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
from fern.npq_participant_outcomes import ParticipantOutcomeCreateRequestData, ParticipantOutcomeCreateRequestDataAttributes, ParticipantOutcomeCreateRequestDataAttributesCourseIdentifier, ParticipantOutcomeCreateRequestDataAttributesState

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.npq_participant_outcomes.submit_a_npq_outcome_for_a_single_participant(
    id="d0b4a32e-a272-489e-b30a-cb17131457fc",
    data=ParticipantOutcomeCreateRequestData(
        type="npq-outcome-confirmation",
        attributes=ParticipantOutcomeCreateRequestDataAttributes(
            course_identifier=ParticipantOutcomeCreateRequestDataAttributesCourseIdentifier.NPQ_SENIOR_LEADERSHIP,
            state=ParticipantOutcomeCreateRequestDataAttributesState.PASSED,
            completion_date="2021-05-31T00:00:00+00:00",
        ),
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

**id:** `IdAttribute` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `ParticipantOutcomeCreateRequestData` — The NPQ outcome submission request attributes
    
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

## NpqParticipants
<details><summary><code>client.npq_participants.<a href="src/fern/npq_participants/client.py">retrieve_multiple_npq_participants</a>(...) -> ParticipantsResponse</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.npq_participants.retrieve_multiple_npq_participants()

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

**filter:** `typing.Optional[ListParticipantsFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[PaginationFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[SortingOptions]` 
    
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

<details><summary><code>client.npq_participants.<a href="src/fern/npq_participants/client.py">retrieve_a_single_npq_participant</a>(...) -> ParticipantResponse</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.npq_participants.retrieve_a_single_npq_participant(
    id="d0b4a32e-a272-489e-b30a-cb17131457fc",
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

**id:** `IdAttribute` 
    
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

<details><summary><code>client.npq_participants.<a href="src/fern/npq_participants/client.py">resume_an_npq_participant</a>(...) -> ParticipantResponse</code></summary>
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
from fern.npq_participants import ParticipantResumeRequestData, ParticipantResumeRequestDataAttributes, ParticipantResumeRequestDataAttributesCourseIdentifier

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.npq_participants.resume_an_npq_participant(
    id="d0b4a32e-a272-489e-b30a-cb17131457fc",
    data=ParticipantResumeRequestData(
        type="participant-resume",
        attributes=ParticipantResumeRequestDataAttributes(
            course_identifier=ParticipantResumeRequestDataAttributesCourseIdentifier.NPQ_SENIOR_LEADERSHIP,
        ),
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

**id:** `IdAttribute` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `ParticipantResumeRequestData` — A participant resume request data
    
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

<details><summary><code>client.npq_participants.<a href="src/fern/npq_participants/client.py">defer_an_npq_participant</a>(...) -> ParticipantResponse</code></summary>
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
from fern.npq_participants import ParticipantDeferRequestData, ParticipantDeferRequestDataAttributes, ParticipantDeferRequestDataAttributesCourseIdentifier, ParticipantDeferRequestDataAttributesReason

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.npq_participants.defer_an_npq_participant(
    id="d0b4a32e-a272-489e-b30a-cb17131457fc",
    data=ParticipantDeferRequestData(
        type="participant-defer",
        attributes=ParticipantDeferRequestDataAttributes(
            course_identifier=ParticipantDeferRequestDataAttributesCourseIdentifier.NPQ_SENIOR_LEADERSHIP,
            reason=ParticipantDeferRequestDataAttributesReason.BEREAVEMENT,
        ),
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

**id:** `IdAttribute` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `ParticipantDeferRequestData` — A participant defer request data
    
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

<details><summary><code>client.npq_participants.<a href="src/fern/npq_participants/client.py">withdraw_an_npq_participant</a>(...) -> ParticipantResponse</code></summary>
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
from fern.npq_participants import ParticipantWithdrawRequestData, ParticipantWithdrawRequestDataAttributes, ParticipantWithdrawRequestDataAttributesCourseIdentifier, ParticipantWithdrawRequestDataAttributesReason

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.npq_participants.withdraw_an_npq_participant(
    id="d0b4a32e-a272-489e-b30a-cb17131457fc",
    data=ParticipantWithdrawRequestData(
        type="participant-withdraw",
        attributes=ParticipantWithdrawRequestDataAttributes(
            course_identifier=ParticipantWithdrawRequestDataAttributesCourseIdentifier.NPQ_SENIOR_LEADERSHIP,
            reason=ParticipantWithdrawRequestDataAttributesReason.INSUFFICIENT_CAPACITY_TO_UNDERTAKE_PROGRAMME,
        ),
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

**id:** `IdAttribute` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `ParticipantWithdrawRequestData` — A participant withdraw request data
    
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

<details><summary><code>client.npq_participants.<a href="src/fern/npq_participants/client.py">notify_that_an_npq_participant_is_changing_training_schedule</a>(...) -> ParticipantResponse</code></summary>
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
from fern.npq_participants import ParticipantChangeScheduleRequestData, ParticipantChangeScheduleRequestDataAttributes, ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier, ParticipantChangeScheduleRequestDataAttributesCourseIdentifier

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.npq_participants.notify_that_an_npq_participant_is_changing_training_schedule(
    id="d0b4a32e-a272-489e-b30a-cb17131457fc",
    data=ParticipantChangeScheduleRequestData(
        type="participant-change-schedule",
        attributes=ParticipantChangeScheduleRequestDataAttributes(
            schedule_identifier=ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier.NPQ_ASO_MARCH,
            course_identifier=ParticipantChangeScheduleRequestDataAttributesCourseIdentifier.NPQ_SENIOR_LEADERSHIP,
        ),
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

**id:** `IdAttribute` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `ParticipantChangeScheduleRequestData` — An NPQ participant change schedule request data
    
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

## Statements
<details><summary><code>client.statements.<a href="src/fern/statements/client.py">retrieve_financial_statements</a>(...) -> StatementsResponse</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.statements.retrieve_financial_statements()

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

**filter:** `typing.Optional[ListStatementsFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[PaginationFilter]` 
    
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

<details><summary><code>client.statements.<a href="src/fern/statements/client.py">retrieve_a_specific_financial_statement</a>(...) -> StatementResponse</code></summary>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.statements.retrieve_a_specific_financial_statement(
    id="d0b4a32e-a272-489e-b30a-cb17131457fc",
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

**id:** `IdAttribute` 
    
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

