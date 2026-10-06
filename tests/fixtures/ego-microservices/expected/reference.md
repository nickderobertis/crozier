# Reference
## Auth
<details><summary><code>client.auth.<a href="src/fern/auth/client.py">user_registration</a>(...) -> TokensResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Регистрация пользователя
</dd>
</dl>
</dd>
</dl>

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

client.auth.user_registration(
    username="username",
    password="password",
    user_email="user_email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `str` — Никнейм пользователя
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — Пароль пользователя
    
</dd>
</dl>

<dl>
<dd>

**user_email:** `str` — Почта пользователя
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">user_login</a>(...) -> TokensResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Вход пользователя и выдача токенов
</dd>
</dl>
</dd>
</dl>

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

client.auth.user_login(
    username="username",
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

**username:** `str` — Никнейм пользователя
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — Пароль пользователя
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">token_verify</a>(...) -> VerifyStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Проверка токена
</dd>
</dl>
</dd>
</dl>

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

client.auth.token_verify(
    authorization="Authorization",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — Enter the token with the 'Bearer:' prefix.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">token_refresh</a>(...) -> RefreshTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Обновление токена
</dd>
</dl>
</dd>
</dl>

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

client.auth.token_refresh(
    authorization="Authorization",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — Enter the token with the 'Bearer:' prefix.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.auth.<a href="src/fern/auth/client.py">update_user_data_auth_users_update_user_patch</a>(...) -> UpdateLoginUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Обнавление данных пользователя
</dd>
</dl>
</dd>
</dl>

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

client.auth.update_user_data_auth_users_update_user_patch(
    authorization="Authorization",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — Enter the token with the 'Bearer:' prefix.
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[UpdateLoginUserRequestPassword]` 
    
</dd>
</dl>

<dl>
<dd>

**user_email:** `typing.Optional[UpdateLoginUserRequestUserEmail]` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.users.<a href="src/fern/users/client.py">get_user</a>(...) -> UserDataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Получение данных о пользователе с помощью его id
</dd>
</dl>
</dd>
</dl>

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

client.users.get_user(
    user_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">create_user</a>(...) -> UserDataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Создание пользователя
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GenderValue
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.users.create_user(
    authorization="Authorization",
    first_name="first_name",
    last_name="last_name",
    gender=GenderValue.MALE,
    birthday=datetime.date.fromisoformat("2023-01-15"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — Enter the token with the 'Bearer:' prefix.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `str` — Имя пользователя
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `str` — Фамилия пользователя
    
</dd>
</dl>

<dl>
<dd>

**gender:** `GenderValue` — Пол пользователя
    
</dd>
</dl>

<dl>
<dd>

**birthday:** `datetime.date` — Дата рождения
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">update_user_info</a>(...) -> UserDataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Обновление данных пользователя
</dd>
</dl>
</dd>
</dl>

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

client.users.update_user_info(
    authorization="Authorization",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — Enter the token with the 'Bearer:' prefix.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[UpdateUserRequestFirstName]` — Имя
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[UpdateUserRequestLastName]` — Фамилия
    
</dd>
</dl>

<dl>
<dd>

**gender:** `typing.Optional[UpdateUserRequestGender]` — Пол
    
</dd>
</dl>

<dl>
<dd>

**birthday:** `typing.Optional[UpdateUserRequestBirthday]` — Дата
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">delete_user</a>(...) -> DeletedUserResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Удаление пользователя
</dd>
</dl>
</dd>
</dl>

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

client.users.delete_user(
    authorization="Authorization",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — Enter the token with the 'Bearer:' prefix.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Avatars
<details><summary><code>client.avatars.<a href="src/fern/avatars/client.py">set_avatar</a>(...) -> SetAvatarResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Установка аватарки у пользователя
</dd>
</dl>
</dd>
</dl>

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

client.avatars.set_avatar(
    authorization="Authorization",
    avatar_data="example_avatar_data",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — Enter the token with the 'Bearer:' prefix.
    
</dd>
</dl>

<dl>
<dd>

**avatar_data:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.avatars.<a href="src/fern/avatars/client.py">delete_avatar</a>(...) -> DeletedAvatarResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Удаление аватарки у пользователя
</dd>
</dl>
</dd>
</dl>

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

client.avatars.delete_avatar(
    authorization="Authorization",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — Enter the token with the 'Bearer:' prefix.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Subscription
<details><summary><code>client.subscription.<a href="src/fern/subscription/client.py">subscribe</a>(...) -> SubscribeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Оформление подписки
</dd>
</dl>
</dd>
</dl>

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

client.subscription.subscribe(
    authorization="Authorization",
    subscription_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — Enter the token with the 'Bearer:' prefix.
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `int` — Айди на кого подписка
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscription.<a href="src/fern/subscription/client.py">unsubscribe</a>(...) -> UnsubscribeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Отписка от пользователя
</dd>
</dl>
</dd>
</dl>

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

client.subscription.unsubscribe(
    authorization="Authorization",
    subscription_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — Enter the token with the 'Bearer:' prefix.
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `int` — Айди от кого отписка
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscription.<a href="src/fern/subscription/client.py">get_subscriptions</a>(...) -> SubscriptionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Получение подписчиков пользователя
</dd>
</dl>
</dd>
</dl>

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

client.subscription.get_subscriptions(
    user_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[GetSubscriptionsSubscriptionGetSubscriptionsGetRequestOffset]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[GetSubscriptionsSubscriptionGetSubscriptionsGetRequestLimit]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetSubscriptionsOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscription.<a href="src/fern/subscription/client.py">get_subscribers</a>(...) -> SubscribersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Получение подписчиков пользователя
</dd>
</dl>
</dd>
</dl>

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

client.subscription.get_subscribers(
    user_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[GetSubscribersSubscriptionGetSubscribersGetRequestOffset]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[GetSubscribersSubscriptionGetSubscribersGetRequestLimit]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetSubscriptionsOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Posts
<details><summary><code>client.posts.<a href="src/fern/posts/client.py">get_user_posts</a>(...) -> PostsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Получение всех постов пользователя
</dd>
</dl>
</dd>
</dl>

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

client.posts.get_user_posts(
    creator_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**creator_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[GetUserPostsPostsUserPostsGetRequestOffset]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[GetUserPostsPostsUserPostsGetRequestLimit]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetPostsOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.posts.<a href="src/fern/posts/client.py">full_text_posts_search</a>(...) -> PostsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Получение всех постов пользователя
</dd>
</dl>
</dd>
</dl>

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

client.posts.full_text_posts_search(
    query_string="query_string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query_string:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[FullTextPostsSearchPostsFullTextSearchGetRequestOffset]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[FullTextPostsSearchPostsFullTextSearchGetRequestLimit]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetPostsOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.posts.<a href="src/fern/posts/client.py">create_post</a>(...) -> PostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Создание поста
</dd>
</dl>
</dd>
</dl>

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

client.posts.create_post(
    authorization="Authorization",
    text_content="text_content",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — Enter the token with the 'Bearer:' prefix.
    
</dd>
</dl>

<dl>
<dd>

**text_content:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.posts.<a href="src/fern/posts/client.py">delete_post</a>(...) -> DeletedPostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Удание поста пользователя
</dd>
</dl>
</dd>
</dl>

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

client.posts.delete_post(
    authorization="Authorization",
    post_id="post_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — Enter the token with the 'Bearer:' prefix.
    
</dd>
</dl>

<dl>
<dd>

**post_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.posts.<a href="src/fern/posts/client.py">update_post</a>(...) -> PostResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Обнволение поста пользователя
</dd>
</dl>
</dd>
</dl>

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

client.posts.update_post(
    authorization="Authorization",
    post_id="post_id",
    text_content="text_content",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `str` — Enter the token with the 'Bearer:' prefix.
    
</dd>
</dl>

<dl>
<dd>

**post_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**text_content:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

