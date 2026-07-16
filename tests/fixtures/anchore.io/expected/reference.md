# Reference
<details><summary><code>client.<a href="src/fern/client.py">ping</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Simple status check
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.ping()

```
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

<details><summary><code>client.<a href="src/fern/client.py">health_check</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Health check, returns 200 and no body if service is running
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.health_check()

```
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

<details><summary><code>client.<a href="src/fern/client.py">list_file_content_search_results</a>(...) -> FileContentSearchList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.list_file_content_search_results(
    image_digest="imageDigest",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_digest:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">list_retrieved_files</a>(...) -> RetrievedFileList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.list_retrieved_files(
    image_digest="imageDigest",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_digest:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">list_secret_search_results</a>(...) -> SecretSearchList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.list_secret_search_results(
    image_digest="imageDigest",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_digest:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_oauth_token</a>(...) -> TokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Request a jwt token for subsequent operations, this request is authenticated with normal HTTP auth
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.get_oauth_token()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — The type of client used for the OAuth token
    
</dd>
</dl>

<dl>
<dd>

**grant_type:** `typing.Optional[str]` — OAuth Grant type for token
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Password for corresponding user
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — User to assign OAuth token to
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">version_check</a>() -> ServiceVersion</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the version object for the service, including db schema version info
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.version_check()

```
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

## Identity
<details><summary><code>client.identity.<a href="src/fern/identity/client.py">get_users_account</a>() -> Account</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.identity.get_users_account()

```
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

<details><summary><code>client.identity.<a href="src/fern/identity/client.py">get_user</a>() -> User</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.identity.get_user()

```
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

<details><summary><code>client.identity.<a href="src/fern/identity/client.py">get_credentials</a>() -> CredentialList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.identity.get_credentials()

```
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

<details><summary><code>client.identity.<a href="src/fern/identity/client.py">add_credential</a>(...) -> User</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AccessCredentialType
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.identity.add_credential(
    type=AccessCredentialType.PASSWORD,
    value="value",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `AccessCredential` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## User Management
<details><summary><code>client.user_management.<a href="src/fern/user_management/client.py">list_accounts</a>(...) -> AccountList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.user_management.list_accounts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**state:** `typing.Optional[ListAccountsRequestState]` — Filter accounts by state
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_management.<a href="src/fern/user_management/client.py">create_account</a>(...) -> Account</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.user_management.create_account(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The account name to use. This will identify the account and must be globally unique in the system.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — An optional email to associate with the account for contact purposes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_management.<a href="src/fern/user_management/client.py">get_account</a>(...) -> Account</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.user_management.get_account(
    accountname="accountname",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**accountname:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_management.<a href="src/fern/user_management/client.py">delete_account</a>(...)</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.user_management.delete_account(
    accountname="accountname",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**accountname:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_management.<a href="src/fern/user_management/client.py">update_account_state</a>(...) -> AccountStatus</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.user_management.update_account_state(
    accountname="accountname",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**accountname:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `AccountStatus` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_management.<a href="src/fern/user_management/client.py">list_users</a>(...) -> typing.List[User]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.user_management.list_users(
    accountname="accountname",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**accountname:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_management.<a href="src/fern/user_management/client.py">create_user</a>(...) -> User</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.user_management.create_user(
    accountname="accountname",
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

**accountname:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — The initial password for the user, must be at least 6 characters, up to 128
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` — The username to create
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_management.<a href="src/fern/user_management/client.py">get_account_user</a>(...) -> User</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.user_management.get_account_user(
    accountname="accountname",
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

**accountname:** `str` 
    
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

<details><summary><code>client.user_management.<a href="src/fern/user_management/client.py">delete_user</a>(...)</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.user_management.delete_user(
    accountname="accountname",
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

**accountname:** `str` 
    
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

<details><summary><code>client.user_management.<a href="src/fern/user_management/client.py">list_user_credentials</a>(...) -> CredentialList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.user_management.list_user_credentials(
    accountname="accountname",
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

**accountname:** `str` 
    
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

<details><summary><code>client.user_management.<a href="src/fern/user_management/client.py">create_user_credential</a>(...) -> User</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AccessCredentialType
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.user_management.create_user_credential(
    accountname="accountname",
    username="username",
    type=AccessCredentialType.PASSWORD,
    value="value",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**accountname:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `AccessCredential` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_management.<a href="src/fern/user_management/client.py">delete_user_credential</a>(...)</code></summary>
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
from fern.user_management import DeleteUserCredentialRequestCredentialType

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.user_management.delete_user_credential(
    accountname="accountname",
    username="username",
    credential_type=DeleteUserCredentialRequestCredentialType.PASSWORD,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**accountname:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**credential_type:** `DeleteUserCredentialRequestCredentialType` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Archives
<details><summary><code>client.archives.<a href="src/fern/archives/client.py">list_archives</a>() -> ArchiveSummary</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.archives.list_archives()

```
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

<details><summary><code>client.archives.<a href="src/fern/archives/client.py">list_analysis_archive</a>() -> ArchivedAnalyses</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.archives.list_analysis_archive()

```
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

<details><summary><code>client.archives.<a href="src/fern/archives/client.py">archive_image_analysis</a>(...) -> AddAnalysisArchiveResult</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.archives.archive_image_analysis(
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

**request:** `ImageAnalysisReferences` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.archives.<a href="src/fern/archives/client.py">get_archived_analysis</a>(...) -> ArchivedAnalysis</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the archive metadata record identifying the image and tags for the analysis in the archive.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.archives.get_archived_analysis(
    image_digest="imageDigest",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_digest:** `str` — The image digest to identify the image analysis
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.archives.<a href="src/fern/archives/client.py">delete_archived_analysis</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Performs a synchronous archive deletion
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.archives.delete_archived_analysis(
    image_digest="imageDigest",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_digest:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**force:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.archives.<a href="src/fern/archives/client.py">list_analysis_archive_rules</a>(...) -> AnalysisArchiveRules</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.archives.list_analysis_archive_rules()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**system_global:** `typing.Optional[bool]` — If true include system global rules (owned by admin) even for non-admin users. Defaults to true if not set. Can be set to false to exclude globals
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.archives.<a href="src/fern/archives/client.py">create_analysis_archive_rule</a>(...) -> AnalysisArchiveTransitionRule</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AnalysisArchiveTransitionRuleTransition
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.archives.create_analysis_archive_rule(
    transition=AnalysisArchiveTransitionRuleTransition.ARCHIVE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `AnalysisArchiveTransitionRule` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.archives.<a href="src/fern/archives/client.py">get_analysis_archive_rule</a>(...) -> AnalysisArchiveTransitionRule</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.archives.get_analysis_archive_rule(
    rule_id="ruleId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rule_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.archives.<a href="src/fern/archives/client.py">delete_analysis_archive_rule</a>(...)</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.archives.delete_analysis_archive_rule(
    rule_id="ruleId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rule_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Events
<details><summary><code>client.events.<a href="src/fern/events/client.py">list_event_types</a>() -> EventTypesList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns list of event types in the category hierarchy
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.events.list_event_types()

```
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

<details><summary><code>client.events.<a href="src/fern/events/client.py">list_events</a>(...) -> EventsList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of events in the descending order of their occurrence. Optional query parameters may be used for filtering results
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.events.list_events()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_servicename:** `typing.Optional[str]` — Filter events by the originating service
    
</dd>
</dl>

<dl>
<dd>

**source_hostid:** `typing.Optional[str]` — Filter events by the originating host ID
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `typing.Optional[str]` — Filter events by a prefix match on the event type (e.g. "user.image.")
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `typing.Optional[str]` — Filter events by the type of resource - tag, imageDigest, repository etc
    
</dd>
</dl>

<dl>
<dd>

**resource_id:** `typing.Optional[str]` — Filter events by the id of the resource
    
</dd>
</dl>

<dl>
<dd>

**level:** `typing.Optional[str]` — Filter events by the level - INFO or ERROR
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[str]` — Return events that occurred after the timestamp
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Return events that occurred before the timestamp
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Pagination controls - return the nth page of results. Defaults to first page if left empty
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of events in the result set. Defaults to 100 if left empty
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/fern/events/client.py">delete_events</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete all or a subset of events filtered using the optional query parameters
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.events.delete_events()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**before:** `typing.Optional[str]` — Delete events that occurred before the timestamp
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[str]` — Delete events that occurred after the timestamp
    
</dd>
</dl>

<dl>
<dd>

**level:** `typing.Optional[str]` — Delete events that match the level - INFO or ERROR
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/fern/events/client.py">get_event</a>(...) -> EventResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lookup an event by its event ID
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.events.get_event(
    event_id="eventId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event_id:** `str` — Event ID of the event for lookup
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/fern/events/client.py">delete_event</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an event by its event ID
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.events.delete_event(
    event_id="eventId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event_id:** `str` — Event ID of the event to be deleted
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.images.<a href="src/fern/images/client.py">list_images</a>(...) -> AnchoreImageList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all images visible to the user
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.list_images()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**history:** `typing.Optional[bool]` — Include image history in the response
    
</dd>
</dl>

<dl>
<dd>

**fulltag:** `typing.Optional[str]` — Full docker-pull string to filter results by (e.g. docker.io/library/nginx:latest, or myhost.com:5000/testimages:v1.1.1)
    
</dd>
</dl>

<dl>
<dd>

**image_status:** `typing.Optional[ListImagesRequestImageStatus]` — Filter by image_status value on the record. Default if omitted is 'active'.
    
</dd>
</dl>

<dl>
<dd>

**analysis_status:** `typing.Optional[ListImagesRequestAnalysisStatus]` — Filter by analysis_status value on the record.
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">add_image</a>(...) -> AnchoreImageList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new analysis task that is executed asynchronously
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.add_image()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**force:** `typing.Optional[bool]` — Override any existing entry in the system
    
</dd>
</dl>

<dl>
<dd>

**autosubscribe:** `typing.Optional[bool]` — Instruct engine to automatically begin watching the added tag for updates from registry
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**annotations:** `typing.Optional[typing.Dict[str, typing.Any]]` — Annotations to be associated with the added image in key/value form
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[datetime.datetime]` — Optional override of the image creation time, only honored when both tag and digest are also supplied  e.g. 2018-10-17T18:14:00Z. Deprecated in favor of the 'source' field
    
</dd>
</dl>

<dl>
<dd>

**digest:** `typing.Optional[str]` — A digest string for an image, maybe a pull string or just a digest. e.g. nginx@sha256:123 or sha256:abc123. If a pull string, it must have same regisry/repo as the tag field. Deprecated in favor of the 'source' field
    
</dd>
</dl>

<dl>
<dd>

**dockerfile:** `typing.Optional[str]` — Base64 encoded content of the dockerfile for the image, if available. Deprecated in favor of the 'source' field.
    
</dd>
</dl>

<dl>
<dd>

**image_type:** `typing.Optional[str]` — Optional. The type of image this is adding, defaults to "docker". This can be ommitted until multiple image types are supported.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[ImageSource]` 
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — Full pullable tag reference for image. e.g. docker.io/nginx:latest. Deprecated in favor of the 'source' field
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">delete_images_async</a>(...) -> DeleteImageResponseList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete analysis for image digests in the list asynchronously
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.delete_images_async(
    image_digests=[
        "imageDigests"
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

**image_digests:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**force:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image_by_image_id</a>(...) -> AnchoreImageList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.get_image_by_image_id(
    image_id="imageId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">delete_image_by_image_id</a>(...) -> DeleteImageResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.delete_image_by_image_id(
    image_id="imageId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**force:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image_policy_check_by_image_id</a>(...) -> PolicyEvaluationList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the policy evaluation for the given image
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.get_image_policy_check_by_image_id(
    image_id="imageId",
    tag="tag",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tag:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**policy_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**detail:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**history:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">list_image_content_by_imageid</a>(...) -> typing.List[str]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.list_image_content_by_imageid(
    image_id="imageId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image_content_by_type_image_id_files</a>(...) -> ContentFilesResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.get_image_content_by_type_image_id_files(
    image_id="imageId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image_content_by_type_image_id_javapackage</a>(...) -> ContentJavaPackageResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.get_image_content_by_type_image_id_javapackage(
    image_id="imageId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image_content_by_type_image_id</a>(...) -> ContentPackageResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.get_image_content_by_type_image_id(
    image_id="imageId",
    ctype="ctype",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**ctype:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image_vulnerability_types_by_image_id</a>(...) -> typing.List[GetImageVulnerabilityTypesByImageIdResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.get_image_vulnerability_types_by_image_id(
    image_id="imageId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image_vulnerabilities_by_type_image_id</a>(...) -> VulnerabilityResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.get_image_vulnerabilities_by_type_image_id(
    image_id="imageId",
    vtype="vtype",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**vtype:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image</a>(...) -> AnchoreImageList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.get_image(
    image_digest="imageDigest",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_digest:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">delete_image</a>(...) -> DeleteImageResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.delete_image(
    image_digest="imageDigest",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_digest:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**force:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image_policy_check</a>(...) -> PolicyEvaluationList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the policy evaluation for the given image
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.get_image_policy_check(
    image_digest="imageDigest",
    tag="tag",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_digest:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tag:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**policy_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**detail:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**history:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**interactive:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">list_image_content</a>(...) -> typing.List[str]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.list_image_content(
    image_digest="imageDigest",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_digest:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image_content_by_type_files</a>(...) -> ContentFilesResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.get_image_content_by_type_files(
    image_digest="imageDigest",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_digest:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image_content_by_type_javapackage</a>(...) -> ContentJavaPackageResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.get_image_content_by_type_javapackage(
    image_digest="imageDigest",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_digest:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image_content_by_type_malware</a>(...) -> ContentMalwareResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.get_image_content_by_type_malware(
    image_digest="imageDigest",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_digest:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image_content_by_type</a>(...) -> ContentPackageResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.get_image_content_by_type(
    image_digest="imageDigest",
    ctype="ctype",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_digest:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**ctype:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">list_image_metadata</a>(...) -> typing.List[str]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.list_image_metadata(
    image_digest="imageDigest",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_digest:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image_metadata_by_type</a>(...) -> MetadataResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.get_image_metadata_by_type(
    image_digest="imageDigest",
    mtype="mtype",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_digest:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**mtype:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image_sbom_native</a>(...) -> typing.Iterator[bytes]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.get_image_sbom_native(
    image_digest="imageDigest",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_digest:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image_vulnerability_types</a>(...) -> typing.List[GetImageVulnerabilityTypesResponseItem]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.get_image_vulnerability_types(
    image_digest="imageDigest",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_digest:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.images.<a href="src/fern/images/client.py">get_image_vulnerabilities_by_type</a>(...) -> VulnerabilityResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.images.get_image_vulnerabilities_by_type(
    image_digest="imageDigest",
    vtype="vtype",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_digest:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**vtype:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**force_refresh:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**vendor_only:** `typing.Optional[bool]` — Filter results to include only vulnerabilities that are not marked as invalid by upstream OS vendor data. When set to true, it will filter out all vulnerabilities where `will_not_fix` is False. If false all vulnerabilities are returned regardless of `will_not_fix`
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Import
<details><summary><code>client.import_.<a href="src/fern/import_/client.py">image_archive</a>(...) -> AnchoreImageList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.import_.image_archive(
    archive_file="example_archive_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**archive_file:** `core.File` — anchore image tar archive.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Imports
<details><summary><code>client.imports.<a href="src/fern/imports/client.py">list_operations</a>() -> ImageImports</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.imports.list_operations()

```
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

<details><summary><code>client.imports.<a href="src/fern/imports/client.py">create_operation</a>() -> ImageImportOperation</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.imports.create_operation()

```
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

<details><summary><code>client.imports.<a href="src/fern/imports/client.py">get_operation</a>(...) -> ImageImportOperation</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.imports.get_operation(
    operation_id="operation_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**operation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.imports.<a href="src/fern/imports/client.py">invalidate_operation</a>(...) -> ImageImportOperation</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.imports.invalidate_operation(
    operation_id="operation_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**operation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.imports.<a href="src/fern/imports/client.py">list_import_dockerfiles</a>(...) -> ImportContentDigestList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.imports.list_import_dockerfiles(
    operation_id="operation_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**operation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.imports.<a href="src/fern/imports/client.py">import_image_dockerfile</a>(...) -> ImageImportContentResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.imports.import_image_dockerfile(
    operation_id="operation_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**operation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.imports.<a href="src/fern/imports/client.py">list_import_image_configs</a>(...) -> ImportContentDigestList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.imports.list_import_image_configs(
    operation_id="operation_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**operation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.imports.<a href="src/fern/imports/client.py">import_image_config</a>(...) -> ImageImportContentResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.imports.import_image_config(
    operation_id="operation_id",
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

**operation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.imports.<a href="src/fern/imports/client.py">list_import_image_manifests</a>(...) -> ImportContentDigestList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.imports.list_import_image_manifests(
    operation_id="operation_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**operation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.imports.<a href="src/fern/imports/client.py">import_image_manifest</a>(...) -> ImageImportContentResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.imports.import_image_manifest(
    operation_id="operation_id",
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

**operation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.imports.<a href="src/fern/imports/client.py">list_import_packages</a>(...) -> ImportContentDigestList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.imports.list_import_packages(
    operation_id="operation_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**operation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.imports.<a href="src/fern/imports/client.py">import_image_packages</a>(...) -> ImageImportContentResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ImportPackage, ImportPackageLocation, ImportDistribution, ImportSource
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.imports.import_image_packages(
    operation_id="operation_id",
    artifacts=[
        ImportPackage(
            cpes=[
                "cpes"
            ],
            language="language",
            licenses=[
                "licenses"
            ],
            locations=[
                ImportPackageLocation(
                    path="path",
                )
            ],
            metadata_type="metadataType",
            name="name",
            type="type",
            version="version",
        )
    ],
    distro=ImportDistribution(
        id_like="idLike",
        name="name",
        version="version",
    ),
    source=ImportSource(
        target={
            "key": "value"
        },
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

**operation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**artifacts:** `typing.List[ImportPackage]` 
    
</dd>
</dl>

<dl>
<dd>

**distro:** `ImportDistribution` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `ImportSource` 
    
</dd>
</dl>

<dl>
<dd>

**artifact_relationships:** `typing.Optional[typing.List[ImportPackageRelationship]]` 
    
</dd>
</dl>

<dl>
<dd>

**descriptor:** `typing.Optional[ImportDescriptor]` 
    
</dd>
</dl>

<dl>
<dd>

**schema:** `typing.Optional[ImportSchema]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.imports.<a href="src/fern/imports/client.py">list_import_parent_manifests</a>(...) -> ImportContentDigestList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.imports.list_import_parent_manifests(
    operation_id="operation_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**operation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.imports.<a href="src/fern/imports/client.py">import_image_parent_manifest</a>(...) -> ImageImportContentResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.imports.import_image_parent_manifest(
    operation_id="operation_id",
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

**operation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Policies
<details><summary><code>client.policies.<a href="src/fern/policies/client.py">list_policies</a>(...) -> PolicyBundleList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all saved policy bundles
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.policies.list_policies()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**detail:** `typing.Optional[bool]` — Include policy bundle detail in the form of the full bundle content for each entry
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.policies.<a href="src/fern/policies/client.py">add_policy</a>(...) -> PolicyBundleRecord</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new policy bundle to the system
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, MappingRule, ImageRef, ImageRefType, Policy
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.policies.add_policy(
    id="id",
    mappings=[
        MappingRule(
            image=ImageRef(
                type=ImageRefType.TAG,
                value="value",
            ),
            name="name",
            registry="registry",
            repository="repository",
        )
    ],
    policies=[
        Policy(
            id="id",
            version="version",
        )
    ],
    version="version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PolicyBundle` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.policies.<a href="src/fern/policies/client.py">get_policy</a>(...) -> PolicyBundleList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the policy bundle content
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.policies.get_policy(
    policy_id="policyId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**policy_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**detail:** `typing.Optional[bool]` — Include policy bundle detail in the form of the full bundle content for each entry
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.policies.<a href="src/fern/policies/client.py">update_policy</a>(...) -> PolicyBundleList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update/replace and existing policy
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.policies.update_policy(
    policy_id_="policyId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**policy_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PolicyBundleRecord` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Mark policy as active
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.policies.<a href="src/fern/policies/client.py">delete_policy</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the specified policy
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.policies.delete_policy(
    policy_id="policyId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**policy_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Query
<details><summary><code>client.query.<a href="src/fern/query/client.py">images_by_package</a>(...) -> PaginatedImageList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Filterable query interface to search for images containing specified package
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.query.images_by_package(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of package to search for (e.g. sed)
    
</dd>
</dl>

<dl>
<dd>

**package_type:** `typing.Optional[str]` — Type of package to filter on (e.g. dpkg)
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Version of named package to filter on (e.g. 4.4-1)
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — The page of results to fetch. Pages start at 1
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.query.<a href="src/fern/query/client.py">images_by_vulnerability</a>(...) -> PaginatedVulnerableImageList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a listing of images and their respective packages vulnerable to the given vulnerability ID
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.query.images_by_vulnerability(
    vulnerability_id="vulnerability_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vulnerability_id:** `str` — The ID of the vulnerability to search for within all images stored in anchore-engine (e.g. CVE-1999-0001)
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[str]` — Filter results to images within the given vulnerability namespace (e.g. debian:8, ubuntu:14.04)
    
</dd>
</dl>

<dl>
<dd>

**affected_package:** `typing.Optional[str]` — Filter results to images with vulnable packages with the given package name (e.g. libssl)
    
</dd>
</dl>

<dl>
<dd>

**severity:** `typing.Optional[QueryImagesByVulnerabilityRequestSeverity]` — Filter results to vulnerable package/vulnerability with the given severity
    
</dd>
</dl>

<dl>
<dd>

**vendor_only:** `typing.Optional[bool]` — Filter results to include only vulnerabilities that are not marked as invalid by upstream OS vendor data
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page of results to fetch. Pages start at 1
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.query.<a href="src/fern/query/client.py">vulnerabilities</a>(...) -> PaginatedVulnerabilityList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List (w/filters) vulnerability records known by the system, with affected packages information if present
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.query.vulnerabilities(
    id=[
        "id"
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

**id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The ID of the vulnerability (e.g. CVE-1999-0001)
    
</dd>
</dl>

<dl>
<dd>

**affected_package:** `typing.Optional[str]` — Filter results by specified package name (e.g. sed)
    
</dd>
</dl>

<dl>
<dd>

**affected_package_version:** `typing.Optional[str]` — Filter results by specified package version (e.g. 4.4-1)
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — The page of results to fetch. Pages start at 1
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page
    
</dd>
</dl>

<dl>
<dd>

**namespace:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Namespace(s) to filter vulnerability records by
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Registries
<details><summary><code>client.registries.<a href="src/fern/registries/client.py">list_registries</a>(...) -> RegistryConfigurationList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all configured registries the system can/will watch
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registries.list_registries()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registries.<a href="src/fern/registries/client.py">create_registry</a>(...) -> RegistryConfigurationList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new registry to the system
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registries.create_registry()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `RegistryConfigurationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**validate:** `typing.Optional[bool]` — flag to determine whether or not to validate registry/credential at registry add time
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registries.<a href="src/fern/registries/client.py">get_registry</a>(...) -> RegistryConfigurationList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information on a specific registry
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registries.get_registry(
    registry="registry",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registry:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registries.<a href="src/fern/registries/client.py">update_registry</a>(...) -> RegistryConfigurationList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replaces an existing registry record with the given record
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registries.update_registry(
    registry_="registry",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registry:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `RegistryConfigurationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**validate:** `typing.Optional[bool]` — flag to determine whether or not to validate registry/credential at registry update time
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registries.<a href="src/fern/registries/client.py">delete_registry</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a registry configuration record from the system. Does not remove any images.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.registries.delete_registry(
    registry="registry",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registry:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Repository Credentials
<details><summary><code>client.repository_credentials.<a href="src/fern/repository_credentials/client.py">add_repository</a>(...) -> SubscriptionList</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.repository_credentials.add_repository(
    repository="repository",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**repository:** `str` — full repository to add e.g. docker.io/library/alpine
    
</dd>
</dl>

<dl>
<dd>

**autosubscribe:** `typing.Optional[bool]` — flag to enable/disable auto tag_update activation when new images from a repo are added
    
</dd>
</dl>

<dl>
<dd>

**dryrun:** `typing.Optional[bool]` — flag to return tags in the repository without actually watching the repository, default is false
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## System
<details><summary><code>client.system.<a href="src/fern/system/client.py">get_status</a>() -> StatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the API service status
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.system.get_status()

```
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

<details><summary><code>client.system.<a href="src/fern/system/client.py">get_service_detail</a>() -> SystemStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the system status including queue lengths
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.system.get_service_detail()

```
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

<details><summary><code>client.system.<a href="src/fern/system/client.py">describe_error_codes</a>() -> typing.List[AnchoreErrorCode]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Describe anchore engine error codes.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.system.describe_error_codes()

```
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

<details><summary><code>client.system.<a href="src/fern/system/client.py">get_system_feeds</a>() -> typing.List[FeedMetadata]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return a list of feed and their groups along with update and record count information. This data reflects the state of the policy engine, not the upstream feed service itself.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.system.get_system_feeds()

```
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

<details><summary><code>client.system.<a href="src/fern/system/client.py">post_system_feeds</a>(...) -> FeedSyncResults</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a synchronous feed sync operation. The response will block until complete, then return the result summary.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.system.post_system_feeds()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**flush:** `typing.Optional[bool]` — instruct system to flush existing data feeds records from anchore-engine
    
</dd>
</dl>

<dl>
<dd>

**sync:** `typing.Optional[bool]` — instruct system to re-sync data feeds
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.system.<a href="src/fern/system/client.py">toggle_feed_enabled</a>(...) -> FeedMetadata</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disable the feed so that it does not sync on subsequent sync operations
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.system.toggle_feed_enabled(
    feed="feed",
    enabled=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**feed:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.system.<a href="src/fern/system/client.py">delete_feed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the groups and data for the feed and disable the feed itself
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.system.delete_feed(
    feed="feed",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**feed:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.system.<a href="src/fern/system/client.py">toggle_group_enabled</a>(...) -> typing.List[FeedMetadata]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disable a specific group within a feed to not sync
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.system.toggle_group_enabled(
    feed="feed",
    group="group",
    enabled=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**feed:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.system.<a href="src/fern/system/client.py">delete_feed_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the group data and disable the group itself
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.system.delete_feed_group(
    feed="feed",
    group="group",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**feed:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**group:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.system.<a href="src/fern/system/client.py">describe_policy</a>() -> typing.List[GateSpec]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the policy language spec for this service
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.system.describe_policy()

```
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

<details><summary><code>client.system.<a href="src/fern/system/client.py">list_services</a>() -> ServiceList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.system.list_services()

```
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

<details><summary><code>client.system.<a href="src/fern/system/client.py">get_services_by_name</a>(...) -> ServiceList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.system.get_services_by_name(
    servicename="servicename",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**servicename:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.system.<a href="src/fern/system/client.py">get_services_by_name_and_host</a>(...) -> ServiceList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.system.get_services_by_name_and_host(
    servicename="servicename",
    hostid="hostid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**servicename:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**hostid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.system.<a href="src/fern/system/client.py">delete_service</a>(...)</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.system.delete_service(
    servicename="servicename",
    hostid="hostid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**servicename:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**hostid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.system.<a href="src/fern/system/client.py">test_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Loads the Webhook configuration for webhook_type, and sends the notification out as a test
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.system.test_webhook(
    webhook_type="webhook_type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_type:** `str` — The Webhook Type that we should test
    
</dd>
</dl>

<dl>
<dd>

**notification_type:** `typing.Optional[TestWebhookRequestNotificationType]` — What kind of Notification to send
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.subscriptions.<a href="src/fern/subscriptions/client.py">list_subscriptions</a>(...) -> SubscriptionList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.subscriptions.list_subscriptions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_key:** `typing.Optional[str]` — filter only subscriptions matching key
    
</dd>
</dl>

<dl>
<dd>

**subscription_type:** `typing.Optional[str]` — filter only subscriptions matching type
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/fern/subscriptions/client.py">add_subscription</a>(...) -> SubscriptionList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new subscription to watch a tag and get notifications of changes
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.subscriptions.add_subscription()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**subscription_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**subscription_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**subscription_value:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/fern/subscriptions/client.py">get_subscription</a>(...) -> SubscriptionList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.subscriptions.get_subscription(
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

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/fern/subscriptions/client.py">update_subscription</a>(...) -> SubscriptionList</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.subscriptions.update_subscription(
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

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Toggle the subscription processing on or off
    
</dd>
</dl>

<dl>
<dd>

**subscription_value:** `typing.Optional[str]` — The new subscription value, e.g. the new tag to be subscribed to
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/fern/subscriptions/client.py">delete_subscription</a>(...)</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.subscriptions.delete_subscription(
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

**subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Summaries
<details><summary><code>client.summaries.<a href="src/fern/summaries/client.py">list_imagetags</a>(...) -> AnchoreImageTagSummaryList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all image tags visible to the user
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.summaries.list_imagetags()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_status:** `typing.Optional[typing.Union[ListImagetagsRequestImageStatusItem, typing.Sequence[ListImagetagsRequestImageStatusItem]]]` — Filter images in one or more states such as active, deleting. Defaults to active images only if unspecified
    
</dd>
</dl>

<dl>
<dd>

**anchore_account:** `typing.Optional[str]` — An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

