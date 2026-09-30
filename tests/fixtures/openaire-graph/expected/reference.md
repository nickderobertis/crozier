# Reference
## Research products
<details><summary><code>client.research_products.<a href="src/fern/research_products/client.py">search</a>(...) -> ResearchProductsSearchResponseV2</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Explore research products exploiting various filter parameters
</dd>
</dl>
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

client.research_products.search()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**logical_operator:** `typing.Optional[SearchRequestLogicalOperator]` 

Logical operator used to combine field-level queries. Default value: *AND* </br>
Use it when specifying multiple fields in the search. </br>
*example: (mainTitle=geography) AND (description=19th century)*
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 

Keyword-based search. </br>Supports logical operators: AND, OR, NOT </br>
Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
Use parentheses `()` to group conditions and control evaluation order. </br>
*example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*
    
</dd>
</dl>

<dl>
<dd>

**main_title:** `typing.Optional[str]` 

Search in the research product's main title. </br>Supports logical operators: AND, OR, NOT </br>
Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
Use parentheses `()` to group conditions and control evaluation order. </br>
*example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 

Search in the research product's description. </br>Supports logical operators: AND, OR, NOT </br>
Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
Use parentheses `()` to group conditions and control evaluation order. </br>
*example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The OpenAIRE id of the research product. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**pid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The persistent identifier of the research product. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**original_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The identifier of the record at the original sources. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**ror_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Research Organization Registry Identifier (ROR). Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[SearchRequestTypeItem, typing.Sequence[SearchRequestTypeItem]]]` — The type of the research product. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**from_publication_date:** `typing.Optional[str]` — Gets the research products whose publication date is greater than or equal to he given date. Provide a date in YYYY or YYYY-MM-DD format
    
</dd>
</dl>

<dl>
<dd>

**to_publication_date:** `typing.Optional[str]` — Gets the research products whose publication date is less than or equal to the given date. Provide a date in YYYY or YYYY-MM-DD format
    
</dd>
</dl>

<dl>
<dd>

**subjects:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List of subjects associated to the research product. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**country_code:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The country code for the country associated with the research product. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**author_full_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The full name of the authors involved in producing this research product. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**author_orcid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The ORCiD of the authors involved in producing this research product. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**publisher:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The name of the entity that holds, archives, publishes prints, distributes, releases, issues, or produces the resource. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**best_open_access_right_label:** `typing.Optional[typing.Union[SearchRequestBestOpenAccessRightLabelItem, typing.Sequence[SearchRequestBestOpenAccessRightLabelItem]]]` — The best open access rights among the research product's instances. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**influence_class:** `typing.Optional[typing.Union[SearchRequestInfluenceClassItem, typing.Sequence[SearchRequestInfluenceClassItem]]]` — Citation-based indicator that reflects the overall impact of a research product; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and average in terms of influence respectively. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**popularity_class:** `typing.Optional[typing.Union[SearchRequestPopularityClassItem, typing.Sequence[SearchRequestPopularityClassItem]]]` — Citation-based indicator that reflects current impact or attention of a research product; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and average in terms of popularity respectively. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**impulse_class:** `typing.Optional[typing.Union[SearchRequestImpulseClassItem, typing.Sequence[SearchRequestImpulseClassItem]]]` — Citation-based indicator that reflects the initial momentum of a research product directly after its publication; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and in terms of average impulse respectively. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**citation_count_class:** `typing.Optional[typing.Union[SearchRequestCitationCountClassItem, typing.Sequence[SearchRequestCitationCountClassItem]]]` — Citation-based indicator that reflects the overall impact of a research product by summing all its citations; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and average in terms of citation count respectively. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**instance_type:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve publications of the given instance type; check <a href='http://api.openaire.eu/vocabularies/dnet:publication_resource' target='_blank'>here</a> for all possible instance type values `[Only for publications]`. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**sdg:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — Retrieves publications classified with the respective Sustainable Development Goal number (for further information check <a href='https://sdgs.un.org/goals' target='_blank'>here</a>); please provide an SDG number between 1 and 17 `[Only for publications]`. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**fos:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieves publications classified with a given Field of Science (FOS); please provide a valid <a href='https://explore.openaire.eu/assets/common-assets/vocabulary/fos.json' target='_blank'>FOS classification identifier</a>  `[Only for publications]`. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**is_peer_reviewed:** `typing.Optional[bool]` — Indicates whether the publications are peerReviewed or not `[Only for publications]`
    
</dd>
</dl>

<dl>
<dd>

**is_in_diamond_journal:** `typing.Optional[bool]` — Indicates whether the publication was published in a diamond journal or not `[Only for publications]`
    
</dd>
</dl>

<dl>
<dd>

**is_publicly_funded:** `typing.Optional[bool]` — Indicates whether the publication was publicly funded or not `[Only for publications]`
    
</dd>
</dl>

<dl>
<dd>

**is_green:** `typing.Optional[bool]` — Indicates whether the publication was published following the green open access model `[Only for publications]`
    
</dd>
</dl>

<dl>
<dd>

**open_access_color:** `typing.Optional[typing.Union[SearchRequestOpenAccessColorItem, typing.Sequence[SearchRequestOpenAccessColorItem]]]` — Specifies the Open Access color of the publication `[Only for publications]`. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_organization_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve research products connected to the organization (with OpenAIRE id). </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_community_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve research products connected to the community (with OpenAIRE id). </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_project_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve research products connected to the project (with OpenAIRE id). </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_project_code:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve research products connected to the project with code. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**has_project_rel:** `typing.Optional[bool]` — Retrieve research products that are connected to a project
    
</dd>
</dl>

<dl>
<dd>

**rel_project_funding_short_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve research products connected to a project that has a funder with the given short name. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_project_funding_stream_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve research products connected to a project that has the given funding identifier. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_hosting_data_source_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve research products hosted by the data source (with OpenAIRE id). </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_collected_from_datasource_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve research products collected from the data source (with OpenAIRE id). </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 

Page number of the results, 
used for basic start/rows pagination. 
Max dataset to retrieve - 10000 records. 
To get more than that, use cursor-based pagination.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results per page
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

Cursor-based pagination. Initial value: `cursor=*`. 
Cursor should be used when it is required to retrieve a big dataset (more than 10000 records). 
To get the next page of results, use nextCursor returned in the response.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — The field to sort the results by and the sort direction. The format should be in the format `fieldname ASC|DESC`, where fieldname is one of 'relevance', 'publicationDate', 'dateOfCollection', 'influence', 'popularity', 'citationCount', 'impulse'. Multiple sorting parameters should be comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.research_products.<a href="src/fern/research_products/client.py">get_by_id</a>(...) -> ApiResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a research product object by specifying its id.
</dd>
</dl>
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

client.research_products.get_by_id(
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

**id:** `str` — The OpenAIRE id of the research product
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.research_products.<a href="src/fern/research_products/client.py">search1</a>(...) -> ResearchProductsSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated: Use <a href="https://api.openaire.eu/graph/swagger-ui/index.html?urls.primaryName=OpenAIRE%20Graph%20API%20V2">version 2.0</a> instead.
This version is no longer supported and will be removed in the future.
</dd>
</dl>
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

client.research_products.search1()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**logical_operator:** `typing.Optional[Search1RequestLogicalOperator]` 

Logical operator used to combine field-level queries. Default value: *AND* </br>
Use it when specifying multiple fields in the search. </br>
*example: (mainTitle=geography) AND (description=19th century)*
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 

Keyword-based search. </br>Supports logical operators: AND, OR, NOT </br>
Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
Use parentheses `()` to group conditions and control evaluation order. </br>
*example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*
    
</dd>
</dl>

<dl>
<dd>

**main_title:** `typing.Optional[str]` 

Search in the research product's main title. </br>Supports logical operators: AND, OR, NOT </br>
Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
Use parentheses `()` to group conditions and control evaluation order. </br>
*example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 

Search in the research product's description. </br>Supports logical operators: AND, OR, NOT </br>
Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
Use parentheses `()` to group conditions and control evaluation order. </br>
*example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The OpenAIRE id of the research product. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**pid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The persistent identifier of the research product. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**original_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The identifier of the record at the original sources. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**ror_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Research Organization Registry Identifier (ROR). Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[Search1RequestTypeItem, typing.Sequence[Search1RequestTypeItem]]]` — The type of the research product. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**from_publication_date:** `typing.Optional[str]` — Gets the research products whose publication date is greater than or equal to he given date. Provide a date in YYYY or YYYY-MM-DD format
    
