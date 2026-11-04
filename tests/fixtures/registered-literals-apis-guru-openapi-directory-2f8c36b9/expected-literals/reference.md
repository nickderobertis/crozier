# Reference
## Accounts
<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">request_password_reset</a>(...) -> SimpleMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requesting a reset for a new password. 
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.request_password_reset(
    username="username",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">verify_password_reset</a>(...) -> SimpleMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Setting a new password and verifying the request to set the password.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.verify_password_reset(
    password="password",
    token="token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">register_user</a>(...) -> UserRegistrationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Registering a new user.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.register_user(
    email="email",
    password="password",
    username="username",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">complete_registration</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Completing a registration e.g. for invited users. Finish registration with a username and a password.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.complete_registration(
    password="password",
    username="username",
    verification_token="verificationToken",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**verification_token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">verify_user_registration</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verifies a new user registration.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.verify_user_registration(
    token="token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">get_all_organization_roles</a>(...) -> PaginatedResponseOfUserRoles</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Listing users and their roles in a paginated manner.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.get_all_organization_roles(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">get_users_of_organization</a>(...) -> PaginatedResponseOfUserPresentation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Finding users in the specified organization in a paginated manner.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.get_users_of_organization(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">invite_users</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, OrganizationUserInvitation
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.invite_users(
    organization_id="organizationId",
    invitations=[
        OrganizationUserInvitation(
            roles=[
                "roles"
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

**organization_id:** `str` — The namespace of the organization where users should be invited
    
</dd>
</dl>

<dl>
<dd>

**invitations:** `typing.List[OrganizationUserInvitation]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">get_user_roles</a>(...) -> PaginatedResponseOfstring</code></summary>
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

client.accounts.get_user_roles(
    organization_id="organizationId",
    username="username",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — The namespace of the organization
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` — username
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">add_user_roles</a>(...)</code></summary>
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

client.accounts.add_user_roles(
    organization_id="organizationId",
    username="username",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — The namespace of the organization
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` — username
    
</dd>
</dl>

<dl>
<dd>

**request:** `ChangeRoleRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">remove_user_roles</a>(...)</code></summary>
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

client.accounts.remove_user_roles(
    organization_id="organizationId",
    username="username",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — The namespace of the organization
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` — username
    
</dd>
</dl>

<dl>
<dd>

**request:** `ChangeRoleRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">list_all_roles</a>(...) -> PaginatedResponseOfRole</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Listing of roles.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.list_all_roles()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**privilege:** `typing.Optional[str]` — If specified the roles will be filtered containing that privilege.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">get_organizations_of_user</a>(...) -> PaginatedResponseOfOrganization</code></summary>
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

client.accounts.get_organizations_of_user()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**role:** `typing.Optional[str]` — role
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">find_users</a>(...) -> PaginatedResponseOfUserPresentation</code></summary>
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

client.accounts.find_users()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username_prefix:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">find_user_by_username</a>(...) -> UserPresentation</code></summary>
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

client.accounts.find_user_by_username(
    username="username",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `str` — username
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/fern/accounts/client.py">login</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

ID4i API Login
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.accounts.login()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**login:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Api Keys
<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">list_all_api_keys_of_organization</a>(...) -> PaginatedResponseOfApiKeyPresentation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Finding all API key assigned to the specified organization in a paginated manner.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.list_all_api_keys_of_organization()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — The namespace of the organization to search in.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">create_new_api_key</a>(...) -> ApiKeyPresentation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creation of a new API key.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.create_new_api_key(
    label="label",
    organization_id="de.acme",
    secret="secret",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**label:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">list_all_api_key_privileges</a>(...) -> PaginatedResponseOfApiKeyPrivilegeInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Listing all possible API key privileges.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.list_all_api_key_privileges()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n_concerning:** `typing.Optional[bool]` — id4nConcerning
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">get_api_key</a>(...) -> ApiKeyPresentation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Showing the details of an API key.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.get_api_key(
    key="key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — The API key to show.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">update_api_key</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

API keys can be updated with new labels, and be activated and deactivated. The secret or UUID cannot be changed.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.update_api_key(
    key="key",
    new_label="newLabel",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — The API key to be updated.
    
</dd>
</dl>

<dl>
<dd>

**new_label:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">delete_api_key</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletion of an API key.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.delete_api_key(
    key="key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — The API key to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">list_api_key_privileges</a>(...) -> PaginatedResponseOfApiKeyPrivilege</code></summary>
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

client.api_keys.list_api_key_privileges(
    key="key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — key
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">add_api_key_privilege</a>(...)</code></summary>
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

client.api_keys.add_api_key_privilege(
    key="key",
    privilege="privilege",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — key
    
</dd>
</dl>

<dl>
<dd>

**privilege:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">remove_api_key_privilege</a>(...)</code></summary>
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

client.api_keys.remove_api_key_privilege(
    key="key",
    privilege="privilege",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — key
    
</dd>
</dl>

<dl>
<dd>

**privilege:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">list_id4ns</a>(...) -> PaginatedResponseOfId4NPresentation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Listing ID4ns of a id4n concerning privilege
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.list_id4ns(
    key="key",
    privilege="privilege",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — key
    
</dd>
</dl>

<dl>
<dd>

**privilege:** `str` — privilege
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">add_api_key_privilege_for_id4ns</a>(...)</code></summary>
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

client.api_keys.add_api_key_privilege_for_id4ns(
    key="key",
    privilege="privilege",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — key
    
</dd>
</dl>

<dl>
<dd>

**privilege:** `str` — privilege
    
</dd>
</dl>

<dl>
<dd>

**request:** `ListOfId4Ns` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">remove_api_key_privilege_for_id4ns</a>(...)</code></summary>
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

client.api_keys.remove_api_key_privilege_for_id4ns(
    key="key",
    privilege="privilege",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — key
    
</dd>
</dl>

<dl>
<dd>

**privilege:** `str` — privilege
    
</dd>
</dl>

<dl>
<dd>

**request:** `ListOfId4Ns` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Billing
<details><summary><code>client.billing.<a href="src/fern/billing/client.py">get_sum_for_organization</a>(...) -> ServiceCosts</code></summary>
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

client.billing.get_sum_for_organization(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — The organization to compute the billing information for
    
</dd>
</dl>

<dl>
<dd>

**from_date:** `typing.Optional[datetime.datetime]` — Billing start date
    
</dd>
</dl>

<dl>
<dd>

**to_date:** `typing.Optional[datetime.datetime]` — Billing end date
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.billing.<a href="src/fern/billing/client.py">get_positions_for_organization</a>(...) -> typing.List[BillingPosition]</code></summary>
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

client.billing.get_positions_for_organization(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — The organization to compute the billing information for
    
</dd>
</dl>

<dl>
<dd>

**from_date:** `typing.Optional[datetime.datetime]` — Billing start date
    
</dd>
</dl>

<dl>
<dd>

**to_date:** `typing.Optional[datetime.datetime]` — Billing end date
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Auditing
<details><summary><code>client.auditing.<a href="src/fern/auditing/client.py">list_organization_change_log</a>(...) -> PaginatedResponseOfChangeLogEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Listing change log entries of the specified organization id.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.auditing.list_organization_change_log(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — The namespace identifying the organization whose change log entries are to be listed
    
</dd>
</dl>

<dl>
<dd>

**message_mime_type:** `typing.Optional[str]` — The Mime-type for the message format that should be returned. e.g. 'text/plain' or 'text/mustache' 
    
</dd>
</dl>

<dl>
<dd>

**from_date:** `typing.Optional[datetime.datetime]` — From date time as UTC Date-Time format
    
</dd>
</dl>

<dl>
<dd>

**to_date:** `typing.Optional[datetime.datetime]` — To date time as UTC Date-Time format
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Collections
<details><summary><code>client.collections.<a href="src/fern/collections/client.py">create_collection</a>(...) -> Id4N</code></summary>
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

client.collections.create_collection(
    length=1,
    organization_id="de.acme",
    type="ROUTING_COLLECTION",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**length:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `CreateCollectionRequestType` 
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">find_collection</a>(...) -> GuidCollection</code></summary>
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

client.collections.find_collection(
    id4n="id4n",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">delete_collection</a>(...)</code></summary>
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

client.collections.delete_collection(
    id4n="id4n",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">update_collection</a>(...) -> typing.Optional[typing.Dict[str, typing.Any]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update collection changing only the given values
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.update_collection(
    id4n_="id4n",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**request:** `GuidCollection` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">list_elements_of_collection</a>(...) -> PaginatedResponseOfGuid</code></summary>
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

client.collections.list_elements_of_collection(
    id4n="id4n",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — The organization namespace.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">add_elements_to_collection</a>(...)</code></summary>
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

client.collections.add_elements_to_collection(
    id4n="id4n",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**request:** `ListOfId4Ns` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">remove_elements_from_collection</a>(...)</code></summary>
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

client.collections.remove_elements_from_collection(
    id4n="id4n",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**request:** `ListOfId4Ns` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">get_properties</a>(...) -> typing.Dict[str, str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all properties of an id4n.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.get_properties(
    id4n="id4n",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — The id4n
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — The organization namespace.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">delete_properties</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partial deletion of id4n properties. If the property does not exist, it will be ignored.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.delete_properties(
    id4n="id4n",
    organization_id="organizationId",
    request=[
        "string"
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

**id4n:** `str` — The id4n
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — The organization namespace to work on while deleting the properties.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">patch_properties</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partial updating of id4n properties. If a property contains a null value the property will be deleted other values will be saved and overwritten if they already exist.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.patch_properties(
    id4n="id4n",
    organization_id="organizationId",
    request={
        "key": "value"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — The id4n
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — The organization namespace to work on while patching the properties.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">get_multiple_properties</a>(...) -> ListOfId4NProperties</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of ID4n properties for the specified ID4ns.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.get_multiple_properties(
    id4ns=[
        "id4ns"
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

**id4ns:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The list of ID4ns to resolve.
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — The organization namespace.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collections.<a href="src/fern/collections/client.py">get_all_collections_of_organization</a>(...) -> PaginatedResponseOfGuidCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieving all collections of an organization in a paginated manner. You may filter the results by specifying id4n properties with filter operations (eq, in, ne) in the query parameters. e.g. `com.yourcompany.orderId.eq=1234`  
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.collections.get_all_collections_of_organization(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — The namespace of the organization
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GetAllCollectionsOfOrganizationRequestType]` — Filter by this type
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — Filter by this label
    
</dd>
</dl>

<dl>
<dd>

**label_prefix:** `typing.Optional[str]` — Filter by this label prefix
    
</dd>
</dl>

<dl>
<dd>

**property:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List of i4dn property filter. e.g. "com.myorga.state:IN:waiting|processing" or "com.myorga.orderId:EQ:SAP001"
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organizations
<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">list_countries</a>(...) -> PaginatedResponseOfCountry</code></summary>
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

client.organizations.list_countries()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">create_organization</a>(...) -> Organization</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creating a new organization.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organizations.create_organization(
    name="ACME Inc.",
    namespace="de.acme",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Organization` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">find_organization</a>(...) -> Organization</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single organization.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organizations.find_organization(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — The namespace of the organization to be retrieved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">update_organization</a>(...) -> Organization</code></summary>
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

client.organizations.update_organization(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — The namespace of the organization to be updated.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">delete_organization</a>(...)</code></summary>
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

client.organizations.delete_organization(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — The namespace of the organization to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">find_organization_billing_address</a>(...) -> OrganizationAddress</code></summary>
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

client.organizations.find_organization_billing_address(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">update_organization_billing_address</a>(...) -> OrganizationAddress</code></summary>
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

client.organizations.update_organization_billing_address(
    organization_id="organizationId",
    city="MyCity",
    country_code="DE",
    firstname="Max",
    lastname="Muster",
    post_code="postCode",
    street="Examplestreet 1",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**request:** `OrganizationAddress` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">delete_organization_billing_address</a>(...)</code></summary>
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

client.organizations.delete_organization_billing_address(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">find_organization_address</a>(...) -> OrganizationAddress</code></summary>
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

client.organizations.find_organization_address(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">update_organization_address</a>(...) -> OrganizationAddress</code></summary>
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

client.organizations.update_organization_address(
    organization_id="organizationId",
    city="MyCity",
    country_code="DE",
    firstname="Max",
    lastname="Muster",
    post_code="postCode",
    street="Examplestreet 1",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**request:** `OrganizationAddress` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">set_organization_logo</a>(...) -> PublicImagePresentation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updating an organization logo using a multipart file upload.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organizations.set_organization_logo(
    organization_id="organizationId",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — The namespace of the organization where the logo should be updated.
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` — An image containing the new logo.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">delete_organization_logo</a>(...)</code></summary>
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

client.organizations.delete_organization_logo(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — The namespace of the organization where the logo should be deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">get_partner_organizations</a>(...) -> PaginatedResponseOfPartnerOrganization</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Listing partners in a paginated manner.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organizations.get_partner_organizations(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — The namespace of the organization to query partner organizations
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">add_partner_organization</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adding a partner organization. If the given organization is already a partner the result will be state 200 too.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organizations.add_partner_organization(
    organization_id_path_param="organizationId",
    organization_id="org.acme",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id_path_param:** `str` — The namespace of the organization
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — The namespace of the partner organization to add
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">remove_partner_organization</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removing a partner organization
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organizations.remove_partner_organization(
    organization_id_path_param="organizationId",
    organization_id="org.acme",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id_path_param:** `str` — The namespace of the organization
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — The namespace of the partner organization to remove
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">get_organization_privileges</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Listing all privileges of the current user/APIKey of the specified organization.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.organizations.get_organization_privileges(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — The namespace of the organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Storage
<details><summary><code>client.storage.<a href="src/fern/storage/client.py">list_all_documents</a>(...) -> PaginatedResponseOfDocument</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Listing all documents of an id4n
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.storage.list_all_documents(
    id4n="id4n",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**owner:** `typing.Optional[str]` — Filter by owner organization
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.storage.<a href="src/fern/storage/client.py">list_documents</a>(...) -> PaginatedResponseOfDocument</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Listing documents of an id4n seen by a specified organization
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.storage.list_documents(
    id4n="id4n",
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**owner:** `typing.Optional[str]` — Filter by owner organization
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.storage.<a href="src/fern/storage/client.py">create_document</a>(...) -> Document</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The documents' mime type is suggested on octet-stream data. Otherwise the specified content mime type is used.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.storage.create_document(
    id4n="id4n",
    organization_id="organizationId",
    content="example_content",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**content:** `core.File` — content
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.storage.<a href="src/fern/storage/client.py">put_document</a>(...) -> Document</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creating or overwriting an existing document 
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.storage.put_document(
    id4n="id4n",
    organization_id="organizationId",
    content="example_content",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**content:** `core.File` — content
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.storage.<a href="src/fern/storage/client.py">read_document</a>(...) -> str</code></summary>
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

client.storage.read_document(
    id4n="id4n",
    organization_id="organizationId",
    file_name="fileName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `str` — fileName
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.storage.<a href="src/fern/storage/client.py">delete_document</a>(...)</code></summary>
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

client.storage.delete_document(
    id4n="id4n",
    organization_id="organizationId",
    file_name="fileName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `str` — fileName
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.storage.<a href="src/fern/storage/client.py">get_document</a>(...) -> Document</code></summary>
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

client.storage.get_document(
    id4n="id4n",
    organization_id="organizationId",
    file_name="fileName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `str` — fileName
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.storage.<a href="src/fern/storage/client.py">update_document_metadata</a>(...) -> typing.Optional[Document]</code></summary>
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

client.storage.update_document_metadata(
    id4n="id4n",
    organization_id="organizationId",
    file_name="fileName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `str` — fileName
    
</dd>
</dl>

<dl>
<dd>

**filename:** `typing.Optional[str]` — File Name
    
</dd>
</dl>

<dl>
<dd>

**mime_type:** `typing.Optional[str]` — Mime Type
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `typing.Optional[VisibilityUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.storage.<a href="src/fern/storage/client.py">read_from_microstorage</a>(...) -> str</code></summary>
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

client.storage.read_from_microstorage(
    id4n="id4n",
    organization="organization",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**organization:** `str` — organization
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.storage.<a href="src/fern/storage/client.py">write_to_microstorage</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
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

client.storage.write_to_microstorage(
    id4n="id4n",
    organization="organization",
    request="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**organization:** `str` — organization
    
</dd>
</dl>

<dl>
<dd>

**request:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Guids
<details><summary><code>client.guids.<a href="src/fern/guids/client.py">create_guid</a>(...) -> ListOfId4Ns</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creating one or more GUIDs with a specified length.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.guids.create_guid(
    count=1,
    length=40,
    organization_id="de.acme",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**count:** `int` — The total number of GUIDs to create
    
</dd>
</dl>

<dl>
<dd>

**length:** `int` — The charactersequence length of the GUID
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — The namespace of the organization where the generated GUIDs should be assigned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guids.<a href="src/fern/guids/client.py">get_guids_without_collection</a>(...) -> PaginatedResponseOfGuid</code></summary>
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

client.guids.get_guids_without_collection(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — The namespace of the organization to search GUIDs for
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guids.<a href="src/fern/guids/client.py">get_guid</a>(...) -> Guid</code></summary>
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

client.guids.get_guid(
    id4n="id4n",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — The GUID number
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — The organization namespace to resolve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guids.<a href="src/fern/guids/client.py">update_guid</a>(...) -> typing.Optional[typing.Dict[str, typing.Any]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allows ownership transfer.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.guids.update_guid(
    id4n_="id4n",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — The GUID number
    
</dd>
</dl>

<dl>
<dd>

**request:** `Guid` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guids.<a href="src/fern/guids/client.py">get_id4n</a>(...) -> Id4NPresentation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieving basic information about an ID like the type and the creation time.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.guids.get_id4n(
    id4n="id4n",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — The ID to resolve to
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — The organization namespace to resolve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guids.<a href="src/fern/guids/client.py">get_collections</a>(...) -> PaginatedResponseOfGuidCollection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieving all owned or holding collections the specified id4n is assigned to.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.guids.get_collections(
    id4n="id4n",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — The ID which the collections should contain
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — The organization holding the collections.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.guids.<a href="src/fern/guids/client.py">import_gs1codes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Importing GS1/MAPP codes that contain unique components.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ListOfGs1S
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.guids.import_gs1codes(
    list_of_gs1s=ListOfGs1S(),
    organization_id="de.acme",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_of_gs1s:** `ListOfGs1S` 
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — The organization where the GS1/Mapp code is imported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## History
<details><summary><code>client.history.<a href="src/fern/history/client.py">filtered_list</a>(...) -> PaginatedResponseOfHistoryItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the history of a GUID
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.history.filtered_list(
    id4n="id4n",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — GUID to retrieve the history for
    
</dd>
</dl>

<dl>
<dd>

**include_private:** `typing.Optional[bool]` — Also return private history entries
    
</dd>
</dl>

<dl>
<dd>

**organization:** `typing.Optional[str]` — Show only entries created by one of the given organizations. This parameter can be used multiple times.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[FilteredListRequestTypeItem, typing.Sequence[FilteredListRequestTypeItem]]]` — Show only entries matching one of the given history item types. This parameter can be used multiple times.
    
</dd>
</dl>

<dl>
<dd>

**qualifier:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Show only entries matching one of the given history item qualifiers (additional property de.id4i.history.item.qualifier). This parameter can be used multiple times.
    
</dd>
</dl>

<dl>
<dd>

**from_date:** `typing.Optional[datetime.datetime]` — From date time as UTC Date-Time format
    
</dd>
</dl>

<dl>
<dd>

**to_date:** `typing.Optional[datetime.datetime]` — To date time as UTC Date-Time format
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.history.<a href="src/fern/history/client.py">add_item</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new history item
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.history.add_item(
    id4n="id4n",
    organization_id="org.acme",
    type="CREATED",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — GUID to retrieve the history for
    
</dd>
</dl>

<dl>
<dd>

**request:** `HistoryItem` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.history.<a href="src/fern/history/client.py">list</a>(...) -> PaginatedResponseOfHistoryItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

DEPRECATED - please use filteredList with organization parameter to achieve the same functionality
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.history.list(
    id4n="id4n",
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — GUID to retrieve the history for
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**include_private:** `typing.Optional[bool]` — Also return private history entries
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.history.<a href="src/fern/history/client.py">retrieve_item</a>(...) -> HistoryItem</code></summary>
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

client.history.retrieve_item(
    id4n="id4n",
    organization_id="organizationId",
    sequence_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — GUID to retrieve the history for
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**sequence_id:** `int` — sequenceId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.history.<a href="src/fern/history/client.py">update_item</a>(...) -> typing.Optional[HistoryItem]</code></summary>
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

client.history.update_item(
    id4n="id4n",
    organization_id_path_param="organizationId",
    sequence_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — GUID to retrieve the history for
    
</dd>
</dl>

<dl>
<dd>

**organization_id_path_param:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**sequence_id:** `int` — sequenceId
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — New organization id displayed for this item. If given, must match the holder of GUID and the organization the history item is found under.
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `typing.Optional[Visibility]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.history.<a href="src/fern/history/client.py">update_item_visibility</a>(...) -> HistoryItem</code></summary>
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

client.history.update_item_visibility(
    id4n="id4n",
    organization_id="organizationId",
    sequence_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — GUID to retrieve the history for
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**sequence_id:** `int` — sequenceId
    
</dd>
</dl>

<dl>
<dd>

**request:** `Visibility` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Alias
<details><summary><code>client.alias.<a href="src/fern/alias/client.py">get_guid_aliases</a>(...) -> typing.Dict[str, str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Looks up the alias for each alias type (group and single) and returns a map of all aliases found.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.alias.get_guid_aliases(
    id4n="id4n",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — The GUID or Collection to operate on
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.alias.<a href="src/fern/alias/client.py">add_guid_alias</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds or replaces aliases for single ID4ns (alias type item and mapp) or groups of ID4ns (alias types gtin, ean and article)
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.alias.add_guid_alias(
    id4n="id4n",
    alias_type="gtin",
    alias="alias",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — The GUID or Collection to operate on
    
</dd>
</dl>

<dl>
<dd>

**alias_type:** `AddGuidAliasRequestAliasType` — Alias type, see the corresponding API model
    
</dd>
</dl>

<dl>
<dd>

**alias:** `str` — An alias
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.alias.<a href="src/fern/alias/client.py">remove_guid_alias</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove the alias of the given type
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.alias.remove_guid_alias(
    id4n="id4n",
    alias_type="gtin",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — The GUID or Collection to operate on
    
</dd>
</dl>

<dl>
<dd>

**alias_type:** `RemoveGuidAliasRequestAliasType` — Alias type, see the corresponding API model
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.alias.<a href="src/fern/alias/client.py">search_by_alias</a>(...) -> PaginatedResponseOfGuid</code></summary>
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

client.alias.search_by_alias(
    alias="alias",
    alias_type="gtin",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**alias:** `str` — The alias to search for
    
</dd>
</dl>

<dl>
<dd>

**alias_type:** `SearchByAliasRequestAliasType` — Alias type type to search for
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.alias.<a href="src/fern/alias/client.py">get_guid_alias_types</a>() -> typing.List[GetGuidAliasTypesResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve this list to find out all alias types to use with alias search and change operations
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.alias.get_guid_alias_types()

```
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

## Meta Information
<details><summary><code>client.meta_information.<a href="src/fern/meta_information/client.py">application_info</a>() -> AppInfoPresentation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieving version information about ID4i.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.meta_information.application_info()

```
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

## Messaging
<details><summary><code>client.messaging.<a href="src/fern/messaging/client.py">get_default_queue</a>(...) -> QueuePresentation</code></summary>
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

client.messaging.get_default_queue(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messaging.<a href="src/fern/messaging/client.py">patch_default_queue</a>(...)</code></summary>
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

client.messaging.patch_default_queue(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — If this value is set to false the queue will be deleted.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**purge_queue:** `typing.Optional[bool]` — Set this value to true if you want to purge the queue.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messaging.<a href="src/fern/messaging/client.py">enqueue_custom_message</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enqueue a custom organisation message with custom data.
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.messaging.enqueue_custom_message(
    organization_id="organizationId",
    data={
        "key": "value"
    },
    name="<event name>",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — The organisation namespace
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Dict[str, str]` — Custom data in a map. You may use JSON content
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the message (organisation specific)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Public Services
<details><summary><code>client.public_services.<a href="src/fern/public_services/client.py">list_all_public_documents</a>(...) -> PaginatedResponseOfDocument</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Listing all public documents of an id4n
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_services.list_all_public_documents(
    id4n="id4n",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**owner:** `typing.Optional[str]` — Filter by owner organization
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.public_services.<a href="src/fern/public_services/client.py">read_public_document</a>(...) -> str</code></summary>
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

client.public_services.read_public_document(
    id4n="id4n",
    organization_id="organizationId",
    file_name="fileName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `str` — fileName
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.public_services.<a href="src/fern/public_services/client.py">get_public_document</a>(...) -> Document</code></summary>
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

client.public_services.get_public_document(
    id4n="id4n",
    organization_id="organizationId",
    file_name="fileName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `str` — fileName
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.public_services.<a href="src/fern/public_services/client.py">list_public_history</a>(...) -> PaginatedResponseOfHistoryItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Only contains public history items
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_services.list_public_history(
    id4n="id4n",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — GUID to retrieve the history for
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Start with the n-th element
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum count of returned elements
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.public_services.<a href="src/fern/public_services/client.py">read_organization_info</a>(...) -> Organization</code></summary>
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

client.public_services.read_organization_info(
    organization_id="organizationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `str` — Organization ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.public_services.<a href="src/fern/public_services/client.py">get_routes</a>(...) -> typing.List[Route]</code></summary>
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

client.public_services.get_routes(
    id4n="id4n",
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

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — type
    
</dd>
</dl>

<dl>
<dd>

**interpolate:** `typing.Optional[bool]` — interpolate
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.public_services.<a href="src/fern/public_services/client.py">go</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Forwarding to the designated route defined in the routing,
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_services.go(
    guid="guid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**guid:** `str` — guid
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.public_services.<a href="src/fern/public_services/client.py">resolve_who_is_entry</a>(...) -> WhoIsResponse</code></summary>
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

client.public_services.resolve_who_is_entry(
    id4n="id4n",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Images
<details><summary><code>client.images.<a href="src/fern/images/client.py">resolve_image_using_get</a>(...) -> str</code></summary>
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

client.images.resolve_image_using_get(
    image_id="imageID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_id:** `str` — The id of the image to be resolved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Routing
<details><summary><code>client.routing.<a href="src/fern/routing/client.py">get_routing_file</a>(...) -> RoutingFile</code></summary>
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

client.routing.get_routing_file(
    id4n="id4n",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.routing.<a href="src/fern/routing/client.py">update_routing_file</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, RoutingFile, Route
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.routing.update_routing_file(
    id4n="id4n",
    routing=RoutingFile(
        routes=[
            Route(
                params={
                    "key": "value"
                },
                public=True,
                type="type",
            )
        ],
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

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**routing:** `RoutingFile` 
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.routing.<a href="src/fern/routing/client.py">get_route</a>(...) -> Route</code></summary>
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

client.routing.get_route(
    id4n="id4n",
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

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The type of route you want to have
    
</dd>
</dl>

<dl>
<dd>

**private_routes:** `typing.Optional[bool]` — privateRoutes
    
</dd>
</dl>

<dl>
<dd>

**public_routes:** `typing.Optional[bool]` — publicRoutes
    
</dd>
</dl>

<dl>
<dd>

**interpolate:** `typing.Optional[bool]` — interpolate
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.routing.<a href="src/fern/routing/client.py">get_all_routes</a>(...) -> typing.List[Route]</code></summary>
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

client.routing.get_all_routes(
    id4n="id4n",
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

**id4n:** `str` — id4n
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The type of route you want to have
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — organizationId
    
</dd>
</dl>

<dl>
<dd>

**interpolate:** `typing.Optional[bool]` — interpolate
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Transfer
<details><summary><code>client.transfer.<a href="src/fern/transfer/client.py">receive</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Taking ownership can be forbidden by a previous owner. See methods prepare and getInfo
</dd>
</dl>
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.transfer.receive(
    id4n="id4n",
    organization_id="de.id4i",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — This ID4N identifies the object to take hold of
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — Organization to take the ownership of the ID. If the sender chose to keep the ownership, this organization becomes the holder. Otherwise, it becomes the new owner.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transfer.<a href="src/fern/transfer/client.py">get_send_info</a>(...) -> TransferSendInfo</code></summary>
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

client.transfer.get_send_info(
    id4n="id4n",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id4n:** `str` — The ID4N to retrieve information about
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transfer.<a href="src/fern/transfer/client.py">prepare</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
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

client.transfer.prepare(
    id4n="id4n",
    keep_ownership=True,
    open_for_claims=False,
    recipient_organization_ids=[
        "de.acme",
        "com.porsche",
        "de.bluerain"
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

**id4n:** `str` — The ID4N to prepare for transfer
    
</dd>
</dl>

<dl>
<dd>

**request:** `TransferSendInfo` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

