# Reference
## PersonEndpoints
<details><summary><code>client.person_endpoints.<a href="src/fern/person_endpoints/client.py">person_enrich</a>(...) -> Person</code></summary>
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

client.person_endpoints.person_enrich(
    pdl_id="qEnOZ5Oh0poWnQ1luFBfVw_0000",
    name="Jennifer C. Jackson",
    first_name="Jennifer",
    last_name="Jackson",
    middle_name="Cassandra",
    location="Medford, OR USA",
    street_address="1234 Main Street",
    locality="Boise",
    region="Idaho",
    country="United States",
    postal_code="83701",
    company="Amazon",
    school="University of Iowa",
    phone="+1 555-234-1234",
    email="renee.c.paulsen1959@yahoo.com",
    email_hash="e206e6cd7fa5f9499fd6d2d943dcf7d9c1469bad351061483f5ce7181663b8d4",
    profile="https://linkedin.com/in/seanthorne",
    lid="145991517",
    birth_date="1996-10-01",
    data_include="full_name,emails.address",
    required="education AND (emails OR phone_numbers)",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pdl_id:** `typing.Optional[str]` — The PDL ID of the person to enrich
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The person's full name, at least first and last
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The person's first name
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The person's last name
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[str]` — The person's middle name
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — A location in which a person lives
    
</dd>
</dl>

<dl>
<dd>

**street_address:** `typing.Optional[str]` — A street address in which the person lives
    
</dd>
</dl>

<dl>
<dd>

**locality:** `typing.Optional[str]` — A locality in which the person lives
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — A state or region in which the person lives
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — A country in which the person lives
    
</dd>
</dl>

<dl>
<dd>

**postal_code:** `typing.Optional[str]` — The postal code where the person lives. If there is no value for country, the postal code is assumed to be US
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[str]` — A name, website, or social url of a company where the person has worked
    
</dd>
</dl>

<dl>
<dd>

**school:** `typing.Optional[str]` — A name, website, or social url of a university or college the person has attended
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — A phone number the person has used
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — An email the person has used
    
</dd>
</dl>

<dl>
<dd>

**email_hash:** `typing.Optional[str]` — A SHA-256 or MD5 email hash
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[str]` — A social profile the person has used. https://docs.peopledatalabs.com/docs/social-networks
    
</dd>
</dl>

<dl>
<dd>

**lid:** `typing.Optional[str]` — The person's LinkedIn ID
    
</dd>
</dl>

<dl>
<dd>

**birth_date:** `typing.Optional[str]` — The person's birth date: either the year or a full birth date in the format YYYY-MM-DD
    
</dd>
</dl>

<dl>
<dd>

**data_include:** `typing.Optional[str]` — A comma-separated string of fields that you would like the response to include. Begin the string with a - if you would instead like to exclude the specified fields. If you would like to exclude all data from being returned, use data_include=""
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Whether the output should have human-readable indentation
    
</dd>
</dl>

<dl>
<dd>

**min_likelihood:** `typing.Optional[int]` — The minimum likelihood score that a response must have in order to count as a match
    
</dd>
</dl>

<dl>
<dd>

**include_if_matched:** `typing.Optional[bool]` — If set to true, includes a top-level (alongside "data", "status", etc) field "matched" which includes a value for each queried field parameter that was "matched-on" during our internal query.
    
</dd>
</dl>

<dl>
<dd>

**required:** `typing.Optional[str]` — The fields a response must have in order to count as a match
    
</dd>
</dl>

<dl>
<dd>

**titlecase:** `typing.Optional[bool]` — Setting titlecase to true will titlecase the person data in 200 responses.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.person_endpoints.<a href="src/fern/person_endpoints/client.py">person_identify</a>(...) -> Person</code></summary>
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

client.person_endpoints.person_identify(
    name="Jennifer C. Jackson",
    first_name="Jennifer",
    last_name="Jackson",
    middle_name="Cassandra",
    location="Medford, OR USA",
    street_address="1234 Main Street",
    locality="Boise",
    region="Idaho",
    country="United States",
    postal_code="83701",
    company="Amazon",
    school="University of Iowa",
    phone="+1 555-234-1234",
    email="renee.c.paulsen1959@yahoo.com",
    email_hash="e206e6cd7fa5f9499fd6d2d943dcf7d9c1469bad351061483f5ce7181663b8d4",
    profile="https://linkedin.com/in/seanthorne",
    lid="145991517",
    birth_date="1996-10-01",
    data_include="full_name,emails.address",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` — The person's full name, at least first and last
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The person's first name
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The person's last name
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[str]` — The person's middle name
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — A location in which a person lives
    
</dd>
</dl>

<dl>
<dd>

**street_address:** `typing.Optional[str]` — A street address in which the person lives
    
</dd>
</dl>

<dl>
<dd>

**locality:** `typing.Optional[str]` — A locality in which the person lives
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — A state or region in which the person lives
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — A country in which the person lives
    
</dd>
</dl>

<dl>
<dd>

**postal_code:** `typing.Optional[str]` — The postal code where the person lives. If there is no value for country, the postal code is assumed to be US
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[str]` — A name, website, or social url of a company where the person has worked
    
</dd>
</dl>

<dl>
<dd>

**school:** `typing.Optional[str]` — A name, website, or social url of a university or college the person has attended
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — A phone number the person has used
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — An email the person has used
    
</dd>
</dl>

<dl>
<dd>

**email_hash:** `typing.Optional[str]` — A sha256 email hash
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[str]` — A social profile the person has used. https://docs.peopledatalabs.com/docs/social-networks
    
</dd>
</dl>

<dl>
<dd>

**lid:** `typing.Optional[str]` — The person's LinkedIn ID
    
</dd>
</dl>

<dl>
<dd>

**birth_date:** `typing.Optional[str]` — The person's birth date: either the year or a full birth date in the format YYYY-MM-DD
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Whether the output should have human-readable indentation
    
</dd>
</dl>

<dl>
<dd>

**titlecase:** `typing.Optional[bool]` — Setting titlecase to true will titlecase the person data in 200 responses.
    
</dd>
</dl>

<dl>
<dd>

**data_include:** `typing.Optional[str]` — A comma-separated string of fields that you would like the response to include. Begin the string with a - if you would instead like to exclude the specified fields. If you would like to exclude all data from being returned, use data_include=""
    
</dd>
</dl>

<dl>
<dd>

**include_if_matched:** `typing.Optional[bool]` — If true, the response will include the field matches.matched_on that contains a list of every query input that matched this profile
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.person_endpoints.<a href="src/fern/person_endpoints/client.py">person_search</a>(...) -> Person</code></summary>
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

client.person_endpoints.person_search(
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

**request:** `PostV5PersonSearchRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.person_endpoints.<a href="src/fern/person_endpoints/client.py">person_retrieve</a>(...) -> PersonRetrieve</code></summary>
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

client.person_endpoints.person_retrieve(
    person_id="person_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**person_id:** `str` — The ID of a person
    
</dd>
</dl>

<dl>
<dd>

**titlecase:** `typing.Optional[bool]` — Setting titlecase to true will titlecase the person data in 200 responses.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.person_endpoints.<a href="src/fern/person_endpoints/client.py">person_retrieve_bulk</a>(...) -> PersonRetrieveBulk</code></summary>
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

client.person_endpoints.person_retrieve_bulk()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**titlecase:** `typing.Optional[bool]` — Setting titlecase to true will titlecase the person data in 200 responses.
    
</dd>
</dl>

<dl>
<dd>

**requests:** `typing.Optional[typing.List[typing.Any]]` — requests contains a list of objects that have a Person ID and optional metadata object.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CleanerEndpoints
<details><summary><code>client.cleaner_endpoints.<a href="src/fern/cleaner_endpoints/client.py">company_clean</a>(...) -> Company</code></summary>
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

client.cleaner_endpoints.company_clean()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the company
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` — A website the company uses
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[str]` — A social profile used by the company (e.g. LinkedIn/Facebook/Twitter)
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Whether the output should have human-readable indentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cleaner_endpoints.<a href="src/fern/cleaner_endpoints/client.py">school_clean</a>(...) -> School</code></summary>
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

client.cleaner_endpoints.school_clean()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the school
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` — A website the school uses
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[str]` — A social profile used by the school (e.g. LinkedIn/Facebook/Twitter)
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Whether the output should have human-readable indentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cleaner_endpoints.<a href="src/fern/cleaner_endpoints/client.py">location_clean</a>(...) -> Location</code></summary>
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

client.cleaner_endpoints.location_clean()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location:** `typing.Optional[str]` — The raw location to process
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Whether the output should have human-readable indentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CompanyEndpoints
<details><summary><code>client.company_endpoints.<a href="src/fern/company_endpoints/client.py">company_enrich</a>(...) -> Company</code></summary>
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

client.company_endpoints.company_enrich(
    required="location AND (website OR linkedin_url)",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pdl_id:** `typing.Optional[str]` — The PDL ID of the company to enrich.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the company.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[str]` — A social profile of the company (linkedin/facebook/twitter/crunchbase).
    
</dd>
</dl>

<dl>
<dd>

**ticker:** `typing.Optional[str]` — The company's stock ticker, if publicly traded.
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` — A website the company uses.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — The location of the company's headquarters. This can be anything from a street address to a country name.
    
</dd>
</dl>

<dl>
<dd>

**street_address:** `typing.Optional[str]` — The company HQ's street address.
    
</dd>
</dl>

<dl>
<dd>

**locality:** `typing.Optional[str]` — The company HQ's locality. e.g. San Francisco
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — The company HQ's region. e.g. California
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — The company HQ's country.
    
</dd>
</dl>

<dl>
<dd>

**postal_code:** `typing.Optional[str]` — The company HQ's postal code.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Whether the output should have human-readable indentation.
    
</dd>
</dl>

<dl>
<dd>

**titlecase:** `typing.Optional[bool]` — All text in API responses returns as lowercase by default. Setting titlecase to true will titlecase response data instead.
    
</dd>
</dl>

<dl>
<dd>

**include_if_matched:** `typing.Optional[bool]` — If true, the response will include the top-level field matched that contains a list of every input that matched this profile.
    
</dd>
</dl>

<dl>
<dd>

**min_likelihood:** `typing.Optional[int]` — The minimum likelihood score a response must possess in order to return a 200.
    
</dd>
</dl>

<dl>
<dd>

**required:** `typing.Optional[str]` — The fields a response must have in order to count as a match.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.company_endpoints.<a href="src/fern/company_endpoints/client.py">company_search</a>(...) -> Company</code></summary>
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

client.company_endpoints.company_search(
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

**request:** `PostV5CompanySearchRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Autocomplete
<details><summary><code>client.autocomplete.<a href="src/fern/autocomplete/client.py">autocomplete</a>(...)</code></summary>
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

client.autocomplete.autocomplete()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**field:** `typing.Optional[PostV5AutocompleteRequestField]` — An enumerated field that will be used to calculate the autocompletion
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` — Text that is used as the seed for autocompletion
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The number of results returned for autocompletion
    
</dd>
</dl>

<dl>
<dd>

**titlecase:** `typing.Optional[bool]` — Setting titlecase to true will titlecase any records returned
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Whether the output should have human-readable indentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## IpEnrichment
<details><summary><code>client.ip_enrichment.<a href="src/fern/ip_enrichment/client.py">ip_enrich</a>(...) -> Ip</code></summary>
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

client.ip_enrichment.ip_enrich(
    ip="ip",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ip:** `str` — IP that will be enriched.
    
</dd>
</dl>

<dl>
<dd>

**return_ip_location:** `typing.Optional[bool]` — IP responses will not include location data for the IP by default.  Setting to `true` will return IP specific location info.
    
</dd>
</dl>

<dl>
<dd>

**return_ip_metadata:** `typing.Optional[bool]` — IP responses will not include metadata for the IP by default.  Setting to `true` will return IP specific metadata.
    
</dd>
</dl>

<dl>
<dd>

**return_person:** `typing.Optional[bool]` — Setting to `true` will return person fields associated with the IP.
    
</dd>
</dl>

<dl>
<dd>

**return_if_unmatched:** `typing.Optional[bool]` — Setting to `true` will return IP specific metadata or location data regardless of a company match.
    
</dd>
</dl>

<dl>
<dd>

**titlecase:** `typing.Optional[bool]` — Setting to `true` will titlecase any records returned.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Whether the output should have human-readable indentation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## JobTitleEnrichment
<details><summary><code>client.job_title_enrichment.<a href="src/fern/job_title_enrichment/client.py">job_title_enrich</a>(...) -> JobTitle</code></summary>
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

client.job_title_enrichment.job_title_enrich()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_title:** `typing.Optional[str]` — Job title that will be enriched
    
</dd>
</dl>

<dl>
<dd>

**titlecase:** `typing.Optional[bool]` — Setting titlecase to true will titlecase any records returned
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Whether the output should have human-readable indentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SkillEnrichment
<details><summary><code>client.skill_enrichment.<a href="src/fern/skill_enrichment/client.py">skill_enrich</a>(...) -> Skill</code></summary>
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

client.skill_enrichment.skill_enrich(
    skill="skill",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**skill:** `str` — skill that will be enriched.
    
</dd>
</dl>

<dl>
<dd>

**titlecase:** `typing.Optional[bool]` — Setting to `true` will titlecase any records returned.
    
</dd>
</dl>

<dl>
<dd>

**pretty:** `typing.Optional[bool]` — Whether the output should have human-readable indentation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