</dd>
</dl>

<dl>
<dd>

**to_publication_date:** `typing.Optional[str]` — Gets the research products whose publication date is less than or equal to the given date. Provide a date in YYYY or YYYY-MM-DD format
    
</dd>
</dl>

<dl>
<dd>

**subjects:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List of subjects associated to the research product. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**country_code:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The country code for the country associated with the research product. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**author_full_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The full name of the authors involved in producing this research product. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**author_orcid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The ORCiD of the authors involved in producing this research product. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**publisher:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The name of the entity that holds, archives, publishes prints, distributes, releases, issues, or produces the resource. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**best_open_access_right_label:** `typing.Optional[typing.Union[Search1RequestBestOpenAccessRightLabelItem, typing.Sequence[Search1RequestBestOpenAccessRightLabelItem]]]` — The best open access rights among the research product's instances. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**influence_class:** `typing.Optional[typing.Union[Search1RequestInfluenceClassItem, typing.Sequence[Search1RequestInfluenceClassItem]]]` — Citation-based indicator that reflects the overall impact of a research product; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and average in terms of influence respectively. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**popularity_class:** `typing.Optional[typing.Union[Search1RequestPopularityClassItem, typing.Sequence[Search1RequestPopularityClassItem]]]` — Citation-based indicator that reflects current impact or attention of a research product; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and average in terms of popularity respectively. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**impulse_class:** `typing.Optional[typing.Union[Search1RequestImpulseClassItem, typing.Sequence[Search1RequestImpulseClassItem]]]` — Citation-based indicator that reflects the initial momentum of a research product directly after its publication; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and in terms of average impulse respectively. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**citation_count_class:** `typing.Optional[typing.Union[Search1RequestCitationCountClassItem, typing.Sequence[Search1RequestCitationCountClassItem]]]` — Citation-based indicator that reflects the overall impact of a research product by summing all its citations; please choose a class among 'C1', 'C2', 'C3', 'C4', 'C5' for  top 0.01%, top 0.1%, top 1%, top 10%, and average in terms of citation count respectively. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**instance_type:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve publications of the given instance type; check <a href='http://api.openaire.eu/vocabularies/dnet:publication_resource' target='_blank'>here</a> for all possible instance type values `[Only for publications]`. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**sdg:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — Retrieves publications classified with the respective Sustainable Development Goal number (for further information check <a href='https://sdgs.un.org/goals' target='_blank'>here</a>); please provide an SDG number between 1 and 17 `[Only for publications]`. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**fos:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieves publications classified with a given Field of Science (FOS); please provide a valid <a href='https://explore.openaire.eu/assets/common-assets/vocabulary/fos.json' target='_blank'>FOS classification identifier</a>  `[Only for publications]`. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**is_peer_reviewed:** `typing.Optional[bool]` — Indicates whether the publications are peerReviewed or not `[Only for publications]`
    
