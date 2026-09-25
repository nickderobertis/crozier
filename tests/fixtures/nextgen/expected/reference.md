# Reference
## Allergies and Intolerances
<details><summary><code>client.allergies_and_intolerances.<a href="src/fern/allergies_and_intolerances/client.py">base_url_persons_person_id_chart_allergies</a>(...) -> Ok</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of allergy summaries for the specified person id after applying additional OData query operations.
</dd>
</dl>
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

client.allergies_and_intolerances.base_url_persons_person_id_chart_allergies(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose allergies are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.allergies_and_intolerances.<a href="src/fern/allergies_and_intolerances/client.py">base_url_persons_person_id_chart_allergies_allergy_id</a>(...) -> Ok1</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the allergy details for the given person id and allergy id.
</dd>
</dl>
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

client.allergies_and_intolerances.base_url_persons_person_id_chart_allergies_allergy_id(
    person_id="personId",
    allergy_id="allergyId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose allergies are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**allergy_id:** `str` — (Required) (Required) The id of the allergy being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.allergies_and_intolerances.<a href="src/fern/allergies_and_intolerances/client.py">base_url_persons_person_id_chart_allergies_allergy_id_dur_check</a>(...) -> Ok1</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

StartFragmentGets a list of interactions for a given allergyId.
</dd>
</dl>
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

client.allergies_and_intolerances.base_url_persons_person_id_chart_allergies_allergy_id_dur_check(
    person_id="personId",
    allergy_id="allergyId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose allergies are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**allergy_id:** `str` — (Required) (Required) The id of the allergy being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.allergies_and_intolerances.<a href="src/fern/allergies_and_intolerances/client.py">base_url_persons_person_id_chart_deleted_allergies</a>(...) -> Ok</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of patient deleted allergies after applying additional OData operations.
</dd>
</dl>
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

client.allergies_and_intolerances.base_url_persons_person_id_chart_deleted_allergies(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose allergies are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.allergies_and_intolerances.<a href="src/fern/allergies_and_intolerances/client.py">base_url_persons_person_id_chart_encounters_encounter_id_allergies</a>(...) -> Ok4</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of allergy summaries for the given person id and encounter id, with the option of including resolved allergies.
</dd>
</dl>
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

client.allergies_and_intolerances.base_url_persons_person_id_chart_encounters_encounter_id_allergies(
    person_id="personId",
    encounter_id="encounterId",
    include_resolved="includeResolved",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose allergies are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter in which the allergies were added
    
</dd>
</dl>

<dl>
<dd>

**include_resolved:** `str` — A true or false value that includes or excludes allergies that are resolved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.allergies_and_intolerances.<a href="src/fern/allergies_and_intolerances/client.py">post_base_url_persons_person_id_chart_encounters_encounter_id_allergies</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add the allergy to patient's encounter
</dd>
</dl>
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

client.allergies_and_intolerances.post_base_url_persons_person_id_chart_encounters_encounter_id_allergies(
    person_id="personId",
    encounter_id="encounterId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose allergy is being added
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter to which the patient allergy belongs
    
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

<details><summary><code>client.allergies_and_intolerances.<a href="src/fern/allergies_and_intolerances/client.py">base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id1</a>(...) -> Ok1</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the allergy details for the given person id, encounter id, and allergy id.
</dd>
</dl>
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

client.allergies_and_intolerances.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id1(
    person_id="personId",
    encounter_id="encounterId",
    allergy_id="allergyId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose allergies are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter in which the allergy was added
    
</dd>
</dl>

<dl>
<dd>

**allergy_id:** `str` — (Required) (Required) The id of the allergy being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.allergies_and_intolerances.<a href="src/fern/allergies_and_intolerances/client.py">put_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a patient allergy
</dd>
</dl>
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

client.allergies_and_intolerances.put_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id(
    person_id="personId",
    encounter_id="encounterId",
    allergy_id="allergyId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose allergy is being updated
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter to which the patient allergy belongs
    
</dd>
</dl>

<dl>
<dd>

**allergy_id:** `str` — (Required) (Required) The id of the patient's allergy to be updated
    
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

<details><summary><code>client.allergies_and_intolerances.<a href="src/fern/allergies_and_intolerances/client.py">base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a patient's allergy
</dd>
</dl>
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

client.allergies_and_intolerances.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id(
    person_id="personId",
    encounter_id="encounterId",
    allergy_id="allergyId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose allergy is being deleted
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter to which the patient allergy belongs
    
</dd>
</dl>

<dl>
<dd>

**allergy_id:** `str` — (Required) (Required) The id of the patient's allergy to be deleted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.allergies_and_intolerances.<a href="src/fern/allergies_and_intolerances/client.py">base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions</a>(...) -> Ok6</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of reactions a patient experiences for the given allergy id.
</dd>
</dl>
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

client.allergies_and_intolerances.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions(
    person_id="personId",
    encounter_id="encounterId",
    allergy_id="allergyId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose allergies are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter to which the patient allergy belongs
    
</dd>
</dl>

<dl>
<dd>

**allergy_id:** `str` — (Required) (Required) The id of the allergy being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.allergies_and_intolerances.<a href="src/fern/allergies_and_intolerances/client.py">post_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a reaction that the patient experiences for the given allergy id
</dd>
</dl>
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

client.allergies_and_intolerances.post_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions(
    person_id="personId",
    encounter_id="encounterId",
    allergy_id="allergyId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose allergy reaction is being added
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter to which the patient allergy belongs
    
</dd>
</dl>

<dl>
<dd>

**allergy_id:** `str` — (Required) (Required) The id of the patient's allergy to which the reaction belongs
    
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

<details><summary><code>client.allergies_and_intolerances.<a href="src/fern/allergies_and_intolerances/client.py">put_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_reaction_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a reaction that the patient experiences for the given allergy id
</dd>
</dl>
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

client.allergies_and_intolerances.put_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_reaction_id(
    person_id="personId",
    encounter_id="encounterId",
    allergy_id="allergyId",
    reaction_id="reactionId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose allergy reaction is being updated
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter to which the patient allergy belongs
    
</dd>
</dl>

<dl>
<dd>

**allergy_id:** `str` — (Required) (Required) The id of the patient's allergy to which the reaction belongs
    
</dd>
</dl>

<dl>
<dd>

**reaction_id:** `str` — (Required) (Required) The id of the patient's allergy reaction to be updated
    
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

<details><summary><code>client.allergies_and_intolerances.<a href="src/fern/allergies_and_intolerances/client.py">base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_reaction_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a reaction that the patient experiences for the given allergy id
</dd>
</dl>
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

client.allergies_and_intolerances.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_reaction_id(
    person_id="personId",
    encounter_id="encounterId",
    allergy_id="allergyId",
    reaction_id="reactionId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose allergy reaction is being deleted
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter to which the patient allergy belongs
    
</dd>
</dl>

<dl>
<dd>

**allergy_id:** `str` — (Required) (Required) The id of the patient's allergy to which the reaction belongs
    
</dd>
</dl>

<dl>
<dd>

**reaction_id:** `str` — (Required) (Required) The id of the patient's allergy reaction to be deleted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.allergies_and_intolerances.<a href="src/fern/allergies_and_intolerances/client.py">base_url_persons_person_id_chart_health_concerns_allergies</a>(...) -> Ok7</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a patient's health concerns allergies.
</dd>
</dl>
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

client.allergies_and_intolerances.base_url_persons_person_id_chart_health_concerns_allergies(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose health concerns allergies are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Assessment and Plan of Treatment
<details><summary><code>client.assessment_and_plan_of_treatment.<a href="src/fern/assessment_and_plan_of_treatment/client.py">base_url_persons_person_id_chart_assessments</a>(...) -> Ok8</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets all assessment plans for the specified patient.
</dd>
</dl>
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

client.assessment_and_plan_of_treatment.base_url_persons_person_id_chart_assessments(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required)
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assessment_and_plan_of_treatment.<a href="src/fern/assessment_and_plan_of_treatment/client.py">base_url_persons_person_id_chart_care_plan_assessments</a>(...) -> Ok8</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns care plan assessments for a patient.
</dd>
</dl>
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

client.assessment_and_plan_of_treatment.base_url_persons_person_id_chart_care_plan_assessments(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required)
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assessment_and_plan_of_treatment.<a href="src/fern/assessment_and_plan_of_treatment/client.py">base_url_persons_person_id_chart_health_concerns_assessment_scales</a>(...) -> Ok10</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a patient's health concerns assessment scale for health concern.
</dd>
</dl>
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

client.assessment_and_plan_of_treatment.base_url_persons_person_id_chart_health_concerns_assessment_scales(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose health concerns assessment scale are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Care Team Members
<details><summary><code>client.care_team_members.<a href="src/fern/care_team_members/client.py">base_url_persons_person_id_chart_care_team_members</a>(...) -> Ok11</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of care team members for the specified person id after applying additional OData query operations.
</dd>
</dl>
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

client.care_team_members.base_url_persons_person_id_chart_care_team_members(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose care team members are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.care_team_members.<a href="src/fern/care_team_members/client.py">post_base_url_persons_person_id_chart_care_team_members</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add care team member for the specified person id
</dd>
</dl>
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

client.care_team_members.post_base_url_persons_person_id_chart_care_team_members(
    person_id="personId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose care team members are being saved
    
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

<details><summary><code>client.care_team_members.<a href="src/fern/care_team_members/client.py">put_base_url_persons_person_id_chart_care_team_members_care_team_member_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a patient's care team member record
</dd>
</dl>
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

client.care_team_members.put_base_url_persons_person_id_chart_care_team_members_care_team_member_id(
    person_id="personId",
    care_team_member_id="careTeamMemberId",
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

**person_id:** `str` — (Required) (Required) The id of patient whose care team member record is being updated
    
</dd>
</dl>

<dl>
<dd>

**care_team_member_id:** `str` — (Required) (Required) The id of the care team member being updated
    
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

<details><summary><code>client.care_team_members.<a href="src/fern/care_team_members/client.py">base_url_persons_person_id_chart_care_team_members_care_team_member_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a patient's care team member
</dd>
</dl>
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

client.care_team_members.base_url_persons_person_id_chart_care_team_members_care_team_member_id(
    person_id="personId",
    care_team_member_id="careTeamMemberId",
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

**person_id:** `str` — (Required) (Required) The id of patient whose care team member record is being deleted
    
</dd>
</dl>

<dl>
<dd>

**care_team_member_id:** `str` — (Required) (Required) The id of the care team member being deleted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Clinical Notes
<details><summary><code>client.clinical_notes.<a href="src/fern/clinical_notes/client.py">base_url_persons_person_id_chart_clinical_notes</a>(...) -> Ok12</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of clinical notes after performing additional OData query operations.
</dd>
</dl>
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

client.clinical_notes.base_url_persons_person_id_chart_clinical_notes(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose documents are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clinical_notes.<a href="src/fern/clinical_notes/client.py">base_url_persons_person_id_chart_encounters_encounter_id_clinical_notes</a>(...) -> Ok12</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of clinical notes for a given encounter.
</dd>
</dl>
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

client.clinical_notes.base_url_persons_person_id_chart_encounters_encounter_id_clinical_notes(
    person_id="personId",
    encounter_id="encounterId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose documents are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clinical_notes.<a href="src/fern/clinical_notes/client.py">base_url_persons_person_id_chart_documents</a>(...) -> Ok12</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of documents for the specified person id after performing additional OData query operations.
</dd>
</dl>
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

client.clinical_notes.base_url_persons_person_id_chart_documents(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose documents are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clinical_notes.<a href="src/fern/clinical_notes/client.py">base_url_persons_person_id_chart_documents_document_id</a>(...) -> Ok15</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the document details for the given person id and document id.
</dd>
</dl>
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

client.clinical_notes.base_url_persons_person_id_chart_documents_document_id(
    person_id="personId",
    document_id="documentId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose document is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` — (Required) (Required) The id of the document being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clinical_notes.<a href="src/fern/clinical_notes/client.py">base_url_persons_person_id_chart_documents_document_id_pdf</a>(...) -> Ok16</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the full document in pdf format for the given person id and document id.

Response will include PDF encoded binary content:

%PDF
...
%EOF)

200 response details show JSON component of response.
</dd>
</dl>
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

client.clinical_notes.base_url_persons_person_id_chart_documents_document_id_pdf(
    person_id="personId",
    document_id="documentId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose document is being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` — (Required) (Required) The id of the document being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clinical_notes.<a href="src/fern/clinical_notes/client.py">base_url_persons_person_id_chart_encounters_encounter_id_documents</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a document for the specified person and encounter.

This POST route does not use a simple JSON request body - this route requires a multipart/form-data request structure (and a Content-Type header of multipart/form-data that also includes a boundary definition).
Comments (which each begin with //DELETE ME) have been inserted into the POST body in this documentation. Removing each of these comment lines will result in a valid request body schema.

When comments are removed and values are entered for each variable request element, this will result in a request body with the structure shown in the example below:

Example Request Header:

"Content-Type": "multipart/form data; boundary=threequarksformustermark"

Example Multipart Request Body:  

--thr33quarks4mustermark
Content-Disposition: form-data; name="request"
Content-Type: application/json
{
"documentType": "EHRImage",
"fileDescription": "Text Description of Document to Appear in UI"
}

--thr33quarks4mustermark
Content-Disposition: form-data; name="file"; filename="this-will-be-the-filename.PDF"
Content-Type: application/pdf

%PDF-1.7
%µµµµ
  //truncated for brevity;
%%EOF

--thr33quarks4mustermark--
</dd>
</dl>
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

client.clinical_notes.base_url_persons_person_id_chart_encounters_encounter_id_documents(
    person_id="personId",
    encounter_id="encounterId",
    request="<string>",
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

**person_id:** `str` — (Required) (Required) The person identifier.
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The encounter id to associate this document with.
    
</dd>
</dl>

<dl>
<dd>

**request:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Goals
<details><summary><code>client.goals.<a href="src/fern/goals/client.py">base_url_persons_person_id_chart_care_plan_goals</a>(...) -> Ok17</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a patient's care plan goals.
</dd>
</dl>
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

client.goals.base_url_persons_person_id_chart_care_plan_goals(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose goals are being fetched
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.goals.<a href="src/fern/goals/client.py">base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals</a>(...) -> Ok17</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a patient's care plan goals for a specified encounter and health concern.
</dd>
</dl>
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

client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals(
    person_id="personId",
    encounter_id="encounterId",
    health_concern_id="healthConcernId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose goals are being fetched
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the patient encounter whose goals are being fetched
    
</dd>
</dl>

<dl>
<dd>

**health_concern_id:** `str` — (Required) (Required) The id of the health concern whose goals are being fetched
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.goals.<a href="src/fern/goals/client.py">post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new care plan goal for a patient for specified encounter and health concern
</dd>
</dl>
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

client.goals.post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals(
    person_id="personId",
    encounter_id="encounterId",
    health_concern_id="healthConcernId",
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

**person_id:** `str` — (Required) (Required) id of the Patient
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) id of the encounter
    
</dd>
</dl>

<dl>
<dd>

**health_concern_id:** `str` — (Required) (Required) id of Health Concern
    
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

<details><summary><code>client.goals.<a href="src/fern/goals/client.py">base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id1</a>(...) -> Ok19</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a patient's care plan goal details.
</dd>
</dl>
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

client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id1(
    person_id="personId",
    encounter_id="encounterId",
    health_concern_id="healthConcernId",
    goal_id="goalId",
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

**person_id:** `str` — (Required) (Required) The id of the patient
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter
    
</dd>
</dl>

<dl>
<dd>

**health_concern_id:** `str` — (Required) (Required) The id of the health concern
    
</dd>
</dl>

<dl>
<dd>

**goal_id:** `str` — (Required) (Required) The id of the goal
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.goals.<a href="src/fern/goals/client.py">put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update patient's careplan goal.
</dd>
</dl>
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

client.goals.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id(
    person_id="personId",
    encounter_id="encounterId",
    health_concern_id="healthConcernId",
    goal_id="goalId",
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

**person_id:** `str` — (Required) (Required) The id of the patient
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) Encounter id of the patient
    
</dd>
</dl>

<dl>
<dd>

**health_concern_id:** `str` — (Required) (Required) Care plan health concern id of the patient
    
</dd>
</dl>

<dl>
<dd>

**goal_id:** `str` — (Required) (Required) Care plan goal id of the patient
    
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

<details><summary><code>client.goals.<a href="src/fern/goals/client.py">base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a Care Plan Goal
</dd>
</dl>
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

client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id(
    person_id="personId",
    encounter_id="encounterId",
    health_concern_id="healthConcernId",
    goal_id="goalId",
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

**person_id:** `str` — (Required) (Required) The id of the patient
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the patient encounter
    
</dd>
</dl>

<dl>
<dd>

**health_concern_id:** `str` — (Required) (Required) The id of the health concern
    
</dd>
</dl>

<dl>
<dd>

**goal_id:** `str` — (Required) (Required) Care plan goal id of patient
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.goals.<a href="src/fern/goals/client.py">base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions</a>(...) -> Ok20</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of interventions for the specified person id, encounter id, health concern id and goal id after applying additional OData query operations.
</dd>
</dl>
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

client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions(
    person_id="personId",
    encounter_id="encounterId",
    health_concern_id="healthConcernId",
    goal_id="goalId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose interventions are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter whose interventions are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**health_concern_id:** `str` — (Required) (Required) The id of the health concern whose interventions are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**goal_id:** `str` — (Required) (Required) The id of the goal whose interventions are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.goals.<a href="src/fern/goals/client.py">post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add new intervention details
</dd>
</dl>
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

client.goals.post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions(
    person_id="personId",
    encounter_id="encounterId",
    health_concern_id="healthConcernId",
    goal_id="goalId",
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

**person_id:** `str` — (Required) (Required) The id of the patient
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the patient encounter
    
</dd>
</dl>

<dl>
<dd>

**health_concern_id:** `str` — (Required) (Required) The id of the health concern
    
</dd>
</dl>

<dl>
<dd>

**goal_id:** `str` — (Required) (Required) Care plan goal id of patient
    
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

<details><summary><code>client.goals.<a href="src/fern/goals/client.py">base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id1</a>(...) -> Ok21</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets intervention details based on person id, encounter id, health concern id , goal id and intervention id.
</dd>
</dl>
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

client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id1(
    person_id="personId",
    encounter_id="encounterId",
    health_concern_id="healthConcernId",
    goal_id="goalId",
    intervention_id="interventionId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose intervention is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter whose intervention is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**health_concern_id:** `str` — (Required) (Required) The id of the health concern whose intervention is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**goal_id:** `str` — (Required) (Required) The id of the goal whose intervention is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**intervention_id:** `str` — (Required) (Required) The id of the intervention to be retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.goals.<a href="src/fern/goals/client.py">put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates intervention details
</dd>
</dl>
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

client.goals.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id(
    person_id="personId",
    encounter_id="encounterId",
    health_concern_id="healthConcernId",
    goal_id="goalId",
    intervention_id="interventionId",
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

**person_id:** `str` — (Required) (Required) The id of the patient.
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the patient encounter.
    
</dd>
</dl>

<dl>
<dd>

**health_concern_id:** `str` — (Required) (Required) The id of the health concern.
    
</dd>
</dl>

<dl>
<dd>

**goal_id:** `str` — (Required) (Required) Care plan goal id of patient.
    
</dd>
</dl>

<dl>
<dd>

**intervention_id:** `str` — (Required) (Required) Care plan intervention id for patient.
    
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

<details><summary><code>client.goals.<a href="src/fern/goals/client.py">base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Patient intervention details
</dd>
</dl>
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

client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id(
    person_id="personId",
    encounter_id="encounterId",
    health_concern_id="healthConcernId",
    goal_id="goalId",
    intervention_id="interventionId",
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

**person_id:** `str` — (Required) (Required) The id of the patient
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter
    
</dd>
</dl>

<dl>
<dd>

**health_concern_id:** `str` — (Required) (Required) The id of the health concern
    
</dd>
</dl>

<dl>
<dd>

**goal_id:** `str` — (Required) (Required) The id of the goal
    
</dd>
</dl>

<dl>
<dd>

**intervention_id:** `str` — (Required) (Required) The id of the intervention
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.goals.<a href="src/fern/goals/client.py">base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes</a>(...) -> Ok22</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of care plan outcomes for the specified person, encounter, concern, and goal after applying additional OData query operations.
</dd>
</dl>
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

client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes(
    person_id="personId",
    encounter_id="encounterId",
    health_concern_id="healthConcernId",
    goal_id="goalId",
    intervention_id="interventionId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose care plan outcomes are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) Encounter id for outcome
    
</dd>
</dl>

<dl>
<dd>

**health_concern_id:** `str` — (Required) (Required) Care plan health concern id of patient
    
</dd>
</dl>

<dl>
<dd>

**goal_id:** `str` — (Required) (Required) Care plan goal id of patient
    
</dd>
</dl>

<dl>
<dd>

**intervention_id:** `str` — (Required) (Required) Care plan intervention id for patient
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.goals.<a href="src/fern/goals/client.py">post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add new outcome details
</dd>
</dl>
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

client.goals.post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes(
    person_id="personId",
    encounter_id="encounterId",
    health_concern_id="healthConcernId",
    goal_id="goalId",
    intervention_id="interventionId",
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

**person_id:** `str` — (Required) (Required) The id of the patient
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the patient encounter
    
</dd>
</dl>

<dl>
<dd>

**health_concern_id:** `str` — (Required) (Required) The id of the health concern
    
</dd>
</dl>

<dl>
<dd>

**goal_id:** `str` — (Required) (Required) Care plan goal id of patient
    
</dd>
</dl>

<dl>
<dd>

**intervention_id:** `str` — (Required) (Required) Care plan intervention id for patient
    
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

<details><summary><code>client.goals.<a href="src/fern/goals/client.py">get_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id</a>(...) -> Ok23</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the care plan outcome details for the given outcome id.
</dd>
</dl>
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

client.goals.get_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
    person_id="personId",
    encounter_id="encounterId",
    health_concern_id="healthConcernId",
    goal_id="goalId",
    intervention_id="interventionId",
    outcome_id="outcomeId",
    expand="$expand",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose care plan outcomes are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) Encounter id for outcome
    
</dd>
</dl>

<dl>
<dd>

**health_concern_id:** `str` — (Required) (Required) Care plan health concern id of patient
    
</dd>
</dl>

<dl>
<dd>

**goal_id:** `str` — (Required) (Required) Care plan goal id of patient
    
</dd>
</dl>

<dl>
<dd>

**intervention_id:** `str` — (Required) (Required) Care plan intervention id for patient
    
</dd>
</dl>

<dl>
<dd>

**outcome_id:** `str` — (Required) (Required) Care plan outcome id for patient
    
</dd>
</dl>

<dl>
<dd>

**expand:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.goals.<a href="src/fern/goals/client.py">put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates outcome details
</dd>
</dl>
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

client.goals.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
    person_id="personId",
    encounter_id="encounterId",
    health_concern_id="healthConcernId",
    goal_id="goalId",
    intervention_id="interventionId",
    outcome_id="outcomeId",
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

**person_id:** `str` — (Required) (Required) The id of the patient.
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the patient encounter.
    
</dd>
</dl>

<dl>
<dd>

**health_concern_id:** `str` — (Required) (Required) The id of the health concern.
    
</dd>
</dl>

<dl>
<dd>

**goal_id:** `str` — (Required) (Required) Care plan goal id of patient.
    
</dd>
</dl>

<dl>
<dd>

**intervention_id:** `str` — (Required) (Required) Care plan intervention id for patient.
    
</dd>
</dl>

<dl>
<dd>

**outcome_id:** `str` — (Required) (Required) Care plan outcome id for patient.
    
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

<details><summary><code>client.goals.<a href="src/fern/goals/client.py">base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete outcome details
</dd>
</dl>
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

client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
    person_id="personId",
    encounter_id="encounterId",
    health_concern_id="healthConcernId",
    goal_id="goalId",
    intervention_id="interventionId",
    outcome_id="outcomeId",
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

**person_id:** `str` — (Required) (Required) The id of the patient
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the patient encounter
    
</dd>
</dl>

<dl>
<dd>

**health_concern_id:** `str` — (Required) (Required) The id of the health concern
    
</dd>
</dl>

<dl>
<dd>

**goal_id:** `str` — (Required) (Required) Care plan goal id of patient
    
</dd>
</dl>

<dl>
<dd>

**intervention_id:** `str` — (Required) (Required) Care plan intervention id of the patient
    
</dd>
</dl>

<dl>
<dd>

**outcome_id:** `str` — (Required) (Required) Care plan outcome of the patient
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Health Concerns
<details><summary><code>client.health_concerns.<a href="src/fern/health_concerns/client.py">base_url_persons_person_id_chart_care_plan_health_concerns</a>(...) -> Ok24</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of health concerns for the specified person id after applying additional OData query operations.
</dd>
</dl>
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

client.health_concerns.base_url_persons_person_id_chart_care_plan_health_concerns(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose health concerns are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.health_concerns.<a href="src/fern/health_concerns/client.py">base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates patient's careplan health concern.
</dd>
</dl>
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

client.health_concerns.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns(
    person_id="personId",
    encounter_id="encounterId",
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

**person_id:** `str` — (Required) (Required) The id of the patient.
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) Encounter id for healthconcern
    
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

<details><summary><code>client.health_concerns.<a href="src/fern/health_concerns/client.py">get_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id</a>(...) -> Ok25</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns specific health concern details for a patient.
</dd>
</dl>
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

client.health_concerns.get_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
    person_id="personId",
    encounter_id="encounterId",
    health_concern_id="healthConcernId",
    expand="$expand",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose health concern are being fetched
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the patient encounter whose health concern are being fetched
    
</dd>
</dl>

<dl>
<dd>

**health_concern_id:** `str` — (Required) (Required) The id of the health concern whose health concern are being fetched
    
</dd>
</dl>

<dl>
<dd>

**expand:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.health_concerns.<a href="src/fern/health_concerns/client.py">put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update patient's careplan health concern.
</dd>
</dl>
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

client.health_concerns.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
    person_id="personId",
    encounter_id="encounterId",
    health_concern_id="healthConcernId",
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

**person_id:** `str` — (Required) (Required) The id of the patient.
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) Encounter id for healthconcern
    
</dd>
</dl>

<dl>
<dd>

**health_concern_id:** `str` — (Required) (Required) Care plan health concern id of patient
    
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

<details><summary><code>client.health_concerns.<a href="src/fern/health_concerns/client.py">base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete health concern details
</dd>
</dl>
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

client.health_concerns.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
    person_id="personId",
    encounter_id="encounterId",
    health_concern_id="healthConcernId",
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

**person_id:** `str` — (Required) (Required) The id of the patient
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the patient encounter
    
</dd>
</dl>

<dl>
<dd>

**health_concern_id:** `str` — (Required) (Required) The id of the health concern
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.health_concerns.<a href="src/fern/health_concerns/client.py">base_url_persons_person_id_chart_health_concerns_encounter_diagnosis</a>(...) -> Ok26</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a patient's health concerns encounter diagnosis for health concern.
</dd>
</dl>
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

client.health_concerns.base_url_persons_person_id_chart_health_concerns_encounter_diagnosis(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose health concerns encounter diagnosis are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.health_concerns.<a href="src/fern/health_concerns/client.py">base_url_persons_person_id_chart_health_concerns_family_histories_organizer</a>(...) -> Ok28</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a patient's family histories for health concern.
</dd>
</dl>
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

client.health_concerns.base_url_persons_person_id_chart_health_concerns_family_histories_organizer(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose health concerns family histories are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.health_concerns.<a href="src/fern/health_concerns/client.py">base_url_persons_person_id_chart_health_concerns_problem_observations</a>(...) -> Ok29</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a patient's health concerns problem observation.
</dd>
</dl>
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

client.health_concerns.base_url_persons_person_id_chart_health_concerns_problem_observations(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose health concerns problem observation are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.health_concerns.<a href="src/fern/health_concerns/client.py">base_url_persons_person_id_chart_health_concerns_social_history</a>(...) -> Ok30</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a patient's social history for health concern.
</dd>
</dl>
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

client.health_concerns.base_url_persons_person_id_chart_health_concerns_social_history(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose health concerns social history are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.health_concerns.<a href="src/fern/health_concerns/client.py">base_url_persons_person_id_chart_health_concerns_vitals</a>(...) -> Ok31</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a patient's vitals for health concern.
</dd>
</dl>
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

client.health_concerns.base_url_persons_person_id_chart_health_concerns_vitals(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose health concern vitals are being fetched
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Immunizations
<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_charts_immunizations</a>(...) -> Ok32</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

GETs immunizations updated within a given interval. If an oData filter of createTimestamp or modifyTimestamp is not specified, immunizations which are created or updated for the last 7 days are retrieved.
</dd>
</dl>
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

client.immunizations.base_url_persons_charts_immunizations(
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**top:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a patient's immunization order record
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders(
    person_id="personId",
    encounter_id="encounterId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose immunization order record is being added
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter for which the immunization order is being added
    
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

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a patient's immunization order record
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id(
    person_id="personId",
    encounter_id="encounterId",
    order_id="orderId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose immunization order record is being updated
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter that contains the immunization order is being updated
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the immunization order being updated
    
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

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a patient's ordered vaccine record
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines(
    person_id="personId",
    encounter_id="encounterId",
    order_id="orderId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose vaccine record is being added
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter that contains the immunization order to which vaccine record id being added
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the immunization order to which vaccine record is being added
    
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

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a patient's vaccine record.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id(
    person_id="personId",
    encounter_id="encounterId",
    order_id="orderId",
    vaccine_id="vaccineId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose vaccine record is being updated
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter for the immunization order which contains the vaccine being updated
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the immunization order which contains the vaccine being updated
    
</dd>
</dl>

<dl>
<dd>

**vaccine_id:** `str` — (Required) (Required) The id of the ordered vaccine being updated
    
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

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds vaccine vis history for the provided ordered vaccine
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories(
    person_id="personId",
    encounter_id="encounterId",
    order_id="orderId",
    vaccine_id="vaccineId",
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

**person_id:** `str` — (Required) (Required) The id of the person associated with the vaccine vis history that is being added
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter associated with the vaccine for which vis history is being added
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the immunization order which contains the vaccine for which vis history is being added
    
</dd>
</dl>

<dl>
<dd>

**vaccine_id:** `str` — (Required) (Required) The id of the vaccine for which vis history is being added
    
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

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories_vis_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a patient's vaccine vis history record.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories_vis_id(
    person_id="personId",
    encounter_id="encounterId",
    order_id="orderId",
    vaccine_id="vaccineId",
    vis_id="visId",
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

**person_id:** `str` — (Required) (Required) The id of the person associated with the vaccine vis history that is being updated
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter associated with the vaccine for which vis history is being updated
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the immunization order which contains the vaccine for which vis history is being updated
    
</dd>
</dl>

<dl>
<dd>

**vaccine_id:** `str` — (Required) (Required) The id of the vaccine for which vis history is being updated
    
</dd>
</dl>

<dl>
<dd>

**vis_id:** `str` — (Required) (Required) The id of the vis history record that is being updated
    
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

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a wasted vaccine record associated with a patient's ordered vaccine.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines(
    person_id="personId",
    encounter_id="encounterId",
    order_id="orderId",
    vaccine_id="vaccineId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose ordered vaccine is associated with the wasted vaccine record that is being added
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter that contains the ordered vaccine that is associated with the wasted vaccine record
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the immunization order which contains the ordered vaccine associated with the wasted vaccine record
    
</dd>
</dl>

<dl>
<dd>

**vaccine_id:** `str` — (Required) (Required) The id of the ordered vaccine that is associated with the wasted vaccine that is being added
    
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

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations</a>(...) -> Ok32</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of ordered vaccines for the specified person id after performing additional OData query operations.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the person whose ordered vaccines are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations_dose_validation</a>(...) -> Ok34</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of vaccine dose validation for the specified person id.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations_dose_validation(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the person whose vaccine dose validation information is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations_exclusions</a>(...) -> Ok35</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of excluded vaccines for the specified person id after performing additional OData query operations.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations_exclusions(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the person whose excluded vaccines are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` — (Required)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">post_base_url_persons_person_id_chart_immunizations_exclusions</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a patient's vaccine exclusion record
</dd>
</dl>
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

client.immunizations.post_base_url_persons_person_id_chart_immunizations_exclusions(
    person_id="personId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose vaccine exclusion record is being added
    
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

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations_exclusions_exclusion_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a patient's excluded vaccine record
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations_exclusions_exclusion_id(
    person_id="personId",
    exclusion_id="exclusionId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose excluded vaccine record is being updated
    
</dd>
</dl>

<dl>
<dd>

**exclusion_id:** `str` — (Required) (Required) The id of the excluded vaccine being updated
    
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

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations_group_status</a>(...) -> Ok36</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of vaccine group status for the specified person id.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations_group_status(
    person_id="personId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose vaccine group statuses are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations_interactions</a>(...) -> Ok37</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets patient interactions for a vaccine with the given CVX and CPT codes.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations_interactions(
    person_id="personId",
    cvx_code="cvxCode",
    cpt_code="cptCode",
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

**person_id:** `str` — (Required) (Required) The id of the person whose interactions are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**cvx_code:** `str` — (Required) The cvx code of the vaccine for which interaction are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**cpt_code:** `str` — (Required) The cpt code of the vaccine for which interaction are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations_orders</a>(...) -> Ok38</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets immunization orders for the specified person after performing additional OData operations.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations_orders(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the person whose immunization order is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations_orders_order_id</a>(...) -> Ok39</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets immunization order details for the specified person and order.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id(
    person_id="personId",
    order_id="orderId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose immunization order is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the immunization order being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations_orders_order_id_insurances</a>(...) -> Ok40</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of insurances that are associated with the specified person Id and order Id.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_insurances(
    person_id="personId",
    order_id="orderId",
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

**person_id:** `str` — (Required) (Required) The id of the person for whom the order insurances are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the immunization order for which insurances are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations_orders_order_id_tracking_comments</a>(...) -> Ok41</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of tracking comments for the given person id and order id.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_tracking_comments(
    person_id="personId",
    order_id="orderId",
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

**person_id:** `str` — (Required) (Required) The id of the person who the order belongs to
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the order whose tracking comments are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">post_base_url_persons_person_id_chart_immunizations_orders_order_id_tracking_comments</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a tracking comment for the given person id and order id
</dd>
</dl>
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

client.immunizations.post_base_url_persons_person_id_chart_immunizations_orders_order_id_tracking_comments(
    person_id="personId",
    order_id="orderId",
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

**person_id:** `str` — (Required) (Required) The id of the person who the order belongs to
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the order whose tracking comments are being retrieved
    
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

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines</a>(...) -> Ok42</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets vaccines for the given person id and order id.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines(
    person_id="personId",
    order_id="orderId",
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

**person_id:** `str` — (Required) (Required) The id of the person who the order belongs to
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the order whose vaccines are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id1</a>(...) -> Ok43</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets vaccine details for the given person id, order id, and vaccine id.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id1(
    person_id="personId",
    order_id="orderId",
    vaccine_id="vaccineId",
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

**person_id:** `str` — (Required) (Required) The id of the person who the order belongs to
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the order whose vaccines are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**vaccine_id:** `str` — (Required) (Required) The id of the vaccine for which we are retrieving the details
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a patient's ordered vaccine record.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id(
    person_id="personId",
    order_id="orderId",
    vaccine_id="vaccineId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose vaccine record is being deleted
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the immunization order which contains the vaccine being deleted
    
</dd>
</dl>

<dl>
<dd>

**vaccine_id:** `str` — (Required) (Required) The id of the ordered vaccine being deleted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_component_lot_numbers</a>(...) -> Ok44</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of component lot numbers for the specified ordered vaccine ID.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_component_lot_numbers(
    person_id="personId",
    order_id="orderId",
    vaccine_id="vaccineId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose ordered vaccine component lot numbers are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the immunization order which contains the vaccine whose component lot numbers are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**vaccine_id:** `str` — (Required) (Required) The id of the ordered vaccine whose component lot numbers are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_suspected_diagnoses</a>(...) -> Ok45</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of diagnosis for the specified ordered vaccine ID.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_suspected_diagnoses(
    person_id="personId",
    order_id="orderId",
    vaccine_id="vaccineId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose diagnosis are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the immunization order which contains the vaccine whose associated diagnosis are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**vaccine_id:** `str` — (Required) (Required) The id of the ordered vaccine whose associated diagnosis are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories</a>(...) -> Ok46</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of VIS histories that are documented as given to the patient for the specified ordered vaccine ID.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories(
    person_id="personId",
    order_id="orderId",
    vaccine_id="vaccineId",
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

**person_id:** `str` — (Required) (Required) The id of the person for who the vaccine VIS history information belongs to
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the immunization order which contains the vaccine for which the vaccine VIS history information was documented
    
</dd>
</dl>

<dl>
<dd>

**vaccine_id:** `str` — (Required) (Required) The id of the ordered vaccine for which the vaccine VIS history information was recorded
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines</a>(...) -> Ok47</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of wasted vaccines for the specified person Id, order Id and vaccine Id.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines(
    person_id="personId",
    order_id="orderId",
    vaccine_id="vaccineId",
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

**person_id:** `str` — (Required) (Required) Id of the person whose wasted vaccines are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) Id of the order associated with the wasted vaccines that are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**vaccine_id:** `str` — (Required) (Required) Id of the ordered vaccine whose wasted vaccines are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines_wasted_vaccine_id</a>(...) -> Ok47</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the wasted vaccine details for the specified person Id, order Id, vaccine Id and wasted vaccine Id.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines_wasted_vaccine_id(
    person_id="personId",
    order_id="orderId",
    vaccine_id="vaccineId",
    wasted_vaccine_id="wastedVaccineId",
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

**person_id:** `str` — (Required) (Required) Id of the person whose wasted vaccine details are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) Id of the order associated with the wasted vaccine detials that are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**vaccine_id:** `str` — (Required) (Required) Id of the ordered vaccine whose wasted vaccine detials are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**wasted_vaccine_id:** `str` — (Required) (Required) Id of the wasted vaccine whose detials are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations_series_completions</a>(...) -> Ok49</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a patient's immunization series completion records.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations_series_completions(
    person_id="personId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose immunization series completion records are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">post_base_url_persons_person_id_chart_immunizations_series_completions</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a patient's immunization series completion record
</dd>
</dl>
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

client.immunizations.post_base_url_persons_person_id_chart_immunizations_series_completions(
    person_id="personId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose immunization series completion record is being added
    
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

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">base_url_persons_person_id_chart_immunizations_series_completions_series_id</a>(...) -> Ok49</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a patient's immunization series completion information for the provided person Id and series completion Id.
</dd>
</dl>
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

client.immunizations.base_url_persons_person_id_chart_immunizations_series_completions_series_id(
    person_id="personId",
    series_id="seriesId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose immunization series completion information is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**series_id:** `str` — (Required) (Required) The id of the series completion record whose details are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.immunizations.<a href="src/fern/immunizations/client.py">put_base_url_persons_person_id_chart_immunizations_series_completions_series_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a patient's immunization series completion record
</dd>
</dl>
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

client.immunizations.put_base_url_persons_person_id_chart_immunizations_series_completions_series_id(
    person_id="personId",
    series_id="seriesId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose immunization series completion record is being updated
    
</dd>
</dl>

<dl>
<dd>

**series_id:** `str` — (Required) (Required) The id of the series being updated
    
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

## Implantable Device Identifiers
<details><summary><code>client.implantable_device_identifiers.<a href="src/fern/implantable_device_identifiers/client.py">base_url_persons_person_id_chart_devices</a>(...) -> Ok51</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of implantable devices for the specified person id after applying additional OData query operations.
</dd>
</dl>
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

client.implantable_device_identifiers.base_url_persons_person_id_chart_devices(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose devices are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.implantable_device_identifiers.<a href="src/fern/implantable_device_identifiers/client.py">base_url_persons_person_id_chart_devices_device_id</a>(...) -> Ok52</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single implantable device for the specified person id and device id.
</dd>
</dl>
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

client.implantable_device_identifiers.base_url_persons_person_id_chart_devices_device_id(
    person_id="personId",
    device_id="deviceId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose device information is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**device_id:** `str` — (Required) (Required) The device id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Laboratory
<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_encounters_encounter_id_lab_orders</a>(...) -> Ok53</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new lab order for the given person id and encounter id.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_encounters_encounter_id_lab_orders(
    person_id="personId",
    encounter_id="encounterId",
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

**person_id:** `str` — (Required) (Required) The id of the patient to add the new lab order for.
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter to add the new lab order to.
    
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

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_orders</a>(...) -> Ok54</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of lab order summaries for the specified person id after applying additional OData query operations.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_orders(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose lab orders are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_orders_order_id1</a>(...) -> Ok53</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the lab order details for the given person id and order id.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id1(
    person_id="personId",
    order_id="orderId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose lab orders are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the lab order being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">put_base_url_persons_person_id_chart_lab_orders_order_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the specified lab order id for the person id.
</dd>
</dl>
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

client.laboratory.put_base_url_persons_person_id_chart_lab_orders_order_id(
    person_id="personId",
    order_id="orderId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose order is to be updated.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the order that is to be updated.
    
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

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_orders_order_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the specified order id for the person id.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id(
    person_id="personId",
    order_id="orderId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose order is to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the order that is to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_orders_order_id_insurances</a>(...) -> Ok56</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of insurances that are associated with the specified person Id and order Id after apply additional OData operations.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_insurances(
    person_id="personId",
    order_id="orderId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the person for whom the order insurances are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the lab order for which the insurances are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_orders_order_id_schedule</a>(...) -> Ok57</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the schedule details for the specified person id and order id.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_schedule(
    person_id="personId",
    order_id="orderId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose order schedule is being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the order whose schedule is being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">post_base_url_persons_person_id_chart_lab_orders_order_id_schedule</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the schedule for the specified person id and order id.
</dd>
</dl>
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

client.laboratory.post_base_url_persons_person_id_chart_lab_orders_order_id_schedule(
    person_id="personId",
    order_id="orderId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose order is being scheduled.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the order that is being scheduled.
    
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

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_orders_order_id_send</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a record to the interface queue with the provided order Id and lab interface agent information that is determined based on the order's lab Id. This route does not control when the order will be processed and sent out to the lab which is controlled by the interface.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_send(
    person_id="personId",
    order_id="orderId",
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

**person_id:** `str` — (Required) (Required) Id of the person whose order is being sent to interface
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) Id of the lab order which is being sent to interface
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_orders_order_id_tests</a>(...) -> Ok58</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of ordered test summaries for the specified person id and order id after apply additional OData operations.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests(
    person_id="personId",
    order_id="orderId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose ordered tests are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the lab order for which the ordered tests are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">post_base_url_persons_person_id_chart_lab_orders_order_id_tests</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a lab test to the specified order id for the person id.
</dd>
</dl>
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

client.laboratory.post_base_url_persons_person_id_chart_lab_orders_order_id_tests(
    person_id="personId",
    order_id="orderId",
    request=[],
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

**person_id:** `str` — (Required) (Required) The id of the person where the new lab test will be added to the order.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the order where the new lab test will be added.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id1</a>(...) -> Ok59</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the ordered test for the specified person id, order id and test id.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id1(
    person_id="personId",
    order_id="orderId",
    test_id="testId",
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

**person_id:** `str` — (Required) (Required) The id of the patient to retrieve the ordered test for.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the lab order which contains the test that were ordered.
    
</dd>
</dl>

<dl>
<dd>

**test_id:** `str` — (Required) (Required) The id of the ordered test being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the specified order test for the specified person and order.
</dd>
</dl>
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

client.laboratory.put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id(
    person_id="personId",
    order_id="orderId",
    test_id="testId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose ordered test is to be updated.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the order whose ordered test is to be updated.
    
</dd>
</dl>

<dl>
<dd>

**test_id:** `str` — (Required) (Required) The id of the ordered test that is to be updated.
    
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

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the specified ordered test for the person and order.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id(
    person_id="personId",
    order_id="orderId",
    test_id="testId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose ordered test will be deleted.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the order whose ordered test will be deleted.
    
</dd>
</dl>

<dl>
<dd>

**test_id:** `str` — (Required) (Required) The id of the order test to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers</a>(...) -> Ok60</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of order entry answers for the specified person id, order id and test id after applying additional OData operations.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers(
    person_id="personId",
    order_id="orderId",
    test_id="testId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the person whose order entry answers are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the order whose order entry answers are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**test_id:** `str` — (Required) (Required) The id of the ordered test whose order entry answers are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds an answer to an order entry question for the specified person id, order id and test id.
</dd>
</dl>
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

client.laboratory.post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers(
    person_id="personId",
    order_id="orderId",
    test_id="testId",
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

**person_id:** `str` — (Required) (Required) This id of the person whose order entry answer is to be added.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the order whose order entry answer is to be added.
    
</dd>
</dl>

<dl>
<dd>

**test_id:** `str` — (Required) (Required) The id of the ordered test whose order entry answer is to be added.
    
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

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the specifed order entry answer for the specified person id, order id, test id and answer id.
</dd>
</dl>
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

client.laboratory.put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id(
    person_id="personId",
    order_id="orderId",
    test_id="testId",
    answer_id="answerId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose order entry answer is being updated.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the order whose order entry answer is being updated.
    
</dd>
</dl>

<dl>
<dd>

**test_id:** `str` — (Required) (Required) The id of the ordered test id whose order entry answer is being udpated.
    
</dd>
</dl>

<dl>
<dd>

**answer_id:** `str` — (Required) (Required) The id of the order entry answer to update.
    
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

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the specified order entry answer for the specified person id, order id and ordered test id.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id(
    person_id="personId",
    order_id="orderId",
    test_id="testId",
    answer_id="answerId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose order entry answer is being deleted.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the order whose order entry answer is being deleted.
    
</dd>
</dl>

<dl>
<dd>

**test_id:** `str` — (Required) (Required) The id of the ordered test id whose order entry answer is being deleted.
    
</dd>
</dl>

<dl>
<dd>

**answer_id:** `str` — (Required) (Required)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses</a>(...) -> Ok61</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of suspected diagnosis for the specified ordered test id after applying addition OData operations.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses(
    person_id="personId",
    order_id="orderId",
    test_id="testId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the person whose suspected diagnoses are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the lab order which contains the test whose suspected diagnosis are beign retrieved.
    
</dd>
</dl>

<dl>
<dd>

**test_id:** `str` — (Required) (Required) The id of the ordered test whose suspected diagnosis are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a suspected diagnosis for the specified person id, order id and test id.
</dd>
</dl>
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

client.laboratory.post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses(
    person_id="personId",
    order_id="orderId",
    test_id="testId",
    request=[],
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

**person_id:** `str` — (Required) (Required) The id of the person for which the suspected diagnosis will be added.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the order for which the suspected diagnosis will be added.
    
</dd>
</dl>

<dl>
<dd>

**test_id:** `str` — (Required) (Required) The id of the ordered test for which the suspected diagnosis will be added.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses_diagnosis_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the specified suspected diagnosis for the specified person id, order id and test id.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses_diagnosis_id(
    person_id="personId",
    order_id="orderId",
    test_id="testId",
    diagnosis_id="diagnosisId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose suspected diagnosis is to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the order whose suspected diagnosis is to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**test_id:** `str` — (Required) (Required) The id of the ordered test whose suspected diagnosis is to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**diagnosis_id:** `str` — (Required) (Required) The id of the suspected diagnosis to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments</a>(...) -> Ok41</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of tracking comments for the given person id and order id.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments(
    person_id="personId",
    order_id="orderId",
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

**person_id:** `str` — (Required) (Required) The id of the person who the order belongs to
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the order whose tracking comments are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">post_base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a tracking comment for the given person id and lab order id.
</dd>
</dl>
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

client.laboratory.post_base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments(
    person_id="personId",
    order_id="orderId",
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

**person_id:** `str` — (Required) (Required) The id of the person who the order belongs to.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — (Required) (Required) The id of the lab order which the tracking comment will be added for.
    
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

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_panels</a>(...) -> Ok63</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of observation panels for the specified person id after applying additional OData operations.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_panels(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the person for whom the observation panels are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">post_base_url_persons_person_id_chart_lab_panels</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds an observation panel the specified person.
</dd>
</dl>
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

client.laboratory.post_base_url_persons_person_id_chart_lab_panels(
    person_id="personId",
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

**person_id:** `str` — (Required) (Required) The id of the person to add the observation panel for.
    
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

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_panels_panel_id1</a>(...) -> Ok64</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets an observation panel for the specified person id and panel id.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_panels_panel_id1(
    person_id="personId",
    panel_id="panelId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose observation panel is being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**panel_id:** `str` — (Required) (Required) The id of the observation panel being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">put_base_url_persons_person_id_chart_lab_panels_panel_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the specified observation panel for the specified personId.
</dd>
</dl>
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

client.laboratory.put_base_url_persons_person_id_chart_lab_panels_panel_id(
    person_id="personId",
    panel_id="panelId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose observation panel is to be updated.
    
</dd>
</dl>

<dl>
<dd>

**panel_id:** `str` — (Required) (Required) The id of the panel to be updated.
    
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

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_panels_panel_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the specified observation panel for the specified person id.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_panels_panel_id(
    person_id="personId",
    panel_id="panelId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose observation panel is to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**panel_id:** `str` — (Required) (Required) The id of the observation panel to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_panels_panel_id_results</a>(...) -> Ok65</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of observation results for the specified person id and observation panel id.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_panels_panel_id_results(
    person_id="personId",
    panel_id="panelId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose observation results are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**panel_id:** `str` — (Required) (Required) The id of the observation panel for whose observation results are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">post_base_url_persons_person_id_chart_lab_panels_panel_id_results</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds observation results for the specified person id and panel id.
</dd>
</dl>
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

client.laboratory.post_base_url_persons_person_id_chart_lab_panels_panel_id_results(
    person_id="personId",
    panel_id="panelId",
    request=[],
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

**person_id:** `str` — (Required) (Required) The id of the person to add observation results for.
    
</dd>
</dl>

<dl>
<dd>

**panel_id:** `str` — (Required) (Required) The id of the observation panel to add results to.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">put_base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the specified observation result for the specifed person id, panel id and sequenceNumber.
</dd>
</dl>
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

client.laboratory.put_base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number(
    person_id="personId",
    panel_id="panelId",
    sequence_number="sequenceNumber",
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

**person_id:** `str` — (Required) (Required) The id of person whose observation result is to be updated.
    
</dd>
</dl>

<dl>
<dd>

**panel_id:** `str` — (Required) (Required) The id of the panel whose observation result is to be updated.
    
</dd>
</dl>

<dl>
<dd>

**sequence_number:** `str` — (Required) (Required) The observation result sequence number that is to be updated.
    
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

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the specified observation result for the specifed person id and panel id.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number(
    person_id="personId",
    panel_id="panelId",
    sequence_number="sequenceNumber",
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

**person_id:** `str` — (Required) (Required) The id of person whose observation result is to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**panel_id:** `str` — (Required) (Required) The id of the panel whose observation result is to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**sequence_number:** `str` — (Required) (Required) The observation result sequence number that is to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.laboratory.<a href="src/fern/laboratory/client.py">base_url_persons_person_id_chart_lab_results</a>(...) -> Ok66</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of observation results for the specified person id after applying additional OData operations.
</dd>
</dl>
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

client.laboratory.base_url_persons_person_id_chart_lab_results(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the person whose observation results are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Medications
<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_charts_medications</a>(...) -> Ok67</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

GETs medications created or modified within a given interval. If an oData filter of createTimestamp or modifyTimestamp is not specified, medications which are created or modified within the last 7 days are retrieved.
</dd>
</dl>
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

client.medications.base_url_persons_charts_medications(
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_person_id_medication_history</a>(...) -> Ok68</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of medication history records for the specified person id.
</dd>
</dl>
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

client.medications.base_url_persons_person_id_medication_history(
    person_id="personId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose medication history is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_person_id_medication_history_create_consent</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates medication history consent for a given person id
</dd>
</dl>
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

client.medications.base_url_persons_person_id_medication_history_create_consent(
    person_id="personId",
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

**person_id:** `str` — (Required) (Required) The id of the person for which medication history consent is being created
    
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

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_person_id_medication_history_create_request</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an medication history request for the given person id
</dd>
</dl>
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

client.medications.base_url_persons_person_id_medication_history_create_request(
    person_id="personId",
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

**person_id:** `str` — (Required) (Required) The id of the person for which medication history is being requested
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_person_id_chart_encounters_encounter_id_medications</a>(...) -> Ok67</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of patient medication for the specified person id and encounter id after applying additional OData query operations.
</dd>
</dl>
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

client.medications.base_url_persons_person_id_chart_encounters_encounter_id_medications(
    person_id="personId",
    encounter_id="encounterId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose medications are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter for which the medications are retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">post_base_url_persons_person_id_chart_encounters_encounter_id_medications</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new medication for the given person id and encounter id
</dd>
</dl>
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

client.medications.post_base_url_persons_person_id_chart_encounters_encounter_id_medications(
    person_id="personId",
    encounter_id="encounterId",
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

**person_id:** `str` — (Required) (Required) The id of the person for which the medication is being added
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter in which the medication is being added
    
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

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">get_base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id</a>(...) -> Ok70</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the patient medication details for the given person id, encounter id and patient medication id.
</dd>
</dl>
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

client.medications.get_base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id(
    person_id="personId",
    encounter_id="encounterId",
    medication_id="medicationId",
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

**person_id:** `str` — (Required) (Required) The id of the patient of whose medication is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter for which the medication is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**medication_id:** `str` — (Required) (Required) The id of the patient medication being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id1</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a patient medication record for the given person id , encounter id and medication id Note: AcknowledgedProblems in prescription request object will be ignored because DUR check is not done while updating a medication. This field should not be set.
</dd>
</dl>
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

client.medications.base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id1(
    person_id="personId",
    encounter_id="encounterId",
    medication_id="medicationId",
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

**person_id:** `str` — (Required) (Required) The id of the person for which the medication is being updated
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter in which the medication is being updated
    
</dd>
</dl>

<dl>
<dd>

**medication_id:** `str` — (Required) (Required) The unique id of the patient medication being updated
    
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

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

deletes a medication for a given person id, encounter id and medication id
</dd>
</dl>
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

client.medications.base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id(
    person_id="personId",
    encounter_id="encounterId",
    medication_id="medicationId",
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

**person_id:** `str` — (Required) (Required) The id of the person for which the medication is being deleted
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter in which the medication is being deleted
    
</dd>
</dl>

<dl>
<dd>

**medication_id:** `str` — (Required) (Required) The id of the patient medication that is being deleted
    
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

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id_renew</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Renews a medication for the given person id, encounter id and medication id
</dd>
</dl>
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

client.medications.base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id_renew(
    person_id="personId",
    encounter_id="encounterId",
    medication_id="medicationId",
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

**person_id:** `str` — (Required) (Required) The id of the person for which the medication is being added
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter in which the medication is being added
    
</dd>
</dl>

<dl>
<dd>

**medication_id:** `str` — (Required) (Required) The id of the patient medication to be renewed
    
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

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_person_id_chart_medications</a>(...) -> Ok67</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of patient medications for the specified person id after applying additional OData query operations.
</dd>
</dl>
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

client.medications.base_url_persons_person_id_chart_medications(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose medications are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_person_id_chart_medications_medication_id</a>(...) -> Ok70</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the patient medication details for the given person id and patient medication id.
</dd>
</dl>
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

client.medications.base_url_persons_person_id_chart_medications_medication_id(
    person_id="personId",
    medication_id="medicationId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose medication is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**medication_id:** `str` — (Required) (Required) The id of the patient medication being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_person_id_chart_medications_medication_id_cancel</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels a medication for the given person id and medication id
</dd>
</dl>
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

client.medications.base_url_persons_person_id_chart_medications_medication_id_cancel(
    person_id="personId",
    medication_id="medicationId",
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

**person_id:** `str` — (Required) (Required) The id of the person for which the medication is being cancelled
    
</dd>
</dl>

<dl>
<dd>

**medication_id:** `str` — (Required) (Required) The id of the patient medication that is being cancelled
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_person_id_chart_medications_medication_id_notes</a>(...) -> Ok73</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of prescription notes for the specified person id and medication id after applying additional OData query operations.
</dd>
</dl>
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

client.medications.base_url_persons_person_id_chart_medications_medication_id_notes(
    person_id="personId",
    medication_id="medicationId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose prescription notes is being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**medication_id:** `str` — (Required) (Required) The id of the patient medication whose prescription notes is being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">post_base_url_persons_person_id_chart_medications_medication_id_notes</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a prescription note for the given person id and medication id.
</dd>
</dl>
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

client.medications.post_base_url_persons_person_id_chart_medications_medication_id_notes(
    person_id="personId",
    medication_id="medicationId",
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

**person_id:** `str` — (Required) (Required) The id of the person for which a prescription note is being added.
    
</dd>
</dl>

<dl>
<dd>

**medication_id:** `str` — (Required) (Required) The id of the patient medication for which a prescription note is being added.
    
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

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_person_id_chart_medications_medication_id_notes_note_id1</a>(...) -> Ok74</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the prescription note for the given person id, patient medication id and note id.
</dd>
</dl>
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

client.medications.base_url_persons_person_id_chart_medications_medication_id_notes_note_id1(
    person_id="personId",
    medication_id="medicationId",
    note_id="noteId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose prescription note is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**medication_id:** `str` — (Required) (Required) The id of the patient medication whose prescription note is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**note_id:** `str` — (Required) (Required) The id of the prescription note being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">put_base_url_persons_person_id_chart_medications_medication_id_notes_note_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the specified prescription note for the person id and medication id.
</dd>
</dl>
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

client.medications.put_base_url_persons_person_id_chart_medications_medication_id_notes_note_id(
    person_id="personId",
    medication_id="medicationId",
    note_id="noteId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose prescription note is to be updated.
    
</dd>
</dl>

<dl>
<dd>

**medication_id:** `str` — (Required) (Required) The id of the medication whose prescription note is to be updated.
    
</dd>
</dl>

<dl>
<dd>

**note_id:** `str` — (Required) (Required) The id of the prescription note to be updated.
    
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

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_person_id_chart_medications_medication_id_notes_note_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the specified prescription note for the person id and medication id.
</dd>
</dl>
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

client.medications.base_url_persons_person_id_chart_medications_medication_id_notes_note_id(
    person_id="personId",
    medication_id="medicationId",
    note_id="noteId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose prescription note is to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**medication_id:** `str` — (Required) (Required) The id of the medication whose prescription note is to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**note_id:** `str` — (Required) (Required) The id of the prescription note to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_person_id_chart_medications_medication_id_send_erx</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits an electronic prescription for the given person id, medication id, and additional details
</dd>
</dl>
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

client.medications.base_url_persons_person_id_chart_medications_medication_id_send_erx(
    person_id="personId",
    medication_id="medicationId",
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

**person_id:** `str` — (Required) (Required) The id of the patient for which the medication is being electronically prescribed
    
</dd>
</dl>

<dl>
<dd>

**medication_id:** `str` — (Required) (Required) The id of the patient medication that is being electronically prescribed
    
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

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_person_id_chart_medications_medication_id_stop</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stops a medication for the given person id and medication id
</dd>
</dl>
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

client.medications.base_url_persons_person_id_chart_medications_medication_id_stop(
    person_id="personId",
    medication_id="medicationId",
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

**person_id:** `str` — (Required) (Required) The id of the person for which the medication is being stopped
    
</dd>
</dl>

<dl>
<dd>

**medication_id:** `str` — (Required) (Required) The id of the patient medication that is being stopped
    
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

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_person_id_chart_medications_medid_dur_check</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Performs a drug utilization review and returns any problems for the given person id and medication id.
</dd>
</dl>
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

client.medications.base_url_persons_person_id_chart_medications_medid_dur_check(
    person_id="personId",
    medid="medid",
    is_representative_ndc="isRepresentativeNdc",
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

**person_id:** `str` — (Required) (Required) The id of the person for which a drug utilization review is being performed
    
</dd>
</dl>

<dl>
<dd>

**medid:** `str` — (Required) (Required) The id of the medication for which a drug utilization review is being performed
    
</dd>
</dl>

<dl>
<dd>

**is_representative_ndc:** `str` — A true or false value that represents whether the medication was prescribed elsewhere and the strength, route, and form were unknown at the time the medication was added
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_person_id_chart_medications_medid_monograph_data</a>(...) -> Ok75</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the monograph data for a medication.
</dd>
</dl>
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

client.medications.base_url_persons_person_id_chart_medications_medid_monograph_data(
    person_id="personId",
    medid="medid",
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

**person_id:** `str` — (Required) (Required) The id of the person for monograph data
    
</dd>
</dl>

<dl>
<dd>

**medid:** `str` — (Required) (Required) The id of the medication for monograph data.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_person_id_chart_medications_medid_patient_education</a>(...) -> Ok76</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the external resources URL and type for patient education.
</dd>
</dl>
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

client.medications.base_url_persons_person_id_chart_medications_medid_patient_education(
    person_id="personId",
    medid="medid",
    resource_type="resourceType",
    encounter_date="encounterDate",
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

**person_id:** `str` — (Required) (Required) The id of the person for whom patient education url is being retreived
    
</dd>
</dl>

<dl>
<dd>

**medid:** `str` — (Required) (Required) The id of the medication for patient education
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` — (Required) Patient education Resource Type - resourceType - 1 (ExternalPatientEducation) or 2 - (ClinicalDecisionSupport) or 3 - (ExternalProviderReferences)
    
</dd>
</dl>

<dl>
<dd>

**encounter_date:** `str` — Encounter Date on which patient education data is being retreived
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.medications.<a href="src/fern/medications/client.py">base_url_persons_person_id_chart_medications_pdmp_report</a>(...) -> Ok67</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get PDMP report for a person.
</dd>
</dl>
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

client.medications.base_url_persons_person_id_chart_medications_pdmp_report(
    person_id="personId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose medications are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Patient Demographics
<details><summary><code>client.patient_demographics.<a href="src/fern/patient_demographics/client.py">base_url_persons</a>(...) -> Ok78</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of persons/patients. If OData $filter criteria for createTimestamp and/or /modifyTimestamp are not specified, the default behavior of this route is to return results for persons/patients that have been created or modified in the last 7 days.
</dd>
</dl>
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

client.patient_demographics.base_url_persons(
    patients_only="patientsOnly",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**patients_only:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_demographics.<a href="src/fern/patient_demographics/client.py">post_base_url_persons</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new person
</dd>
</dl>
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

client.patient_demographics.post_base_url_persons(
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

<details><summary><code>client.patient_demographics.<a href="src/fern/patient_demographics/client.py">base_url_persons_person_id</a>(...) -> Ok79</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the demographics for the specified person id.
</dd>
</dl>
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

client.patient_demographics.base_url_persons_person_id(
    person_id="personId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose demographics are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_demographics.<a href="src/fern/patient_demographics/client.py">base_url_persons_person_id1</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a person's demographic information
</dd>
</dl>
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

client.patient_demographics.base_url_persons_person_id1(
    person_id="personId",
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

**person_id:** `str` — (Required) (Required) The id for the person being updated
    
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

<details><summary><code>client.patient_demographics.<a href="src/fern/patient_demographics/client.py">patch_base_url_persons_person_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates properties on existing person demographics given in the request.
</dd>
</dl>
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

client.patient_demographics.patch_base_url_persons_person_id(
    person_id="personId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose demographics are being updated.
    
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

<details><summary><code>client.patient_demographics.<a href="src/fern/patient_demographics/client.py">base_url_persons_person_id_address_histories</a>(...) -> Ok79</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the address histories for the specified personId.
</dd>
</dl>
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

client.patient_demographics.base_url_persons_person_id_address_histories(
    person_id="personId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose demographics are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_demographics.<a href="src/fern/patient_demographics/client.py">base_url_persons_person_id_ethnicities</a>(...) -> Ok81</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the ethnicities for the specified person id.
</dd>
</dl>
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

client.patient_demographics.base_url_persons_person_id_ethnicities(
    person_id="personId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose ethnicities are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_demographics.<a href="src/fern/patient_demographics/client.py">base_url_persons_person_id_gender_identities</a>(...) -> Ok81</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the gender identities for the specified person id.
</dd>
</dl>
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

client.patient_demographics.base_url_persons_person_id_gender_identities(
    person_id="personId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose ethnicities are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_demographics.<a href="src/fern/patient_demographics/client.py">base_url_persons_person_id_races</a>(...) -> Ok83</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the races for the specified person id.
</dd>
</dl>
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

client.patient_demographics.base_url_persons_person_id_races(
    person_id="personId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose races are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_demographics.<a href="src/fern/patient_demographics/client.py">base_url_persons_lookup</a>(...) -> Ok84</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of persons/patients based on various search criteria.  Since these results are returned from a /persons/ endpoint, the "id" of each result (whose value is a guid) is a personId and can be used as the value of personId in all other routes that require a personId.

Using the /persons/lookup route:

-At least one query parameter must be provided as lookup criteria.
-Use of multiple criteria is allowed, and will results will include person records matching all criteria.
-The two "quickSearch" parameters are exceptions to the above; see the quickSearchId & quickSearchInput parameter descriptions for details.
</dd>
</dl>
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

client.patient_demographics.base_url_persons_lookup(
    name="name",
    first_name="firstName",
    last_name="lastName",
    middle_name="middleName",
    prior_last_name="priorLastName",
    address_line1="addressLine1",
    city="city",
    zip="zip",
    sex="sex",
    current_gender="currentGender",
    date_of_birth="dateOfBirth",
    external_id="externalId",
    external_system_id="externalSystemId",
    exclude_expired="excludeExpired",
    is_next_md_enabled="isNextMdEnabled",
    search_patients_only="searchPatientsOnly",
    quick_search_id="quickSearchId",
    quick_search_input="quickSearchInput",
    expand="$expand",
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

**first_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**prior_last_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**address_line1:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**city:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**zip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sex:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**current_gender:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**date_of_birth:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**external_system_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**exclude_expired:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**is_next_md_enabled:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**search_patients_only:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**quick_search_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**quick_search_input:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expand:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patient_demographics.<a href="src/fern/patient_demographics/client.py">base_url_persons_person_id_chart_encounters</a>(...) -> Ok78</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

While this route does not directly return USCDI data, knowledge of an encounterId is sometimes necessary to utilize other routes to obtain USCDI data.

This route returns a list of encounters (each identified by "id", which in all other routes will be an {encounterId} whose value is a guid) for the specified person id after applying additional OData query operations.
</dd>
</dl>
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

client.patient_demographics.base_url_persons_person_id_chart_encounters(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose encounters are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Problems
<details><summary><code>client.problems.<a href="src/fern/problems/client.py">base_url_persons_person_id_chart_problems</a>(...) -> Ok86</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of patient problems after performing additional OData query operations.
</dd>
</dl>
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

client.problems.base_url_persons_person_id_chart_problems(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the person for which the problems are being displayed
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.problems.<a href="src/fern/problems/client.py">post_base_url_persons_person_id_chart_problems</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new problem for the given person id
</dd>
</dl>
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

client.problems.post_base_url_persons_person_id_chart_problems(
    person_id="personId",
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

**person_id:** `str` — (Required) (Required) The id of the person for which the problem is being added
    
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

<details><summary><code>client.problems.<a href="src/fern/problems/client.py">base_url_persons_person_id_chart_problems_problem_id1</a>(...) -> Ok87</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the details of a patient problem.
</dd>
</dl>
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

client.problems.base_url_persons_person_id_chart_problems_problem_id1(
    person_id="personId",
    problem_id="problemId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose problem is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**problem_id:** `str` — (Required) (Required) The id of the problem
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.problems.<a href="src/fern/problems/client.py">put_base_url_persons_person_id_chart_problems_problem_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a patient problem
</dd>
</dl>
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

client.problems.put_base_url_persons_person_id_chart_problems_problem_id(
    person_id="personId",
    problem_id="problemId",
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

**person_id:** `str` — (Required) (Required) The id of the person for which the problem is being modified
    
</dd>
</dl>

<dl>
<dd>

**problem_id:** `str` — (Required) (Required) The id of the problem being modified
    
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

<details><summary><code>client.problems.<a href="src/fern/problems/client.py">base_url_persons_person_id_chart_problems_problem_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a patient problem
</dd>
</dl>
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

client.problems.base_url_persons_person_id_chart_problems_problem_id(
    person_id="personId",
    problem_id="problemId",
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

**person_id:** `str` — (Required) (Required) The id of the person for which the problem is being removed
    
</dd>
</dl>

<dl>
<dd>

**problem_id:** `str` — (Required) (Required) The id of the problem being removed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.problems.<a href="src/fern/problems/client.py">base_url_persons_person_id_chart_problems_problem_id_interactions</a>(...) -> typing.List[Ok37]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets patient interactions for an existing problems after adding the problem so that user will be aware of the contraindications while updating them.
</dd>
</dl>
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

client.problems.base_url_persons_person_id_chart_problems_problem_id_interactions(
    person_id="personId",
    problem_id="problemId",
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

**person_id:** `str` — (Required) (Required) The id of the person whose interactions are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**problem_id:** `str` — (Required) (Required) The id of the problem for which interactions are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.problems.<a href="src/fern/problems/client.py">base_url_persons_person_id_chart_problems_problem_id_notes</a>(...) -> Ok89</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of notes attached to a patient problem after performing additional OData query operations.
</dd>
</dl>
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

client.problems.base_url_persons_person_id_chart_problems_problem_id_notes(
    person_id="personId",
    problem_id="problemId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the person for which the problem notes are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**problem_id:** `str` — (Required) (Required) The id of the problem for which the notes are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.problems.<a href="src/fern/problems/client.py">post_base_url_persons_person_id_chart_problems_problem_id_notes</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a note to a patient problem
</dd>
</dl>
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

client.problems.post_base_url_persons_person_id_chart_problems_problem_id_notes(
    person_id="personId",
    problem_id="problemId",
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

**person_id:** `str` — (Required) (Required) The id of the person for which we are adding the problem note
    
</dd>
</dl>

<dl>
<dd>

**problem_id:** `str` — (Required) (Required) The id of the problem that the note is being added to
    
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

<details><summary><code>client.problems.<a href="src/fern/problems/client.py">base_url_persons_person_id_chart_problems_problem_id_notes_note_id1</a>(...) -> Ok90</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a problem note.
</dd>
</dl>
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

client.problems.base_url_persons_person_id_chart_problems_problem_id_notes_note_id1(
    person_id="personId",
    problem_id="problemId",
    note_id="noteId",
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

**person_id:** `str` — (Required) (Required) The id of the person for which the note is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**problem_id:** `str` — (Required) (Required) The id of the problem that the note is associated with
    
</dd>
</dl>

<dl>
<dd>

**note_id:** `str` — (Required) (Required) The id of the note
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.problems.<a href="src/fern/problems/client.py">put_base_url_persons_person_id_chart_problems_problem_id_notes_note_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a problem note
</dd>
</dl>
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

client.problems.put_base_url_persons_person_id_chart_problems_problem_id_notes_note_id(
    person_id="personId",
    problem_id="problemId",
    note_id="noteId",
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

**person_id:** `str` — (Required) (Required) The id of the person for which the note is being updated
    
</dd>
</dl>

<dl>
<dd>

**problem_id:** `str` — (Required) (Required) The id of the problem that the note is associated with
    
</dd>
</dl>

<dl>
<dd>

**note_id:** `str` — (Required) (Required) The id of the note
    
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

<details><summary><code>client.problems.<a href="src/fern/problems/client.py">base_url_persons_person_id_chart_problems_problem_id_notes_note_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a problem note
</dd>
</dl>
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

client.problems.base_url_persons_person_id_chart_problems_problem_id_notes_note_id(
    person_id="personId",
    problem_id="problemId",
    note_id="noteId",
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

**person_id:** `str` — (Required) (Required) The id of the person for which the note is being deleted
    
</dd>
</dl>

<dl>
<dd>

**problem_id:** `str` — (Required) (Required) The id of the problem that the note is associated with
    
</dd>
</dl>

<dl>
<dd>

**note_id:** `str` — (Required) (Required) The id of the note
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.problems.<a href="src/fern/problems/client.py">base_url_persons_person_id_chart_problems_interactions</a>(...) -> typing.List[Ok37]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This route is meant to be used in conjunction with the POST for Patient Problem. The results of this route will be required by the POST for verification that interactions were viewed.
</dd>
</dl>
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

client.problems.base_url_persons_person_id_chart_problems_interactions(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the person whose interactions are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Procedures
<details><summary><code>client.procedures.<a href="src/fern/procedures/client.py">base_url_persons_person_id_chart_procedures</a>(...) -> Ok92</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a patient's procedures summary.
</dd>
</dl>
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

client.procedures.base_url_persons_person_id_chart_procedures(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose procedures summary is being fetched
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.procedures.<a href="src/fern/procedures/client.py">base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id</a>(...) -> Ok93</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a specific patient procedure.
</dd>
</dl>
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

client.procedures.base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id(
    person_id="personId",
    encounter_id="encounterId",
    procedure_id="procedureId",
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

**person_id:** `str` — (Required) (Required) The id of the patient
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of patient's encounter
    
</dd>
</dl>

<dl>
<dd>

**procedure_id:** `str` — (Required) (Required) The id of patient's procedure
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.procedures.<a href="src/fern/procedures/client.py">put_base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a patient procedure
</dd>
</dl>
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

client.procedures.put_base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id(
    person_id="personId",
    encounter_id="encounterId",
    procedure_id="procedureId",
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

**person_id:** `str` — (Required) (Required) The id of the patient
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of patient's encounter
    
</dd>
</dl>

<dl>
<dd>

**procedure_id:** `str` — (Required) (Required) The id of patient's procedure
    
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

<details><summary><code>client.procedures.<a href="src/fern/procedures/client.py">base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id1</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a patient procedure
</dd>
</dl>
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

client.procedures.base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id1(
    person_id="personId",
    encounter_id="encounterId",
    procedure_id="procedureId",
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

**person_id:** `str` — (Required) (Required) The id of the patient
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of patient's encounter
    
</dd>
</dl>

<dl>
<dd>

**procedure_id:** `str` — (Required) (Required) The id of patient's procedure
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.procedures.<a href="src/fern/procedures/client.py">base_url_persons_person_id_chart_encounters_encounter_id_procedures</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a procedure to patient's encounter
</dd>
</dl>
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

client.procedures.base_url_persons_person_id_chart_encounters_encounter_id_procedures(
    person_id="personId",
    encounter_id="encounterId",
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

**person_id:** `str` — (Required) (Required) The id of the patient
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the patient's encounter
    
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

## Smoking Status
<details><summary><code>client.smoking_status.<a href="src/fern/smoking_status/client.py">base_url_persons_person_id_chart_health_concerns_tobacco_smoking_usage_status</a>(...) -> Ok94</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a patient's tobacco uses status for health concern.
</dd>
</dl>
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

client.smoking_status.base_url_persons_person_id_chart_health_concerns_tobacco_smoking_usage_status(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose health concerns tobacco uses status are being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.smoking_status.<a href="src/fern/smoking_status/client.py">base_url_persons_person_id_chart_social_history</a>(...) -> Ok95</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of social history for the given person id after applying additional OData query operations.
</dd>
</dl>
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

client.smoking_status.base_url_persons_person_id_chart_social_history(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose social history is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.smoking_status.<a href="src/fern/smoking_status/client.py">base_url_persons_person_id_chart_tobacco_usage</a>(...) -> Ok96</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of tobacco usage for the given person id after applying additional OData query operations.
</dd>
</dl>
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

client.smoking_status.base_url_persons_person_id_chart_tobacco_usage(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose tobacco usage is being retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Vital Signs
<details><summary><code>client.vital_signs.<a href="src/fern/vital_signs/client.py">base_url_persons_person_id_chart_vitals</a>(...) -> Ok97</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of vital sign summaries for the given person id after applying additional OData query operations.
</dd>
</dl>
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

client.vital_signs.base_url_persons_person_id_chart_vitals(
    person_id="personId",
    top="$top",
    filter="$filter",
    orderby="$orderby",
    skip="$skip",
    inlinecount="$inlinecount",
    count="$count",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose vital signs are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**top:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**orderby:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**inlinecount:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**count:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vital_signs.<a href="src/fern/vital_signs/client.py">base_url_persons_person_id_chart_encounters_encounter_id_vitals_vitals_id</a>(...) -> Ok98</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the vital sign details for the given person id, encounter id, and vital signs id.
</dd>
</dl>
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

client.vital_signs.base_url_persons_person_id_chart_encounters_encounter_id_vitals_vitals_id(
    person_id="personId",
    encounter_id="encounterId",
    vitals_id="vitalsId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose vital signs are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter in which the vital signs were taken
    
</dd>
</dl>

<dl>
<dd>

**vitals_id:** `str` — (Required) (Required) The id of the vital signs that are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vital_signs.<a href="src/fern/vital_signs/client.py">put_base_url_persons_person_id_chart_encounters_encounter_id_vitals_vitals_id</a>(...) -> Ok98</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates Vital Signs for the given person id, encounter id and vital signs Id.
</dd>
</dl>
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

client.vital_signs.put_base_url_persons_person_id_chart_encounters_encounter_id_vitals_vitals_id(
    person_id="personId",
    encounter_id="encounterId",
    vitals_id="vitalsId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose vital signs are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter in which the vital signs were taken
    
</dd>
</dl>

<dl>
<dd>

**vitals_id:** `str` — (Required) (Required) The id of the vital signs that are being retrieved
    
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

<details><summary><code>client.vital_signs.<a href="src/fern/vital_signs/client.py">base_url_persons_person_id_chart_encounters_encounter_id_vitals</a>(...) -> Ok98</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates Vital Signs for the given person id, encounter id and vital signs Id.
</dd>
</dl>
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

client.vital_signs.base_url_persons_person_id_chart_encounters_encounter_id_vitals(
    person_id="personId",
    encounter_id="encounterId",
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

**person_id:** `str` — (Required) (Required) The id of the patient whose vital signs are being retrieved
    
</dd>
</dl>

<dl>
<dd>

**encounter_id:** `str` — (Required) (Required) The id of the encounter in which the vital signs were taken
    
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

