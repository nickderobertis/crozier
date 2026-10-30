# Reference
<details><summary><code>client.<a href="src/fern/client.py">posts_the_users_review_to_stellastra</a>(...) -> PostPostReviewResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.posts_the_users_review_to_stellastra(
    user_email="user_email",
    rating=1,
    post_post_review_request_rating=5,
    post_post_review_request_user_email="johnsmith@usercompanyxyz.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_email:** `str` — User's email to which the review verification will be sent. 
    
</dd>
</dl>

<dl>
<dd>

**rating:** `int` — The user's star rating, must be a single integer from [1, 2, 3, 4, 5]
    
</dd>
</dl>

<dl>
<dd>

**post_post_review_request_rating:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**post_post_review_request_user_email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**user_name:** `typing.Optional[str]` — The user's name, defaults to empty string "".  Thus, if this is omitted, the email to the user will not use the user's name. 
    
</dd>
</dl>

<dl>
<dd>

**post_post_review_request_user_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

