# Reference
## Studies
<details><summary><code>client.studies.<a href="src/fern/studies/client.py">get_investigation_results</a>(...) -> Investigation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Multiple studies in tabular form
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.studies import GetInvestigationResultsRequestDb, GetInvestigationResultsRequestType

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.studies.get_investigation_results(
    db=GetInvestigationResultsRequestDb.CALIBRATE,
    type=GetInvestigationResultsRequestType.BYINVESTIGATION,
    search="PC_GRANULOMETRY_SECTION",
    inchikey="YUYCVXFAYWRXLS-UHFFFAOYSA-N",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**db:** `GetInvestigationResultsRequestDb` — Database ID
    
</dd>
</dl>

<dl>
<dd>

**type:** `GetInvestigationResultsRequestType` — query type
    
</dd>
</dl>

<dl>
<dd>

**search:** `str` — Search parameter, UUID of the investigation or a substance
    
</dd>
</dl>

<dl>
<dd>

**inchikey:** `typing.Optional[str]` — Search parameter, InChI key(s) of the substance component(s), comma delimited
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Search parameter, chemical structure or substance identifier(s), comma delimited
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Starting page
    
</dd>
</dl>

<dl>
<dd>

**pagesize:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.studies.<a href="src/fern/studies/client.py">get_endpoint_summary</a>(...) -> Facet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns endpoint summary
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.studies import GetEndpointSummaryRequestDb

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.studies.get_endpoint_summary(
    db=GetEndpointSummaryRequestDb.CALIBRATE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**db:** `GetEndpointSummaryRequestDb` — Database ID
    
</dd>
</dl>

<dl>
<dd>

**top:** `typing.Optional[GetEndpointSummaryRequestTop]` — Top endpoint category
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` — Endpoint category (The value in the protocol.category.code field)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.studies.<a href="src/fern/studies/client.py">get_substance_study</a>(...) -> SubstanceStudy</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns substance study representation
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.studies import GetSubstanceStudyRequestDb

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.studies.get_substance_study(
    db=GetSubstanceStudyRequestDb.CALIBRATE,
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

**db:** `GetSubstanceStudyRequestDb` — Database ID
    
</dd>
</dl>

<dl>
<dd>

**uuid:** `str` — Substance UUID
    
</dd>
</dl>

<dl>
<dd>

**top:** `typing.Optional[GetSubstanceStudyRequestTop]` — Top endpoint category
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` — Endpoint category (The value in the protocol.category.code field)
    
</dd>
</dl>

<dl>
<dd>

**property_uri:** `typing.Optional[str]` — Property URI https://data.enanomapper.net/property/{UUID} , see Property service
    
</dd>
</dl>

<dl>
<dd>

**property:** `typing.Optional[str]` — Property UUID
    
</dd>
</dl>

<dl>
<dd>

**investigation_uuid:** `typing.Optional[str]` — Investigation UUID, a code to link different studies
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Starting page
    
</dd>
</dl>

<dl>
<dd>

**pagesize:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.studies.<a href="src/fern/studies/client.py">get_substance_study_summary</a>(...) -> SubstanceStudySummary</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Study summary
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.studies import GetSubstanceStudySummaryRequestDb

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.studies.get_substance_study_summary(
    db=GetSubstanceStudySummaryRequestDb.CALIBRATE,
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

**db:** `GetSubstanceStudySummaryRequestDb` — Database ID
    
</dd>
</dl>

<dl>
<dd>

**uuid:** `str` — Substance UUID
    
</dd>
</dl>

<dl>
<dd>

**top:** `typing.Optional[GetSubstanceStudySummaryRequestTop]` — Top endpoint category
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` — Endpoint category (The value in the protocol.category.code field)
    
</dd>
</dl>

<dl>
<dd>

**property_uri:** `typing.Optional[str]` — Property URI https://data.enanomapper.net/property/{UUID} , see Property service
    
</dd>
</dl>

<dl>
<dd>

**property:** `typing.Optional[str]` — Property UUID, see Property service
    
</dd>
</dl>

<dl>
<dd>

**result:** `typing.Optional[bool]` — If true will group by topcategory,endpointcategory,interpretation result
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Starting page
    
</dd>
</dl>

<dl>
<dd>

**pagesize:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Structures
<details><summary><code>client.structures.<a href="src/fern/structures/client.py">search_by_identifier</a>(...) -> Dataset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns compounds found
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.structures import SearchByIdentifierRequestDb, SearchByIdentifierRequestTerm, SearchByIdentifierRequestRepresentation

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.structures.search_by_identifier(
    db=SearchByIdentifierRequestDb.CALIBRATE,
    term=SearchByIdentifierRequestTerm.SEARCH,
    representation=SearchByIdentifierRequestRepresentation.ALL,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**db:** `SearchByIdentifierRequestDb` — Database ID
    
</dd>
</dl>

<dl>
<dd>

**term:** `SearchByIdentifierRequestTerm` — search term type
    
</dd>
</dl>

<dl>
<dd>

**representation:** `SearchByIdentifierRequestRepresentation` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Compound identifier (SMILES, InChI, name, registry identifiers)
    
</dd>
</dl>

<dl>
<dd>

**b64search:** `typing.Optional[str]` — Base64 encoded mol file; if included, will be used instead of the 'search' parameter
    
</dd>
</dl>

<dl>
<dd>

**casesens:** `typing.Optional[bool]` — Case sensitive search if yes
    
</dd>
</dl>

<dl>
<dd>

**bundle_uri:** `typing.Optional[str]` — Bundle URI
    
</dd>
</dl>

<dl>
<dd>

**sameas:** `typing.Optional[str]` — Ontology URI to define groups of columns
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Starting page
    
</dd>
</dl>

<dl>
<dd>

**pagesize:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.structures.<a href="src/fern/structures/client.py">search_by_similarity</a>(...) -> Dataset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns similar compounds
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.structures import SearchBySimilarityRequestDb

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.structures.search_by_similarity(
    db=SearchBySimilarityRequestDb.CALIBRATE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**db:** `SearchBySimilarityRequestDb` — Database ID
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Compound identifier (SMILES, InChI, name, registry identifiers)
    
</dd>
</dl>

<dl>
<dd>

**b64search:** `typing.Optional[str]` — Base64 encoded mol file; if included, will be used instead of the 'search' parameter
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[SearchBySimilarityRequestType]` — Defines the expected content of the search parameter
    
</dd>
</dl>

<dl>
<dd>

**threshold:** `typing.Optional[float]` — Similarity threshold
    
</dd>
</dl>

<dl>
<dd>

**dataset_uri:** `typing.Optional[str]` — Restrict the search within the AMBIT dataset specified with the URI
    
</dd>
</dl>

<dl>
<dd>

**filter_by_substance:** `typing.Optional[bool]` — Restrict the search within the set of structures with assigned substances
    
</dd>
</dl>

<dl>
<dd>

**bundle_uri:** `typing.Optional[str]` — If the structure is used in the specified bundle URI, the selection tag will be returned
    
</dd>
</dl>

<dl>
<dd>

**sameas:** `typing.Optional[str]` — Ontology URI to define groups of columns
    
</dd>
</dl>

<dl>
<dd>

**mol:** `typing.Optional[bool]` — Only for application/json; to include mol as JSON field
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Starting page
    
</dd>
</dl>

<dl>
<dd>

**pagesize:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.structures.<a href="src/fern/structures/client.py">search_by_smarts</a>(...) -> Dataset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns compounds with the specified substructure
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.structures import SearchBySmartsRequestDb

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.structures.search_by_smarts(
    db=SearchBySmartsRequestDb.CALIBRATE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**db:** `SearchBySmartsRequestDb` — Database ID
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Compound identifier (SMILES, InChI, name, registry identifiers)
    
</dd>
</dl>

<dl>
<dd>

**b64search:** `typing.Optional[str]` — Base64 encoded mol file; if included, will be used instead of the 'search' parameter
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[SearchBySmartsRequestType]` — Defines the expected content of the search parameter
    
</dd>
</dl>

<dl>
<dd>

**dataset_uri:** `typing.Optional[str]` — Restrict the search within the AMBIT dataset specified with the URI
    
</dd>
</dl>

<dl>
<dd>

**filter_by_substance:** `typing.Optional[bool]` — Restrict the search within the set of structures with assigned substances
    
</dd>
</dl>

<dl>
<dd>

**bundle_uri:** `typing.Optional[str]` — If the structure is used in the specified bundle URI, the selection tag will be returned
    
</dd>
</dl>

<dl>
<dd>

**sameas:** `typing.Optional[str]` — Ontology URI to define groups of columns
    
</dd>
</dl>

<dl>
<dd>

**mol:** `typing.Optional[bool]` — Only for application/json; to include mol as JSON field
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Starting page
    
</dd>
</dl>

<dl>
<dd>

**pagesize:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.structures.<a href="src/fern/structures/client.py">get_substance_composition</a>(...) -> SubstanceComposition</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns substance composition
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.structures import GetSubstanceCompositionRequestDb

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.structures.get_substance_composition(
    db=GetSubstanceCompositionRequestDb.CALIBRATE,
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

**db:** `GetSubstanceCompositionRequestDb` — Database ID
    
</dd>
</dl>

<dl>
<dd>

**uuid:** `str` — Substance UUID
    
</dd>
</dl>

<dl>
<dd>

**all:** `typing.Optional[bool]` — true (Show all compositions) false (do not show hidden compositions)
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Starting page
    
</dd>
</dl>

<dl>
<dd>

**pagesize:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.structures.<a href="src/fern/structures/client.py">get_substance_structures</a>(...) -> Dataset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns substance composition
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.structures import GetSubstanceStructuresRequestDb

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.structures.get_substance_structures(
    db=GetSubstanceStructuresRequestDb.CALIBRATE,
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

**db:** `GetSubstanceStructuresRequestDb` — Database ID
    
</dd>
</dl>

<dl>
<dd>

**uuid:** `str` — Substance UUID
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Starting page
    
</dd>
</dl>

<dl>
<dd>

**pagesize:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Substances
<details><summary><code>client.substances.<a href="src/fern/substances/client.py">get_substances</a>(...) -> Substance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of substances, according to the search criteria
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.substances import GetSubstancesRequestDb

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.substances.get_substances(
    db=GetSubstancesRequestDb.CALIBRATE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**db:** `GetSubstancesRequestDb` — Database ID
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search parameter
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GetSubstancesRequestType]` 
    
</dd>
</dl>

<dl>
<dd>

**compound_uri:** `typing.Optional[str]` — If type=related finds all substances containing this compound; if typ =reference - finds all substances with this compound as reference structure
    
</dd>
</dl>

<dl>
<dd>

**bundle_uri:** `typing.Optional[str]` — Retrieves if selected in this bundle
    
</dd>
</dl>

<dl>
<dd>

**add_dummy_substance:** `typing.Optional[bool]` — Adds a compound record as substance in JSON; only if type=related
    
</dd>
</dl>

<dl>
<dd>

**studysummary:** `typing.Optional[bool]` — If true retrieves study summary for each substance
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Starting page
    
</dd>
</dl>

<dl>
<dd>

**pagesize:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.substances.<a href="src/fern/substances/client.py">get_substance_by_uuid</a>(...) -> Substance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns substance representation
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.substances import GetSubstanceByUuidRequestDb

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.substances.get_substance_by_uuid(
    db=GetSubstanceByUuidRequestDb.CALIBRATE,
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

**db:** `GetSubstanceByUuidRequestDb` — Database ID
    
</dd>
</dl>

<dl>
<dd>

**uuid:** `str` — Substance UUID
    
</dd>
</dl>

<dl>
<dd>

**property_uris_array:** `typing.Optional[str]` — Property URIs
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Starting page
    
</dd>
</dl>

<dl>
<dd>

**pagesize:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.search.<a href="src/fern/search/client.py">solrquery_get</a>(...) -> SolrResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

GET is simpler to use, but imposes restrictions on the complexity and the lenght of the parameters.
</dd>
</dl>
</dd>
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

client.search.solrquery_get(
    q="*:*",
    fl="*",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `typing.Optional[str]` — The query
    
</dd>
</dl>

<dl>
<dd>

**fq:** `typing.Optional[str]` — Filter query
    
</dd>
</dl>

<dl>
<dd>

**fl:** `typing.Optional[str]` — Field list
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[int]` — Starting page
    
</dd>
</dl>

<dl>
<dd>

**rows:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**wt:** `typing.Optional[SolrqueryGetRequestWt]` — Response format
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.search.<a href="src/fern/search/client.py">solrquery_post</a>(...) -> SolrResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

POST is more complex to use, but also allows for much for complex and lengthy queries.
</dd>
</dl>
</dd>
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

client.search.solrquery_post()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**wt:** `typing.Optional[SolrqueryPostRequestWt]` — Response format
    
</dd>
</dl>

<dl>
<dd>

**facet:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[SolrqueryPostRequestParams]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

