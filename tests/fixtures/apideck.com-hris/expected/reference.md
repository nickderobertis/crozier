# Reference
## Companies
<details><summary><code>client.companies.<a href="src/fern/companies/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Companies
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
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

Create Company
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.companies.add(
    legal_name="SpaceX",
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

**legal_name:** `str` 
    
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

**company_number:** `typing.Optional[str]` — An Company Number, Company ID or Company Code, is a unique number that has been assigned to each company.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**debtor_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.Sequence[Email]]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.Sequence[PhoneNumber]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[HrisCompanyStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**subdomain:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

Get Company
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
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

Delete Company
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
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

Update Company
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.companies.update(
    id_="id",
    legal_name="SpaceX",
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

**legal_name:** `str` 
    
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

**company_number:** `typing.Optional[str]` — An Company Number, Company ID or Company Code, is a unique number that has been assigned to each company.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**debtor_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.Sequence[Email]]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.Sequence[PhoneNumber]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[HrisCompanyStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**subdomain:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

## Departments
<details><summary><code>client.departments.<a href="src/fern/departments/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Departments
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.departments.all_(
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

<details><summary><code>client.departments.<a href="src/fern/departments/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Department
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.departments.add()

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

**code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Department name
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` — Parent ID
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

<details><summary><code>client.departments.<a href="src/fern/departments/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Department
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.departments.one(
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

<details><summary><code>client.departments.<a href="src/fern/departments/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Department
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.departments.delete(
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

<details><summary><code>client.departments.<a href="src/fern/departments/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Department
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.departments.update(
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

**code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Department name
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` — Parent ID
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

## Employees
<details><summary><code>client.employees.<a href="src/fern/employees/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Employees
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.employees.all_(
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

**filter:** `typing.Optional[EmployeesFilter]` — Apply filters
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[EmployeesSort]` — Apply sorting
    
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

<details><summary><code>client.employees.<a href="src/fern/employees/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Employee
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.employees.add()

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

**addresses:** `typing.Optional[typing.Sequence[Address]]` 
    
</dd>
</dl>

<dl>
<dd>

**birthday:** `typing.Optional[dt.date]` — The date of birth of the person.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[CompanyId]` 
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[CompanyName]` 
    
</dd>
</dl>

<dl>
<dd>

**compensations:** `typing.Optional[typing.Sequence[EmployeeCompensationsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**country_of_birth:** `typing.Optional[str]` — Country code according to ISO 3166-1 alpha-2.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.Sequence[CustomField]]` 
    
</dd>
</dl>

<dl>
<dd>

**deceased_on:** `typing.Optional[dt.date]` — The date the person deceased.
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**department:** `typing.Optional[str]` — The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field.
    
</dd>
</dl>

<dl>
<dd>

**department_id:** `typing.Optional[str]` — Unique identifier of the department ID this employee belongs to.
    
</dd>
</dl>

<dl>
<dd>

**department_name:** `typing.Optional[str]` — Name of the department this employee belongs to.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[Description]` 
    
</dd>
</dl>

<dl>
<dd>

**dietary_preference:** `typing.Optional[str]` — Indicate the employee's dietary preference.
    
</dd>
</dl>

<dl>
<dd>

**direct_reports:** `typing.Optional[typing.Sequence[str]]` — The direct reports refer to the individuals who report directly to a person in the organizational hierarchy.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — The name used to display the employee, often a combination of their first and last names.
    
</dd>
</dl>

<dl>
<dd>

**division:** `typing.Optional[Division]` 
    
</dd>
</dl>

<dl>
<dd>

**division_id:** `typing.Optional[str]` — Unique identifier of the division this employee belongs to.
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.Sequence[Email]]` 
    
</dd>
</dl>

<dl>
<dd>

**employee_number:** `typing.Optional[EmployeeNumber]` 
    
</dd>
</dl>

<dl>
<dd>

**employment_end_date:** `typing.Optional[str]` — An End Date is the date that the employee ended working at the company
    
</dd>
</dl>

<dl>
<dd>

**employment_role:** `typing.Optional[EmployeeEmploymentRole]` 
    
</dd>
</dl>

<dl>
<dd>

**employment_start_date:** `typing.Optional[str]` — A Start Date is the date that the employee started working at the company
    
</dd>
</dl>

<dl>
<dd>

**employment_status:** `typing.Optional[EmploymentStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[FirstName]` 
    
</dd>
</dl>

<dl>
<dd>

**food_allergies:** `typing.Optional[typing.Sequence[str]]` — Indicate the employee's food allergies.
    
</dd>
</dl>

<dl>
<dd>

**gender:** `typing.Optional[Gender]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**initials:** `typing.Optional[str]` — The initials of the person, usually derived from their first, middle, and last names.
    
</dd>
</dl>

<dl>
<dd>

**jobs:** `typing.Optional[typing.Sequence[EmployeeJobsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**languages:** `typing.Optional[typing.Sequence[typing.Optional[Language]]]` 
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[LastName]` 
    
</dd>
</dl>

<dl>
<dd>

**leaving_reason:** `typing.Optional[EmployeeLeavingReason]` — The reason because the employment ended.
    
</dd>
</dl>

<dl>
<dd>

**manager:** `typing.Optional[EmployeeManager]` 
    
</dd>
</dl>

<dl>
<dd>

**marital_status:** `typing.Optional[str]` — The marital status of the employee.
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[MiddleName]` 
    
</dd>
</dl>

<dl>
<dd>

**nationalities:** `typing.Optional[typing.Sequence[typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**partner:** `typing.Optional[EmployeePartner]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.Sequence[PhoneNumber]]` 
    
</dd>
</dl>

<dl>
<dd>

**photo_url:** `typing.Optional[PhotoUrl]` 
    
</dd>
</dl>

<dl>
<dd>

**preferred_language:** `typing.Optional[Language]` 
    
</dd>
</dl>

<dl>
<dd>

**preferred_name:** `typing.Optional[str]` — The name the employee prefers to be addressed by, which may be different from their legal name.
    
</dd>
</dl>

<dl>
<dd>

**pronouns:** `typing.Optional[str]` — The preferred pronouns of the person.
    
</dd>
</dl>

<dl>
<dd>

**record_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**salutation:** `typing.Optional[str]` — A formal salutation for the person. For example, 'Mr', 'Mrs'
    
</dd>
</dl>

<dl>
<dd>

**social_links:** `typing.Optional[typing.Sequence[EmployeeSocialLinksItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**social_security_number:** `typing.Optional[str]` — A unique identifier assigned by the government. This field is considered sensitive information and may be subject to special security and privacy restrictions.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` — When the employee is imported as a new hire, this field indicates what system (e.g. the name of the ATS) this employee was imported from.
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `typing.Optional[str]` — Unique identifier of the employee in the system this employee was imported from (e.g. the ID in the ATS).
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**team:** `typing.Optional[EmployeeTeam]` — The team the person is currently in.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — The time zone related to the resource. The value is a string containing a standard time zone identifier, e.g. Europe/London.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[Title]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**works_remote:** `typing.Optional[bool]` — Indicates if the employee works from a remote location.
    
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

<details><summary><code>client.employees.<a href="src/fern/employees/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Employee
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.employees.one(
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

<details><summary><code>client.employees.<a href="src/fern/employees/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Employee
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.employees.delete(
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

<details><summary><code>client.employees.<a href="src/fern/employees/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Employee
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.employees.update(
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

**addresses:** `typing.Optional[typing.Sequence[Address]]` 
    
</dd>
</dl>

<dl>
<dd>

**birthday:** `typing.Optional[dt.date]` — The date of birth of the person.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[CompanyId]` 
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[CompanyName]` 
    
</dd>
</dl>

<dl>
<dd>

**compensations:** `typing.Optional[typing.Sequence[EmployeeCompensationsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**country_of_birth:** `typing.Optional[str]` — Country code according to ISO 3166-1 alpha-2.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[typing.Sequence[CustomField]]` 
    
</dd>
</dl>

<dl>
<dd>

**deceased_on:** `typing.Optional[dt.date]` — The date the person deceased.
    
</dd>
</dl>

<dl>
<dd>

**deleted:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**department:** `typing.Optional[str]` — The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field.
    
</dd>
</dl>

<dl>
<dd>

**department_id:** `typing.Optional[str]` — Unique identifier of the department ID this employee belongs to.
    
</dd>
</dl>

<dl>
<dd>

**department_name:** `typing.Optional[str]` — Name of the department this employee belongs to.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[Description]` 
    
</dd>
</dl>

<dl>
<dd>

**dietary_preference:** `typing.Optional[str]` — Indicate the employee's dietary preference.
    
</dd>
</dl>

<dl>
<dd>

**direct_reports:** `typing.Optional[typing.Sequence[str]]` — The direct reports refer to the individuals who report directly to a person in the organizational hierarchy.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — The name used to display the employee, often a combination of their first and last names.
    
</dd>
</dl>

<dl>
<dd>

**division:** `typing.Optional[Division]` 
    
</dd>
</dl>

<dl>
<dd>

**division_id:** `typing.Optional[str]` — Unique identifier of the division this employee belongs to.
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.Sequence[Email]]` 
    
</dd>
</dl>

<dl>
<dd>

**employee_number:** `typing.Optional[EmployeeNumber]` 
    
</dd>
</dl>

<dl>
<dd>

**employment_end_date:** `typing.Optional[str]` — An End Date is the date that the employee ended working at the company
    
</dd>
</dl>

<dl>
<dd>

**employment_role:** `typing.Optional[EmployeeEmploymentRole]` 
    
</dd>
</dl>

<dl>
<dd>

**employment_start_date:** `typing.Optional[str]` — A Start Date is the date that the employee started working at the company
    
</dd>
</dl>

<dl>
<dd>

**employment_status:** `typing.Optional[EmploymentStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[FirstName]` 
    
</dd>
</dl>

<dl>
<dd>

**food_allergies:** `typing.Optional[typing.Sequence[str]]` — Indicate the employee's food allergies.
    
</dd>
</dl>

<dl>
<dd>

**gender:** `typing.Optional[Gender]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**initials:** `typing.Optional[str]` — The initials of the person, usually derived from their first, middle, and last names.
    
</dd>
</dl>

<dl>
<dd>

**jobs:** `typing.Optional[typing.Sequence[EmployeeJobsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**languages:** `typing.Optional[typing.Sequence[typing.Optional[Language]]]` 
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[LastName]` 
    
</dd>
</dl>

<dl>
<dd>

**leaving_reason:** `typing.Optional[EmployeeLeavingReason]` — The reason because the employment ended.
    
</dd>
</dl>

<dl>
<dd>

**manager:** `typing.Optional[EmployeeManager]` 
    
</dd>
</dl>

<dl>
<dd>

**marital_status:** `typing.Optional[str]` — The marital status of the employee.
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[MiddleName]` 
    
</dd>
</dl>

<dl>
<dd>

**nationalities:** `typing.Optional[typing.Sequence[typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**partner:** `typing.Optional[EmployeePartner]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.Sequence[PhoneNumber]]` 
    
</dd>
</dl>

<dl>
<dd>

**photo_url:** `typing.Optional[PhotoUrl]` 
    
</dd>
</dl>

<dl>
<dd>

**preferred_language:** `typing.Optional[Language]` 
    
</dd>
</dl>

<dl>
<dd>

**preferred_name:** `typing.Optional[str]` — The name the employee prefers to be addressed by, which may be different from their legal name.
    
</dd>
</dl>

<dl>
<dd>

**pronouns:** `typing.Optional[str]` — The preferred pronouns of the person.
    
</dd>
</dl>

<dl>
<dd>

**record_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**row_version:** `typing.Optional[RowVersion]` 
    
</dd>
</dl>

<dl>
<dd>

**salutation:** `typing.Optional[str]` — A formal salutation for the person. For example, 'Mr', 'Mrs'
    
</dd>
</dl>

<dl>
<dd>

**social_links:** `typing.Optional[typing.Sequence[EmployeeSocialLinksItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**social_security_number:** `typing.Optional[str]` — A unique identifier assigned by the government. This field is considered sensitive information and may be subject to special security and privacy restrictions.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` — When the employee is imported as a new hire, this field indicates what system (e.g. the name of the ATS) this employee was imported from.
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `typing.Optional[str]` — Unique identifier of the employee in the system this employee was imported from (e.g. the ID in the ATS).
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**team:** `typing.Optional[EmployeeTeam]` — The team the person is currently in.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — The time zone related to the resource. The value is a string containing a standard time zone identifier, e.g. Europe/London.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[Title]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**works_remote:** `typing.Optional[bool]` — Indicates if the employee works from a remote location.
    
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

## Jobs
<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Jobs for employee.
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.jobs.all_(
    employee_id="employee_id",
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

**employee_id:** `str` — ID of the employee you are acting upon.
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A Job for employee.
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.jobs.one(
    employee_id="employee_id",
    job_id="job_id",
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

**employee_id:** `str` — ID of the employee you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `str` — ID of the job you are acting upon.
    
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

## Payrolls
<details><summary><code>client.payrolls.<a href="src/fern/payrolls/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Payroll
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.payrolls.all_(
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

**filter:** `typing.Optional[PayrollsFilter]` — Apply filters
    
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

<details><summary><code>client.payrolls.<a href="src/fern/payrolls/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Payroll
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.payrolls.one(
    payroll_id="payroll_id",
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

**payroll_id:** `str` — ID of the payroll you are acting upon.
    
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

## Employee Payrolls
<details><summary><code>client.employee_payrolls.<a href="src/fern/employee_payrolls/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List payrolls for employee
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.employee_payrolls.all_(
    employee_id="employee_id",
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

**employee_id:** `str` — ID of the employee you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**raw:** `typing.Optional[bool]` — Include raw response. Mostly used for debugging purposes
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[PayrollsFilter]` — Apply filters
    
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

<details><summary><code>client.employee_payrolls.<a href="src/fern/employee_payrolls/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get payroll for employee
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.employee_payrolls.one(
    employee_id="employee_id",
    payroll_id="payroll_id",
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

**employee_id:** `str` — ID of the employee you are acting upon.
    
</dd>
</dl>

<dl>
<dd>

**payroll_id:** `str` — ID of the payroll you are acting upon.
    
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

## Employee Schedules
<details><summary><code>client.employee_schedules.<a href="src/fern/employee_schedules/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List schedules for employee, a schedule is a work pattern, not the actual worked hours, for an employee.
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.employee_schedules.all_(
    employee_id="employee_id",
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

**employee_id:** `str` — ID of the employee you are acting upon.
    
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

## Time Off Requests
<details><summary><code>client.time_off_requests.<a href="src/fern/time_off_requests/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Time Off Requests
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.time_off_requests.all_(
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

**filter:** `typing.Optional[TimeOffRequestsFilter]` — Apply filters
    
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

<details><summary><code>client.time_off_requests.<a href="src/fern/time_off_requests/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Time Off Request
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.time_off_requests.add()

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

**amount:** `typing.Optional[float]` — The amount of time off requested.
    
</dd>
</dl>

<dl>
<dd>

**approval_date:** `typing.Optional[str]` — The date the request was approved
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the time off request.
    
</dd>
</dl>

<dl>
<dd>

**employee_id:** `typing.Optional[str]` — ID of the employee
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — The end date of the time off request.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[TimeOffRequestNotes]` 
    
</dd>
</dl>

<dl>
<dd>

**policy_id:** `typing.Optional[str]` — ID of the policy
    
</dd>
</dl>

<dl>
<dd>

**request_date:** `typing.Optional[str]` — The date the request was made.
    
</dd>
</dl>

<dl>
<dd>

**request_type:** `typing.Optional[TimeOffRequestRequestType]` — The type of request
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — The start date of the time off request.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[TimeOffRequestStatus]` — The status of the time off request.
    
</dd>
</dl>

<dl>
<dd>

**units:** `typing.Optional[TimeOffRequestUnits]` — The unit of time off requested. Possible values include: `hours`, `days`, or `other`.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

<details><summary><code>client.time_off_requests.<a href="src/fern/time_off_requests/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Time Off Request
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.time_off_requests.one(
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

<details><summary><code>client.time_off_requests.<a href="src/fern/time_off_requests/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Time Off Request
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.time_off_requests.delete(
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

<details><summary><code>client.time_off_requests.<a href="src/fern/time_off_requests/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Time Off Request
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
    apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
    apideck_app_id="YOUR_APIDECK_APP_ID",
    apideck_service_id="YOUR_APIDECK_SERVICE_ID",
    api_key="YOUR_API_KEY",
)
client.time_off_requests.update(
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

**amount:** `typing.Optional[float]` — The amount of time off requested.
    
</dd>
</dl>

<dl>
<dd>

**approval_date:** `typing.Optional[str]` — The date the request was approved
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[CreatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[CreatedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the time off request.
    
</dd>
</dl>

<dl>
<dd>

**employee_id:** `typing.Optional[str]` — ID of the employee
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — The end date of the time off request.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[TimeOffRequestNotes]` 
    
</dd>
</dl>

<dl>
<dd>

**policy_id:** `typing.Optional[str]` — ID of the policy
    
</dd>
</dl>

<dl>
<dd>

**request_date:** `typing.Optional[str]` — The date the request was made.
    
</dd>
</dl>

<dl>
<dd>

**request_type:** `typing.Optional[TimeOffRequestRequestType]` — The type of request
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — The start date of the time off request.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[TimeOffRequestStatus]` — The status of the time off request.
    
</dd>
</dl>

<dl>
<dd>

**units:** `typing.Optional[TimeOffRequestUnits]` — The unit of time off requested. Possible values include: `hours`, `days`, or `other`.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[UpdatedAt]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[UpdatedBy]` 
    
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

