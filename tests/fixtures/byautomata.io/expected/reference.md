# Reference
## ContentproSearch
<details><summary><code>client.contentpro_search.<a href="src/fern/contentpro_search/client.py">send_search_terms_to_receive_the_most_relevant_articles_and_companies</a>(...) -> GetContentproSearchResponse</code></summary>
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

client.contentpro_search.send_search_terms_to_receive_the_most_relevant_articles_and_companies(
    terms="terms",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**terms:** `str` — We provide information about related companies and articles based on the search terms you provide. Separate search terms with commas. Ex. https://api.byautomata.io/contentpro-search?terms=cloud+computing,enterprise,security
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ContentproSimilarText
<details><summary><code>client.contentpro_similar_text.<a href="src/fern/contentpro_similar_text/client.py">the_contentpro_similar_text_endpoint_accepts_and_arbitrary_piece_of_text_and_returns_similar_articles_and_blogs_written_by_companies</a>(...) -> PostContentproSimilarTextResponse</code></summary>
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

client.contentpro_similar_text.the_contentpro_similar_text_endpoint_accepts_and_arbitrary_piece_of_text_and_returns_similar_articles_and_blogs_written_by_companies(
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

**text:** `str` — Any piece of text
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Search
<details><summary><code>client.search.<a href="src/fern/search/client.py">send_search_terms_to_receive_the_most_relevant_companies_along_with_text_snippets</a>(...) -> GetSearchResponse</code></summary>
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

client.search.send_search_terms_to_receive_the_most_relevant_companies_along_with_text_snippets(
    terms="terms",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**terms:** `str` — We provide information about related companies based on the search terms you provide. Separate search terms with commas. Ex. https://api.byautomata.io/search?link=cloud+computing,enterprise,security
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — Page number of search results. Ex. https://api.byautomata.io/search?page=0&link=cloud+computing,enterprise,security
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Similar
<details><summary><code>client.similar.<a href="src/fern/similar/client.py">send_a_company_website_to_receive_a_list_of_companies_related_to_them</a>(...) -> GetSimilarResponse</code></summary>
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

client.similar.send_a_company_website_to_receive_a_list_of_companies_related_to_them(
    link="link",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**link:** `str` — We'll provide information about related companies based on the site you provide. If a LinkedIn page is sent, we will try to identify the company related to the page. Ex. https://api.byautomata.io/similar?link=ibm.com
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — Page number of search results. Ex. https://api.byautomata.io/similar?link=ibm.com&page=1
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

