# Reference
## Activities
<details><summary><code>client.activities.<a href="src/fern/activities/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List activities
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.activities.all_(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[ActivitiesFilter]` — Apply filters
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.activities.<a href="src/fern/activities/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create activity
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
from fern import ActivityType, FernApi

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.activities.add(
    type=ActivityType.CALL,
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

**type:** `ActivityType` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**activity_date:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**activity_datetime:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**all_day_event:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**asset_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**attendees:** `typing.Optional[typing.Sequence[ActivityAttendee]]` 
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**case_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**child:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**contract_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.Sequence[CustomField]]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_object_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**done:** `typing.Optional[bool]` — Whether the Activity is done or not
    
</dd>
</dl>

<dl>
<dd>

**downstream_id:** `typing.Optional[str]` — The third-party API ID of original entity
    
</dd>
</dl>

<dl>
<dd>

**duration_minutes:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**duration_seconds:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**end_datetime:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**event_sub_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**group_event:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**group_event_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**lead_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**location_address:** `typing.Optional[Address]` 
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**opportunity_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**private:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**recurrent:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**reminder_datetime:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**reminder_set:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**show_as:** `typing.Optional[ActivityShowAs]` 
    
</dd>
</dl>

<dl>
<dd>

**solution_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**start_datetime:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**video_conference_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**video_conference_url:** `typing.Optional[str]` 
    
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

<details><summary><code>client.activities.<a href="src/fern/activities/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get activity
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.activities.one(
    id="id",
    fields="id,updated_at",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.activities.<a href="src/fern/activities/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete activity
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.activities.delete(
    id="id",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
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

<details><summary><code>client.activities.<a href="src/fern/activities/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update activity
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
from fern import ActivityType, FernApi

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.activities.update(
    id_="id",
    type=ActivityType.CALL,
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

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**type:** `ActivityType` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**activity_date:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**activity_datetime:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**all_day_event:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**asset_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**attendees:** `typing.Optional[typing.Sequence[ActivityAttendee]]` 
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**case_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**child:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**contract_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.Sequence[CustomField]]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_object_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**done:** `typing.Optional[bool]` — Whether the Activity is done or not
    
</dd>
</dl>

<dl>
<dd>

**downstream_id:** `typing.Optional[str]` — The third-party API ID of original entity
    
</dd>
</dl>

<dl>
<dd>

**duration_minutes:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**duration_seconds:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**end_datetime:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**event_sub_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**group_event:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**group_event_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**lead_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**location_address:** `typing.Optional[Address]` 
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**opportunity_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**private:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**recurrent:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**reminder_datetime:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**reminder_set:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**show_as:** `typing.Optional[ActivityShowAs]` 
    
</dd>
</dl>

<dl>
<dd>

**solution_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**start_datetime:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**video_conference_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**video_conference_url:** `typing.Optional[str]` 
    
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

## Companies
<details><summary><code>client.companies.<a href="src/fern/companies/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List companies
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.companies.all_(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[CompaniesFilter]` — Apply filters
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[CompaniesSort]` — Apply sorting
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.companies.<a href="src/fern/companies/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create company
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.companies.add(
    name="SpaceX",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**abn_branch:** `typing.Optional[str]` — An ABN Branch (also known as a GST Branch) is used if part of your business needs to account for GST separately from its parent entity.
    
</dd>
</dl>

<dl>
<dd>

**abn_or_tfn:** `typing.Optional[str]` — An ABN is necessary for operating a business, while a TFN (Tax File Number) is required for any person working in Australia.
    
</dd>
</dl>

<dl>
<dd>

**acn:** `typing.Optional[str]` — The Australian Company Number (ACN) is a nine digit number with the last digit being a check digit calculated using a modified modulus 10 calculation. ASIC has adopted a convention of always printing and displaying the ACN in the format XXX XXX XXX; three blocks of three characters, each block separated by a blank.
    
</dd>
</dl>

<dl>
<dd>

**addresses:** `typing.Optional[typing.Sequence[Address]]` 
    
</dd>
</dl>

<dl>
<dd>

**annual_revenue:** `typing.Optional[str]` — Annual revenue
    
</dd>
</dl>

<dl>
<dd>

**bank_accounts:** `typing.Optional[typing.Sequence[BankAccount]]` 
    
</dd>
</dl>

<dl>
<dd>

**birthday:** `typing.Optional[dt.date]` — The date of birth of the person.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.Sequence[CustomField]]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.Sequence[Email]]` 
    
</dd>
</dl>

<dl>
<dd>

**fax:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[FirstName]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**image:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**industry:** `typing.Optional[str]` — Industry
    
</dd>
</dl>

<dl>
<dd>

**interaction_count:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**last_activity_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[LastName]` 
    
</dd>
</dl>

<dl>
<dd>

**number_of_employees:** `typing.Optional[str]` — Number of employees
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ownership:** `typing.Optional[str]` — Ownership
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` — Parent ID
    
</dd>
</dl>

<dl>
<dd>

**payee_number:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.Sequence[PhoneNumber]]` 
    
</dd>
</dl>

<dl>
<dd>

**read_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**row_type:** `typing.Optional[CompanyRowType]` 
    
</dd>
</dl>

<dl>
<dd>

**sales_tax_number:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**salutation:** `typing.Optional[str]` — A formal salutation for the person. For example, 'Mr', 'Mrs'
    
</dd>
</dl>

<dl>
<dd>

**social_links:** `typing.Optional[typing.Sequence[SocialLink]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[Tags]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**vat_number:** `typing.Optional[str]` — VAT number
    
</dd>
</dl>

<dl>
<dd>

**websites:** `typing.Optional[typing.Sequence[Website]]` 
    
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

<details><summary><code>client.companies.<a href="src/fern/companies/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get company
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.companies.one(
    id="id",
    fields="id,updated_at",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.companies.<a href="src/fern/companies/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete company
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.companies.delete(
    id="id",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
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

<details><summary><code>client.companies.<a href="src/fern/companies/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update company
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.companies.update(
    id_="id",
    name="SpaceX",
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

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**abn_branch:** `typing.Optional[str]` — An ABN Branch (also known as a GST Branch) is used if part of your business needs to account for GST separately from its parent entity.
    
</dd>
</dl>

<dl>
<dd>

**abn_or_tfn:** `typing.Optional[str]` — An ABN is necessary for operating a business, while a TFN (Tax File Number) is required for any person working in Australia.
    
</dd>
</dl>

<dl>
<dd>

**acn:** `typing.Optional[str]` — The Australian Company Number (ACN) is a nine digit number with the last digit being a check digit calculated using a modified modulus 10 calculation. ASIC has adopted a convention of always printing and displaying the ACN in the format XXX XXX XXX; three blocks of three characters, each block separated by a blank.
    
</dd>
</dl>

<dl>
<dd>

**addresses:** `typing.Optional[typing.Sequence[Address]]` 
    
</dd>
</dl>

<dl>
<dd>

**annual_revenue:** `typing.Optional[str]` — Annual revenue
    
</dd>
</dl>

<dl>
<dd>

**bank_accounts:** `typing.Optional[typing.Sequence[BankAccount]]` 
    
</dd>
</dl>

<dl>
<dd>

**birthday:** `typing.Optional[dt.date]` — The date of birth of the person.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.Sequence[CustomField]]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.Sequence[Email]]` 
    
</dd>
</dl>

<dl>
<dd>

**fax:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[FirstName]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**image:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**industry:** `typing.Optional[str]` — Industry
    
</dd>
</dl>

<dl>
<dd>

**interaction_count:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**last_activity_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[LastName]` 
    
</dd>
</dl>

<dl>
<dd>

**number_of_employees:** `typing.Optional[str]` — Number of employees
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ownership:** `typing.Optional[str]` — Ownership
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` — Parent ID
    
</dd>
</dl>

<dl>
<dd>

**payee_number:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.Sequence[PhoneNumber]]` 
    
</dd>
</dl>

<dl>
<dd>

**read_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**row_type:** `typing.Optional[CompanyRowType]` 
    
</dd>
</dl>

<dl>
<dd>

**sales_tax_number:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**salutation:** `typing.Optional[str]` — A formal salutation for the person. For example, 'Mr', 'Mrs'
    
</dd>
</dl>

<dl>
<dd>

**social_links:** `typing.Optional[typing.Sequence[SocialLink]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[Tags]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**vat_number:** `typing.Optional[str]` — VAT number
    
</dd>
</dl>

<dl>
<dd>

**websites:** `typing.Optional[typing.Sequence[Website]]` 
    
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

## Contacts
<details><summary><code>client.contacts.<a href="src/fern/contacts/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List contacts
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.contacts.all_(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[ContactsFilter]` — Apply filters
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ContactsSort]` — Apply sorting
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.contacts.<a href="src/fern/contacts/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create contact
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.contacts.add(
    name="Elon Musk",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**addresses:** `typing.Optional[typing.Sequence[Address]]` 
    
</dd>
</dl>

<dl>
<dd>

**birthday:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**current_balance:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.Sequence[CustomField]]` 
    
</dd>
</dl>

<dl>
<dd>

**department:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email_domain:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.Sequence[Email]]` 
    
</dd>
</dl>

<dl>
<dd>

**fax:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**first_call_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**first_email_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**gender:** `typing.Optional[ContactGender]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**image:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — language code according to ISO 639-1. For the United States - EN
    
