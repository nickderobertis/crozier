# Reference
## Customers
<details><summary><code>client.customers.<a href="src/fern/customers/client.py">all_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Customer Support Customers
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
client.customers.all_(
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

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Customer Support Customer
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
client.customers.add()

```
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

**bank_accounts:** `typing.Optional[BankAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[CompanyName]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` — The date and time when the object was created.
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` — The user who created the object.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.Sequence[Email]]` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[FirstName]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — A unique identifier for an object.
    
</dd>
</dl>

<dl>
<dd>

**individual:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[LastName]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.Sequence[PhoneNumber]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[CustomerSupportCustomerStatus]` — Customer status
    
</dd>
</dl>

<dl>
<dd>

**tax_number:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[dt.datetime]` — The date and time when the object was last updated.
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[str]` — The user who last updated the object.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">one</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Customer Support Customer
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
client.customers.one(
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

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Customer Support Customer
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
client.customers.delete(
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

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Customer Support Customer
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
client.customers.update(
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

**bank_accounts:** `typing.Optional[BankAccount]` 
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[CompanyName]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` — The date and time when the object was created.
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` — The user who created the object.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[Currency]` 
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.Sequence[Email]]` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[FirstName]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — A unique identifier for an object.
    
</dd>
</dl>

<dl>
<dd>

**individual:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[LastName]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[typing.Sequence[PhoneNumber]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[CustomerSupportCustomerStatus]` — Customer status
    
</dd>
</dl>

<dl>
<dd>

**tax_number:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[dt.datetime]` — The date and time when the object was last updated.
    
</dd>
</dl>

<dl>
<dd>

**updated_by:** `typing.Optional[str]` — The user who last updated the object.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

