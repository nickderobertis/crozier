# Reference
## Articles
<details><summary><code>client.articles.<a href="src/fern/articles/client.py">get_articles</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.articles.get_articles()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — What's being searched for
    
</dd>
</dl>

<dl>
<dd>

**exclude_featured:** `typing.Optional[int]` — Number of featured articles to exclude
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.articles.<a href="src/fern/articles/client.py">list_of_all_article_categories</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of all article categories
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.articles.list_of_all_article_categories()

```
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

## Categories
<details><summary><code>client.categories.<a href="src/fern/categories/client.py">list_of_supported_product_categories</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of supported product categories
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.categories.list_of_supported_product_categories()

```
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

<details><summary><code>client.categories.<a href="src/fern/categories/client.py">get_categories_flat</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.categories.get_categories_flat()

```
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

<details><summary><code>client.categories.<a href="src/fern/categories/client.py">full_taxonomy_tree_of_categories_including_middle_categories</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Full taxonomy tree of categories including middle categories
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.categories.full_taxonomy_tree_of_categories_including_middle_categories()

```
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

<details><summary><code>client.categories.<a href="src/fern/categories/client.py">get_subcategory_details</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get subcategory details
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.categories.get_subcategory_details(
    product_type="product_type",
    category="category",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**category:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.categories.<a href="src/fern/categories/client.py">get_category_details</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get category details
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.categories.get_category_details(
    uuid_="uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**uuid_:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ComparisonShoppingPages
<details><summary><code>client.comparison_shopping_pages.<a href="src/fern/comparison_shopping_pages/client.py">returns_a_set_of_comparison_shopping_pages_based_on_the_current_params</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a set of comparison shopping pages based on the current params
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.comparison_shopping_pages.returns_a_set_of_comparison_shopping_pages_based_on_the_current_params()

```
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

<details><summary><code>client.comparison_shopping_pages.<a href="src/fern/comparison_shopping_pages/client.py">show_comparison_shopping_page</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Show comparison shopping page
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.comparison_shopping_pages.show_comparison_shopping_page()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[str]` — ID of the comparison shopping page
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — Slug of the comparison shopping page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.comparison_shopping_pages.<a href="src/fern/comparison_shopping_pages/client.py">get_comparison_shopping_pages_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.comparison_shopping_pages.get_comparison_shopping_pages_id(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.comparison_shopping_pages.<a href="src/fern/comparison_shopping_pages/client.py">return_new_or_used_listings_for_a_comparison_shopping_page</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return new or used listings for a comparison shopping page
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.comparison_shopping_pages.return_new_or_used_listings_for_a_comparison_shopping_page(
    id="id",
    condition="condition",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**condition:** `str` — Condition of the listing
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.comparison_shopping_pages.<a href="src/fern/comparison_shopping_pages/client.py">view_reviews_of_a_comparison_shopping_page</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View reviews of a comparison shopping page
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.comparison_shopping_pages.view_reviews_of_a_comparison_shopping_page(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Conversations
<details><summary><code>client.conversations.<a href="src/fern/conversations/client.py">make_an_offer_to_the_other_participant_in_the_conversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Make an offer to the other participant in the conversation
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.conversations.make_an_offer_to_the_other_participant_in_the_conversation(
    id="id",
    price="price",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**price:** `str` — Offer price
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[str]` — Message to include with counter offer
    
</dd>
</dl>

<dl>
<dd>

**shipping_price:** `typing.Optional[str]` — Shipping price (sellers only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Countries
<details><summary><code>client.countries.<a href="src/fern/countries/client.py">retrieve_a_list_of_country_codes_with_corresponding_subregions</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of country codes with corresponding subregions
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.countries.retrieve_a_list_of_country_codes_with_corresponding_subregions()

```
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

## Csps
<details><summary><code>client.csps.<a href="src/fern/csps/client.py">returns_a_set_of_comparison_shopping_pages_based_on_the_current_params</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a set of comparison shopping pages based on the current params
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.csps.returns_a_set_of_comparison_shopping_pages_based_on_the_current_params()

```
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

<details><summary><code>client.csps.<a href="src/fern/csps/client.py">get_csps_categories</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.csps.get_csps_categories()

```
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

<details><summary><code>client.csps.<a href="src/fern/csps/client.py">show_comparison_shopping_page</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Show comparison shopping page
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.csps.show_comparison_shopping_page()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[str]` — ID of the comparison shopping page
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — Slug of the comparison shopping page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.csps.<a href="src/fern/csps/client.py">get_csps_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.csps.get_csps_id(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CuratedSets
<details><summary><code>client.curated_sets.<a href="src/fern/curated_sets/client.py">get_curated_sets_slug</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.curated_sets.get_curated_sets_slug(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Currencies
<details><summary><code>client.currencies.<a href="src/fern/currencies/client.py">list_of_supported_display_currencies_for_browsing_listings</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of supported display currencies for browsing listings
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.currencies.list_of_supported_display_currencies_for_browsing_listings()

```
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

<details><summary><code>client.currencies.<a href="src/fern/currencies/client.py">list_of_supported_listing_currencies_for_shops</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of supported listing currencies for shops
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.currencies.list_of_supported_listing_currencies_for_shops()

```
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

## Feedback
<details><summary><code>client.feedback.<a href="src/fern/feedback/client.py">feedback_details</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Feedback details
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.feedback.feedback_details(
    feedback_id="feedback_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**feedback_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Handpicked
<details><summary><code>client.handpicked.<a href="src/fern/handpicked/client.py">get_results_from_a_handpicked_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get results from a handpicked collection
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.handpicked.get_results_from_a_handpicked_collection(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search query.
    
</dd>
</dl>

<dl>
<dd>

**auction_price_max:** `typing.Optional[float]` — Maximum current auction price
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` — Category slug from /api/categories
    
</dd>
</dl>

<dl>
<dd>

**product_type:** `typing.Optional[str]` — Product type slug from /api/categories
    
</dd>
</dl>

<dl>
<dd>

**conditions:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint
    
</dd>
</dl>

<dl>
<dd>

**decade:** `typing.Optional[str]` — Decade: e.g. 1970s, early 70s
    
</dd>
</dl>

<dl>
<dd>

**finish:** `typing.Optional[str]` — Visual finish of the item, common for guitars
    
</dd>
</dl>

<dl>
<dd>

**handmade:** `typing.Optional[bool]` — Handmade items only
    
</dd>
</dl>

<dl>
<dd>

**item_city:** `typing.Optional[str]` — City where item is located
    
</dd>
</dl>

<dl>
<dd>

**item_country:** `typing.Optional[str]` — DEPRECATED - Country code where item is located
    
</dd>
</dl>

<dl>
<dd>

**item_region:** `typing.Optional[str]` — Country code where item is located
    
</dd>
</dl>

<dl>
<dd>

**item_state:** `typing.Optional[str]` — State or region code where item is located
    
</dd>
</dl>

<dl>
<dd>

**make:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Make(s)/brand of item (e.g. Fender). Can take a single value or an array.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — Model of item (e.g. Stratocaster)
    
</dd>
</dl>

<dl>
<dd>

**must_not:** `typing.Optional[str]` — Search term negation. If you want to exclude a term, add it here
    
</dd>
</dl>

<dl>
<dd>

**price_max:** `typing.Optional[float]` — Maximum price of search results (USD)
    
</dd>
</dl>

<dl>
<dd>

**price_min:** `typing.Optional[float]` — Minimum price of search results (USD)
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — The currency to be used for the price filters
    
</dd>
</dl>

<dl>
<dd>

**year_max:** `typing.Optional[int]` — Maximum year of manufacture
    
</dd>
</dl>

<dl>
<dd>

**year_min:** `typing.Optional[int]` — Minumum year of manufacture
    
</dd>
</dl>

<dl>
<dd>

**accepts_gift_cards:** `typing.Optional[bool]` — If true, include only items that accept gift cards
    
</dd>
</dl>

<dl>
<dd>

**preferred_seller:** `typing.Optional[bool]` — If true, include only items by Reverb Preferred Sellers
    
</dd>
</dl>

<dl>
<dd>

**shop:** `typing.Optional[str]` — Slug of shop to search
    
</dd>
</dl>

<dl>
<dd>

**shop_id:** `typing.Optional[str]` — ID of shop to search
    
</dd>
</dl>

<dl>
<dd>

**listing_type:** `typing.Optional[str]` — Type of listing: auctions,offers
    
</dd>
</dl>

<dl>
<dd>

**ships_to:** `typing.Optional[str]` — Limit search to items that ship to this country code
    
</dd>
</dl>

<dl>
<dd>

**exclude_auctions:** `typing.Optional[bool]` — If true, exclude auctions
    
</dd>
</dl>

<dl>
<dd>

**accepts_payment_plans:** `typing.Optional[bool]` — If true, only show items that can be purchased with a payment plan
    
</dd>
</dl>

<dl>
<dd>

**watchers_count_min:** `typing.Optional[int]` — Minimum number of watchers (used to find popular items)
    
</dd>
</dl>

<dl>
<dd>

**not_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Listing ID negation. If you want to exclude a listing, add it here.
    
</dd>
</dl>

<dl>
<dd>

**local_pickup:** `typing.Optional[bool]` — Only items that offer local pickup
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ListingConditions
<details><summary><code>client.listing_conditions.<a href="src/fern/listing_conditions/client.py">list_of_supported_product_conditions</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of supported product conditions
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listing_conditions.list_of_supported_product_conditions()

```
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

## Listings
<details><summary><code>client.listings.<a href="src/fern/listings/client.py">default_search_of_listings_includes_only_used_handmade_add_a_filter_to_view_all_listings_or_use_the_listings_all_endpoint</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Default search of listings includes only used & handmade. Add a filter to view all listings or use the /listings/all endpoint.
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listings.default_search_of_listings_includes_only_used_handmade_add_a_filter_to_view_all_listings_or_use_the_listings_all_endpoint()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search query.
    
</dd>
</dl>

<dl>
<dd>

**auction_price_max:** `typing.Optional[float]` — Maximum current auction price
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` — Category slug from /api/categories
    
</dd>
</dl>

<dl>
<dd>

**product_type:** `typing.Optional[str]` — Product type slug from /api/categories
    
</dd>
</dl>

<dl>
<dd>

**conditions:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint
    
</dd>
</dl>

<dl>
<dd>

**decade:** `typing.Optional[str]` — Decade: e.g. 1970s, early 70s
    
</dd>
</dl>

<dl>
<dd>

**finish:** `typing.Optional[str]` — Visual finish of the item, common for guitars
    
</dd>
</dl>

<dl>
<dd>

**handmade:** `typing.Optional[bool]` — Handmade items only
    
</dd>
</dl>

<dl>
<dd>

**item_city:** `typing.Optional[str]` — City where item is located
    
</dd>
</dl>

<dl>
<dd>

**item_country:** `typing.Optional[str]` — DEPRECATED - Country code where item is located
    
</dd>
</dl>

<dl>
<dd>

**item_region:** `typing.Optional[str]` — Country code where item is located
    
</dd>
</dl>

<dl>
<dd>

**item_state:** `typing.Optional[str]` — State or region code where item is located
    
</dd>
</dl>

<dl>
<dd>

**make:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Make(s)/brand of item (e.g. Fender). Can take a single value or an array.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — Model of item (e.g. Stratocaster)
    
</dd>
</dl>

<dl>
<dd>

**must_not:** `typing.Optional[str]` — Search term negation. If you want to exclude a term, add it here
    
</dd>
</dl>

<dl>
<dd>

**price_max:** `typing.Optional[float]` — Maximum price of search results (USD)
    
</dd>
</dl>

<dl>
<dd>

**price_min:** `typing.Optional[float]` — Minimum price of search results (USD)
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — The currency to be used for the price filters
    
</dd>
</dl>

<dl>
<dd>

**year_max:** `typing.Optional[int]` — Maximum year of manufacture
    
</dd>
</dl>

<dl>
<dd>

**year_min:** `typing.Optional[int]` — Minumum year of manufacture
    
</dd>
</dl>

<dl>
<dd>

**accepts_gift_cards:** `typing.Optional[bool]` — If true, include only items that accept gift cards
    
</dd>
</dl>

<dl>
<dd>

**preferred_seller:** `typing.Optional[bool]` — If true, include only items by Reverb Preferred Sellers
    
</dd>
</dl>

<dl>
<dd>

**shop:** `typing.Optional[str]` — Slug of shop to search
    
</dd>
</dl>

<dl>
<dd>

**shop_id:** `typing.Optional[str]` — ID of shop to search
    
</dd>
</dl>

<dl>
<dd>

**listing_type:** `typing.Optional[str]` — Type of listing: auctions,offers
    
</dd>
</dl>

<dl>
<dd>

**ships_to:** `typing.Optional[str]` — Limit search to items that ship to this country code
    
</dd>
</dl>

<dl>
<dd>

**exclude_auctions:** `typing.Optional[bool]` — If true, exclude auctions
    
</dd>
</dl>

<dl>
<dd>

**accepts_payment_plans:** `typing.Optional[bool]` — If true, only show items that can be purchased with a payment plan
    
</dd>
</dl>

<dl>
<dd>

**watchers_count_min:** `typing.Optional[int]` — Minimum number of watchers (used to find popular items)
    
</dd>
</dl>

<dl>
<dd>

**not_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Listing ID negation. If you want to exclude a listing, add it here.
    
</dd>
</dl>

<dl>
<dd>

**local_pickup:** `typing.Optional[bool]` — Only items that offer local pickup
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.listings.<a href="src/fern/listings/client.py">create_a_listing</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a listing
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listings.create_a_listing()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**categories:** `typing.Optional[typing.Sequence[PostListingsRequestCategoriesItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**condition:** `typing.Optional[PostListingsRequestCondition]` — Condition
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Product description. Please keep formatting to a minimum.
    
</dd>
</dl>

<dl>
<dd>

**exclusive_channel:** `typing.Optional[PostListingsRequestExclusiveChannel]` — Currently for users of seller sites only, this allows you to have a listing available only to your seller site by setting this to 'seller_site'
    
</dd>
</dl>

<dl>
<dd>

**finish:** `typing.Optional[str]` — Finish, e.g. 'Sunburst'
    
</dd>
</dl>

<dl>
<dd>

**has_inventory:** `typing.Optional[bool]` — Set true if selling more than one
    
</dd>
</dl>

<dl>
<dd>

**inventory:** `typing.Optional[int]` — Number of items available for sale. Reverb will increment and decrement automatically.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[PostListingsRequestLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**make:** `typing.Optional[str]` — ex: Fender, Gibson
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — ex: Stratocaster, SG
    
</dd>
</dl>

<dl>
<dd>

**multi_item:** `typing.Optional[bool]` — Specifies if the listing is a bundle of multiple individual items
    
</dd>
</dl>

<dl>
<dd>

**offers_enabled:** `typing.Optional[bool]` — Whether the listing accepts negotiated offers (default: true)
    
</dd>
</dl>

<dl>
<dd>

**origin_country_code:** `typing.Optional[str]` — Country of origin/manufacture, ISO code (e.g: US)
    
</dd>
</dl>

<dl>
<dd>

**photos:** `typing.Optional[typing.Sequence[str]]` — An array of image URLs. Ex: ['http://my.site.com/image.jpg']
    
</dd>
</dl>

<dl>
<dd>

**preorder_info:** `typing.Optional[PostListingsRequestPreorderInfo]` — Create or update a preorder listing. Requires opt-in. Please contact sales@reverb.com if you would like to activate this feature.
    
</dd>
</dl>

<dl>
<dd>

**price:** `typing.Optional[PostListingsRequestPrice]` 
    
</dd>
</dl>

<dl>
<dd>

**prop65warning:** `typing.Optional[str]` — If your listing contains chemicals that are required to be reported under California Prop 65, please provide your warning statement. We will add the required 'Warning' label and link to California's information page, so you only need to provide the body of the warning. For more information, see https://www.p65warnings.ca.gov/new-proposition-65-warnings
    
</dd>
</dl>

<dl>
<dd>

**publish:** `typing.Optional[bool]` — Publish your listing if draft
    
</dd>
</dl>

<dl>
<dd>

**seller:** `typing.Optional[PostListingsRequestSeller]` 
    
</dd>
</dl>

<dl>
<dd>

**seller_cost:** `typing.Optional[str]` — Cost of goods in your currency as a POSIX-compliant decimal number (internal use only, not shown to buyers)
    
</dd>
</dl>

<dl>
<dd>

**shipping:** `typing.Optional[PostListingsRequestShipping]` 
    
</dd>
</dl>

<dl>
<dd>

**shipping_profile_id:** `typing.Optional[str]` — id of a shop's shipping profile
    
</dd>
</dl>

<dl>
<dd>

**shipping_profile_name:** `typing.Optional[str]` — DEPRECATED, please use shipping_profile_id. Name of a shipping profile
    
</dd>
</dl>

<dl>
<dd>

**sku:** `typing.Optional[str]` — Unique identifier for product
    
</dd>
</dl>

<dl>
<dd>

**sold_as_is:** `typing.Optional[bool]` — This item is sold As-Is and cannot be returned
    
</dd>
</dl>

<dl>
<dd>

**storage_location:** `typing.Optional[str]` — Internal note used by sellers to back reference their catalog system when entering a listing
    
</dd>
</dl>

<dl>
<dd>

**tax_exempt:** `typing.Optional[bool]` — Listing is exempt from taxes / VAT
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Title of your listing
    
</dd>
</dl>

<dl>
<dd>

**upc:** `typing.Optional[str]` — Valid UPC code
    
</dd>
</dl>

<dl>
<dd>

**upc_does_not_apply:** `typing.Optional[bool]` — True if a brand new product has no UPC code, ie for a handmade or custom item
    
</dd>
</dl>

<dl>
<dd>

**videos:** `typing.Optional[typing.Sequence[PostListingsRequestVideosItem]]` — List of YouTube video urls. Note: ONLY ONE ALLOWED
    
</dd>
</dl>

<dl>
<dd>

**year:** `typing.Optional[str]` — Supports many formats. Ex: 1979, mid-70s, late 90s
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.listings.<a href="src/fern/listings/client.py">all_listings_including_used_handmade_and_brand_new</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

All listings including used, handmade, and brand new
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listings.all_listings_including_used_handmade_and_brand_new()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search query.
    
</dd>
</dl>

<dl>
<dd>

**auction_price_max:** `typing.Optional[float]` — Maximum current auction price
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` — Category slug from /api/categories
    
</dd>
</dl>

<dl>
<dd>

**product_type:** `typing.Optional[str]` — Product type slug from /api/categories
    
</dd>
</dl>

<dl>
<dd>

**conditions:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint
    
</dd>
</dl>

<dl>
<dd>

**decade:** `typing.Optional[str]` — Decade: e.g. 1970s, early 70s
    
</dd>
</dl>

<dl>
<dd>

**finish:** `typing.Optional[str]` — Visual finish of the item, common for guitars
    
</dd>
</dl>

<dl>
<dd>

**handmade:** `typing.Optional[bool]` — Handmade items only
    
</dd>
</dl>

<dl>
<dd>

**item_city:** `typing.Optional[str]` — City where item is located
    
</dd>
</dl>

<dl>
<dd>

**item_country:** `typing.Optional[str]` — DEPRECATED - Country code where item is located
    
</dd>
</dl>

<dl>
<dd>

**item_region:** `typing.Optional[str]` — Country code where item is located
    
</dd>
</dl>

<dl>
<dd>

**item_state:** `typing.Optional[str]` — State or region code where item is located
    
</dd>
</dl>

<dl>
<dd>

**make:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Make(s)/brand of item (e.g. Fender). Can take a single value or an array.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — Model of item (e.g. Stratocaster)
    
</dd>
</dl>

<dl>
<dd>

**must_not:** `typing.Optional[str]` — Search term negation. If you want to exclude a term, add it here
    
</dd>
</dl>

<dl>
<dd>

**price_max:** `typing.Optional[float]` — Maximum price of search results (USD)
    
</dd>
</dl>

<dl>
<dd>

**price_min:** `typing.Optional[float]` — Minimum price of search results (USD)
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — The currency to be used for the price filters
    
</dd>
</dl>

<dl>
<dd>

**year_max:** `typing.Optional[int]` — Maximum year of manufacture
    
</dd>
</dl>

<dl>
<dd>

**year_min:** `typing.Optional[int]` — Minumum year of manufacture
    
</dd>
</dl>

<dl>
<dd>

**accepts_gift_cards:** `typing.Optional[bool]` — If true, include only items that accept gift cards
    
</dd>
</dl>

<dl>
<dd>

**preferred_seller:** `typing.Optional[bool]` — If true, include only items by Reverb Preferred Sellers
    
</dd>
</dl>

<dl>
<dd>

**shop:** `typing.Optional[str]` — Slug of shop to search
    
</dd>
</dl>

<dl>
<dd>

**shop_id:** `typing.Optional[str]` — ID of shop to search
    
</dd>
</dl>

<dl>
<dd>

**listing_type:** `typing.Optional[str]` — Type of listing: auctions,offers
    
</dd>
</dl>

<dl>
<dd>

**ships_to:** `typing.Optional[str]` — Limit search to items that ship to this country code
    
</dd>
</dl>

<dl>
<dd>

**exclude_auctions:** `typing.Optional[bool]` — If true, exclude auctions
    
</dd>
</dl>

<dl>
<dd>

**accepts_payment_plans:** `typing.Optional[bool]` — If true, only show items that can be purchased with a payment plan
    
</dd>
</dl>

<dl>
<dd>

**watchers_count_min:** `typing.Optional[int]` — Minimum number of watchers (used to find popular items)
    
</dd>
</dl>

<dl>
<dd>

**not_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Listing ID negation. If you want to exclude a listing, add it here.
    
</dd>
</dl>

<dl>
<dd>

**local_pickup:** `typing.Optional[bool]` — Only items that offer local pickup
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.listings.<a href="src/fern/listings/client.py">individual_facets</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Individual facets
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listings.individual_facets()

```
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

<details><summary><code>client.listings.<a href="src/fern/listings/client.py">returns_the_latest_negotiation_for_the_requesting_user_given_a_listing_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the latest negotiation for the requesting user given a listing id
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listings.returns_the_latest_negotiation_for_the_requesting_user_given_a_listing_id(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.listings.<a href="src/fern/listings/client.py">make_an_offer_to_the_seller_of_a_listing</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Make an offer to the seller of a listing
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listings.make_an_offer_to_the_seller_of_a_listing(
    id="id",
    price="price",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**price:** `str` — Offer price
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[str]` — Message to include with counter offer
    
</dd>
</dl>

<dl>
<dd>

**shipping_price:** `typing.Optional[str]` — Shipping price (sellers only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.listings.<a href="src/fern/listings/client.py">view_available_bump_tiers_and_stats_for_a_listing</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View available bump tiers and stats for a listing
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listings.view_available_bump_tiers_and_stats_for_a_listing(
    listing_id="listing_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**listing_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.listings.<a href="src/fern/listings/client.py">bump_a_listing</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bump a listing
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listings.bump_a_listing(
    listing_id="listing_id",
    budget_type="budget_type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**listing_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**budget_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.listings.<a href="src/fern/listings/client.py">start_a_conversation_with_a_seller</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start a conversation with a seller
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listings.start_a_conversation_with_a_seller(
    listing_id="listing_id",
    body="body",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**listing_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.listings.<a href="src/fern/listings/client.py">view_the_images_associated_with_a_particular_listing</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View the images associated with a particular listing
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listings.view_the_images_associated_with_a_particular_listing(
    listing_id="listing_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**listing_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.listings.<a href="src/fern/listings/client.py">delete_an_image_from_a_listing</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an image from a listing
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listings.delete_an_image_from_a_listing(
    listing_id="listing_id",
    image_id="image_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**listing_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**image_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.listings.<a href="src/fern/listings/client.py">see_all_sales_that_include_a_listing</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

See all sales that include a listing.
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listings.see_all_sales_that_include_a_listing(
    listing_id="listing_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**listing_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.listings.<a href="src/fern/listings/client.py">listing_details</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Listing details
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listings.listing_details(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.listings.<a href="src/fern/listings/client.py">update_a_listing</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a listing
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listings.update_a_listing(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**categories:** `typing.Optional[typing.Sequence[PutListingsSlugRequestCategoriesItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**condition:** `typing.Optional[PutListingsSlugRequestCondition]` — Condition
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Product description. Please keep formatting to a minimum.
    
</dd>
</dl>

<dl>
<dd>

**exclusive_channel:** `typing.Optional[PutListingsSlugRequestExclusiveChannel]` — Currently for users of seller sites only, this allows you to have a listing available only to your seller site by setting this to 'seller_site'
    
</dd>
</dl>

<dl>
<dd>

**finish:** `typing.Optional[str]` — Finish, e.g. 'Sunburst'
    
</dd>
</dl>

<dl>
<dd>

**has_inventory:** `typing.Optional[bool]` — Set true if selling more than one
    
</dd>
</dl>

<dl>
<dd>

**inventory:** `typing.Optional[int]` — Number of items available for sale. Reverb will increment and decrement automatically.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[PutListingsSlugRequestLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**make:** `typing.Optional[str]` — ex: Fender, Gibson
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — ex: Stratocaster, SG
    
</dd>
</dl>

<dl>
<dd>

**multi_item:** `typing.Optional[bool]` — Specifies if the listing is a bundle of multiple individual items
    
</dd>
</dl>

<dl>
<dd>

**offers_enabled:** `typing.Optional[bool]` — Whether the listing accepts negotiated offers (default: true)
    
</dd>
</dl>

<dl>
<dd>

**origin_country_code:** `typing.Optional[str]` — Country of origin/manufacture, ISO code (e.g: US)
    
</dd>
</dl>

<dl>
<dd>

**photos:** `typing.Optional[typing.Sequence[str]]` — An array of image URLs. Ex: ['http://my.site.com/image.jpg']
    
</dd>
</dl>

<dl>
<dd>

**preorder_info:** `typing.Optional[PutListingsSlugRequestPreorderInfo]` — Create or update a preorder listing. Requires opt-in. Please contact sales@reverb.com if you would like to activate this feature.
    
</dd>
</dl>

<dl>
<dd>

**price:** `typing.Optional[PutListingsSlugRequestPrice]` 
    
</dd>
</dl>

<dl>
<dd>

**prop65warning:** `typing.Optional[str]` — If your listing contains chemicals that are required to be reported under California Prop 65, please provide your warning statement. We will add the required 'Warning' label and link to California's information page, so you only need to provide the body of the warning. For more information, see https://www.p65warnings.ca.gov/new-proposition-65-warnings
    
</dd>
</dl>

<dl>
<dd>

**publish:** `typing.Optional[bool]` — Publish your listing if draft
    
</dd>
</dl>

<dl>
<dd>

**seller:** `typing.Optional[PutListingsSlugRequestSeller]` 
    
</dd>
</dl>

<dl>
<dd>

**seller_cost:** `typing.Optional[str]` — Cost of goods in your currency as a POSIX-compliant decimal number (internal use only, not shown to buyers)
    
</dd>
</dl>

<dl>
<dd>

**shipping:** `typing.Optional[PutListingsSlugRequestShipping]` 
    
</dd>
</dl>

<dl>
<dd>

**shipping_profile_id:** `typing.Optional[str]` — id of a shop's shipping profile
    
</dd>
</dl>

<dl>
<dd>

**shipping_profile_name:** `typing.Optional[str]` — DEPRECATED, please use shipping_profile_id. Name of a shipping profile
    
</dd>
</dl>

<dl>
<dd>

**sku:** `typing.Optional[str]` — Unique identifier for product
    
</dd>
</dl>

<dl>
<dd>

**sold_as_is:** `typing.Optional[bool]` — This item is sold As-Is and cannot be returned
    
</dd>
</dl>

<dl>
<dd>

**storage_location:** `typing.Optional[str]` — Internal note used by sellers to back reference their catalog system when entering a listing
    
</dd>
</dl>

<dl>
<dd>

**tax_exempt:** `typing.Optional[bool]` — Listing is exempt from taxes / VAT
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Title of your listing
    
</dd>
</dl>

<dl>
<dd>

**upc:** `typing.Optional[str]` — Valid UPC code
    
</dd>
</dl>

<dl>
<dd>

**upc_does_not_apply:** `typing.Optional[bool]` — True if a brand new product has no UPC code, ie for a handmade or custom item
    
</dd>
</dl>

<dl>
<dd>

**videos:** `typing.Optional[typing.Sequence[PutListingsSlugRequestVideosItem]]` — List of YouTube video urls. Note: ONLY ONE ALLOWED
    
</dd>
</dl>

<dl>
<dd>

**year:** `typing.Optional[str]` — Supports many formats. Ex: 1979, mid-70s, late 90s
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.listings.<a href="src/fern/listings/client.py">delete_a_draft_listing_cannot_be_used_on_non_drafts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a draft listing. Cannot be used on non-drafts.
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listings.delete_a_draft_listing_cannot_be_used_on_non_drafts(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.listings.<a href="src/fern/listings/client.py">edit_listing</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edit listing.
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listings.edit_listing(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.listings.<a href="src/fern/listings/client.py">flag_a_listing_for_inappropriate_content_or_fraud</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Flag a listing for inappropriate content or fraud
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listings.flag_a_listing_for_inappropriate_content_or_fraud(
    slug="slug",
    reason="reason",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**reason:** `str` — Valid reasons: 'Sexuality/nudity', 'Hateful or inappropriate speech', 'Item not as described or potential fraud', 'Trademark infringement', 'Other'
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — User input description specifying what is flag-worthy about this listing
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.listings.<a href="src/fern/listings/client.py">view_reviews_of_a_listing</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View reviews of a listing
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listings.view_reviews_of_a_listing(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.listings.<a href="src/fern/listings/client.py">create_a_review_for_a_listing</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a review for a listing
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.listings.create_a_review_for_a_listing(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## My
<details><summary><code>client.my.<a href="src/fern/my/client.py">get_account_details</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get account details
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.get_account_details()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">update_account_details</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update account details
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.update_account_details()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**currency:** `typing.Optional[str]` — The currency preference for the account
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The first name of the account holder
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The last name of the account holder
    
</dd>
</dl>

<dl>
<dd>

**locale_code:** `typing.Optional[str]` — The locale code for the account
    
</dd>
</dl>

<dl>
<dd>

**shipping_region_code:** `typing.Optional[str]` — The shipping region preference for the account
    
</dd>
</dl>

<dl>
<dd>

**third_party_ad_data_consent:** `typing.Optional[bool]` — The privacy setting preference for the account
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">see_all_addresses_in_your_address_book</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

See all addresses in your address book
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.see_all_addresses_in_your_address_book()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">create_a_new_address_in_your_address_book</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new address in your address book
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.create_a_new_address_in_your_address_book()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">update_an_existing_address_in_your_address_book</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing address in your address book
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.update_an_existing_address_in_your_address_book(
    address_id="address_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**address_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">delete_an_existing_address_in_your_address_book</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an existing address in your address book
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.delete_an_existing_address_in_your_address_book(
    address_id="address_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**address_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">get_a_list_of_your_conversations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of your conversations
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.get_a_list_of_your_conversations()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `typing.Optional[str]` — Query string to search conversations by
    
</dd>
</dl>

<dl>
<dd>

**unread_only:** `typing.Optional[bool]` — Show unread conversations only
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">start_a_conversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start a conversation
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.start_a_conversation(
    body="body",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**body:** `str` — The body of the message
    
</dd>
</dl>

<dl>
<dd>

**cloudinary_photos:** `typing.Optional[typing.Sequence[str]]` — An array of cloudinary data hashes (Reverb internal use only).
    
</dd>
</dl>

<dl>
<dd>

**listing_id:** `typing.Optional[int]` — The id of the listing being discussed
    
</dd>
</dl>

<dl>
<dd>

**recipient_id:** `typing.Optional[int]` — The id of the user you are trying to contact
    
</dd>
</dl>

<dl>
<dd>

**recipient_uuid:** `typing.Optional[str]` — The uuid of the user you are trying to contact
    
</dd>
</dl>

<dl>
<dd>

**shop_id:** `typing.Optional[str]` — The id of the shop you are trying to contact
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">send_a_message</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a message
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.send_a_message(
    conversation_id="conversation_id",
    body="body",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">display_conversation_details_with_messages_in_natural_time_order_oldest_to_newest</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Display conversation details with messages in natural time order (oldest to newest)
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.display_conversation_details_with_messages_in_natural_time_order_oldest_to_newest(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">mark_a_conversation_read_unread</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mark a conversation read/unread
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.mark_a_conversation_read_unread(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**read:** `typing.Optional[bool]` — Should the conversation be marked as read
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">get_your_actionable_status_counts</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get your actionable status counts
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.get_your_actionable_status_counts()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">post_my_curated_set_product_product_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.my.post_my_curated_set_product_product_id(
    product_id="product_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">delete_my_curated_set_product_product_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.my.delete_my_curated_set_product_product_id(
    product_id="product_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">get_listings_from_your_feed</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get listings from your feed
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.get_listings_from_your_feed()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">get_your_feed_customization_options</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

get your feed customization options
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.get_your_feed_customization_options()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">get_your_feed</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

get your feed
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.get_your_feed()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">list_of_received_feedback</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of received feedback
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.list_of_received_feedback()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">list_of_sent_feedback</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of sent feedback
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.list_of_sent_feedback()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">see_what_the_user_is_following</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

See what the user is following
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.see_what_the_user_is_following()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">returns_a_users_article_category_follows</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a user's ArticleCategoryFollows
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.returns_a_users_article_category_follows()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">set_a_users_article_category_follows</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set a user's ArticleCategoryFollows
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.set_a_users_article_category_follows(
    category_uuids="category_uuids",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category_uuids:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">follow_status_for_a_brand</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow status for a brand
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.follow_status_for_a_brand(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">follow_a_brand</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow a brand
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.follow_a_brand(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">unfollow_a_brand</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unfollow a brand
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.unfollow_a_brand(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">follow_status_for_a_subcategory</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow status for a subcategory
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.follow_status_for_a_subcategory(
    category="category",
    subcategory="subcategory",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**subcategory:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">follow_a_subcategory</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow a subcategory
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.follow_a_subcategory(
    category="category",
    subcategory="subcategory",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**subcategory:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">unfollow_a_subcategory</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unfollow a subcategory
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.unfollow_a_subcategory(
    category="category",
    subcategory="subcategory",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**subcategory:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">follow_status_for_a_category</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow status for a category
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.follow_status_for_a_category(
    identifier="identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">follow_a_category</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow a category
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.follow_a_category(
    uuid_="uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**uuid_:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">unfollow_a_category</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unfollow a category
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.unfollow_a_category(
    identifier="identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">follow_status_for_a_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow status for a collection
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.follow_status_for_a_collection(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">follow_a_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow a collection
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.follow_a_collection(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">unfollow_a_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unfollow a collection
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.unfollow_a_collection(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">follow_status_for_a_handpicked_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow status for a handpicked collection
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.follow_status_for_a_handpicked_collection(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">follow_a_handpicked_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow a handpicked collection
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.follow_a_handpicked_collection(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">unfollow_a_handpicked_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unfollow a handpicked collection
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.unfollow_a_handpicked_collection(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">follow_status_for_a_search</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow status for a search
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.follow_status_for_a_search()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">follow_a_search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow a search
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.follow_a_search()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**accepts_gift_cards:** `typing.Optional[bool]` — If true, include only items that accept gift cards
    
</dd>
</dl>

<dl>
<dd>

**accepts_payment_plans:** `typing.Optional[bool]` — If true, only show items that can be purchased with a payment plan
    
</dd>
</dl>

<dl>
<dd>

**auction_price_max:** `typing.Optional[float]` — Maximum current auction price
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` — Category slug from /api/categories
    
</dd>
</dl>

<dl>
<dd>

**conditions:** `typing.Optional[typing.Sequence[str]]` — Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[PostMyFollowsSearchRequestCurrency]` — The currency to be used for the price filters
    
</dd>
</dl>

<dl>
<dd>

**decade:** `typing.Optional[str]` — Decade: e.g. 1970s, early 70s
    
</dd>
</dl>

<dl>
<dd>

**exclude_auctions:** `typing.Optional[bool]` — If true, exclude auctions
    
</dd>
</dl>

<dl>
<dd>

**finish:** `typing.Optional[str]` — Visual finish of the item, common for guitars
    
</dd>
</dl>

<dl>
<dd>

**handmade:** `typing.Optional[bool]` — Handmade items only
    
</dd>
</dl>

<dl>
<dd>

**item_city:** `typing.Optional[str]` — City where item is located
    
</dd>
</dl>

<dl>
<dd>

**item_country:** `typing.Optional[str]` — DEPRECATED - Country code where item is located
    
</dd>
</dl>

<dl>
<dd>

**item_region:** `typing.Optional[str]` — Country code where item is located
    
</dd>
</dl>

<dl>
<dd>

**item_state:** `typing.Optional[str]` — State or region code where item is located
    
</dd>
</dl>

<dl>
<dd>

**listing_type:** `typing.Optional[PostMyFollowsSearchRequestListingType]` — Type of listing: auctions,offers
    
</dd>
</dl>

<dl>
<dd>

**local_pickup:** `typing.Optional[bool]` — Only items that offer local pickup
    
</dd>
</dl>

<dl>
<dd>

**make:** `typing.Optional[typing.Sequence[str]]` — Make(s)/brand of item (e.g. Fender). Can take a single value or an array.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — Model of item (e.g. Stratocaster)
    
</dd>
</dl>

<dl>
<dd>

**must_not:** `typing.Optional[str]` — Search term negation. If you want to exclude a term, add it here
    
</dd>
</dl>

<dl>
<dd>

**not_ids:** `typing.Optional[typing.Sequence[int]]` — Listing ID negation. If you want to exclude a listing, add it here.
    
</dd>
</dl>

<dl>
<dd>

**preferred_seller:** `typing.Optional[bool]` — If true, include only items by Reverb Preferred Sellers
    
</dd>
</dl>

<dl>
<dd>

**price_max:** `typing.Optional[float]` — Maximum price of search results (USD)
    
</dd>
</dl>

<dl>
<dd>

**price_min:** `typing.Optional[float]` — Minimum price of search results (USD)
    
</dd>
</dl>

<dl>
<dd>

**product_type:** `typing.Optional[str]` — Product type slug from /api/categories
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search query.
    
</dd>
</dl>

<dl>
<dd>

**ships_to:** `typing.Optional[str]` — Limit search to items that ship to this country code
    
</dd>
</dl>

<dl>
<dd>

**shop:** `typing.Optional[str]` — Slug of shop to search
    
</dd>
</dl>

<dl>
<dd>

**shop_id:** `typing.Optional[str]` — ID of shop to search
    
</dd>
</dl>

<dl>
<dd>

**watchers_count_min:** `typing.Optional[int]` — Minimum number of watchers (used to find popular items)
    
</dd>
</dl>

<dl>
<dd>

**year_max:** `typing.Optional[int]` — Maximum year of manufacture
    
</dd>
</dl>

<dl>
<dd>

**year_min:** `typing.Optional[int]` — Minumum year of manufacture
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">follow_status_for_a_shop</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow status for a shop
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.follow_status_for_a_shop(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">follow_a_shop</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow a shop
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.follow_a_shop(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">unfollow_a_shop</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unfollow a shop
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.unfollow_a_shop(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">delete_a_follow</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a follow
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.delete_a_follow(
    follow_id="follow_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**follow_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">post_my_follows_follow_id_alert</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.my.post_my_follows_follow_id_alert(
    follow_id="follow_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**follow_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">delete_my_follows_follow_id_alert</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.my.delete_my_follows_follow_id_alert(
    follow_id="follow_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**follow_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">retrieve_a_list_of_live_listings_for_the_seller_to_search_all_listings_specify_state_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of live listings for the seller. To search all listings specify state=all
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.retrieve_a_list_of_live_listings_for_the_seller_to_search_all_listings_specify_state_all()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search query.
    
</dd>
</dl>

<dl>
<dd>

**auction_price_max:** `typing.Optional[float]` — Maximum current auction price
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` — Category slug from /api/categories
    
</dd>
</dl>

<dl>
<dd>

**product_type:** `typing.Optional[str]` — Product type slug from /api/categories
    
</dd>
</dl>

<dl>
<dd>

**conditions:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint
    
</dd>
</dl>

<dl>
<dd>

**decade:** `typing.Optional[str]` — Decade: e.g. 1970s, early 70s
    
</dd>
</dl>

<dl>
<dd>

**finish:** `typing.Optional[str]` — Visual finish of the item, common for guitars
    
</dd>
</dl>

<dl>
<dd>

**handmade:** `typing.Optional[bool]` — Handmade items only
    
</dd>
</dl>

<dl>
<dd>

**item_city:** `typing.Optional[str]` — City where item is located
    
</dd>
</dl>

<dl>
<dd>

**item_country:** `typing.Optional[str]` — DEPRECATED - Country code where item is located
    
</dd>
</dl>

<dl>
<dd>

**item_region:** `typing.Optional[str]` — Country code where item is located
    
</dd>
</dl>

<dl>
<dd>

**item_state:** `typing.Optional[str]` — State or region code where item is located
    
</dd>
</dl>

<dl>
<dd>

**make:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Make(s)/brand of item (e.g. Fender). Can take a single value or an array.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — Model of item (e.g. Stratocaster)
    
</dd>
</dl>

<dl>
<dd>

**must_not:** `typing.Optional[str]` — Search term negation. If you want to exclude a term, add it here
    
</dd>
</dl>

<dl>
<dd>

**price_max:** `typing.Optional[float]` — Maximum price of search results (USD)
    
</dd>
</dl>

<dl>
<dd>

**price_min:** `typing.Optional[float]` — Minimum price of search results (USD)
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — The currency to be used for the price filters
    
</dd>
</dl>

<dl>
<dd>

**year_max:** `typing.Optional[int]` — Maximum year of manufacture
    
</dd>
</dl>

<dl>
<dd>

**year_min:** `typing.Optional[int]` — Minumum year of manufacture
    
</dd>
</dl>

<dl>
<dd>

**accepts_gift_cards:** `typing.Optional[bool]` — If true, include only items that accept gift cards
    
</dd>
</dl>

<dl>
<dd>

**preferred_seller:** `typing.Optional[bool]` — If true, include only items by Reverb Preferred Sellers
    
</dd>
</dl>

<dl>
<dd>

**shop:** `typing.Optional[str]` — Slug of shop to search
    
</dd>
</dl>

<dl>
<dd>

**shop_id:** `typing.Optional[str]` — ID of shop to search
    
</dd>
</dl>

<dl>
<dd>

**listing_type:** `typing.Optional[str]` — Type of listing: auctions,offers
    
</dd>
</dl>

<dl>
<dd>

**ships_to:** `typing.Optional[str]` — Limit search to items that ship to this country code
    
</dd>
</dl>

<dl>
<dd>

**exclude_auctions:** `typing.Optional[bool]` — If true, exclude auctions
    
</dd>
</dl>

<dl>
<dd>

**accepts_payment_plans:** `typing.Optional[bool]` — If true, only show items that can be purchased with a payment plan
    
</dd>
</dl>

<dl>
<dd>

**watchers_count_min:** `typing.Optional[int]` — Minimum number of watchers (used to find popular items)
    
</dd>
</dl>

<dl>
<dd>

**not_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Listing ID negation. If you want to exclude a listing, add it here.
    
</dd>
</dl>

<dl>
<dd>

**local_pickup:** `typing.Optional[bool]` — Only items that offer local pickup
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` — Available: ["all", "draft", "ended", "live", "ordered", "sold_out", "suspended", "seller_unavailable"]. Defaults to 'live'
    
</dd>
</dl>

<dl>
<dd>

**sku:** `typing.Optional[str]` — Find a listing by sku
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">retrieve_a_list_your_draft_listings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list your draft listings
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.retrieve_a_list_your_draft_listings()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search query.
    
</dd>
</dl>

<dl>
<dd>

**auction_price_max:** `typing.Optional[float]` — Maximum current auction price
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` — Category slug from /api/categories
    
</dd>
</dl>

<dl>
<dd>

**product_type:** `typing.Optional[str]` — Product type slug from /api/categories
    
</dd>
</dl>

<dl>
<dd>

**conditions:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint
    
</dd>
</dl>

<dl>
<dd>

**decade:** `typing.Optional[str]` — Decade: e.g. 1970s, early 70s
    
</dd>
</dl>

<dl>
<dd>

**finish:** `typing.Optional[str]` — Visual finish of the item, common for guitars
    
</dd>
</dl>

<dl>
<dd>

**handmade:** `typing.Optional[bool]` — Handmade items only
    
</dd>
</dl>

<dl>
<dd>

**item_city:** `typing.Optional[str]` — City where item is located
    
</dd>
</dl>

<dl>
<dd>

**item_country:** `typing.Optional[str]` — DEPRECATED - Country code where item is located
    
</dd>
</dl>

<dl>
<dd>

**item_region:** `typing.Optional[str]` — Country code where item is located
    
</dd>
</dl>

<dl>
<dd>

**item_state:** `typing.Optional[str]` — State or region code where item is located
    
</dd>
</dl>

<dl>
<dd>

**make:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Make(s)/brand of item (e.g. Fender). Can take a single value or an array.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — Model of item (e.g. Stratocaster)
    
</dd>
</dl>

<dl>
<dd>

**must_not:** `typing.Optional[str]` — Search term negation. If you want to exclude a term, add it here
    
</dd>
</dl>

<dl>
<dd>

**price_max:** `typing.Optional[float]` — Maximum price of search results (USD)
    
</dd>
</dl>

<dl>
<dd>

**price_min:** `typing.Optional[float]` — Minimum price of search results (USD)
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — The currency to be used for the price filters
    
</dd>
</dl>

<dl>
<dd>

**year_max:** `typing.Optional[int]` — Maximum year of manufacture
    
</dd>
</dl>

<dl>
<dd>

**year_min:** `typing.Optional[int]` — Minumum year of manufacture
    
</dd>
</dl>

<dl>
<dd>

**accepts_gift_cards:** `typing.Optional[bool]` — If true, include only items that accept gift cards
    
</dd>
</dl>

<dl>
<dd>

**preferred_seller:** `typing.Optional[bool]` — If true, include only items by Reverb Preferred Sellers
    
</dd>
</dl>

<dl>
<dd>

**shop:** `typing.Optional[str]` — Slug of shop to search
    
</dd>
</dl>

<dl>
<dd>

**shop_id:** `typing.Optional[str]` — ID of shop to search
    
</dd>
</dl>

<dl>
<dd>

**listing_type:** `typing.Optional[str]` — Type of listing: auctions,offers
    
</dd>
</dl>

<dl>
<dd>

**ships_to:** `typing.Optional[str]` — Limit search to items that ship to this country code
    
</dd>
</dl>

<dl>
<dd>

**exclude_auctions:** `typing.Optional[bool]` — If true, exclude auctions
    
</dd>
</dl>

<dl>
<dd>

**accepts_payment_plans:** `typing.Optional[bool]` — If true, only show items that can be purchased with a payment plan
    
</dd>
</dl>

<dl>
<dd>

**watchers_count_min:** `typing.Optional[int]` — Minimum number of watchers (used to find popular items)
    
</dd>
</dl>

<dl>
<dd>

**not_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Listing ID negation. If you want to exclude a listing, add it here.
    
</dd>
</dl>

<dl>
<dd>

**local_pickup:** `typing.Optional[bool]` — Only items that offer local pickup
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">get_a_list_of_active_negotiations_as_a_seller</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of active negotiations as a seller
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.get_a_list_of_active_negotiations_as_a_seller()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">end_a_listing</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

End a listing
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern.my import PutMyListingsSlugStateEndRequestReason

from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.my.end_a_listing(
    slug="slug",
    reason=PutMyListingsSlugStateEndRequestReason.NOT_SOLD,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**reason:** `PutMyListingsSlugStateEndRequestReason` — The reason this listing is being ended. Valid reasons: ["not_sold", "reverb_sale"].
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">get_a_list_of_your_lists_wishlist_watch_list_etc</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of your lists (wishlist, watch list, etc)
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.get_a_list_of_your_lists_wishlist_watch_list_etc()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">get_a_list_of_active_negotiations_as_a_buyer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of active negotiations as a buyer
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.get_a_list_of_active_negotiations_as_a_buyer()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">get_offer_details</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get offer details
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.get_offer_details(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">accept_an_offer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Accept an offer
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.accept_an_offer(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[str]` — Message to include with accepted offer
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">counter_an_offer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Counter an offer
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.counter_an_offer(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**country_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**layaway_terms_slug:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[str]` — Message to include with counter offer
    
</dd>
</dl>

<dl>
<dd>

**offer_items:** `typing.Optional[
    typing.Sequence[PostMyNegotiationsIdCounterRequestOfferItemsItem]
]` 
    
</dd>
</dl>

<dl>
<dd>

**price:** `typing.Optional[PostMyNegotiationsIdCounterRequestPrice]` 
    
</dd>
</dl>

<dl>
<dd>

**quantity:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**recipient_id:** `typing.Optional[str]` — ID of the recipient of the offer. Required if you are the seller pushing an offer to a buyer.
    
</dd>
</dl>

<dl>
<dd>

**region_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**shipping_price:** `typing.Optional[PostMyNegotiationsIdCounterRequestShippingPrice]` — Shipping price (sellers only)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">decline_an_offer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Decline an offer
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.decline_an_offer(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">list_of_orders_that_need_feedback</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of orders that need feedback
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.list_of_orders_that_need_feedback()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">returns_all_orders_newest_first</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all orders, newest first.
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.returns_all_orders_newest_first()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">get_my_orders_buying_by_uuid_uuid</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.my.get_my_orders_buying_by_uuid_uuid(
    uuid_="uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**uuid_:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">returns_unpaid_orders_newest_first</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns unpaid orders, newest first.
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.returns_unpaid_orders_newest_first()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">returns_order_details_for_a_buyer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns order details for a buyer
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.returns_order_details_for_a_buyer(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">marks_an_order_as_received_by_the_buyer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Marks an order as received by the buyer
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.marks_an_order_as_received_by_the_buyer(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">get_all_seller_orders_newest_first</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all seller orders, newest first.
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.get_all_seller_orders_newest_first()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">get_unpaid_seller_orders_newest_first</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get unpaid seller orders, newest first.
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.get_unpaid_seller_orders_newest_first()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">see_previous_orders_from_buyer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

See previous orders from buyer
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.see_previous_orders_from_buyer(
    buyer_id="buyer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**buyer_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">get_my_orders_selling_by_uuid_uuid</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.my.get_my_orders_selling_by_uuid_uuid(
    uuid_="uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**uuid_:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">returns_order_details_for_a_seller</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns order details for a seller
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.returns_order_details_for_a_seller(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">marks_an_order_as_picked_up</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Marks an order as picked up
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.marks_an_order_as_picked_up(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**date:** `typing.Optional[str]` — Date the item was picked up.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">marks_an_order_as_shipped</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Marks an order as shipped
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.marks_an_order_as_shipped(
    id="id",
    provider="provider",
    send_notification=True,
    tracking_number="tracking_number",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**provider:** `str` — Shipping provider: One of UPS, USPS, FedEx, DHL Deutschland, DHLExpress, DHLGlobalMail, DHL, Canada Post, CanPar, Royal Mail, PostNL, Australia Post, EMS, La Poste - Colissimo, China Post, GLS, Parcelforce, Purolator, Interlogistica, Correos España, Ukraine Post, DPD Germany, DPD UK, DPD France, Hermes, TNT, Other
    
</dd>
</dl>

<dl>
<dd>

**send_notification:** `bool` — Should we send an email notification to the buyer
    
</dd>
</dl>

<dl>
<dd>

**tracking_number:** `str` — Tracking number provided by the shipping provider
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">initiate_a_refund_for_a_sold_order</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiate a refund for a sold order
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.initiate_a_refund_for_a_sold_order(
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

**order_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">get_payments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get payments
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.get_payments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**created_start_date:** `typing.Optional[str]` — Filter by date created in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00
    
</dd>
</dl>

<dl>
<dd>

**created_end_date:** `typing.Optional[str]` — Filter by date created in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00
    
</dd>
</dl>

<dl>
<dd>

**updated_start_date:** `typing.Optional[str]` — Filter by date modified in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00
    
</dd>
</dl>

<dl>
<dd>

**updated_end_date:** `typing.Optional[str]` — Filter by date modified in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `typing.Optional[str]` — Look up payments by order id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">get_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get payment
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.get_payment(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">get_a_list_of_payouts</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of payouts
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.get_a_list_of_payouts()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">read_the_line_items_of_a_payout</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read the line items of a payout
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.read_the_line_items_of_a_payout(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">get_a_list_of_refund_requests_as_a_seller</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of refund requests as a seller
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.get_a_list_of_refund_requests_as_a_seller()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">update_a_refund_request_for_a_sold_order</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a refund request for a sold order
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.update_a_refund_request_for_a_sold_order(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">get_a_list_of_your_recently_viewed_listings</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of your recently viewed listings.
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.get_a_list_of_your_recently_viewed_listings()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">get_a_list_of_wishlisted_items</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of wishlisted items
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.get_a_list_of_wishlisted_items()

```
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

<details><summary><code>client.my.<a href="src/fern/my/client.py">add_a_listing_to_your_wishlist</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a listing to your wishlist
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.add_a_listing_to_your_wishlist(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.my.<a href="src/fern/my/client.py">remove_a_listing_from_your_wishlist</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a listing from your wishlist
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.my.remove_a_listing_from_your_wishlist(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.orders.<a href="src/fern/orders/client.py">feedback_details_for_an_orders_buyer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Feedback details for an order's buyer
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.orders.feedback_details_for_an_orders_buyer(
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

**order_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/fern/orders/client.py">add_feedback_about_an_orders_buyer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add feedback about an order's buyer
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.orders.add_feedback_about_an_orders_buyer(
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

**order_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/fern/orders/client.py">feedback_details_for_an_orders_seller</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Feedback details for an order's seller
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.orders.feedback_details_for_an_orders_seller(
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

**order_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/fern/orders/client.py">add_feedback_about_an_orders_seller</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add feedback about an order's seller
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.orders.add_feedback_about_an_orders_seller(
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

**order_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PaymentMethods
<details><summary><code>client.payment_methods.<a href="src/fern/payment_methods/client.py">get_list_of_payment_methods</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get list of payment methods
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.payment_methods.get_list_of_payment_methods()

```
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

## Priceguide
<details><summary><code>client.priceguide.<a href="src/fern/priceguide/client.py">get_a_summary_of_transactions_for_a_given_price_guide</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a summary of transactions for a given price guide
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.priceguide.get_a_summary_of_transactions_for_a_given_price_guide(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**number_of_months:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**condition:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Products
<details><summary><code>client.products.<a href="src/fern/products/client.py">view_a_review</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View a review
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.products.view_a_review(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/fern/products/client.py">update_a_review</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a review
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.products.update_a_review(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[str]` — Content of the review
    
</dd>
</dl>

<dl>
<dd>

**rating:** `typing.Optional[int]` — Rating from 1 to 5
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Title for the review
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/fern/products/client.py">view_reviews_of_a_comparison_shopping_page</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View reviews of a comparison shopping page
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.products.view_reviews_of_a_comparison_shopping_page(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/fern/products/client.py">create_a_review_for_a_product</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a review for a product
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.products.create_a_review_for_a_product(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sales
<details><summary><code>client.sales.<a href="src/fern/sales/client.py">view_upcoming_and_live_reverb_official_sales</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View upcoming and live Reverb official sales.
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.sales.view_upcoming_and_live_reverb_official_sales()

```
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

<details><summary><code>client.sales.<a href="src/fern/sales/client.py">view_your_created_sales</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

View your created sales.
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.sales.view_your_created_sales()

```
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

<details><summary><code>client.sales.<a href="src/fern/sales/client.py">add_listings_to_a_sale</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add listings to a sale
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.sales.add_listings_to_a_sale(
    sale_id="sale_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sale_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sales.<a href="src/fern/sales/client.py">remove_a_listing_from_a_sale</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a listing from a sale
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.sales.remove_a_listing_from_a_sale(
    sale_id="sale_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sale_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sales.<a href="src/fern/sales/client.py">get_sales_slug</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.sales.get_sales_slug(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Shipping
<details><summary><code>client.shipping.<a href="src/fern/shipping/client.py">list_of_supported_shipping_providers</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of supported shipping providers
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.shipping.list_of_supported_shipping_providers()

```
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

<details><summary><code>client.shipping.<a href="src/fern/shipping/client.py">get_shipping_regions</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.shipping.get_shipping_regions()

```
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

## Shop
<details><summary><code>client.shop.<a href="src/fern/shop/client.py">get_your_own_shop_details</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get your own shop details
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.shop.get_your_own_shop_details()

```
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

<details><summary><code>client.shop.<a href="src/fern/shop/client.py">update_your_shop_profile</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update your shop profile
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.shop.update_your_shop_profile()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**address:** `typing.Optional[PutShopRequestAddress]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[PutShopRequestCurrency]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**legal_country_code:** `typing.Optional[PutShopRequestLegalCountryCode]` 
    
</dd>
</dl>

<dl>
<dd>

**legal_country_code_confirmed:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**payment_policy:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**return_policy:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**shipping_policy:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**shop_type:** `typing.Optional[PutShopRequestShopType]` 
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shop.<a href="src/fern/shop/client.py">list_of_supported_product_conditions</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of supported product conditions
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.shop.list_of_supported_product_conditions()

```
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

<details><summary><code>client.shop.<a href="src/fern/shop/client.py">get_accepted_payment_methods</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get accepted payment methods
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.shop.get_accepted_payment_methods()

```
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

<details><summary><code>client.shop.<a href="src/fern/shop/client.py">returns_shop_vacation_status</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns shop vacation status
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.shop.returns_shop_vacation_status()

```
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

<details><summary><code>client.shop.<a href="src/fern/shop/client.py">enable_vacation_mode_all_listings_will_be_unavailable_until_vacation_mode_is_turned_off</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enable vacation mode. All listings will be unavailable until vacation mode is turned off.
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.shop.enable_vacation_mode_all_listings_will_be_unavailable_until_vacation_mode_is_turned_off()

```
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

<details><summary><code>client.shop.<a href="src/fern/shop/client.py">disable_vacation_mode_all_listings_will_be_re_enabled</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disable vacation mode. All listings will be re-enabled.
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.shop.disable_vacation_mode_all_listings_will_be_re_enabled()

```
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

## Shops
<details><summary><code>client.shops.<a href="src/fern/shops/client.py">get_storefront_details_on_a_shop</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get storefront details on a shop.
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.shops.get_storefront_details_on_a_shop(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shops.<a href="src/fern/shops/client.py">list_of_shipping_profiles_for_your_shop</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of shipping profiles for your shop
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.shops.list_of_shipping_profiles_for_your_shop(
    shop_id="shop_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**shop_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shops.<a href="src/fern/shops/client.py">get_details_on_a_shop</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details on a shop.
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.shops.get_details_on_a_shop(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**include_listing_count:** `typing.Optional[bool]` — Include the live listing count in the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shops.<a href="src/fern/shops/client.py">get_sellers_feedback</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get seller's feedback
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.shops.get_sellers_feedback(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shops.<a href="src/fern/shops/client.py">get_sellers_feedback_as_a_buyer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get seller's feedback as a buyer
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.shops.get_sellers_feedback_as_a_buyer(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shops.<a href="src/fern/shops/client.py">get_sellers_feedback_as_a_seller</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get seller's feedback as a seller
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.shops.get_sellers_feedback_as_a_seller(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**slug:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Wants
<details><summary><code>client.wants.<a href="src/fern/wants/client.py">a_list_of_wanted_items_by_the_user</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A list of wanted items by the user
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.wants.a_list_of_wanted_items_by_the_user()

```
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

<details><summary><code>client.wants.<a href="src/fern/wants/client.py">mark_an_item_wanted_returns200on_success_or422on_failure</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mark an item wanted. Returns 200 on success or 422 on failure.
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.wants.mark_an_item_wanted_returns200on_success_or422on_failure(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.wants.<a href="src/fern/wants/client.py">unmark_an_item_wanted</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unmark an item wanted.
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.wants.unmark_an_item_wanted(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks
<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">get_webhook_registrations</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get webhook registrations
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.webhooks.get_webhook_registrations()

```
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

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">register_a_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register a webhook
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern.webhooks import PostWebhooksRegistrationsRequestTopic

from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
)
client.webhooks.register_a_webhook(
    topic=PostWebhooksRegistrationsRequestTopic.LISTINGS_UPDATE,
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

**topic:** `PostWebhooksRegistrationsRequestTopic` — Valid values: listings/update, listings/publish, listings/bumps-ran-out, orders/create, orders/update, payments/create, payments/update, app/uninstalled
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">get_details_of_a_webhook_registration</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a webhook registration
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.webhooks.get_details_of_a_webhook_registration(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">remove_a_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a webhook
</dd>
</dl>
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
    token="YOUR_TOKEN",
)
client.webhooks.remove_a_webhook(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

