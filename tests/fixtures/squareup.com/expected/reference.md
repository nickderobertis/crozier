# Reference
## MobileAuthorization
<details><summary><code>client.mobile_authorization.<a href="src/fern/mobile_authorization/client.py">create_mobile_authorization_code</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates code to authorize a mobile application to connect to a Square card reader

Authorization codes are one-time-use and expire __60 minutes__ after being issued.

__Important:__ The `Authorization` header you provide to this endpoint must have the following format:

```
Authorization: Bearer ACCESS_TOKEN
```

Replace `ACCESS_TOKEN` with a
[valid production authorization credential](https://developer.squareup.com/docs/build-basics/access-tokens).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.mobile_authorization.create_mobile_authorization_code()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `typing.Optional[str]` — The Square location ID the authorization code should be tied to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## OAuth
<details><summary><code>client.o_auth.<a href="src/fern/o_auth/client.py">renew_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`RenewToken` is deprecated. For information about refreshing OAuth access tokens, see
[Migrate from Renew to Refresh OAuth Tokens](https://developer.squareup.com/docs/oauth-api/migrate-to-refresh-tokens).


Renews an OAuth access token before it expires.

OAuth access tokens besides your application's personal access token expire after __30 days__.
You can also renew expired tokens within __15 days__ of their expiration.
You cannot renew an access token that has been expired for more than 15 days.
Instead, the associated user must re-complete the OAuth flow from the beginning.

__Important:__ The `Authorization` header for this endpoint must have the
following format:

```
Authorization: Client APPLICATION_SECRET
```

Replace `APPLICATION_SECRET` with the application secret on the Credentials
page in the [developer dashboard](https://developer.squareup.com/apps).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.o_auth.renew_token(
    client_id="client_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` — Your application ID, available from the [developer dashboard](https://developer.squareup.com/apps).
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` — The token you want to renew.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.o_auth.<a href="src/fern/o_auth/client.py">revoke_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revokes an access token generated with the OAuth flow.

If an account has more than one OAuth access token for your application, this
endpoint revokes all of them, regardless of which token you specify. When an
OAuth access token is revoked, all of the active subscriptions associated
with that OAuth token are canceled immediately.

__Important:__ The `Authorization` header for this endpoint must have the
following format:

```
Authorization: Client APPLICATION_SECRET
```

Replace `APPLICATION_SECRET` with the application secret on the OAuth
page in the [developer dashboard](https://developer.squareup.com/apps).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.o_auth.revoke_token()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**access_token:** `typing.Optional[str]` 

The access token of the merchant whose token you want to revoke.
Do not provide a value for merchant_id if you provide this parameter.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` 

The Square issued ID for your application, available from the
[developer dashboard](https://developer.squareup.com/apps).
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `typing.Optional[str]` 

The ID of the merchant whose token you want to revoke.
Do not provide a value for access_token if you provide this parameter.
    
</dd>
</dl>

<dl>
<dd>

**revoke_only_access_token:** `typing.Optional[bool]` 

If `true`, terminate the given single access token, but do not
terminate the entire authorization.
Default: `false`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.o_auth.<a href="src/fern/o_auth/client.py">obtain_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an OAuth access token.

The endpoint supports distinct methods of obtaining OAuth access tokens.
Applications specify a method by adding the `grant_type` parameter
in the request and also provide relevant information.

__Note:__ Regardless of the method application specified,
the endpoint always returns two items; an OAuth access token and
a refresh token in the response.

__OAuth tokens should only live on secure servers. Application clients
should never interact directly with OAuth tokens__.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.o_auth.obtain_token(
    client_id="client_id",
    client_secret="client_secret",
    grant_type="grant_type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 

The Square-issued ID of your application, available from the
[developer dashboard](https://developer.squareup.com/apps).
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` 

The Square-issued application secret for your application, available
from the [developer dashboard](https://developer.squareup.com/apps).
    
</dd>
</dl>

<dl>
<dd>

**grant_type:** `str` 

Specifies the method to request an OAuth access token.
Valid values are: `authorization_code`, `refresh_token`, and `migration_token`
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` 

The authorization code to exchange.
This is required if `grant_type` is set to `authorization_code`, to indicate that
the application wants to exchange an authorization code for an OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**migration_token:** `typing.Optional[str]` 

Legacy OAuth access token obtained using a Connect API version prior
to 2019-03-13. This parameter is required if `grant_type` is set to
`migration_token` to indicate that the application wants to get a replacement
OAuth access token. The response also returns a refresh token.
For more information, see [Migrate to Using Refresh Tokens](https://developer.squareup.com/docs/oauth-api/migrate-to-refresh-tokens).
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `typing.Optional[str]` — The redirect URL assigned in the [developer dashboard](https://developer.squareup.com/apps).
    
</dd>
</dl>

<dl>
<dd>

**refresh_token:** `typing.Optional[str]` 

A valid refresh token for generating a new OAuth access token.
A valid refresh token is required if `grant_type` is set to `refresh_token` , to indicate the application wants a replacement for an expired OAuth access token.
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.Optional[typing.Sequence[str]]` 

A JSON list of strings representing the permissions the application is requesting.
For example: "`["MERCHANT_PROFILE_READ","PAYMENTS_READ","BANK_ACCOUNTS_READ"]`"
The access token returned in the response is granted the permissions
that comprise the intersection between the requested list of permissions, and those
that belong to the provided refresh token.
    
</dd>
</dl>

<dl>
<dd>

**short_lived:** `typing.Optional[bool]` 

A boolean indicating a request for a short-lived access token.
The short-lived access token returned in the response will expire in 24 hours.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V1Employees
<details><summary><code>client.v1employees.<a href="src/fern/v1employees/client.py">list_employees</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides summary information for all of a business's employees.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.v1employees.list_employees()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[str]` — The order in which employees are listed in the response, based on their created_at field.      Default value: ASC
    
</dd>
</dl>

<dl>
<dd>

**begin_updated_at:** `typing.Optional[str]` — If filtering results by their updated_at field, the beginning of the requested reporting period, in ISO 8601 format
    
</dd>
</dl>

<dl>
<dd>

**end_updated_at:** `typing.Optional[str]` — If filtering results by there updated_at field, the end of the requested reporting period, in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**begin_created_at:** `typing.Optional[str]` — If filtering results by their created_at field, the beginning of the requested reporting period, in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**end_created_at:** `typing.Optional[str]` — If filtering results by their created_at field, the end of the requested reporting period, in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — If provided, the endpoint returns only employee entities with the specified status (ACTIVE or INACTIVE).
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[str]` — If provided, the endpoint returns only employee entities with the specified external_id.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum integer number of employee entities to return in a single response. Default 100, maximum 200.
    
</dd>
</dl>

<dl>
<dd>

**batch_token:** `typing.Optional[str]` 

A pagination cursor to retrieve the next set of results for your
original query to the endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1employees.<a href="src/fern/v1employees/client.py">create_employee</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

 Use the CreateEmployee endpoint to add an employee to a Square
account. Employees created with the Connect API have an initial status
of `INACTIVE`. Inactive employees cannot sign in to Square Point of Sale
until they are activated from the Square Dashboard. Employee status
cannot be changed with the Connect API.

Employee entities cannot be deleted. To disable employee profiles,
set the employee's status to <code>INACTIVE</code>
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.v1employees.create_employee(
    first_name="first_name",
    last_name="last_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**first_name:** `str` — The employee's first name.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `str` — The employee's last name.
    
</dd>
</dl>

<dl>
<dd>

**authorized_location_ids:** `typing.Optional[typing.Sequence[str]]` — The IDs of the locations the employee is allowed to clock in at.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[str]` — The time when the employee entity was created, in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — The employee's email address.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[str]` — An ID the merchant can set to associate the employee with an entity in another system.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — The employee's unique ID.
    
</dd>
</dl>

<dl>
<dd>

**role_ids:** `typing.Optional[typing.Sequence[str]]` — The ids of the employee's associated roles. Currently, you can specify only one or zero roles per employee.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Whether the employee is ACTIVE or INACTIVE. Inactive employees cannot sign in to Square Register.Merchants update this field from the Square Dashboard.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[str]` — The time when the employee entity was most recently updated, in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1employees.<a href="src/fern/v1employees/client.py">retrieve_employee</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides the details for a single employee.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.v1employees.retrieve_employee(
    employee_id="employee_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**employee_id:** `str` — The employee's ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1employees.<a href="src/fern/v1employees/client.py">update_employee</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.v1employees.update_employee(
    employee_id="employee_id",
    first_name="first_name",
    last_name="last_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**employee_id:** `str` — The ID of the role to modify.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `str` — The employee's first name.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `str` — The employee's last name.
    
</dd>
</dl>

<dl>
<dd>

**authorized_location_ids:** `typing.Optional[typing.Sequence[str]]` — The IDs of the locations the employee is allowed to clock in at.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[str]` — The time when the employee entity was created, in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — The employee's email address.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[str]` — An ID the merchant can set to associate the employee with an entity in another system.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — The employee's unique ID.
    
</dd>
</dl>

<dl>
<dd>

**role_ids:** `typing.Optional[typing.Sequence[str]]` — The ids of the employee's associated roles. Currently, you can specify only one or zero roles per employee.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Whether the employee is ACTIVE or INACTIVE. Inactive employees cannot sign in to Square Register.Merchants update this field from the Square Dashboard.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[str]` — The time when the employee entity was most recently updated, in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1employees.<a href="src/fern/v1employees/client.py">list_employee_roles</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides summary information for all of a business's employee roles.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.v1employees.list_employee_roles()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[str]` — The order in which employees are listed in the response, based on their created_at field.Default value: ASC
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum integer number of employee entities to return in a single response. Default 100, maximum 200.
    
</dd>
</dl>

<dl>
<dd>

**batch_token:** `typing.Optional[str]` 

A pagination cursor to retrieve the next set of results for your
original query to the endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1employees.<a href="src/fern/v1employees/client.py">create_employee_role</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an employee role you can then assign to employees.

Square accounts can include any number of roles that can be assigned to
employees. These roles define the actions and permissions granted to an
employee with that role. For example, an employee with a "Shift Manager"
role might be able to issue refunds in Square Point of Sale, whereas an
employee with a "Clerk" role might not.

Roles are assigned with the [V1UpdateEmployee](https://developer.squareup.com/reference/square_2021-08-18/v1-employees-api/update-employee-role)
endpoint. An employee can have only one role at a time.

If an employee has no role, they have none of the permissions associated
with roles. All employees can accept payments with Square Point of Sale.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.v1employees.create_employee_role(
    name="name",
    permissions=["permissions"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The role's merchant-defined name.
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.Sequence[str]` — The role's permissions.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[str]` — The time when the employee entity was created, in ISO 8601 format. Is set by Square when the Role is created.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — The role's unique ID, Can only be set by Square.
    
</dd>
</dl>

<dl>
<dd>

**is_owner:** `typing.Optional[bool]` — If true, employees with this role have all permissions, regardless of the values indicated in permissions.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[str]` — The time when the employee entity was most recently updated, in ISO 8601 format. Is set by Square when the Role updated.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1employees.<a href="src/fern/v1employees/client.py">retrieve_employee_role</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides the details for a single employee role.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.v1employees.retrieve_employee_role(
    role_id="role_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**role_id:** `str` — The role's ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1employees.<a href="src/fern/v1employees/client.py">update_employee_role</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modifies the details of an employee role.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.v1employees.update_employee_role(
    role_id="role_id",
    name="name",
    permissions=["permissions"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**role_id:** `str` — The ID of the role to modify.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The role's merchant-defined name.
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.Sequence[str]` — The role's permissions.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[str]` — The time when the employee entity was created, in ISO 8601 format. Is set by Square when the Role is created.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — The role's unique ID, Can only be set by Square.
    
</dd>
</dl>

<dl>
<dd>

**is_owner:** `typing.Optional[bool]` — If true, employees with this role have all permissions, regardless of the values indicated in permissions.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[str]` — The time when the employee entity was most recently updated, in ISO 8601 format. Is set by Square when the Role updated.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V1Transactions
<details><summary><code>client.v1transactions.<a href="src/fern/v1transactions/client.py">list_orders</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides summary information for a merchant's online store orders.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.v1transactions.list_orders(
    location_id="location_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the location to list online store orders for.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — The order in which payments are listed in the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of payments to return in a single response. This value cannot exceed 200.
    
</dd>
</dl>

<dl>
<dd>

**batch_token:** `typing.Optional[str]` 

A pagination cursor to retrieve the next set of results for your
original query to the endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1transactions.<a href="src/fern/v1transactions/client.py">retrieve_order</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides comprehensive information for a single online store order, including the order's history.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.v1transactions.retrieve_order(
    location_id="location_id",
    order_id="order_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the order's associated location.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — The order's Square-issued ID. You obtain this value from Order objects returned by the List Orders endpoint
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1transactions.<a href="src/fern/v1transactions/client.py">update_order</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the details of an online store order. Every update you perform on an order corresponds to one of three actions:
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.v1transactions.update_order(
    location_id="location_id",
    order_id="order_id",
    action="action",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the order's associated location.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — The order's Square-issued ID. You obtain this value from Order objects returned by the List Orders endpoint
    
</dd>
</dl>

<dl>
<dd>

**action:** `str` — The action to perform on the order (COMPLETE, CANCEL, or REFUND).
    
</dd>
</dl>

<dl>
<dd>

**canceled_note:** `typing.Optional[str]` — A merchant-specified note about the canceling of the order. Only valid if action is CANCEL.
    
</dd>
</dl>

<dl>
<dd>

**completed_note:** `typing.Optional[str]` — A merchant-specified note about the completion of the order. Only valid if action is COMPLETE.
    
</dd>
</dl>

<dl>
<dd>

**refunded_note:** `typing.Optional[str]` — A merchant-specified note about the refunding of the order. Only valid if action is REFUND.
    
</dd>
</dl>

<dl>
<dd>

**shipped_tracking_number:** `typing.Optional[str]` — The tracking number of the shipment associated with the order. Only valid if action is COMPLETE.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1transactions.<a href="src/fern/v1transactions/client.py">list_payments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides summary information for all payments taken for a given
Square account during a date range. Date ranges cannot exceed 1 year in
length. See Date ranges for details of inclusive and exclusive dates.

*Note**: Details for payments processed with Square Point of Sale while
in offline mode may not be transmitted to Square for up to 72 hours.
Offline payments have a `created_at` value that reflects the time the
payment was originally processed, not the time it was subsequently
transmitted to Square. Consequently, the ListPayments endpoint might
list an offline payment chronologically between online payments that
were seen in a previous request.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.v1transactions.list_payments(
    location_id="location_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the location to list payments for. If you specify me, this endpoint returns payments aggregated from all of the business's locations.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — The order in which payments are listed in the response.
    
</dd>
</dl>

<dl>
<dd>

**begin_time:** `typing.Optional[str]` — The beginning of the requested reporting period, in ISO 8601 format. If this value is before January 1, 2013 (2013-01-01T00:00:00Z), this endpoint returns an error. Default value: The current time minus one year.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — The end of the requested reporting period, in ISO 8601 format. If this value is more than one year greater than begin_time, this endpoint returns an error. Default value: The current time.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of payments to return in a single response. This value cannot exceed 200.
    
</dd>
</dl>

<dl>
<dd>

**batch_token:** `typing.Optional[str]` 

A pagination cursor to retrieve the next set of results for your
original query to the endpoint.
    
</dd>
</dl>

<dl>
<dd>

**include_partial:** `typing.Optional[bool]` — Indicates whether or not to include partial payments in the response. Partial payments will have the tenders collected so far, but the itemizations will be empty until the payment is completed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1transactions.<a href="src/fern/v1transactions/client.py">retrieve_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides comprehensive information for a single payment.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.v1transactions.retrieve_payment(
    location_id="location_id",
    payment_id="payment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the payment's associated location.
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `str` — The Square-issued payment ID. payment_id comes from Payment objects returned by the List Payments endpoint, Settlement objects returned by the List Settlements endpoint, or Refund objects returned by the List Refunds endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1transactions.<a href="src/fern/v1transactions/client.py">list_refunds</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides the details for all refunds initiated by a merchant or any of the merchant's mobile staff during a date range. Date ranges cannot exceed one year in length.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.v1transactions.list_refunds(
    location_id="location_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the location to list refunds for.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — The order in which payments are listed in the response.
    
</dd>
</dl>

<dl>
<dd>

**begin_time:** `typing.Optional[str]` — The beginning of the requested reporting period, in ISO 8601 format. If this value is before January 1, 2013 (2013-01-01T00:00:00Z), this endpoint returns an error. Default value: The current time minus one year.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — The end of the requested reporting period, in ISO 8601 format. If this value is more than one year greater than begin_time, this endpoint returns an error. Default value: The current time.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The approximate number of refunds to return in a single response. Default: 100. Max: 200. Response may contain more results than the prescribed limit when refunds are made simultaneously to multiple tenders in a payment or when refunds are generated in an exchange to account for the value of returned goods.
    
</dd>
</dl>

<dl>
<dd>

**batch_token:** `typing.Optional[str]` 

A pagination cursor to retrieve the next set of results for your
original query to the endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1transactions.<a href="src/fern/v1transactions/client.py">create_refund</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Issues a refund for a previously processed payment. You must issue
a refund within 60 days of the associated payment.

You cannot issue a partial refund for a split tender payment. You must
instead issue a full or partial refund for a particular tender, by
providing the applicable tender id to the V1CreateRefund endpoint.
Issuing a full refund for a split tender payment refunds all tenders
associated with the payment.

Issuing a refund for a card payment is not reversible. For development
purposes, you can create fake cash payments in Square Point of Sale and
refund them.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.v1transactions.create_refund(
    location_id="location_id",
    payment_id="payment_id",
    reason="reason",
    type="type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the original payment's associated location.
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `str` 

The ID of the payment to refund. If you are creating a `PARTIAL`
refund for a split tender payment, instead provide the id of the
particular tender you want to refund.
    
</dd>
</dl>

<dl>
<dd>

**reason:** `str` — The reason for the refund.
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The type of refund (FULL or PARTIAL).
    
</dd>
</dl>

<dl>
<dd>

**refunded_money:** `typing.Optional[V1Money]` 
    
</dd>
</dl>

<dl>
<dd>

**request_idempotence_key:** `typing.Optional[str]` — An optional key to ensure idempotence if you issue the same PARTIAL refund request more than once.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1transactions.<a href="src/fern/v1transactions/client.py">list_settlements</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides summary information for all deposits and withdrawals
initiated by Square to a linked bank account during a date range. Date
ranges cannot exceed one year in length.

*Note**: the ListSettlements endpoint does not provide entry
information.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.v1transactions.list_settlements(
    location_id="location_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the location to list settlements for. If you specify me, this endpoint returns settlements aggregated from all of the business's locations.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — The order in which settlements are listed in the response.
    
</dd>
</dl>

<dl>
<dd>

**begin_time:** `typing.Optional[str]` — The beginning of the requested reporting period, in ISO 8601 format. If this value is before January 1, 2013 (2013-01-01T00:00:00Z), this endpoint returns an error. Default value: The current time minus one year.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — The end of the requested reporting period, in ISO 8601 format. If this value is more than one year greater than begin_time, this endpoint returns an error. Default value: The current time.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of settlements to return in a single response. This value cannot exceed 200.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Provide this parameter to retrieve only settlements with a particular status (SENT or FAILED).
    
</dd>
</dl>

<dl>
<dd>

**batch_token:** `typing.Optional[str]` 

A pagination cursor to retrieve the next set of results for your
original query to the endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1transactions.<a href="src/fern/v1transactions/client.py">retrieve_settlement</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides comprehensive information for a single settlement.

The returned `Settlement` objects include an `entries` field that lists
the transactions that contribute to the settlement total. Most
settlement entries correspond to a payment payout, but settlement
entries are also generated for less common events, like refunds, manual
adjustments, or chargeback holds.

Square initiates its regular deposits as indicated in the
[Deposit Options with Square](https://squareup.com/help/us/en/article/3807)
help article. Details for a regular deposit are usually not available
from Connect API endpoints before 10 p.m. PST the same day.

Square does not know when an initiated settlement **completes**, only
whether it has failed. A completed settlement is typically reflected in
a bank account within 3 business days, but in exceptional cases it may
take longer.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.v1transactions.retrieve_settlement(
    location_id="location_id",
    settlement_id="settlement_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the settlements's associated location.
    
</dd>
</dl>

<dl>
<dd>

**settlement_id:** `str` — The settlement's Square-issued ID. You obtain this value from Settlement objects returned by the List Settlements endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ApplePay
<details><summary><code>client.apple_pay.<a href="src/fern/apple_pay/client.py">register_domain</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Activates a domain for use with Apple Pay on the Web and Square. A validation
is performed on this domain by Apple to ensure that it is properly set up as
an Apple Pay enabled domain.

This endpoint provides an easy way for platform developers to bulk activate
Apple Pay on the Web with Square for merchants using their platform.

To learn more about Web Apple Pay, see
[Add the Apple Pay on the Web Button](https://developer.squareup.com/docs/payment-form/add-digital-wallets/apple-pay).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.apple_pay.register_domain(
    domain_name="domain_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_name:** `str` — A domain name as described in RFC-1034 that will be registered with ApplePay.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## BankAccounts
<details><summary><code>client.bank_accounts.<a href="src/fern/bank_accounts/client.py">list_bank_accounts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount) objects linked to a Square account.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.bank_accounts.list_bank_accounts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The pagination cursor returned by a previous call to this endpoint.
Use it in the next `ListBankAccounts` request to retrieve the next set 
of results.

See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

Upper limit on the number of bank accounts to return in the response. 
Currently, 1000 is the largest supported limit. You can specify a limit 
of up to 1000 bank accounts. This is also the default limit.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

Location ID. You can specify this optional filter 
to retrieve only the linked bank accounts belonging to a specific location.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bank_accounts.<a href="src/fern/bank_accounts/client.py">get_bank_account_by_v1id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details of a [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount) identified by V1 bank account ID.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.bank_accounts.get_bank_account_by_v1id(
    v1bank_account_id="v1_bank_account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**v1bank_account_id:** `str` 

Connect V1 ID of the desired `BankAccount`. For more information, see 
[Retrieve a bank account by using an ID issued by V1 Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api#retrieve-a-bank-account-by-using-an-id-issued-by-v1-bank-accounts-api).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bank_accounts.<a href="src/fern/bank_accounts/client.py">get_bank_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details of a [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount)
linked to a Square account.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.bank_accounts.get_bank_account(
    bank_account_id="bank_account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bank_account_id:** `str` — Square-issued ID of the desired `BankAccount`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Bookings
<details><summary><code>client.bookings.<a href="src/fern/bookings/client.py">create_booking</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a booking.
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
from fern import AppointmentSegment, Booking, FernApi

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.bookings.create_booking(
    booking=Booking(
        appointment_segments=[
            AppointmentSegment(
                duration_minutes=60,
                service_variation_id="RU3PBTZTK7DXZDQFCJHOK2MC",
                service_variation_version=1599775456731,
                team_member_id="TMXUrsBWWcHTt79t",
            )
        ],
        customer_id="EX2QSVGTZN4K1E5QE1CBFNVQ8M",
        location_id="LEQHH0YY8B42M",
        start_at="2020-11-26T13:00:00Z",
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

**booking:** `Booking` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — A unique key to make this request an idempotent operation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.<a href="src/fern/bookings/client.py">search_availability</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for availabilities for booking.
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
from fern import (
    FernApi,
    FilterValue,
    SearchAvailabilityFilter,
    SearchAvailabilityQuery,
    SegmentFilter,
    TimeRange,
)

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.bookings.search_availability(
    query=SearchAvailabilityQuery(
        filter=SearchAvailabilityFilter(
            location_id="LEQHH0YY8B42M",
            segment_filters=[
                SegmentFilter(
                    service_variation_id="RU3PBTZTK7DXZDQFCJHOK2MC",
                    team_member_id_filter=FilterValue(
                        any=["TMXUrsBWWcHTt79t", "TMaJcbiRqPIGZuS9"],
                    ),
                )
            ],
            start_at_range=TimeRange(
                end_at="2020-11-27T13:00:00Z",
                start_at="2020-11-26T13:00:00Z",
            ),
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

**query:** `SearchAvailabilityQuery` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.<a href="src/fern/bookings/client.py">retrieve_business_booking_profile</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a seller's booking profile.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.bookings.retrieve_business_booking_profile()

```
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

<details><summary><code>client.bookings.<a href="src/fern/bookings/client.py">list_team_member_booking_profiles</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists booking profiles for team members.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.bookings.list_team_member_booking_profiles()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bookable_only:** `typing.Optional[bool]` — Indicates whether to include only bookable team members in the returned result (`true`) or not (`false`).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The cursor for paginating through the results.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` — Indicates whether to include only team members enabled at the given location in the returned result.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.<a href="src/fern/bookings/client.py">retrieve_team_member_booking_profile</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a team member's booking profile.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.bookings.retrieve_team_member_booking_profile(
    team_member_id="team_member_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_member_id:** `str` — The ID of the team member to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.<a href="src/fern/bookings/client.py">retrieve_booking</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a booking.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.bookings.retrieve_booking(
    booking_id="booking_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**booking_id:** `str` — The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-retrieved booking.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.<a href="src/fern/bookings/client.py">update_booking</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a booking.
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
from fern import Booking, FernApi

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.bookings.update_booking(
    booking_id="booking_id",
    booking=Booking(
        customer_note="I would like to sit near the window please",
        version=1,
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

**booking_id:** `str` — The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-updated booking.
    
</dd>
</dl>

<dl>
<dd>

**booking:** `Booking` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — A unique key to make this request an idempotent operation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.<a href="src/fern/bookings/client.py">cancel_booking</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels an existing booking.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.bookings.cancel_booking(
    booking_id="booking_id",
    booking_version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**booking_id:** `str` — The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-cancelled booking.
    
</dd>
</dl>

<dl>
<dd>

**booking_version:** `typing.Optional[int]` — The revision number for the booking used for optimistic concurrency.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — A unique key to make this request an idempotent operation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Cards
<details><summary><code>client.cards.<a href="src/fern/cards/client.py">list_cards</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of cards owned by the account making the request.
A max of 25 cards will be returned.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.cards.list_cards()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for your original query.

See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` 

Limit results to cards associated with the customer supplied.
By default, all cards owned by the merchant are returned.
    
</dd>
</dl>

<dl>
<dd>

**include_disabled:** `typing.Optional[bool]` 

Includes disabled cards.
By default, all enabled cards owned by the merchant are returned.
    
</dd>
</dl>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` — Limit results to cards associated with the reference_id supplied.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[str]` 

Sorts the returned list by when the card was created with the specified order.
This field defaults to ASC.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cards.<a href="src/fern/cards/client.py">create_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a card on file to an existing merchant.
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
from fern import Card, FernApi

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.cards.create_card(
    card=Card(),
    idempotency_key="idempotency_key",
    source_id="source_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**card:** `Card` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this CreateCard request. Keys can be
any valid string and must be unique for every request.

Max: 45 characters

See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `str` — The ID of the source which represents the card information to be stored. This can be a card nonce or a payment id.
    
</dd>
</dl>

<dl>
<dd>

**verification_token:** `typing.Optional[str]` 

An identifying token generated by [Payments.verifyBuyer()](https://developer.squareup.com/reference/sdks/web/payments/objects/Payments#Payments.verifyBuyer).
Verification tokens encapsulate customer device information and 3-D Secure
challenge results to indicate that Square has verified the buyer identity.

See the [SCA Overview](https://developer.squareup.com/docs/sca-overview).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cards.<a href="src/fern/cards/client.py">retrieve_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves details for a specific Card.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.cards.retrieve_card(
    card_id="card_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**card_id:** `str` — Unique ID for the desired Card.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cards.<a href="src/fern/cards/client.py">disable_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disables the card, preventing any further updates or charges.
Disabling an already disabled card is allowed but has no effect.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.cards.disable_card(
    card_id="card_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**card_id:** `str` — Unique ID for the desired Card.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CashDrawers
<details><summary><code>client.cash_drawers.<a href="src/fern/cash_drawers/client.py">list_cash_drawer_shifts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides the details for all of the cash drawer shifts for a location
in a date range.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.cash_drawers.list_cash_drawer_shifts(
    location_id="location_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the location to query for a list of cash drawer shifts.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[str]` 

The order in which cash drawer shifts are listed in the response,
based on their opened_at field. Default value: ASC
    
</dd>
</dl>

<dl>
<dd>

**begin_time:** `typing.Optional[str]` — The inclusive start time of the query on opened_at, in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — The exclusive end date of the query on opened_at, in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

Number of cash drawer shift events in a page of results (200 by
default, 1000 max).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor for fetching the next page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cash_drawers.<a href="src/fern/cash_drawers/client.py">retrieve_cash_drawer_shift</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides the summary details for a single cash drawer shift. See
[ListCashDrawerShiftEvents](https://developer.squareup.com/reference/square_2021-08-18/cash-drawers-api/list-cash-drawer-shift-events) for a list of cash drawer shift events.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.cash_drawers.retrieve_cash_drawer_shift(
    shift_id="shift_id",
    location_id="location_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**shift_id:** `str` — The shift ID.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `str` — The ID of the location to retrieve cash drawer shifts from.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cash_drawers.<a href="src/fern/cash_drawers/client.py">list_cash_drawer_shift_events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides a paginated list of events for a single cash drawer shift.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.cash_drawers.list_cash_drawer_shift_events(
    shift_id="shift_id",
    location_id="location_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**shift_id:** `str` — The shift ID.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `str` — The ID of the location to list cash drawer shifts for.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

Number of resources to be returned in a page of results (200 by
default, 1000 max).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor for fetching the next page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Catalog
<details><summary><code>client.catalog.<a href="src/fern/catalog/client.py">batch_delete_catalog_objects</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a set of [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem)s based on the
provided list of target IDs and returns a set of successfully deleted IDs in
the response. Deletion is a cascading event such that all children of the
targeted object are also deleted. For example, deleting a CatalogItem will
also delete all of its [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation)
children.

`BatchDeleteCatalogObjects` succeeds even if only a portion of the targeted
IDs can be deleted. The response will only include IDs that were
actually deleted.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.catalog.batch_delete_catalog_objects()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_ids:** `typing.Optional[typing.Sequence[str]]` 

The IDs of the CatalogObjects to be deleted. When an object is deleted, other objects
in the graph that depend on that object will be deleted as well (for example, deleting a
CatalogItem will delete its CatalogItemVariation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.<a href="src/fern/catalog/client.py">batch_retrieve_catalog_objects</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a set of objects based on the provided ID.
Each [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) returned in the set includes all of its
child information including: all of its
[CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) objects, references to
its [CatalogModifierList](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifierList) objects, and the ids of
any [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects that apply to it.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.catalog.batch_retrieve_catalog_objects(
    object_ids=["object_ids"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_ids:** `typing.Sequence[str]` — The IDs of the CatalogObjects to be retrieved.
    
</dd>
</dl>

<dl>
<dd>

**catalog_version:** `typing.Optional[int]` 

The specific version of the catalog objects to be included in the response. 
This allows you to retrieve historical versions of objects. The specified version value is matched against
the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s' `version` attribute.
    
</dd>
</dl>

<dl>
<dd>

**include_related_objects:** `typing.Optional[bool]` 

If `true`, the response will include additional objects that are related to the
requested objects, as follows:

If the `objects` field of the response contains a CatalogItem, its associated
CatalogCategory objects, CatalogTax objects, CatalogImage objects and
CatalogModifierLists will be returned in the `related_objects` field of the
response. If the `objects` field of the response contains a CatalogItemVariation,
its parent CatalogItem will be returned in the `related_objects` field of
the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.<a href="src/fern/catalog/client.py">batch_upsert_catalog_objects</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates up to 10,000 target objects based on the provided
list of objects. The target objects are grouped into batches and each batch is
inserted/updated in an all-or-nothing manner. If an object within a batch is
malformed in some way, or violates a database constraint, the entire batch
containing that item will be disregarded. However, other batches in the same
request may still succeed. Each batch may contain up to 1,000 objects, and
batches will be processed in order as long as the total object count for the
request (items, variations, modifier lists, discounts, and taxes) is no more
than 10,000.
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
from fern import CatalogObject, CatalogObjectBatch, FernApi

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.catalog.batch_upsert_catalog_objects(
    batches=[
        CatalogObjectBatch(
            objects=[
                CatalogObject(
                    id="id",
                    type="type",
                )
            ],
        )
    ],
    idempotency_key="idempotency_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batches:** `typing.Sequence[CatalogObjectBatch]` 

A batch of CatalogObjects to be inserted/updated atomically.
The objects within a batch will be inserted in an all-or-nothing fashion, i.e., if an error occurs
attempting to insert or update an object within a batch, the entire batch will be rejected. However, an error
in one batch will not affect other batches within the same request.

For each object, its `updated_at` field is ignored and replaced with a current [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates), and its
`is_deleted` field must not be set to `true`.

To modify an existing object, supply its ID. To create a new object, use an ID starting
with `#`. These IDs may be used to create relationships between an object and attributes of
other objects that reference it. For example, you can create a CatalogItem with
ID `#ABC` and a CatalogItemVariation with its `item_id` attribute set to
`#ABC` in order to associate the CatalogItemVariation with its parent
CatalogItem.

Any `#`-prefixed IDs are valid only within a single atomic batch, and will be replaced by server-generated IDs.

Each batch may contain up to 1,000 objects. The total number of objects across all batches for a single request
may not exceed 10,000. If either of these limits is violated, an error will be returned and no objects will
be inserted or updated.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A value you specify that uniquely identifies this
request among all your requests. A common way to create
a valid idempotency key is to use a Universally unique
identifier (UUID).

If you're unsure whether a particular request was successful,
you can reattempt it with the same idempotency key without
worrying about creating duplicate objects.

See [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.<a href="src/fern/catalog/client.py">catalog_info</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves information about the Square Catalog API, such as batch size
limits that can be used by the `BatchUpsertCatalogObjects` endpoint.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.catalog.catalog_info()

```
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

<details><summary><code>client.catalog.<a href="src/fern/catalog/client.py">list_catalog</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s that includes
all objects of a set of desired types (for example, all [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem)
and [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects) in the catalog. The `types` parameter
is specified as a comma-separated list of valid [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) types:
`ITEM`, `ITEM_VARIATION`, `MODIFIER`, `MODIFIER_LIST`, `CATEGORY`, `DISCOUNT`, `TAX`, `IMAGE`.

__Important:__ ListCatalog does not return deleted catalog items. To retrieve
deleted catalog items, use [SearchCatalogObjects](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-objects)
and set the `include_deleted_objects` attribute value to `true`.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.catalog.list_catalog()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The pagination cursor returned in the previous response. Leave unset for an initial request.
The page size is currently set to be 100.
See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[str]` 

An optional case-insensitive, comma-separated list of object types to retrieve.

The valid values are defined in the [CatalogObjectType](https://developer.squareup.com/reference/square_2021-08-18/enums/CatalogObjectType) enum, including
`ITEM`, `ITEM_VARIATION`, `CATEGORY`, `DISCOUNT`, `TAX`,
`MODIFIER`, `MODIFIER_LIST`, or `IMAGE`.

If this is unspecified, the operation returns objects of all the types at the version of the Square API used to make the request.
    
</dd>
</dl>

<dl>
<dd>

**catalog_version:** `typing.Optional[int]` 

The specific version of the catalog objects to be included in the response. 
This allows you to retrieve historical
versions of objects. The specified version value is matched against
the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s' `version` attribute.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.<a href="src/fern/catalog/client.py">upsert_catalog_object</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates the target [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject).
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
from fern import CatalogObject, FernApi

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.catalog.upsert_catalog_object(
    idempotency_key="idempotency_key",
    object=CatalogObject(
        id="id",
        type="type",
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

**idempotency_key:** `str` 

A value you specify that uniquely identifies this
request among all your requests. A common way to create
a valid idempotency key is to use a Universally unique
identifier (UUID).

If you're unsure whether a particular request was successful,
you can reattempt it with the same idempotency key without
worrying about creating duplicate objects.

See [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.
    
</dd>
</dl>

<dl>
<dd>

**object:** `CatalogObject` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.<a href="src/fern/catalog/client.py">retrieve_catalog_object</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) as a
[CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) based on the provided ID. The returned
object includes all of the relevant [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem)
information including: [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation)
children, references to its
[CatalogModifierList](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifierList) objects, and the ids of
any [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects that apply to it.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.catalog.retrieve_catalog_object(
    object_id="object_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_id:** `str` — The object ID of any type of catalog objects to be retrieved.
    
</dd>
</dl>

<dl>
<dd>

**include_related_objects:** `typing.Optional[bool]` 

If `true`, the response will include additional objects that are related to the
requested object, as follows:

If the `object` field of the response contains a `CatalogItem`, its associated
`CatalogCategory`, `CatalogTax`, `CatalogImage` and `CatalogModifierList` objects will
be returned in the `related_objects` field of the response. If the `object` field of
the response contains a `CatalogItemVariation`, its parent `CatalogItem` will be returned
in the `related_objects` field of the response.

Default value: `false`
    
</dd>
</dl>

<dl>
<dd>

**catalog_version:** `typing.Optional[int]` 

Requests objects as of a specific version of the catalog. This allows you to retrieve historical
versions of objects. The value to retrieve a specific version of an object can be found
in the version field of [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.<a href="src/fern/catalog/client.py">delete_catalog_object</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a single [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) based on the
provided ID and returns the set of successfully deleted IDs in the response.
Deletion is a cascading event such that all children of the targeted object
are also deleted. For example, deleting a [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem)
will also delete all of its
[CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) children.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.catalog.delete_catalog_object(
    object_id="object_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_id:** `str` 

The ID of the catalog object to be deleted. When an object is deleted, other
objects in the graph that depend on that object will be deleted as well (for example, deleting a
catalog item will delete its catalog item variations).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.<a href="src/fern/catalog/client.py">search_catalog_objects</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) of any type by matching supported search attribute values,
excluding custom attribute values on items or item variations, against one or more of the specified query expressions.

This (`SearchCatalogObjects`) endpoint differs from the [SearchCatalogItems](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-items)
endpoint in the following aspects:

- `SearchCatalogItems` can only search for items or item variations, whereas `SearchCatalogObjects` can search for any type of catalog objects.
- `SearchCatalogItems` supports the custom attribute query filters to return items or item variations that contain custom attribute values, where `SearchCatalogObjects` does not.
- `SearchCatalogItems` does not support the `include_deleted_objects` filter to search for deleted items or item variations, whereas `SearchCatalogObjects` does.
- The both endpoints have different call conventions, including the query filter formats.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.catalog.search_catalog_objects()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**begin_time:** `typing.Optional[str]` 

Return objects modified after this [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates), in RFC 3339
format, e.g., `2016-09-04T23:59:33.123Z`. The timestamp is exclusive - objects with a
timestamp equal to `begin_time` will not be included in the response.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The pagination cursor returned in the previous response. Leave unset for an initial request.
See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.
    
</dd>
</dl>

<dl>
<dd>

**include_deleted_objects:** `typing.Optional[bool]` 

If `true`, deleted objects will be included in the results. Deleted objects will have their
`is_deleted` field set to `true`.
    
</dd>
</dl>

<dl>
<dd>

**include_related_objects:** `typing.Optional[bool]` 

If `true`, the response will include additional objects that are related to the
requested object, as follows:

If a CatalogItem is returned in the object field of the response,
its associated CatalogCategory, CatalogTax objects,
CatalogImage objects and CatalogModifierList objects
will be included in the `related_objects` field of the response.

If a CatalogItemVariation is returned in the object field of the
response, its parent CatalogItem will be included in the `related_objects` field of
the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

A limit on the number of results to be returned in a single page. The limit is advisory -
the implementation may return more or fewer results. If the supplied limit is negative, zero, or
is higher than the maximum limit of 1,000, it will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**object_types:** `typing.Optional[typing.Sequence[str]]` — The desired set of object types to appear in the search results.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[CatalogQuery]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.<a href="src/fern/catalog/client.py">search_catalog_items</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for catalog items or item variations by matching supported search attribute values, including
custom attribute values, against one or more of the specified query expressions.

This (`SearchCatalogItems`) endpoint differs from the [SearchCatalogObjects](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-objects)
endpoint in the following aspects:

- `SearchCatalogItems` can only search for items or item variations, whereas `SearchCatalogObjects` can search for any type of catalog objects.
- `SearchCatalogItems` supports the custom attribute query filters to return items or item variations that contain custom attribute values, where `SearchCatalogObjects` does not.
- `SearchCatalogItems` does not support the `include_deleted_objects` filter to search for deleted items or item variations, whereas `SearchCatalogObjects` does.
- The both endpoints use different call conventions, including the query filter formats.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.catalog.search_catalog_items()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category_ids:** `typing.Optional[typing.Sequence[str]]` — The category id query expression to return items containing the specified category IDs.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination token, returned in the previous response, used to fetch the next batch of pending results.
    
</dd>
</dl>

<dl>
<dd>

**custom_attribute_filters:** `typing.Optional[typing.Sequence[CustomAttributeFilter]]` 

The customer-attribute filter to return items or item variations matching the specified
custom attribute expressions. A maximum number of 10 custom attribute expressions are supported in
a single call to the [SearchCatalogItems](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-items) endpoint.
    
</dd>
</dl>

<dl>
<dd>

**enabled_location_ids:** `typing.Optional[typing.Sequence[str]]` — The enabled-location query expression to return items and item variations having specified enabled locations.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return per page. The default value is 100.
    
</dd>
</dl>

<dl>
<dd>

**product_types:** `typing.Optional[typing.Sequence[str]]` — The product types query expression to return items or item variations having the specified product types.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[str]` — The order to sort the results by item names. The default sort order is ascending (`ASC`).
    
</dd>
</dl>

<dl>
<dd>

**stock_levels:** `typing.Optional[typing.Sequence[str]]` — The stock-level query expression to return item variations with the specified stock levels.
    
</dd>
</dl>

<dl>
<dd>

**text_filter:** `typing.Optional[str]` 

The text filter expression to return items or item variations containing specified text in
the `name`, `description`, or `abbreviation` attribute value of an item, or in
the `name`, `sku`, or `upc` attribute value of an item variation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.<a href="src/fern/catalog/client.py">update_item_modifier_lists</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the [CatalogModifierList](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifierList) objects
that apply to the targeted [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) without having
to perform an upsert on the entire item.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.catalog.update_item_modifier_lists(
    item_ids=["item_ids"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_ids:** `typing.Sequence[str]` — The IDs of the catalog items associated with the CatalogModifierList objects being updated.
    
</dd>
</dl>

<dl>
<dd>

**modifier_lists_to_disable:** `typing.Optional[typing.Sequence[str]]` — The IDs of the CatalogModifierList objects to disable for the CatalogItem.
    
</dd>
</dl>

<dl>
<dd>

**modifier_lists_to_enable:** `typing.Optional[typing.Sequence[str]]` — The IDs of the CatalogModifierList objects to enable for the CatalogItem.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.<a href="src/fern/catalog/client.py">update_item_taxes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects that apply to the
targeted [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) without having to perform an
upsert on the entire item.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.catalog.update_item_taxes(
    item_ids=["item_ids"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_ids:** `typing.Sequence[str]` — IDs for the CatalogItems associated with the CatalogTax objects being updated.
    
</dd>
</dl>

<dl>
<dd>

**taxes_to_disable:** `typing.Optional[typing.Sequence[str]]` — IDs of the CatalogTax objects to disable.
    
</dd>
</dl>

<dl>
<dd>

**taxes_to_enable:** `typing.Optional[typing.Sequence[str]]` — IDs of the CatalogTax objects to enable.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Customers
<details><summary><code>client.customers.<a href="src/fern/customers/client.py">list_customers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists customer profiles associated with a Square account.

Under normal operating conditions, newly created or updated customer profiles become available
for the listing operation in well under 30 seconds. Occasionally, propagation of the new or updated
profiles can take closer to one minute or longer, especially during network incidents and outages.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.customers.list_customers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for your original query.

For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results. 
The limit is ignored if it is less than 1 or greater than 100. The default value is 100.

For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[str]` 

Indicates how customers should be sorted.

The default value is `DEFAULT`.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[str]` 

Indicates whether customers should be sorted in ascending (`ASC`) or
descending (`DESC`) order.

The default value is `ASC`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">create_customer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new customer for a business.

You must provide at least one of the following values in your request to this
endpoint:

- `given_name`
- `family_name`
- `company_name`
- `email_address`
- `phone_number`
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.customers.create_customer()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**address:** `typing.Optional[Address]` 
    
</dd>
</dl>

<dl>
<dd>

**birthday:** `typing.Optional[str]` 

The birthday associated with the customer profile, in RFC 3339 format. The year is optional. The timezone and time are not allowed.
For example, `0000-09-21T00:00:00-00:00` represents a birthday on September 21 and `1998-09-21T00:00:00-00:00` represents a birthday on September 21, 1998.
You can also specify this value in `YYYY-MM-DD` format.
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[str]` — A business name associated with the customer profile.
    
</dd>
</dl>

<dl>
<dd>

**email_address:** `typing.Optional[str]` — The email address associated with the customer profile.
    
</dd>
</dl>

<dl>
<dd>

**family_name:** `typing.Optional[str]` — The family name (that is, the last name) associated with the customer profile.
    
</dd>
</dl>

<dl>
<dd>

**given_name:** `typing.Optional[str]` — The given name (that is, the first name) associated with the customer profile.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

The idempotency key for the request.	For more information, see
[Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**nickname:** `typing.Optional[str]` — A nickname for the customer profile.
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` — A custom note associated with the customer profile.
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — The 11-digit phone number associated with the customer profile.
    
</dd>
</dl>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` 

An optional second ID used to associate the customer profile with an
entity in another system.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">search_customers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches the customer profiles associated with a Square account using a supported query filter.

Calling `SearchCustomers` without any explicit query filter returns all
customer profiles ordered alphabetically based on `given_name` and
`family_name`.

Under normal operating conditions, newly created or updated customer profiles become available
for the search operation in well under 30 seconds. Occasionally, propagation of the new or updated
profiles can take closer to one minute or longer, especially during network incidents and outages.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.customers.search_customers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

Include the pagination cursor in subsequent calls to this endpoint to retrieve
the next set of results associated with the original query.

For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results. 
The limit is ignored if it is less than the minimum or greater than the maximum value. The default value is 100.

For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[CustomerQuery]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">retrieve_customer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details for a single customer.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.customers.retrieve_customer(
    customer_id="customer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — The ID of the customer to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">update_customer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a customer profile. To change an attribute, specify the new value. To remove an attribute, specify the value as an empty string or empty object.

As a best practice, you should include the `version` field in the request to enable [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency) control. The value must be set to the current version of the customer profile.

To update a customer profile that was created by merging existing profiles, you must use the ID of the newly created profile.

You cannot use this endpoint to change cards on file. To make changes, use the [Cards API](https://developer.squareup.com/reference/square_2021-08-18/cards-api) or [Gift Cards API](https://developer.squareup.com/reference/square_2021-08-18/gift-cards-api).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.customers.update_customer(
    customer_id="customer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — The ID of the customer to update.
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[Address]` 
    
</dd>
</dl>

<dl>
<dd>

**birthday:** `typing.Optional[str]` 

The birthday associated with the customer profile, in RFC 3339 format. The year is optional. The timezone and time are not allowed.
For example, `0000-09-21T00:00:00-00:00` represents a birthday on September 21 and `1998-09-21T00:00:00-00:00` represents a birthday on September 21, 1998.
You can also specify this value in `YYYY-MM-DD` format.
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[str]` — A business name associated with the customer profile.
    
</dd>
</dl>

<dl>
<dd>

**email_address:** `typing.Optional[str]` — The email address associated with the customer profile.
    
</dd>
</dl>

<dl>
<dd>

**family_name:** `typing.Optional[str]` — The family name (that is, the last name) associated with the customer profile.
    
</dd>
</dl>

<dl>
<dd>

**given_name:** `typing.Optional[str]` — The given name (that is, the first name) associated with the customer profile.
    
</dd>
</dl>

<dl>
<dd>

**nickname:** `typing.Optional[str]` — A nickname for the customer profile.
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` — A custom note associated with the customer profile.
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` — The 11-digit phone number associated with the customer profile.
    
</dd>
</dl>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` 

An optional second ID used to associate the customer profile with an
entity in another system.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 

The current version of the customer profile.

As a best practice, you should include this field to enable [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency) control. For more information, see [Update a customer profile](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#update-a-customer-profile).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">delete_customer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a customer profile from a business. This operation also unlinks any associated cards on file. 

As a best practice, you should include the `version` field in the request to enable [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency) control. The value must be set to the current version of the customer profile. 

To delete a customer profile that was created by merging existing profiles, you must use the ID of the newly created profile.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.customers.delete_customer(
    customer_id="customer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — The ID of the customer to delete.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 

The current version of the customer profile.

As a best practice, you should include this parameter to enable [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency) control.  For more information, see [Delete a customer profile](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#delete-customer-profile).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">create_customer_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a card on file to an existing customer.

As with charges, calls to `CreateCustomerCard` are idempotent. Multiple
calls with the same card nonce return the same card record that was created
with the provided nonce during the _first_ call.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.customers.create_customer_card(
    customer_id="customer_id",
    card_nonce="card_nonce",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — The Square ID of the customer profile the card is linked to.
    
</dd>
</dl>

<dl>
<dd>

**card_nonce:** `str` 

A card nonce representing the credit card to link to the customer.

Card nonces are generated by the Square payment form when customers enter
their card information. For more information, see
[Walkthrough: Integrate Square Payments in a Website](https://developer.squareup.com/docs/web-payments/take-card-payment).

__NOTE:__ Card nonces generated by digital wallets (such as Apple Pay)
cannot be used to create a customer card.
    
</dd>
</dl>

<dl>
<dd>

**billing_address:** `typing.Optional[Address]` 
    
</dd>
</dl>

<dl>
<dd>

**cardholder_name:** `typing.Optional[str]` — The full name printed on the credit card.
    
</dd>
</dl>

<dl>
<dd>

**verification_token:** `typing.Optional[str]` 

An identifying token generated by [Payments.verifyBuyer()](https://developer.squareup.com/reference/sdks/web/payments/objects/Payments#Payments.verifyBuyer).
Verification tokens encapsulate customer device information and 3-D Secure
challenge results to indicate that Square has verified the buyer identity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">delete_customer_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a card on file from a customer.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.customers.delete_customer_card(
    customer_id="customer_id",
    card_id="card_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — The ID of the customer that the card on file belongs to.
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `str` — The ID of the card on file to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">add_group_to_customer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a group membership to a customer.

The customer is identified by the `customer_id` value
and the customer group is identified by the `group_id` value.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.customers.add_group_to_customer(
    customer_id="customer_id",
    group_id="group_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — The ID of the customer to add to a group.
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `str` — The ID of the customer group to add the customer to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">remove_group_from_customer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a group membership from a customer.

The customer is identified by the `customer_id` value
and the customer group is identified by the `group_id` value.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.customers.remove_group_from_customer(
    customer_id="customer_id",
    group_id="group_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — The ID of the customer to remove from the group.
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `str` — The ID of the customer group to remove the customer from.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CustomerGroups
<details><summary><code>client.customer_groups.<a href="src/fern/customer_groups/client.py">list_customer_groups</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the list of customer groups of a business.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.customer_groups.list_customer_groups()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for your original query.

For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results. 
The limit is ignored if it is less than 1 or greater than 50. The default value is 50.

For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customer_groups.<a href="src/fern/customer_groups/client.py">create_customer_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new customer group for a business.

The request must include the `name` value of the group.
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
from fern import CustomerGroup, FernApi

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.customer_groups.create_customer_group(
    group=CustomerGroup(
        name="name",
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

**group:** `CustomerGroup` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — The idempotency key for the request. For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customer_groups.<a href="src/fern/customer_groups/client.py">retrieve_customer_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specific customer group as identified by the `group_id` value.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.customer_groups.retrieve_customer_group(
    group_id="group_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` — The ID of the customer group to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customer_groups.<a href="src/fern/customer_groups/client.py">update_customer_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a customer group as identified by the `group_id` value.
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
from fern import CustomerGroup, FernApi

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.customer_groups.update_customer_group(
    group_id="group_id",
    group=CustomerGroup(
        name="name",
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

**group_id:** `str` — The ID of the customer group to update.
    
</dd>
</dl>

<dl>
<dd>

**group:** `CustomerGroup` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customer_groups.<a href="src/fern/customer_groups/client.py">delete_customer_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a customer group as identified by the `group_id` value.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.customer_groups.delete_customer_group(
    group_id="group_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` — The ID of the customer group to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CustomerSegments
<details><summary><code>client.customer_segments.<a href="src/fern/customer_segments/client.py">list_customer_segments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the list of customer segments of a business.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.customer_segments.list_customer_segments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by previous calls to `ListCustomerSegments`.
This cursor is used to retrieve the next set of query results.

For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results. 
The limit is ignored if it is less than 1 or greater than 50. The default value is 50.

For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customer_segments.<a href="src/fern/customer_segments/client.py">retrieve_customer_segment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specific customer segment as identified by the `segment_id` value.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.customer_segments.retrieve_customer_segment(
    segment_id="segment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**segment_id:** `str` — The Square-issued ID of the customer segment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Devices
<details><summary><code>client.devices.<a href="src/fern/devices/client.py">list_device_codes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all DeviceCodes associated with the merchant.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.devices.list_device_codes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for your original query.

See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

If specified, only returns DeviceCodes of the specified location.
Returns DeviceCodes of all locations if empty.
    
</dd>
</dl>

<dl>
<dd>

**product_type:** `typing.Optional[str]` 

If specified, only returns DeviceCodes targeting the specified product type.
Returns DeviceCodes of all product types if empty.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 

If specified, returns DeviceCodes with the specified statuses.
Returns DeviceCodes of status `PAIRED` and `UNPAIRED` if empty.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.devices.<a href="src/fern/devices/client.py">create_device_code</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a DeviceCode that can be used to login to a Square Terminal device to enter the connected
terminal mode.
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
from fern import DeviceCode, FernApi

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.devices.create_device_code(
    device_code=DeviceCode(
        product_type="product_type",
    ),
    idempotency_key="idempotency_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device_code:** `DeviceCode` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this CreateDeviceCode request. Keys can
be any valid string but must be unique for every CreateDeviceCode request.

See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.devices.<a href="src/fern/devices/client.py">get_device_code</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves DeviceCode with the associated ID.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.devices.get_device_code(
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

**id:** `str` — The unique identifier for the device code.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Disputes
<details><summary><code>client.disputes.<a href="src/fern/disputes/client.py">list_disputes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of disputes associated with a particular account.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.disputes.list_disputes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.
For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[str]` 

The dispute states to filter the result.
If not specified, the endpoint returns all open disputes (the dispute status is not `INQUIRY_CLOSED`, `WON`,
or `LOST`).
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

The ID of the location for which to return a list of disputes. If not specified, the endpoint returns
all open disputes (the dispute status is not `INQUIRY_CLOSED`, `WON`, or `LOST`) associated with all locations.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.disputes.<a href="src/fern/disputes/client.py">retrieve_dispute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details about a specific dispute.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.disputes.retrieve_dispute(
    dispute_id="dispute_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dispute_id:** `str` — The ID of the dispute you want more details about.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.disputes.<a href="src/fern/disputes/client.py">accept_dispute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Accepts the loss on a dispute. Square returns the disputed amount to the cardholder and
updates the dispute state to ACCEPTED.

Square debits the disputed amount from the seller’s Square account. If the Square account
does not have sufficient funds, Square debits the associated bank account.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.disputes.accept_dispute(
    dispute_id="dispute_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dispute_id:** `str` — The ID of the dispute you want to accept.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.disputes.<a href="src/fern/disputes/client.py">list_dispute_evidence</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of evidence associated with a dispute.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.disputes.list_dispute_evidence(
    dispute_id="dispute_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dispute_id:** `str` — The ID of the dispute.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.
For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.disputes.<a href="src/fern/disputes/client.py">create_dispute_evidence_text</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads text to use as evidence for a dispute challenge.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.disputes.create_dispute_evidence_text(
    dispute_id="dispute_id",
    evidence_text="evidence_text",
    idempotency_key="idempotency_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dispute_id:** `str` — The ID of the dispute you want to upload evidence for.
    
</dd>
</dl>

<dl>
<dd>

**evidence_text:** `str` — The evidence string.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` — The Unique ID. For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**evidence_type:** `typing.Optional[str]` — The type of evidence you are uploading.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.disputes.<a href="src/fern/disputes/client.py">retrieve_dispute_evidence</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the evidence metadata specified by the evidence ID in the request URL path

You must maintain a copy of the evidence you upload if you want to reference it later. You cannot
download the evidence after you upload it.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.disputes.retrieve_dispute_evidence(
    dispute_id="dispute_id",
    evidence_id="evidence_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dispute_id:** `str` — The ID of the dispute that you want to retrieve evidence from.
    
</dd>
</dl>

<dl>
<dd>

**evidence_id:** `str` — The ID of the evidence to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.disputes.<a href="src/fern/disputes/client.py">delete_dispute_evidence</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes specified evidence from a dispute.

Square does not send the bank any evidence that is removed. Also, you cannot remove evidence after
submitting it to the bank using [SubmitEvidence](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/submit-evidence).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.disputes.delete_dispute_evidence(
    dispute_id="dispute_id",
    evidence_id="evidence_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dispute_id:** `str` — The ID of the dispute you want to remove evidence from.
    
</dd>
</dl>

<dl>
<dd>

**evidence_id:** `str` — The ID of the evidence you want to remove.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.disputes.<a href="src/fern/disputes/client.py">submit_evidence</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits evidence to the cardholder's bank.

Before submitting evidence, Square compiles all available evidence. This includes evidence uploaded
using the [CreateDisputeEvidenceFile](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-file) and
[CreateDisputeEvidenceText](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-text) endpoints and
evidence automatically provided by Square, when available.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.disputes.submit_evidence(
    dispute_id="dispute_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dispute_id:** `str` — The ID of the dispute that you want to submit evidence for.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.employees.<a href="src/fern/employees/client.py">list_employees</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.employees.list_employees()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Specifies the EmployeeStatus to filter the employee by.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of employees to be returned on each page.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The token required to retrieve the specified page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.employees.<a href="src/fern/employees/client.py">retrieve_employee</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.employees.retrieve_employee(
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

**id:** `str` — UUID for the employee that was requested.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## GiftCards
<details><summary><code>client.gift_cards.<a href="src/fern/gift_cards/client.py">list_gift_cards</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all gift cards. You can specify optional filters to retrieve 
a subset of the gift cards.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.gift_cards.list_gift_cards()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `typing.Optional[str]` 

If a type is provided, gift cards of this type are returned 
(see [GiftCardType](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardType)).
If no type is provided, it returns gift cards of all types.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` 

If the state is provided, it returns the gift cards in the specified state 
(see [GiftCardStatus](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardStatus)).
Otherwise, it returns the gift cards of all states.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

If a value is provided, it returns only that number of results per page.
The maximum number of results allowed per page is 50. The default value is 30.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.
If a cursor is not provided, it returns the first page of the results. 
For more information, see [Pagination](https://developer.squareup.com/docs/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — If a value is provided, returns only the gift cards linked to the specified customer
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gift_cards.<a href="src/fern/gift_cards/client.py">create_gift_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a digital gift card or registers a physical (plastic) gift card. You must activate the gift card before 
it can be used for payment. For more information, see 
[Selling gift cards](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api#selling-square-gift-cards).
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
from fern import FernApi, GiftCard

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.gift_cards.create_gift_card(
    gift_card=GiftCard(
        type={"key": "value"},
    ),
    idempotency_key="x",
    location_id="x",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**gift_card:** `GiftCard` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` — A unique string that identifies the `CreateGiftCard` request.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `str` — The location ID where the gift card that will be created should be registered.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gift_cards.<a href="src/fern/gift_cards/client.py">retrieve_gift_card_from_gan</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a gift card using the gift card account number (GAN).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.gift_cards.retrieve_gift_card_from_gan(
    gan="gan",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**gan:** `str` 

The gift card account number (GAN) of the gift card to retrieve.
The maximum length of a GAN is 255 digits to account for third-party GANs that have been imported.
Square-issued gift cards have 16-digit GANs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gift_cards.<a href="src/fern/gift_cards/client.py">retrieve_gift_card_from_nonce</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a gift card using a nonce (a secure token) that represents the gift card.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.gift_cards.retrieve_gift_card_from_nonce(
    nonce="nonce",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**nonce:** `str` — The nonce of the gift card to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gift_cards.<a href="src/fern/gift_cards/client.py">link_customer_to_gift_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Links a customer to a gift card
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.gift_cards.link_customer_to_gift_card(
    gift_card_id="gift_card_id",
    customer_id="customer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**gift_card_id:** `str` — The ID of the gift card to link.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `str` — The ID of the customer to be linked.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gift_cards.<a href="src/fern/gift_cards/client.py">unlink_customer_from_gift_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unlinks a customer from a gift card
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.gift_cards.unlink_customer_from_gift_card(
    gift_card_id="gift_card_id",
    customer_id="customer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**gift_card_id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gift_cards.<a href="src/fern/gift_cards/client.py">retrieve_gift_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a gift card using its ID.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.gift_cards.retrieve_gift_card(
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

**id:** `str` — The ID of the gift card to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## GiftCardActivities
<details><summary><code>client.gift_card_activities.<a href="src/fern/gift_card_activities/client.py">list_gift_card_activities</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists gift card activities. By default, you get gift card activities for all
gift cards in the seller's account. You can optionally specify query parameters to
filter the list. For example, you can get a list of gift card activities for a gift card,
for all gift cards in a specific region, or for activities within a time window.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.gift_card_activities.list_gift_card_activities()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**gift_card_id:** `typing.Optional[str]` 

If you provide a gift card ID, the endpoint returns activities that belong 
to the specified gift card. Otherwise, the endpoint returns all gift card activities for 
the seller.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 

If you provide a type, the endpoint returns gift card activities of this type. 
Otherwise, the endpoint returns all types of gift card activities.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

If you provide a location ID, the endpoint returns gift card activities for that location. 
Otherwise, the endpoint returns gift card activities for all locations.
    
</dd>
</dl>

<dl>
<dd>

**begin_time:** `typing.Optional[str]` 

The timestamp for the beginning of the reporting period, in RFC 3339 format.
Inclusive. Default: The current time minus one year.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` 

The timestamp for the end of the reporting period, in RFC 3339 format.
Inclusive. Default: The current time.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

If you provide a limit value, the endpoint returns the specified number 
of results (or less) per page. A maximum value is 100. The default value is 50.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.
If you do not provide the cursor, the call returns the first page of the results.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[str]` 

The order in which the endpoint returns the activities, based on `created_at`.
- `ASC` - Oldest to newest.
- `DESC` - Newest to oldest (default).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gift_card_activities.<a href="src/fern/gift_card_activities/client.py">create_gift_card_activity</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a gift card activity. For more information, see 
[GiftCardActivity](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api#giftcardactivity) and 
[Using activated gift cards](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api#using-activated-gift-cards).
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
from fern import FernApi, GiftCardActivity

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.gift_card_activities.create_gift_card_activity(
    gift_card_activity=GiftCardActivity(
        location_id="location_id",
        type={"key": "value"},
    ),
    idempotency_key="x",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**gift_card_activity:** `GiftCardActivity` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` — A unique string that identifies the `CreateGiftCardActivity` request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Inventory
<details><summary><code>client.inventory.<a href="src/fern/inventory/client.py">deprecated_retrieve_inventory_adjustment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated version of [RetrieveInventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/retrieve-inventory-adjustment) after the endpoint URL 
is updated to conform to the standard convention.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.inventory.deprecated_retrieve_inventory_adjustment(
    adjustment_id="adjustment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**adjustment_id:** `str` — ID of the [InventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryAdjustment) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/fern/inventory/client.py">retrieve_inventory_adjustment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the [InventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryAdjustment) object
with the provided `adjustment_id`.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.inventory.retrieve_inventory_adjustment(
    adjustment_id="adjustment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**adjustment_id:** `str` — ID of the [InventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryAdjustment) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/fern/inventory/client.py">deprecated_batch_change_inventory</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated version of [BatchChangeInventory](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-change-inventory) after the endpoint URL 
is updated to conform to the standard convention.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.inventory.deprecated_batch_change_inventory(
    idempotency_key="idempotency_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

A client-supplied, universally unique identifier (UUID) for the
request.

See [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency) in the
[API Development 101](https://developer.squareup.com/docs/basics/api101/overview) section for more
information.
    
</dd>
</dl>

<dl>
<dd>

**changes:** `typing.Optional[typing.Sequence[InventoryChange]]` 

The set of physical counts and inventory adjustments to be made.
Changes are applied based on the client-supplied timestamp and may be sent
out of order.
    
</dd>
</dl>

<dl>
<dd>

**ignore_unchanged_counts:** `typing.Optional[bool]` 

Indicates whether the current physical count should be ignored if
the quantity is unchanged since the last physical count. Default: `true`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/fern/inventory/client.py">deprecated_batch_retrieve_inventory_changes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated version of [BatchRetrieveInventoryChanges](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-retrieve-inventory-changes) after the endpoint URL 
is updated to conform to the standard convention.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.inventory.deprecated_batch_retrieve_inventory_changes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**catalog_object_ids:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `CatalogObject` ID.
The filter is only applicable when set. The default value is null.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for the original query.

See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    
</dd>
</dl>

<dl>
<dd>

**location_ids:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `Location` ID. 
The filter is only applicable when set. The default value is null.
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.Sequence[str]]` 

The filter to return `ADJUSTMENT` query results by
`InventoryState`. This filter is only applied when set.
The default value is null.
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `InventoryChangeType` values other than `TRANSFER`.
The default value is `[PHYSICAL_COUNT, ADJUSTMENT]`.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[str]` 

The filter to return results with their `calculated_at` value  
after the given time as specified in an RFC 3339 timestamp. 
The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[str]` 

The filter to return results with their `created_at` or `calculated_at` value  
strictly before the given time as specified in an RFC 3339 timestamp. 
The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/fern/inventory/client.py">deprecated_batch_retrieve_inventory_counts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated version of [BatchRetrieveInventoryCounts](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-retrieve-inventory-counts) after the endpoint URL 
is updated to conform to the standard convention.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.inventory.deprecated_batch_retrieve_inventory_counts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**catalog_object_ids:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `CatalogObject` ID.
The filter is applicable only when set.  The default is null.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for the original query.

See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    
</dd>
</dl>

<dl>
<dd>

**location_ids:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `Location` ID. 
This filter is applicable only when set. The default is null.
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `InventoryState`. The filter is only applicable when set.
Ignored are untracked states of `NONE`, `SOLD`, and `UNLINKED_RETURN`.
The default is null.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[str]` 

The filter to return results with their `calculated_at` value 
after the given time as specified in an RFC 3339 timestamp. 
The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/fern/inventory/client.py">batch_change_inventory</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Applies adjustments and counts to the provided item quantities.

On success: returns the current calculated counts for all objects
referenced in the request.
On failure: returns a list of related errors.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.inventory.batch_change_inventory(
    idempotency_key="idempotency_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

A client-supplied, universally unique identifier (UUID) for the
request.

See [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency) in the
[API Development 101](https://developer.squareup.com/docs/basics/api101/overview) section for more
information.
    
</dd>
</dl>

<dl>
<dd>

**changes:** `typing.Optional[typing.Sequence[InventoryChange]]` 

The set of physical counts and inventory adjustments to be made.
Changes are applied based on the client-supplied timestamp and may be sent
out of order.
    
</dd>
</dl>

<dl>
<dd>

**ignore_unchanged_counts:** `typing.Optional[bool]` 

Indicates whether the current physical count should be ignored if
the quantity is unchanged since the last physical count. Default: `true`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/fern/inventory/client.py">batch_retrieve_inventory_changes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns historical physical counts and adjustments based on the
provided filter criteria.

Results are paginated and sorted in ascending order according their
`occurred_at` timestamp (oldest first).

BatchRetrieveInventoryChanges is a catch-all query endpoint for queries
that cannot be handled by other, simpler endpoints.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.inventory.batch_retrieve_inventory_changes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**catalog_object_ids:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `CatalogObject` ID.
The filter is only applicable when set. The default value is null.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for the original query.

See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    
</dd>
</dl>

<dl>
<dd>

**location_ids:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `Location` ID. 
The filter is only applicable when set. The default value is null.
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.Sequence[str]]` 

The filter to return `ADJUSTMENT` query results by
`InventoryState`. This filter is only applied when set.
The default value is null.
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `InventoryChangeType` values other than `TRANSFER`.
The default value is `[PHYSICAL_COUNT, ADJUSTMENT]`.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[str]` 

The filter to return results with their `calculated_at` value  
after the given time as specified in an RFC 3339 timestamp. 
The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[str]` 

The filter to return results with their `created_at` or `calculated_at` value  
strictly before the given time as specified in an RFC 3339 timestamp. 
The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/fern/inventory/client.py">batch_retrieve_inventory_counts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns current counts for the provided
[CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s at the requested
[Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location)s.

Results are paginated and sorted in descending order according to their
`calculated_at` timestamp (newest first).

When `updated_after` is specified, only counts that have changed since that
time (based on the server timestamp for the most recent change) are
returned. This allows clients to perform a "sync" operation, for example
in response to receiving a Webhook notification.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.inventory.batch_retrieve_inventory_counts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**catalog_object_ids:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `CatalogObject` ID.
The filter is applicable only when set.  The default is null.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for the original query.

See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    
</dd>
</dl>

<dl>
<dd>

**location_ids:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `Location` ID. 
This filter is applicable only when set. The default is null.
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `InventoryState`. The filter is only applicable when set.
Ignored are untracked states of `NONE`, `SOLD`, and `UNLINKED_RETURN`.
The default is null.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[str]` 

The filter to return results with their `calculated_at` value 
after the given time as specified in an RFC 3339 timestamp. 
The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/fern/inventory/client.py">deprecated_retrieve_inventory_physical_count</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated version of [RetrieveInventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/retrieve-inventory-physical-count) after the endpoint URL 
is updated to conform to the standard convention.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.inventory.deprecated_retrieve_inventory_physical_count(
    physical_count_id="physical_count_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**physical_count_id:** `str` 

ID of the
[InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/fern/inventory/client.py">retrieve_inventory_physical_count</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount)
object with the provided `physical_count_id`.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.inventory.retrieve_inventory_physical_count(
    physical_count_id="physical_count_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**physical_count_id:** `str` 

ID of the
[InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/fern/inventory/client.py">retrieve_inventory_transfer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the [InventoryTransfer](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryTransfer) object
with the provided `transfer_id`.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.inventory.retrieve_inventory_transfer(
    transfer_id="transfer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transfer_id:** `str` — ID of the [InventoryTransfer](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryTransfer) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/fern/inventory/client.py">retrieve_inventory_count</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the current calculated stock count for a given
[CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) at a given set of
[Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location)s. Responses are paginated and unsorted.
For more sophisticated queries, use a batch endpoint.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.inventory.retrieve_inventory_count(
    catalog_object_id="catalog_object_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**catalog_object_id:** `str` — ID of the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**location_ids:** `typing.Optional[str]` 

The [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) IDs to look up as a comma-separated
list. An empty list queries all locations.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for the original query.

See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/fern/inventory/client.py">retrieve_inventory_changes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a set of physical counts and inventory adjustments for the
provided [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) at the requested
[Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location)s. 

You can achieve the same result by calling [BatchRetrieveInventoryChanges](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-retrieve-inventory-changes) 
and having the `catalog_object_ids` list contain a single element of the `CatalogObject` ID.

Results are paginated and sorted in descending order according to their
`occurred_at` timestamp (newest first).

There are no limits on how far back the caller can page. This endpoint can be 
used to display recent changes for a specific item. For more
sophisticated queries, use a batch endpoint.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.inventory.retrieve_inventory_changes(
    catalog_object_id="catalog_object_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**catalog_object_id:** `str` — ID of the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**location_ids:** `typing.Optional[str]` 

The [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) IDs to look up as a comma-separated
list. An empty list queries all locations.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for the original query.

See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Invoices
<details><summary><code>client.invoices.<a href="src/fern/invoices/client.py">list_invoices</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of invoices for a given location. The response 
is paginated. If truncated, the response includes a `cursor` that you    
use in a subsequent request to retrieve the next set of invoices.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.invoices.list_invoices(
    location_id="location_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the location for which to list invoices.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint. 
Provide this cursor to retrieve the next set of results for your original query.

For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of invoices to return (200 is the maximum `limit`). 
If not provided, the server uses a default limit of 100 invoices.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/fern/invoices/client.py">create_invoice</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a draft [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) 
for an order created using the Orders API.

A draft invoice remains in your account and no action is taken. 
You must publish the invoice before Square can process it (send it to the customer's email address or charge the customer’s card on file).
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
from fern import FernApi, Invoice

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.invoices.create_invoice(
    invoice=Invoice(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice:** `Invoice` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique string that identifies the `CreateInvoice` request. If you do not 
provide `idempotency_key` (or provide an empty string as the value), the endpoint 
treats each request as independent.

For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/fern/invoices/client.py">search_invoices</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for invoices from a location specified in 
the filter. You can optionally specify customers in the filter for whom to 
retrieve invoices. In the current implementation, you can only specify one location and 
optionally one customer.

The response is paginated. If truncated, the response includes a `cursor` 
that you use in a subsequent request to retrieve the next set of invoices.
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
from fern import FernApi, InvoiceFilter, InvoiceQuery

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.invoices.search_invoices(
    query=InvoiceQuery(
        filter=InvoiceFilter(
            location_ids=["location_ids"],
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

**query:** `InvoiceQuery` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint. 
Provide this cursor to retrieve the next set of results for your original query.

For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of invoices to return (200 is the maximum `limit`). 
If not provided, the server uses a default limit of 100 invoices.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/fern/invoices/client.py">get_invoice</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves an invoice by invoice ID.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.invoices.get_invoice(
    invoice_id="invoice_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `str` — The ID of the invoice to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/fern/invoices/client.py">update_invoice</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an invoice by modifying fields, clearing fields, or both. For most updates, you can use a sparse 
`Invoice` object to add fields or change values and use the `fields_to_clear` field to specify fields to clear. 
However, some restrictions apply. For example, you cannot change the `order_id` or `location_id` field and you 
must provide the complete `custom_fields` list to update a custom field. Published invoices have additional restrictions.
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
from fern import FernApi, Invoice

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.invoices.update_invoice(
    invoice_id="invoice_id",
    invoice=Invoice(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `str` — The ID of the invoice to update.
    
</dd>
</dl>

<dl>
<dd>

**invoice:** `Invoice` 
    
</dd>
</dl>

<dl>
<dd>

**fields_to_clear:** `typing.Optional[typing.Sequence[str]]` 

The list of fields to clear.
For examples, see [Update an invoice](https://developer.squareup.com/docs/invoices-api/overview#update-an-invoice).
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique string that identifies the `UpdateInvoice` request. If you do not
provide `idempotency_key` (or provide an empty string as the value), the endpoint
treats each request as independent.

For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/fern/invoices/client.py">delete_invoice</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the specified invoice. When an invoice is deleted, the 
associated order status changes to CANCELED. You can only delete a draft 
invoice (you cannot delete a published invoice, including one that is scheduled for processing).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.invoices.delete_invoice(
    invoice_id="invoice_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `str` — The ID of the invoice to delete.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 

The version of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to delete.
If you do not know the version, you can call [GetInvoice](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/get-invoice) or 
[ListInvoices](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/list-invoices).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/fern/invoices/client.py">cancel_invoice</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels an invoice. The seller cannot collect payments for 
the canceled invoice.

You cannot cancel an invoice in the `DRAFT` state or in a terminal state: `PAID`, `REFUNDED`, `CANCELED`, or `FAILED`.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.invoices.cancel_invoice(
    invoice_id="invoice_id",
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `str` — The ID of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to cancel.
    
</dd>
</dl>

<dl>
<dd>

**version:** `int` 

The version of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to cancel.
If you do not know the version, you can call 
[GetInvoice](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/get-invoice) or [ListInvoices](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/list-invoices).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/fern/invoices/client.py">publish_invoice</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publishes the specified draft invoice. 

After an invoice is published, Square 
follows up based on the invoice configuration. For example, Square 
sends the invoice to the customer's email address, charges the customer's card on file, or does 
nothing. Square also makes the invoice available on a Square-hosted invoice page. 

The invoice `status` also changes from `DRAFT` to a status 
based on the invoice configuration. For example, the status changes to `UNPAID` if 
Square emails the invoice or `PARTIALLY_PAID` if Square charge a card on file for a portion of the 
invoice amount.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.invoices.publish_invoice(
    invoice_id="invoice_id",
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `str` — The ID of the invoice to publish.
    
</dd>
</dl>

<dl>
<dd>

**version:** `int` 

The version of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to publish.
This must match the current version of the invoice; otherwise, the request is rejected.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique string that identifies the `PublishInvoice` request. If you do not 
provide `idempotency_key` (or provide an empty string as the value), the endpoint 
treats each request as independent.

For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Labor
<details><summary><code>client.labor.<a href="src/fern/labor/client.py">list_break_types</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of `BreakType` instances for a business.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.labor.list_break_types()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

Filter the returned `BreakType` results to only those that are associated with the
specified location.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of `BreakType` results to return per page. The number can range between 1
and 200. The default is 200.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A pointer to the next page of `BreakType` results to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/fern/labor/client.py">create_break_type</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new `BreakType`.

A `BreakType` is a template for creating `Break` objects.
You must provide the following values in your request to this
endpoint:

- `location_id`
- `break_name`
- `expected_duration`
- `is_paid`

You can only have three `BreakType` instances per location. If you attempt to add a fourth
`BreakType` for a location, an `INVALID_REQUEST_ERROR` "Exceeded limit of 3 breaks per location."
is returned.
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
from fern import BreakType, FernApi

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.labor.create_break_type(
    break_type=BreakType(
        break_name="break_name",
        expected_duration="expected_duration",
        is_paid=True,
        location_id="location_id",
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

**break_type:** `BreakType` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — A unique string value to ensure the idempotency of the operation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/fern/labor/client.py">get_break_type</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single `BreakType` specified by `id`.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.labor.get_break_type(
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

**id:** `str` — The UUID for the `BreakType` being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/fern/labor/client.py">update_break_type</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing `BreakType`.
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
from fern import BreakType, FernApi

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.labor.update_break_type(
    id="id",
    break_type=BreakType(
        break_name="break_name",
        expected_duration="expected_duration",
        is_paid=True,
        location_id="location_id",
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

**id:** `str` —  The UUID for the `BreakType` being updated.
    
</dd>
</dl>

<dl>
<dd>

**break_type:** `BreakType` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/fern/labor/client.py">delete_break_type</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing `BreakType`.

A `BreakType` can be deleted even if it is referenced from a `Shift`.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.labor.delete_break_type(
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

**id:** `str` — The UUID for the `BreakType` being deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/fern/labor/client.py">list_employee_wages</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of `EmployeeWage` instances for a business.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.labor.list_employee_wages()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**employee_id:** `typing.Optional[str]` — Filter the returned wages to only those that are associated with the specified employee.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of `EmployeeWage` results to return per page. The number can range between
1 and 200. The default is 200.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A pointer to the next page of `EmployeeWage` results to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/fern/labor/client.py">get_employee_wage</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single `EmployeeWage` specified by `id`.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.labor.get_employee_wage(
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

**id:** `str` — The UUID for the `EmployeeWage` being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/fern/labor/client.py">create_shift</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new `Shift`.

A `Shift` represents a complete workday for a single employee.
You must provide the following values in your request to this
endpoint:

- `location_id`
- `employee_id`
- `start_at`

An attempt to create a new `Shift` can result in a `BAD_REQUEST` error when:
- The `status` of the new `Shift` is `OPEN` and the employee has another
shift with an `OPEN` status.
- The `start_at` date is in the future.
- The `start_at` or `end_at` date overlaps another shift for the same employee.
- The `Break` instances are set in the request and a break `start_at`
is before the `Shift.start_at`, a break `end_at` is after
the `Shift.end_at`, or both.
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
from fern import FernApi, Shift

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.labor.create_shift(
    shift=Shift(
        start_at="start_at",
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

**shift:** `Shift` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — A unique string value to ensure the idempotency of the operation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/fern/labor/client.py">search_shifts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of `Shift` records for a business.
The list to be returned can be filtered by:
- Location IDs.
- Employee IDs.
- Shift status (`OPEN` and `CLOSED`).
- Shift start.
- Shift end.
- Workday details.

The list can be sorted by:
- `start_at`.
- `end_at`.
- `created_at`.
- `updated_at`.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.labor.search_shifts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — An opaque cursor for fetching the next page.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of resources in a page (200 by default).
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[ShiftQuery]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/fern/labor/client.py">get_shift</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single `Shift` specified by `id`.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.labor.get_shift(
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

**id:** `str` — The UUID for the `Shift` being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/fern/labor/client.py">update_shift</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing `Shift`.

When adding a `Break` to a `Shift`, any earlier `Break` instances in the `Shift` have
the `end_at` property set to a valid RFC-3339 datetime string.

When closing a `Shift`, all `Break` instances in the `Shift` must be complete with `end_at`
set on each `Break`.
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
from fern import FernApi, Shift

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.labor.update_shift(
    id="id",
    shift=Shift(
        start_at="start_at",
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

**id:** `str` — The ID of the object being updated.
    
</dd>
</dl>

<dl>
<dd>

**shift:** `Shift` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/fern/labor/client.py">delete_shift</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a `Shift`.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.labor.delete_shift(
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

**id:** `str` — The UUID for the `Shift` being deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/fern/labor/client.py">list_team_member_wages</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of `TeamMemberWage` instances for a business.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.labor.list_team_member_wages()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_member_id:** `typing.Optional[str]` 

Filter the returned wages to only those that are associated with the
specified team member.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of `TeamMemberWage` results to return per page. The number can range between
1 and 200. The default is 200.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A pointer to the next page of `EmployeeWage` results to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/fern/labor/client.py">get_team_member_wage</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single `TeamMemberWage` specified by `id `.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.labor.get_team_member_wage(
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

**id:** `str` — The UUID for the `TeamMemberWage` being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/fern/labor/client.py">list_workweek_configs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `WorkweekConfig` instances for a business.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.labor.list_workweek_configs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of `WorkweekConfigs` results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A pointer to the next page of `WorkweekConfig` results to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/fern/labor/client.py">update_workweek_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a `WorkweekConfig`.
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
from fern import FernApi, WorkweekConfig

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.labor.update_workweek_config(
    id="id",
    workweek_config=WorkweekConfig(
        start_of_day_local_time="start_of_day_local_time",
        start_of_week="start_of_week",
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

**id:** `str` — The UUID for the `WorkweekConfig` object being updated.
    
</dd>
</dl>

<dl>
<dd>

**workweek_config:** `WorkweekConfig` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Locations
<details><summary><code>client.locations.<a href="src/fern/locations/client.py">list_locations</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides information of all locations of a business.

Many Square API endpoints require a `location_id` parameter.
The `id` field of the [`Location`](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) objects returned by this
endpoint correspond to that `location_id` parameter.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.locations.list_locations()

```
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

<details><summary><code>client.locations.<a href="src/fern/locations/client.py">create_location</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a location.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.locations.create_location()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location:** `typing.Optional[Location]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.locations.<a href="src/fern/locations/client.py">retrieve_location</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves details of a location. You can specify "main" 
as the location ID to retrieve details of the 
main location.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.locations.retrieve_location(
    location_id="location_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` 

The ID of the location to retrieve. If you specify the string "main",
then the endpoint returns the main location.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.locations.<a href="src/fern/locations/client.py">update_location</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a location.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.locations.update_location(
    location_id="location_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the location to update.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[Location]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Checkout
<details><summary><code>client.checkout.<a href="src/fern/checkout/client.py">create_checkout</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Links a `checkoutId` to a `checkout_page_url` that customers are
directed to in order to provide their payment information using a
payment processing workflow hosted on connect.squareup.com.
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
from fern import CreateOrderRequest, FernApi

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.checkout.create_checkout(
    location_id="location_id",
    idempotency_key="idempotency_key",
    order=CreateOrderRequest(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the business location to associate the checkout with.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this checkout among others you have created. It can be
any valid string but must be unique for every order sent to Square Checkout for a given location ID.

The idempotency key is used to avoid processing the same order more than once. If you are 
unsure whether a particular checkout was created successfully, you can attempt it again with
the same idempotency key and all the same other parameters without worrying about creating duplicates.

You should use a random number/string generator native to the language
you are working in to generate strings for your idempotency keys.

For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**order:** `CreateOrderRequest` 
    
</dd>
</dl>

<dl>
<dd>

**additional_recipients:** `typing.Optional[typing.Sequence[ChargeRequestAdditionalRecipient]]` 

The basic primitive of a multi-party transaction. The value is optional.
The transaction facilitated by you can be split from here.

If you provide this value, the `amount_money` value in your `additional_recipients` field
cannot be more than 90% of the `total_money` calculated by Square for your order.
The `location_id` must be a valid seller location where the checkout is occurring.

This field requires `PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS` OAuth permission.

This field is currently not supported in the Square Sandbox.
    
</dd>
</dl>

<dl>
<dd>

**ask_for_shipping_address:** `typing.Optional[bool]` 

If `true`, Square Checkout collects shipping information on your behalf and stores 
that information with the transaction information in the Square Seller Dashboard.

Default: `false`.
    
</dd>
</dl>

<dl>
<dd>

**merchant_support_email:** `typing.Optional[str]` 

The email address to display on the Square Checkout confirmation page
and confirmation email that the buyer can use to contact the seller.

If this value is not set, the confirmation page and email display the
primary email address associated with the seller's Square account.

Default: none; only exists if explicitly set.
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` 

An optional note to associate with the `checkout` object.

This value cannot exceed 60 characters.
    
</dd>
</dl>

<dl>
<dd>

**pre_populate_buyer_email:** `typing.Optional[str]` 

If provided, the buyer's email is prepopulated on the checkout page
as an editable text field.

Default: none; only exists if explicitly set.
    
</dd>
</dl>

<dl>
<dd>

**pre_populate_shipping_address:** `typing.Optional[Address]` 
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` 

The URL to redirect to after the checkout is completed with `checkoutId`,
`transactionId`, and `referenceId` appended as URL parameters. For example,
if the provided redirect URL is `http://www.example.com/order-complete`, a
successful transaction redirects the customer to:

<pre><code>http://www.example.com/order-complete?checkoutId=xxxxxx&amp;referenceId=xxxxxx&amp;transactionId=xxxxxx</code></pre>

If you do not provide a redirect URL, Square Checkout displays an order
confirmation page on your behalf; however, it is strongly recommended that
you provide a redirect URL so you can verify the transaction results and
finalize the order through your existing/normal confirmation workflow.

Default: none; only exists if explicitly set.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Transactions
<details><summary><code>client.transactions.<a href="src/fern/transactions/client.py">list_refunds</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists refunds for one of a business's locations.

In addition to full or partial tender refunds processed through Square APIs,
refunds may result from itemized returns or exchanges through Square's
Point of Sale applications.

Refunds with a `status` of `PENDING` are not currently included in this
endpoint's response.

Max results per [page](https://developer.squareup.com/docs/working-with-apis/pagination): 50
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.transactions.list_refunds(
    location_id="location_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the location to list refunds for.
    
</dd>
</dl>

<dl>
<dd>

**begin_time:** `typing.Optional[str]` 

The beginning of the requested reporting period, in RFC 3339 format.

See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.

Default value: The current time minus one year.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` 

The end of the requested reporting period, in RFC 3339 format.

See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.

Default value: The current time.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[str]` 

The order in which results are listed in the response (`ASC` for
oldest first, `DESC` for newest first).

Default value: `DESC`
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for your original query.

See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/fern/transactions/client.py">list_transactions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists transactions for a particular location.

Transactions include payment information from sales and exchanges and refund
information from returns and exchanges.

Max results per [page](https://developer.squareup.com/docs/working-with-apis/pagination): 50
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.transactions.list_transactions(
    location_id="location_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the location to list transactions for.
    
</dd>
</dl>

<dl>
<dd>

**begin_time:** `typing.Optional[str]` 

The beginning of the requested reporting period, in RFC 3339 format.

See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.

Default value: The current time minus one year.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` 

The end of the requested reporting period, in RFC 3339 format.

See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.

Default value: The current time.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[str]` 

The order in which results are listed in the response (`ASC` for
oldest first, `DESC` for newest first).

Default value: `DESC`
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for your original query.

See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/fern/transactions/client.py">charge</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Charges a card represented by a card nonce or a customer's card on file.

Your request to this endpoint must include _either_:

- A value for the `card_nonce` parameter (to charge a card payment token generated
with the Web Payments SDK)
- Values for the `customer_card_id` and `customer_id` parameters (to charge
a customer's card on file)

In order for an eCommerce payment to potentially qualify for
[Square chargeback protection](https://squareup.com/help/article/5394), you
_must_ provide values for the following parameters in your request:

- `buyer_email_address`
- At least one of `billing_address` or `shipping_address`

When this response is returned, the amount of Square's processing fee might not yet be
calculated. To obtain the processing fee, wait about ten seconds and call
[RetrieveTransaction](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/retrieve-transaction). See the `processing_fee_money`
field of each [Tender included](https://developer.squareup.com/reference/square_2021-08-18/objects/Tender) in the transaction.
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
from fern import FernApi, Money

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.transactions.charge(
    location_id="location_id",
    amount_money=Money(),
    idempotency_key="idempotency_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the location to associate the created transaction with.
    
</dd>
</dl>

<dl>
<dd>

**amount_money:** `Money` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A value you specify that uniquely identifies this
transaction among transactions you've created.

If you're unsure whether a particular transaction succeeded,
you can reattempt it with the same idempotency key without
worrying about double-charging the buyer.

See [Idempotency keys](https://developer.squareup.com/docs/working-with-apis/idempotency) for more information.
    
</dd>
</dl>

<dl>
<dd>

**additional_recipients:** `typing.Optional[typing.Sequence[AdditionalRecipient]]` 

The basic primitive of multi-party transaction. The value is optional.
The transaction facilitated by you can be split from here.

If you provide this value, the `amount_money` value in your additional_recipients
must not be more than 90% of the `amount_money` value in the charge request.
The `location_id` must be the valid location of the app owner merchant.

This field requires the `PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS` OAuth permission.

This field is currently not supported in sandbox.
    
</dd>
</dl>

<dl>
<dd>

**billing_address:** `typing.Optional[Address]` 
    
</dd>
</dl>

<dl>
<dd>

**buyer_email_address:** `typing.Optional[str]` 

The buyer's email address, if available. This value is optional,
but this transaction is ineligible for chargeback protection if it is not
provided.
    
</dd>
</dl>

<dl>
<dd>

**card_nonce:** `typing.Optional[str]` 

A payment token generated from the [Card.tokenize()](https://developer.squareup.com/reference/sdks/web/payments/objects/Card#Card.tokenize) that represents the card
to charge.

The application that provides a payment token to this endpoint must be the
_same application_ that generated the payment token with the Web Payments SDK.
Otherwise, the nonce is invalid.

Do not provide a value for this field if you provide a value for
`customer_card_id`.
    
</dd>
</dl>

<dl>
<dd>

**customer_card_id:** `typing.Optional[str]` 

The ID of the customer card on file to charge. Do
not provide a value for this field if you provide a value for `card_nonce`.

If you provide this value, you _must_ also provide a value for
`customer_id`.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` 

The ID of the customer to associate this transaction with. This field
is required if you provide a value for `customer_card_id`, and optional
otherwise.
    
</dd>
</dl>

<dl>
<dd>

**delay_capture:** `typing.Optional[bool]` 

If `true`, the request will only perform an Auth on the provided
card. You can then later perform either a Capture (with the
[CaptureTransaction](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/capture-transaction) endpoint) or a Void
(with the [VoidTransaction](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/void-transaction) endpoint).

Default value: `false`
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` 

An optional note to associate with the transaction.

This value cannot exceed 60 characters.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `typing.Optional[str]` 

The ID of the order to associate with this transaction.

If you provide this value, the `amount_money` value of your request must
__exactly match__ the value of the order's `total_money` field.
    
</dd>
</dl>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` 

An optional ID you can associate with the transaction for your own
purposes (such as to associate the transaction with an entity ID in your
own database).

This value cannot exceed 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**shipping_address:** `typing.Optional[Address]` 
    
</dd>
</dl>

<dl>
<dd>

**verification_token:** `typing.Optional[str]` 

A token generated by SqPaymentForm's verifyBuyer() that represents
customer's device info and 3ds challenge result.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/fern/transactions/client.py">retrieve_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves details for a single transaction.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.transactions.retrieve_transaction(
    location_id="location_id",
    transaction_id="transaction_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the transaction's associated location.
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `str` — The ID of the transaction to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/fern/transactions/client.py">capture_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Captures a transaction that was created with the [Charge](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/charge)
endpoint with a `delay_capture` value of `true`.


See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture)
for more information.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.transactions.capture_transaction(
    location_id="location_id",
    transaction_id="transaction_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/fern/transactions/client.py">create_refund</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiates a refund for a previously charged tender.

You must issue a refund within 120 days of the associated payment. See
[this article](https://squareup.com/help/us/en/article/5060) for more information
on refund behavior.

NOTE: Card-present transactions with Interac credit cards **cannot be
refunded using the Connect API**. Interac transactions must refunded
in-person (e.g., dipping the card using POS app).
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
from fern import FernApi, Money

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.transactions.create_refund(
    location_id="location_id",
    transaction_id="transaction_id",
    amount_money=Money(),
    idempotency_key="idempotency_key",
    tender_id="tender_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the original transaction's associated location.
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `str` — The ID of the original transaction that includes the tender to refund.
    
</dd>
</dl>

<dl>
<dd>

**amount_money:** `Money` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A value you specify that uniquely identifies this
refund among refunds you've created for the tender.

If you're unsure whether a particular refund succeeded,
you can reattempt it with the same idempotency key without
worrying about duplicating the refund.

See [Idempotency keys](https://developer.squareup.com/docs/working-with-apis/idempotency) for more information.
    
</dd>
</dl>

<dl>
<dd>

**tender_id:** `str` 

The ID of the tender to refund.

A [`Transaction`](https://developer.squareup.com/reference/square_2021-08-18/objects/Transaction) has one or more `tenders` (i.e., methods
of payment) associated with it, and you refund each tender separately with
the Connect API.
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` 

A description of the reason for the refund.

Default value: `Refund via API`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/fern/transactions/client.py">void_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels a transaction that was created with the [Charge](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/charge)
endpoint with a `delay_capture` value of `true`.


See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture)
for more information.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.transactions.void_transaction(
    location_id="location_id",
    transaction_id="transaction_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Loyalty
<details><summary><code>client.loyalty.<a href="src/fern/loyalty/client.py">create_loyalty_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a loyalty account. To create a loyalty account, you must provide the `program_id` and a `mapping` with the `phone_number` of the buyer.
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
from fern import FernApi, LoyaltyAccount

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.loyalty.create_loyalty_account(
    idempotency_key="idempotency_key",
    loyalty_account=LoyaltyAccount(
        program_id="program_id",
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

**idempotency_key:** `str` 

A unique string that identifies this `CreateLoyaltyAccount` request. 
Keys can be any valid string, but must be unique for every request.
    
</dd>
</dl>

<dl>
<dd>

**loyalty_account:** `LoyaltyAccount` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.<a href="src/fern/loyalty/client.py">search_loyalty_accounts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for loyalty accounts in a loyalty program.  

You can search for a loyalty account using the phone number or customer ID associated with the account. To return all loyalty accounts, specify an empty `query` object or omit it entirely.  

Search results are sorted by `created_at` in ascending order.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.loyalty.search_loyalty_accounts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to 
this endpoint. Provide this to retrieve the next set of 
results for the original query.

For more information, 
see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to include in the response.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[SearchLoyaltyAccountsRequestLoyaltyAccountQuery]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.<a href="src/fern/loyalty/client.py">retrieve_loyalty_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a loyalty account.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.loyalty.retrieve_loyalty_account(
    account_id="account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — The ID of the [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.<a href="src/fern/loyalty/client.py">accumulate_loyalty_points</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds points to a loyalty account.

- If you are using the Orders API to manage orders, you only provide the `order_id`. 
The endpoint reads the order to compute points to add to the buyer's account.
- If you are not using the Orders API to manage orders, 
you first perform a client-side computation to compute the points.  
For spend-based and visit-based programs, you can first call 
[CalculateLoyaltyPoints](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/calculate-loyalty-points) to compute the points  
that you provide to this endpoint. 

__Note:__ The country of the seller's Square account determines whether tax is included in the purchase amount when accruing points for spend-based and visit-based programs. 
For more information, see [Availability of Square Loyalty](https://developer.squareup.com/docs/loyalty-api/overview#loyalty-market-availability).
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
from fern import FernApi, LoyaltyEventAccumulatePoints

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.loyalty.accumulate_loyalty_points(
    account_id="account_id",
    accumulate_points=LoyaltyEventAccumulatePoints(),
    idempotency_key="idempotency_key",
    location_id="location_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — The [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) ID to which to add the points.
    
</dd>
</dl>

<dl>
<dd>

**accumulate_points:** `LoyaltyEventAccumulatePoints` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies the `AccumulateLoyaltyPoints` request. 
Keys can be any valid string but must be unique for every request.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `str` — The [location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) where the purchase was made.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.<a href="src/fern/loyalty/client.py">adjust_loyalty_points</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds points to or subtracts points from a buyer's account. 

Use this endpoint only when you need to manually adjust points. Otherwise, in your application flow, you call 
[AccumulateLoyaltyPoints](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/accumulate-loyalty-points) 
to add points when a buyer pays for the purchase.
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
from fern import FernApi, LoyaltyEventAdjustPoints

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.loyalty.adjust_loyalty_points(
    account_id="account_id",
    adjust_points=LoyaltyEventAdjustPoints(
        points=1,
    ),
    idempotency_key="idempotency_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — The ID of the [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) in which to adjust the points.
    
</dd>
</dl>

<dl>
<dd>

**adjust_points:** `LoyaltyEventAdjustPoints` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this `AdjustLoyaltyPoints` request. 
Keys can be any valid string, but must be unique for every request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.<a href="src/fern/loyalty/client.py">search_loyalty_events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for loyalty events.

A Square loyalty program maintains a ledger of events that occur during the lifetime of a 
buyer's loyalty account. Each change in the point balance 
(for example, points earned, points redeemed, and points expired) is 
recorded in the ledger. Using this endpoint, you can search the ledger for events.

Search results are sorted by `created_at` in descending order.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.loyalty.search_loyalty_events()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for your original query.
For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to include in the response. 
The last page might contain fewer events. 
The default is 30 events.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[LoyaltyEventQuery]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.<a href="src/fern/loyalty/client.py">list_loyalty_programs</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of loyalty programs in the seller's account.
Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).


Replaced with [RetrieveLoyaltyProgram](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/retrieve-loyalty-program) when used with the keyword `main`.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.loyalty.list_loyalty_programs()

```
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

<details><summary><code>client.loyalty.<a href="src/fern/loyalty/client.py">retrieve_loyalty_program</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the loyalty program in a seller's account, specified by the program ID or the keyword `main`. 

Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.loyalty.retrieve_loyalty_program(
    program_id="program_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `str` — The ID of the loyalty program or the keyword `main`. Either value can be used to retrieve the single loyalty program that belongs to the seller.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.<a href="src/fern/loyalty/client.py">calculate_loyalty_points</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Calculates the points a purchase earns.

- If you are using the Orders API to manage orders, you provide `order_id` in the request. The 
endpoint calculates the points by reading the order.
- If you are not using the Orders API to manage orders, you provide the purchase amount in 
the request for the endpoint to calculate the points.

An application might call this endpoint to show the points that a buyer can earn with the 
specific purchase.

__Note:__ The country of the seller's Square account determines whether tax is included in the purchase amount when accruing points for spend-based and visit-based programs. 
For more information, see [Availability of Square Loyalty](https://developer.squareup.com/docs/loyalty-api/overview#loyalty-market-availability).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.loyalty.calculate_loyalty_points(
    program_id="program_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `str` — The [loyalty program](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyProgram) ID, which defines the rules for accruing points.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `typing.Optional[str]` 

The [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) ID for which to calculate the points.
Specify this field if your application uses the Orders API to process orders.
Otherwise, specify the `transaction_amount_money`.
    
</dd>
</dl>

<dl>
<dd>

**transaction_amount_money:** `typing.Optional[Money]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.<a href="src/fern/loyalty/client.py">create_loyalty_reward</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a loyalty reward. In the process, the endpoint does following:

- Uses the `reward_tier_id` in the request to determine the number of points 
to lock for this reward. 
- If the request includes `order_id`, it adds the reward and related discount to the order. 

After a reward is created, the points are locked and 
not available for the buyer to redeem another reward.
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
from fern import FernApi, LoyaltyReward

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.loyalty.create_loyalty_reward(
    idempotency_key="idempotency_key",
    reward=LoyaltyReward(
        loyalty_account_id="loyalty_account_id",
        reward_tier_id="reward_tier_id",
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

**idempotency_key:** `str` 

A unique string that identifies this `CreateLoyaltyReward` request. 
Keys can be any valid string, but must be unique for every request.
    
</dd>
</dl>

<dl>
<dd>

**reward:** `LoyaltyReward` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.<a href="src/fern/loyalty/client.py">search_loyalty_rewards</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for loyalty rewards in a loyalty account. 

In the current implementation, the endpoint supports search by the reward `status`.

If you know a reward ID, use the 
[RetrieveLoyaltyReward](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/retrieve-loyalty-reward) endpoint.

Search results are sorted by `updated_at` in descending order.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.loyalty.search_loyalty_rewards()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to 
this endpoint. Provide this to retrieve the next set of 
results for the original query.
For more information, 
see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return in the response.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[SearchLoyaltyRewardsRequestLoyaltyRewardQuery]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.<a href="src/fern/loyalty/client.py">retrieve_loyalty_reward</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a loyalty reward.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.loyalty.retrieve_loyalty_reward(
    reward_id="reward_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**reward_id:** `str` — The ID of the [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.<a href="src/fern/loyalty/client.py">delete_loyalty_reward</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a loyalty reward by doing the following:

- Returns the loyalty points back to the loyalty account.
- If an order ID was specified when the reward was created 
(see [CreateLoyaltyReward](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/create-loyalty-reward)), 
it updates the order by removing the reward and related 
discounts.

You cannot delete a reward that has reached the terminal state (REDEEMED).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.loyalty.delete_loyalty_reward(
    reward_id="reward_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**reward_id:** `str` — The ID of the [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward) to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.<a href="src/fern/loyalty/client.py">redeem_loyalty_reward</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Redeems a loyalty reward.

The endpoint sets the reward to the `REDEEMED` terminal state. 

If you are using your own order processing system (not using the 
Orders API), you call this endpoint after the buyer paid for the 
purchase.

After the reward reaches the terminal state, it cannot be deleted. 
In other words, points used for the reward cannot be returned 
to the account.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.loyalty.redeem_loyalty_reward(
    reward_id="reward_id",
    idempotency_key="idempotency_key",
    location_id="location_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**reward_id:** `str` — The ID of the [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward) to redeem.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this `RedeemLoyaltyReward` request. 
Keys can be any valid string, but must be unique for every request.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `str` — The ID of the [location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) where the reward is redeemed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Merchants
<details><summary><code>client.merchants.<a href="src/fern/merchants/client.py">list_merchants</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns `Merchant` information for a given access token.

If you don't know a `Merchant` ID, you can use this endpoint to retrieve the merchant ID for an access token.
You can specify your personal access token to get your own merchant information or specify an OAuth token
to get the information for the  merchant that granted you access.

If you know the merchant ID, you can also use the [RetrieveMerchant](https://developer.squareup.com/reference/square_2021-08-18/merchants-api/retrieve-merchant)
endpoint to get the merchant information.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.merchants.list_merchants()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[int]` — The cursor generated by the previous response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.<a href="src/fern/merchants/client.py">retrieve_merchant</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a `Merchant` object for the given `merchant_id`.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.merchants.retrieve_merchant(
    merchant_id="merchant_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` 

The ID of the merchant to retrieve. If the string "me" is supplied as the ID,
then retrieve the merchant that is currently accessible to this call.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Orders
<details><summary><code>client.orders.<a href="src/fern/orders/client.py">create_order</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) that can include information about products for
purchase and settings to apply to the purchase.

To pay for a created order, see 
[Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).

You can modify open orders using the [UpdateOrder](https://developer.squareup.com/reference/square_2021-08-18/orders-api/update-order) endpoint.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.orders.create_order()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A value you specify that uniquely identifies this
order among orders you have created.

If you are unsure whether a particular order was created successfully,
you can try it again with the same idempotency key without
worrying about creating duplicate orders.

For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[Order]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/fern/orders/client.py">batch_retrieve_orders</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a set of [orders](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) by their IDs.

If a given order ID does not exist, the ID is ignored instead of generating an error.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.orders.batch_retrieve_orders(
    order_ids=["order_ids"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_ids:** `typing.Sequence[str]` — The IDs of the orders to retrieve. A maximum of 100 orders can be retrieved per request.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

The ID of the location for these orders. This field is optional: omit it to retrieve
orders within the scope of the current authorization's merchant ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/fern/orders/client.py">calculate_order</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enables applications to preview order pricing without creating an order.
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
from fern import FernApi, Order

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.orders.calculate_order(
    order=Order(
        location_id="location_id",
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

**order:** `Order` 
    
</dd>
</dl>

<dl>
<dd>

**proposed_rewards:** `typing.Optional[typing.Sequence[OrderReward]]` 

Identifies one or more loyalty reward tiers to apply during the order calculation.
The discounts defined by the reward tiers are added to the order only to preview the
effect of applying the specified rewards. The rewards do not correspond to actual
redemptions; that is, no `reward`s are created. Therefore, the reward `id`s are
random strings used only to reference the reward tier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/fern/orders/client.py">search_orders</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search all orders for one or more locations. Orders include all sales,
returns, and exchanges regardless of how or when they entered the Square
ecosystem (such as Point of Sale, Invoices, and Connect APIs).

`SearchOrders` requests need to specify which locations to search and define a
[SearchOrdersQuery](https://developer.squareup.com/reference/square_2021-08-18/objects/SearchOrdersQuery) object that controls
how to sort or filter the results. Your `SearchOrdersQuery` can:

  Set filter criteria.
  Set the sort order.
  Determine whether to return results as complete `Order` objects or as
[OrderEntry](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderEntry) objects.

Note that details for orders processed with Square Point of Sale while in
offline mode might not be transmitted to Square for up to 72 hours. Offline
orders have a `created_at` value that reflects the time the order was created,
not the time it was subsequently transmitted to Square.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.orders.search_orders()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for your original query.
For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to be returned in a single page. It is
possible to receive fewer results than the specified limit on a given page.

Default: `500`
    
</dd>
</dl>

<dl>
<dd>

**location_ids:** `typing.Optional[typing.Sequence[str]]` 

The location IDs for the orders to query. All locations must belong to
the same merchant.

Min: 1 location ID.

Max: 10 location IDs.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[SearchOrdersQuery]` 
    
</dd>
</dl>

<dl>
<dd>

**return_entries:** `typing.Optional[bool]` 

A Boolean that controls the format of the search results. If `true`,
`SearchOrders` returns [OrderEntry](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderEntry) objects. If `false`, `SearchOrders`
returns complete order objects.

Default: `false`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/fern/orders/client.py">retrieve_order</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves an [Order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) by ID.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.orders.retrieve_order(
    order_id="order_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` — The ID of the order to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/fern/orders/client.py">update_order</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an open [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) by adding, replacing, or deleting
fields. Orders with a `COMPLETED` or `CANCELED` state cannot be updated.

An `UpdateOrder` request requires the following:

- The `order_id` in the endpoint path, identifying the order to update.
- The latest `version` of the order to update.
- The [sparse order](https://developer.squareup.com/docs/orders-api/manage-orders#sparse-order-objects)
containing only the fields to update and the version to which the update is
being applied.
- If deleting fields, the [dot notation paths](https://developer.squareup.com/docs/orders-api/manage-orders#on-dot-notation)
identifying the fields to clear.

To pay for an order, see 
[Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.orders.update_order(
    order_id="order_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` — The ID of the order to update.
    
</dd>
</dl>

<dl>
<dd>

**fields_to_clear:** `typing.Optional[typing.Sequence[str]]` 

The [dot notation paths](https://developer.squareup.com/docs/orders-api/manage-orders#on-dot-notation)
fields to clear. For example, `line_items[uid].note`.
For more information, see [Deleting fields](https://developer.squareup.com/docs/orders-api/manage-orders#delete-fields).
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A value you specify that uniquely identifies this update request.

If you are unsure whether a particular update was applied to an order successfully,
you can reattempt it with the same idempotency key without
worrying about creating duplicate updates to the order.
The latest order version is returned.

For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[Order]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/fern/orders/client.py">pay_order</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Pay for an [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) using one or more approved [payments](https://developer.squareup.com/reference/square_2021-08-18/objects/Payment)
or settle an order with a total of `0`.

The total of the `payment_ids` listed in the request must be equal to the order
total. Orders with a total amount of `0` can be marked as paid by specifying an empty
array of `payment_ids` in the request.

To be used with `PayOrder`, a payment must:

- Reference the order by specifying the `order_id` when [creating the payment](https://developer.squareup.com/reference/square_2021-08-18/payments-api/create-payment).
Any approved payments that reference the same `order_id` not specified in the
`payment_ids` is canceled.
- Be approved with [delayed capture](https://developer.squareup.com/docs/payments-api/take-payments#delayed-capture).
Using a delayed capture payment with `PayOrder` completes the approved payment.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.orders.pay_order(
    order_id="order_id",
    idempotency_key="idempotency_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` — The ID of the order being paid.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A value you specify that uniquely identifies this request among requests you have sent. If
you are unsure whether a particular payment request was completed successfully, you can reattempt
it with the same idempotency key without worrying about duplicate payments.

For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**order_version:** `typing.Optional[int]` — The version of the order being paid. If not supplied, the latest version will be paid.
    
</dd>
</dl>

<dl>
<dd>

**payment_ids:** `typing.Optional[typing.Sequence[str]]` 

The IDs of the [payments](https://developer.squareup.com/reference/square_2021-08-18/objects/Payment) to collect.
The payment total must match the order total.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Payments
<details><summary><code>client.payments.<a href="src/fern/payments/client.py">list_payments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of payments taken by the account making the request.

Results are eventually consistent, and new payments or changes to payments might take several
seconds to appear.

The maximum results per page is 100.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.payments.list_payments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**begin_time:** `typing.Optional[str]` 

The timestamp for the beginning of the reporting period, in RFC 3339 format.
Inclusive. Default: The current time minus one year.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` 

The timestamp for the end of the reporting period, in RFC 3339 format.

Default: The current time.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[str]` 

The order in which results are listed:
- `ASC` - Oldest to newest.
- `DESC` - Newest to oldest (default).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.

For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

Limit results to the location supplied. By default, results are returned
for the default (main) location associated with the seller.
    
</dd>
</dl>

<dl>
<dd>

**total:** `typing.Optional[int]` — The exact amount in the `total_money` for a payment.
    
</dd>
</dl>

<dl>
<dd>

**last4:** `typing.Optional[str]` — The last four digits of a payment card.
    
</dd>
</dl>

<dl>
<dd>

**card_brand:** `typing.Optional[str]` — The brand of the payment card (for example, VISA).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to be returned in a single page.
It is possible to receive fewer results than the specified limit on a given page.

The default value of 100 is also the maximum allowed value. If the provided value is 
greater than 100, it is ignored and the default value is used instead.

Default: `100`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payments.<a href="src/fern/payments/client.py">create_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a payment using the provided source. You can use this endpoint 
to charge a card (credit/debit card or    
Square gift card) or record a payment that the seller received outside of Square 
(cash payment from a buyer or a payment that an external entity 
processed on behalf of the seller).

The endpoint creates a 
`Payment` object and returns it in the response.
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
from fern import FernApi, Money

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.payments.create_payment(
    amount_money=Money(),
    idempotency_key="idempotency_key",
    source_id="source_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amount_money:** `Money` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this `CreatePayment` request. Keys can be any valid string
but must be unique for every `CreatePayment` request.

Max: 45 characters

Note: The number of allowed characters might be less than the stated maximum, if multi-byte
characters are used.

For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `str` 

The ID for the source of funds for this payment. This can be a payment token 
(card nonce) generated by the Square payment form or a card on file made with the 
Customers API. If recording a payment that the seller 
received outside of Square, specify either "CASH" or "EXTERNAL". 
For more information, see 
[Take Payments](https://developer.squareup.com/docs/payments-api/take-payments).
    
</dd>
</dl>

<dl>
<dd>

**accept_partial_authorization:** `typing.Optional[bool]` 

If set to `true` and charging a Square Gift Card, a payment might be returned with
`amount_money` equal to less than what was requested. For example, a request for $20 when charging
a Square Gift Card with a balance of $5 results in an APPROVED payment of $5. You might choose
to prompt the buyer for an additional payment to cover the remainder or cancel the Gift Card
payment. This field cannot be `true` when `autocomplete = true`.

For more information, see
[Partial amount with Square Gift Cards](https://developer.squareup.com/docs/payments-api/take-payments#partial-payment-gift-card).

Default: false
    
</dd>
</dl>

<dl>
<dd>

**app_fee_money:** `typing.Optional[Money]` 
    
</dd>
</dl>

<dl>
<dd>

**autocomplete:** `typing.Optional[bool]` 

If set to `true`, this payment will be completed when possible. If
set to `false`, this payment is held in an approved state until either
explicitly completed (captured) or canceled (voided). For more information, see
[Delayed capture](https://developer.squareup.com/docs/payments-api/take-payments/card-payments#delayed-capture-of-a-card-payment).

Default: true
    
</dd>
</dl>

<dl>
<dd>

**billing_address:** `typing.Optional[Address]` 
    
</dd>
</dl>

<dl>
<dd>

**buyer_email_address:** `typing.Optional[str]` — The buyer's email address.
    
</dd>
</dl>

<dl>
<dd>

**cash_details:** `typing.Optional[CashPaymentDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` 

The [Customer](https://developer.squareup.com/reference/square_2021-08-18/objects/Customer) ID of the customer associated with the payment.

This is required if the `source_id` refers to a card on file created using the Customers API.
    
</dd>
</dl>

<dl>
<dd>

**delay_duration:** `typing.Optional[str]` 

The duration of time after the payment's creation when Square automatically cancels the
payment. This automatic cancellation applies only to payments that do not reach a terminal state
(COMPLETED, CANCELED, or FAILED) before the `delay_duration` time period.

This parameter should be specified as a time duration, in RFC 3339 format, with a minimum value
of 1 minute.

Note: This feature is only supported for card payments. This parameter can only be set for a delayed
capture payment (`autocomplete=false`).

Default:

- Card-present payments: "PT36H" (36 hours) from the creation time.
- Card-not-present payments: "P7D" (7 days) from the creation time.
    
</dd>
</dl>

<dl>
<dd>

**external_details:** `typing.Optional[ExternalPaymentDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

The location ID to associate with the payment. If not specified, the default location is
used.
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` 

An optional note to be entered by the developer when creating a payment.

Limit 500 characters.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `typing.Optional[str]` — Associates a previously created order with this payment.
    
</dd>
</dl>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` 

A user-defined ID to associate with the payment.

You can use this field to associate the payment to an entity in an external system 
(for example, you might specify an order ID that is generated by a third-party shopping cart).

Limit 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**shipping_address:** `typing.Optional[Address]` 
    
</dd>
</dl>

<dl>
<dd>

**statement_description_identifier:** `typing.Optional[str]` 

Optional additional payment information to include on the customer's card statement
as part of the statement description. This can be, for example, an invoice number, ticket number,
or short description that uniquely identifies the purchase.

Note that the `statement_description_identifier` might get truncated on the statement description
to fit the required information including the Square identifier (SQ *) and name of the
seller taking the payment.
    
</dd>
</dl>

<dl>
<dd>

**tip_money:** `typing.Optional[Money]` 
    
</dd>
</dl>

<dl>
<dd>

**verification_token:** `typing.Optional[str]` 

An identifying token generated by [payments.verifyBuyer()](https://developer.squareup.com/reference/sdks/web/payments/objects/Payments#Payments.verifyBuyer).
Verification tokens encapsulate customer device information and 3-D Secure
challenge results to indicate that Square has verified the buyer identity.

For more information, see [SCA Overview](https://developer.squareup.com/docs/sca-overview).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payments.<a href="src/fern/payments/client.py">cancel_payment_by_idempotency_key</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels (voids) a payment identified by the idempotency key that is specified in the
request.

Use this method when the status of a `CreatePayment` request is unknown (for example, after you send a
`CreatePayment` request, a network error occurs and you do not get a response). In this case, you can
direct Square to cancel the payment using this endpoint. In the request, you provide the same
idempotency key that you provided in your `CreatePayment` request that you want to cancel. After
canceling the payment, you can submit your `CreatePayment` request again.

Note that if no payment with the specified idempotency key is found, no action is taken and the endpoint
returns successfully.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.payments.cancel_payment_by_idempotency_key(
    idempotency_key="idempotency_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` — The `idempotency_key` identifying the payment to be canceled.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payments.<a href="src/fern/payments/client.py">get_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves details for a specific payment.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.payments.get_payment(
    payment_id="payment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_id:** `str` — A unique ID for the desired payment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payments.<a href="src/fern/payments/client.py">update_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a payment with the APPROVED status.
You can update the `amount_money` and `tip_money` using this endpoint.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.payments.update_payment(
    payment_id="payment_id",
    idempotency_key="idempotency_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_id:** `str` — The ID of the payment to update.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this `UpdatePayment` request. Keys can be any valid string
but must be unique for every `UpdatePayment` request.

The maximum is 45 characters.

For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**payment:** `typing.Optional[Payment]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payments.<a href="src/fern/payments/client.py">cancel_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels (voids) a payment. You can use this endpoint to cancel a payment with 
the APPROVED `status`.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.payments.cancel_payment(
    payment_id="payment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_id:** `str` — The ID of the payment to cancel.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payments.<a href="src/fern/payments/client.py">complete_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Completes (captures) a payment.
By default, payments are set to complete immediately after they are created.

You can use this endpoint to complete a payment with the APPROVED `status`.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.payments.complete_payment(
    payment_id="payment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_id:** `str` — The unique ID identifying the payment to be completed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Refunds
<details><summary><code>client.refunds.<a href="src/fern/refunds/client.py">list_payment_refunds</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of refunds for the account making the request.

Results are eventually consistent, and new refunds or changes to refunds might take several
seconds to appear.

The maximum results per page is 100.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.refunds.list_payment_refunds()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**begin_time:** `typing.Optional[str]` 

The timestamp for the beginning of the requested reporting period, in RFC 3339 format.

Default: The current time minus one year.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` 

The timestamp for the end of the requested reporting period, in RFC 3339 format.

Default: The current time.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[str]` 

The order in which results are listed:
- `ASC` - Oldest to newest.
- `DESC` - Newest to oldest (default).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.

For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

Limit results to the location supplied. By default, results are returned
for all locations associated with the seller.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 

If provided, only refunds with the given status are returned.
For a list of refund status values, see [PaymentRefund](https://developer.squareup.com/reference/square_2021-08-18/objects/PaymentRefund).

Default: If omitted, refunds are returned regardless of their status.
    
</dd>
</dl>

<dl>
<dd>

**source_type:** `typing.Optional[str]` 

If provided, only refunds with the given source type are returned.
- `CARD` - List refunds only for payments where `CARD` was specified as the payment
source.

Default: If omitted, refunds are returned regardless of the source type.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to be returned in a single page.

It is possible to receive fewer results than the specified limit on a given page.

If the supplied value is greater than 100, no more than 100 results are returned.

Default: 100
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.refunds.<a href="src/fern/refunds/client.py">refund_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Refunds a payment. You can refund the entire payment amount or a
portion of it. You can use this endpoint to refund a card payment or record a 
refund of a cash or external payment. For more information, see
[Refund Payment](https://developer.squareup.com/docs/payments-api/refund-payments).
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
from fern import FernApi, Money

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.refunds.refund_payment(
    amount_money=Money(),
    idempotency_key="idempotency_key",
    payment_id="payment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amount_money:** `Money` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

 A unique string that identifies this `RefundPayment` request. The key can be any valid string
but must be unique for every `RefundPayment` request.

For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `str` — The unique ID of the payment being refunded.
    
</dd>
</dl>

<dl>
<dd>

**app_fee_money:** `typing.Optional[Money]` 
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` — A description of the reason for the refund.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.refunds.<a href="src/fern/refunds/client.py">get_payment_refund</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specific refund using the `refund_id`.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.refunds.get_payment_refund(
    refund_id="refund_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**refund_id:** `str` — The unique ID for the desired `PaymentRefund`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sites
<details><summary><code>client.sites.<a href="src/fern/sites/client.py">list_sites</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the Square Online sites that belong to a seller.


__Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.sites.list_sites()

```
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

## Snippets
<details><summary><code>client.snippets.<a href="src/fern/snippets/client.py">retrieve_snippet</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves your snippet from a Square Online site. A site can contain snippets from multiple snippet applications, but you can retrieve only the snippet that was added by your application.

You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.


__Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.snippets.retrieve_snippet(
    site_id="site_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — The ID of the site that contains the snippet.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.snippets.<a href="src/fern/snippets/client.py">upsert_snippet</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a snippet to a Square Online site or updates the existing snippet on the site. 
The snippet code is appended to the end of the `head` element on every page of the site, except checkout pages. A snippet application can add one snippet to a given site. 

You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.


__Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).
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
from fern import FernApi, Snippet

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.snippets.upsert_snippet(
    site_id="site_id",
    snippet=Snippet(
        content="content",
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

**site_id:** `str` — The ID of the site where you want to add or update the snippet.
    
</dd>
</dl>

<dl>
<dd>

**snippet:** `Snippet` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.snippets.<a href="src/fern/snippets/client.py">delete_snippet</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes your snippet from a Square Online site.

You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.


__Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.snippets.delete_snippet(
    site_id="site_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — The ID of the site that contains the snippet.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Subscriptions
<details><summary><code>client.subscriptions.<a href="src/fern/subscriptions/client.py">create_subscription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a subscription for a customer to a subscription plan.

If you provide a card on file in the request, Square charges the card for
the subscription. Otherwise, Square bills an invoice to the customer's email
address. The subscription starts immediately, unless the request includes
the optional `start_date`. Each individual subscription is associated with a particular location.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.subscriptions.create_subscription(
    customer_id="customer_id",
    location_id="location_id",
    plan_id="plan_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — The ID of the [customer](https://developer.squareup.com/reference/square_2021-08-18/objects/Customer) profile.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `str` — The ID of the location the subscription is associated with.
    
</dd>
</dl>

<dl>
<dd>

**plan_id:** `str` 

The ID of the subscription plan created using the Catalog API.
For more information, see
[Set Up and Manage a Subscription Plan](https://developer.squareup.com/docs/subscriptions-api/setup-plan) and 
[Subscriptions Walkthrough](https://developer.squareup.com/docs/subscriptions-api/walkthrough).
    
</dd>
</dl>

<dl>
<dd>

**canceled_date:** `typing.Optional[str]` 

The date when the subscription should be canceled, in
YYYY-MM-DD format (for example, 2025-02-29). This overrides the plan configuration
if it comes before the date the subscription would otherwise end.
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `typing.Optional[str]` 

The ID of the [customer](https://developer.squareup.com/reference/square_2021-08-18/objects/Customer) [card](https://developer.squareup.com/reference/square_2021-08-18/objects/Card) to charge.
If not specified, Square sends an invoice via email. For an example to
create a customer and add a card on file, see [Subscriptions Walkthrough](https://developer.squareup.com/docs/subscriptions-api/walkthrough).
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique string that identifies this `CreateSubscription` request.
If you do not provide a unique string (or provide an empty string as the value),
the endpoint treats each request as independent.

For more information, see [Idempotency keys](https://developer.squareup.com/docs/working-with-apis/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**price_override_money:** `typing.Optional[Money]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` 

The start date of the subscription, in YYYY-MM-DD format. For example,
2013-01-15. If the start date is left empty, the subscription begins
immediately.
    
</dd>
</dl>

<dl>
<dd>

**tax_percentage:** `typing.Optional[str]` 

The tax to add when billing the subscription.
The percentage is expressed in decimal form, using a `'.'` as the decimal
separator and without a `'%'` sign. For example, a value of 7.5
corresponds to 7.5%.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` 

The timezone that is used in date calculations for the subscription. If unset, defaults to
the location timezone. If a timezone is not configured for the location, defaults to "America/New_York".
Format: the IANA Timezone Database identifier for the location timezone. For
a list of time zones, see [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/fern/subscriptions/client.py">search_subscriptions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for subscriptions.
Results are ordered chronologically by subscription creation date. If
the request specifies more than one location ID,
the endpoint orders the result
by location ID, and then by creation date within each location. If no locations are given
in the query, all locations are searched.

You can also optionally specify `customer_ids` to search by customer.
If left unset, all customers
associated with the specified locations are returned.
If the request specifies customer IDs, the endpoint orders results
first by location, within location by customer ID, and within
customer by subscription creation date.

For more information, see
[Retrieve subscriptions](https://developer.squareup.com/docs/subscriptions-api/overview#retrieve-subscriptions).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.subscriptions.search_subscriptions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for the original query.

For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The upper limit on the number of subscriptions to return
in the response.

Default: `200`
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[SearchSubscriptionsQuery]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/fern/subscriptions/client.py">retrieve_subscription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a subscription.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.subscriptions.retrieve_subscription(
    subscription_id="subscription_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The ID of the subscription to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/fern/subscriptions/client.py">update_subscription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a subscription. You can set, modify, and clear the
`subscription` field values.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.subscriptions.update_subscription(
    subscription_id="subscription_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The ID for the subscription to update.
    
</dd>
</dl>

<dl>
<dd>

**subscription:** `typing.Optional[Subscription]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/fern/subscriptions/client.py">cancel_subscription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets the `canceled_date` field to the end of the active billing period.
After this date, the status changes from ACTIVE to CANCELED.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.subscriptions.cancel_subscription(
    subscription_id="subscription_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The ID of the subscription to cancel.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/fern/subscriptions/client.py">list_subscription_events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all events for a specific subscription.
In the current implementation, only `START_SUBSCRIPTION` and `STOP_SUBSCRIPTION` (when the subscription was canceled) events are returned.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.subscriptions.list_subscription_events(
    subscription_id="subscription_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The ID of the subscription to retrieve the events for.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for the original query.

For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The upper limit on the number of subscription events to return
in the response.

Default: `200`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/fern/subscriptions/client.py">resume_subscription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resumes a deactivated subscription.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.subscriptions.resume_subscription(
    subscription_id="subscription_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The ID of the subscription to resume.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Team
<details><summary><code>client.team.<a href="src/fern/team/client.py">create_team_member</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a single `TeamMember` object. The `TeamMember` object is returned on successful creates.
You must provide the following values in your request to this endpoint:
- `given_name`
- `family_name`

Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#createteammember).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.team.create_team_member()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique string that identifies this `CreateTeamMember` request.
Keys can be any valid string, but must be unique for every request.
For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency).

The minimum length is 1 and the maximum length is 45.
    
</dd>
</dl>

<dl>
<dd>

**team_member:** `typing.Optional[TeamMember]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.team.<a href="src/fern/team/client.py">bulk_create_team_members</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates multiple `TeamMember` objects. The created `TeamMember` objects are returned on successful creates.
This process is non-transactional and processes as much of the request as possible. If one of the creates in
the request cannot be successfully processed, the request is not marked as failed, but the body of the response
contains explicit error information for the failed create.

Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#bulk-create-team-members).
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
from fern import CreateTeamMemberRequest, FernApi

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.team.bulk_create_team_members(
    team_members={"key": CreateTeamMemberRequest()},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_members:** `typing.Dict[str, CreateTeamMemberRequest]` — The data used to create the `TeamMember` objects. Each key is the `idempotency_key` that maps to the `CreateTeamMemberRequest`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.team.<a href="src/fern/team/client.py">bulk_update_team_members</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates multiple `TeamMember` objects. The updated `TeamMember` objects are returned on successful updates.
This process is non-transactional and processes as much of the request as possible. If one of the updates in
the request cannot be successfully processed, the request is not marked as failed, but the body of the response
contains explicit error information for the failed update.
Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#bulk-update-team-members).
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
from fern import FernApi, UpdateTeamMemberRequest

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.team.bulk_update_team_members(
    team_members={"key": UpdateTeamMemberRequest()},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_members:** `typing.Dict[str, UpdateTeamMemberRequest]` — The data used to update the `TeamMember` objects. Each key is the `team_member_id` that maps to the `UpdateTeamMemberRequest`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.team.<a href="src/fern/team/client.py">search_team_members</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of `TeamMember` objects for a business.
The list can be filtered by the following:
- location IDs
- `status`
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.team.search_team_members()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The opaque cursor for fetching the next page. For more information, see
[pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of `TeamMember` objects in a page (100 by default).
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[SearchTeamMembersQuery]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.team.<a href="src/fern/team/client.py">retrieve_team_member</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a `TeamMember` object for the given `TeamMember.id`.
Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrieve-a-team-member).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.team.retrieve_team_member(
    team_member_id="team_member_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_member_id:** `str` — The ID of the team member to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.team.<a href="src/fern/team/client.py">update_team_member</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a single `TeamMember` object. The `TeamMember` object is returned on successful updates.
Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#update-a-team-member).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.team.update_team_member(
    team_member_id="team_member_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_member_id:** `str` — The ID of the team member to update.
    
</dd>
</dl>

<dl>
<dd>

**team_member:** `typing.Optional[TeamMember]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.team.<a href="src/fern/team/client.py">retrieve_wage_setting</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a `WageSetting` object for a team member specified
by `TeamMember.id`.
Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrievewagesetting).
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.team.retrieve_wage_setting(
    team_member_id="team_member_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_member_id:** `str` — The ID of the team member for which to retrieve the wage setting.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.team.<a href="src/fern/team/client.py">update_wage_setting</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates a `WageSetting` object. The object is created if a
`WageSetting` with the specified `team_member_id` does not exist. Otherwise,
it fully replaces the `WageSetting` object for the team member.
The `WageSetting` is returned on a successful update.
Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#create-or-update-a-wage-setting).
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
from fern import FernApi, WageSetting

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.team.update_wage_setting(
    team_member_id="team_member_id",
    wage_setting=WageSetting(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_member_id:** `str` — The ID of the team member for which to update the `WageSetting` object.
    
</dd>
</dl>

<dl>
<dd>

**wage_setting:** `WageSetting` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Terminal
<details><summary><code>client.terminal.<a href="src/fern/terminal/client.py">create_terminal_checkout</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a Terminal checkout request and sends it to the specified device to take a payment
for the requested amount.
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
from fern import DeviceCheckoutOptions, FernApi, Money, TerminalCheckout

client = FernApi(
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.terminal.create_terminal_checkout(
    checkout=TerminalCheckout(
        amount_money=Money(),
        device_options=DeviceCheckoutOptions(
            device_id="device_id",
        ),
    ),
    idempotency_key="idempotency_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**checkout:** `TerminalCheckout` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this `CreateCheckout` request. Keys can be any valid string but
must be unique for every `CreateCheckout` request.

See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminal.<a href="src/fern/terminal/client.py">search_terminal_checkouts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a filtered list of Terminal checkout requests created by the account making the request.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.terminal.search_terminal_checkouts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.
See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits the number of results returned for a single request.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[TerminalCheckoutQuery]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminal.<a href="src/fern/terminal/client.py">get_terminal_checkout</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a Terminal checkout request by `checkout_id`.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.terminal.get_terminal_checkout(
    checkout_id="checkout_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**checkout_id:** `str` — The unique ID for the desired `TerminalCheckout`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminal.<a href="src/fern/terminal/client.py">cancel_terminal_checkout</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels a Terminal checkout request if the status of the request permits it.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.terminal.cancel_terminal_checkout(
    checkout_id="checkout_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**checkout_id:** `str` — The unique ID for the desired `TerminalCheckout`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminal.<a href="src/fern/terminal/client.py">create_terminal_refund</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a request to refund an Interac payment completed on a Square Terminal.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.terminal.create_terminal_refund(
    idempotency_key="idempotency_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this `CreateRefund` request. Keys can be any valid string but
must be unique for every `CreateRefund` request.

See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.
    
</dd>
</dl>

<dl>
<dd>

**refund:** `typing.Optional[TerminalRefund]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminal.<a href="src/fern/terminal/client.py">search_terminal_refunds</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a filtered list of Interac Terminal refund requests created by the seller making the request.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.terminal.search_terminal_refunds()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits the number of results returned for a single request.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[TerminalRefundQuery]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminal.<a href="src/fern/terminal/client.py">get_terminal_refund</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves an Interac Terminal refund object by ID.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.terminal.get_terminal_refund(
    terminal_refund_id="terminal_refund_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**terminal_refund_id:** `str` — The unique ID for the desired `TerminalRefund`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminal.<a href="src/fern/terminal/client.py">cancel_terminal_refund</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels an Interac Terminal refund request by refund request ID if the status of the request permits it.
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
    authorization="YOUR_AUTHORIZATION",
    token="YOUR_TOKEN",
)
client.terminal.cancel_terminal_refund(
    terminal_refund_id="terminal_refund_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**terminal_refund_id:** `str` — The unique ID for the desired `TerminalRefund`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