</dd>
</dl>

<dl>
<dd>

**last_activity_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**lead_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**lead_source:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.Sequence[PhoneNumber]]` 
    
</dd>
</dl>

<dl>
<dd>

**photo_url:** `typing.Optional[str]` — The URL of the photo of a person.
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**social_links:** `typing.Optional[typing.Sequence[SocialLink]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**suffix:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[Tags]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ContactType]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**websites:** `typing.Optional[typing.Sequence[Website]]` 
    
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

<details><summary><code>client.contacts.<a href="src/fern/contacts/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get contact
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.contacts.one(
    id="id",
    fields="id,updated_at",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.contacts.<a href="src/fern/contacts/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete contact
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.contacts.delete(
    id="id",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
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

<details><summary><code>client.contacts.<a href="src/fern/contacts/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update contact
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.contacts.update(
    id_="id",
    name="Elon Musk",
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

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**addresses:** `typing.Optional[typing.Sequence[Address]]` 
    
</dd>
</dl>

<dl>
<dd>

**birthday:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**current_balance:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.Sequence[CustomField]]` 
    
</dd>
</dl>

<dl>
<dd>

**department:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email_domain:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.Sequence[Email]]` 
    
</dd>
</dl>

<dl>
<dd>

**fax:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**first_call_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**first_email_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**gender:** `typing.Optional[ContactGender]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**image:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — language code according to ISO 639-1. For the United States - EN
    
</dd>
</dl>

<dl>
<dd>

**last_activity_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**lead_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**lead_source:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.Sequence[PhoneNumber]]` 
    
</dd>
</dl>

<dl>
<dd>

**photo_url:** `typing.Optional[str]` — The URL of the photo of a person.
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**social_links:** `typing.Optional[typing.Sequence[SocialLink]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**suffix:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[Tags]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ContactType]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**websites:** `typing.Optional[typing.Sequence[Website]]` 
    
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

## Leads
<details><summary><code>client.leads.<a href="src/fern/leads/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List leads
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.leads.all_(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[LeadsFilter]` — Apply filters
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[LeadsSort]` — Apply sorting
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.leads.<a href="src/fern/leads/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create lead
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.leads.add(
    name="Elon Musk",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**addresses:** `typing.Optional[typing.Sequence[Address]]` 
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.Sequence[CustomField]]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.Sequence[Email]]` 
    
</dd>
</dl>

<dl>
<dd>

**fax:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — language code according to ISO 639-1. For the United States - EN
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**lead_source:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**monetary_amount:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.Sequence[PhoneNumber]]` 
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**social_links:** `typing.Optional[typing.Sequence[SocialLink]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[Tags]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**websites:** `typing.Optional[typing.Sequence[Website]]` 
    
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

<details><summary><code>client.leads.<a href="src/fern/leads/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get lead
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.leads.one(
    id="id",
    fields="id,updated_at",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.leads.<a href="src/fern/leads/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete lead
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.leads.delete(
    id="id",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
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

<details><summary><code>client.leads.<a href="src/fern/leads/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update lead
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.leads.update(
    id_="id",
    name="Elon Musk",
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

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**addresses:** `typing.Optional[typing.Sequence[Address]]` 
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.Sequence[CustomField]]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.Sequence[Email]]` 
    
</dd>
</dl>

<dl>
<dd>

**fax:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — language code according to ISO 639-1. For the United States - EN
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**lead_source:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**monetary_amount:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.Sequence[PhoneNumber]]` 
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**social_links:** `typing.Optional[typing.Sequence[SocialLink]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[Tags]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**websites:** `typing.Optional[typing.Sequence[Website]]` 
    
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

## Notes
<details><summary><code>client.notes.<a href="src/fern/notes/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List notes
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.notes.all_(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.notes.<a href="src/fern/notes/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create note
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.notes.add()

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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**lead_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**opportunity_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[str]` 
    
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

<details><summary><code>client.notes.<a href="src/fern/notes/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get note
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.notes.one(
    id="id",
    fields="id,updated_at",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.notes.<a href="src/fern/notes/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete note
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.notes.delete(
    id="id",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
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

<details><summary><code>client.notes.<a href="src/fern/notes/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update note
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.notes.update(
    id_="id",
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

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**lead_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**opportunity_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[str]` 
    
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

## Opportunities
<details><summary><code>client.opportunities.<a href="src/fern/opportunities/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List opportunities
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.opportunities.all_(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[OpportunitiesFilter]` — Apply filters
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[OpportunitiesSort]` — Apply sorting
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.opportunities.<a href="src/fern/opportunities/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create opportunity
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.opportunities.add(
    title="New Rocket",
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

**title:** `str` — The title or name of the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**close_date:** `typing.Optional[dt.date]` — The actual closing date for the opportunity. If close_date is null, the opportunity is not closed yet.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` — The unique identifier of the company associated with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[str]` — The name of the company associated with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` — The unique identifier of the contact associated with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**contact_ids:** `typing.Optional[typing.Sequence[str]]` — An array of unique identifiers of all contacts associated with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` — The date and time when the opportunity was created.
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` — The unique identifier of the user who created the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.Sequence[CustomField]]` 
    
</dd>
</dl>

<dl>
<dd>

**date_last_contacted:** `typing.Optional[dt.datetime]` — The date and time when the opportunity was last contacted.
    
</dd>
</dl>

<dl>
<dd>

**date_lead_created:** `typing.Optional[dt.datetime]` — The date and time when the lead associated with the opportunity was created.
    
</dd>
</dl>

<dl>
<dd>

**date_stage_changed:** `typing.Optional[dt.datetime]` — The date and time when the stage of the opportunity was last changed.
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` — Indicates whether the opportunity has been deleted.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A description of the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**expected_revenue:** `typing.Optional[float]` — The expected revenue from the opportunity
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — A unique identifier for the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**interaction_count:** `typing.Optional[float]` — The number of interactions with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**last_activity_at:** `typing.Optional[str]` — The date and time of the last activity associated with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**lead_id:** `typing.Optional[str]` — The unique identifier of the lead associated with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**lead_source:** `typing.Optional[str]` — The source of the lead associated with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**loss_reason:** `typing.Optional[str]` — The reason why the opportunity was lost.
    
</dd>
</dl>

<dl>
<dd>

**loss_reason_id:** `typing.Optional[str]` — The unique identifier of the reason why the opportunity was lost.
    
</dd>
</dl>

<dl>
<dd>

**monetary_amount:** `typing.Optional[float]` — The monetary value associated with the opportunity
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[str]` — The unique identifier of the user who owns the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**pipeline_id:** `typing.Optional[str]` — The unique identifier of the pipeline associated with the opportunity
    
</dd>
</dl>

<dl>
<dd>

**pipeline_stage_id:** `typing.Optional[str]` — The unique identifier of the stage in the pipeline associated with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**primary_contact_id:** `typing.Optional[str]` — The unique identifier of the primary contact associated with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — The priority level of the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `typing.Optional[str]` — The unique identifier of the source of the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**stage_last_changed_at:** `typing.Optional[dt.datetime]` — The date and time when the stage of the opportunity was last changed.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The current status of the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**status_id:** `typing.Optional[str]` — The unique identifier of the current status of the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[Tags]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — The type of the opportunity
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[dt.datetime]` — The date and time when the opportunity was last updated.
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[str]` — The unique identifier of the user who last updated the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**win_probability:** `typing.Optional[float]` — The probability of winning the opportunity, expressed as a percentage.
    
</dd>
</dl>

<dl>
<dd>

**won_reason:** `typing.Optional[str]` — The reason why the opportunity was won.
    
</dd>
</dl>

<dl>
<dd>

**won_reason_id:** `typing.Optional[str]` — The unique identifier of the reason why the opportunity was won.
    
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

<details><summary><code>client.opportunities.<a href="src/fern/opportunities/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get opportunity
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.opportunities.one(
    id="id",
    fields="id,updated_at",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.opportunities.<a href="src/fern/opportunities/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete opportunity
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.opportunities.delete(
    id="id",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
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

<details><summary><code>client.opportunities.<a href="src/fern/opportunities/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update opportunity
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.opportunities.update(
    id_="id",
    title="New Rocket",
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

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` — The title or name of the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**close_date:** `typing.Optional[dt.date]` — The actual closing date for the opportunity. If close_date is null, the opportunity is not closed yet.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` — The unique identifier of the company associated with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[str]` — The name of the company associated with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` — The unique identifier of the contact associated with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**contact_ids:** `typing.Optional[typing.Sequence[str]]` — An array of unique identifiers of all contacts associated with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` — The date and time when the opportunity was created.
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` — The unique identifier of the user who created the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.Sequence[CustomField]]` 
    
</dd>
</dl>

<dl>
<dd>

**date_last_contacted:** `typing.Optional[dt.datetime]` — The date and time when the opportunity was last contacted.
    
</dd>
</dl>

<dl>
<dd>

**date_lead_created:** `typing.Optional[dt.datetime]` — The date and time when the lead associated with the opportunity was created.
    
</dd>
</dl>

<dl>
<dd>

**date_stage_changed:** `typing.Optional[dt.datetime]` — The date and time when the stage of the opportunity was last changed.
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` — Indicates whether the opportunity has been deleted.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A description of the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**expected_revenue:** `typing.Optional[float]` — The expected revenue from the opportunity
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — A unique identifier for the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**interaction_count:** `typing.Optional[float]` — The number of interactions with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**last_activity_at:** `typing.Optional[str]` — The date and time of the last activity associated with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**lead_id:** `typing.Optional[str]` — The unique identifier of the lead associated with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**lead_source:** `typing.Optional[str]` — The source of the lead associated with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**loss_reason:** `typing.Optional[str]` — The reason why the opportunity was lost.
    
</dd>
</dl>

<dl>
<dd>

**loss_reason_id:** `typing.Optional[str]` — The unique identifier of the reason why the opportunity was lost.
    
</dd>
</dl>

<dl>
<dd>

**monetary_amount:** `typing.Optional[float]` — The monetary value associated with the opportunity
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[str]` — The unique identifier of the user who owns the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**pipeline_id:** `typing.Optional[str]` — The unique identifier of the pipeline associated with the opportunity
    
</dd>
</dl>

<dl>
<dd>

**pipeline_stage_id:** `typing.Optional[str]` — The unique identifier of the stage in the pipeline associated with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**primary_contact_id:** `typing.Optional[str]` — The unique identifier of the primary contact associated with the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[str]` — The priority level of the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `typing.Optional[str]` — The unique identifier of the source of the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**stage_last_changed_at:** `typing.Optional[dt.datetime]` — The date and time when the stage of the opportunity was last changed.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — The current status of the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**status_id:** `typing.Optional[str]` — The unique identifier of the current status of the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[Tags]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — The type of the opportunity
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[dt.datetime]` — The date and time when the opportunity was last updated.
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[str]` — The unique identifier of the user who last updated the opportunity.
    
</dd>
</dl>

<dl>
<dd>

**win_probability:** `typing.Optional[float]` — The probability of winning the opportunity, expressed as a percentage.
    
</dd>
</dl>

<dl>
<dd>

**won_reason:** `typing.Optional[str]` — The reason why the opportunity was won.
    
</dd>
</dl>

<dl>
<dd>

**won_reason_id:** `typing.Optional[str]` — The unique identifier of the reason why the opportunity was won.
    
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

## Pipelines
<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List pipelines
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.pipelines.all_(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create pipeline
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.pipelines.add(
    name="Sales Pipeline",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` — The date and time when the object was created.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**display_order:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**stages:** `typing.Optional[typing.Sequence[PipelineStagesItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[dt.datetime]` — The date and time when the object was last updated.
    
</dd>
</dl>

<dl>
<dd>

**win_probability_enabled:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get pipeline
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.pipelines.one(
    id="id",
    fields="id,updated_at",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete pipeline
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.pipelines.delete(
    id="id",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
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

<details><summary><code>client.pipelines.<a href="src/fern/pipelines/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update pipeline
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.pipelines.update(
    id_="id",
    name="Sales Pipeline",
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

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` — The date and time when the object was created.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**display_order:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**stages:** `typing.Optional[typing.Sequence[PipelineStagesItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[dt.datetime]` — The date and time when the object was last updated.
    
</dd>
</dl>

<dl>
<dd>

**win_probability_enabled:** `typing.Optional[bool]` 
    
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

## Users
<details><summary><code>client.users.<a href="src/fern/users/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List users
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.users.all_(
    fields="id,updated_at",
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

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return. Minimum 1, Maximum 200, Default 20
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.users.<a href="src/fern/users/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create user
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
from fern import Email, FernApi

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.users.add(
    emails=[
        Email(
            email="elon@musk.com",
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

**emails:** `typing.Sequence[Email]` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**addresses:** `typing.Optional[typing.Sequence[Address]]` 
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[str]` — The name of the company.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**department:** `typing.Optional[str]` — The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A description of the object.
    
</dd>
</dl>

<dl>
<dd>

**division:** `typing.Optional[str]` — The division the person is currently in. Usually a collection of departments or teams or regions.
    
</dd>
</dl>

<dl>
<dd>

**employee_number:** `typing.Optional[str]` — An Employee Number, Employee ID or Employee Code, is a unique number that has been assigned to each individual staff member within a company.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[FirstName]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**image:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — language code according to ISO 639-1. For the United States - EN
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[LastName]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.Sequence[PhoneNumber]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The job title of the person.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` 
    
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

<details><summary><code>client.users.<a href="src/fern/users/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get user
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.users.one(
    id="id",
    fields="id,updated_at",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.
    
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

<details><summary><code>client.users.<a href="src/fern/users/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete user
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

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.users.delete(
    id="id",
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

**id:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
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

<details><summary><code>client.users.<a href="src/fern/users/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update user
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
from fern import Email, FernApi

client = FernApi(
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    api_key="YOUR_API_KEY",
)
client.users.update(
    id_="id",
    emails=[
        Email(
            email="elon@musk.com",
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

**id_:** `str` — ID of the record you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Sequence[Email]` 
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**addresses:** `typing.Optional[typing.Sequence[Address]]` 
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[str]` — The name of the company.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**department:** `typing.Optional[str]` — The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A description of the object.
    
</dd>
</dl>

<dl>
<dd>

**division:** `typing.Optional[str]` — The division the person is currently in. Usually a collection of departments or teams or regions.
    
</dd>
</dl>

<dl>
<dd>

**employee_number:** `typing.Optional[str]` — An Employee Number, Employee ID or Employee Code, is a unique number that has been assigned to each individual staff member within a company.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[FirstName]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**image:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — language code according to ISO 639-1. For the United States - EN
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[LastName]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.Sequence[PhoneNumber]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The job title of the person.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` 
    
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

