# Reference
## App Definitions
<details><summary><code>client.app_definitions.<a href="src/fern/app_definitions/client.py#L26-L59">regenerate_benchling_app_definition_client_secret</a>(...) -> AppClientSecret</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Regenerate the oauth2 client key for the given app definition. Note that this will invalidate the previous key, and the value returned by this call can't be retrieved from Benchling.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.app_definitions.regenerate_benchling_app_definition_client_secret(
    app_def_id="appdef_e59sjL23Pqn30xHg",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_def_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Apps
<details><summary><code>client.apps.<a href="src/fern/apps/client.py#L25-L56">get_benchling_app_manifest</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get app manifest
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.apps.get_benchling_app_manifest(
    app_id="app_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apps.<a href="src/fern/apps/client.py#L58-L89">put_benchling_app_manifest</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update from an app manifest
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.apps.put_benchling_app_manifest(
    app_id="app_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Assemblies
<details><summary><code>client.assemblies.<a href="src/fern/assemblies/client.py#L36-L68">get_assembly</a>(...) -> Assembly</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a bulk assembly by its API identifier.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.assemblies.get_assembly(
    bulk_assembly_id="bulk_assembly_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bulk_assembly_id:** `str` — API identifier of bulk assembly
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assemblies.<a href="src/fern/assemblies/client.py#L70-L188">create_and_finalize_assembly</a>(...) -> AsyncTaskLink</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create and finalize a new bulk assembly in a single step.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AssemblySpecSharedAssemblyParameters_Concatenation, AssemblyConcatenationMethodParameters, AssemblySpecSharedBinsItem_Constant, AssemblySpecSharedConstructsItem, AssemblySpecSharedFragmentsItem, AssemblyPolymerReference_AaSequence, AssemblySpecFinalizedOutputLocation
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assemblies.create_and_finalize_assembly(
    assembly_parameters=AssemblySpecSharedAssemblyParameters_Concatenation(
        parameters=AssemblyConcatenationMethodParameters(
            fragment_production_method="SLICE",
            polymer_type="DNA",
        ),
    ),
    bins=[
        AssemblySpecSharedBinsItem_Constant(
            id="id",
            name="name",
            residues="residues",
        )
    ],
    constructs=[
        AssemblySpecSharedConstructsItem(
            fragments=[
                "fragments"
            ],
            id="id",
        )
    ],
    fragments=[
        AssemblySpecSharedFragmentsItem(
            end=1.1,
            id="id",
            orientation="FORWARD",
            polymer=AssemblyPolymerReference_AaSequence(
                protein_id="proteinId",
            ),
            start=1.1,
            bin_id="bin1",
        )
    ],
    topology="CIRCULAR",
    folder_id="folderId",
    name="name",
    output_location=AssemblySpecFinalizedOutputLocation(
        construct_folder_id="constructFolderId",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assembly_parameters:** `AssemblySpecSharedAssemblyParameters` — Assembly-wide parameters to describe requirements and procedures for the assembly.
    
</dd>
</dl>

<dl>
<dd>

**bins:** `typing.List[AssemblySpecSharedBinsItem]` — Bins are used to group fragments according to their position in the output construct or add a spacer (i.e. constant) region.
    
</dd>
</dl>

<dl>
<dd>

**constructs:** `typing.List[AssemblySpecSharedConstructsItem]` — Output constructs that should be created.
    
</dd>
</dl>

<dl>
<dd>

**fragments:** `typing.List[AssemblySpecSharedFragmentsItem]` — Fragments to be used in the assembly.
    
</dd>
</dl>

<dl>
<dd>

**topology:** `AssemblySpecSharedTopology` — Whether the created constructs should be circular or linear.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `str` — API identifier of the folder in which the assembly should be created.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the bulk assembly.
    
</dd>
</dl>

<dl>
<dd>

**output_location:** `AssemblySpecFinalizedOutputLocation` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assemblies.<a href="src/fern/assemblies/client.py#L190-L288">validate_assembly</a>(...) -> AsyncTaskLink</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validate an assembly prior to finalization to see if it will succeed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AssemblySpecSharedAssemblyParameters_Concatenation, AssemblyConcatenationMethodParameters, AssemblySpecSharedBinsItem_Constant, AssemblySpecSharedConstructsItem, AssemblySpecSharedFragmentsItem, AssemblyPolymerReference_AaSequence
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assemblies.validate_assembly(
    assembly_parameters=AssemblySpecSharedAssemblyParameters_Concatenation(
        parameters=AssemblyConcatenationMethodParameters(
            fragment_production_method="SLICE",
            polymer_type="DNA",
        ),
    ),
    bins=[
        AssemblySpecSharedBinsItem_Constant(
            id="id",
            name="name",
            residues="residues",
        )
    ],
    constructs=[
        AssemblySpecSharedConstructsItem(
            fragments=[
                "fragments"
            ],
            id="id",
        )
    ],
    fragments=[
        AssemblySpecSharedFragmentsItem(
            end=1.1,
            id="id",
            orientation="FORWARD",
            polymer=AssemblyPolymerReference_AaSequence(
                protein_id="proteinId",
            ),
            start=1.1,
            bin_id="bin1",
        )
    ],
    topology="CIRCULAR",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `AssemblySpecShared` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Lab Automation
<details><summary><code>client.lab_automation.<a href="src/fern/lab_automation/client.py#L27-L128">list_connect_files</a>(...) -> ConnectionFilesPaginatedList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Benchling Connect files
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.lab_automation.list_connect_files()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return. Defaults to 50, maximum of 100.
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Token for pagination
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created before the specified time. e.g. < 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created after the specified time. e.g. > 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created on or before the specified time. e.g. <= 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created on or after the specified time. e.g. >= 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_lt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified before the specified time. e.g. < 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_gt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified after the specified time. e.g. > 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_lte:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or before the specified time. e.g. <= 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_gte:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or after the specified time. e.g. >= 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**filename_includes:** `typing.Optional[str]` — Name substring of a file. Restricts results to those with names that include the provided substring.
    
</dd>
</dl>

<dl>
<dd>

**connection_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of connection IDs. Restricts results to those created by the given connections.
    
</dd>
</dl>

<dl>
<dd>

**connection_schema_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of connection schema IDs. Restricts results to those created by connections with the given connection schemas.
    
</dd>
</dl>

<dl>
<dd>

**data_type:** `typing.Optional[ListConnectFilesRequestDataType]` — File data type. Restricts results to those with the specified data type.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Collaborations
<details><summary><code>client.collaborations.<a href="src/fern/collaborations/client.py#L30-L153">list_collaborations</a>(...) -> CollaborationsPaginatedList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all collaborations. Collaboration endpoints are moving to beta. Visit the [beta v2 docs](https://benchling.com/api/v2-beta/reference?showLA=true#/Collaborations).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collaborations.list_collaborations(
    item_ids="src_1234",
    user_id="ent_1234",
    app_id="app_1234",
    team_id="team_1234",
    organization_id="ent_1234",
    ids="clb_123abc",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_ids:** `typing.Optional[str]` — Comma-separated list of ids of items for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**item_type:** `typing.Optional[ListCollaborationsRequestItemType]` — Type of item for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — ID of user for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[str]` — ID of app for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `typing.Optional[str]` — ID of team for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — ID of organization for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[ListCollaborationsRequestRole]` — Organization or team membership role for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[str]` — Comma-separated list of collaboration ids. Matches all of the provided IDs, or returns a 400 error that includes a list of which IDs are invalid.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created before the specified time. e.g. < 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created after the specified time. e.g. > 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_lt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified before the specified time. e.g. < 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_gt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified after the specified time. e.g. > 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_lte:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or before the specified time. e.g. <= 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_gte:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or after the specified time. e.g. >= 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of collaborations to return. Defaults to 50, maximum of 100.
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Token for pagination
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListCollaborationsRequestSort]` — Method by which to order search results. Valid sort method is modifiedAt (modified time, most recent first). Optionally add :asc or :desc to specify ascending or descending order. Default is modifiedAt:desc.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.collaborations.<a href="src/fern/collaborations/client.py#L155-L187">get_collaboration</a>(...) -> Collaboration</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a collaboration by ID. Collaboration endpoints are moving to beta. Visit the [beta v2 docs](https://benchling.com/api/v2-beta/reference?showLA=true#/Collaborations).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.collaborations.get_collaboration(
    collaboration_id="clb_1234",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collaboration_id:** `str` — ID of collaboration to get
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DNA Oligos
<details><summary><code>client.dna_oligos.<a href="src/fern/dna_oligos/client.py#L37-L169">list_dna_oligos_helm</a>(...) -> DnaOligosPaginatedListHelm</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List DNA Oligos with HELM Deprecated as HELM support is now in stable.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.dna_oligos.list_dna_oligos_helm(
    modified_at="> 2022-03-01 AND < 2022-04-01",
    ids="seq_yWs5X7lv,seq_RhYGVnHF",
    entity_registry_ids_any_of="TP001,TP002",
    names_any_of="MyName1, MyName2",
    names_any_of_case_sensitive="MyName1,MyName2",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return. Defaults to 50, maximum of 100.
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Token for pagination
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListDnaOligosHelmRequestSort]` — Method by which to order search results. Valid sorts are modifiedAt (modified time, most recent first) and name (entity name, alphabetical). Optionally add :asc or :desc to specify ascending or descending order.
    
</dd>
</dl>

<dl>
<dd>

**modified_at:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Supports the > and < operators. Time zone defaults to UTC. Restricts results to those modified in the specified range. e.g. > 2017-04-30. Date ranges can be specified with the following nomenclature > YYYY-MM-DD AND <YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of a DNA Oligo. Restricts results to those with the specified name, alias, or entity registry ID.
    
</dd>
</dl>

<dl>
<dd>

**name_includes:** `typing.Optional[str]` — Name substring of a DNA Oligo. Restricts results to those with names, aliases, or entity registry IDs that include the provided substring.
    
</dd>
</dl>

<dl>
<dd>

**bases:** `typing.Optional[str]` — Full bases of the DNA Oligo. Restricts results to those with the specified bases, case-insensitive, allowing for circular or reverse complement matches. Does not allow partial matching or loose matching via degenerate bases.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` — ID of a folder. Restricts results to those in the folder.
    
</dd>
</dl>

<dl>
<dd>

**mentioned_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of entry IDs. Restricts results to DNA Oligos mentioned in those entries.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — ID of a project. Restricts results to those in the project.
    
</dd>
</dl>

<dl>
<dd>

**registry_id:** `typing.Optional[str]` — ID of a registry. Restricts results to those registered in this registry. Specifying "null" returns unregistered items.
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `typing.Optional[str]` — ID of a schema. Restricts results to those of the specified schema.
    
</dd>
</dl>

<dl>
<dd>

**schema_fields:** `typing.Optional[SchemaFieldsQueryParam]` — Schema field value. For Integer, Float, and Date type fields, supports the >= and <= operators. If present, the schemaId param must also be present. Restricts results to those with a field of whose value matches the filter.
    
</dd>
</dl>

<dl>
<dd>

**archive_reason:** `typing.Optional[str]` — Archive reason. Restricts results to those with the specified archive reason. Use “NOT_ARCHIVED” to filter for unarchived DNA Oligos.
    
</dd>
</dl>

<dl>
<dd>

**mentions:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of item IDs. Restricts results to those that mention the given items in the description.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[str]` — Comma-separated list of ids. Matches all of the provided IDs, or returns a 400 error that includes a list of which IDs are invalid.
    
</dd>
</dl>

<dl>
<dd>

**entity_registry_ids_any_of:** `typing.Optional[str]` — Comma-separated list of entity registry IDs. Restricts results to those that match any of the specified registry IDs.
    
</dd>
</dl>

<dl>
<dd>

**names_any_of:** `typing.Optional[str]` — Comma-separated list of names. Restricts results to those that match any of the specified names, aliases, or entity registry IDs, case insensitive.  Warning - this filter can be non-performant due to case insensitivity.
    
</dd>
</dl>

<dl>
<dd>

**names_any_of_case_sensitive:** `typing.Optional[str]` — Comma-separated list of names. Restricts results to those that match any of the specified names, aliases, or entity registry IDs, case sensitive.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dna_oligos.<a href="src/fern/dna_oligos/client.py#L171-L266">create_dna_oligo_with_helm</a>(...) -> DnaOligoHelm</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a DNA Oligo with optional HELM Deprecated as HELM support is now in stable.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.dna_oligos.create_dna_oligo_with_helm(
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

**request:** `OligoCreateHelm` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dna_oligos.<a href="src/fern/dna_oligos/client.py#L268-L299">get_dna_oligo_helm</a>(...) -> DnaOligoHelm</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a DNA Oligo with HELM Deprecated as HELM support is now in stable.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.dna_oligos.get_dna_oligo_helm(
    oligo_id="oligo_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**oligo_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dna_oligos.<a href="src/fern/dna_oligos/client.py#L301-L383">update_dna_oligo_helm</a>(...) -> DnaOligoHelm</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a DNA Oligo with optional HELM Deprecated as HELM support is now in stable.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.dna_oligos.update_dna_oligo_helm(
    oligo_id="oligo_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**oligo_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**aliases:** `typing.Optional[typing.List[str]]` — Aliases to add to the Oligo
    
</dd>
</dl>

<dl>
<dd>

**author_ids:** `typing.Optional[typing.List[str]]` — IDs of users to set as the Oligo's authors.
    
</dd>
</dl>

<dl>
<dd>

**bases:** `typing.Optional[str]` — Base pairs of the oligo.
    
</dd>
</dl>

<dl>
<dd>

**custom_fields:** `typing.Optional[CustomFields]` — Custom fields to add to the Oligo. Every field should have its name as a key, mapping to an object with information about the value of the field.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[Fields]` — Fields to set on the Oligo. Must correspond with the schema's field definitions. Every field should have its name as a key, mapping to an object with information about the value of the field.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` — ID of the folder containing the Oligo.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the Oligo.
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `typing.Optional[str]` — ID of the oligo's schema.
    
</dd>
</dl>

<dl>
<dd>

**helm:** `typing.Optional[str]` — Representation of the oligo in HELM syntax, including any chemical modifications
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dna_oligos.<a href="src/fern/dna_oligos/client.py#L385-L417">bulk_create_dna_oligos_helm</a>(...) -> AsyncTaskLink</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk Create DNA Oligos with optional HELM Deprecated as HELM support is now in stable.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.dna_oligos.bulk_create_dna_oligos_helm()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dna_oligos:** `typing.Optional[typing.List[OligoCreateHelm]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Schemas
<details><summary><code>client.schemas.<a href="src/fern/schemas/client.py#L38-L89">list_entity_schemas</a>(...) -> EntitySchemasPaginatedList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List entity schemas
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.schemas.list_entity_schemas(
    modified_at="> 2022-03-01 AND < 2022-04-01",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**next_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**modified_at:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Supports the > and < operators. Time zone defaults to UTC. Restricts results to those modified in the specified range. e.g. > 2017-04-30. Date ranges can be specified with the following nomenclature > YYYY-MM-DD AND <YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**registry_id:** `typing.Optional[str]` — ID of a registry. Restricts results to schemas in this registry.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schemas.<a href="src/fern/schemas/client.py#L91-L199">create_entity_schema</a>(...) -> EntitySchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an entity schema
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.schemas.create_entity_schema(
    name="name",
    prefix="prefix",
    registry_id="registryId",
    type="custom_entity",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**registry_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `EntitySchemaCreateType` 
    
</dd>
</dl>

<dl>
<dd>

**auth_parent_option:** `typing.Optional[EntitySchemaCreateAuthParentOption]` 
    
</dd>
</dl>

<dl>
<dd>

**constraint:** `typing.Optional[ConstraintCreate]` 
    
</dd>
</dl>

<dl>
<dd>

**containable_type:** `typing.Optional[EntitySchemaCreateContainableType]` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.List[FieldCreate]]` 
    
</dd>
</dl>

<dl>
<dd>

**include_registry_id_in_chips:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_containable:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**labeling_strategies:** `typing.Optional[typing.List[NamingStrategy]]` 
    
</dd>
</dl>

<dl>
<dd>

**mixture_schema_config:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**result_schema_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sequence_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**should_create_as_oligo:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**should_order_name_parts_by_sequence:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**show_residues:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**use_organization_collection_alias_for_display_label:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schemas.<a href="src/fern/schemas/client.py#L201-L233">get_entity_schema</a>(...) -> EntitySchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an entity schema by ID
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.schemas.get_entity_schema(
    schema_id="schema_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_id:** `str` — ID of schema to get
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schemas.<a href="src/fern/schemas/client.py#L235-L287">list_schema_classes</a>(...) -> SchemaClassesPaginatedList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List schema classes
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.schemas.list_schema_classes(
    modified_at="> 2022-03-01 AND < 2022-04-01",
    schema_ids_all_of="bfi_ed1ef7,con_1c76c9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**next_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**modified_at:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Supports the > and < operators. Time zone defaults to UTC. Restricts results to those modified in the specified range. e.g. > 2017-04-30. Date ranges can be specified with the following nomenclature > YYYY-MM-DD AND <YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**schema_ids_all_of:** `typing.Optional[str]` — Comma separated list of bioentity IDs. Returns schema classes where the schema class is implemented by all of the provided items.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schemas.<a href="src/fern/schemas/client.py#L289-L321">get_schema_class</a>(...) -> SchemaClass</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a schema class by ID
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.schemas.get_schema_class(
    schema_class_id="schema_class_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_class_id:** `str` — ID of schema class to get
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entries
<details><summary><code>client.entries.<a href="src/fern/entries/client.py#L40-L184">list_entries</a>(...) -> EntriesPaginatedList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List notebook entries
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.entries.list_entries(
    modified_at="> 2022-03-01 AND < 2022-04-01",
    archive_reason="NOT_ARCHIVED",
    names_any_of="MyName1,MyName2",
    names_any_of_case_sensitive="MyName1,MyName2",
    assigned_reviewer_ids_any_of="ent_a0SApq3z,ent_SdUvia1v",
    creator_ids="ent_a0SApq3z",
    author_ids_any_of="ent_a0SApq3z,ent_b4AApz9b",
    display_ids="VPR001,VPR002",
    returning="entries.id, entries.name, entries.modifiedAt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return. Defaults to 50, maximum of 100.
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Token for pagination
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListEntriesRequestSort]` — Method by which to order search results. Valid sorts are modifiedAt (modified time, most recent first) and name (entity name, alphabetical). Optionally add :asc or :desc to specify ascending or descending order.
    
</dd>
</dl>

<dl>
<dd>

**modified_at:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Supports the > and < operators. Time zone defaults to UTC. Restricts results to those modified in the specified range. e.g. > 2017-04-30. Date ranges can be specified with the following nomenclature > YYYY-MM-DD AND <YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of an Entry. Restricts results to those with the specified name.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — ID of a project. Restricts results to those in the project.
    
</dd>
</dl>

<dl>
<dd>

**archive_reason:** `typing.Optional[str]` — Archive reason. Restricts items to those with the specified archive reason. Use "NOT_ARCHIVED" to filter for unarchived entries. Use "ANY_ARCHIVED" to filter for archived entries regardless of reason. Use "ANY_ARCHIVED_OR_NOT_ARCHIVED" to return items for both archived and unarchived.
    
</dd>
</dl>

<dl>
<dd>

**review_status:** `typing.Optional[ListEntriesRequestReviewStatus]` — Restrict results to those with the given review status. Supported statuses: IN_PROGRESS, ACCEPTED, REJECTED, NEEDS_REVIEW, RETRACTED
    
</dd>
</dl>

<dl>
<dd>

**mentioned_in:** `typing.Optional[str]` — Comma-separated list of entry IDs. Restricts results to those mentioned within the entries in this list.
    
</dd>
</dl>

<dl>
<dd>

**mentions:** `typing.Optional[str]` — Comma-separated list of resource IDs. Restricts results to entries that mention the given items.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[str]` — Comma-separated list of ids. Matches all of the provided IDs, or returns a 400 error that includes a list of which IDs are invalid.
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `typing.Optional[str]` — ID of a schema. Restricts results to those of the specified schema.
    
</dd>
</dl>

<dl>
<dd>

**names_any_of:** `typing.Optional[str]` — Comma-separated list of names. Restricts results to those that match any of the specified names, case insensitive.  Warning - this filter can be non-performant due to case insensitivity.
    
</dd>
</dl>

<dl>
<dd>

**names_any_of_case_sensitive:** `typing.Optional[str]` — Comma-separated list of names. Restricts results to those that match any of the specified names, case sensitive.
    
</dd>
</dl>

<dl>
<dd>

**assigned_reviewer_ids_any_of:** `typing.Optional[str]` — Comma-separated list of ids. Restricts results to entries that have assignees of any of the specified ids.
    
</dd>
</dl>

<dl>
<dd>

**creator_ids:** `typing.Optional[str]` — Comma separated list of users IDs
    
</dd>
</dl>

<dl>
<dd>

**author_ids_any_of:** `typing.Optional[str]` — Comma separated list of user or app IDs
    
</dd>
</dl>

<dl>
<dd>

**display_ids:** `typing.Optional[str]` — Comma-separated list of Entry Display IDs.
    
</dd>
</dl>

<dl>
<dd>

**returning:** `typing.Optional[str]` 

Comma-separated list of fields to return. Modifies the output shape. To return all keys at a given level, enumerate them or use the wildcard, '*'. For more information, [click here](https://docs.benchling.com/docs/getting-started-1#returning-query-parameter).

**Note:** "entries.days.notes" cannot be introspected with the returning parameter, and any sub fields will be ignored. E.g., "entries.days.notes.text" will return the same model as "entries.days.notes".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entries.<a href="src/fern/entries/client.py#L186-L278">create_entry_with_attachments</a>(...) -> AsyncTaskLink</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a notebook entry with optional attachments. Attachments will be placed into the entry body in the order they are specified.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.entries.create_entry_with_attachments(
    folder_id="folderId",
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

**request:** `EntryCreateAttachments` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entries.<a href="src/fern/entries/client.py#L280-L328">get_entry</a>(...) -> EntryById</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a notebook entry by ID
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.entries.get_entry(
    entry_id="entry_id",
    returning="id, name, modifiedAt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entry_id:** `str` — ID of the entry
    
</dd>
</dl>

<dl>
<dd>

**returning:** `typing.Optional[str]` 

Comma-separated list of fields to return. Modifies the output shape. To return all keys at a given level, enumerate them or use the wildcard, '*'. For more information, [click here](https://docs.benchling.com/docs/getting-started-1#returning-query-parameter).

**Note:** "days.notes" cannot be introspected with the returning parameter, and any sub fields will be ignored. E.g., "days.notes.text" will return the same model as "days.notes".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entries.<a href="src/fern/entries/client.py#L330-L362">bulk_create_entries</a>(...) -> AsyncTaskLink</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk create notebook entries with optional attachments. Limit of 100 Entries per request. Attachments will be placed into the entry body in the order they are specified.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.entries.bulk_create_entries()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entry_datas:** `typing.Optional[typing.List[EntryCreateAttachments]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entries.<a href="src/fern/entries/client.py#L364-L396">get_template_entry</a>(...) -> EntryTemplate</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a notebook template entry by ID
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.entries.get_template_entry(
    entry_template_id="entry_template_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entry_template_id:** `str` — ID of the entry template
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Folders
<details><summary><code>client.folders.<a href="src/fern/folders/client.py#L28-L146">list_folder_collaborations</a>(...) -> CollaborationsPaginatedList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about collaborations on the specified Folders. Collaboration endpoints are moving to beta. Visit the [beta v2 docs](https://benchling.com/api/v2-beta/reference?showLA=true#/Folders).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.folders.list_folder_collaborations(
    folder_id="lib_1234",
    user_id="ent_1234",
    app_id="app_1234",
    team_id="team_1234",
    organization_id="ent_1234",
    ids="clb_1234",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `str` — ID of folder for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — ID of user for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[str]` — ID of app for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `typing.Optional[str]` — ID of team for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — ID of organization for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[ListFolderCollaborationsRequestRole]` — Organization or team membership role for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[str]` — Comma-separated list of collaboration ids. Matches all of the provided IDs, or returns a 400 error that includes a list of which IDs are invalid.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created before the specified time. e.g. < 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created after the specified time. e.g. > 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_lt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified before the specified time. e.g. < 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_gt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified after the specified time. e.g. > 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_lte:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or before the specified time. e.g. <= 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_gte:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or after the specified time. e.g. >= 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of collaborations to return. Defaults to 50, maximum of 100.
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Token for pagination
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListFolderCollaborationsRequestSort]` — Method by which to order search results. Valid sort method is modifiedAt (modified time, most recent first). Optionally add :asc or :desc to specify ascending or descending order. Default is modifiedAt:desc.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Forms
<details><summary><code>client.forms.<a href="src/fern/forms/client.py#L28-L86">get_form_definitions</a>(...) -> FormDefinitionsPaginatedList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists available form definitions. Only the latest version along is returned for each definition.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.forms.get_form_definitions(
    modified_at="> 2022-03-01 AND < 2022-04-01",
    returning="formDefinitions.id,formDefinitions.modifiedAt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Token for pagination
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**modified_at:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Supports the > and < operators. Time zone defaults to UTC. Restricts results to those modified in the specified range. e.g. > 2017-04-30. Date ranges can be specified with the following nomenclature > YYYY-MM-DD AND <YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetFormDefinitionsRequestSort]` — Sets the sort-order of the response. Valid sorts are modifiedAt (modified time, most recent first). Optionally add :asc or :desc to specify ascending or descending order.
    
</dd>
</dl>

<dl>
<dd>

**returning:** `typing.Optional[str]` — Comma-separated list of fields to return. Modifies the output shape. To return all keys at a given level, enumerate them or use the wildcard, '*'. For more information, [click here](https://docs.benchling.com/docs/getting-started-1#returning-query-parameter).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.forms.<a href="src/fern/forms/client.py#L88-L130">get_form_definition</a>(...) -> FormDefinition</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific form definition. Only the latest version is returned
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.forms.get_form_definition(
    form_definition_id="fmdef_W7KgYydE",
    returning="id,modifiedAt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**form_definition_id:** `str` — API ID of the specific form definition desired
    
</dd>
</dl>

<dl>
<dd>

**returning:** `typing.Optional[str]` — Comma-separated list of fields to return. Modifies the output shape. To return all keys at a given level, enumerate them or use the wildcard, '*'. For more information, [click here](https://docs.benchling.com/docs/getting-started-1#returning-query-parameter).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Access Policies
<details><summary><code>client.access_policies.<a href="src/fern/access_policies/client.py#L27-L64">list_general_access_policies</a>(...) -> AccessPoliciesPaginatedList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of general (project/registry) access policies.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.access_policies.list_general_access_policies()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**next_token:** `typing.Optional[str]` 
    
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

<details><summary><code>client.access_policies.<a href="src/fern/access_policies/client.py#L66-L98">get_general_access_policy</a>(...) -> AccessPolicy</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a general (project/registry) policy by ID.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.access_policies.get_general_access_policy(
    policy_id="policy_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**policy_id:** `str` — ID of policy to get
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.access_policies.<a href="src/fern/access_policies/client.py#L100-L137">list_schema_access_policies</a>(...) -> AccessPoliciesPaginatedList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of schema access policies.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.access_policies.list_schema_access_policies()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**next_token:** `typing.Optional[str]` 
    
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

<details><summary><code>client.access_policies.<a href="src/fern/access_policies/client.py#L139-L171">get_schema_access_policy</a>(...) -> AccessPolicy</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a schema access policy by ID.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.access_policies.get_schema_access_policy(
    policy_id="policy_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**policy_id:** `str` — ID of policy to get
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.projects.<a href="src/fern/projects/client.py#L28-L146">list_project_collaborations</a>(...) -> CollaborationsPaginatedList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about collaborations on the specified project. Collaboration endpoints are moving to beta. Visit the [beta v2 docs](https://benchling.com/api/v2-beta/reference?showLA=true#/Projects).
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.projects.list_project_collaborations(
    project_id="src_1234",
    user_id="ent_1234",
    app_id="app_1234",
    team_id="team_1234",
    organization_id="ent_1234",
    ids="clb_1234",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` — ID of project for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — ID of user for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[str]` — ID of app for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `typing.Optional[str]` — ID of team for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — ID of organization for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[ListProjectCollaborationsRequestRole]` — Organization or team membership role for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[str]` — Comma-separated list of collaboration ids. Matches all of the provided IDs, or returns a 400 error that includes a list of which IDs are invalid.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created before the specified time. e.g. < 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created after the specified time. e.g. > 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_lt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified before the specified time. e.g. < 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_gt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified after the specified time. e.g. > 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_lte:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or before the specified time. e.g. <= 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_gte:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or after the specified time. e.g. >= 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of collaborations to return. Defaults to 50, maximum of 100.
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Token for pagination
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListProjectCollaborationsRequestSort]` — Method by which to order search results. Valid sort method is modifiedAt (modified time, most recent first). Optionally add :asc or :desc to specify ascending or descending order. Default is modifiedAt:desc.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Legacy Workflows
<details><summary><code>client.legacy_workflows.<a href="src/fern/legacy_workflows/client.py#L27-L59">get_stage_entry</a>(...) -> StageEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a stage entry by ID
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.legacy_workflows.get_stage_entry(
    stage_entry_id="stage_entry_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stage_entry_id:** `str` — ID of the stage entry
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.legacy_workflows.<a href="src/fern/legacy_workflows/client.py#L61-L99">get_external_file_metadata</a>(...) -> EntryExternalFileById</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the metadata for an external file. Use the 'downloadURL' to download the actual file. (Expand the schema view for details)
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.legacy_workflows.get_external_file_metadata(
    stage_entry_id="stage_entry_id",
    external_file_id="external_file_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stage_entry_id:** `str` — ID of the legacy workflow stage entry the file was uploaded to
    
</dd>
</dl>

<dl>
<dd>

**external_file_id:** `str` — ID of the external file
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Studies
<details><summary><code>client.studies.<a href="src/fern/studies/client.py#L43-L185">list_studies</a>(...) -> StudiesPaginatedList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Studies
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.studies.list_studies(
    archive_reason="ANY_ARCHIVED",
    ids="stdy_yWs5X7lv,stdy_RhYGVnHF",
    names_any_of="MyName1,MyName2",
    names_any_of_case_sensitive="MyName1,MyName2",
    author_ids_any_of="ent_a0SApq3z,ent_b4AApz9b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return. Defaults to 50, maximum of 100.
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Token for pagination
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListStudiesRequestSort]` — Method by which to order search results. Valid sorts are modifiedAt (modified time, most recent first) and name (entity name, alphabetical). Optionally add :asc or :desc to specify ascending or descending order.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created before the specified time. e.g. < 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created after the specified time. e.g. > 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created on or before the specified time. e.g. <= 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created on or after the specified time. e.g. >= 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_lt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified before the specified time. e.g. < 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_gt:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified after the specified time. e.g. > 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_lte:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or before the specified time. e.g. <= 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**modified_at_gte:** `typing.Optional[str]` — Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or after the specified time. e.g. >= 2017-04-30.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of a Study. Restricts results to those with the specified name, alias, or entity registry ID.
    
</dd>
</dl>

<dl>
<dd>

**name_includes:** `typing.Optional[str]` — Name substring of a Study. Restricts results to those with names that include the provided substring.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` — ID of a folder. Restricts results to those in the folder.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — ID of a project. Restricts results to those in the project.
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `typing.Optional[str]` — ID of a schema. Restricts results to those of the specified schema.
    
</dd>
</dl>

<dl>
<dd>

**archive_reason:** `typing.Optional[str]` — Archive reason. Restricts results to those with the specified archive reason. Use “NOT_ARCHIVED” to filter for unarchived Studies. Use "ANY_ARCHIVED" to filter for archived Molecules regardless of reason. Use "ANY_ARCHIVED_OR_NOT_ARCHIVED" to return items for both archived and unarchived.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[str]` — Comma-separated list of ids. Matches all of the provided IDs, or returns a 400 error that includes a list of which IDs are invalid.
    
</dd>
</dl>

<dl>
<dd>

**names_any_of:** `typing.Optional[str]` — Comma-separated list of names. Maximum of 100. Restricts results to those that match any of the specified names.
    
</dd>
</dl>

<dl>
<dd>

**names_any_of_case_sensitive:** `typing.Optional[str]` — Comma-separated list of app names. Maximum of 100. Restricts results to those that match any of the specified names, case sensitive.
    
</dd>
</dl>

<dl>
<dd>

**author_ids_any_of:** `typing.Optional[str]` — Comma separated list of user or app IDs. Maximum of 100.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.studies.<a href="src/fern/studies/client.py#L187-L255">create_study</a>(...) -> Study</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a Study.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, EntryCreate, Field
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.studies.create_study(
    entry_information=EntryCreate(
        folder_id="folderId",
        name="name",
    ),
    fields={
        "key": Field(
            value=None,
        )
    },
    folder_id="folderId",
    name="name",
    study_schema_id="studySchemaId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `StudyCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.studies.<a href="src/fern/studies/client.py#L257-L286">get_study</a>(...) -> Study</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a Study
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.studies.get_study(
    study_id="study_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**study_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.studies.<a href="src/fern/studies/client.py#L288-L362">update_study</a>(...) -> Study</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a Study
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.studies.update_study(
    study_id="stdy_OnnsW08k",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**study_id:** `str` — The ID of the study
    
</dd>
</dl>

<dl>
<dd>

**request:** `StudyUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.studies.<a href="src/fern/studies/client.py#L364-L393">get_study_items</a>(...) -> StudyItems</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get items for a Study
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.studies.get_study_items(
    study_id="study_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**study_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.studies.<a href="src/fern/studies/client.py#L395-L432">add_study_items</a>(...) -> StudyItemsCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add one or more items to a Study
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.studies.add_study_items(
    study_id="study_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**study_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**item_ids:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.studies.<a href="src/fern/studies/client.py#L434-L471">remove_study_items</a>(...) -> EmptyObject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove one or more items from a Study
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.studies.remove_study_items(
    study_id="study_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**study_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**item_ids:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.studies.<a href="src/fern/studies/client.py#L473-L514">archive_studies</a>(...) -> StudiesArchivalChange</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Archive Studies
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.studies.archive_studies(
    reason="Made in error",
    study_ids=[
        "studyIds"
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

**reason:** `StudiesArchiveReason` — The reason for archiving the provided Studies. Accepted reasons may differ based on tenant configuration.
    
</dd>
</dl>

<dl>
<dd>

**study_ids:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.studies.<a href="src/fern/studies/client.py#L516-L548">bulk_create_studies</a>(...) -> StudiesBulkCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create one or more Studies
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.studies.bulk_create_studies()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**studies:** `typing.Optional[typing.List[StudyCreate]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.studies.<a href="src/fern/studies/client.py#L550-L582">bulk_update_studies</a>(...) -> StudiesBulkUpdateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk Update Studies
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.studies.bulk_update_studies()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**studies:** `typing.Optional[typing.List[StudyUpdate]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.studies.<a href="src/fern/studies/client.py#L584-L615">unarchive_studies</a>(...) -> StudiesArchivalChange</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unarchive Studies
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.studies.unarchive_studies(
    study_ids=[
        "studyIds"
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

**study_ids:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Authentication
<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py#L30-L97">generate_token</a>(...) -> TokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a token
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.authentication.generate_token(
    grant_type="client_credentials",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `TokenCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Units
<details><summary><code>client.units.<a href="src/fern/units/client.py#L27-L65">list_unit_types</a>(...) -> ListUnitTypesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all unit types in the tenant Unit Dictionary, including their constituent units.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.units.list_unit_types()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Token for pagination
    
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

<details><summary><code>client.units.<a href="src/fern/units/client.py#L67-L96">get_unit_type</a>(...) -> UnitType</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific unit type, including constituent units.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.units.get_unit_type(
    unit_type_id="qnty_7W2R1EFJ",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**unit_type_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Worklists
<details><summary><code>client.worklists.<a href="src/fern/worklists/client.py#L26-L70">list_worklist_collaborations</a>(...) -> CollaborationsPaginatedList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about collaborations on the specified Worklists.
</dd>
</dl>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.worklists.list_worklist_collaborations(
    worklist_id="worklist_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**worklist_id:** `str` — ID of worklist for which to retrieve collaborations.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Token for pagination
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

