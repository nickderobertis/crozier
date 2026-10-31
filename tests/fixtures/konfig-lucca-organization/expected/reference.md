# Reference
## Axis-sections
<details><summary><code>client.axis_sections.<a href="src/fern/axis_sections/client.py">get_api_v3axes</a>(...) -> GetApiV3AxesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all Axes satisfying query filters.
</dd>
</dl>
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

client.axis_sections.get_api_v3axes(
    paging="100,0",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**paging:** `str` — {offset},{limit}. Defaults to 0,1000.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — Filter on axes unique identifiers.
    
</dd>
</dl>

<dl>
<dd>

**is_active:** `typing.Optional[bool]` — Filter on axes active status.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.axis_sections.<a href="src/fern/axis_sections/client.py">get_api_v3axissections</a>(...) -> GetApiV3AxissectionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all AxisSections satisfying query filters.
</dd>
</dl>
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

client.axis_sections.get_api_v3axissections(
    paging="100,0",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**paging:** `str` — {offset},{limit}. Defaults to 0,1000.
    
</dd>
</dl>

<dl>
<dd>

**axis_id:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — Filter on the axis it belongs to.
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — Filter on the owner managing it.
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Filter on active status.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.axis_sections.<a href="src/fern/axis_sections/client.py">post_api_v3axis_sections</a>(...) -> PostApiV3AxisSectionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new AxisSection.
</dd>
</dl>
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

client.axis_sections.post_api_v3axis_sections(
    code="code",
    multilingual_name="multilingualName",
    axis_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `AxisSection` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.axis_sections.<a href="src/fern/axis_sections/client.py">get_api_v3axis_sections_axis_section_id</a>(...) -> GetApiV3AxisSectionsAxisSectionIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a single AxisSection by its unique identifier.
</dd>
</dl>
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

client.axis_sections.get_api_v3axis_sections_axis_section_id(
    axis_section_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**axis_section_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.axis_sections.<a href="src/fern/axis_sections/client.py">put_api_v3axis_sections_axis_section_id</a>(...) -> PutApiV3AxisSectionsAxisSectionIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partial or complete update to an existing AxisSection.
</dd>
</dl>
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

client.axis_sections.put_api_v3axis_sections_axis_section_id(
    axis_section_id=1,
    code="code",
    multilingual_name="multilingualName",
    axis_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**axis_section_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `AxisSection` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.axis_sections.<a href="src/fern/axis_sections/client.py">delete_api_v3axis_sections_axis_section_id</a>(...)</code></summary>
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
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.axis_sections.delete_api_v3axis_sections_axis_section_id(
    axis_section_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**axis_section_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Departments
<details><summary><code>client.departments.<a href="src/fern/departments/client.py">get_api_v3departments</a>(...) -> GetApiV3DepartmentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all Departments satisfying query filters.
</dd>
</dl>
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

client.departments.get_api_v3departments(
    paging="100,0",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**paging:** `str` — {offset},{limit}. Defaults to 0,1000.
    
</dd>
</dl>

<dl>
<dd>

**head_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.departments.<a href="src/fern/departments/client.py">get_api_v3departments_tree</a>() -> GetApiV3DepartmentsTreeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all departments as a tree.
Remark: first node is always empty and represents the starting point of the tree as multiple departments might be set to the highest level. 
</dd>
</dl>
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

client.departments.get_api_v3departments_tree()

```
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

<details><summary><code>client.departments.<a href="src/fern/departments/client.py">get_api_v3departments_department_id</a>(...) -> GetApiV3DepartmentsDepartmentIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a single Department by its unique identifier.
</dd>
</dl>
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

client.departments.get_api_v3departments_department_id(
    department_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**department_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