</dd>
</dl>

<dl>
<dd>

**is_in_diamond_journal:** `typing.Optional[bool]` — Indicates whether the publication was published in a diamond journal or not `[Only for publications]`
    
</dd>
</dl>

<dl>
<dd>

**is_publicly_funded:** `typing.Optional[bool]` — Indicates whether the publication was publicly funded or not `[Only for publications]`
    
</dd>
</dl>

<dl>
<dd>

**is_green:** `typing.Optional[bool]` — Indicates whether the publication was published following the green open access model `[Only for publications]`
    
</dd>
</dl>

<dl>
<dd>

**open_access_color:** `typing.Optional[typing.Union[Search1RequestOpenAccessColorItem, typing.Sequence[Search1RequestOpenAccessColorItem]]]` — Specifies the Open Access color of the publication `[Only for publications]`. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_organization_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve research products connected to the organization (with OpenAIRE id). </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_community_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve research products connected to the community (with OpenAIRE id). </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_project_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve research products connected to the project (with OpenAIRE id). </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_project_code:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve research products connected to the project with code. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**has_project_rel:** `typing.Optional[bool]` — Retrieve research products that are connected to a project
    
</dd>
</dl>

<dl>
<dd>

**rel_project_funding_short_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve research products connected to a project that has a funder with the given short name. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_project_funding_stream_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve research products connected to a project that has the given funding identifier. </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_hosting_data_source_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve research products hosted by the data source (with OpenAIRE id). </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_collected_from_datasource_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve research products collected from the data source (with OpenAIRE id). </br> Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 

