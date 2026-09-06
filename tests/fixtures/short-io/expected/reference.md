# Reference
## LinkQueries
<details><summary><code>client.link_queries.<a href="src/fern/link_queries/client.py">fetch_and_inspect_open_graph_tags_for_a_url_public_h_captcha_protected</a>(...) -> PostLinksOpengraphDebugResponse</code></summary>
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

client.link_queries.fetch_and_inspect_open_graph_tags_for_a_url_public_h_captcha_protected(
    hcaptcha_token="hcaptchaToken",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**hcaptcha_token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_queries.<a href="src/fern/link_queries/client.py">get_link_opengraph_properties</a>(...)</code></summary>
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

client.link_queries.get_link_opengraph_properties(
    domain_id=1.1,
    link_id="linkId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**link_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_queries.<a href="src/fern/link_queries/client.py">link_list</a>(...) -> GetApiLinksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get domain links
</dd>
</dl>
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

client.link_queries.link_list(
    domain_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_id:** `int` — Domain ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**id_string:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**before_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**after_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**date_sort_order:** `typing.Optional[GetApiLinksRequestDateSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_queries.<a href="src/fern/link_queries/client.py">get_link_info_by_link_id</a>(...) -> GetLinksLinkIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get link info by link id. Rate limit: 20/s
</dd>
</dl>
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

client.link_queries.get_link_info_by_link_id(
    link_id="linkId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_id:** `typing.Optional[str]` — [DEPRECATED] Domain ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_queries.<a href="src/fern/link_queries/client.py">get_link_info_by_path</a>(...) -> GetLinksExpandResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get link info by path. Rate limit: 20/s
</dd>
</dl>
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

client.link_queries.get_link_info_by_path(
    domain="domain",
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

**domain:** `str` — Domain hostname
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Link path
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_queries.<a href="src/fern/link_queries/client.py">get_link_info_by_original_url</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**DEPRECATED** Get link info by original URL. Rate limit: 20/s
</dd>
</dl>
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

client.link_queries.get_link_info_by_original_url(
    domain="domain",
    original_url="originalURL",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain:** `str` — Domain hostname
    
</dd>
</dl>

<dl>
<dd>

**original_url:** `str` — Link original URL
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_queries.<a href="src/fern/link_queries/client.py">get_links_info_by_original_url</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all links with the same original URL
</dd>
</dl>
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

client.link_queries.get_links_info_by_original_url(
    domain="domain",
    original_url="originalURL",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain:** `str` — Domain hostname
    
</dd>
</dl>

<dl>
<dd>

**original_url:** `str` — Link original URL
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_queries.<a href="src/fern/link_queries/client.py">get_links_folders_domain_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get links folders for the specified domain id
</dd>
</dl>
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

client.link_queries.get_links_folders_domain_id(
    domain_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_queries.<a href="src/fern/link_queries/client.py">get_links_folders_domain_id_folder_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get links folder for the specified domain id and user id
</dd>
</dl>
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

client.link_queries.get_links_folders_domain_id_folder_id(
    domain_id=1,
    folder_id="folderId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_queries.<a href="src/fern/link_queries/client.py">post_links_folders</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new folder
</dd>
</dl>
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

client.link_queries.post_links_folders(
    domain_id=1,
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

**domain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**color:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**background_color:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**logo_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**logo_height:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**logo_width:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**ec_level:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**border_radius:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**no_excavate:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**finder_outer_shape:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**finder_inner_shape:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**finder_color:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**corner_mode:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**label_text:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**label_style:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**label_color:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**label_bg_color:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**label_font_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**label_font_family:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**integration_fb:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**integration_tt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**integration_ga:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**integration_gtm:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**integration_adroll:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**utm_campaign:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**utm_medium:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**utm_source:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**utm_term:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**utm_content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**redirect_type:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**expires_at_days:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**icon:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## LinkManagement
<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">set_link_opengraph_properties</a>(...)</code></summary>
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

client.link_management.set_link_opengraph_properties(
    domain_id=1.1,
    link_id="linkId",
    request=[
        [],
        []
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

**domain_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**link_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[typing.List[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">get_link_permissions</a>(...) -> typing.List[GetLinksPermissionsDomainIdLinkIdResponseItem]</code></summary>
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

client.link_management.get_link_permissions(
    domain_id="domainId",
    link_id="linkId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**link_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">add_link_permission</a>(...) -> PostLinksPermissionsDomainIdLinkIdUserIdResponse</code></summary>
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

client.link_management.add_link_permission(
    domain_id="domainId",
    link_id="lnk_abc123_abcdef",
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

**domain_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**link_id:** `str` — Link ID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">delete_link_permissions</a>(...) -> DeleteLinksPermissionsDomainIdLinkIdUserIdResponse</code></summary>
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

client.link_management.delete_link_permissions(
    domain_id=1,
    link_id="linkId",
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

**domain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**link_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">generate_qr_code_for_the_link</a>(...)</code></summary>
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

client.link_management.generate_qr_code_for_the_link(
    link_id_string="lnk_abc123_abcdef",
    use_domain_settings=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_id_string:** `str` — Link ID
    
</dd>
</dl>

<dl>
<dd>

**use_domain_settings:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**accept:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**color:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**background_color:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[PostLinksQrLinkIdStringRequestType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">generate_qr_codes_for_the_link_in_bulk</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate QR codes for the link in bulk. Rate limit - 1 request per minute
</dd>
</dl>
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
from fern.link_management import PostLinksQrBulkRequestType

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.link_management.generate_qr_codes_for_the_link_in_bulk(
    type=PostLinksQrBulkRequestType.PNG,
    use_domain_settings=True,
    link_ids=[
        "linkIds"
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

**type:** `PostLinksQrBulkRequestType` 
    
</dd>
</dl>

<dl>
<dd>

**use_domain_settings:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**link_ids:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**color:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**background_color:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**no_excavate:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**domain_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">delete_link</a>(...) -> DeleteLinksLinkIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete link by id

**Rate limit**: 20/s
</dd>
</dl>
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

client.link_management.delete_link(
    link_id="lnk_abc123_abcdef",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_id:** `str` — Link ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">delete_links_in_bulk</a>(...) -> DeleteLinksDeleteBulkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete links in bulk by ids

**Rate limit**: 1/s
</dd>
</dl>
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

client.link_management.delete_links_in_bulk(
    link_ids=[
        "lnk_abc123_abcdef"
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

**link_ids:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">archive_link</a>(...) -> PostLinksArchiveResponse</code></summary>
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

client.link_management.archive_link(
    link_id="link_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">archive_links_in_bulk</a>(...) -> PostLinksArchiveBulkResponse</code></summary>
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

client.link_management.archive_links_in_bulk(
    link_ids=[
        "link_ids"
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

**link_ids:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**domain_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">unarchive_link</a>(...) -> PostLinksUnarchiveResponse</code></summary>
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

client.link_management.unarchive_link(
    link_id="link_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">unarchive_links_in_bulk</a>(...) -> PostLinksUnarchiveBulkResponse</code></summary>
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

client.link_management.unarchive_links_in_bulk(
    link_ids=[
        "link_ids"
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

**link_ids:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**domain_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">update_existing_url</a>(...) -> PostLinksLinkIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update original url, title or path for existing URL by id

**Rate limit**: 20/s
</dd>
</dl>
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

client.link_management.update_existing_url(
    link_id="linkId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cloaking:** `typing.Optional[bool]` — Cloaking
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Link password
    
</dd>
</dl>

<dl>
<dd>

**redirect_type:** `typing.Optional[int]` — HTTP code for redirect
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[PostLinksLinkIdRequestExpiresAt]` — Link expiration date in milliseconds or ISO string
    
</dd>
</dl>

<dl>
<dd>

**expired_url:** `typing.Optional[str]` — Expired URL
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Link title
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Array of link tags
    
</dd>
</dl>

<dl>
<dd>

**utm_source:** `typing.Optional[str]` — set utm_source parameter to destination link
    
</dd>
</dl>

<dl>
<dd>

**utm_medium:** `typing.Optional[str]` — set utm_medium parameter to destination link
    
</dd>
</dl>

<dl>
<dd>

**utm_campaign:** `typing.Optional[str]` — set utm_campaign parameter to destination link
    
</dd>
</dl>

<dl>
<dd>

**utm_term:** `typing.Optional[str]` — set utm_term parameter to destination link
    
</dd>
</dl>

<dl>
<dd>

**utm_content:** `typing.Optional[str]` — set utm_content parameter to destination link
    
</dd>
</dl>

<dl>
<dd>

**ttl:** `typing.Optional[PostLinksLinkIdRequestTtl]` — Time to live in milliseconds or ISO string
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` — Link slug. For case-insensitive domains, the path is normalized to lowercase and the original value is preserved in displayPath.
    
</dd>
</dl>

<dl>
<dd>

**android_url:** `typing.Optional[str]` — Android URL
    
</dd>
</dl>

<dl>
<dd>

**iphone_url:** `typing.Optional[str]` — iPhone URL
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[PostLinksLinkIdRequestCreatedAt]` — Link creation date in milliseconds
    
</dd>
</dl>

<dl>
<dd>

**clicks_limit:** `typing.Optional[int]` — disable link after specified number of clicks
    
</dd>
</dl>

<dl>
<dd>

**password_contact:** `typing.Optional[bool]` — Provide your email to users to get a password
    
</dd>
</dl>

<dl>
<dd>

**skip_qs:** `typing.Optional[bool]` — Skip query string merging
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — Link is archived
    
</dd>
</dl>

<dl>
<dd>

**split_url:** `typing.Optional[str]` — Split URL
    
</dd>
</dl>

<dl>
<dd>

**split_percent:** `typing.Optional[int]` — Split URL percentage
    
</dd>
</dl>

<dl>
<dd>

**split_urlv2:** `typing.Optional[typing.List[PostLinksLinkIdRequestSplitUrlv2Item]]` — Split URL configurations for multi-way A/B testing
    
</dd>
</dl>

<dl>
<dd>

**integration_adroll:** `typing.Optional[str]` — Adroll integration
    
</dd>
</dl>

<dl>
<dd>

**integration_fb:** `typing.Optional[str]` — Facebook integration
    
</dd>
</dl>

<dl>
<dd>

**integration_tt:** `typing.Optional[str]` — TikTok integration
    
</dd>
</dl>

<dl>
<dd>

**integration_ga:** `typing.Optional[str]` — Google Analytics integration
    
</dd>
</dl>

<dl>
<dd>

**integration_gtm:** `typing.Optional[str]` — Google Tag Manager integration
    
</dd>
</dl>

<dl>
<dd>

**original_url:** `typing.Optional[str]` — Original URL
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">create_a_new_link</a>(...) -> PostLinksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This method creates a new link. If parameter "path" is omitted, it
generates path by algorithm, chosen in domain settings.

Notes:

1. If URL with a given path already exists and originalURL of the URL in database is equal to originalURL argument, it returns information about existing URL
2. If URL with a given path already exists and originalURL is different from originalURL in database, it returns error with a status `409`
3. If URL with a given originalURL exists, and no path is given, it returns information about existing URL and does not create anything
4. If URL with a given originalURL exists, and custom path is given, it creates a new short URL

**Rate limit**: 50/s
</dd>
</dl>
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

client.link_management.create_a_new_link(
    original_url="https://example.com",
    domain="domain",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**original_url:** `str` — Original URL
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` — Domain hostname
    
</dd>
</dl>

<dl>
<dd>

**cloaking:** `typing.Optional[bool]` — Cloaking
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Link password
    
</dd>
</dl>

<dl>
<dd>

**redirect_type:** `typing.Optional[int]` — HTTP code for redirect
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[PostLinksRequestExpiresAt]` — Link expiration date in milliseconds or ISO string
    
</dd>
</dl>

<dl>
<dd>

**expired_url:** `typing.Optional[str]` — Expired URL
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Link title
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Array of link tags
    
</dd>
</dl>

<dl>
<dd>

**utm_source:** `typing.Optional[str]` — set utm_source parameter to destination link
    
</dd>
</dl>

<dl>
<dd>

**utm_medium:** `typing.Optional[str]` — set utm_medium parameter to destination link
    
</dd>
</dl>

<dl>
<dd>

**utm_campaign:** `typing.Optional[str]` — set utm_campaign parameter to destination link
    
</dd>
</dl>

<dl>
<dd>

**utm_term:** `typing.Optional[str]` — set utm_term parameter to destination link
    
</dd>
</dl>

<dl>
<dd>

**utm_content:** `typing.Optional[str]` — set utm_content parameter to destination link
    
</dd>
</dl>

<dl>
<dd>

**ttl:** `typing.Optional[PostLinksRequestTtl]` — Time to live in milliseconds or ISO string
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` — Link slug. For case-insensitive domains, the path is normalized to lowercase and the original value is preserved in displayPath.
    
</dd>
</dl>

<dl>
<dd>

**android_url:** `typing.Optional[str]` — Android URL
    
</dd>
</dl>

<dl>
<dd>

**iphone_url:** `typing.Optional[str]` — iPhone URL
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[PostLinksRequestCreatedAt]` — Link creation date in milliseconds
    
</dd>
</dl>

<dl>
<dd>

**clicks_limit:** `typing.Optional[int]` — disable link after specified number of clicks
    
</dd>
</dl>

<dl>
<dd>

**password_contact:** `typing.Optional[bool]` — Provide your email to users to get a password
    
</dd>
</dl>

<dl>
<dd>

**post_links_request_skip_qs:** `typing.Optional[bool]` — Skip query string merging
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — Link is archived
    
</dd>
</dl>

<dl>
<dd>

**split_url:** `typing.Optional[str]` — Split URL
    
</dd>
</dl>

<dl>
<dd>

**split_percent:** `typing.Optional[int]` — Split URL percentage
    
</dd>
</dl>

<dl>
<dd>

**split_urlv2:** `typing.Optional[typing.List[PostLinksRequestSplitUrlv2Item]]` — Split URL configurations for multi-way A/B testing
    
</dd>
</dl>

<dl>
<dd>

**integration_adroll:** `typing.Optional[str]` — Adroll integration
    
</dd>
</dl>

<dl>
<dd>

**integration_fb:** `typing.Optional[str]` — Facebook integration
    
</dd>
</dl>

<dl>
<dd>

**integration_tt:** `typing.Optional[str]` — TikTok integration
    
</dd>
</dl>

<dl>
<dd>

**integration_ga:** `typing.Optional[str]` — Google Analytics integration
    
</dd>
</dl>

<dl>
<dd>

**integration_gtm:** `typing.Optional[str]` — Google Tag Manager integration
    
</dd>
</dl>

<dl>
<dd>

**allow_duplicates:** `typing.Optional[bool]` — Allow duplicates
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` — Folder ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">create_a_new_link_simple_version</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


                    Simple version of link create endpoint. You can use it if you can not use POST method
                    **Rate limit**: 50/s
                
</dd>
</dl>
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

client.link_management.create_a_new_link_simple_version(
    domain="domain",
    original_url="originalURL",
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain:** `str` — Domain hostname
    
</dd>
</dl>

<dl>
<dd>

**original_url:** `str` — Link original URL
    
</dd>
</dl>

<dl>
<dd>

**api_key:** `str` — API key
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` — Link path
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Link title
    
</dd>
</dl>

<dl>
<dd>

**url_only:** `typing.Optional[GetLinksTweetbotRequestUrlOnly]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">create_a_new_link_using_public_api_key</a>(...) -> PostLinksPublicResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This method creates a new link. Only this method should be used in client-side applications

If parameter "path" is omitted, it generates path by algorithm, chosen in domain settings.

You can use it with public API key in your frontend applications (client-side javascript, Android & iPhone apps)
**Rate limit**: 50/s
</dd>
</dl>
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

client.link_management.create_a_new_link_using_public_api_key(
    original_url="https://example.com",
    domain="domain",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**original_url:** `str` — Original URL
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**additional_properties:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cloaking:** `typing.Optional[bool]` — Cloaking
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Link password
    
</dd>
</dl>

<dl>
<dd>

**redirect_type:** `typing.Optional[int]` — HTTP code for redirect
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[PostLinksPublicRequestExpiresAt]` — Link expiration date in milliseconds or ISO string
    
</dd>
</dl>

<dl>
<dd>

**expired_url:** `typing.Optional[str]` — Expired URL
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Link title
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Array of link tags
    
</dd>
</dl>

<dl>
<dd>

**utm_source:** `typing.Optional[str]` — set utm_source parameter to destination link
    
</dd>
</dl>

<dl>
<dd>

**utm_medium:** `typing.Optional[str]` — set utm_medium parameter to destination link
    
</dd>
</dl>

<dl>
<dd>

**utm_campaign:** `typing.Optional[str]` — set utm_campaign parameter to destination link
    
</dd>
</dl>

<dl>
<dd>

**utm_term:** `typing.Optional[str]` — set utm_term parameter to destination link
    
</dd>
</dl>

<dl>
<dd>

**utm_content:** `typing.Optional[str]` — set utm_content parameter to destination link
    
</dd>
</dl>

<dl>
<dd>

**ttl:** `typing.Optional[PostLinksPublicRequestTtl]` — Time to live in milliseconds or ISO string
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` — Link slug. For case-insensitive domains, the path is normalized to lowercase and the original value is preserved in displayPath.
    
</dd>
</dl>

<dl>
<dd>

**android_url:** `typing.Optional[str]` — Android URL
    
</dd>
</dl>

<dl>
<dd>

**iphone_url:** `typing.Optional[str]` — iPhone URL
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[PostLinksPublicRequestCreatedAt]` — Link creation date in milliseconds
    
</dd>
</dl>

<dl>
<dd>

**clicks_limit:** `typing.Optional[int]` — disable link after specified number of clicks
    
</dd>
</dl>

<dl>
<dd>

**password_contact:** `typing.Optional[bool]` — Provide your email to users to get a password
    
</dd>
</dl>

<dl>
<dd>

**skip_qs:** `typing.Optional[bool]` — Skip query string merging
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — Link is archived
    
</dd>
</dl>

<dl>
<dd>

**split_url:** `typing.Optional[str]` — Split URL
    
</dd>
</dl>

<dl>
<dd>

**split_percent:** `typing.Optional[int]` — Split URL percentage
    
</dd>
</dl>

<dl>
<dd>

**split_urlv2:** `typing.Optional[typing.List[PostLinksPublicRequestSplitUrlv2Item]]` — Split URL configurations for multi-way A/B testing
    
</dd>
</dl>

<dl>
<dd>

**integration_adroll:** `typing.Optional[str]` — Adroll integration
    
</dd>
</dl>

<dl>
<dd>

**integration_fb:** `typing.Optional[str]` — Facebook integration
    
</dd>
</dl>

<dl>
<dd>

**integration_tt:** `typing.Optional[str]` — TikTok integration
    
</dd>
</dl>

<dl>
<dd>

**integration_ga:** `typing.Optional[str]` — Google Analytics integration
    
</dd>
</dl>

<dl>
<dd>

**integration_gtm:** `typing.Optional[str]` — Google Tag Manager integration
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">create_up_to1000links_in_one_call</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Please use this method if you need to create big packs of links. It
accepts up to 1000 links in one API call.

It works almost the same as single link creation endpoint, but accepts
an array of URLs and returns an array of responses.

Returns list of Link objects. If any URL is failed to insert, it returns
error object instead as array element. Method is not transactional – it
can insert some links from the list and return an error for others.

**Rate limit**: 5 queries in 10 seconds
</dd>
</dl>
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
from fern.link_management import PostLinksBulkRequestLinksItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.link_management.create_up_to1000links_in_one_call(
    domain="domain",
    links=[
        PostLinksBulkRequestLinksItem(
            original_url="https://example.com",
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

**domain:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**links:** `typing.List[PostLinksBulkRequestLinksItem]` 
    
</dd>
</dl>

<dl>
<dd>

**allow_duplicates:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` — Folder ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">generate_example_links_for_a_domain</a>(...) -> PostLinksExamplesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a set of demo/example links to showcase various features of the short link service.

Example links include:
- A/B testing with split URLs
- Mobile targeting (different URLs for Android/iPhone)
- Expiring links with time limits
- File download links
- Password-protected links

**Rate limit**: 5/10s
</dd>
</dl>
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

client.link_management.generate_example_links_for_a_domain(
    domain="domain",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain:** `str` — Domain hostname to create examples for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">duplicate_an_existing_link</a>(...) -> PostLinksDuplicateLinkIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Duplicates an existing link with all its properties, targeting rules, and settings.
The duplicated link will have a new random path (or custom if provided) and be fully independent.

**Rate limit**: 50/s
</dd>
</dl>
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

client.link_management.duplicate_an_existing_link(
    link_id="linkId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` — Custom path for duplicated link
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_management.<a href="src/fern/link_management/client.py">append_a_single_tag_to_the_links_in_bulk</a>(...)</code></summary>
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

client.link_management.append_a_single_tag_to_the_links_in_bulk(
    tag="tag",
    link_ids=[
        "lnk_abc123_abcdef"
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

**tag:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**link_ids:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## LinkTargeting
<details><summary><code>client.link_targeting.<a href="src/fern/link_targeting/client.py">get_link_countries</a>(...)</code></summary>
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

client.link_targeting.get_link_countries(
    link_id="linkId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_targeting.<a href="src/fern/link_targeting/client.py">create_link_country</a>(...)</code></summary>
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
from fern.link_targeting import PostLinkCountryLinkIdRequestCountry

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.link_targeting.create_link_country(
    link_id="linkId",
    country=PostLinkCountryLinkIdRequestCountry.AD,
    original_url="originalURL",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `PostLinkCountryLinkIdRequestCountry` — Country code
    
</dd>
</dl>

<dl>
<dd>

**original_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_targeting.<a href="src/fern/link_targeting/client.py">create_link_countries_in_bulk</a>(...)</code></summary>
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
from fern.link_targeting import PostLinkCountryBulkLinkIdRequestBodyItem, PostLinkCountryBulkLinkIdRequestBodyItemCountry

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.link_targeting.create_link_countries_in_bulk(
    link_id="linkId",
    request=[
        PostLinkCountryBulkLinkIdRequestBodyItem(
            country=PostLinkCountryBulkLinkIdRequestBodyItemCountry.AD,
            original_url="originalURL",
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

**link_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[PostLinkCountryBulkLinkIdRequestBodyItem]` 
    
</dd>
</dl>

<dl>
<dd>

**domain_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_targeting.<a href="src/fern/link_targeting/client.py">delete_link_country</a>(...)</code></summary>
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
from fern.link_targeting import DeleteLinkCountryLinkIdCountryRequestCountry

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.link_targeting.delete_link_country(
    link_id="linkId",
    country=DeleteLinkCountryLinkIdCountryRequestCountry.AD,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `DeleteLinkCountryLinkIdCountryRequestCountry` — Country code
    
</dd>
</dl>

<dl>
<dd>

**domain_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_targeting.<a href="src/fern/link_targeting/client.py">get_link_regions</a>(...)</code></summary>
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

client.link_targeting.get_link_regions(
    link_id="linkId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_targeting.<a href="src/fern/link_targeting/client.py">add_region_targeting_to_link</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add region targeting to link
</dd>
</dl>
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
from fern.link_targeting import PostLinkRegionLinkIdRequestCountry

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.link_targeting.add_region_targeting_to_link(
    link_id="linkId",
    country=PostLinkRegionLinkIdRequestCountry.AD,
    region="region",
    original_url="https://example.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `PostLinkRegionLinkIdRequestCountry` — Country code
    
</dd>
</dl>

<dl>
<dd>

**region:** `str` — ISO 3166-2 region code
    
</dd>
</dl>

<dl>
<dd>

**original_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_id:** `typing.Optional[int]` — Domain ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_targeting.<a href="src/fern/link_targeting/client.py">get_all_regions_by_country</a>(...)</code></summary>
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
from fern.link_targeting import GetLinkRegionListCountryRequestCountry

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.link_targeting.get_all_regions_by_country(
    country=GetLinkRegionListCountryRequestCountry.AD,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**country:** `GetLinkRegionListCountryRequestCountry` — Country code
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_targeting.<a href="src/fern/link_targeting/client.py">create_link_regions_in_bulk</a>(...)</code></summary>
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
from fern.link_targeting import PostLinkRegionBulkLinkIdRequestBodyItem, PostLinkRegionBulkLinkIdRequestBodyItemCountry

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.link_targeting.create_link_regions_in_bulk(
    link_id="linkId",
    request=[
        PostLinkRegionBulkLinkIdRequestBodyItem(
            country=PostLinkRegionBulkLinkIdRequestBodyItemCountry.AD,
            region="region",
            original_url="https://example.com",
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

**link_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[PostLinkRegionBulkLinkIdRequestBodyItem]` 
    
</dd>
</dl>

<dl>
<dd>

**domain_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_targeting.<a href="src/fern/link_targeting/client.py">delete_link_region_by_country</a>(...)</code></summary>
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
from fern.link_targeting import DeleteLinkRegionLinkIdCountryRegionRequestCountry

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.link_targeting.delete_link_region_by_country(
    link_id="linkId",
    country=DeleteLinkRegionLinkIdCountryRegionRequestCountry.AD,
    region="region",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `DeleteLinkRegionLinkIdCountryRegionRequestCountry` — Country code
    
</dd>
</dl>

<dl>
<dd>

**region:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Domains
<details><summary><code>client.domains.<a href="src/fern/domains/client.py">list_domains</a>(...) -> typing.List[GetApiDomainsResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Shows all domains of current user
</dd>
</dl>
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

client.domains.list_domains()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**no_team_id:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**pattern:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**additional_properties:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.domains.<a href="src/fern/domains/client.py">get_domain_details_by_id</a>(...) -> GetDomainsDomainIdResponse</code></summary>
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

client.domains.get_domain_details_by_id(
    domain_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.domains.<a href="src/fern/domains/client.py">update_domain_settings</a>(...) -> PostDomainsSettingsDomainIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update domain settings
</dd>
</dl>
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

client.domains.update_domain_settings(
    domain_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**https_level:** `typing.Optional[PostDomainsSettingsDomainIdRequestHttpsLevel]` 
    
</dd>
</dl>

<dl>
<dd>

**robots:** `typing.Optional[PostDomainsSettingsDomainIdRequestRobots]` 
    
</dd>
</dl>

<dl>
<dd>

**segment_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**link_type:** `typing.Optional[PostDomainsSettingsDomainIdRequestLinkType]` 
    
</dd>
</dl>

<dl>
<dd>

**cloaking:** `typing.Optional[bool]` — Enable cloaking for all links on the domain
    
</dd>
</dl>

<dl>
<dd>

**hide_referer:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**hide_visitor_ip:** `typing.Optional[bool]` — Don't store visitor IPs in our database
    
</dd>
</dl>

<dl>
<dd>

**https_links:** `typing.Optional[bool]` — Set to null to reissue a certificate
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[PostDomainsSettingsDomainIdRequestWebhookUrl]` 
    
</dd>
</dl>

<dl>
<dd>

**integration_ga:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**integration_fb:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**integration_tt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**integration_adroll:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**enable_conversion_tracking:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**qr_scan_tracking:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**integration_gtm:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**client_storage:** `typing.Optional[typing.Dict[str, typing.Any]]` — For internal use
    
</dd>
</dl>

<dl>
<dd>

**purge_expired_links:** `typing.Optional[bool]` — [DEPRECATED] do not use
    
</dd>
</dl>

<dl>
<dd>

**enable_ai:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**case_sensitive:** `typing.Optional[bool]` — Enable case sensitivity for short links
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.domains.<a href="src/fern/domains/client.py">create_a_domain</a>(...) -> PostDomainsResponse</code></summary>
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

client.domains.create_a_domain(
    hostname="😀.link",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**hostname:** `str` — Domain hostname
    
</dd>
</dl>

<dl>
<dd>

**hide_referer:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**link_type:** `typing.Optional[PostDomainsRequestLinkType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## LinkBundles
<details><summary><code>client.link_bundles.<a href="src/fern/link_bundles/client.py">get_bundle_templates</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all available bundle templates
</dd>
</dl>
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

client.link_bundles.get_bundle_templates()

```
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

<details><summary><code>client.link_bundles.<a href="src/fern/link_bundles/client.py">get_bundle_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns bundle details by ULID id
</dd>
</dl>
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

client.link_bundles.get_bundle_by_id(
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

**id:** `str` — Bundle ULID id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_bundles.<a href="src/fern/link_bundles/client.py">update_bundle</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates bundle details, social media links, and branding
</dd>
</dl>
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

client.link_bundles.update_bundle(
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

**id:** `str` — Bundle ULID id
    
</dd>
</dl>

<dl>
<dd>

**domain_id:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[str]` — Template ID
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Bundle title
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Bundle description
    
</dd>
</dl>

<dl>
<dd>

**logo_url:** `typing.Optional[str]` — Profile or logo URL
    
</dd>
</dl>

<dl>
<dd>

**background_image_url:** `typing.Optional[str]` — Background image URL
    
</dd>
</dl>

<dl>
<dd>

**twitter_username:** `typing.Optional[str]` — Twitter username (without @)
    
</dd>
</dl>

<dl>
<dd>

**fb_username:** `typing.Optional[str]` — Facebook username
    
</dd>
</dl>

<dl>
<dd>

**linkedin_companyname:** `typing.Optional[str]` — LinkedIn company name (mutually exclusive with linkedinUsername)
    
</dd>
</dl>

<dl>
<dd>

**linkedin_username:** `typing.Optional[str]` — LinkedIn username (mutually exclusive with linkedinCompanyname)
    
</dd>
</dl>

<dl>
<dd>

**instagram_username:** `typing.Optional[str]` — Instagram username (without @)
    
</dd>
</dl>

<dl>
<dd>

**whatsapp_url:** `typing.Optional[str]` — WhatsApp URL (must start with whatsapp:// or https://)
    
</dd>
</dl>

<dl>
<dd>

**viber_url:** `typing.Optional[str]` — Viber URL (must start with viber:// or https://)
    
</dd>
</dl>

<dl>
<dd>

**telegram_url:** `typing.Optional[str]` — Telegram URL
    
</dd>
</dl>

<dl>
<dd>

**threads_username:** `typing.Optional[str]` — Threads username (without @)
    
</dd>
</dl>

<dl>
<dd>

**mastodon_username:** `typing.Optional[str]` — Mastodon username
    
</dd>
</dl>

<dl>
<dd>

**bluesky_username:** `typing.Optional[str]` — Bluesky username
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Contact email address
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_bundles.<a href="src/fern/link_bundles/client.py">delete_bundle</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a bundle by ULID id
</dd>
</dl>
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

client.link_bundles.delete_bundle(
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

**id:** `str` — Bundle ULID id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_bundles.<a href="src/fern/link_bundles/client.py">upload_bundle_logo</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads a logo image for a bundle
</dd>
</dl>
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

client.link_bundles.upload_bundle_logo(
    id="id",
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Bundle ULID id
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_bundles.<a href="src/fern/link_bundles/client.py">upload_bundle_background_image</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads a background image for a bundle
</dd>
</dl>
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

client.link_bundles.upload_bundle_background_image(
    id="id",
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Bundle ULID id
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Any` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_bundles.<a href="src/fern/link_bundles/client.py">create_bundle</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new link bundle with customizable template, social media links, and branding
</dd>
</dl>
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

client.link_bundles.create_bundle(
    domain_id=1.1,
    template_id="TemplateId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_id:** `float` — Domain ID where the bundle will be created
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `str` — Template ID from available templates
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Bundle title
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Bundle description
    
</dd>
</dl>

<dl>
<dd>

**logo_url:** `typing.Optional[str]` — Profile or logo URL
    
</dd>
</dl>

<dl>
<dd>

**background_image_url:** `typing.Optional[str]` — Background image URL
    
</dd>
</dl>

<dl>
<dd>

**twitter_username:** `typing.Optional[str]` — Twitter username (without @)
    
</dd>
</dl>

<dl>
<dd>

**fb_username:** `typing.Optional[str]` — Facebook username
    
</dd>
</dl>

<dl>
<dd>

**linkedin_companyname:** `typing.Optional[str]` — LinkedIn company name (mutually exclusive with linkedinUsername)
    
</dd>
</dl>

<dl>
<dd>

**linkedin_username:** `typing.Optional[str]` — LinkedIn username (mutually exclusive with linkedinCompanyname)
    
</dd>
</dl>

<dl>
<dd>

**instagram_username:** `typing.Optional[str]` — Instagram username (without @)
    
</dd>
</dl>

<dl>
<dd>

**whatsapp_url:** `typing.Optional[str]` — WhatsApp URL (must start with whatsapp:// or https://)
    
</dd>
</dl>

<dl>
<dd>

**viber_url:** `typing.Optional[str]` — Viber URL (must start with viber:// or https://)
    
</dd>
</dl>

<dl>
<dd>

**telegram_url:** `typing.Optional[str]` — Telegram URL
    
</dd>
</dl>

<dl>
<dd>

**threads_username:** `typing.Optional[str]` — Threads username (without @)
    
</dd>
</dl>

<dl>
<dd>

**mastodon_username:** `typing.Optional[str]` — Mastodon username
    
</dd>
</dl>

<dl>
<dd>

**bluesky_username:** `typing.Optional[str]` — Bluesky username
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Contact email address
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_bundles.<a href="src/fern/link_bundles/client.py">get_bundle_links</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all links in a bundle, ordered by sort order
</dd>
</dl>
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

client.link_bundles.get_bundle_links(
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

**id:** `str` — Bundle ULID id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_bundles.<a href="src/fern/link_bundles/client.py">add_link_to_bundle</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a short link to a bundle. If the link doesn't exist, it will be created.
</dd>
</dl>
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

client.link_bundles.add_link_to_bundle(
    id="id",
    path="path",
    title="title",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Bundle ULID id
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Short link path or full URL
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` — Display title for the link
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_bundles.<a href="src/fern/link_bundles/client.py">update_link_sort_order</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the sort order of links in a bundle
</dd>
</dl>
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
from fern.link_bundles import PatchLinksBundleIdLinksRequestBodyItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.link_bundles.update_link_sort_order(
    id="id",
    request=[
        PatchLinksBundleIdLinksRequestBodyItem(
            id="id",
            sort_order=1.1,
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

**id:** `str` — Bundle ULID id
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[PatchLinksBundleIdLinksRequestBodyItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link_bundles.<a href="src/fern/link_bundles/client.py">remove_link_from_bundle</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a link from a bundle by its link template ID
</dd>
</dl>
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

client.link_bundles.remove_link_from_bundle(
    id="id",
    link_template_id="linkTemplateId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Bundle ULID id
    
</dd>
</dl>

<dl>
<dd>

**link_template_id:** `str` — Link template ID to remove
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

