# Reference
## Files
<details><summary><code>client.files.<a href="src/fern/files/client.py">list</a>(...) -> FileList</code></summary>
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

client.files.list(
    api_version="api-version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_version:** `str` — The requested API version.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">upload</a>(...) -> File</code></summary>
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

client.files.upload(
    api_version="api-version",
    file="example_file",
    purpose="fine-tune",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_version:** `str` — The requested API version.
    
</dd>
</dl>

<dl>
<dd>

**purpose:** `FilesUploadRequestPurpose` — The intended purpose of the uploaded documents. Use "fine-tune" for fine-tuning. This allows us to validate the format of the uploaded file.
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` — Gets or sets the file to upload into Azure OpenAI.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">get</a>(...) -> File</code></summary>
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

client.files.get(
    file_id="file-id",
    api_version="api-version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — The identifier of the file.
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The requested API version.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">delete</a>(...)</code></summary>
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

client.files.delete(
    file_id="file-id",
    api_version="api-version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — The identifier of the file.
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The requested API version.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">getcontent</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.files.getcontent(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — The identifier of the file.
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The requested API version.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/fern/files/client.py">import</a>(...) -> File</code></summary>
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

client.files.import_(
    api_version="api-version",
    purpose="fine-tune",
    filename="filename",
    content_url="content_url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_version:** `str` — The requested API version.
    
</dd>
</dl>

<dl>
<dd>

**purpose:** `Purpose` 
    
</dd>
</dl>

<dl>
<dd>

**filename:** `str` 

The name of the [JSON Lines](https://jsonlines.readthedocs.io/en/latest/) file to be uploaded.
If the `purpose` is set to "fine-tune", each line is a JSON record with "prompt" and "completion" fields representing your training examples.
    
</dd>
</dl>

<dl>
<dd>

**content_url:** `str` — The url to download the document from (can be SAS url of a blob or any other external url accessible with a GET request).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## FineTunes
<details><summary><code>client.fine_tunes.<a href="src/fern/fine_tunes/client.py">fine_tunes_list</a>(...) -> FineTuneList</code></summary>
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

client.fine_tunes.fine_tunes_list(
    api_version="api-version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_version:** `str` — The requested API version.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fine_tunes.<a href="src/fern/fine_tunes/client.py">fine_tunes_create</a>(...) -> FineTune</code></summary>
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

client.fine_tunes.fine_tunes_create(
    api_version="api-version",
    model="model",
    training_file="training_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_version:** `str` — The requested API version.
    
</dd>
</dl>

<dl>
<dd>

**model:** `str` — The identifier (model-id) of the base model used for this fine-tune.
    
</dd>
</dl>

<dl>
<dd>

**training_file:** `str` — The file identity (file-id) that is used for training this fine tuned model.
    
</dd>
</dl>

<dl>
<dd>

**validation_file:** `typing.Optional[str]` — The file identity (file-id) that is used to evaluate the fine tuned model during training.
    
</dd>
</dl>

<dl>
<dd>

**suffix:** `typing.Optional[str]` — The suffix used to identify the fine-tuned model. The suffix can contain up to 40 characters (a-z, A-Z, 0-9,- and _) that will be added to your fine-tuned model name.
    
</dd>
</dl>

<dl>
<dd>

**n_epochs:** `typing.Optional[int]` — The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.
    
</dd>
</dl>

<dl>
<dd>

**batch_size:** `typing.Optional[int]` 

The batch size to use for training. The batch size is the number of training examples used to train a single forward and backward pass.
In general, we've found that larger batch sizes tend to work better for larger datasets.
The default value as well as the maximum value for this property are specific to a base model.
    
</dd>
</dl>

<dl>
<dd>

**learning_rate_multiplier:** `typing.Optional[float]` 

The learning rate multiplier to use for training. The fine-tuning learning rate is the original learning rate used for pre-training multiplied by this value.
Larger learning rates tend to perform better with larger batch sizes.
We recommend experimenting with values in the range 0.02 to 0.2 to see what produces the best results.
    
</dd>
</dl>

<dl>
<dd>

**prompt_loss_weight:** `typing.Optional[float]` 

The weight to use for loss on the prompt tokens. This controls how much the model tries to learn to generate the prompt
(as compared to the completion which always has a weight of 1.0), and can add a stabilizing effect to training when completions are short.
If prompts are extremely long (relative to completions), it may make sense to reduce this weight so as to avoid over-prioritizing learning the prompt.
    
</dd>
</dl>

<dl>
<dd>

**compute_classification_metrics:** `typing.Optional[bool]` 

A value indicating whether to compute classification metrics.
If set, we calculate classification-specific metrics such as accuracy and F-1 score using the validation set at the end of every epoch.
These metrics can be viewed in the results file. In order to compute classification metrics, you must provide a validation_file.Additionally,
you must specify classification_n_classes for multiclass classification or classification_positive_class for binary classification.
    
</dd>
</dl>

<dl>
<dd>

**classification_n_classes:** `typing.Optional[int]` 

The number of classes in a classification task.
This parameter is required for multiclass classification.
    
</dd>
</dl>

<dl>
<dd>

**classification_positive_class:** `typing.Optional[str]` 

The positive class in binary classification.
This parameter is needed to generate precision, recall, and F1 metrics when doing binary classification.
    
</dd>
</dl>

<dl>
<dd>

**classification_betas:** `typing.Optional[typing.List[float]]` 

The classification beta values. If this is provided, we calculate F-beta scores at the specified beta values.
The F-beta score is a generalization of F-1 score. This is only used for binary classification.
With a beta of 1 (i.e.the F-1 score), precision and recall are given the same weight.
A larger beta score puts more weight on recall and less on precision. A smaller beta score puts more weight on precision and less on recall.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fine_tunes.<a href="src/fern/fine_tunes/client.py">fine_tunes_get</a>(...) -> FineTune</code></summary>
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

client.fine_tunes.fine_tunes_get(
    fine_tune_id="fine-tune-id",
    api_version="api-version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fine_tune_id:** `str` — The identifier of the fine-tune job.
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The requested API version.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fine_tunes.<a href="src/fern/fine_tunes/client.py">fine_tunes_delete</a>(...)</code></summary>
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

client.fine_tunes.fine_tunes_delete(
    fine_tune_id="fine-tune-id",
    api_version="api-version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fine_tune_id:** `str` — The identifier of the fine-tune job.
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The requested API version.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fine_tunes.<a href="src/fern/fine_tunes/client.py">fine_tunes_get_events</a>(...) -> EventList</code></summary>
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

client.fine_tunes.fine_tunes_get_events(
    fine_tune_id="fine-tune-id",
    api_version="api-version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fine_tune_id:** `str` — The identifier of the fine-tune job.
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The requested API version.
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[bool]` 

A flag indicating whether to stream events for the fine-tune job. If set to true,
events will be sent as data-only server-sent events as they become available. The stream will terminate with
   a data: [DONE] message when the job is finished (succeeded, cancelled, or failed). 
If set to false, only events generated so far will be returned..
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fine_tunes.<a href="src/fern/fine_tunes/client.py">fine_tunes_cancel</a>(...) -> FineTune</code></summary>
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

client.fine_tunes.fine_tunes_cancel(
    fine_tune_id="fine-tune-id",
    api_version="api-version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fine_tune_id:** `str` — The identifier of the fine-tune job.
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The requested API version.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Models
<details><summary><code>client.models.<a href="src/fern/models/client.py">list</a>(...) -> ModelList</code></summary>
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

client.models.list(
    api_version="api-version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_version:** `str` — The requested API version.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/fern/models/client.py">get</a>(...) -> Model</code></summary>
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

client.models.get(
    model_id="model-id",
    api_version="api-version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model_id:** `str` — The identifier of the model.
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `str` — The requested API version.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