Page number of the results, 
used for basic start/rows pagination. 
Max dataset to retrieve - 10000 records. 
To get more than that, use cursor-based pagination.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results per page
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

Cursor-based pagination. Initial value: `cursor=*`. 
Cursor should be used when it is required to retrieve a big dataset (more than 10000 records). 
To get the next page of results, use nextCursor returned in the response.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — The field to sort the results by and the sort direction. The format should be in the format `fieldname ASC|DESC`, where fieldname is one of 'relevance', 'publicationDate', 'dateOfCollection', 'influence', 'popularity', 'citationCount', 'impulse'. Multiple sorting parameters should be comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.research_products.<a href="src/fern/research_products/client.py">get_by_id1</a>(...) -> GraphResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated: Use <a href="https://api.openaire.eu/graph/swagger-ui/index.html?urls.primaryName=OpenAIRE%20Graph%20API%20V2">version 2.0</a> instead.
This version is no longer supported and will be removed in the future.
</dd>
</dl>
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

client.research_products.get_by_id1(
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

**id:** `str` — The OpenAIRE id of the research product
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.research_products.<a href="src/fern/research_products/client.py">get_links</a>(...) -> SearchResponseRelation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve scholix links
</dd>
</dl>
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

client.research_products.get_links()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**target_pid:** `typing.Optional[str]` — Filter relationships by target pid
    
</dd>
</dl>

<dl>
<dd>

**target_publisher:** `typing.Optional[str]` — Filter relationships by target publisher
    
</dd>
</dl>

<dl>
<dd>

**target_type:** `typing.Optional[str]` — Filter relationships by target type (publication, dataset, software, other)
    
</dd>
</dl>

<dl>
<dd>

**source_pid:** `typing.Optional[str]` — Filter relationships by source pid
    
</dd>
</dl>

<dl>
<dd>

**source_publisher:** `typing.Optional[str]` — Filter relationships by source publisher
    
</dd>
</dl>

<dl>
<dd>

**source_type:** `typing.Optional[str]` — Filter relationships by source type (publication, dataset, software, other)
    
</dd>
</dl>

<dl>
<dd>

**relation:** `typing.Optional[str]` — Filter by specific relationships
    
</dd>
</dl>

<dl>
<dd>

**from_date:** `typing.Optional[str]` — Provide From date in YYYY or YYYY-MM-DD format
    
</dd>
</dl>

<dl>
<dd>

**to_date:** `typing.Optional[str]` — Provide To date in YYYY or YYYY-MM-DD format
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number of the results
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Page size - maximum value: 100
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.research_products.<a href="src/fern/research_products/client.py">get_relations_info</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve information about available relation types from scholexplorer
</dd>
</dl>
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

client.research_products.get_relations_info()

```
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

## Projects
<details><summary><code>client.projects.<a href="src/fern/projects/client.py">search2</a>(...) -> SearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Explore projects exploiting various filter parameters
</dd>
</dl>
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

client.projects.search2()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**logical_operator:** `typing.Optional[Search2RequestLogicalOperator]` 

Logical operator used to combine field-level queries. Default value: *AND* </br>
Use it when specifying multiple fields in the search. </br>
*example: (mainTitle=geography) AND (description=19th century)*
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 

Keyword-based search. </br>Supports logical operators: AND, OR, NOT </br>
Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
Use parentheses `()` to group conditions and control evaluation order. </br>
*example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 

Search in the project's title. </br>Supports logical operators: AND, OR, NOT </br>
Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
Use parentheses `()` to group conditions and control evaluation order. </br>
*example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*
    
</dd>
</dl>

<dl>
<dd>

**keywords:** `typing.Optional[str]` 

The project's keywords. </br>Supports logical operators: AND, OR, NOT </br>
Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
Use parentheses `()` to group conditions and control evaluation order. </br>
*example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The OpenAIRE id of the project. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The grant agreement (GA) code of the project. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**acronym:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Project's acronym. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**call_identifier:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The identifier of the research call. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**funding_short_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The short name of the funder. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**funding_stream_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The identifier of the funding stream. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**from_start_date:** `typing.Optional[str]` — Gets the projects with start date greater than or equal to the given date. Provide a date in YYYY or YYYY-MM-DD format
    
</dd>
</dl>

<dl>
<dd>

**to_start_date:** `typing.Optional[str]` — Gets the projects with start date less than or equal to the given date. Provide a date in YYYY or YYYY-MM-DD format
    
</dd>
</dl>

<dl>
<dd>

**from_end_date:** `typing.Optional[str]` — Gets the projects with end date greater than or equal to the given date. Provide a date in YYYY or YYYY-MM-DD format
    
</dd>
</dl>

<dl>
<dd>

**to_end_date:** `typing.Optional[str]` — Gets the projects with end date less than or equal to the given date. Provide a date in YYYY or YYYY-MM-DD format
    
</dd>
</dl>

<dl>
<dd>

**rel_organization_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The name or short name of the related organization. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_organization_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The organization identifier of the related organization. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_community_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve projects connected to the community (with OpenAIRE id). Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_organization_country_code:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The country code of the related organizations. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_collected_from_datasource_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve projects collected from the data source (with OpenAIRE id). Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 

Page number of the results, 
used for basic start/rows pagination. 
Max dataset to retrieve - 10000 records. 
To get more than that, use cursor-based pagination.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results per page
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

Cursor-based pagination. Initial value: `cursor=*`. 
Cursor should be used when it is required to retrieve a big dataset (more than 10000 records). 
To get the next page of results, use nextCursor returned in the response.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — The field to sort the results by and the sort direction. The format should be in the format `fieldname ASC|DESC`, where fieldname is one of 'relevance', 'startDate', 'endDate'. Multiple sorting parameters should be comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">get_by_id2</a>(...) -> ProjectSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a project object by specifying its id.
</dd>
</dl>
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

client.projects.get_by_id2(
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

**id:** `str` — The OpenAIRE id of the project
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">search8</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search and filter projects using the legacy XML API format.
</dd>
</dl>
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

client.projects.search8()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**format:** `typing.Optional[Search8RequestFormat]` — Response format
    
</dd>
</dl>

<dl>
<dd>

**keywords:** `typing.Optional[str]` — Keyword-based search
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Search in project title/name
    
</dd>
</dl>

<dl>
<dd>

**acronym:** `typing.Optional[str]` — Filter by project acronym(s)
    
</dd>
</dl>

<dl>
<dd>

**grant_id:** `typing.Optional[str]` — Filter by grant ID / project code(s)
    
</dd>
</dl>

<dl>
<dd>

**call_id:** `typing.Optional[str]` — Filter by call identifier(s)
    
</dd>
</dl>

<dl>
<dd>

**funder:** `typing.Optional[str]` — Filter by funder shortname(s)
    
</dd>
</dl>

<dl>
<dd>

**funding_stream:** `typing.Optional[str]` — Filter by funding stream name(s)
    
</dd>
</dl>

<dl>
<dd>

**openaire_publication_id:** `typing.Optional[str]` — Filter by OpenAIRE publication ID(s)
    
</dd>
</dl>

<dl>
<dd>

**participant_countries:** `typing.Optional[str]` — Filter by participant country codes
    
</dd>
</dl>

<dl>
<dd>

**participant_acronyms:** `typing.Optional[str]` — Filter by participant organization acronyms
    
</dd>
</dl>

<dl>
<dd>

**has_ec_funding:** `typing.Optional[str]` — Filter projects with EC (European Commission) funding
    
</dd>
</dl>

<dl>
<dd>

**has_wt_funding:** `typing.Optional[str]` — Filter projects with Wellcome Trust funding
    
</dd>
</dl>

<dl>
<dd>

**start_year:** `typing.Optional[str]` — Filter by project start year
    
</dd>
</dl>

<dl>
<dd>

**end_year:** `typing.Optional[str]` — Filter by project end year
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` 

sortBy=field,[ascending|descending] <br>
'field' is one of: projectstartdate, projectstartyear, projectenddate, projectendyear, projectduration
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — Page number
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[str]` — Number of results per page (max 100)
    
</dd>
</dl>

<dl>
<dd>

**cursor_mark:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Persons
<details><summary><code>client.persons.<a href="src/fern/persons/client.py">search3</a>(...) -> ApiPerson</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for persons using filters and pagination options
</dd>
</dl>
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

client.persons.search3()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**logical_operator:** `typing.Optional[Search3RequestLogicalOperator]` 

Logical operator used to combine field-level queries. Default value: *AND* </br>
Use it when specifying multiple fields in the search. </br>
*example: (mainTitle=geography) AND (description=19th century)*
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 

Keyword-based search. </br>Supports logical operators: AND, OR, NOT </br>
Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
Use parentheses `()` to group conditions and control evaluation order. </br>
*example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The OpenAIRE id of the project. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**original_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The identifier of the record at the original sources. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**given_name:** `typing.Optional[str]` 

The given name of the person. </br>Supports logical operators: AND, OR, NOT </br>
Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
Use parentheses `()` to group conditions and control evaluation order. </br>
*example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` 

The last name of the person. </br>Supports logical operators: AND, OR, NOT </br>
Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
Use parentheses `()` to group conditions and control evaluation order. </br>
*example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 

Page number of the results, 
used for basic start/rows pagination. 
Max dataset to retrieve - 10000 records. 
To get more than that, use cursor-based pagination.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results per page
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

Cursor-based pagination. Initial value: `cursor=*`. 
Cursor should be used when it is required to retrieve a big dataset (more than 10000 records). 
To get the next page of results, use nextCursor returned in the response.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — The field to sort the results by and the sort direction. The format should be in the format `fieldname ASC|DESC`, where fieldname is one of 'relevance', 'startDate', 'endDate'. Multiple sorting parameters should be comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.persons.<a href="src/fern/persons/client.py">get_by_id3</a>(...) -> GraphResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a person by id
</dd>
</dl>
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

client.persons.get_by_id3(
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

**id:** `str` — The OpenAIRE id of the person
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organizations
<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">search4</a>(...) -> OrganizationSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Explore organizations exploiting various filter parameters
</dd>
</dl>
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

client.organizations.search4()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**logical_operator:** `typing.Optional[Search4RequestLogicalOperator]` 

Logical operator used to combine field-level queries. Default value: *AND* </br>
Use it when specifying multiple fields in the search. </br>
*example: (mainTitle=geography) AND (description=19th century)*
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 

Keyword-based search. </br>Supports logical operators: AND, OR, NOT </br>
Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
Use parentheses `()` to group conditions and control evaluation order. </br>
*example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*
    
</dd>
</dl>

<dl>
<dd>

**legal_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The legal name of the organization. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**legal_short_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The legal name of the organization in short form. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The OpenAIRE id of the organization. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**pid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The persistent identifier of the organization. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**country_code:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The country code of the organization. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_community_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve organizations connected to the community (with OpenAIRE id). Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_collected_from_datasource_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve organizations collected from the data source (with OpenAIRE id). Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 

Page number of the results, 
used for basic start/rows pagination. 
Max dataset to retrieve - 10000 records. 
To get more than that, use cursor-based pagination.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results per page
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

Cursor-based pagination. Initial value: `cursor=*`. 
Cursor should be used when it is required to retrieve a big dataset (more than 10000 records). 
To get the next page of results, use nextCursor returned in the response.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — The field to sort the results by and the sort direction. The format should be in the format `fieldname ASC|DESC`, organizations can be only sorted by the 'relevance'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organizations.<a href="src/fern/organizations/client.py">get_by_id4</a>(...) -> ApiOrganization</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a organization object by specifying its id.
</dd>
</dl>
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

client.organizations.get_by_id4(
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

**id:** `str` — The OpenAIRE id of the project
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Data sources
<details><summary><code>client.data_sources.<a href="src/fern/data_sources/client.py">search5</a>(...) -> DataSourceSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Explore data sources exploiting various filter parameters
</dd>
</dl>
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

client.data_sources.search5()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**logical_operator:** `typing.Optional[Search5RequestLogicalOperator]` 

Logical operator used to combine field-level queries. Default value: *AND* </br>
Use it when specifying multiple fields in the search. </br>
*example: (mainTitle=geography) AND (description=19th century)*
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 

Keyword-based search. </br>Supports logical operators: AND, OR, NOT </br>
Logical operators must be in UPPERCASE (AND, OR, NOT). Lowercase operators (and, or, not) are treated as ***search terms***, not as operators. </br>
Use parentheses `()` to group conditions and control evaluation order. </br>
*example: ((geography OR physics) AND (applied mathematics)) OR (literature and arts)*
    
</dd>
</dl>

<dl>
<dd>

**official_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The official name of the data source. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**english_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The English name of the data source. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**legal_short_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The legal name of the organization in short form. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The OpenAIRE id of the data source. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**pid:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The persistent identifier of the data source. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**subjects:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List of subjects associated to the datasource. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**data_source_type_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The data source type; see all possible values <a href='https://api.openaire.eu/vocabularies/dnet:datasource_typologies' target='_blank'>here</a>. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**content_types:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Types of content in the data source, as defined by OpenDOAR. Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_organization_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve data sources connected to the organization (with OpenAIRE id). Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_community_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve data sources connected to the community (with OpenAIRE id). Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**rel_collected_from_datasource_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Retrieve data sources collected from the data source (with OpenAIRE id). Logical operator: *OR*
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 

Page number of the results, 
used for basic start/rows pagination. 
Max dataset to retrieve - 10000 records. 
To get more than that, use cursor-based pagination.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results per page
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

Cursor-based pagination. Initial value: `cursor=*`. 
Cursor should be used when it is required to retrieve a big dataset (more than 10000 records). 
To get the next page of results, use nextCursor returned in the response.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — The field to sort the results by and the sort direction. The format should be in the format `fieldname ASC|DESC`, organizations can be only sorted by the 'relevance'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_sources.<a href="src/fern/data_sources/client.py">get_by_id5</a>(...) -> Datasource</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a data source object by specifying its id.
</dd>
</dl>
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

client.data_sources.get_by_id5(
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

**id:** `str` — The OpenAIRE id of the data source
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.products.<a href="src/fern/products/client.py">search6</a>(...) -> SkgIfJsonLdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of `product` matching the provided filter criteria.
</dd>
</dl>
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

client.products.search6(
    filter="product_type:publication",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter:** `str` 

   Filter string with pipe-separated values for multiple values per key.

   **Format:** `key1:value1|value2,key2:value3`

   **Examples:**
   - Single values: `product_type:publication,cf.search.title:ocean`
   - Multiple values: `product_type:publication|dataset|software`
   - Mixed: `product_type:publication|dataset,cf.search.title:ocean`

   **IMPORTANT:** Duplicate keys are not allowed (use pipe `|` to separate multiple values)

   **Attribute Filters:**
- `product_type`: publication, dataset, software, other
- `identifiers.id`: product identifier (DOI, arXiv, etc.)
- `identifiers.scheme`: identifier scheme (doi, arxiv, etc.)
- `contributions.by.local_identifier`: contributor local ID
- `contributions.by.identifiers.id`: contributor identifier (ORCID, etc.)
- `contributions.by.identifiers.scheme`: contributor ID scheme (orcid, etc.)
- `contributions.by.family_name`: contributor family name
- `contributions.by.given_name`: contributor given name
- `contributions.by.name`: contributor full name
- `contributions.declared_affiliations.local_identifier`: affiliation local ID
- `contributions.declared_affiliations.identifiers.id`: affiliation identifier
- `contributions.declared_affiliations.identifiers.scheme`: affiliation ID scheme
- `contributions.declared_affiliations.name`: affiliation name
- `contributions.declared_affiliations.short_name`: affiliation short name
- `funding.local_identifier`: funding local identifier
- `funding.grant_number`: funding grant number
- `funding.identifiers.id`: funding identifier
- `funding.identifiers.scheme`: funding identifier scheme

**Convenience Filters:**
- `cf.search.title`: title search
- `cf.search.title_abstract`: title and abstract search
- `cf.contributions_orcid`: ORCID-based contributor search
- `cf.cites`: citation relationships
- `cf.subject`: subject classification
- `cf.publication_year`: publication year
- `cf.language`: language filter
- `cf.access_rights`: access rights filter
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/fern/products/client.py">get_by_id6</a>(...) -> SkgIfJsonLdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get product by local identifier.
</dd>
</dl>
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

client.products.get_by_id6(
    local_identifier="localIdentifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**local_identifier:** `str` — The local identifier of the product
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Publications
<details><summary><code>client.publications.<a href="src/fern/publications/client.py">search7</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search and filter publications using the legacy XML API format.
</dd>
</dl>
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

client.publications.search7()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**format:** `typing.Optional[Search7RequestFormat]` — Response format
    
</dd>
</dl>

<dl>
<dd>

**keywords:** `typing.Optional[str]` — Keyword-based search in title, description, authors, etc.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Search in publication title
    
</dd>
</dl>

<dl>
<dd>

**author:** `typing.Optional[str]` — Search by author name/surname
    
</dd>
</dl>

<dl>
<dd>

**doi:** `typing.Optional[str]` — Filter by DOI(s)
    
</dd>
</dl>

<dl>
<dd>

**orcid:** `typing.Optional[str]` — Filter by author ORCID(s)
    
</dd>
</dl>

<dl>
<dd>

**from_date_accepted:** `typing.Optional[str]` — Filter from date of acceptance (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**to_date_accepted:** `typing.Optional[str]` — Filter to date of acceptance (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**openaire_provider_id:** `typing.Optional[str]` — Filter by OpenAIRE provider ID(s)
    
</dd>
</dl>

<dl>
<dd>

**openaire_project_id:** `typing.Optional[str]` — Filter by OpenAIRE project ID(s)
    
</dd>
</dl>

<dl>
<dd>

**has_project:** `typing.Optional[str]` — Filter research products that have a link to a project
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Filter by project grant number
    
</dd>
</dl>

<dl>
<dd>

**funder:** `typing.Optional[str]` — Filter by funder shortname(s)
    
</dd>
</dl>

<dl>
<dd>

**funding_stream:** `typing.Optional[str]` — Filter by funding stream
    
</dd>
</dl>

<dl>
<dd>

**has_ec_funding:** `typing.Optional[str]` — Filter projects with EC funding
    
</dd>
</dl>

<dl>
<dd>

**has_wt_funding:** `typing.Optional[str]` — Filter projects with Wellcome Trust funding
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Filter by country code
    
</dd>
</dl>

<dl>
<dd>

**influence:** `typing.Optional[str]` — Filter by influence class (C1-C5)
    
</dd>
</dl>

<dl>
<dd>

**popularity:** `typing.Optional[str]` — Filter by popularity class (C1-C5)
    
</dd>
</dl>

<dl>
<dd>

**impulse:** `typing.Optional[str]` — Filter by impulse class (C1-C5)
    
</dd>
</dl>

<dl>
<dd>

**citation_count:** `typing.Optional[str]` — Filter by citation count class (C1-C5)
    
</dd>
</dl>

<dl>
<dd>

**instancetype:** `typing.Optional[str]` — Filter by publication instance type
    
</dd>
</dl>

<dl>
<dd>

**original_id:** `typing.Optional[str]` — Filter by original identifier(s)
    
</dd>
</dl>

<dl>
<dd>

**sdg:** `typing.Optional[str]` — Filter by Sustainable Development Goal number (1-17)
    
</dd>
</dl>

<dl>
<dd>

**fos:** `typing.Optional[str]` — Filter by Field of Science classification value
    
</dd>
</dl>

<dl>
<dd>

**openaire_publication_id:** `typing.Optional[str]` — Filter by OpenAIRE publication ID(s)
    
</dd>
</dl>

<dl>
<dd>

**peer_reviewed:** `typing.Optional[str]` — Filter by peer review status
    
</dd>
</dl>

<dl>
<dd>

**diamond_journal:** `typing.Optional[str]` — Filter by diamond journal status
    
</dd>
</dl>

<dl>
<dd>

**publicly_funded:** `typing.Optional[str]` — Filter by publicly funded status
    
</dd>
</dl>

<dl>
<dd>

**green:** `typing.Optional[str]` — Filter by green open access status
    
</dd>
</dl>

<dl>
<dd>

**open_access_color:** `typing.Optional[str]` — Filter by open access color (gold, bronze, hybrid)
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` 

sortBy=field,[ascending|descending] <br>
'field' is one of: projectstartdate, projectstartyear, projectenddate, projectendyear, projectduration
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — Page number
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[str]` — Number of results per page (max 100)
    
</dd>
</dl>

<dl>
<dd>

**cursor_mark:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

