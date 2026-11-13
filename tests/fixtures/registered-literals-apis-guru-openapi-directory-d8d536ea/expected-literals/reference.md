# Reference
## Case Docket API
<details><summary><code>client.case_docket_api.<a href="src/fern/case_docket_api/client.py#L42-L73">get_attorney_by_id</a>(...) -> typing.Optional[Attorney]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the attorney with the specified attorneyId value.
</dd>
</dl>
</dd>
</dl>

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

client.case_docket_api.get_attorney_by_id(
    attorney_id="ATTYgu01be2e4de654",
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

**attorney_id:** `str` — Retrieve the attorney with the specified attorneyId value.
    
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

<details><summary><code>client.case_docket_api.<a href="src/fern/case_docket_api/client.py#L75-L115">get_attorney_associated_parties</a>(...) -> typing.Optional[PartyAttorneyAssociations]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the parties represented by the attorney with the specified attorneyId value.
</dd>
</dl>
</dd>
</dl>

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

client.case_docket_api.get_attorney_associated_parties(
    attorney_id="ATTYgu01be2e4de654",
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

**attorney_id:** `str` — Retrieve the parties represented by the attorney with the specified attorneyId value.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Query parameter specifying the page number of the search results to be retrieved.
    
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

<details><summary><code>client.case_docket_api.<a href="src/fern/case_docket_api/client.py#L117-L148">get_case</a>(...) -> typing.Optional[Case]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the case with the specified caseId value.
</dd>
</dl>
</dd>
</dl>

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

client.case_docket_api.get_case(
    case_id="CASEgr45196c84f3ff",
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

**case_id:** `str` — Retrieve the case with the specified caseId value.
    
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

<details><summary><code>client.case_docket_api.<a href="src/fern/case_docket_api/client.py#L150-L194">get_case_attorneys</a>(...) -> typing.Optional[Attorneys]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the attorneys in the case with the specified caseId value.
</dd>
</dl>
</dd>
</dl>

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

client.case_docket_api.get_case_attorneys(
    case_id="CASEgq5943bd47a6d2",
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

**case_id:** `str` — Retrieve the case with the specified caseId value.
    
</dd>
</dl>

<dl>
<dd>

**is_visible:** `typing.Optional[bool]` — Retrieve attorneys in the case with the specified caseId value whose isVisible flag is set to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Query parameter specifying the page number of the search results to be retrieved.
    
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

<details><summary><code>client.case_docket_api.<a href="src/fern/case_docket_api/client.py#L196-L248">get_case_docket_entries</a>(...) -> typing.Optional[DocketEntries]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the docket entries in the case with the specified caseId value.
</dd>
</dl>
</dd>
</dl>

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

client.case_docket_api.get_case_docket_entries(
    case_id="CASEgle0bf14b74a96",
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

**case_id:** `str` — Retrieve the case with the specified caseId value.
    
</dd>
</dl>

<dl>
<dd>

**docket_number:** `typing.Optional[int]` — Retrieve the docket entry witih the specified docket number in the case with the specified caseId value.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetCaseDocketEntriesRequestSortBy]` — Sort the retrieved docket entries in ascending order or descending order of date.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Query parameter specifying the page number of the search results to be retrieved.
    
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

<details><summary><code>client.case_docket_api.<a href="src/fern/case_docket_api/client.py#L250-L321">get_primary_documents_for_docket_entries</a>(...) -> typing.Optional[DocketEntryPrimaryDocuments]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the primary documents in the case with the specified caseId value.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.case_docket_api.get_primary_documents_for_docket_entries(
    case_id="CASEgued96d541f794",
    docket_number=1,
    after_first_fetch_date=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    library_date=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
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

**case_id:** `str` — Retrieve the case with the specified caseId value.
    
</dd>
</dl>

<dl>
<dd>

**docket_number:** `int` — Retrieve the primary documents associated with the specified docket number in the case with the specified caseId value.
    
</dd>
</dl>

<dl>
<dd>

**in_library:** `typing.Optional[bool]` — Retrieve the primary documents in the with the specified inLibrary flag in the case with the specified caseId value.
    
</dd>
</dl>

<dl>
<dd>

**after_first_fetch_date:** `typing.Optional[datetime.datetime]` — Retrieve all primary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.
    
</dd>
</dl>

<dl>
<dd>

**library_date:** `typing.Optional[datetime.datetime]` — Retrieve all primary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Query parameter specifying the page number of the search results to be retrieved.
    
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

<details><summary><code>client.case_docket_api.<a href="src/fern/case_docket_api/client.py#L323-L394">get_secondary_documents_for_docket_entries</a>(...) -> typing.Optional[DocketEntrySecondaryDocuments]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the secondary documents in the case with the specified caseId value.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.case_docket_api.get_secondary_documents_for_docket_entries(
    case_id="CASEgq5da86597e9a4",
    docket_number=1,
    after_first_fetch_date=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    library_date=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
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

**case_id:** `str` — Retrieve the case with the specified caseId value.
    
</dd>
</dl>

<dl>
<dd>

**docket_number:** `int` — Retrieve the secondary documents associated with the specified docket number in the case with the specified caseId value.
    
</dd>
</dl>

<dl>
<dd>

**in_library:** `typing.Optional[bool]` — Retrieve the secondary documents in the with the specified inLibrary flag in the case with the specified caseId value.
    
</dd>
</dl>

<dl>
<dd>

**after_first_fetch_date:** `typing.Optional[datetime.datetime]` — Retrieve all secondary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.
    
</dd>
</dl>

<dl>
<dd>

**library_date:** `typing.Optional[datetime.datetime]` — Retrieve all secondary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Query parameter specifying the page number of the search results to be retrieved.
    
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

<details><summary><code>client.case_docket_api.<a href="src/fern/case_docket_api/client.py#L396-L441">get_case_hearings</a>(...) -> typing.Optional[Hearings]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets Hearings for a requested Case ID.
</dd>
</dl>
</dd>
</dl>

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

client.case_docket_api.get_case_hearings(
    case_id="CASEar3c45901ef267",
    page_number=1,
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

**case_id:** `str` — Retrieve the case with the specified caseId value.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetCaseHearingsRequestSortBy]` — Specify the sort order of hearings in the case with the specified caseId.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Query parameter specifying the page number of the search results to be retrieved.
    
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

<details><summary><code>client.case_docket_api.<a href="src/fern/case_docket_api/client.py#L443-L487">get_case_judges</a>(...) -> typing.Optional[Judges]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the judges involved in the specified case.
</dd>
</dl>
</dd>
</dl>

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

client.case_docket_api.get_case_judges(
    case_id="CASEgq6e6ea66cd91d",
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

**case_id:** `str` — Retrieve the case with the specified caseId value.
    
</dd>
</dl>

<dl>
<dd>

**is_visible:** `typing.Optional[bool]` — Retrieve attorneys judges in the case with the specified caseId value whose isVisible flag is set to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Query parameter specifying the page number of the search results to be retrieved.
    
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

<details><summary><code>client.case_docket_api.<a href="src/fern/case_docket_api/client.py#L489-L559">get_case_parties</a>(...) -> typing.Optional[Parties]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the parties involved in the case with the specified caseId value.
</dd>
</dl>
</dd>
</dl>

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

client.case_docket_api.get_case_parties(
    case_id="CASEgq8f4cea2d8e1a",
    party_role_id="PTYRiMsyk7znqq5684",
    party_role_group_id="PTYGUZYzpfQ8eCm895",
    attorney_representation_type_id="ATRP2jCCwDRNaP9695",
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

**case_id:** `str` — Retrieve the case with the specified caseId value.
    
</dd>
</dl>

<dl>
<dd>

**is_visible:** `typing.Optional[bool]` — Retrieve parties in the case with the specified caseId value whose isVisible flag is set to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Query parameter specifying the page number of the search results to be retrieved.
    
</dd>
</dl>

<dl>
<dd>

**party_role_id:** `typing.Optional[str]` — Retrieve all parties with the specified partyRoleId value in the case with the specified caseId value.
    
</dd>
</dl>

<dl>
<dd>

**party_role_group_id:** `typing.Optional[str]` — Retrieve all parties with the specified partyRoleGroupId value in the case with the specified caseId value.
    
</dd>
</dl>

<dl>
<dd>

**attorney_representation_type_id:** `typing.Optional[str]` — Retrieve all parties with the specified attorneyRepresentationTypeId value in the case with the specified caseId value.
    
</dd>
</dl>

<dl>
<dd>

**party_classification_type:** `typing.Optional[GetCasePartiesRequestPartyClassificationType]` — Retrieve all parties with the specified partyClassificationType value in the case with the specified caseId value.
    
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

<details><summary><code>client.case_docket_api.<a href="src/fern/case_docket_api/client.py#L561-L601">get_case_related_cases</a>(...) -> typing.Optional[RelatedCases]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve cases that UniCourt has identified as related to the case with the specified caseId value.
</dd>
</dl>
</dd>
</dl>

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

client.case_docket_api.get_case_related_cases(
    case_id="CASEba328623913f9f",
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

**case_id:** `str` — Retrieve the case with the specified caseId value.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Query parameter specifying the page number of the search results to be retrieved.
    
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

<details><summary><code>client.case_docket_api.<a href="src/fern/case_docket_api/client.py#L603-L634">get_judge_by_id</a>(...) -> typing.Optional[Judge]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the judge with the specified judgeId value.
</dd>
</dl>
</dd>
</dl>

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

client.case_docket_api.get_judge_by_id(
    judge_id="JUDGgue04d2894de7a",
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

**judge_id:** `str` — Retrieve the judge with the specified judgeId value.
    
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

<details><summary><code>client.case_docket_api.<a href="src/fern/case_docket_api/client.py#L636-L667">get_party_by_id</a>(...) -> typing.Optional[Party]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the party with the specified partyId value.
</dd>
</dl>
</dd>
</dl>

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

client.case_docket_api.get_party_by_id(
    party_id="PRTYgla171a8952aed",
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

**party_id:** `str` — Retrieve the party with the specified partyId value.
    
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

<details><summary><code>client.case_docket_api.<a href="src/fern/case_docket_api/client.py#L669-L709">get_party_associated_attorneys</a>(...) -> typing.Optional[PartyAttorneyAssociations]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the attorneys in the case with the specified partyId value.
</dd>
</dl>
</dd>
</dl>

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

client.case_docket_api.get_party_associated_attorneys(
    party_id="PRTYgu537f3901f406",
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

**party_id:** `str` — Retrieve the party with the specified partyId value.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Query parameter specifying the page number of the search results to be retrieved.
    
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

## Usage API
<details><summary><code>client.usage_api.<a href="src/fern/usage_api/client.py#L29-L60">get_billing_usage_by_billing_cycle</a>(...) -> BillingCycleUsageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An endpoint to obtain information on API usage for a specific billing cycle.
</dd>
</dl>
</dd>
</dl>

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

client.usage_api.get_billing_usage_by_billing_cycle(
    billing_cycle="2023-01-25to2023-02-25",
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

**billing_cycle:** `str` — The date obtainable from the /billingCycles endpoint which is used as an identifier for the specific billing cycle you wish to obtain information on.
    
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

<details><summary><code>client.usage_api.<a href="src/fern/usage_api/client.py#L62-L86">get_billing_cycles</a>() -> BillingCyclesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An endpoint to obtain information on the previous 12 billing cycles.
</dd>
</dl>
</dd>
</dl>

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

client.usage_api.get_billing_cycles()

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.usage_api.<a href="src/fern/usage_api/client.py#L88-L123">get_daily_usage_by_date</a>(...) -> DailyUsageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An endpoint to obtain information on API usage for a specific day.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.usage_api.get_daily_usage_by_date(
    date=datetime.date.fromisoformat("2023-01-15"),
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

**date:** `datetime.date` — The specific date for which you wish to obtain information on API usage.
    
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

## CallbackApi
<details><summary><code>client.callback_api.<a href="src/fern/callback_api/client.py#L28-L64">get_callbacks</a>(...) -> CallbackListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get list of callback types with count for a requested Date.
</dd>
</dl>
</dd>
</dl>

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

client.callback_api.get_callbacks()

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

**date:** `typing.Optional[datetime.datetime]` — Date for which fetch the callback type list. By default, the date will be set to current date.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[GetCallbacksRequestStatus]` — Status of the callbacks. Default status will fetch all callbacks.
    
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

## Case Documents API
<details><summary><code>client.case_documents_api.<a href="src/fern/case_documents_api/client.py#L37-L115">get_case_documents</a>(...) -> typing.Optional[CaseDocuments]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets Documents for a requested Case ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.case_documents_api.get_case_documents(
    case_id="CASEgua4c06e119ea8",
    after_first_fetch_date=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    library_date=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    first_fetch_date=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
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

**case_id:** `str` — Case ID for which you want the data for.
    
</dd>
</dl>

<dl>
<dd>

**in_library:** `typing.Optional[bool]` — Filter all the documents those are added to the UniCourt library.
    
</dd>
</dl>

<dl>
<dd>

**after_first_fetch_date:** `typing.Optional[datetime.datetime]` — Get all the documents which were added to the case on or after a specific date.
    
</dd>
</dl>

<dl>
<dd>

**library_date:** `typing.Optional[datetime.datetime]` — Sort all the documents based on the date when the document was added to the UniCourt Library.
    
</dd>
</dl>

<dl>
<dd>

**first_fetch_date:** `typing.Optional[datetime.datetime]` — Sort all the documents based on the date it was fetched from the source site.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetCaseDocumentsRequestSortBy]` — Sort documents with document order.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — The page for which the result should be retrieved.
    
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

<details><summary><code>client.case_documents_api.<a href="src/fern/case_documents_api/client.py#L117-L148">get_document_by_id</a>(...) -> typing.Optional[CaseDocument]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets details for a requested Document ID.
</dd>
</dl>
</dd>
</dl>

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

client.case_documents_api.get_document_by_id(
    case_document_id="CDOCag3e5eba43b870",
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

**case_document_id:** `str` — Specific Case Dcoument ID for which you want the data for.
    
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

<details><summary><code>client.case_documents_api.<a href="src/fern/case_documents_api/client.py#L150-L190">get_case_document_download_by_id</a>(...) -> GetCaseDocumentDownloadByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets downloadable URL for a requested Document ID.
</dd>
</dl>
</dd>
</dl>

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

client.case_documents_api.get_case_document_download_by_id(
    case_document_id="CDOCaqe42a86394f63",
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

**case_document_id:** `str` — Document ID which you want to download.
    
</dd>
</dl>

<dl>
<dd>

**is_preview_document:** `typing.Optional[bool]` — If the document you want to download is a preview of a document.
    
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

<details><summary><code>client.case_documents_api.<a href="src/fern/case_documents_api/client.py#L192-L239">order_case_document</a>(...) -> CaseDocumentOrderCallback</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add Case Document Order for requested Document Ids.
</dd>
</dl>
</dd>
</dl>

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

client.case_documents_api.order_case_document(
    case_document_id="CDOCcre989d654fa05",
    is_preview_only=False,
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

**case_document_id:** `str` — Document ID which you want to order.
    
</dd>
</dl>

<dl>
<dd>

**is_preview_only:** `bool` — Flag value to determine if the document order is a preview order or no.
    
</dd>
</dl>

<dl>
<dd>

**pacer_options:** `typing.Optional[CaseDocumentOrderPacerOptions]` 
    
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

<details><summary><code>client.case_documents_api.<a href="src/fern/case_documents_api/client.py#L241-L284">get_case_document_order_callbacks</a>(...) -> CaseDocumentOrderCallbackListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Case Document Order Callback list for a requested Date.
</dd>
</dl>
</dd>
</dl>

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

client.case_documents_api.get_case_document_order_callbacks()

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

**date:** `typing.Optional[datetime.datetime]` — Date for which fetch the Case Document Order Callback list. By default, the date will be set to current date.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[GetCaseDocumentOrderCallbacksRequestStatus]` — Status of Document Order callbacks. Default status will fetch all callbacks.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

Page to fetch the Case Document Order Callback list.<br>
  - Minimum: 1
    
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

<details><summary><code>client.case_documents_api.<a href="src/fern/case_documents_api/client.py#L286-L319">get_case_document_order_callback_by_id</a>(...) -> CaseDocumentOrderCallback</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Case Document Order Callback for a requested Case Document Order Callback Id.
</dd>
</dl>
</dd>
</dl>

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

client.case_documents_api.get_case_document_order_callback_by_id(
    case_document_order_callback_id="CBDOnrb63f4808bjO3",
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

**case_document_order_callback_id:** `str` — Unique Id for the Case Document Order Callback.
    
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

## Case Analytics API
<details><summary><code>client.case_analytics_api.<a href="src/fern/case_analytics_api/client.py#L44-L114">get_case_count_analytics_by_area_of_law</a>(...) -> CaseCountAnalyticsByAreaOfLawResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Case Count Analytics by Area Of Law.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get case count grouped by Area Of Law of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.case_analytics_api.get_case_count_analytics_by_area_of_law(
    page_number=1,
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

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.case_analytics_api.<a href="src/fern/case_analytics_api/client.py#L116-L186">get_case_count_analytics_by_case_class</a>(...) -> CaseCountAnalyticsByCaseClassResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Analytics by Case Class.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed   |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get case count grouped by Case Class  of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.case_analytics_api.get_case_count_analytics_by_case_class(
    page_number=1,
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

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.case_analytics_api.<a href="src/fern/case_analytics_api/client.py#L188-L263">get_case_count_analytics_by_case_filed_date</a>(...) -> CaseCountAnalyticsByCaseFiledDateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Case Count Analytics grouped by Filing Date.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get case count grouped by case filed date of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.case_analytics_api.get_case_count_analytics_by_case_filed_date(
    page_number=1,
    group_by="Yearly",
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

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `GetCaseCountAnalyticsByCaseFiledDateRequestGroupBy` — GroupBy
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.case_analytics_api.<a href="src/fern/case_analytics_api/client.py#L265-L335">get_case_count_analytics_by_case_type</a>(...) -> CaseCountAnalyticsByCaseTypeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Case Count Analytics by Case Type.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed  |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get case count grouped by case types  of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.case_analytics_api.get_case_count_analytics_by_case_type(
    page_number=1,
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

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.case_analytics_api.<a href="src/fern/case_analytics_api/client.py#L337-L407">get_case_count_analytics_by_case_type_group</a>(...) -> CaseCountAnalyticsByCaseTypeGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Analytics by Case Type Group.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed  |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed  |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed  |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed   |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get case count grouped by case type catgeory of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.case_analytics_api.get_case_count_analytics_by_case_type_group(
    page_number=1,
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

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.case_analytics_api.<a href="src/fern/case_analytics_api/client.py#L409-L479">get_case_count_analytics_by_court</a>(...) -> CaseCountAnalyticsByCourtResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Case Count Analytics grouped by Court.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed  |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed  |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get case count grouped by Court of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.case_analytics_api.get_case_count_analytics_by_court(
    page_number=1,
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

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.case_analytics_api.<a href="src/fern/case_analytics_api/client.py#L481-L551">get_case_count_analytics_by_court_location</a>(...) -> CaseCountAnalyticsByCourtLocationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Case Count Analytics grouped by Court Location.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed  |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed  |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get case count grouped by court location  of all cases with court id CORTV4vCEaKrhystBz and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=courtId:"CORTV4vCEaKrhystBz" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.case_analytics_api.get_case_count_analytics_by_court_location(
    page_number=1,
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

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.case_analytics_api.<a href="src/fern/case_analytics_api/client.py#L553-L623">get_case_count_analytics_by_court_system</a>(...) -> CaseCountAnalyticsByCourtSystemResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Case Count Analytics grouped by Court System.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get case count grouped by court system of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.case_analytics_api.get_case_count_analytics_by_court_system(
    page_number=1,
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

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.case_analytics_api.<a href="src/fern/case_analytics_api/client.py#L625-L695">get_case_count_analytics_by_court_type</a>(...) -> CaseCountAnalyticsByCourtTypeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Case Count Analytics grouped by Court Type.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed  |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed   |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get case count grouped by court type  of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.case_analytics_api.get_case_count_analytics_by_court_type(
    page_number=1,
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

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.case_analytics_api.<a href="src/fern/case_analytics_api/client.py#L697-L767">get_case_count_analytics_by_jurisdiction_geo</a>(...) -> CaseCountAnalyticsByJurisdictionGeoResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Case Count Analytics grouped by Jurisdiction Geo.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get case count grouped by jurisdiction geo of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.case_analytics_api.get_case_count_analytics_by_jurisdiction_geo(
    page_number=1,
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

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.case_analytics_api.<a href="src/fern/case_analytics_api/client.py#L769-L839">get_case_count_analytics_by_norm_attorney</a>(...) -> CaseCountAnalyticsByNormAttorneyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns Case Analytics by Attorney.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed  |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get case count grouped by norm attorney of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.case_analytics_api.get_case_count_analytics_by_norm_attorney(
    page_number=1,
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

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.case_analytics_api.<a href="src/fern/case_analytics_api/client.py#L841-L907">get_case_count_analytics_by_norm_judge</a>(...) -> CaseCountAnalyticsByNormJudgeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns Case Analytics by Judge.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **normAttorneyId** | Multiple Ids Allowed |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normPartyId** | Multiple Ids Allowed  |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Multiple Ids Allowed  |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed  |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get case count grouped by norm judge of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.case_analytics_api.get_case_count_analytics_by_norm_judge(
    page_number=1,
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

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.case_analytics_api.<a href="src/fern/case_analytics_api/client.py#L909-L979">get_case_count_analytics_by_norm_law_firm</a>(...) -> CaseCountAnalyticsByNormLawFirmResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns Case Analytics by Norm Law Firm.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normLawFirmId** | Multiple Ids Allowed  |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed  |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get case count grouped by norm lawfirm  of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.case_analytics_api.get_case_count_analytics_by_norm_law_firm(
    page_number=1,
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

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.case_analytics_api.<a href="src/fern/case_analytics_api/client.py#L981-L1051">get_case_count_analytics_by_norm_party</a>(...) -> CaseCountAnalyticsByNormPartyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns Case Analytics by Party.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Multiple Ids Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normLawFirmId** | Multiple Ids Allowed  |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normPartyId** | Multiple Ids Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Multiple Ids Allowed  |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get case count grouped by norm party of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.case_analytics_api.get_case_count_analytics_by_norm_party(
    page_number=1,
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

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.case_analytics_api.<a href="src/fern/case_analytics_api/client.py#L1053-L1120">get_case_count_analytics_by_party_role</a>(...) -> CaseCountAnalyticsByPartyRoleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns Case Analytics by Party Type.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normPartyId** | Multiple Ids Allowed  |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get case count grouped by party role of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.case_analytics_api.get_case_count_analytics_by_party_role(
    page_number=1,
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

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.case_analytics_api.<a href="src/fern/case_analytics_api/client.py#L1122-L1189">get_case_count_analytics_by_party_role_group</a>(...) -> CaseCountAnalyticsByPartyRoleGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns Case Analytics by Party Type Group.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normPartyId** | Multiple Ids Allowed  |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get case count grouped by Party Role Group of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.case_analytics_api.get_case_count_analytics_by_party_role_group(
    page_number=1,
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

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.case_analytics_api.<a href="src/fern/case_analytics_api/client.py#L1191-L1267">get_case_count_analytics_by_opposing_norm_attorney_for_a_norm_attorney</a>(...) -> CaseCountAnalyticsByNormAttorneyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns Case Analytics by Attorney.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normPartyId** | Single Allowed  |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normLawFirmId** | Single Allowed |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Single Allowed |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDiNU45NWikKVxSH"** |
| **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get case count grouped by norm attorney with norm id NATYY29p78c7UoyJJ of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.case_analytics_api.get_case_count_analytics_by_opposing_norm_attorney_for_a_norm_attorney(
    norm_attorney_id="NATYfwmXwRHS279WPY",
    page_number=1,
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

**norm_attorney_id:** `str` 

Norm ID of Attorney. 
  - minimum: 18
  - maximum: 18
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.case_analytics_api.<a href="src/fern/case_analytics_api/client.py#L1269-L1345">get_case_count_analytics_by_opposing_norm_law_firm_for_a_norm_law_firm</a>(...) -> CaseCountAnalyticsByNormLawFirmResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns Case Analytics by Norm Law Firm.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Single Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYp7kmEQtt8jQ3eQ"** |
| **normPartyId** | Single Allowed |Find Analytics for a particular Party Object. | **normPartyId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Single Allowed  |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get case count grouped by norm lawfirm with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.case_analytics_api.get_case_count_analytics_by_opposing_norm_law_firm_for_a_norm_law_firm(
    norm_law_firm_id="NORGrPmQyLdx9NGHcT",
    page_number=1,
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

**norm_law_firm_id:** `str` 

Norm  ID of the Law Firm.
  - minimum: 18
  - maximum: 18
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.case_analytics_api.<a href="src/fern/case_analytics_api/client.py#L1347-L1423">get_case_count_analytics_by_opposing_norm_party_for_a_norm_party</a>(...) -> CaseCountAnalyticsByNormPartyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns Case Analytics by Opposing Norm Party.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **normAttorneyId** | Single Allowed  |Find Analytics for a particular norm Attorney Object. | **normAttorneyId:"NATYfwmXwRHS279WPY"** |
| **normLawFirmId** | Single Allowed |Find Analytics for a particular Norm LawFirm Object. | **normLawFirmId:"NORGrPmQyLdx9NGHcT"** |
| **normJudgeId** | Single Allowed  |Find Analytics for a particular Judge Object. | **normJudgeId:"NJUDT7jCZyFNeLGpRq"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get case count grouped by norm party with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and filed between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.case_analytics_api.get_case_count_analytics_by_opposing_norm_party_for_a_norm_party(
    norm_party_id="NORGrPmQyLdx9NGHcT",
    page_number=1,
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

**norm_party_id:** `str` 

Norm ID of the Party.
  - minimum: 18
  - maximum: 18
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

## Case Export API
<details><summary><code>client.case_export_api.<a href="src/fern/case_export_api/client.py#L29-L74">get_case_export_callbacks</a>(...) -> CaseExportCallbackListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve callbacks according to the specified criteria.
</dd>
</dl>
</dd>
</dl>

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

client.case_export_api.get_case_export_callbacks(
    page_number=1,
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

**date:** `typing.Optional[datetime.datetime]` — The date for which callbacks are to be retrieved.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[GetCaseExportCallbacksRequestStatus]` — The status code of the callbacks to be retrieved.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the callbacks to be retrieved.<br>
  - Minimum: 1
    
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

<details><summary><code>client.case_export_api.<a href="src/fern/case_export_api/client.py#L76-L109">get_case_export_callback_by_id</a>(...) -> CaseExportCallback</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified case export callback object.
</dd>
</dl>
</dd>
</dl>

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

client.case_export_api.get_case_export_callback_by_id(
    case_export_callback_id="CBCEG63f4e233eXqD1",
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

**case_export_callback_id:** `str` — The caseExportCallbackId value of the case export callback object to be retrieved.
    
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

<details><summary><code>client.case_export_api.<a href="src/fern/case_export_api/client.py#L111-L142">export_case</a>(...) -> CaseExportCallback</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve information about the specified case export.
</dd>
</dl>
</dd>
</dl>

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

client.case_export_api.export_case(
    case_id="CASEhq2c3224900a48",
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

**case_id:** `str` — The caseId value of the case for which case export information is to be retrieved.
    
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

## Case Search API
<details><summary><code>client.case_search_api.<a href="src/fern/case_search_api/client.py#L28-L139">search_cases</a>(...) -> CaseSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint retrieves cases according to keyword expressions you provide.
<br>
Keyword expressions are constructed according to the rules described below.
<br><br>
This API supports multiple use cases:
  - Search for multiple keywords  `Google OR Facebook`.
  - Search within particular attributes.
  - Relational search using terms and connectors.
  - And much more.
----

## Allowed Connectors in Keyword Expressions
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find cases containing each of the terms joined by AND connectors.|**personal AND injury**|
| **OR**  |Find cases containing any of the terms joined by OR connectors.|**order OR decision**|
| **NOT** |Find cases that do not contain the specified term.|**personal AND NOT injury**.  Find cases with the word “personal” and not “injury”.|
| **“[phrase]”** |Find the exact phrase placed between the quotation marks.|**"personal injury”**|
| **~**  |Find cases in which the specified words appear near each other. For example, "personal injury" ~ 5 targets cases in which the word "personal" appears within 5 words of the word "injury".|**“personal injury” ~ 5** - Find cases with “personal” within five words of “injury”. |
| **( … )** |Specifies the order in which connectors are to be appliied in a keyword expression.| **personal AND (injury OR fall)** - Find cases with the word personal injury or personal fall.|

<br><br>
## Fields and Connectors Searching
| Filed | Description  | Example |
| ------| ------|------|
|**caseNumber** |Find cases with the specified case number (i.e., docket number).| **caseNumber:"2020-L-007212"** - Find cases whose case number matches given case number number.|
|**caseName** |Find cases with the specified case title.| **caseName:"THOMAS P. CARNEY, INC. VS BEHLER JAMES Et Al"** - Find cases whose case name matches given terms.|
|**Court**|Find cases in the specified court.|**(Court:(name:(New York)))** - Find cases in New York state.<br>|
|**CaseStatus**|Find cases witih the specified case status.|**(CaseStatus:(name:Disposed))** - All disposed cases.<br>|
|**CaseType**|Find cases of the specified case type. | **(CaseType:(name:Property))** - Cases with case type “property”.|
|**Party** | Find cases involving the specified party.| **(Party:(name:Apple))** - Find cases involving Apple. |
|**partyId**|Find cases involving a party with the specified partyId value.|**(Party:(partyId:"PRTYgu1ffe866484c2"))**|
|**PartyRole** | Find cases in which at least one party has the specified party role. | **(Party:((PartyRole:(name:"plaintiff"))))** - Find cases with party role “plaintiff”.<br><br> **(Party:((PartyRole:(name:defendant)) AND (AttorneyRepresentationType:(name:(Attorney represented)))))** - Find cases where a party is acting as defendant and represented by an attorney.|
|**AttorneyRepresentationType**| Find cases in which at least one party has the specified attorney representation type.|**(Party:(AttorneyRepresentationType:(name:"attorney represented")))** - Find cases where a party is represented by an attorney. |
|**Attorney** | Find cases involving the specified attorney. | **(Attorney:(name:"David Boies"))** - Find cases involving the attorney David Boies. |
|**AttorneyType**|Find cases involving at least one attorney of the specified attorney type.|**(Attorney:((AttorneyType:(name:"Lead Attorney"))))**|
|**Judge** |Find cases involving the specified judge. | **(Judge:(name:"Posner"))** - Find cases involving Judge Posner.|
|**JudgeType**|Find cases involving at least one judge of the specified judge type.|**(Judge:((JudgeType:(name:"Magistrate"))))**|
|**CaseStats**|Find cases with the specified case statistics.|**(CaseStats:(partyCount:[10 TO 100]))** - Find cases involving 10 to 100 parties.<br>**(CaseStats:(attorneyCount:[2 TO 40]))** - Find cases involving 2 to 40 attorneys.<br>**(CaseStats:(judgeCount:[\* TO 2]))** - Find cases involving up to 2 judges. <br>**(CaseStats:(docketEntryCount:[10 TO 100]))** - Find cases having 10 to 100 docket_entries. <br>**(CaseStats:(allCaseDocumentCount:[10 TO 100]))** - Find cases having 10 to 100 documents. |
|**filedDate** | Find cases that were filed on the specified date or within the specified date range. | **filedDate:[2020-03-15 TO 2021-12-01]** - Find the most recently filed cases between March 15, 2020 and December 1, 2021 (inclusive). |
|**lastFetchDate**| Find cases in which UniCourt last checked for updates on the specified date or within the specified date range. |**(lastFetchDate:[now-60d TO \*\])** - Find cases that were updated by UniCourt in the last 60 days. |
|**lastFetchDateWithUpdates**|Find cases in which UniCourt last detected an update on the specified date or within the specified date range.|**(lastFetchDateWithUpdates:[now-6d TO \*\])** - Find cases for the changes found on court site in last 6 days.|
|**participantsLastFetchDate**|Find cases in which information cocnerning participants was last updated on the specified date or within the specified date range.|**(participantsLastFetchDate:[now-6d TO \*\])** - Find cases where the participant's information was updated in last 6 days.|
|**DocketEntry**|Find cases in which at least one docket entry contains the specified text.|**(DocketEntry:(text:(Motion to Compel Responses) AND docketEntryDate:[2020-01-01T00:00:00 TO 2020-05-01T00:00:00]))** - Find cases with docket text “Motion to Compel Responses” and action date between 2020-01-01 and 2020-05-01.|
|**docketEntryDate**|Find cases in which at least one docket entry was made on the specified date or within the specified date range.|**(DocketEntry:(docketEntryDate:[2020-01-01T00:00:00 TO 2020-05-01T00:00:00])) AND (CaseStats:(allCaseDocumentCount:[0 TO 10]))** - Find cases with docket action date between 2020-01-01 and 2020-05-01 having up to 10 documents associated with it.|
|**HearingDate**| Find cases with at least one hearing scheduled for the specified date or within the specified date range.|**(Hearing:(hearingDate:[now TO now+10d]))** - Find cases where hearing is scheduled in next 10 days.|
|**HearingDate**| Search for cases where hearing is going to happen in 10 to 20days.|**(Hearing:(hearingDate:[now+10d TO now+20d]))** - Find cases where hearing is scheduled in next 10 to 20 days.|
|**JurisdictionGeo**|Find cases in which the law of the specified state governs.|**(JurisdictionGeo:(state:"New York"))**- Find cases where Jurisdiction is New York state.|
|**Party Address Exists**|Find cases with Party addresses.|**(Party:(Contact:(Address:(stateName:\*))))**- Returns only those cases that have addresses for parties.|
|**Document**|Find cases with specific document name and preview is available for the document.|**(CaseDocument:(name:"civil case cover sheet" AND isPreviewAvailable:true))**- Returns cases with document civil case cover sheet and preview is available.|

<br><br>
---
## Party Sub Filter Examples
|Example |Explanation |
|---|---|
|**(Party:(name:google AND (PartyRole:(name:"plaintiff"))))**|Find cases involving at least one plaintiff whose name contains the term "Google".|
|**(Party:(name:"OTELIA PEREIDA" AND (AttorneyRepresentationType:(name:"Attorney represented")))) AND (Attorney:(name:"Law Offices of Todd M Friedman"))**|Find cases where the Party is *OTELIA PEREIDA* and is represented by the attorney *Law Offices of Todd M Friedman*.|

---
### All query parameters supported for this API can be found in below schema section. Schema -->  CaseSearchQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.case_search_api.search_cases(
    q="caseNumber:\"JP07-22-DC00026818\"",
    page_number=1,
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

**q:** `str` — Query parameter for keyword expressions.</a>
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[SearchCasesRequestSort]` — Query parameter specifying how results are to be sorted. Results can be sorted according to filedDate or relevancy.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[SearchCasesRequestOrder]` — Query parameter specifying whether search result are sorted in ascending or descending order.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

Query parameter specifying the page number of the search results to be retrieved.
- Minimum: 1
- Maximum: 1000
    
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

<details><summary><code>client.case_search_api.<a href="src/fern/case_search_api/client.py#L141-L184">search_cases_by_id</a>(...) -> CaseSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the search results corresponding to the specified caseSearchId value.
</dd>
</dl>
</dd>
</dl>

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

client.case_search_api.search_cases_by_id(
    case_search_id="CSRCU3qFUH8BjLnba5",
    page_number=1,
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

**case_search_id:** `str` — Case Search information for the given caseSearchId.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

Query parameter specifying the page number of the search results to be retrieved.
- Minimum: 1
- Maximum: 1000
    
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

## Case Tracking API
<details><summary><code>client.case_tracking_api.<a href="src/fern/case_tracking_api/client.py#L34-L78">track_case</a>(...) -> Success</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Track the specified case.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, CaseUpdateRequest, CaseTrackSchedule
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.case_tracking_api.track_case(
    case_track_params=CaseUpdateRequest(
        case_id="CASEak470fff73ba4e",
    ),
    schedule=CaseTrackSchedule(
        days=[
            1,
            3,
            5
        ],
        type="daily",
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

**case_track_params:** `CaseUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `CaseTrackSchedule` 
    
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

<details><summary><code>client.case_tracking_api.<a href="src/fern/case_tracking_api/client.py#L80-L111">get_case_track_by_id</a>(...) -> CaseTrack</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve case tracking information for the specified caseId value.
</dd>
</dl>
</dd>
</dl>

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

client.case_tracking_api.get_case_track_by_id(
    case_id="CASEak99a698ea5413",
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

**case_id:** `str` — The caseId value for which case tracking information is to be retrieved.
    
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

<details><summary><code>client.case_tracking_api.<a href="src/fern/case_tracking_api/client.py#L113-L144">remove_case_track_by_id</a>(...) -> Success</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove Case Track for a specific Case Id.
</dd>
</dl>
</dd>
</dl>

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

client.case_tracking_api.remove_case_track_by_id(
    case_id="CASEak99a698ea5413",
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

**case_id:** `str` — The caseId value for which case tracking information is to be retrieved.
    
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

<details><summary><code>client.case_tracking_api.<a href="src/fern/case_tracking_api/client.py#L146-L194">get_case_tracks</a>(...) -> CaseTrackListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of all tracked cases.
</dd>
</dl>
</dd>
</dl>

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

client.case_tracking_api.get_case_tracks(
    page_number=1,
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

**last_fetch_date:** `typing.Optional[datetime.datetime]` — The lastFetchDate value of the tracked case. The date value should be entered in the format YYYY-MM-DDTHH:MM:SS+ZZ:zz.
    
</dd>
</dl>

<dl>
<dd>

**last_fetch_date_with_updates:** `typing.Optional[datetime.datetime]` — The date on which changes were last found in the case information.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.<br>
  - Minimum: 1
    
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

## Case Update API
<details><summary><code>client.case_update_api.<a href="src/fern/case_update_api/client.py#L33-L72">update_case</a>(...) -> CaseUpdate</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Request case updates for the specified case.
</dd>
</dl>
</dd>
</dl>

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

client.case_update_api.update_case(
    case_id="CASEak99a698ea5413",
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

**request:** `CaseUpdateRequest` 
    
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

<details><summary><code>client.case_update_api.<a href="src/fern/case_update_api/client.py#L74-L105">get_case_update_by_case_id</a>(...) -> CaseUpdate</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve case updates for the specified case object.
</dd>
</dl>
</dd>
</dl>

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

client.case_update_api.get_case_update_by_case_id(
    case_id="CASEeqfb72ba4726f1",
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

**case_id:** `str` — The caseId value of the case object for which updates are to be retrieved.
    
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

<details><summary><code>client.case_update_api.<a href="src/fern/case_update_api/client.py#L107-L161">get_case_updates</a>(...) -> CaseUpdateListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve case updates for the specified date.
</dd>
</dl>
</dd>
</dl>

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

client.case_update_api.get_case_updates(
    case_id="CASEak99a698ea5413",
    page_number=1,
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

**case_id:** `typing.Optional[str]` — The caseId value of the case for which updates should be retrieved.
    
</dd>
</dl>

<dl>
<dd>

**requested_date:** `typing.Optional[datetime.datetime]` — The date for which case updates are to be retrieved.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[GetCaseUpdatesRequestStatus]` — Status of the case updates to be retrieved.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the callbacks to be retrieved.<br>
  - Minimum: 1
    
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

## Court Availability API
<details><summary><code>client.court_availability_api.<a href="src/fern/court_availability_api/client.py#L26-L57">get_court_coverage</a>(...) -> typing.Optional[CourtCoverage]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Determine whether the specified court is covered by UniCourt.
</dd>
</dl>
</dd>
</dl>

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

client.court_availability_api.get_court_coverage(
    court_id="CORTV4vCEaKrhystBz",
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

**court_id:** `str` — The courtId value of the target court.
    
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

## Authentication API
<details><summary><code>client.authentication_api.<a href="src/fern/authentication_api/client.py#L31-L68">generate_new_token</a>(...) -> AccessTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows you to generate a new access token, which is a required field for all UniCourt API endpoints except for the Authentication API. To generate a new token, you must provide your Client ID and Client Secret ID which you can find by logging into your UniCourt account. At any time, you can have a maximum of 10 active access tokens. The tokens never expire and, if you make a request which would otherwise lead to you having more than 10 active tokens, you will receive an error message.
</dd>
</dl>
</dd>
</dl>

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

client.authentication_api.generate_new_token(
    client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
    client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
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

**request:** `AccessTokenRequest` 
    
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

<details><summary><code>client.authentication_api.<a href="src/fern/authentication_api/client.py#L70-L107">invalidate_all_tokens</a>(...) -> Success</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An endpoint which allows you to invalidate all existing access tokens associated with your UniCourt account.
</dd>
</dl>
</dd>
</dl>

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

client.authentication_api.invalidate_all_tokens(
    client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
    client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
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

**request:** `AccessTokenRequest` 
    
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

<details><summary><code>client.authentication_api.<a href="src/fern/authentication_api/client.py#L109-L155">invalidate_token</a>(...) -> Success</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An endpoint which allows you to invalidate a given access token.
</dd>
</dl>
</dd>
</dl>

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

client.authentication_api.invalidate_token(
    client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
    client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
    token_id="TKID384a057WFC3Dp3",
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

**client_id:** `str` — Your Client ID obtainable by logging into your UniCourt account.
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` — Your Client Secret ID obtainable by logging into your UniCourt account.
    
</dd>
</dl>

<dl>
<dd>

**token_id:** `str` — The Token ID of token being invalidated
    
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

<details><summary><code>client.authentication_api.<a href="src/fern/authentication_api/client.py#L157-L194">list_all_token_ids</a>(...) -> AccessTokenIdListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An endpoint which allows you to view all active access tokens associated with your Client ID and Client Secret ID.
</dd>
</dl>
</dd>
</dl>

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

client.authentication_api.list_all_token_ids(
    client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
    client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
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

**request:** `AccessTokenRequest` 
    
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

## Court Standards API
<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L139-L201">get_areas_of_law</a>(...) -> AreaOfLawResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The keyword expression targeting the desired area of law. 

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> AreaOfLawQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_areas_of_law(
    q="areaOfLawId: \"AOFLGAd9Ah5qkTRNw9\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — Retrieve one or more areas of law using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetAreasOfLawRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetAreasOfLawRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L203-L234">get_area_of_law</a>(...) -> AreaOfLaw</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified area of law.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_area_of_law(
    area_of_law_id="AOFLGAd9Ah5qkTRNw9",
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

**area_of_law_id:** `str` — The areaOfLawId value of the desired area of law.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L236-L297">get_attorney_representation_types</a>(...) -> AttorneyRepresentationTypeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an attorney representation type using a keyword expression. Keyword expressions should be constructed according to the rules given above.
## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyRepresentationTypeQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_attorney_representation_types(
    q="attorneyRepresentationTypeId: \"ATRPYgPMGJufoCsR6Q\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression targeting the attorney representation type.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetAttorneyRepresentationTypesRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetAttorneyRepresentationTypesRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L299-L332">get_attorney_representation_type</a>(...) -> typing.Optional[AttorneyRepresentationType]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified attorney representation type.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_attorney_representation_type(
    attorney_representation_type_id="ATRPYgPMGJufoCsR6Q",
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

**attorney_representation_type_id:** `str` — The attorneyRepresentationTypeId value of the desired attorney representation type.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L334-L396">get_attorney_types</a>(...) -> AttorneyTypeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an attorney type using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyTypeQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_attorney_types(
    q="attorneyTypeId:\"ATYPWXtARwvzu5HLcf\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression targeting the attorney type.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetAttorneyTypesRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetAttorneyTypesRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L398-L429">get_attorney_type</a>(...) -> typing.Optional[AttorneyType]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specified attorney type object.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_attorney_type(
    attorney_type_id="ATYPWXtARwvzu5HLcf",
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

**attorney_type_id:** `str` — The attorneyTypeId value of the desired attorney type.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L431-L493">get_cases_class</a>(...) -> CaseClassResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve one or more case classes using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseClassQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_cases_class(
    q="caseClassId:\"CSCLNjbKTN7Yfo2wdb\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression targeting the desired case class.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCasesClassRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetCasesClassRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L495-L526">get_case_class</a>(...) -> CaseClass</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified case class.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_case_class(
    case_class_id="CSCLNjbKTN7Yfo2wdb",
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

**case_class_id:** `str` — The caseClassId value of the desired case class.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L528-L590">get_case_relationship_types</a>(...) -> CaseRelationshipTypeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an case relationship type using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseRelationshipTypeQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_case_relationship_types(
    q="caseRelationshipTypeId: \"CRTPgkmnzpiBXstT3s\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression targeting the case relationship type.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCaseRelationshipTypesRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetCaseRelationshipTypesRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L592-L625">get_case_relationship_type</a>(...) -> typing.Optional[CaseRelationshipType]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified case relationship type.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_case_relationship_type(
    case_relationship_type_id="CRTPgkmnzpiBXstT3s",
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

**case_relationship_type_id:** `str` — The caseRelationshipTypeId value of the desired case relationship type.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L627-L689">get_cases_status</a>(...) -> CaseStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a case status using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> CaseStatusQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_cases_status(
    q="caseStatusId: \"CSSTBtqf3R2LYFt4j4\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression targeting the desired case status.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCasesStatusRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetCasesStatusRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L691-L722">get_case_status</a>(...) -> typing.Optional[CaseStatus]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified case status.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_case_status(
    case_status_id="CSSTBtqf3R2LYFt4j4",
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

**case_status_id:** `str` — The caseStatusId value of the desired case status.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L724-L786">get_case_status_groups</a>(...) -> CaseStatusGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a case status group using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseStatusGroupQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_case_status_groups(
    q="caseStatusGroupId:\"CSSG6ERqyFdydo52WK\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression targeting the desired case status group.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCaseStatusGroupsRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetCaseStatusGroupsRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L788-L819">get_case_status_group</a>(...) -> CaseStatusGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified case status group.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_case_status_group(
    case_status_group_id="CSSG6ERqyFdydo52WK",
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

**case_status_group_id:** `str` — The caseStatusGroupId value of the desired case status group.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L821-L883">get_case_types</a>(...) -> CaseTypeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_case_types(
    q="caseTypeId: \"CTYPoLU7sWaGjWtkBx\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCaseTypesRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetCaseTypesRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L885-L916">get_case_type</a>(...) -> typing.Optional[CaseType]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified case type.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_case_type(
    case_type_id="CTYPoLU7sWaGjWtkBx",
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

**case_type_id:** `str` — The caseTypeId value of the desired case type.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L918-L980">get_case_type_groups</a>(...) -> CaseTypeGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeGroupQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_case_type_groups(
    q="caseTypeGroupId: \"CTYGSpWaVityBQndsv\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCaseTypeGroupsRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetCaseTypeGroupsRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L982-L1013">get_case_type_group</a>(...) -> CaseTypeGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified case type group.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_case_type_group(
    case_type_group_id="CTYGSpWaVityBQndsv",
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

**case_type_group_id:** `str` — caseTypeGroupId
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1015-L1077">get_causes_of_action</a>(...) -> CauseOfActionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a cause of action using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_causes_of_action(
    q="causeOfActionId:\"CATNiHoKn66p3bkcNs\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression targeting the desired cause of action.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCausesOfActionRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetCausesOfActionRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1079-L1110">get_cause_of_action</a>(...) -> typing.Optional[CauseOfAction]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified cause of action.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_cause_of_action(
    cause_of_action_id="CATNoLU7sWaGjWtkBx",
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

**cause_of_action_id:** `str` — The causeOfActionId value of the desired cause of action.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1112-L1174">get_causes_of_action_additional_data</a>(...) -> CauseOfActionAdditionalDataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a cause of action additional data using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionAdditionalDataQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_causes_of_action_additional_data(
    q="causeOfActionAdditionalDataId:\"CAADiHoKn66p3bkcNs\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression targeting the desired cause of action additional data.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCausesOfActionAdditionalDataRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetCausesOfActionAdditionalDataRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1176-L1209">get_cause_of_action_additional_data</a>(...) -> CauseOfActionAdditionalData</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified cause of action additional data.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_cause_of_action_additional_data(
    cause_of_action_additional_data_id="CAADoLU7sWaGjWtkBx",
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

**cause_of_action_additional_data_id:** `str` — The causeOfActionAdditionalDataId value of the desired cause of action additional data.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1211-L1273">get_causes_of_action_group</a>(...) -> CauseOfActionGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a cause of action group using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionGroupQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_causes_of_action_group(
    q="causeOfActionGroupId:\"CAGPiHoKn66p3bkcNs\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression targeting the desired cause of action group.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCausesOfActionGroupRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetCausesOfActionGroupRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1275-L1308">get_cause_of_action_group</a>(...) -> CauseOfActionGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified cause of action group.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_cause_of_action_group(
    cause_of_action_group_id="CAGPoLU7sWaGjWtkBx",
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

**cause_of_action_group_id:** `str` — causeOfActionGroupId
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1310-L1372">get_charges</a>(...) -> ChargeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve one or more charges using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_charges(
    q="chargeId:\"CHRGoLU7sWaGjWtkBx\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression targeting the desired charge.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetChargesRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetChargesRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1374-L1405">get_charge</a>(...) -> typing.Optional[Charge]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified charge.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_charge(
    charge_id="CHRGiHoKn66p3bkcNs",
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

**charge_id:** `str` — The chargeId value of the desired charge.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1407-L1469">get_charges_additional_data</a>(...) -> ChargeAdditionalDataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve additional information on a charge using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeAdditionalDataQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_charges_additional_data(
    q="chargeAdditionalDataId:\"CHADoLU7sWaGjWtkBx\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression targeting the desired charge additional data.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetChargesAdditionalDataRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetChargesAdditionalDataRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1471-L1504">get_charge_additional_data</a>(...) -> ChargeAdditionalData</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified charge additional data.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_charge_additional_data(
    charge_additional_data_id="CHADiHoKn66p3bkcNs",
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

**charge_additional_data_id:** `str` — The chargeAdditionalDataId value of the desired charge additional data.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1506-L1568">get_charges_degree</a>(...) -> ChargeDegreeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a charge degree using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeDegreeQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_charges_degree(
    q="chargeDegreeId:\"CHDGiHoKn66p3bkcNs\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression targeting the desired charge degree.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetChargesDegreeRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetChargesDegreeRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1570-L1601">get_charge_degree</a>(...) -> typing.Optional[ChargeDegree]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified charge degree.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_charge_degree(
    charge_degree_id="CHDGiHoKn66p3bkcNs",
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

**charge_degree_id:** `str` — The chargeDegreeId value of the desired charge degree.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1603-L1665">get_charge_groups</a>(...) -> ChargeGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve one or more charge groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeGroupQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_charge_groups(
    q="chargeGroupId:\"CHRGoLU7sWaGjWtkBx\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression targeting the desired charge group.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetChargeGroupsRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetChargeGroupsRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1667-L1698">get_charge_group</a>(...) -> ChargeGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified charge group.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_charge_group(
    charge_group_id="CHGPiHoKn66p3bkcNs",
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

**charge_group_id:** `str` — The chargeGroupId value of the desired charge group.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1700-L1762">get_charges_severity</a>(...) -> ChargeSeverityResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a charge severity using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeSeverityQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_charges_severity(
    q="chargeSeverityId:\"CHSEiHoKn66p3bkcNs\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression targeting the desired charge severity.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetChargesSeverityRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetChargesSeverityRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1764-L1795">get_charge_severity</a>(...) -> typing.Optional[ChargeSeverity]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified charge severity.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_charge_severity(
    charge_severity_id="CHSEiHoKn66p3bkcNs",
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

**charge_severity_id:** `str` — The chargeSeverityId value of the desired charge severity.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1797-L1859">get_courts</a>(...) -> CourtResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve information about a specified court or courts.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_courts(
    q="courtId:\"CORThSxcef8eGUSkuC\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression that sets forth the criteria concerning the court or courts to be retrieved. Keyword expressions should be constructed according to the rules shown above.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCourtsRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetCourtsRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1861-L1892">get_court</a>(...) -> typing.Optional[Court]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve information about a specified court.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_court(
    court_id="CORThSxcef8eGUSkuC",
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

**court_id:** `str` — The courtId value of the target court.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1894-L1945">get_appeal_courts_for_court</a>(...) -> CourtResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the appeals courts associated with the specified court.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_appeal_courts_for_court(
    court_id="CORThSxcef8eGUSkuC",
    page_number=1,
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

**court_id:** `str` — The courtId value of the target court.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetAppealCourtsForCourtRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetAppealCourtsForCourtRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L1947-L1998">get_court_locations_for_court</a>(...) -> CourtLocationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the court locations associated with the specified court.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_court_locations_for_court(
    court_id="CORThSxcef8eGUSkuC",
    page_number=1,
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

**court_id:** `str` — The courtId value of the target court.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCourtLocationsForCourtRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetCourtLocationsForCourtRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L2000-L2051">get_jurisdiction_geo_for_court</a>(...) -> JurisdictionGeoResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the jurisdiction geography object for the specified court.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_jurisdiction_geo_for_court(
    court_id="CORThSxcef8eGUSkuC",
    page_number=1,
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

**court_id:** `str` — The courtId value of the target court.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetJurisdictionGeoForCourtRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetJurisdictionGeoForCourtRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L2053-L2115">get_court_locations</a>(...) -> CourtLocationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified court location or court locations.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtLocationQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_court_locations(
    q="courtLocationId:\"COLO9g3fhYM4bmxveA\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression that sets forth the criteria concerning the court location or court locations to target. Keyword expressions should be constructed according to the rules shown above.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCourtLocationsRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetCourtLocationsRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L2117-L2148">get_court_location</a>(...) -> typing.Optional[CourtLocation]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Contains the Court Location Object.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_court_location(
    court_location_id="COLOV75AKgqMqnfVhM",
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

**court_location_id:** `str` — courtLocationId
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L2150-L2201">get_courts_for_court_location</a>(...) -> CourtResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the courts associated with the specified court location.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_courts_for_court_location(
    court_location_id="COLOV75AKgqMqnfVhM",
    page_number=1,
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

**court_location_id:** `str` — The courtLocationId value of the court location for which courts are to be retrieved.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCourtsForCourtLocationRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetCourtsForCourtLocationRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L2203-L2265">get_courts_service_status</a>(...) -> CourtServiceStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the status of one or more courts using a keyword expression.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtServiceStatusQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_courts_service_status(
    q="courtServiceStatusId: \"CTSSf45fd1bd792e97\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression targeting the desired court. Keyword expressions should be constructed according to the rules given above.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCourtsServiceStatusRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetCourtsServiceStatusRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L2267-L2298">get_court_service_status</a>(...) -> typing.Optional[CourtServiceStatus]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the court status of the specified court.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_court_service_status(
    court_service_status_id="CTSSf45fd1bd792e97",
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

**court_service_status_id:** `str` — The courtServiceStatusId value of the desired court.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L2300-L2362">get_court_systems</a>(...) -> CourtSystemResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve information about the specified court system or court systems.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtSystemQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_court_systems(
    q="courtSystemId:\"COSY4vuCtGQeAmdDdN\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression that sets forth the criteria concerning the court system or court systems. Keyword expressions should be constructed according to the rules shown above.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCourtSystemsRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetCourtSystemsRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L2364-L2395">get_court_system</a>(...) -> CourtSystem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified court system.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_court_system(
    court_system_id="COSY4vuCtGQeAmdDdN",
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

**court_system_id:** `str` — The courtSystemId value of the court system to be retrieved.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L2397-L2459">get_court_types</a>(...) -> CourtTypeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve court types recognized by UniCourt.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtTypeQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_court_types(
    q="courtTypeId:\"COTPm8jjc2PAydpFhq\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression that sets forth the criteria concerning the court type or court types. Keyword expressions should be constructed according to the rules shown above.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCourtTypesRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetCourtTypesRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L2461-L2492">get_court_type</a>(...) -> CourtType</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the information concerning the specific court type.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_court_type(
    court_type_id="COTPm8jjc2PAydpFhq",
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

**court_type_id:** `str` — The courtTypeId value of the court type to be retrieved.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L2494-L2556">get_judge_types</a>(...) -> JudgeTypeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a judge type using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> JudgeTypeQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_judge_types(
    q="judgeTypeId: \"JGTPkwrfzkDJUvxpN9\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression targeting the judge type.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetJudgeTypesRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetJudgeTypesRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L2558-L2589">get_judge_type</a>(...) -> typing.Optional[JudgeType]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified judge type.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_judge_type(
    judge_type_id="JGTPkwrfzkDJUvxpN9",
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

**judge_type_id:** `str` — The judgeTypeId of the desired judge type.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L2591-L2653">get_jurisdictions_geo</a>(...) -> JurisdictionGeoResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve one or more jurisdiction geographies using a keyword expression.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> JurisdictionGeoQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_jurisdictions_geo(
    q="jurisdictionGeoId:\"JUGO8s7HvM84dLvVMu\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression targeting the desired jurisdiction geography. Keyword expressions should be constructed according to the rules given above.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetJurisdictionsGeoRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetJurisdictionsGeoRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L2655-L2686">get_jurisdiction_geo</a>(...) -> JurisdictionGeo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified jurisdiction geography.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_jurisdiction_geo(
    jurisdiction_geo_id="JUGO8s7HvM84dLvVMu",
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

**jurisdiction_geo_id:** `str` — The jurisdictionGeoId value of the desired jurisdiction geography.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L2688-L2739">get_courts_for_jurisdiction_geo</a>(...) -> CourtResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns Associated Court for given Jurisdiction Geo.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_courts_for_jurisdiction_geo(
    jurisdiction_geo_id="JUGO8s7HvM84dLvVMu",
    page_number=1,
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

**jurisdiction_geo_id:** `str` — jurisdictionGeoId
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

Page number.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetCourtsForJurisdictionGeoRequestSort]` — Sort field.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetCourtsForJurisdictionGeoRequestOrder]` — Sort order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L2741-L2803">get_party_roles</a>(...) -> PartyRoleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a party role using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_party_roles(
    q="partyRoleId: \"PTYRVRgMKueGmhnxRN\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression targeting the desired party role.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetPartyRolesRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetPartyRolesRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L2805-L2836">get_party_role</a>(...) -> typing.Optional[PartyRole]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified party role.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_party_role(
    party_role_id="PTYRVRgMKueGmhnxRN",
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

**party_role_id:** `str` — The partyRoleId value of the desired party role.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L2838-L2900">get_party_role_groups</a>(...) -> PartyRoleGroupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a party role group using a keyword expression. Keyword expressions should be constructed according to the rules given above.

## Logical Operators
| Connector | Description  | Example |
| ------| ------|------|
| **AND** |Find data containing all connected terms.|**google AND facebook**|
| **OR**  |Find data containing any connected term.| **order OR decision**|
| **NOT** |Exclude data.| **google NOT apple**.|
| **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
| **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

### All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleGroupQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_party_role_groups(
    q="partyRoleGroupId: \"PTYGBnjxbx6tKNfVEP\"",
    page_number=1,
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

**q:** `typing.Optional[str]` — The keyword expression targeting the desired party role group.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

The page number of the results to be retrieved.
- minimum: 1
- maximum: 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetPartyRoleGroupsRequestSort]` — The field according to which search results are to be sorted.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetPartyRoleGroupsRequestOrder]` — Whether search results are to be shown in ascending or descending order.
    
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

<details><summary><code>client.court_standards_api.<a href="src/fern/court_standards_api/client.py#L2902-L2933">get_party_role_group</a>(...) -> PartyRoleGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the specified party role group.
</dd>
</dl>
</dd>
</dl>

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

client.court_standards_api.get_party_role_group(
    party_role_group_id="PTYGBnjxbx6tKNfVEP",
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

**party_role_group_id:** `str` — The partyRoleGroupId value of the desired party role group.
    
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

## Attorney Analytics API
<details><summary><code>client.attorney_analytics_api.<a href="src/fern/attorney_analytics_api/client.py#L30-L63">get_norm_attorney_by_id</a>(...) -> NormAttorney</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint retrieves information on the attorney in our normalized attorney database which matches the normAttorneyId specified in the request.
</dd>
</dl>
</dd>
</dl>

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

client.attorney_analytics_api.get_norm_attorney_by_id(
    norm_attorney_id="NATYs4P6kDBkhKL8CF",
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

**norm_attorney_id:** `str` 

Norm ID of Attorney. 
  - minimum: 18
  - maximum: 18
    
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

<details><summary><code>client.attorney_analytics_api.<a href="src/fern/attorney_analytics_api/client.py#L65-L135">get_norm_judges_associated_with_norm_attorney</a>(...) -> AssociatedNormJudgeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint returns information on all judges which have appeared in cases with the attorney specified by the normAttorneyId. The returned judges are ordered in descending order of number of cases shared with the relevant attorney.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz"  AND  courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz", "CORTKQiA4LJuv54tEj")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get all judges associated with attorney with norm id NATYfwmXwRHS279WPY of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>
</dd>
</dl>
</dd>
</dl>

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

client.attorney_analytics_api.get_norm_judges_associated_with_norm_attorney(
    norm_attorney_id="NATYfwmXwRHS279WPY",
    page_number=1,
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

**norm_attorney_id:** `str` 

Norm ID of Attorney. 
  - minimum: 18
  - maximum: 18
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.attorney_analytics_api.<a href="src/fern/attorney_analytics_api/client.py#L137-L211">get_norm_law_firms_associated_with_norm_attorney</a>(...) -> AssociatedNormLawFirmResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of Law Firms the norm Attorney has worked for.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz"  AND  courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz", "CORTKQiA4LJuv54tEj")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get all LawFirms associated with attorney with norm id NATYfwmXwRHS279WPY of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>
</dd>
</dl>
</dd>
</dl>

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

client.attorney_analytics_api.get_norm_law_firms_associated_with_norm_attorney(
    norm_attorney_id="NATYfwmXwRHS279WPY",
    page_number=1,
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

**norm_attorney_id:** `str` 

Norm ID of Attorney. 
  - minimum: 18
  - maximum: 18
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.attorney_analytics_api.<a href="src/fern/attorney_analytics_api/client.py#L213-L288">get_norm_parties_associated_with_norm_attorney</a>(...) -> AssociatedNormPartyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of Parties the Attorney has represented.
<br><br>
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz"  AND  courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz", "CORTKQiA4LJuv54tEj")**|
| **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Group Object.. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **caseFiledDate** | Single Allowed   |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get all parties associated with attorney with norm id NATYfwmXwRHS279WPY of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>
</dd>
</dl>
</dd>
</dl>

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

client.attorney_analytics_api.get_norm_parties_associated_with_norm_attorney(
    norm_attorney_id="NATYfwmXwRHS279WPY",
    page_number=1,
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

**norm_attorney_id:** `str` 

Norm ID of Attorney. 
  - minimum: 18
  - maximum: 18
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.attorney_analytics_api.<a href="src/fern/attorney_analytics_api/client.py#L290-L334">search_normalized_attorneys</a>(...) -> NormAttorneySearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

### This endpoint retrieves information, including the normAttorneyId, on all attorneys in our normalized attorney database which match the request parameters. All query parameters supported by this API can be found in the schema section below.
</dd>
</dl>
</dd>
</dl>

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

client.attorney_analytics_api.search_normalized_attorneys(
    q="normAttorneyId:\"NATYhUvNaef3b2iP8D\"",
    page_number=1,
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

**q:** `typing.Optional[str]` 

The URL encoded query you are searching for.
The query can be as simple as a keyword, but supports many additional options and filters.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

Query parameter specifying the page number of the search results to be retrieved.
- Minimum: 1
- Maximum: 1000
    
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

<details><summary><code>client.attorney_analytics_api.<a href="src/fern/attorney_analytics_api/client.py#L336-L379">search_normalized_attorneys_by_id</a>(...) -> NormAttorneySearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

### All query parameters supported for this API can be found in below schema section. Schema --> NormAttorneySearchQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.attorney_analytics_api.search_normalized_attorneys_by_id(
    norm_attorney_search_id="ASRCJxUHYsgddr4Hc5",
    page_number=1,
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

**norm_attorney_search_id:** `str` — Norm Attorney Search information for the given normAttorneySearchId.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

Query parameter specifying the page number of the search results to be retrieved.
- Minimum: 1
- Maximum: 1000
    
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

## Judge Analytics API
<details><summary><code>client.judge_analytics_api.<a href="src/fern/judge_analytics_api/client.py#L30-L63">get_norm_judge_by_id</a>(...) -> NormJudge</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Judge API allows you to look up Judge Details by normJudgeId.
</dd>
</dl>
</dd>
</dl>

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

client.judge_analytics_api.get_norm_judge_by_id(
    norm_judge_id="NJUDT7jCZyFNeLGpRq",
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

**norm_judge_id:** `str` 

Norm  ID of the Judge.
  - minimum: 18
  - maximum: 18
    
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

<details><summary><code>client.judge_analytics_api.<a href="src/fern/judge_analytics_api/client.py#L65-L135">get_norm_attorneys_associated_with_norm_judge</a>(...) -> AssociatedNormAttorneyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of attorneys associated with a judge.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtLocationId IN ("COLODj4BBVTho3pKpz","COLOPUfJRhw5yPxgRi")**|
| **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get all attorneys associated with judge with norm id NJUDT7jCZyFNeLGpRq of all cases with case type id CTYPATMYyaJekdgj2c and case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>
</dd>
</dl>
</dd>
</dl>

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

client.judge_analytics_api.get_norm_attorneys_associated_with_norm_judge(
    norm_judge_id="NJUDT7jCZyFNeLGpRq",
    page_number=1,
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

**norm_judge_id:** `str` 

Norm  ID of the Judge.
  - minimum: 18
  - maximum: 18
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.judge_analytics_api.<a href="src/fern/judge_analytics_api/client.py#L137-L207">get_norm_law_firms_associated_with_norm_judge</a>(...) -> AssociatedNormLawFirmResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of Law Firms a Judge has heard.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLOPUfJRhw5yPxgRi"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtLocationId IN ("COLODj4BBVTho3pKpz","COLOPUfJRhw5yPxgRi")**|
| **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo**  | Multiple Ids Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get all Law Firms associated with judge with norm id NJUDT7jCZyFNeLGpRq of all cases with case type id CTYPATMYyaJekdgj2c and case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>
</dd>
</dl>
</dd>
</dl>

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

client.judge_analytics_api.get_norm_law_firms_associated_with_norm_judge(
    norm_judge_id="NJUDT7jCZyFNeLGpRq",
    page_number=1,
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

**norm_judge_id:** `str` 

Norm  ID of the Judge.
  - minimum: 18
  - maximum: 18
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.judge_analytics_api.<a href="src/fern/judge_analytics_api/client.py#L209-L279">get_norm_parties_associated_with_norm_judge</a>(...) -> AssociatedNormPartyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of Parties A Judge has seen.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtLocationId IN ("COLODj4BBVTho3pKpz","COLOPUfJRhw5yPxgRi")**|
| **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get all Parties associated with judge with norm id NJUDT7jCZyFNeLGpRq of all cases with case type id CTYPATMYyaJekdgj2c and case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>
</dd>
</dl>
</dd>
</dl>

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

client.judge_analytics_api.get_norm_parties_associated_with_norm_judge(
    norm_judge_id="NJUDT7jCZyFNeLGpRq",
    page_number=1,
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

**norm_judge_id:** `str` 

Norm  ID of the Judge.
  - minimum: 18
  - maximum: 18
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.judge_analytics_api.<a href="src/fern/judge_analytics_api/client.py#L281-L325">search_normalized_judges</a>(...) -> NormJudgeSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

### All query parameters supported for this API can be found in below schema section. Schema --> NormJudgeSearchQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.judge_analytics_api.search_normalized_judges(
    q="normJudgeId:\"NJUD5STmDbUZGukfQm\"",
    page_number=1,
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

**q:** `typing.Optional[str]` 

The URL encoded query you are searching for.
The query can be as simple as a keyword, but supports many additional options and filters.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

Query parameter specifying the page number of the search results to be retrieved.
- Minimum: 1
- Maximum: 1000
    
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

<details><summary><code>client.judge_analytics_api.<a href="src/fern/judge_analytics_api/client.py#L327-L370">search_normalized_judges_by_id</a>(...) -> NormJudgeSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

### All query parameters supported for this API can be found in below schema section. Schema --> NormJudgeSearchQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.judge_analytics_api.search_normalized_judges_by_id(
    norm_judge_search_id="JSRCNUSK3pLGe48QcU",
    page_number=1,
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

**norm_judge_search_id:** `str` — Norm judge Search information for the given normJudgeSearchId.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

Query parameter specifying the page number of the search results to be retrieved.
- Minimum: 1
- Maximum: 1000
    
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

## Law Firm Analytics API
<details><summary><code>client.law_firm_analytics_api.<a href="src/fern/law_firm_analytics_api/client.py#L30-L63">get_norm_law_firm_by_id</a>(...) -> NormLawFirm</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Law Firm API allows you to look up Law Firms by normLawFirmId.
</dd>
</dl>
</dd>
</dl>

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

client.law_firm_analytics_api.get_norm_law_firm_by_id(
    norm_law_firm_id="NORGrPmQyLdx9NGHcT",
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

**norm_law_firm_id:** `str` 

Norm  ID of the Law Firm.
  - minimum: 18
  - maximum: 18
    
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

<details><summary><code>client.law_firm_analytics_api.<a href="src/fern/law_firm_analytics_api/client.py#L65-L139">get_norm_attorneys_associated_with_norm_law_firm</a>(...) -> AssociatedNormAttorneyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of Attorneys associated to a Law Firm.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId**  | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **caseFiledDate**  | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo**  | Multiple Ids Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>        
## Example Query
Query to get all attorneys associated with LawFirm with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>
</dd>
</dl>
</dd>
</dl>

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

client.law_firm_analytics_api.get_norm_attorneys_associated_with_norm_law_firm(
    norm_law_firm_id="NORGrPmQyLdx9NGHcT",
    page_number=1,
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

**norm_law_firm_id:** `str` 

Norm  ID of the Law Firm.
  - minimum: 18
  - maximum: 18
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.law_firm_analytics_api.<a href="src/fern/law_firm_analytics_api/client.py#L141-L212">get_norm_judges_associated_with_norm_law_firm</a>(...) -> AssociatedNormJudgeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns list of Judges faced by the Law Firm.
<br><br>
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **caseFiledDate** | Single Allowed   |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get all judges associated with LawFirm with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>
</dd>
</dl>
</dd>
</dl>

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

client.law_firm_analytics_api.get_norm_judges_associated_with_norm_law_firm(
    norm_law_firm_id="NORGrPmQyLdx9NGHcT",
    page_number=1,
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

**norm_law_firm_id:** `str` 

Norm  ID of the Law Firm.
  - minimum: 18
  - maximum: 18
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.law_firm_analytics_api.<a href="src/fern/law_firm_analytics_api/client.py#L214-L288">get_norm_parties_associated_with_norm_law_firm</a>(...) -> AssociatedNormPartyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns list of Parties represented by the Law Firm.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTKQiA4LJuv54tEj","CORTV4vCEaKrhystBz")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get all parties associated with LawFirm with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>
</dd>
</dl>
</dd>
</dl>

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

client.law_firm_analytics_api.get_norm_parties_associated_with_norm_law_firm(
    norm_law_firm_id="NORGrPmQyLdx9NGHcT",
    page_number=1,
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

**norm_law_firm_id:** `str` 

Norm  ID of the Law Firm.
  - minimum: 18
  - maximum: 18
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.law_firm_analytics_api.<a href="src/fern/law_firm_analytics_api/client.py#L290-L334">search_normalized_law_firms</a>(...) -> NormLawFirmSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

### All query parameters supported for this API can be found in below schema section. Schema --> NormLawFirmSearchQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.law_firm_analytics_api.search_normalized_law_firms(
    q="normLawFirmId:\"NORGDiJQPjeed2mtvx\"",
    page_number=1,
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

**q:** `typing.Optional[str]` 

The URL encoded query you are searching for.
The query can be as simple as a keyword, but supports many additional options and filters.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

Query parameter specifying the page number of the search results to be retrieved.
- Minimum: 1
- Maximum: 1000
    
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

<details><summary><code>client.law_firm_analytics_api.<a href="src/fern/law_firm_analytics_api/client.py#L336-L379">search_normalized_law_firms_by_id</a>(...) -> NormLawFirmSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

### All query parameters supported for this API can be found in below schema section. Schema --> NormLawFirmSearchQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.law_firm_analytics_api.search_normalized_law_firms_by_id(
    norm_law_firm_search_id="LSRCeCT9pC3maopkW7",
    page_number=1,
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

**norm_law_firm_search_id:** `str` — Norm law firm search information for the given normLawFirmSearchId.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

Query parameter specifying the page number of the search results to be retrieved.
- Minimum: 1
- Maximum: 1000
    
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

## Party Analytics API
<details><summary><code>client.party_analytics_api.<a href="src/fern/party_analytics_api/client.py#L30-L63">get_norm_party_by_id</a>(...) -> NormParty</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Party Details API allows you to look up Parties by normPartyId.
</dd>
</dl>
</dd>
</dl>

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

client.party_analytics_api.get_norm_party_by_id(
    norm_party_id="NORGrPmQyLdx9NGHcT",
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

**norm_party_id:** `str` 

Norm ID of the Party.
  - minimum: 18
  - maximum: 18
    
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

<details><summary><code>client.party_analytics_api.<a href="src/fern/party_analytics_api/client.py#L65-L139">get_norm_attorneys_associated_with_norm_party</a>(...) -> AssociatedNormAttorneyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of  Attorneys the Party has been represented by.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz","CORTYsomR6GiiiPovp")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get all attorneys associated with Party with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>
</dd>
</dl>
</dd>
</dl>

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

client.party_analytics_api.get_norm_attorneys_associated_with_norm_party(
    norm_party_id="NORGrPmQyLdx9NGHcT",
    page_number=1,
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

**norm_party_id:** `str` 

Norm ID of the Party.
  - minimum: 18
  - maximum: 18
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.party_analytics_api.<a href="src/fern/party_analytics_api/client.py#L141-L212">get_norm_judges_associated_with_norm_party</a>(...) -> AssociatedNormJudgeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of Judges the party has faced.
<br><br>
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz","CORTYsomR6GiiiPovp")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get all judges associated with Party with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
<br><br>
</dd>
</dl>
</dd>
</dl>

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

client.party_analytics_api.get_norm_judges_associated_with_norm_party(
    norm_party_id="NORGrPmQyLdx9NGHcT",
    page_number=1,
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

**norm_party_id:** `str` 

Norm ID of the Party.
  - minimum: 18
  - maximum: 18
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.party_analytics_api.<a href="src/fern/party_analytics_api/client.py#L214-L287">get_norm_law_firms_associated_with_norm_party</a>(...) -> AssociatedNormLawFirmResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of Law Firms the Party has been represented by.
## Terms and Connectors
| Connector | Schema   | Description  | Example |
| ------| ------| ------|------|
| **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
| **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz","CORTYsomR6GiiiPovp")**|
| **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
| **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
| **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
| **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
| **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
| **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
| **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
| **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
| **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
| **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
| **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
| **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
| **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \*]** |
| **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
<br>
## Example Query
Query to get all lawfirms associated with Party with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
</dd>
</dl>
</dd>
</dl>

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

client.party_analytics_api.get_norm_law_firms_associated_with_norm_party(
    norm_party_id="NORGrPmQyLdx9NGHcT",
    page_number=1,
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

**norm_party_id:** `str` 

Norm ID of the Party.
  - minimum: 18
  - maximum: 18
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` 

Page number.
- minimum: 1
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.
    
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

<details><summary><code>client.party_analytics_api.<a href="src/fern/party_analytics_api/client.py#L289-L333">search_normalized_parties</a>(...) -> NormPartySearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

### All query parameters supported for this API can be found in below schema section. Schema --> NormPartySearchQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.party_analytics_api.search_normalized_parties(
    q="normPartyId:\"NORGJWPpNLekV7dKTm\"",
    page_number=1,
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

**q:** `typing.Optional[str]` 

The URL encoded query you are searching for.
The query can be as simple as a keyword, but supports many additional options and filters.</a>
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

Query parameter specifying the page number of the search results to be retrieved.
- Minimum: 1
- Maximum: 1000
    
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

<details><summary><code>client.party_analytics_api.<a href="src/fern/party_analytics_api/client.py#L335-L378">search_normalized_parties_by_id</a>(...) -> NormPartySearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

### All query parameters supported for this API can be found in below schema section. Schema --> NormPartySearchQueryObject
</dd>
</dl>
</dd>
</dl>

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

client.party_analytics_api.search_normalized_parties_by_id(
    norm_party_search_id="PSRCUoacNCGj9ezvqf",
    page_number=1,
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

**norm_party_search_id:** `str` — Norm Party Search information for the given normPartySearchId.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 

Query parameter specifying the page number of the search results to be retrieved.
- Minimum: 1
- Maximum: 1000
    
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

## PACER API
<details><summary><code>client.pacer_api.<a href="src/fern/pacer_api/client.py#L65-L132">import_pacer_case_by_court_using_case_number</a>(...) -> PacerImportCase</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import the specified case from PACER. 

	Workflow: 

		1.This API will return the Find Case results from the court site in a form of array of UniCourt Case Objects. These case objects will consists only Meta information of the case if not already present in the UniCourt Database. 

		2.To get the full updated case information one will have to request the caseUpdate API by passing the caseId. 

	Note: 

		1.Charges for Find Case in District, Bankruptcy and National Courts is free. Find case for Appeal Courts will be charged at minimum rate of $0.1. The fee charged by the court for find case can be found in the response of this API in the field courtFee. 

		2.The results of the search has less Meta information in case objects compared to the Meta information of cases found using the PCL search APIs.
</dd>
</dl>
</dd>
</dl>

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

client.pacer_api.import_pacer_case_by_court_using_case_number(
    pacer_user_id="johndoe",
    pacer_client_code="john",
    case_number="2:15-mc-12345",
    court_id="CORTjF63b8Z4d2i9UB",
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

**pacer_user_id:** `str` — The PACER username of the PACER account under which the case should be imported.
    
</dd>
</dl>

<dl>
<dd>

**pacer_client_code:** `str` — The PACER client code under which the case should be imported.
    
</dd>
</dl>

<dl>
<dd>

**case_number:** `str` — The case number of the case to be imported.
    
</dd>
</dl>

<dl>
<dd>

**court_id:** `str` — The courtId value of the court from which the case is to be imported.
    
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

<details><summary><code>client.pacer_api.<a href="src/fern/pacer_api/client.py#L134-L305">all_courts_pacer_case_locator_case_search</a>(...) -> PclCase</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search all courts within the PACER system for a particular case.
</dd>
</dl>
</dd>
</dl>

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

client.pacer_api.all_courts_pacer_case_locator_case_search(
    pacer_user_id="johndoe",
    pacer_client_code="john",
    case_number="12-1234",
    case_title="A",
    sort_parameter_query="sort=caseYear",
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

**pacer_user_id:** `str` — The username of the PACER account under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**pacer_client_code:** `str` — The PACER client code under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**case_number:** `typing.Optional[str]` 

The case number of the target case. You may use the following case-number formats: 

	yy-nnnnn 

	yy-tp-nnnnn 

	yy tp nnnnn 

	yytpnnnnn 

	o:yy-nnnnn 

	o:yy-tp-nnnnn 

	o:yy tp nnnnn 

	o:yytpnnnnn 

where: 

yy  case year (may be 2 or 4 digits) 

nnnnn  case number (up to 5 digits) 

tp  case type (up to 2 characters) 

o  office where the case was filed (1 digit).
    
</dd>
</dl>

<dl>
<dd>

**pacer_case_id:** `typing.Optional[int]` — The PACER-assigned identifier of the target case.
    
</dd>
</dl>

<dl>
<dd>

**case_title:** `typing.Optional[str]` 

The title of the target case. 

	Examples: 

	A search for case title john doe v will result in all cases with the case title John Doe v. 

	A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
    
</dd>
</dl>

<dl>
<dd>

**case_office:** `typing.Optional[int]` — The divisional office in which the case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_sequence_number:** `typing.Optional[int]` — The PACER-assigned sequence number of the target case. Ex 12345
    
</dd>
</dl>

<dl>
<dd>

**case_year:** `typing.Optional[int]` — The two- or four-digit year in which the target case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_type_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values. 

	Scenario: When mulitple case types needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below. 

	Example: caseTypeArray=cv&caseTypeArray=cr
    
</dd>
</dl>

<dl>
<dd>

**court_region_id_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values. 

	Scenario: When mulitple court region ids needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below. 

	Example: courtRegionIdArray=cac&courtRegionIdArray=cae
    
</dd>
</dl>

<dl>
<dd>

**case_filed_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_filed_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**sort_parameter_query:** `typing.Optional[str]` 

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings. 

	Scenario: When mulitple sort paramters needs to be requested. 

	Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below. 

	Example: sortParameterQuery=courtId,ASC&caseId,ASC
    
</dd>
</dl>

<dl>
<dd>

**case_status:** `typing.Optional[AllCourtsPacerCaseLocatorCaseSearchRequestCaseStatus]` — Whether the target case is marked as 'open' or 'closed' within PACER.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — The page number of the search results to be retrieved.
    
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

<details><summary><code>client.pacer_api.<a href="src/fern/pacer_api/client.py#L307-L472">appeal_courts_pacer_case_locator_case_search</a>(...) -> PclCase</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for PACER cases filed in U.S. Courts of Appeals.
</dd>
</dl>
</dd>
</dl>

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

client.pacer_api.appeal_courts_pacer_case_locator_case_search(
    pacer_user_id="johndoe",
    pacer_client_code="john",
    case_number="12-1234",
    case_title="A",
    sort_parameter_query="sort=caseYear",
    page_number=1,
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

**pacer_user_id:** `str` — The username of the PACER account under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**pacer_client_code:** `str` — The PACER client code under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**case_number:** `typing.Optional[str]` 

The case number of the target case. You may use the following case-number formats: 

	yy-nnnnn  

where: 

yy  case year (may be 2 or 4 digits) 

nnnnn  case number (up to 5 digits).
    
</dd>
</dl>

<dl>
<dd>

**pacer_case_id:** `typing.Optional[int]` — The PACER-assigned identifier of the target case.
    
</dd>
</dl>

<dl>
<dd>

**case_title:** `typing.Optional[str]` 

The title of the target case. 

	Examples: 

	A search for case title john doe v will result in all cases with the case title John Doe v. 

	A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
    
</dd>
</dl>

<dl>
<dd>

**case_office:** `typing.Optional[int]` — The divisional office in which the case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_sequence_number:** `typing.Optional[int]` — The PACER-assigned sequence number of the target case. Ex 12345
    
</dd>
</dl>

<dl>
<dd>

**case_year:** `typing.Optional[int]` — The two- or four-digit year in which the target case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_type_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values. 

	Scenario: When mulitple case types needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below. 

	Example: caseTypeArray=cv&caseTypeArray=cr
    
</dd>
</dl>

<dl>
<dd>

**nature_of_suits_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned nature of suit classification of the target case. Please see Appendix E for valid nature-of-suit classifications for cases in U.S. Courts of Appeals. 

	Scenario: When mulitple nature of suits needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search with the nature of suit 1110 (Insurance) and 1150 (Overpayments & Enforc. of Judgments), My query in the request will look like the example mentioned below. 

	Example: natureOfSuitsArray=1110&natureOfSuitsArray=1150
    
</dd>
</dl>

<dl>
<dd>

**court_region_id_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values. 

	Scenario: When mulitple court region ids needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below. 

	Example: courtRegionIdArray=cac&courtRegionIdArray=cae
    
</dd>
</dl>

<dl>
<dd>

**case_filed_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_filed_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**sort_parameter_query:** `typing.Optional[str]` 

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings. 

	Scenario: When mulitple sort paramters needs to be requested. 

	Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below. 

	Example: sortParameterQuery=courtId,ASC&caseId,ASC
    
</dd>
</dl>

<dl>
<dd>

**case_status:** `typing.Optional[AppealCourtsPacerCaseLocatorCaseSearchRequestCaseStatus]` — Whether the target case is marked as 'open' or 'closed' within PACER.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — The page number of the search results to be retrieved.
    
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

<details><summary><code>client.pacer_api.<a href="src/fern/pacer_api/client.py#L474-L682">bankruptcy_courts_pacer_case_locator_case_search</a>(...) -> PclCase</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for PACER cases filed in U.S. Bankruptcy Courts.
</dd>
</dl>
</dd>
</dl>

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

client.pacer_api.bankruptcy_courts_pacer_case_locator_case_search(
    pacer_user_id="johndoe",
    pacer_client_code="john",
    case_number="12-1234",
    case_title="A",
    sort_parameter_query="sort=caseYear",
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

**pacer_user_id:** `str` — The username of the PACER account under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**pacer_client_code:** `str` — The PACER client code under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**case_number:** `typing.Optional[str]` 

The case number of the target case. You may use the following case-number formats: 

	yy-nnnnn 

	yy-tp-nnnnn 

	yy tp nnnnn 

	yytpnnnnn 

	o:yy-nnnnn 

	o:yy-tp-nnnnn 

	o:yy tp nnnnn 

	o:yytpnnnnn 

where: 

yy  case year (may be 2 or 4 digits) 

nnnnn  case number (up to 5 digits) 

tp  case type (up to 2 characters) 

o  office where the case was filed (1 digit).
    
</dd>
</dl>

<dl>
<dd>

**pacer_case_id:** `typing.Optional[int]` — The PACER-assigned identifier of the target case.
    
</dd>
</dl>

<dl>
<dd>

**case_title:** `typing.Optional[str]` 

The title of the target case. 

	Examples: 

	A search for case title john doe v will result in all cases with the case title John Doe v. 

	A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
    
</dd>
</dl>

<dl>
<dd>

**case_office:** `typing.Optional[int]` — The divisional office in which the case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_sequence_number:** `typing.Optional[int]` — The PACER-assigned sequence number of the target case. Ex 12345
    
</dd>
</dl>

<dl>
<dd>

**case_year:** `typing.Optional[int]` — The two- or four-digit year in which the target case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_type_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values. 

	Scenario: When mulitple case types needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below. 

	Example: caseTypeArray=cv&caseTypeArray=cr
    
</dd>
</dl>

<dl>
<dd>

**federal_bankruptcy_chapter_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The chapter of the U.S. Bankruptcy Code under which the target case was filed. Please see Appendix D for a list of valid chapter numbers. 

	Scenario: When mulitple Federal Bankruptcy Chapters needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search with the Federal Bankruptcy Chapters 7 (Chapter 7) and 11 (Chapter 11), My query in the request will look like the example mentioned below. 

	Example: federalBankruptcyChapterArray=7&federalBankruptcyChapterArray=11
    
</dd>
</dl>

<dl>
<dd>

**court_region_id_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values. 

	Scenario: When mulitple court region ids needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below. 

	Example: courtRegionIdArray=cac&courtRegionIdArray=cae
    
</dd>
</dl>

<dl>
<dd>

**case_filed_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_filed_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_discharged_start_date:** `typing.Optional[datetime.datetime]` 

The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). 

	Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
    
</dd>
</dl>

<dl>
<dd>

**case_discharged_end_date:** `typing.Optional[datetime.datetime]` 

The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). 

	Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
    
</dd>
</dl>

<dl>
<dd>

**case_dismissed_start_date:** `typing.Optional[datetime.datetime]` 

The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). 

	Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
    
</dd>
</dl>

<dl>
<dd>

**case_dismissed_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**sort_parameter_query:** `typing.Optional[str]` 

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings. 

	Scenario: When mulitple sort paramters needs to be requested. 

	Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below. 

	Example: sortParameterQuery=courtId,ASC&caseId,ASC
    
</dd>
</dl>

<dl>
<dd>

**case_status:** `typing.Optional[BankruptcyCourtsPacerCaseLocatorCaseSearchRequestCaseStatus]` — Whether the target case is marked as 'open' or 'closed' within PACER.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — The page number of the search results to be retrieved.
    
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

<details><summary><code>client.pacer_api.<a href="src/fern/pacer_api/client.py#L684-L866">civil_courts_pacer_case_locator_case_search</a>(...) -> PclCase</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for civil cases filed in PACER.
</dd>
</dl>
</dd>
</dl>

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

client.pacer_api.civil_courts_pacer_case_locator_case_search(
    pacer_user_id="johndoe",
    pacer_client_code="john",
    case_number="12-1234",
    case_title="A",
    sort_parameter_query="sort=caseYear",
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

**pacer_user_id:** `str` — The username of the PACER account under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**pacer_client_code:** `str` — The PACER client code under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**case_number:** `typing.Optional[str]` 

The case number of the target case. You may use the following case-number formats: 

	yy-nnnnn 

	yy-tp-nnnnn 

	yy tp nnnnn 

	yytpnnnnn 

	o:yy-nnnnn 

	o:yy-tp-nnnnn 

	o:yy tp nnnnn 

	o:yytpnnnnn 

where: 

yy  case year (may be 2 or 4 digits) 

nnnnn  case number (up to 5 digits) 

tp  case type (up to 2 characters) 

o  office where the case was filed (1 digit).
    
</dd>
</dl>

<dl>
<dd>

**pacer_case_id:** `typing.Optional[int]` — The PACER-assigned identifier of the target case.
    
</dd>
</dl>

<dl>
<dd>

**case_title:** `typing.Optional[str]` 

The title of the target case. 

	Examples: 

	A search for case title john doe v will result in all cases with the case title John Doe v. 

	A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
    
</dd>
</dl>

<dl>
<dd>

**case_office:** `typing.Optional[int]` — The divisional office in which the case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_sequence_number:** `typing.Optional[int]` — The PACER-assigned sequence number of the target case.
    
</dd>
</dl>

<dl>
<dd>

**case_year:** `typing.Optional[int]` — The two- or four-digit year in which the target case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_type_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values. 

	Scenario: When mulitple case types needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below. 

	Example: caseTypeArray=cv&caseTypeArray=cr
    
</dd>
</dl>

<dl>
<dd>

**nature_of_suits_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned nature of suit classification of the target case. Please see Appendix E for valid nature-of-suit classifications for cases. 

	Scenario: When mulitple nature of suits needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search with the nature of suit 110 (Insurance) and 140 (Negotiable Instrument), My query in the request will look like the example mentioned below. 

	Example: natureOfSuitsArray=110&natureOfSuitsArray=140
    
</dd>
</dl>

<dl>
<dd>

**court_region_id_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values. 

	Scenario: When mulitple court region ids needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below. 

	Example: courtRegionIdArray=cac&courtRegionIdArray=cae
    
</dd>
</dl>

<dl>
<dd>

**case_filed_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_filed_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**sort_parameter_query:** `typing.Optional[str]` 

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings. 

	Scenario: When mulitple sort paramters needs to be requested. 

	Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below. 

	Example: sortParameterQuery=courtId,ASC&caseId,ASC
    
</dd>
</dl>

<dl>
<dd>

**case_status:** `typing.Optional[CivilCourtsPacerCaseLocatorCaseSearchRequestCaseStatus]` — Whether the target case is marked as 'open' or 'closed' within PACER.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — The page number of the search results to be retrieved.
    
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

<details><summary><code>client.pacer_api.<a href="src/fern/pacer_api/client.py#L868-L1039">criminal_courts_pacer_case_locator_case_search</a>(...) -> PclCase</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for criminal cases in PACER.
</dd>
</dl>
</dd>
</dl>

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

client.pacer_api.criminal_courts_pacer_case_locator_case_search(
    pacer_user_id="johndoe",
    pacer_client_code="john",
    case_number="12-1234",
    case_title="A",
    sort_parameter_query="sort=caseYear",
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

**pacer_user_id:** `str` — The username of the PACER account under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**pacer_client_code:** `str` — The PACER client code under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**case_number:** `typing.Optional[str]` 

The case number of the target case. You may use the following case-number formats: 

	yy-nnnnn 

	yy-tp-nnnnn 

	yy tp nnnnn 

	yytpnnnnn 

	o:yy-nnnnn 

	o:yy-tp-nnnnn 

	o:yy tp nnnnn 

	o:yytpnnnnn 

where: 

yy  case year (may be 2 or 4 digits) 

nnnnn  case number (up to 5 digits) 

tp  case type (up to 2 characters) 

o  office where the case was filed (1 digit).
    
</dd>
</dl>

<dl>
<dd>

**pacer_case_id:** `typing.Optional[int]` — The PACER-assigned identifier of the target case.
    
</dd>
</dl>

<dl>
<dd>

**case_title:** `typing.Optional[str]` 

The title of the target case. 

	Examples: 

	A search for case title john doe v will result in all cases with the case title John Doe v. 

	A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
    
</dd>
</dl>

<dl>
<dd>

**case_office:** `typing.Optional[int]` — The divisional office in which the case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_sequence_number:** `typing.Optional[int]` — The PACER-assigned sequence number of the target case. Ex 12345
    
</dd>
</dl>

<dl>
<dd>

**case_year:** `typing.Optional[int]` — The two- or four-digit year in which the target case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_type_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values. 

	Scenario: When mulitple case types needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below. 

	Example: caseTypeArray=cv&caseTypeArray=cr
    
</dd>
</dl>

<dl>
<dd>

**court_region_id_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values. 

	Scenario: When mulitple court region ids needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below. 

	Example: courtRegionIdArray=cac&courtRegionIdArray=cae
    
</dd>
</dl>

<dl>
<dd>

**case_filed_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_filed_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**sort_parameter_query:** `typing.Optional[str]` 

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings. 

	Scenario: When mulitple sort paramters needs to be requested. 

	Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below. 

	Example: sortParameterQuery=courtId,ASC&caseId,ASC
    
</dd>
</dl>

<dl>
<dd>

**case_status:** `typing.Optional[CriminalCourtsPacerCaseLocatorCaseSearchRequestCaseStatus]` — Whether the target case is marked as 'open' or 'closed' within PACER.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — The page number of the search results to be retrieved.
    
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

<details><summary><code>client.pacer_api.<a href="src/fern/pacer_api/client.py#L1041-L1217">multi_district_courts_pacer_case_locator_case_search</a>(...) -> PclCase</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for multidistrict litigation in PACER.
</dd>
</dl>
</dd>
</dl>

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

client.pacer_api.multi_district_courts_pacer_case_locator_case_search(
    pacer_user_id="johndoe",
    pacer_client_code="john",
    case_number="12-1234",
    case_title="A",
    sort_parameter_query="sort=caseYear",
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

**pacer_user_id:** `str` — The username of the PACER account under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**pacer_client_code:** `str` — The PACER client code under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**case_number:** `typing.Optional[str]` 

The case number of the target case. You may use the following case-number formats: 

	yy-nnnnn 

	yy-tp-nnnnn 

	yy tp nnnnn 

	yytpnnnnn 

	o:yy-nnnnn 

	o:yy-tp-nnnnn 

	o:yy tp nnnnn 

	o:yytpnnnnn 

where: 

yy  case year (may be 2 or 4 digits) 

nnnnn  case number (up to 5 digits) 

tp  case type (up to 2 characters) 

o  office where the case was filed (1 digit).
    
</dd>
</dl>

<dl>
<dd>

**jpml_number:** `typing.Optional[int]` — Master JPML Case Number.
    
</dd>
</dl>

<dl>
<dd>

**pacer_case_id:** `typing.Optional[int]` — The PACER-assigned identifier of the target case.
    
</dd>
</dl>

<dl>
<dd>

**case_title:** `typing.Optional[str]` 

The title of the target case. 

	Examples: 

	A search for case title john doe v will result in all cases with the case title John Doe v. 

	A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
    
</dd>
</dl>

<dl>
<dd>

**case_office:** `typing.Optional[int]` — The divisional office in which the case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_sequence_number:** `typing.Optional[int]` — The PACER-assigned sequence number of the target case. Ex 12345
    
</dd>
</dl>

<dl>
<dd>

**case_year:** `typing.Optional[int]` — The two- or four-digit year in which the target case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_type_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values. 

	Scenario: When mulitple case types needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below. 

	Example: caseTypeArray=cv&caseTypeArray=cr
    
</dd>
</dl>

<dl>
<dd>

**court_region_id_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values. 

	Scenario: When mulitple court region ids needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below. 

	Example: courtRegionIdArray=cac&courtRegionIdArray=cae
    
</dd>
</dl>

<dl>
<dd>

**case_filed_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_filed_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**sort_parameter_query:** `typing.Optional[str]` 

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings. 

	Scenario: When mulitple sort paramters needs to be requested. 

	Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below. 

	Example: sortParameterQuery=courtId,ASC&caseId,ASC
    
</dd>
</dl>

<dl>
<dd>

**case_status:** `typing.Optional[MultiDistrictCourtsPacerCaseLocatorCaseSearchRequestCaseStatus]` — Whether the target case is marked as 'open' or 'closed' within PACER.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — The page number of the search results to be retrieved.
    
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

<details><summary><code>client.pacer_api.<a href="src/fern/pacer_api/client.py#L1219-L1447">all_courts_pacer_case_locator_party_search</a>(...) -> PclParty</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for the specified party across all PACER case filings.
</dd>
</dl>
</dd>
</dl>

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

client.pacer_api.all_courts_pacer_case_locator_party_search(
    pacer_user_id="johndoe",
    pacer_client_code="john",
    case_number="12-1234",
    last_name="John",
    first_name="John",
    middle_name="Doe",
    generation="III",
    party_type="ptf",
    party_role_array=[
        "plantiff"
    ],
    case_title="A",
    sort_parameter_query="sort=caseYear",
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

**pacer_user_id:** `str` — The username of the PACER account under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**pacer_client_code:** `str` — The PACER client code under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**case_number:** `typing.Optional[str]` 

The case number of the target case. You may use the following case-number formats: 

	yy-nnnnn 

	yy-tp-nnnnn 

	yy tp nnnnn 

	yytpnnnnn 

	o:yy-nnnnn 

	o:yy-tp-nnnnn 

	o:yy tp nnnnn 

	o:yytpnnnnn 

where: 

yy  case year (may be 2 or 4 digits) 

nnnnn  case number (up to 5 digits) 

tp  case type (up to 2 characters) 

o  office where the case was filed (1 digit).
    
</dd>
</dl>

<dl>
<dd>

**pacer_case_id:** `typing.Optional[int]` — The PACER-assigned identifier of the target case.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The last name (for an individual) or the entity name (for a business entity) of the target party.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The first name of the target party.
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[str]` — The middle name of the target party.
    
</dd>
</dl>

<dl>
<dd>

**generation:** `typing.Optional[str]` — The suffix (e.g., Jr., III) of the target party's name.
    
</dd>
</dl>

<dl>
<dd>

**party_type:** `typing.Optional[str]` — The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
    
</dd>
</dl>

<dl>
<dd>

**party_exact_name_match:** `typing.Optional[bool]` — Specify whether the search string must match the name of the target party exactly.
    
</dd>
</dl>

<dl>
<dd>

**party_role_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` — The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
    
</dd>
</dl>

<dl>
<dd>

**case_title:** `typing.Optional[str]` 

The title of the target case. 

	Examples: 

	A search for case title john doe v will result in all cases with the case title John Doe v. 

	A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
    
</dd>
</dl>

<dl>
<dd>

**case_office:** `typing.Optional[int]` — The divisional office in which the case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_sequence_number:** `typing.Optional[int]` — The PACER-assigned sequence number of the target case.
    
</dd>
</dl>

<dl>
<dd>

**case_year:** `typing.Optional[int]` — The two- or four-digit year in which the target case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_type_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values. 

	Scenario: When mulitple case types needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below. 

	Example: caseTypeArray=cv&caseTypeArray=cr
    
</dd>
</dl>

<dl>
<dd>

**court_region_id_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values. 

	Scenario: When mulitple court region ids needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below. 

	Example: courtRegionIdArray=cac&courtRegionIdArray=cae
    
</dd>
</dl>

<dl>
<dd>

**case_year_from:** `typing.Optional[int]` — Limit the results of the search to those cases from the year specified or later
    
</dd>
</dl>

<dl>
<dd>

**case_year_to:** `typing.Optional[int]` — Limit the results of the search to those cases from the year specified or earlier
    
</dd>
</dl>

<dl>
<dd>

**case_filed_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_filed_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**sort_parameter_query:** `typing.Optional[str]` 

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings. 

	Scenario 1: When mulitple sort paramters needs to be requested. 

	Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below. 

	Example: sortParameterQuery=courtId,ASC&caseId,ASC 

	Scenario 2: When you want to sort the response using the case parameters in the party search. 

	Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below. 

	Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC
    
</dd>
</dl>

<dl>
<dd>

**case_status:** `typing.Optional[AllCourtsPacerCaseLocatorPartySearchRequestCaseStatus]` — Whether the target case is marked as 'open' or 'closed' within PACER.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — The page number of the search results to be retrieved.
    
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

<details><summary><code>client.pacer_api.<a href="src/fern/pacer_api/client.py#L1449-L1677">appeal_courts_pacer_case_locator_party_search</a>(...) -> PclParty</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for the specified party across all PACER appeals cases.
</dd>
</dl>
</dd>
</dl>

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

client.pacer_api.appeal_courts_pacer_case_locator_party_search(
    pacer_user_id="johndoe",
    pacer_client_code="john",
    case_number="12-1234",
    last_name="John",
    first_name="John",
    middle_name="Doe",
    generation="III",
    party_type="ptf",
    party_role_array=[
        "plantiff"
    ],
    case_title="A",
    sort_parameter_query="sort=caseYear",
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

**pacer_user_id:** `str` — The username of the PACER account under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**pacer_client_code:** `str` — The PACER client code under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**case_number:** `typing.Optional[str]` 

The case number of the target case. You may use the following case-number formats: 

	yy-nnnnn 

	yy-tp-nnnnn 

	yy tp nnnnn 

	yytpnnnnn 

	o:yy-nnnnn 

	o:yy-tp-nnnnn 

	o:yy tp nnnnn 

	o:yytpnnnnn 

where: 

yy  case year (may be 2 or 4 digits) 

nnnnn  case number (up to 5 digits) 

tp  case type (up to 2 characters) 

o  office where the case was filed (1 digit).
    
</dd>
</dl>

<dl>
<dd>

**pacer_case_id:** `typing.Optional[int]` — The PACER-assigned identifier of the target case.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The last name (for an individual) or the entity name (for a business entity) of the target party.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The first name of the target party.
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[str]` — The middle name of the target party.
    
</dd>
</dl>

<dl>
<dd>

**generation:** `typing.Optional[str]` — The suffix (e.g., Jr., III) of the target party's name.
    
</dd>
</dl>

<dl>
<dd>

**party_type:** `typing.Optional[str]` — The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
    
</dd>
</dl>

<dl>
<dd>

**party_exact_name_match:** `typing.Optional[bool]` — Specify whether the search string must match the name of the target party exactly.
    
</dd>
</dl>

<dl>
<dd>

**party_role_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` — The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
    
</dd>
</dl>

<dl>
<dd>

**case_title:** `typing.Optional[str]` 

The title of the target case. 

	Examples: 

	A search for case title john doe v will result in all cases with the case title John Doe v. 

	A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
    
</dd>
</dl>

<dl>
<dd>

**case_office:** `typing.Optional[int]` — The divisional office in which the case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_sequence_number:** `typing.Optional[int]` — The PACER-assigned sequence number of the target case. Ex 12345
    
</dd>
</dl>

<dl>
<dd>

**case_year:** `typing.Optional[int]` — The two- or four-digit year in which the target case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_type_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values. 

	Scenario: When mulitple case types needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below. 

	Example: caseTypeArray=cv&caseTypeArray=cr
    
</dd>
</dl>

<dl>
<dd>

**court_region_id_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values. 

	Scenario: When mulitple court region ids needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below. 

	Example: courtRegionIdArray=cac&courtRegionIdArray=cae
    
</dd>
</dl>

<dl>
<dd>

**case_year_from:** `typing.Optional[int]` — Limit the results of the search to those cases from the year specified or later
    
</dd>
</dl>

<dl>
<dd>

**case_year_to:** `typing.Optional[int]` — Limit the results of the search to those cases from the year specified or earlier
    
</dd>
</dl>

<dl>
<dd>

**case_filed_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_filed_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**sort_parameter_query:** `typing.Optional[str]` 

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings. 

	Scenario 1: When mulitple sort paramters needs to be requested. 

	Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below. 

	Example: sortParameterQuery=courtId,ASC&caseId,ASC 

	Scenario 2: When you want to sort the response using the case parameters in the party search. 

	Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below. 

	Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC
    
</dd>
</dl>

<dl>
<dd>

**case_status:** `typing.Optional[AppealCourtsPacerCaseLocatorPartySearchRequestCaseStatus]` — Whether the target case is marked as 'open' or 'closed' within PACER.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — The page number of the search results to be retrieved.
    
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

<details><summary><code>client.pacer_api.<a href="src/fern/pacer_api/client.py#L1679-L1946">bankruptcy_courts_pacer_case_locator_party_search</a>(...) -> PclParty</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for the specified party in PACER bankruptcy filings.
</dd>
</dl>
</dd>
</dl>

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

client.pacer_api.bankruptcy_courts_pacer_case_locator_party_search(
    pacer_user_id="johndoe",
    pacer_client_code="john",
    case_number="12-1234",
    last_name="John",
    first_name="John",
    middle_name="Doe",
    generation="III",
    party_type="ptf",
    party_role_array=[
        "plantiff"
    ],
    case_title="A",
    ssn_or_ein="125689545669954655",
    sort_parameter_query="sort=caseYear",
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

**pacer_user_id:** `str` — The username of the PACER account under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**pacer_client_code:** `str` — The PACER client code under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**case_number:** `typing.Optional[str]` 

The case number of the target case. You may use the following case-number formats: 

	yy-nnnnn 

	yy-tp-nnnnn 

	yy tp nnnnn 

	yytpnnnnn 

	o:yy-nnnnn 

	o:yy-tp-nnnnn 

	o:yy tp nnnnn 

	o:yytpnnnnn 

where: 

yy  case year (may be 2 or 4 digits) 

nnnnn  case number (up to 5 digits) 

tp  case type (up to 2 characters) 

o  office where the case was filed (1 digit).
    
</dd>
</dl>

<dl>
<dd>

**pacer_case_id:** `typing.Optional[int]` — The PACER-assigned identifier of the target case.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The last name (for an individual) or the entity name (for a business entity) of the target party.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The first name of the target party.
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[str]` — The middle name of the target party.
    
</dd>
</dl>

<dl>
<dd>

**generation:** `typing.Optional[str]` — The suffix (e.g., Jr., III) of the target party's name.
    
</dd>
</dl>

<dl>
<dd>

**party_type:** `typing.Optional[str]` — The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
    
</dd>
</dl>

<dl>
<dd>

**party_exact_name_match:** `typing.Optional[bool]` — Specify whether the search string must match the name of the target party exactly.
    
</dd>
</dl>

<dl>
<dd>

**party_role_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` — The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
    
</dd>
</dl>

<dl>
<dd>

**case_title:** `typing.Optional[str]` 

The title of the target case. 

	Examples: 

	A search for case title john doe v will result in all cases with the case title John Doe v. 

	A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
    
</dd>
</dl>

<dl>
<dd>

**case_office:** `typing.Optional[int]` — The divisional office in which the case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_sequence_number:** `typing.Optional[int]` — The PACER-assigned sequence number of the target case. Ex 12345
    
</dd>
</dl>

<dl>
<dd>

**case_year:** `typing.Optional[int]` — The two- or four-digit year in which the target case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_type_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values. 

	Scenario: When mulitple case types needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below. 

	Example: caseTypeArray=cv&caseTypeArray=cr
    
</dd>
</dl>

<dl>
<dd>

**court_region_id_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values. 

	Scenario: When mulitple court region ids needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below. 

	Example: courtRegionIdArray=cac&courtRegionIdArray=cae
    
</dd>
</dl>

<dl>
<dd>

**case_year_from:** `typing.Optional[int]` — Limit the results of the search to those cases from the year specified or later
    
</dd>
</dl>

<dl>
<dd>

**case_year_to:** `typing.Optional[int]` — Limit the results of the search to those cases from the year specified or earlier
    
</dd>
</dl>

<dl>
<dd>

**ssn_or_ein:** `typing.Optional[str]` — The Social Security number or the federal Employer Identification Number of the target party. Either number can be entered with or without dashes.
    
</dd>
</dl>

<dl>
<dd>

**four_digit_ssn:** `typing.Optional[str]` 

The last four digits of the Social Security number of the target party.

	Note: When specified, a last name/entity name must also be specified.
    
</dd>
</dl>

<dl>
<dd>

**case_filed_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_filed_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_discharged_start_date:** `typing.Optional[datetime.datetime]` 

The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). 

	Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
    
</dd>
</dl>

<dl>
<dd>

**case_discharged_end_date:** `typing.Optional[datetime.datetime]` 

The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). 

	Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
    
</dd>
</dl>

<dl>
<dd>

**case_dismissed_start_date:** `typing.Optional[datetime.datetime]` 

The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). 

	Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.
    
</dd>
</dl>

<dl>
<dd>

**case_dismissed_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**sort_parameter_query:** `typing.Optional[str]` 

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings. 

	Scenario 1: When mulitple sort paramters needs to be requested. 

	Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below. 

	Example: sortParameterQuery=courtId,ASC&caseId,ASC 

	Scenario 2: When you want to sort the response using the case parameters in the party search. 

	Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below. 

	Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC
    
</dd>
</dl>

<dl>
<dd>

**case_status:** `typing.Optional[BankruptcyCourtsPacerCaseLocatorPartySearchRequestCaseStatus]` — Whether the target case is marked as 'open' or 'closed' within PACER.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — The page number of the search results to be retrieved.
    
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

<details><summary><code>client.pacer_api.<a href="src/fern/pacer_api/client.py#L1948-L2176">civil_courts_pacer_case_locator_party_search</a>(...) -> PclParty</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for the specified party in civil cases filed in PACER.
</dd>
</dl>
</dd>
</dl>

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

client.pacer_api.civil_courts_pacer_case_locator_party_search(
    pacer_user_id="johndoe",
    pacer_client_code="john",
    case_number="12-1234",
    last_name="John",
    first_name="John",
    middle_name="Doe",
    generation="III",
    party_type="ptf",
    party_role_array=[
        "plantiff"
    ],
    case_title="A",
    sort_parameter_query="sort=caseYear",
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

**pacer_user_id:** `str` — The username of the PACER account under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**pacer_client_code:** `str` — The PACER client code under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**case_number:** `typing.Optional[str]` 

The case number of the target case. You may use the following case-number formats: 

	yy-nnnnn 

	yy-tp-nnnnn 

	yy tp nnnnn 

	yytpnnnnn 

	o:yy-nnnnn 

	o:yy-tp-nnnnn 

	o:yy tp nnnnn 

	o:yytpnnnnn 

where: 

yy  case year (may be 2 or 4 digits) 

nnnnn  case number (up to 5 digits) 

tp  case type (up to 2 characters) 

o  office where the case was filed (1 digit).
    
</dd>
</dl>

<dl>
<dd>

**pacer_case_id:** `typing.Optional[int]` — The PACER-assigned identifier of the target case.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The last name (for an individual) or the entity name (for a business entity) of the target party.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The first name of the target party.
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[str]` — The middle name of the target party.
    
</dd>
</dl>

<dl>
<dd>

**generation:** `typing.Optional[str]` — The name suffix (e.g., III, MD).
    
</dd>
</dl>

<dl>
<dd>

**party_type:** `typing.Optional[str]` — The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
    
</dd>
</dl>

<dl>
<dd>

**party_exact_name_match:** `typing.Optional[bool]` — Specify whether the search string must match the name of the target party exactly.
    
</dd>
</dl>

<dl>
<dd>

**party_role_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` — The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
    
</dd>
</dl>

<dl>
<dd>

**case_title:** `typing.Optional[str]` 

The title of the target case. 

	Examples: 

	A search for case title john doe v will result in all cases with the case title John Doe v. 

	A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
    
</dd>
</dl>

<dl>
<dd>

**case_office:** `typing.Optional[int]` — The divisional office in which the case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_sequence_number:** `typing.Optional[int]` — The PACER-assigned sequence number of the target case. Ex 12345
    
</dd>
</dl>

<dl>
<dd>

**case_year:** `typing.Optional[int]` — The two- or four-digit year in which the target case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_type_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values. 

	Scenario: When mulitple case types needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below. 

	Example: caseTypeArray=cv&caseTypeArray=cr
    
</dd>
</dl>

<dl>
<dd>

**court_region_id_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values. 

	Scenario: When mulitple court region ids needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below. 

	Example: courtRegionIdArray=cac&courtRegionIdArray=cae
    
</dd>
</dl>

<dl>
<dd>

**case_year_from:** `typing.Optional[int]` — Limit the results of the search to those cases from the year specified or later
    
</dd>
</dl>

<dl>
<dd>

**case_year_to:** `typing.Optional[int]` — Limit the results of the search to those cases from the year specified or earlier
    
</dd>
</dl>

<dl>
<dd>

**case_filed_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_filed_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**sort_parameter_query:** `typing.Optional[str]` 

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings. 

	Scenario 1: When mulitple sort paramters needs to be requested. 

	Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below. 

	Example: sortParameterQuery=courtId,ASC&caseId,ASC 

	Scenario 2: When you want to sort the response using the case parameters in the party search. 

	Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below. 

	Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC
    
</dd>
</dl>

<dl>
<dd>

**case_status:** `typing.Optional[CivilCourtsPacerCaseLocatorPartySearchRequestCaseStatus]` — Whether the target case is marked as 'open' or 'closed' within PACER.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — The page number of the search results to be retrieved.
    
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

<details><summary><code>client.pacer_api.<a href="src/fern/pacer_api/client.py#L2178-L2406">criminal_courts_pacer_case_locator_party_search</a>(...) -> PclParty</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for the specified party in PACER criminal cases.
</dd>
</dl>
</dd>
</dl>

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

client.pacer_api.criminal_courts_pacer_case_locator_party_search(
    pacer_user_id="johndoe",
    pacer_client_code="john",
    case_number="12-1234",
    last_name="John",
    first_name="John",
    middle_name="Doe",
    generation="III",
    party_type="ptf",
    party_role_array=[
        "plantiff"
    ],
    case_title="A",
    sort_parameter_query="sort=caseYear",
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

**pacer_user_id:** `str` — The username of the PACER account under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**pacer_client_code:** `str` — The PACER client code under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**case_number:** `typing.Optional[str]` 

The case number of the target case. You may use the following case-number formats: 

	yy-nnnnn 

	yy-tp-nnnnn 

	yy tp nnnnn 

	yytpnnnnn 

	o:yy-nnnnn 

	o:yy-tp-nnnnn 

	o:yy tp nnnnn 

	o:yytpnnnnn 

where: 

yy  case year (may be 2 or 4 digits) 

nnnnn  case number (up to 5 digits) 

tp  case type (up to 2 characters) 

o  office where the case was filed (1 digit).
    
</dd>
</dl>

<dl>
<dd>

**pacer_case_id:** `typing.Optional[int]` — The PACER-assigned identifier of the target case.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The last name (for an individual) or the entity name (for a business entity) of the target party.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The first name of the target party.
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[str]` — The middle name of the target party.
    
</dd>
</dl>

<dl>
<dd>

**generation:** `typing.Optional[str]` — The suffix (e.g., Jr., III) of the target party's name.
    
</dd>
</dl>

<dl>
<dd>

**party_type:** `typing.Optional[str]` — The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
    
</dd>
</dl>

<dl>
<dd>

**party_exact_name_match:** `typing.Optional[bool]` — Specify whether the search string must match the name of the target party exactly.
    
</dd>
</dl>

<dl>
<dd>

**party_role_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` — The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
    
</dd>
</dl>

<dl>
<dd>

**case_title:** `typing.Optional[str]` 

The title of the target case. 

	Examples: 

	A search for case title john doe v will result in all cases with the case title John Doe v. 

	A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
    
</dd>
</dl>

<dl>
<dd>

**case_office:** `typing.Optional[int]` — The divisional office in which the case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_sequence_number:** `typing.Optional[int]` — The PACER-assigned sequence number of the target case. Ex 12345
    
</dd>
</dl>

<dl>
<dd>

**case_year:** `typing.Optional[int]` — The two- or four-digit year in which the target case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_type_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values. 

	Scenario: When mulitple case types needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below. 

	Example: caseTypeArray=cv&caseTypeArray=cr
    
</dd>
</dl>

<dl>
<dd>

**court_region_id_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values. 

	Scenario: When mulitple court region ids needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below. 

	Example: courtRegionIdArray=cac&courtRegionIdArray=cae
    
</dd>
</dl>

<dl>
<dd>

**case_year_from:** `typing.Optional[int]` — Limit the results of the search to those cases from the year specified or later
    
</dd>
</dl>

<dl>
<dd>

**case_year_to:** `typing.Optional[int]` — Limit the results of the search to those cases from the year specified or earlier
    
</dd>
</dl>

<dl>
<dd>

**case_filed_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_filed_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**sort_parameter_query:** `typing.Optional[str]` 

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings. 

	Scenario 1: When mulitple sort paramters needs to be requested. 

	Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below. 

	Example: sortParameterQuery=courtId,ASC&caseId,ASC 

	Scenario 2: When you want to sort the response using the case parameters in the party search. 

	Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below. 

	Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC
    
</dd>
</dl>

<dl>
<dd>

**case_status:** `typing.Optional[CriminalCourtsPacerCaseLocatorPartySearchRequestCaseStatus]` — Whether the target case is marked as 'open' or 'closed' within PACER.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — The page number of the search results to be retrieved.
    
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

<details><summary><code>client.pacer_api.<a href="src/fern/pacer_api/client.py#L2408-L2641">multi_district_courts_pacer_case_locator_party_search</a>(...) -> PclParty</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for the specified party in multidistrict litigation in PACER.
</dd>
</dl>
</dd>
</dl>

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

client.pacer_api.multi_district_courts_pacer_case_locator_party_search(
    pacer_user_id="johndoe",
    pacer_client_code="john",
    case_number="12-1234",
    last_name="John",
    first_name="John",
    middle_name="Doe",
    generation="III",
    party_type="ptf",
    party_role_array=[
        "plantiff"
    ],
    case_title="A",
    sort_parameter_query="sort=caseYear",
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

**pacer_user_id:** `str` — The username of the PACER account under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**pacer_client_code:** `str` — The PACER client code under which the search is to be performed.
    
</dd>
</dl>

<dl>
<dd>

**case_number:** `typing.Optional[str]` 

The case number of the target case. You may use the following case-number formats: 

	yy-nnnnn 

	yy-tp-nnnnn 

	yy tp nnnnn 

	yytpnnnnn 

	o:yy-nnnnn 

	o:yy-tp-nnnnn 

	o:yy tp nnnnn 

	o:yytpnnnnn 

where: 

yy  case year (may be 2 or 4 digits) 

nnnnn  case number (up to 5 digits) 

tp  case type (up to 2 characters) 

o  office where the case was filed (1 digit).
    
</dd>
</dl>

<dl>
<dd>

**jpml_number:** `typing.Optional[int]` — Master JPML Case Number.
    
</dd>
</dl>

<dl>
<dd>

**pacer_case_id:** `typing.Optional[int]` — The PACER-assigned identifier of the target case.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The last name (for an individual) or the entity name (for a business entity) of the target party.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The first name of the target party.
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[str]` — The middle name of the target party.
    
</dd>
</dl>

<dl>
<dd>

**generation:** `typing.Optional[str]` — The suffix (e.g., Jr., III) of the target party's name.
    
</dd>
</dl>

<dl>
<dd>

**party_type:** `typing.Optional[str]` — The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
    
</dd>
</dl>

<dl>
<dd>

**party_exact_name_match:** `typing.Optional[bool]` — Specify whether the search string must match the name of the target party exactly.
    
</dd>
</dl>

<dl>
<dd>

**party_role_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` — The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.
    
</dd>
</dl>

<dl>
<dd>

**case_title:** `typing.Optional[str]` 

The title of the target case. 

	Examples: 

	A search for case title john doe v will result in all cases with the case title John Doe v. 

	A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.
    
</dd>
</dl>

<dl>
<dd>

**case_office:** `typing.Optional[int]` — The divisional office in which the case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_sequence_number:** `typing.Optional[int]` — The PACER-assigned sequence number of the target case. Ex 12345
    
</dd>
</dl>

<dl>
<dd>

**case_year:** `typing.Optional[int]` — The two- or four-digit year in which the target case was filed.
    
</dd>
</dl>

<dl>
<dd>

**case_type_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values. 

	Scenario: When mulitple case types needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below. 

	Example: caseTypeArray=cv&caseTypeArray=cr
    
</dd>
</dl>

<dl>
<dd>

**court_region_id_array:** `typing.Optional[typing.Union[typing.Optional[str], typing.Sequence[typing.Optional[str]]]]` 

The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values. 

	Scenario: When mulitple court region ids needs to be requested. 

	Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below. 

	Example: courtRegionIdArray=cac&courtRegionIdArray=cae
    
</dd>
</dl>

<dl>
<dd>

**case_year_from:** `typing.Optional[int]` — Limit the results of the search to those cases from the year specified or later
    
</dd>
</dl>

<dl>
<dd>

**case_year_to:** `typing.Optional[int]` — Limit the results of the search to those cases from the year specified or earlier
    
</dd>
</dl>

<dl>
<dd>

**case_filed_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_filed_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_start_date:** `typing.Optional[datetime.datetime]` — The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**case_terminated_end_date:** `typing.Optional[datetime.datetime]` — The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).
    
</dd>
</dl>

<dl>
<dd>

**sort_parameter_query:** `typing.Optional[str]` 

How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings. 

	Scenario 1: When mulitple sort paramters needs to be requested. 

	Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below. 

	Example: sortParameterQuery=courtId,ASC&caseId,ASC 

	Scenario 2: When you want to sort the response using the case parameters in the party search. 

	Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below. 

	Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC
    
</dd>
</dl>

<dl>
<dd>

**case_status:** `typing.Optional[MultiDistrictCourtsPacerCaseLocatorPartySearchRequestCaseStatus]` — Whether the target case is marked as 'open' or 'closed' within PACER.
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — The page number of the search results to be retrieved.
    
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

## PACER Credential API
<details><summary><code>client.pacer_credential_api.<a href="src/fern/pacer_credential_api/client.py#L31-L63">get_pacer_credential</a>(...) -> PacerCredentialListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List registered PACER credentials.
</dd>
</dl>
</dd>
</dl>

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

client.pacer_credential_api.get_pacer_credential(
    page_number=1,
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

**page_number:** `typing.Optional[int]` 

The page number of the PACER credentials to be retrieved.<br>
  - Minimum: 1
    
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

<details><summary><code>client.pacer_credential_api.<a href="src/fern/pacer_credential_api/client.py#L65-L114">add_pacer_credential</a>(...) -> Success</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register PACER credentials with UniCourt.
</dd>
</dl>
</dd>
</dl>

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

client.pacer_credential_api.add_pacer_credential(
    default_pacer_client_code="Test UniCourt API",
    pacer_user_id="URKYwer3tyh5r56gq2",
    password="your password",
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

**pacer_user_id:** `str` — Pacer User Id.
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — Password.
    
</dd>
</dl>

<dl>
<dd>

**default_pacer_client_code:** `typing.Optional[str]` — Pacer Client Code.
    
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

<details><summary><code>client.pacer_credential_api.<a href="src/fern/pacer_credential_api/client.py#L116-L147">get_pacer_credential_by_id</a>(...) -> PacerCredential</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the PACER credentials for the specified PACER username.
</dd>
</dl>
</dd>
</dl>

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

client.pacer_credential_api.get_pacer_credential_by_id(
    pacer_user_id="URKYwer3tyh5r56gq2",
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

**pacer_user_id:** `str` — The PACER username for which PACER credentials are to be retrieved.
    
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

<details><summary><code>client.pacer_credential_api.<a href="src/fern/pacer_credential_api/client.py#L149-L180">remove_pacer_credential_by_id</a>(...) -> Success</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

De-register the PACER credentials for the specified PACER username.
</dd>
</dl>
</dd>
</dl>

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

client.pacer_credential_api.remove_pacer_credential_by_id(
    pacer_user_id="URKYwer3tyh5r56gq2",
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

**pacer_user_id:** `str` — The PACER username for which PACER credentials are to be retrieved.
    
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

