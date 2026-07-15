# Reference
## account
<details><summary><code>client.account.<a href="src/fern/account/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get currently logged in user data as JSON object.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.get()

```
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

<details><summary><code>client.account.<a href="src/fern/account/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use this endpoint to allow a new user to register a new account in your project. After the user registration completes successfully, you can use the [/account/verfication](/docs/client/account#accountCreateVerification) route to start verifying the user email address. To allow the new user to login to their new account, you need to create a new [account session](/docs/client/account#accountCreateSession).
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.create(
    email="email",
    password="password",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — User email.
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — User password. Must be between 6 to 32 chars.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — User name. Max length: 128 chars.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account.<a href="src/fern/account/client.py">delete</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a currently logged in user account. Behind the scene, the user record is not deleted but permanently blocked from any access. This is done to avoid deleted accounts being overtaken by new users with the same email address. Any user-related resources like documents or storage files should be deleted separately.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.delete()

```
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

<details><summary><code>client.account.<a href="src/fern/account/client.py">update_email</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update currently logged in user account email address. After changing user address, user confirmation status is being reset and a new confirmation mail is sent. For security measures, user password is required to complete this request.
This endpoint can also be used to convert an anonymous account to a normal one, by passing an email address and a new password.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.update_email(
    email="email",
    password="password",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — User email.
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — User password. Must be between 6 to 32 chars.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account.<a href="src/fern/account/client.py">account_create_jwt</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use this endpoint to create a JSON Web Token. You can use the resulting JWT to authenticate on behalf of the current user when working with the Appwrite server-side API and SDKs. The JWT secret is valid for 15 minutes from its creation and will be invalid if the user will logout in that time frame.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.account_create_jwt()

```
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

<details><summary><code>client.account.<a href="src/fern/account/client.py">get_logs</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get currently logged in user list of latest security activity logs. Each log returns user IP address, location and date and time of log.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.get_logs()

```
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

<details><summary><code>client.account.<a href="src/fern/account/client.py">update_name</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update currently logged in user account name.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.update_name(
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

**name:** `str` — User name. Max length: 128 chars.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account.<a href="src/fern/account/client.py">update_password</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update currently logged in user password. For validation, user is required to pass in the new password, and the old password. For users created with OAuth and Team Invites, oldPassword is optional.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.update_password(
    password="password",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**password:** `str` — New user password. Must be between 6 to 32 chars.
    
</dd>
</dl>

<dl>
<dd>

**old_password:** `typing.Optional[str]` — Old user password. Must be between 6 to 32 chars.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account.<a href="src/fern/account/client.py">get_prefs</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get currently logged in user preferences as a key-value object.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.get_prefs()

```
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

<details><summary><code>client.account.<a href="src/fern/account/client.py">update_prefs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update currently logged in user account preferences. You can pass only the specific settings you wish to update.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.update_prefs(
    prefs={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prefs:** `typing.Dict[str, typing.Optional[typing.Any]]` — Prefs key-value JSON object.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account.<a href="src/fern/account/client.py">create_recovery</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sends the user an email with a temporary secret key for password reset. When the user clicks the confirmation link he is redirected back to your app password reset URL with the secret key and email address values attached to the URL query string. Use the query string params to submit a request to the [PUT /account/recovery](/docs/client/account#accountUpdateRecovery) endpoint to complete the process. The verification link sent to the user's email address is valid for 1 hour.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.create_recovery(
    email="email",
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — User email.
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — URL to redirect the user back to your app from the recovery email. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account.<a href="src/fern/account/client.py">update_recovery</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use this endpoint to complete the user account password reset. Both the **userId** and **secret** arguments will be passed as query parameters to the redirect URL you have provided when sending your request to the [POST /account/recovery](/docs/client/account#accountCreateRecovery) endpoint.

Please note that in order to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) the only valid redirect URLs are the ones from domains you have set when adding your platforms in the console interface.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.update_recovery(
    password="password",
    password_again="passwordAgain",
    secret="secret",
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**password:** `str` — New password. Must be between 6 to 32 chars.
    
</dd>
</dl>

<dl>
<dd>

**password_again:** `str` — New password again. Must be between 6 to 32 chars.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `str` — Valid reset token.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — User account UID address.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account.<a href="src/fern/account/client.py">get_sessions</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get currently logged in user list of active sessions across different devices.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.get_sessions()

```
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

<details><summary><code>client.account.<a href="src/fern/account/client.py">create_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allow the user to login into their account by providing a valid email and password combination. This route will create a new session for the user.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.create_session(
    email="email",
    password="password",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — User email.
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — User password. Must be between 6 to 32 chars.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account.<a href="src/fern/account/client.py">delete_sessions</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete all sessions from the user account and remove any sessions cookies from the end client.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.delete_sessions()

```
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

<details><summary><code>client.account.<a href="src/fern/account/client.py">create_anonymous_session</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use this endpoint to allow a new user to register an anonymous account in your project. This route will also create a new session for the user. To allow the new user to convert an anonymous account to a normal account, you need to update its [email and password](/docs/client/account#accountUpdateEmail) or create an [OAuth2 session](/docs/client/account#accountCreateOAuth2Session).
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.create_anonymous_session()

```
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

<details><summary><code>client.account.<a href="src/fern/account/client.py">account_create_o_auth2session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allow the user to login to their account using the OAuth2 provider of their choice. Each OAuth2 provider should be enabled from the Appwrite console first. Use the success and failure arguments to provide a redirect URL's back to your app when login is completed.

If there is already an active session, the new session will be attached to the logged-in account. If there are no active sessions, the server will attempt to look for a user with the same email address as the email received from the OAuth2 provider and attach the new session to the existing user. If no matching user is found - the server will create a new user..
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.account_create_o_auth2session(
    provider="provider",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider:** `str` — OAuth2 Provider. Currently, supported providers are: amazon, apple, bitbucket, bitly, box, discord, dropbox, facebook, github, gitlab, google, linkedin, microsoft, paypal, paypalSandbox, salesforce, slack, spotify, tradeshift, tradeshiftBox, twitch, vk, yahoo, yandex, wordpress.
    
</dd>
</dl>

<dl>
<dd>

**success:** `typing.Optional[str]` — URL to redirect back to your app after a successful login attempt.  Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
    
</dd>
</dl>

<dl>
<dd>

**failure:** `typing.Optional[str]` — URL to redirect back to your app after a failed login attempt.  Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of custom OAuth2 scopes. Check each provider internal docs for a list of supported scopes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account.<a href="src/fern/account/client.py">get_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use this endpoint to get a logged in user's session using a Session ID. Inputting 'current' will return the current session being used.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.get_session(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — Session unique ID. Use the string 'current' to get the current device session.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account.<a href="src/fern/account/client.py">delete_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use this endpoint to log out the currently logged in user from all their account sessions across all of their different devices. When using the option id argument, only the session unique ID provider will be deleted.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.delete_session(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — Session unique ID. Use the string 'current' to delete the current device session.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account.<a href="src/fern/account/client.py">create_verification</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use this endpoint to send a verification message to your user email address to confirm they are the valid owners of that address. Both the **userId** and **secret** arguments will be passed as query parameters to the URL you have provided to be attached to the verification email. The provided URL should redirect the user back to your app and allow you to complete the verification process by verifying both the **userId** and **secret** parameters. Learn more about how to [complete the verification process](/docs/client/account#accountUpdateVerification). The verification link sent to the user's email address is valid for 7 days.

Please note that in order to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md), the only valid redirect URLs are the ones from domains you have set when adding your platforms in the console interface.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.create_verification(
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url:** `str` — URL to redirect the user back to your app from the verification email. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account.<a href="src/fern/account/client.py">update_verification</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use this endpoint to complete the user email verification process. Use both the **userId** and **secret** parameters that were attached to your app URL to verify the user email ownership. If confirmed this route will return a 200 status code.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.account.update_verification(
    secret="secret",
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**secret:** `str` — Valid verification token.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — User unique ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## avatars
<details><summary><code>client.avatars.<a href="src/fern/avatars/client.py">get_browser</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can use this endpoint to show different browser icons to your users. The code argument receives the browser code as it appears in your user /account/sessions endpoint. Use width, height and quality arguments to change the output settings.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.avatars.get_browser(
    code="code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**code:** `str` — Browser Code.
    
</dd>
</dl>

<dl>
<dd>

**width:** `typing.Optional[int]` — Image width. Pass an integer between 0 to 2000. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**height:** `typing.Optional[int]` — Image height. Pass an integer between 0 to 2000. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` — Image quality. Pass an integer between 0 to 100. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.avatars.<a href="src/fern/avatars/client.py">get_credit_card</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The credit card endpoint will return you the icon of the credit card provider you need. Use width, height and quality arguments to change the output settings.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.avatars.get_credit_card(
    code="code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**code:** `str` — Credit Card Code. Possible values: amex, argencard, cabal, censosud, diners, discover, elo, hipercard, jcb, mastercard, naranja, targeta-shopping, union-china-pay, visa, mir, maestro.
    
</dd>
</dl>

<dl>
<dd>

**width:** `typing.Optional[int]` — Image width. Pass an integer between 0 to 2000. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**height:** `typing.Optional[int]` — Image height. Pass an integer between 0 to 2000. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` — Image quality. Pass an integer between 0 to 100. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.avatars.<a href="src/fern/avatars/client.py">get_favicon</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use this endpoint to fetch the favorite icon (AKA favicon) of any remote website URL.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.avatars.get_favicon(
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url:** `str` — Website URL which you want to fetch the favicon from.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.avatars.<a href="src/fern/avatars/client.py">get_flag</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can use this endpoint to show different country flags icons to your users. The code argument receives the 2 letter country code. Use width, height and quality arguments to change the output settings.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.avatars.get_flag(
    code="code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**code:** `str` — Country Code. ISO Alpha-2 country code format.
    
</dd>
</dl>

<dl>
<dd>

**width:** `typing.Optional[int]` — Image width. Pass an integer between 0 to 2000. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**height:** `typing.Optional[int]` — Image height. Pass an integer between 0 to 2000. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` — Image quality. Pass an integer between 0 to 100. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.avatars.<a href="src/fern/avatars/client.py">get_image</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use this endpoint to fetch a remote image URL and crop it to any image size you want. This endpoint is very useful if you need to crop and display remote images in your app or in case you want to make sure a 3rd party image is properly served using a TLS protocol.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.avatars.get_image(
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url:** `str` — Image URL which you want to crop.
    
</dd>
</dl>

<dl>
<dd>

**width:** `typing.Optional[int]` — Resize preview image width, Pass an integer between 0 to 2000.
    
</dd>
</dl>

<dl>
<dd>

**height:** `typing.Optional[int]` — Resize preview image height, Pass an integer between 0 to 2000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.avatars.<a href="src/fern/avatars/client.py">get_initials</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use this endpoint to show your user initials avatar icon on your website or app. By default, this route will try to print your logged-in user name or email initials. You can also overwrite the user name if you pass the 'name' parameter. If no name is given and no user is logged, an empty avatar will be returned.

You can use the color and background params to change the avatar colors. By default, a random theme will be selected. The random theme will persist for the user's initials when reloading the same theme will always return for the same initials.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.avatars.get_initials()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` — Full Name. When empty, current user name or email will be used. Max length: 128 chars.
    
</dd>
</dl>

<dl>
<dd>

**width:** `typing.Optional[int]` — Image width. Pass an integer between 0 to 2000. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**height:** `typing.Optional[int]` — Image height. Pass an integer between 0 to 2000. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**color:** `typing.Optional[str]` — Changes text color. By default a random color will be picked and stay will persistent to the given name.
    
</dd>
</dl>

<dl>
<dd>

**background:** `typing.Optional[str]` — Changes background color. By default a random color will be picked and stay will persistent to the given name.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.avatars.<a href="src/fern/avatars/client.py">avatars_get_qr</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Converts a given plain text to a QR code image. You can use the query parameters to change the size and style of the resulting image.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.avatars.avatars_get_qr(
    text="text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text:** `str` — Plain text to be converted to QR code image.
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — QR code size. Pass an integer between 0 to 1000. Defaults to 400.
    
</dd>
</dl>

<dl>
<dd>

**margin:** `typing.Optional[int]` — Margin from edge. Pass an integer between 0 to 10. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**download:** `typing.Optional[bool]` — Return resulting image with 'Content-Disposition: attachment ' headers for the browser to start downloading it. Pass 0 for no header, or 1 for otherwise. Default value is set to 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## database
<details><summary><code>client.database.<a href="src/fern/database/client.py">list_documents</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all the user documents. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's documents. [Learn more about different API modes](/docs/admin).
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.database.list_documents(
    collection_id="collectionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Array of filter strings. Each filter is constructed from a key name, comparison operator (=, !=, >, <, <=, >=) and a value. You can also use a dot (.) separator in attribute names to filter by child document attributes. Examples: 'name=John Doe' or 'category.$id>=5bed2d152c362'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of documents to return in response.  Use this value to manage pagination. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset value. The default value is 0. Use this param to manage pagination.
    
</dd>
</dl>

<dl>
<dd>

**order_field:** `typing.Optional[str]` — Document field that results will be sorted by.
    
</dd>
</dl>

<dl>
<dd>

**order_type:** `typing.Optional[str]` — Order direction. Possible values are DESC for descending order, or ASC for ascending order.
    
</dd>
</dl>

<dl>
<dd>

**order_cast:** `typing.Optional[str]` — Order field type casting. Possible values are int, string, date, time or datetime. The database will attempt to cast the order field to the value you pass here. The default value is a string.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search query. Enter any free text search. The database will try to find a match against all document attributes and children. Max length: 256 chars.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.database.<a href="src/fern/database/client.py">create_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Document. Before using this route, you should create a new collection resource using either a [server integration](/docs/server/database#databaseCreateCollection) API or directly from your database console.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.database.create_document(
    collection_id="collectionId",
    data={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Dict[str, typing.Optional[typing.Any]]` — Document data as JSON object.
    
</dd>
</dl>

<dl>
<dd>

**parent_document:** `typing.Optional[str]` — Parent document unique ID. Use when you want your new document to be a child of a parent document.
    
</dd>
</dl>

<dl>
<dd>

**parent_property:** `typing.Optional[str]` — Parent document property name. Use when you want your new document to be a child of a parent document.
    
</dd>
</dl>

<dl>
<dd>

**parent_property_type:** `typing.Optional[str]` — Parent document property connection type. You can set this value to **assign**, **append** or **prepend**, default value is assign. Use when you want your new document to be a child of a parent document.
    
</dd>
</dl>

<dl>
<dd>

**read:** `typing.Optional[typing.Sequence[str]]` — An array of strings with read permissions. By default only the current user is granted with read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.
    
</dd>
</dl>

<dl>
<dd>

**write:** `typing.Optional[typing.Sequence[str]]` — An array of strings with write permissions. By default only the current user is granted with write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.database.<a href="src/fern/database/client.py">get_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a document by its unique ID. This endpoint response returns a JSON object with the document data.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.database.get_document(
    collection_id="collectionId",
    document_id="documentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` — Document unique ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.database.<a href="src/fern/database/client.py">delete_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a document by its unique ID. This endpoint deletes only the parent documents, its attributes and relations to other documents. Child documents **will not** be deleted.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.database.delete_document(
    collection_id="collectionId",
    document_id="documentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` — Document unique ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.database.<a href="src/fern/database/client.py">update_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a document by its unique ID. Using the patch method you can pass only specific fields that will get updated.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.database.update_document(
    collection_id="collectionId",
    document_id="documentId",
    data={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` — Document unique ID.
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Dict[str, typing.Optional[typing.Any]]` — Document data as JSON object.
    
</dd>
</dl>

<dl>
<dd>

**read:** `typing.Optional[typing.Sequence[str]]` — An array of strings with read permissions. By default inherits the existing read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.
    
</dd>
</dl>

<dl>
<dd>

**write:** `typing.Optional[typing.Sequence[str]]` — An array of strings with write permissions. By default inherits the existing write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## functions
<details><summary><code>client.functions.<a href="src/fern/functions/client.py">list_executions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all the current user function execution logs. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's executions. [Learn more about different API modes](/docs/admin).
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.functions.list_executions(
    function_id="functionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**function_id:** `str` — Function unique ID.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search term to filter your list results. Max length: 256 chars.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Results offset. The default value is 0. Use this param to manage pagination.
    
</dd>
</dl>

<dl>
<dd>

**order_type:** `typing.Optional[str]` — Order result by ASC or DESC order.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.functions.<a href="src/fern/functions/client.py">create_execution</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Trigger a function execution. The returned object will return you the current execution status. You can ping the `Get Execution` endpoint to get updates on the current execution status. Once this endpoint is called, your function execution process will start asynchronously.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.functions.create_execution(
    function_id="functionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**function_id:** `str` — Function unique ID.
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Optional[str]` — String of custom data to send to function.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.functions.<a href="src/fern/functions/client.py">get_execution</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a function execution log by its unique ID.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.functions.get_execution(
    function_id="functionId",
    execution_id="executionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**function_id:** `str` — Function unique ID.
    
</dd>
</dl>

<dl>
<dd>

**execution_id:** `str` — Execution unique ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## locale
<details><summary><code>client.locale.<a href="src/fern/locale/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the current user location based on IP. Returns an object with user country code, country name, continent name, continent code, ip address and suggested currency. You can use the locale header to get the data in a supported language.

([IP Geolocation by DB-IP](https://db-ip.com))
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.locale.get()

```
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

<details><summary><code>client.locale.<a href="src/fern/locale/client.py">get_continents</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all continents. You can use the locale header to get the data in a supported language.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.locale.get_continents()

```
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

<details><summary><code>client.locale.<a href="src/fern/locale/client.py">get_countries</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all countries. You can use the locale header to get the data in a supported language.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.locale.get_countries()

```
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

<details><summary><code>client.locale.<a href="src/fern/locale/client.py">locale_get_countries_eu</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all countries that are currently members of the EU. You can use the locale header to get the data in a supported language.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.locale.locale_get_countries_eu()

```
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

<details><summary><code>client.locale.<a href="src/fern/locale/client.py">get_countries_phones</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all countries phone codes. You can use the locale header to get the data in a supported language.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.locale.get_countries_phones()

```
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

<details><summary><code>client.locale.<a href="src/fern/locale/client.py">get_currencies</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all currencies, including currency symbol, name, plural, and decimal digits for all major and minor currencies. You can use the locale header to get the data in a supported language.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.locale.get_currencies()

```
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

<details><summary><code>client.locale.<a href="src/fern/locale/client.py">get_languages</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all languages classified by ISO 639-1 including 2-letter code, name in English, and name in the respective language.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.locale.get_languages()

```
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

## storage
<details><summary><code>client.storage.<a href="src/fern/storage/client.py">list_files</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all the user files. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's files. [Learn more about different API modes](/docs/admin).
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.storage.list_files()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search term to filter your list results. Max length: 256 chars.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Results offset. The default value is 0. Use this param to manage pagination.
    
</dd>
</dl>

<dl>
<dd>

**order_type:** `typing.Optional[str]` — Order result by ASC or DESC order.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.storage.<a href="src/fern/storage/client.py">create_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new file. The user who creates the file will automatically be assigned to read and write access unless he has passed custom values for read and write arguments.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.storage.create_file(
    file="file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `str` — Binary file.
    
</dd>
</dl>

<dl>
<dd>

**read:** `typing.Optional[typing.List[str]]` — An array of strings with read permissions. By default only the current user is granted with read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.
    
</dd>
</dl>

<dl>
<dd>

**write:** `typing.Optional[typing.List[str]]` — An array of strings with write permissions. By default only the current user is granted with write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.storage.<a href="src/fern/storage/client.py">get_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a file by its unique ID. This endpoint response returns a JSON object with the file metadata.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.storage.get_file(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — File unique ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.storage.<a href="src/fern/storage/client.py">update_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a file by its unique ID. Only users with write permissions have access to update this resource.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.storage.update_file(
    file_id="fileId",
    read=["read"],
    write=["write"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — File unique ID.
    
</dd>
</dl>

<dl>
<dd>

**read:** `typing.Sequence[str]` — An array of strings with read permissions. By default no user is granted with any read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.
    
</dd>
</dl>

<dl>
<dd>

**write:** `typing.Sequence[str]` — An array of strings with write permissions. By default no user is granted with any write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.storage.<a href="src/fern/storage/client.py">delete_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a file by its unique ID. Only users with write permissions have access to delete this resource.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.storage.delete_file(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — File unique ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.storage.<a href="src/fern/storage/client.py">get_file_download</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a file content by its unique ID. The endpoint response return with a 'Content-Disposition: attachment' header that tells the browser to start downloading the file to user downloads directory.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.storage.get_file_download(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — File unique ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.storage.<a href="src/fern/storage/client.py">get_file_preview</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a file preview image. Currently, this method supports preview for image files (jpg, png, and gif), other supported formats, like pdf, docs, slides, and spreadsheets, will return the file icon image. You can also pass query string arguments for cutting and resizing your preview image.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.storage.get_file_preview(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — File unique ID
    
</dd>
</dl>

<dl>
<dd>

**width:** `typing.Optional[int]` — Resize preview image width, Pass an integer between 0 to 4000.
    
</dd>
</dl>

<dl>
<dd>

**height:** `typing.Optional[int]` — Resize preview image height, Pass an integer between 0 to 4000.
    
</dd>
</dl>

<dl>
<dd>

**gravity:** `typing.Optional[str]` — Image crop gravity. Can be one of center,top-left,top,top-right,left,right,bottom-left,bottom,bottom-right
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` — Preview image quality. Pass an integer between 0 to 100. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**border_width:** `typing.Optional[int]` — Preview image border in pixels. Pass an integer between 0 to 100. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**border_color:** `typing.Optional[str]` — Preview image border color. Use a valid HEX color, no # is needed for prefix.
    
</dd>
</dl>

<dl>
<dd>

**border_radius:** `typing.Optional[int]` — Preview image border radius in pixels. Pass an integer between 0 to 4000.
    
</dd>
</dl>

<dl>
<dd>

**opacity:** `typing.Optional[float]` — Preview image opacity. Only works with images having an alpha channel (like png). Pass a number between 0 to 1.
    
</dd>
</dl>

<dl>
<dd>

**rotation:** `typing.Optional[int]` — Preview image rotation in degrees. Pass an integer between 0 and 360.
    
</dd>
</dl>

<dl>
<dd>

**background:** `typing.Optional[str]` — Preview image background color. Only works with transparent images (png). Use a valid HEX color, no # is needed for prefix.
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` — Output format type (jpeg, jpg, png, gif and webp).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.storage.<a href="src/fern/storage/client.py">get_file_view</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a file content by its unique ID. This endpoint is similar to the download method but returns with no  'Content-Disposition: attachment' header.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.storage.get_file_view(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — File unique ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## teams
<details><summary><code>client.teams.<a href="src/fern/teams/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all the current user teams. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's teams. [Learn more about different API modes](/docs/admin).
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.teams.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search term to filter your list results. Max length: 256 chars.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Results offset. The default value is 0. Use this param to manage pagination.
    
</dd>
</dl>

<dl>
<dd>

**order_type:** `typing.Optional[str]` — Order result by ASC or DESC order.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new team. The user who creates the team will automatically be assigned as the owner of the team. The team owner can invite new members, who will be able add new owners and update or delete the team from your project.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.teams.create(
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

**name:** `str` — Team name. Max length: 128 chars.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.Sequence[str]]` — Array of strings. Use this param to set the roles in the team for the user who created it. The default role is **owner**. A role can be any string. Learn more about [roles and permissions](/docs/permissions). Max length for each role is 32 chars.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a team by its unique ID. All team members have read access for this resource.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.teams.get(
    team_id="teamId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — Team unique ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a team by its unique ID. Only team owners have write access for this resource.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.teams.update(
    team_id="teamId",
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

**team_id:** `str` — Team unique ID.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Team name. Max length: 128 chars.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a team by its unique ID. Only team owners have write access for this resource.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.teams.delete(
    team_id="teamId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — Team unique ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">get_memberships</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a team members by the team unique ID. All team members have read access for this list of resources.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.teams.get_memberships(
    team_id="teamId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — Team unique ID.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search term to filter your list results. Max length: 256 chars.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Results offset. The default value is 0. Use this param to manage pagination.
    
</dd>
</dl>

<dl>
<dd>

**order_type:** `typing.Optional[str]` — Order result by ASC or DESC order.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">create_membership</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use this endpoint to invite a new member to join your team. If initiated from Client SDK, an email with a link to join the team will be sent to the new member's email address if the member doesn't exist in the project it will be created automatically. If initiated from server side SDKs, new member will automatically be added to the team.

Use the 'URL' parameter to redirect the user from the invitation email back to your app. When the user is redirected, use the [Update Team Membership Status](/docs/client/teams#teamsUpdateMembershipStatus) endpoint to allow the user to accept the invitation to the team.  While calling from side SDKs the redirect url can be empty string.

Please note that in order to avoid a [Redirect Attacks](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) the only valid redirect URL's are the once from domains you have set when added your platforms in the console interface.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.teams.create_membership(
    team_id="teamId",
    email="email",
    roles=["roles"],
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — Team unique ID.
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — New team member email.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Sequence[str]` — Array of strings. Use this param to set the user roles in the team. A role can be any string. Learn more about [roles and permissions](/docs/permissions). Max length for each role is 32 chars.
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — URL to redirect the user back to your app from the invitation email.  Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — New team member name. Max length: 128 chars.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">delete_membership</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows a user to leave a team or for a team owner to delete the membership of any other team member. You can also use this endpoint to delete a user membership even if it is not accepted.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.teams.delete_membership(
    team_id="teamId",
    membership_id="membershipId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — Team unique ID.
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `str` — Membership ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">update_membership_roles</a>(...)</code></summary>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.teams.update_membership_roles(
    team_id="teamId",
    membership_id="membershipId",
    roles=["roles"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — Team unique ID.
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `str` — Membership ID.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Sequence[str]` — Array of strings. Use this param to set the user roles in the team. A role can be any string. Learn more about [roles and permissions](/docs/permissions). Max length for each role is 32 chars.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">update_membership_status</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use this endpoint to allow a user to accept an invitation to join a team after being redirected back to your app from the invitation email recieved by the user.
</dd>
</dl>
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
    appwrite_locale="YOUR_APPWRITE_LOCALE",
    appwrite_project="YOUR_APPWRITE_PROJECT",
    api_key="YOUR_API_KEY",
)
client.teams.update_membership_status(
    team_id="teamId",
    membership_id="membershipId",
    secret="secret",
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — Team unique ID.
    
</dd>
</dl>

<dl>
<dd>

**membership_id:** `str` — Membership ID.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `str` — Secret key.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — User unique ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

