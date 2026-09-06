# Reference
## healthcheck
<details><summary><code>client.healthcheck.<a href="src/fern/healthcheck/client.py">healthz</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint can be used to check if the application is running and responding to requests
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.healthcheck.healthz()

```
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

## public shares
<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">get_share</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A zip file, containing the shared files and folders, will be generated on the fly and returned as response body. Only folders and regular files will be included in the zip. The share must be defined with the read scope and the associated user must have list and download permissions
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.get_share(
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

**id:** `str` — the share id
    
</dd>
</dl>

<dl>
<dd>

**compress:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">upload_to_share</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The share must be defined with the write scope and the associated user must have the upload permission
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.upload_to_share(
    id="id",
    filenames=["example_filenames"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — the share id
    
</dd>
</dl>

<dl>
<dd>

**filenames:** `typing.Optional[typing.List[core.File]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">download_share_file</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the file contents as response body. The share must have exactly one path defined and it must be a directory for this to work
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.download_share_file(
    id="id",
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — the share id
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Path to the file to download. It must be URL encoded, for example the path "my dir/àdir/file.txt" must be sent as "my%20dir%2F%C3%A0dir%2Ffile.txt"
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">get_share_dir_contents</a>(...) -> typing.List[DirEntry]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the contents of the specified directory for the specified share. The share must have exactly one path defined and it must be a directory for this to work
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.public_shares.get_share_dir_contents(
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

**id:** `str` — the share id
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` — Path to the folder to read. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir". If empty or missing the user's start directory is assumed. If relative, the user's start directory is used as the base
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.public_shares.<a href="src/fern/public_shares/client.py">upload_single_to_share</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The share must be defined with the write scope and the associated user must have the upload/overwrite permissions
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.public_shares.upload_single_to_share(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — the share id
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `str` — the name of the new file. It must be path encoded. Sub directories are not accepted
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## token
<details><summary><code>client.token.<a href="src/fern/token/client.py">get_token</a>(...) -> Token</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an access token and its expiration
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.token.get_token()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sftpgo_otp:** `typing.Optional[str]` — If you have 2FA configured for the admin attempting to log in you need to set the authentication code using this header parameter
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.token.<a href="src/fern/token/client.py">logout</a>() -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allows to invalidate an admin token before its expiration
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.token.logout()

```
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

<details><summary><code>client.token.<a href="src/fern/token/client.py">get_user_token</a>(...) -> Token</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an access token and its expiration
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.token.get_user_token()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sftpgo_otp:** `typing.Optional[str]` — If you have 2FA configured, for the HTTP protocol, for the user attempting to log in you need to set the authentication code using this header parameter
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.token.<a href="src/fern/token/client.py">client_logout</a>() -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allows to invalidate a client token before its expiration
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.token.client_logout()

```
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

## maintenance
<details><summary><code>client.maintenance.<a href="src/fern/maintenance/client.py">get_version</a>() -> VersionInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns version details such as the version number, build date, commit hash and enabled features
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.maintenance.get_version()

```
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

<details><summary><code>client.maintenance.<a href="src/fern/maintenance/client.py">get_status</a>() -> ServicesStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the status of the active services
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.maintenance.get_status()

```
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

<details><summary><code>client.maintenance.<a href="src/fern/maintenance/client.py">dumpdata</a>(...) -> DumpdataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Backups data as data provider independent JSON. The backup can be saved in a local file on the server, to avoid exposing sensitive data over the network, or returned as response body. The output of dumpdata can be used as input for loaddata
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.maintenance.dumpdata()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**output_file:** `typing.Optional[str]` — Path for the file to write the JSON serialized data to. This path is relative to the configured "backups_path". If this file already exists it will be overwritten. To return the backup as response body set `output_data` to true instead.
    
</dd>
</dl>

<dl>
<dd>

**output_data:** `typing.Optional[int]` 

output data:
  * `0` or any other value != 1, the backup will be saved to a file on the server, `output_file` is required
  * `1` the backup will be returned as response body
    
</dd>
</dl>

<dl>
<dd>

**indent:** `typing.Optional[int]` 

indent:
  * `0` no indentation. This is the default
  * `1` format the output JSON
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.Optional[typing.Union[DumpDataScopes, typing.Sequence[DumpDataScopes]]]` — You can limit the dump contents to the specified scopes. Empty or missing means any supported scope. Scopes must be specified comma separated
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.maintenance.<a href="src/fern/maintenance/client.py">loaddata_from_file</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores SFTPGo data from a JSON backup file on the server. Objects will be restored one by one and the restore is stopped if a object cannot be added or updated, so it could happen a partial restore
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.maintenance.loaddata_from_file(
    input_file="input-file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input_file:** `str` — Path for the file to read the JSON serialized data from. This can be an absolute path or a path relative to the configured "backups_path". The max allowed file size is 10MB
    
</dd>
</dl>

<dl>
<dd>

**scan_quota:** `typing.Optional[int]` 

Quota scan:
  * `0` no quota scan is done, the imported users/folders will have used_quota_size and used_quota_files = 0 or the existing values if they already exists. This is the default
  * `1` scan quota
  * `2` scan quota if the user has quota restrictions
required: false
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[int]` 

Mode:
  * `0` New objects are added, existing ones are updated. This is the default
  * `1` New objects are added, existing ones are not modified
  * `2` New objects are added, existing ones are updated and connected users are disconnected and so forced to use the new configuration
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.maintenance.<a href="src/fern/maintenance/client.py">loaddata_from_request_body</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restores SFTPGo data from a JSON backup. Objects will be restored one by one and the restore is stopped if a object cannot be added or updated, so it could happen a partial restore
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.maintenance.loaddata_from_request_body()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `BackupData` 
    
</dd>
</dl>

<dl>
<dd>

**scan_quota:** `typing.Optional[int]` 

Quota scan:
  * `0` no quota scan is done, the imported users/folders will have used_quota_size and used_quota_files = 0 or the existing values if they already exists. This is the default
  * `1` scan quota
  * `2` scan quota if the user has quota restrictions
required: false
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[int]` 

Mode:
  * `0` New objects are added, existing ones are updated. This is the default
  * `1` New objects are added, existing ones are not modified
  * `2` New objects are added, existing ones are updated and connected users are disconnected and so forced to use the new configuration
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## admins
<details><summary><code>client.admins.<a href="src/fern/admins/client.py">change_admin_password</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Changes the password for the logged in admin
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.admins.change_admin_password()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PwdChange` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admins.<a href="src/fern/admins/client.py">get_admin_profile</a>() -> AdminProfile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the profile for the logged in admin
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.admins.get_admin_profile()

```
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

<details><summary><code>client.admins.<a href="src/fern/admins/client.py">update_admin_profile</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allows to update the profile for the logged in admin
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.admins.update_admin_profile()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `AdminProfile` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admins.<a href="src/fern/admins/client.py">get_admin_recovery_codes</a>() -> typing.List[RecoveryCode]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the recovery codes for the logged in admin. Recovery codes can be used if the admin loses access to their second factor auth device. Recovery codes are returned unencrypted
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.admins.get_admin_recovery_codes()

```
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

<details><summary><code>client.admins.<a href="src/fern/admins/client.py">generate_admin_recovery_codes</a>() -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates new recovery codes for the logged in admin. Generating new recovery codes you automatically invalidate old ones
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.admins.generate_admin_recovery_codes()

```
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

<details><summary><code>client.admins.<a href="src/fern/admins/client.py">get_admin_totp_configs</a>() -> typing.List[TotpConfig]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the available TOTP configurations for the logged in admin
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.admins.get_admin_totp_configs()

```
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

<details><summary><code>client.admins.<a href="src/fern/admins/client.py">generate_admin_totp_secret</a>(...) -> GenerateAdminTotpSecretResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates a new TOTP secret, including the QR code as png, using the specified configuration for the logged in admin
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.admins.generate_admin_totp_secret()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**config_name:** `typing.Optional[str]` — name of the configuration to use to generate the secret
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admins.<a href="src/fern/admins/client.py">validate_admin_totp_secret</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Checks if the given authentication code can be validated using the specified secret and config name
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.admins.validate_admin_totp_secret()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**config_name:** `typing.Optional[str]` — name of the configuration to use to validate the passcode
    
</dd>
</dl>

<dl>
<dd>

**passcode:** `typing.Optional[str]` — passcode to validate
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[str]` — secret to use to validate the passcode
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admins.<a href="src/fern/admins/client.py">save_admin_totp_config</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Saves the specified TOTP config for the logged in admin
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.admins.save_admin_totp_config()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `AdminTotpConfig` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admins.<a href="src/fern/admins/client.py">get_admins</a>(...) -> typing.List[Admin]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array with one or more admins. For security reasons hashed passwords are omitted in the response
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.admins.get_admins()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of items to return. Max value is 500, default is 100
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetAdminsRequestOrder]` — Ordering admins by username. Default ASC
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admins.<a href="src/fern/admins/client.py">add_admin</a>(...) -> Admin</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new admin. Recovery codes and TOTP configuration cannot be set using this API: each admin must use the specific APIs
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.admins.add_admin()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Admin` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admins.<a href="src/fern/admins/client.py">get_admin_by_username</a>(...) -> Admin</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the admin with the given username, if it exists. For security reasons the hashed password is omitted in the response
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.admins.get_admin_by_username(
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

**username:** `str` — the admin username
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admins.<a href="src/fern/admins/client.py">update_admin</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing admin. Recovery codes and TOTP configuration cannot be set/updated using this API: each admin must use the specific APIs. You are not allowed to update the admin impersonated using an API key
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.admins.update_admin(
    username_="username",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `str` — the admin username
    
</dd>
</dl>

<dl>
<dd>

**request:** `Admin` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admins.<a href="src/fern/admins/client.py">delete_admin</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing admin
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.admins.delete_admin(
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

**username:** `str` — the admin username
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admins.<a href="src/fern/admins/client.py">disable_admin2fa</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disables second factor authentication for the given admin. This API must be used if the admin loses access to their second factor auth device and has no recovery codes
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.admins.disable_admin2fa(
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

**username:** `str` — the admin username
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admins.<a href="src/fern/admins/client.py">admin_forgot_password</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You must set up an SMTP server. SFTPGo will send a code via email to reset the password if the specified admin exists and has a valid email address. Requests that do not meet these conditions are silently ignored (a success response will be returned) to avoid disclosing existing admins
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.admins.admin_forgot_password(
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

**username:** `str` — the admin username
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admins.<a href="src/fern/admins/client.py">admin_reset_password</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set a new password using the code received via email
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.admins.admin_reset_password(
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

**username:** `str` — the admin username
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` 
    
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

## connections
<details><summary><code>client.connections.<a href="src/fern/connections/client.py">get_connections</a>() -> typing.List[ConnectionStatus]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the active users and info about their current uploads/downloads
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connections.get_connections()

```
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

<details><summary><code>client.connections.<a href="src/fern/connections/client.py">close_connection</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Terminates an active connection
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.connections.close_connection(
    connection_id="connectionID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `str` — ID of the connection to close
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## IP Lists
<details><summary><code>client.ip_lists.<a href="src/fern/ip_lists/client.py">get_ip_list_entries</a>(...) -> typing.List[IpListEntry]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array with one or more IP list entry
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ip_lists.get_ip_list_entries(
    type=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `IpListType` — IP list type
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — restrict results to ipornet matching or starting with this filter
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[str]` — ipornet to start from
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of items to return. Max value is 500, default is 100
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetIpListEntriesRequestOrder]` — Ordering entries by ipornet field. Default ASC
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ip_lists.<a href="src/fern/ip_lists/client.py">add_ip_list_entry</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add an IP address or a CIDR network to a supported list
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ip_lists.add_ip_list_entry(
    type_=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `IpListType` — IP list type
    
</dd>
</dl>

<dl>
<dd>

**request:** `IpListEntry` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ip_lists.<a href="src/fern/ip_lists/client.py">get_ip_list_by_ipornet</a>(...) -> IpListEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the entry with the given ipornet if it exists.
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ip_lists.get_ip_list_by_ipornet(
    type=1,
    ipornet="ipornet",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `IpListType` — IP list type
    
</dd>
</dl>

<dl>
<dd>

**ipornet:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ip_lists.<a href="src/fern/ip_lists/client.py">update_ip_list_entry</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing IP list entry
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ip_lists.update_ip_list_entry(
    type_=1,
    ipornet_="ipornet",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `IpListType` — IP list type
    
</dd>
</dl>

<dl>
<dd>

**ipornet:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `IpListEntry` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ip_lists.<a href="src/fern/ip_lists/client.py">delete_ip_list_entry</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing IP list entry
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.ip_lists.delete_ip_list_entry(
    type=1,
    ipornet="ipornet",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `IpListType` — IP list type
    
</dd>
</dl>

<dl>
<dd>

**ipornet:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## defender
<details><summary><code>client.defender.<a href="src/fern/defender/client.py">get_defender_hosts</a>() -> typing.List[DefenderEntry]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns hosts that are banned or for which some violations have been detected
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.defender.get_defender_hosts()

```
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

<details><summary><code>client.defender.<a href="src/fern/defender/client.py">get_defender_host_by_id</a>(...) -> DefenderEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the host with the given id, if it exists
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.defender.get_defender_host_by_id(
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

**id:** `str` — host id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.defender.<a href="src/fern/defender/client.py">delete_defender_host_by_id</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unbans the specified host or clears its violations
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.defender.delete_defender_host_by_id(
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

**id:** `str` — host id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## data retention
<details><summary><code>client.data_retention.<a href="src/fern/data_retention/client.py">get_users_retention_checks</a>() -> typing.List[RetentionCheck]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the active retention checks
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.data_retention.get_users_retention_checks()

```
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

## quota
<details><summary><code>client.quota.<a href="src/fern/quota/client.py">get_users_quota_scans</a>() -> typing.List[QuotaScan]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the active user quota scans
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.quota.get_users_quota_scans()

```
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

<details><summary><code>client.quota.<a href="src/fern/quota/client.py">start_user_quota_scan</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts a new quota scan for the given user. A quota scan updates the number of files and their total size for the specified user and the virtual folders, if any, included in his quota
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.quota.start_user_quota_scan(
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

**username:** `str` — the username
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quota.<a href="src/fern/quota/client.py">user_quota_update_usage</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets the current used quota limits for the given user
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.quota.user_quota_update_usage(
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

**username:** `str` — the username
    
</dd>
</dl>

<dl>
<dd>

**request:** `QuotaUsage` 
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[UserQuotaUpdateUsageRequestMode]` — the update mode specifies if the given quota usage values should be added or replace the current ones
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quota.<a href="src/fern/quota/client.py">user_transfer_quota_update_usage</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets the current used transfer quota limits for the given user
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.quota.user_transfer_quota_update_usage(
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

**username:** `str` — the username
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[UserTransferQuotaUpdateUsageRequestMode]` — the update mode specifies if the given quota usage values should be added or replace the current ones
    
</dd>
</dl>

<dl>
<dd>

**used_upload_data_transfer:** `typing.Optional[int]` — The value must be specified as bytes
    
</dd>
</dl>

<dl>
<dd>

**used_download_data_transfer:** `typing.Optional[int]` — The value must be specified as bytes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quota.<a href="src/fern/quota/client.py">get_folders_quota_scans</a>() -> typing.List[FolderQuotaScan]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the active folder quota scans
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.quota.get_folders_quota_scans()

```
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

<details><summary><code>client.quota.<a href="src/fern/quota/client.py">start_folder_quota_scan</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts a new quota scan for the given folder. A quota scan update the number of files and their total size for the specified folder
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.quota.start_folder_quota_scan(
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

**name:** `str` — folder name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quota.<a href="src/fern/quota/client.py">folder_quota_update_usage</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets the current used quota limits for the given folder
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.quota.folder_quota_update_usage(
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

**name:** `str` — folder name
    
</dd>
</dl>

<dl>
<dd>

**request:** `QuotaUsage` 
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[FolderQuotaUpdateUsageRequestMode]` — the update mode specifies if the given quota usage values should be added or replace the current ones
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## folders
<details><summary><code>client.folders.<a href="src/fern/folders/client.py">get_folders</a>(...) -> typing.List[BaseVirtualFolder]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array with one or more folders
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.folders.get_folders()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of items to return. Max value is 500, default is 100
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetFoldersRequestOrder]` — Ordering folders by name. Default ASC
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">add_folder</a>(...) -> BaseVirtualFolder</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new folder. A quota scan is required to update the used files/size
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.folders.add_folder()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `BaseVirtualFolder` 
    
</dd>
</dl>

<dl>
<dd>

**confidential_data:** `typing.Optional[int]` — If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">get_folder_by_name</a>(...) -> BaseVirtualFolder</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the folder with the given name if it exists.
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.folders.get_folder_by_name(
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

**name:** `str` — folder name
    
</dd>
</dl>

<dl>
<dd>

**confidential_data:** `typing.Optional[int]` — If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">update_folder</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing folder
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.folders.update_folder(
    name_="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — folder name
    
</dd>
</dl>

<dl>
<dd>

**request:** `BaseVirtualFolder` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.folders.<a href="src/fern/folders/client.py">delete_folder</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing folder. A folder referenced by users or groups cannot be deleted, remove the references first
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.folders.delete_folder(
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

**name:** `str` — folder name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## groups
<details><summary><code>client.groups.<a href="src/fern/groups/client.py">get_groups</a>(...) -> typing.List[Group]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array with one or more groups
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.groups.get_groups()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of items to return. Max value is 500, default is 100
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetGroupsRequestOrder]` — Ordering groups by name. Default ASC
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">add_group</a>(...) -> Group</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new group
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.groups.add_group()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Group` 
    
</dd>
</dl>

<dl>
<dd>

**confidential_data:** `typing.Optional[int]` — If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">get_group_by_name</a>(...) -> Group</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the group with the given name if it exists.
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.groups.get_group_by_name(
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

**name:** `str` — group name
    
</dd>
</dl>

<dl>
<dd>

**confidential_data:** `typing.Optional[int]` — If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">update_group</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing group
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.groups.update_group(
    name_="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — group name
    
</dd>
</dl>

<dl>
<dd>

**request:** `Group` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">delete_group</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing group. A group referenced by users or admins cannot be deleted, remove the references first
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.groups.delete_group(
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

**name:** `str` — group name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## roles
<details><summary><code>client.roles.<a href="src/fern/roles/client.py">get_roles</a>(...) -> typing.List[Role]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array with one or more roles
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.roles.get_roles()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of items to return. Max value is 500, default is 100
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetRolesRequestOrder]` — Ordering groups by name. Default ASC
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/fern/roles/client.py">add_role</a>(...) -> Role</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new role
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.roles.add_role()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Role` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/fern/roles/client.py">get_role_by_name</a>(...) -> Role</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the role with the given name if it exists.
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.roles.get_role_by_name(
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

**name:** `str` — role name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/fern/roles/client.py">update_role</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing role
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.roles.update_role(
    name_="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — role name
    
</dd>
</dl>

<dl>
<dd>

**request:** `Role` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/fern/roles/client.py">delete_role</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing role. A role referenced by users or admins cannot be deleted, remove the references first
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.roles.delete_role(
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

**name:** `str` — role name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## event manager
<details><summary><code>client.event_manager.<a href="src/fern/event_manager/client.py">get_event_actons</a>(...) -> typing.List[BaseEventAction]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array with one or more event actions
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event_manager.get_event_actons()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of items to return. Max value is 500, default is 100
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetEventActonsRequestOrder]` — Ordering actions by name. Default ASC
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_manager.<a href="src/fern/event_manager/client.py">add_event_action</a>(...) -> BaseEventAction</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new event actions
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event_manager.add_event_action()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `BaseEventAction` 
    
</dd>
</dl>

<dl>
<dd>

**confidential_data:** `typing.Optional[int]` — If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_manager.<a href="src/fern/event_manager/client.py">get_event_action_by_name</a>(...) -> BaseEventAction</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the event action with the given name if it exists.
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event_manager.get_event_action_by_name(
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

**name:** `str` — action name
    
</dd>
</dl>

<dl>
<dd>

**confidential_data:** `typing.Optional[int]` — If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_manager.<a href="src/fern/event_manager/client.py">update_event_action</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing event action
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event_manager.update_event_action(
    name_="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — action name
    
</dd>
</dl>

<dl>
<dd>

**request:** `BaseEventAction` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_manager.<a href="src/fern/event_manager/client.py">delete_event_action</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing event action
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event_manager.delete_event_action(
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

**name:** `str` — action name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_manager.<a href="src/fern/event_manager/client.py">get_event_rules</a>(...) -> typing.List[EventRule]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array with one or more event rules
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event_manager.get_event_rules()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of items to return. Max value is 500, default is 100
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetEventRulesRequestOrder]` — Ordering rules by name. Default ASC
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_manager.<a href="src/fern/event_manager/client.py">add_event_rule</a>(...) -> EventRule</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new event rule
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event_manager.add_event_rule()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `EventRuleMinimal` 
    
</dd>
</dl>

<dl>
<dd>

**confidential_data:** `typing.Optional[int]` — If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_manager.<a href="src/fern/event_manager/client.py">get_event_rile_by_name</a>(...) -> EventRule</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the event rule with the given name if it exists.
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event_manager.get_event_rile_by_name(
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

**name:** `str` — rule name
    
</dd>
</dl>

<dl>
<dd>

**confidential_data:** `typing.Optional[int]` — If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_manager.<a href="src/fern/event_manager/client.py">update_event_rule</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing event rule
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event_manager.update_event_rule(
    name_="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — rule name
    
</dd>
</dl>

<dl>
<dd>

**request:** `EventRuleMinimal` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_manager.<a href="src/fern/event_manager/client.py">delete_event_rule</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing event rule
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event_manager.delete_event_rule(
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

**name:** `str` — rule name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_manager.<a href="src/fern/event_manager/client.py">run_event_rule</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The rule's actions will run in background. SFTPGo will not monitor any concurrency and such. If you want to be notified at the end of the execution please add an appropriate action
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event_manager.run_event_rule(
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

**name:** `str` — on-demand rule name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## events
<details><summary><code>client.events.<a href="src/fern/events/client.py">get_fs_events</a>(...) -> typing.List[FsEvent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array with one or more filesystem events applying the specified filters. This API is only available if you configure an "eventsearcher" plugin
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.events.get_fs_events()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_timestamp:** `typing.Optional[int]` — the event timestamp, unix timestamp in nanoseconds, must be greater than or equal to the specified one. 0 or missing means omit this filter
    
</dd>
</dl>

<dl>
<dd>

**end_timestamp:** `typing.Optional[int]` — the event timestamp, unix timestamp in nanoseconds, must be less than or equal to the specified one. 0 or missing means omit this filter
    
</dd>
</dl>

<dl>
<dd>

**actions:** `typing.Optional[typing.Union[FsEventAction, typing.Sequence[FsEventAction]]]` — the event action must be included among those specified. Empty or missing means omit this filter. Actions must be specified comma separated
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — the event username must be the same as the one specified. Empty or missing means omit this filter
    
</dd>
</dl>

<dl>
<dd>

**ip:** `typing.Optional[str]` — the event IP must be the same as the one specified. Empty or missing means omit this filter
    
</dd>
</dl>

<dl>
<dd>

**ssh_cmd:** `typing.Optional[str]` — the event SSH command must be the same as the one specified. Empty or missing means omit this filter
    
</dd>
</dl>

<dl>
<dd>

**fs_provider:** `typing.Optional[FsProviders]` — the event filesystem provider must be the same as the one specified. Empty or missing means omit this filter
    
</dd>
</dl>

<dl>
<dd>

**bucket:** `typing.Optional[str]` — the bucket must be the same as the one specified. Empty or missing means omit this filter
    
</dd>
</dl>

<dl>
<dd>

**endpoint:** `typing.Optional[str]` — the endpoint must be the same as the one specified. Empty or missing means omit this filter
    
</dd>
</dl>

<dl>
<dd>

**protocols:** `typing.Optional[typing.Union[EventProtocols, typing.Sequence[EventProtocols]]]` — the event protocol must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated
    
</dd>
</dl>

<dl>
<dd>

**statuses:** `typing.Optional[typing.Union[FsEventStatus, typing.Sequence[FsEventStatus]]]` — the event status must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated
    
</dd>
</dl>

<dl>
<dd>

**instance_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — the event instance id must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated
    
</dd>
</dl>

<dl>
<dd>

**from_id:** `typing.Optional[str]` — the event id to start from. This is useful for cursor based pagination. Empty or missing means omit this filter.
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[str]` — User role. Empty or missing means omit this filter. Ignored if the admin has a role
    
</dd>
</dl>

<dl>
<dd>

**csv_export:** `typing.Optional[bool]` — If enabled, events are exported as a CSV file
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of items to return. Max value is 1000, default is 100
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetFsEventsRequestOrder]` — Ordering events by timestamp. Default DESC
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/fern/events/client.py">get_provider_events</a>(...) -> typing.List[ProviderEvent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array with one or more provider events applying the specified filters. This API is only available if you configure an "eventsearcher" plugin
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.events.get_provider_events()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_timestamp:** `typing.Optional[int]` — the event timestamp, unix timestamp in nanoseconds, must be greater than or equal to the specified one. 0 or missing means omit this filter
    
</dd>
</dl>

<dl>
<dd>

**end_timestamp:** `typing.Optional[int]` — the event timestamp, unix timestamp in nanoseconds, must be less than or equal to the specified one. 0 or missing means omit this filter
    
</dd>
</dl>

<dl>
<dd>

**actions:** `typing.Optional[typing.Union[ProviderEventAction, typing.Sequence[ProviderEventAction]]]` — the event action must be included among those specified. Empty or missing means omit this filter. Actions must be specified comma separated
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — the event username must be the same as the one specified. Empty or missing means omit this filter
    
</dd>
</dl>

<dl>
<dd>

**ip:** `typing.Optional[str]` — the event IP must be the same as the one specified. Empty or missing means omit this filter
    
</dd>
</dl>

<dl>
<dd>

**object_name:** `typing.Optional[str]` — the event object name must be the same as the one specified. Empty or missing means omit this filter
    
</dd>
</dl>

<dl>
<dd>

**object_types:** `typing.Optional[typing.Union[ProviderEventObjectType, typing.Sequence[ProviderEventObjectType]]]` — the event object type must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated
    
</dd>
</dl>

<dl>
<dd>

**instance_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — the event instance id must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated
    
</dd>
</dl>

<dl>
<dd>

**from_id:** `typing.Optional[str]` — the event id to start from. This is useful for cursor based pagination. Empty or missing means omit this filter.
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[str]` — Admin role. Empty or missing means omit this filter. Ignored if the admin has a role
    
</dd>
</dl>

<dl>
<dd>

**csv_export:** `typing.Optional[bool]` — If enabled, events are exported as a CSV file
    
</dd>
</dl>

<dl>
<dd>

**omit_object_data:** `typing.Optional[bool]` — If enabled, returned events will not contain the `object_data` field
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of items to return. Max value is 1000, default is 100
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetProviderEventsRequestOrder]` — Ordering events by timestamp. Default DESC
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/fern/events/client.py">get_log_events</a>(...) -> typing.List[LogEvent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array with one or more log events applying the specified filters. This API is only available if you configure an "eventsearcher" plugin
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.events.get_log_events()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_timestamp:** `typing.Optional[int]` — the event timestamp, unix timestamp in nanoseconds, must be greater than or equal to the specified one. 0 or missing means omit this filter
    
</dd>
</dl>

<dl>
<dd>

**end_timestamp:** `typing.Optional[int]` — the event timestamp, unix timestamp in nanoseconds, must be less than or equal to the specified one. 0 or missing means omit this filter
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.Optional[typing.Union[LogEventType, typing.Sequence[LogEventType]]]` — the log events must be included among those specified. Empty or missing means omit this filter. Events must be specified comma separated
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — the event username must be the same as the one specified. Empty or missing means omit this filter
    
</dd>
</dl>

<dl>
<dd>

**ip:** `typing.Optional[str]` — the event IP must be the same as the one specified. Empty or missing means omit this filter
    
</dd>
</dl>

<dl>
<dd>

**protocols:** `typing.Optional[typing.Union[EventProtocols, typing.Sequence[EventProtocols]]]` — the event protocol must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated
    
</dd>
</dl>

<dl>
<dd>

**instance_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — the event instance id must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated
    
</dd>
</dl>

<dl>
<dd>

**from_id:** `typing.Optional[str]` — the event id to start from. This is useful for cursor based pagination. Empty or missing means omit this filter.
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[str]` — User role. Empty or missing means omit this filter. Ignored if the admin has a role
    
</dd>
</dl>

<dl>
<dd>

**csv_export:** `typing.Optional[bool]` — If enabled, events are exported as a CSV file
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of items to return. Max value is 1000, default is 100
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetLogEventsRequestOrder]` — Ordering events by timestamp. Default DESC
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## API keys
<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">get_api_keys</a>(...) -> typing.List[ApiKey]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array with one or more API keys. For security reasons hashed keys are omitted in the response
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.get_api_keys()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of items to return. Max value is 500, default is 100
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetApiKeysRequestOrder]` — Ordering API keys by id. Default ASC
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">add_api_key</a>(...) -> AddApiKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new API key
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.add_api_key()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ApiKey` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">get_api_key_by_id</a>(...) -> ApiKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the API key with the given id, if it exists. For security reasons the hashed key is omitted in the response
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.get_api_key_by_id(
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

**id:** `str` — the key id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">update_api_key</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing API key. You cannot update the key itself, the creation date and the last use
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.update_api_key(
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

**id:** `str` — the key id
    
</dd>
</dl>

<dl>
<dd>

**request:** `ApiKey` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/fern/api_keys/client.py">delete_api_key</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing API key
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.api_keys.delete_api_key(
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

**id:** `str` — the key id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## users
<details><summary><code>client.users.<a href="src/fern/users/client.py">get_users</a>(...) -> typing.List[User]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array with one or more users. For security reasons hashed passwords are omitted in the response
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.get_users()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of items to return. Max value is 500, default is 100
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetUsersRequestOrder]` — Ordering users by username. Default ASC
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">add_user</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new user.Recovery codes and TOTP configuration cannot be set using this API: each user must use the specific APIs
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.add_user()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `User` 
    
</dd>
</dl>

<dl>
<dd>

**confidential_data:** `typing.Optional[int]` — If set to 1 confidential data will not be hidden. This means that the response will contain the hash of the password and the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">get_user_by_username</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the user with the given username if it exists. For security reasons the hashed password is omitted in the response
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.get_user_by_username(
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

**username:** `str` — the username
    
</dd>
</dl>

<dl>
<dd>

**confidential_data:** `typing.Optional[int]` — If set to 1 confidential data will not be hidden. This means that the response will contain the hash of the password and the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">update_user</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing user and optionally disconnects it, if connected, to apply the new settings. The current password will be preserved if the password field is omitted in the request body. Recovery codes and TOTP configuration cannot be set/updated using this API: each user must use the specific APIs
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.update_user(
    username_="username",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `str` — the username
    
</dd>
</dl>

<dl>
<dd>

**request:** `User` 
    
</dd>
</dl>

<dl>
<dd>

**disconnect:** `typing.Optional[int]` 

Disconnect:
  * `0` The user will not be disconnected and it will continue to use the old configuration until connected. This is the default
  * `1` The user will be disconnected after a successful update. It must login again and so it will be forced to use the new configuration
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">delete_user</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing user
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.delete_user(
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

**username:** `str` — the username
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">disable_user2fa</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disables second factor authentication for the given user. This API must be used if the user loses access to their second factor auth device and has no recovery codes
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.disable_user2fa(
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

**username:** `str` — the username
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">user_forgot_password</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You must configure an SMTP server. SFTPGo will send a code via email to reset the password if the specified user exists, has a valid email address and does not have the "reset-password-disabled" restriction. Requests that do not meet these conditions are silently ignored (a success response will be returned) to avoid disclosing existing users
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.user_forgot_password(
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

**username:** `str` — the username
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">user_reset_password</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set a new password using the code received via email
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.user_reset_password(
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

**username:** `str` — the username
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` 
    
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

## user APIs
<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">change_user_password</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Changes the password for the logged in user
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.change_user_password()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PwdChange` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">get_user_profile</a>() -> UserProfile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the profile for the logged in user
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.get_user_profile()

```
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

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">update_user_profile</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allows to update the profile for the logged in user
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.update_user_profile()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `UserProfile` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">get_user_recovery_codes</a>() -> typing.List[RecoveryCode]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the recovery codes for the logged in user. Recovery codes can be used if the user loses access to their second factor auth device. Recovery codes are returned unencrypted
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.get_user_recovery_codes()

```
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

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">generate_user_recovery_codes</a>() -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates new recovery codes for the logged in user. Generating new recovery codes you automatically invalidate old ones
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.generate_user_recovery_codes()

```
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

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">get_user_totp_configs</a>() -> typing.List[TotpConfig]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the available TOTP configurations for the logged in user
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.get_user_totp_configs()

```
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

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">generate_user_totp_secret</a>(...) -> GenerateUserTotpSecretResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates a new TOTP secret, including the QR code as png, using the specified configuration for the logged in user
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.generate_user_totp_secret()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**config_name:** `typing.Optional[str]` — name of the configuration to use to generate the secret
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">validate_user_totp_secret</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Checks if the given authentication code can be validated using the specified secret and config name
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.validate_user_totp_secret()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**config_name:** `typing.Optional[str]` — name of the configuration to use to validate the passcode
    
</dd>
</dl>

<dl>
<dd>

**passcode:** `typing.Optional[str]` — passcode to validate
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[str]` — secret to use to validate the passcode
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">save_user_totp_config</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Saves the specified TOTP config for the logged in user
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.save_user_totp_config()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `UserTotpConfig` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">get_user_shares</a>(...) -> typing.List[Share]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the share for the logged in user
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.get_user_shares()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of items to return. Max value is 500, default is 100
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetUserSharesRequestOrder]` — Ordering shares by ID. Default ASC
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">add_share</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new share. The share id will be auto-generated
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.add_share()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Share` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">get_user_share_by_id</a>(...) -> Share</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a share by id for the logged in user
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.get_user_share_by_id(
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

**id:** `str` — the share id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">update_user_share</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing share belonging to the logged in user
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.update_user_share(
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

**id:** `str` — the share id
    
</dd>
</dl>

<dl>
<dd>

**request:** `Share` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">delete_user_share</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing share belonging to the logged in user
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.delete_user_share(
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

**id:** `str` — the share id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">copy_a_file_or_a_directory</a>(...) -> ApiResponse</code></summary>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.copy_a_file_or_a_directory(
    path="path",
    target="target",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `str` — Path to the file/folder to copy. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"
    
</dd>
</dl>

<dl>
<dd>

**target:** `str` — New name. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">move_rename_a_file_or_a_directory</a>(...) -> ApiResponse</code></summary>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.move_rename_a_file_or_a_directory(
    path="path",
    target="target",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `str` — Path to the file/folder to rename. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"
    
</dd>
</dl>

<dl>
<dd>

**target:** `str` — New name. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">get_user_dir_contents</a>(...) -> typing.List[DirEntry]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the contents of the specified directory for the logged in user
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.get_user_dir_contents()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `typing.Optional[str]` — Path to the folder to read. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir". If empty or missing the user's start directory is assumed. If relative, the user's start directory is used as the base
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">create_user_dir</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a directory for the logged in user
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.create_user_dir(
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `str` — Path to the folder to create. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"
    
</dd>
</dl>

<dl>
<dd>

**mkdir_parents:** `typing.Optional[bool]` — Create parent directories if they do not exist?
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">delete_user_dir</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a directory and any children it contains for the logged in user
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.delete_user_dir(
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `str` — Path to the folder to delete. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">rename_user_dir</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rename a directory for the logged in user. The rename is allowed for empty directory or for non empty local directories, with no virtual folders inside
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.rename_user_dir(
    path="path",
    target="target",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `str` — Path to the folder to rename. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"
    
</dd>
</dl>

<dl>
<dd>

**target:** `str` — New name. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir"
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">download_user_file</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the file contents as response body
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.download_user_file(
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `str` — Path to the file to download. It must be URL encoded, for example the path "my dir/àdir/file.txt" must be sent as "my%20dir%2F%C3%A0dir%2Ffile.txt"
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">create_user_files</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload one or more files for the logged in user
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.create_user_files(
    filenames=["example_filenames"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `typing.Optional[str]` — Parent directory for the uploaded files. It must be URL encoded, for example the path "my dir/àdir" must be sent as "my%20dir%2F%C3%A0dir". If empty or missing the root path is assumed. If a file with the same name already exists, it will be overwritten
    
</dd>
</dl>

<dl>
<dd>

**mkdir_parents:** `typing.Optional[bool]` — Create parent directories if they do not exist?
    
</dd>
</dl>

<dl>
<dd>

**filenames:** `typing.Optional[typing.List[core.File]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">delete_user_file</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a file for the logged in user.
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.delete_user_file(
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `str` — Path to the file to delete. It must be URL encoded
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">rename_user_file</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rename a file for the logged in user. Deprecated, use "file-actions/move"
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.rename_user_file(
    path="path",
    target="target",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `str` — Path to the file to rename. It must be URL encoded
    
</dd>
</dl>

<dl>
<dd>

**target:** `str` — New name. It must be URL encoded
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">create_user_file</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a single file for the logged in user to an existing directory. This API does not use multipart/form-data and so no temporary files are created server side but only a single file can be uploaded as POST body
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.user_ap_is.create_user_file(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `str` — Full file path. It must be path encoded, for example the path "my dir/àdir/file.txt" must be sent as "my%20dir%2F%C3%A0dir%2Ffile.txt". The parent directory must exist. If a file with the same name already exists, it will be overwritten
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` 
    
</dd>
</dl>

<dl>
<dd>

**mkdir_parents:** `typing.Optional[bool]` — Create parent directories if they do not exist?
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">setprops_user_file</a>(...) -> ApiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set supported metadata attributes for the specified file or directory
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.setprops_user_file(
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**path:** `str` — Full file/directory path. It must be URL encoded, for example the path "my dir/àdir/file.txt" must be sent as "my%20dir%2F%C3%A0dir%2Ffile.txt"
    
</dd>
</dl>

<dl>
<dd>

**modification_time:** `typing.Optional[int]` — File modification time as unix timestamp in milliseconds
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_ap_is.<a href="src/fern/user_ap_is/client.py">streamzip</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A zip file, containing the specified files and folders, will be generated on the fly and returned as response body. Only folders and regular files will be included in the zip
</dd>
</dl>
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
    username="<username>",
    password="<password>",
    sftpgo_api_key="<X-SFTPGO-API-KEY>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user_ap_is.streamzip(
    request=[
        "string",
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

