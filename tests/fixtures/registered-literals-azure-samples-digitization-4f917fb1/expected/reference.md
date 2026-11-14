# Reference
<details><summary><code>client.<a href="src/fern/client.py#L102-L126">metrics_get</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Endpoint that serves Prometheus metrics.
</dd>
</dl>
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
    base_url="https://yourhost.com/path/to/api",
)

client.metrics_get()

```
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

## PidDigitization
<details><summary><code>client.pid_digitization.<a href="src/fern/pid_digitization/client.py#L41-L90">detect_symbols</a>(...) -> SymbolDetectionInferenceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detects symbols in an image and returns the bounding boxes of the detected symbols.

param pid: The PID.
param bounding_box_inclusive_str: The bounding box of the P&ID image without extraneous legend information.
param file: The image to detect symbols in.
return: The bounding boxes of the detected symbols.
rtype: symbol_detection.ObjectDetectionPrediction
</dd>
</dl>
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
    base_url="https://yourhost.com/path/to/api",
)

client.pid_digitization.detect_symbols(
    pid_id="pid_id",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` — The P&ID image to detect symbols in.
    
</dd>
</dl>

<dl>
<dd>

**bounding_box_inclusive_str:** `typing.Optional[typing.Any]` — The bounding box of the P&ID image without extraneous legend information.This should be provided as a JSON string with the following format: {"topX": 0.0, "topY": 0.0, "bottomX": 1.0, "bottomY": 1.0}.  The coordinates should be normalized to the range [0, 1]. The default value is the entire image.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pid_digitization.<a href="src/fern/pid_digitization/client.py#L92-L165">detect_text</a>(...) -> TextDetectionInferenceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint takes in the P&ID image id to download the original image and recognize the texts of the image.
Additionally, it takes in the corrected symbol detected inference results which will be stored and used to
associate a text with a symbol.

Returns the text detection inference results, which includes all text detected and
the text and symbols associated on a P&ID image.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ImageDetails, Label

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.pid_digitization.detect_text(
    pid_id="pid_id",
    image_url="image_url",
    image_details=ImageDetails(
        width=1,
        height=1,
    ),
    label=[
        Label(
            top_x=1.1,
            top_y=1.1,
            bottom_x=1.1,
            bottom_y=1.1,
            id=1,
            label="label",
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

**pid_id:** `str` — The P&ID image id
    
</dd>
</dl>

<dl>
<dd>

**request:** `SymbolDetectionInferenceResponse` — The corrected symbol detection                                                                                 inference results
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pid_digitization.<a href="src/fern/pid_digitization/client.py#L167-L273">detect_lines_and_construct_graph</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint takes in the P&ID image id and the text response and then will build an asset connected
graph based on the line segments, text detection results and symbol associations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ImageDetails, TextRecognized, SymbolAndTextAssociated

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.pid_digitization.detect_lines_and_construct_graph(
    pid_id="pid_id",
    image_url="image_url",
    image_details=ImageDetails(
        width=1,
        height=1,
    ),
    all_text_list=[
        TextRecognized(
            top_x=1.1,
            top_y=1.1,
            bottom_x=1.1,
            bottom_y=1.1,
            text="text",
        )
    ],
    text_and_symbols_associated_list=[
        SymbolAndTextAssociated(
            top_x=1.1,
            top_y=1.1,
            bottom_x=1.1,
            bottom_y=1.1,
            id=1,
            label="label",
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

**pid_id:** `str` — The P&ID image id
    
</dd>
</dl>

<dl>
<dd>

**image_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**image_details:** `ImageDetails` 
    
</dd>
</dl>

<dl>
<dd>

**all_text_list:** `typing.List[TextRecognized]` 
    
</dd>
</dl>

<dl>
<dd>

**text_and_symbols_associated_list:** `typing.List[SymbolAndTextAssociated]` 
    
</dd>
</dl>

<dl>
<dd>

**bounding_box_inclusive:** `typing.Optional[BoundingBox]` 
    
</dd>
</dl>

<dl>
<dd>

**hough_threshold:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**hough_min_line_length:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**hough_max_line_gap:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**hough_rho:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**hough_theta:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**thinning_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pid_digitization.<a href="src/fern/pid_digitization/client.py#L275-L371">persist_graph</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

For the given P&ID image id, the graph output (if any) from the prior step is persisted in the graph database.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ImageDetails, ConnectedSymbolsItem, BoundingBox, ConnectedSymbolsConnectionItem, FlowDirection

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.pid_digitization.persist_graph(
    pid_id="pid_id",
    image_url="image_url",
    image_details=ImageDetails(
        width=1,
        height=1,
    ),
    connected_symbols=[
        ConnectedSymbolsItem(
            id=1,
            label="label",
            text_associated="text_associated",
            bounding_box=BoundingBox(
                top_x=1.1,
                top_y=1.1,
                bottom_x=1.1,
                bottom_y=1.1,
            ),
            connections=[
                ConnectedSymbolsConnectionItem(
                    id=1,
                    label="label",
                    text_associated="text_associated",
                    bounding_box=BoundingBox(
                        top_x=1.1,
                        top_y=1.1,
                        bottom_x=1.1,
                        bottom_y=1.1,
                    ),
                    flow_direction=FlowDirection.UNKNOWN,
                    segments=[
                        BoundingBox(
                            top_x=1.1,
                            top_y=1.1,
                            bottom_x=1.1,
                            bottom_y=1.1,
                        )
                    ],
                )
            ],
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

**pid_id:** `str` — The P&ID image id
    
</dd>
</dl>

<dl>
<dd>

**request:** `GraphConstructionInferenceResponse` — Persist the final graph                                                                                 into the graph database
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pid_digitization.<a href="src/fern/pid_digitization/client.py#L373-L417">get_inference_results</a>(...) -> GetInferenceResultsApiPidDigitizationInferenceResultTypePidIdGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the inference results for a given pid id and inference result type.

param pid: The PID id.
param inference_result_type: The inference result type.
return: The inference results.
rtype: symbol_detection.InferenceResponse
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, InferenceResult

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.pid_digitization.get_inference_results(
    inference_result_type=InferenceResult.SYMBOL_DETECTION,
    pid_id="pid_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inference_result_type:** `InferenceResult` 
    
</dd>
</dl>

<dl>
<dd>

**pid_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pid_digitization.<a href="src/fern/pid_digitization/client.py#L419-L450">get_job_status</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the inference job status for a given pid id .
param pid: The PID id.
return: The JobStatus of pid_id.
rtype: JobStatus
</dd>
</dl>
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
    base_url="https://yourhost.com/path/to/api",
)

client.pid_digitization.get_job_status(
    pid_id="pid_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pid_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pid_digitization.<a href="src/fern/pid_digitization/client.py#L452-L496">get_output_inference_images</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the inference output image for a given pid id and inference result type.
param pid: The PID id.
param inference_result_type: The inference result type.
rtype: ImageResponse
The inference output image has information overlayed on the original image
that provides user insight into what was done in the inferencing service.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, InferenceResult

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.pid_digitization.get_output_inference_images(
    inference_result_type=InferenceResult.SYMBOL_DETECTION,
    pid_id="pid_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inference_result_type:** `InferenceResult` 
    
</dd>
</dl>

<dl>
<dd>

**pid_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

