# Reference
## General
<details><summary><code>client.general.<a href="src/fern/general/client.py">service_status</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul><li>Return the seismic store service status.</li><li>Required roles: none</li></ul>
</dd>
</dl>
</dd>
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

client.general.service_status()

```
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

<details><summary><code>client.general.<a href="src/fern/general/client.py">service_status_check</a>() -> Status</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul><li>Validates if the token audience is allowed</li><li>Required roles: none</li></ul>
</dd>
</dl>
</dd>
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

client.general.service_status_check()

```
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

## Dataset
<details><summary><code>client.dataset.<a href="src/fern/dataset/client.py">get</a>(...) -> Dataset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul> <li>Return the dataset metadata from seismic store.</li> <li>Required roles: <ul> <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li> <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li> </ul> </li></ul>
</dd>
</dl>
</dd>
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

client.dataset.get(
    tenantid="tenantid",
    subprojectid="subprojectid",
    datasetid="datasetid",
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenantid:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**subprojectid:** `str` — Name of the subproject.
    
</dd>
</dl>

<dl>
<dd>

**datasetid:** `str` — Name of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Hierarchical path of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**seismicmeta:** `typing.Optional[bool]` — Include the seismic storage metadata record if it exists.
    
</dd>
</dl>

<dl>
<dd>

**translate_user_info:** `typing.Optional[bool]` — translate the user-id to a more human readable user info
    
</dd>
</dl>

<dl>
<dd>

**record_version:** `typing.Optional[str]` — Retrieve a specific version of the seismic storage metadata record
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset.<a href="src/fern/dataset/client.py">register</a>(...) -> Dataset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul><li>Register a new dataset in the seismic store.</li><li>Required roles: subproject.admin</li></ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.dataset import DatasetRegisterBodySeismicmeta, DatasetRegisterBodyOpenzgyV1, DatasetRegisterBodyOpenzgyV1Acl, DatasetRegisterBodyOpenzgyV1Legal, DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureId, DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureIdKind, DatasetRegisterBodyOpenzgyV1Data, DatasetRegisterBodyOpenzgyV1DataEndian, DatasetRegisterBodyOpenzgyV1DataDatasetProperties, DatasetRegisterBodyOpenzgyV1DataDatasetPropertiesFileSourceInfosItem, DatasetRegisterBodySegyV1, DatasetRegisterBodySegyV1Acl, DatasetRegisterBodySegyV1Legal, DatasetRegisterBodySegyV1Ancestry, DatasetRegisterBodySegyV1MetaItemUnitOfMeasureId, DatasetRegisterBodySegyV1MetaItemUnitOfMeasureIdKind, DatasetRegisterBodySegyV1Data, DatasetRegisterBodySegyV1DataEndian, DatasetRegisterBodySegyV1DataDatasetProperties, DatasetRegisterBodySegyV1DataDatasetPropertiesFileSourceInfosItem, DatasetRegisterBodySegyV1DataVectorHeaderMappingItem, DatasetRegisterBodySegyV1DataVectorHeaderMappingItemScalarIndicator, DatasetRegisterBodyAcls
import datetime

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.dataset.register(
    tenantid="tenantid",
    subprojectid="subprojectid",
    datasetid="datasetid",
    path="path",
    gtags=[
        "tagA",
        "tagB",
        "tagC"
    ],
    seismicmeta=DatasetRegisterBodySeismicmeta(
        kind="osdu:sdms:seismic3d:1.0.0",
    ),
    openzgy_v1=DatasetRegisterBodyOpenzgyV1(
        id="opendes:dataset--FileCollection.Slb.OpenZGY:5771c352-dc52-5d26-9351-2b8dbc9eb474",
        kind="osdu:wks:dataset--FileCollection.Slb.OpenZGY:1.0.0",
        version=1637208623527796,
        acl=DatasetRegisterBodyOpenzgyV1Acl(
            owners=[
                "data.default.viewers@opendes.enterprisedata.cloud.slb-ds.com"
            ],
            viewers=[
                "data.default.viewers@opendes.enterprisedata.cloud.slb-ds.com"
            ],
        ),
        legal=DatasetRegisterBodyOpenzgyV1Legal(
            legaltags=[
                "opendes-seistore-test-01"
            ],
            other_relevant_data_countries=[
                "US"
            ],
            status="compliant",
        ),
        tags={
            "NameOfKey": "String value"
        },
        create_time=datetime.datetime.fromisoformat("2021-11-16T02:08:16+00:00"),
        create_user="vmanohar@slb.com",
        modify_time=datetime.datetime.fromisoformat("2021-11-18T04:10:23+00:00"),
        modify_user="39916b94-71a9-409e-856e-0f29558fa908",
        meta=[
            DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureId(
                kind=DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureIdKind.UNIT,
                persistable_reference="{\"abcd\":{\"a\":0.0,\"b\":1200.0,\"c\":3937.0,\"d\":0.0},\"symbol\":\"ft[US]\",\"baseMeasurement\":{\"ancestry\":\"L\",\"type\":\"UM\"},\"type\":\"UAD\"}",
            )
        ],
        data=DatasetRegisterBodyOpenzgyV1Data(
            resource_home_region_id="opendes:reference-data--OSDURegion:AWSEastUSA:",
            resource_host_region_i_ds=[
                "opendes:reference-data--OSDURegion:AWSEastUSA:"
            ],
            resource_curation_status="opendes:reference-data--ResourceCurationStatus:CREATED:",
            resource_lifecycle_status="opendes:reference-data--ResourceLifecycleStatus:LOADING:",
            resource_security_classification="opendes:reference-data--ResourceSecurityClassification:RESTRICTED:",
            source="Example Data Source",
            existence_kind="opendes:reference-data--ExistenceKind:Prototype:",
            name="Dataset X221/15",
            description="As originally delivered by ACME.com.",
            total_size="13245217273",
            encoding_format_type_id="opendes:reference-data--EncodingFormatType:text%2Fcsv:",
            schema_format_type_id="opendes:reference-data--SchemaFormatType:CWLS%20LAS3:",
            endian=DatasetRegisterBodyOpenzgyV1DataEndian.BIG,
            dataset_properties=DatasetRegisterBodyOpenzgyV1DataDatasetProperties(
                file_collection_path="s3://default_bucket/opendes/data/vds-dataset/",
                index_file_path="s3://default_bucket/opendes/data/vds-dataset/vds-dataset.index",
                file_source_infos=[
                    DatasetRegisterBodyOpenzgyV1DataDatasetPropertiesFileSourceInfosItem(
                        file_source="s3://default_bucket/opendes/data/vds-dataset/vds-file-1",
                        preload_file_path="s3://staging-area/r7/raw-data/provided/documents/vds-file-1",
                        preload_file_create_user="somebody@acme.org",
                        preload_file_create_date=datetime.datetime.fromisoformat("2019-12-16T11:46:20+00:00"),
                        preload_file_modify_user="somebody.else@acme.org",
                        preload_file_modify_date=datetime.datetime.fromisoformat("2019-12-20T17:20:05+00:00"),
                        name="vds-file-1",
                        file_size="439452464",
                        checksum="checksum-value",
                        checksum_algorithm="MD5",
                    ),
                    DatasetRegisterBodyOpenzgyV1DataDatasetPropertiesFileSourceInfosItem(
                        file_source="s3://default_bucket/opendes/data/vds-dataset/vds-file-2",
                        preload_file_path="s3://staging-area/r7/raw-data/provided/documents/vds-file-2",
                        preload_file_create_user="somebody@acme.org",
                        preload_file_create_date=datetime.datetime.fromisoformat("2019-12-16T11:50:40+00:00"),
                        preload_file_modify_user="somebody.else@acme.org",
                        preload_file_modify_date=datetime.datetime.fromisoformat("2019-12-20T17:59:03+00:00"),
                        name="vds-file-2",
                        file_size="433645463",
                        checksum="checksum-value",
                        checksum_algorithm="MD5",
                    )
                ],
                checksum="checksum-value",
            ),
            extension_properties={
                "key": "value"
            },
        ),
    ),
    segy_v1=DatasetRegisterBodySegyV1(
        id="osdu:dataset--FileCollection.SEGY:b47f793a-dc9c-5d11-8d59-6cc611a98926",
        kind="osdu:wks:dataset--FileCollection.SEGY:1.0.0",
        version=1562066009929332,
        acl=DatasetRegisterBodySegyV1Acl(
            owners=[
                "someone@company.com"
            ],
            viewers=[
                "someone@company.com"
            ],
        ),
        legal=DatasetRegisterBodySegyV1Legal(
            legaltags=[
                "Example legaltags"
            ],
            other_relevant_data_countries=[
                "US"
            ],
            status="compliant",
        ),
        tags={
            "NameOfKey": "String value"
        },
        create_time=datetime.datetime.fromisoformat("2020-12-16T11:46:20+00:00"),
        create_user="some-user@some-company-cloud.com",
        modify_time=datetime.datetime.fromisoformat("2020-12-16T11:52:24+00:00"),
        modify_user="some-user@some-company-cloud.com",
        ancestry=DatasetRegisterBodySegyV1Ancestry(
            parents=[
                "parents"
            ],
        ),
        meta=[
            DatasetRegisterBodySegyV1MetaItemUnitOfMeasureId(
                kind=DatasetRegisterBodySegyV1MetaItemUnitOfMeasureIdKind.UNIT,
                persistable_reference="{\"abcd\":{\"a\":0.0,\"b\":1200.0,\"c\":3937.0,\"d\":0.0},\"symbol\":\"ft[US]\",\"baseMeasurement\":{\"ancestry\":\"L\",\"type\":\"UM\"},\"type\":\"UAD\"}",
            )
        ],
        data=DatasetRegisterBodySegyV1Data(
            resource_home_region_id="namespace:reference-data--OSDURegion:AWSEastUSA:",
            resource_host_region_i_ds=[
                "namespace:reference-data--OSDURegion:AWSEastUSA:"
            ],
            resource_curation_status="namespace:reference-data--ResourceCurationStatus:CREATED:",
            resource_lifecycle_status="namespace:reference-data--ResourceLifecycleStatus:LOADING:",
            resource_security_classification="namespace:reference-data--ResourceSecurityClassification:RESTRICTED:",
            source="Example Data Source",
            existence_kind="namespace:reference-data--ExistenceKind:Prototype:",
            name="Dataset X221/15",
            description="As originally delivered by ACME.com.",
            total_size="13245217273",
            encoding_format_type_id="namespace:reference-data--EncodingFormatType:text%2Fcsv:",
            schema_format_type_id="namespace:reference-data--SchemaFormatType:CWLS%20LAS3:",
            endian=DatasetRegisterBodySegyV1DataEndian.BIG,
            dataset_properties=DatasetRegisterBodySegyV1DataDatasetProperties(
                file_collection_path="s3://default_bucket/opendes/data/vds-dataset/",
                index_file_path="s3://default_bucket/opendes/data/vds-dataset/vds-dataset.index",
                file_source_infos=[
                    DatasetRegisterBodySegyV1DataDatasetPropertiesFileSourceInfosItem(
                        file_source="s3://default_bucket/opendes/data/vds-dataset/vds-file-1",
                        preload_file_path="s3://staging-area/r7/raw-data/provided/documents/vds-file-1",
                        preload_file_create_user="somebody@acme.org",
                        preload_file_create_date=datetime.datetime.fromisoformat("2019-12-16T11:46:20+00:00"),
                        preload_file_modify_user="somebody.else@acme.org",
                        preload_file_modify_date=datetime.datetime.fromisoformat("2019-12-20T17:20:05+00:00"),
                        name="vds-file-1",
                        file_size="439452464",
                        checksum="checksum-value",
                        checksum_algorithm="MD5",
                    ),
                    DatasetRegisterBodySegyV1DataDatasetPropertiesFileSourceInfosItem(
                        file_source="s3://default_bucket/opendes/data/vds-dataset/vds-file-2",
                        preload_file_path="s3://staging-area/r7/raw-data/provided/documents/vds-file-2",
                        preload_file_create_user="somebody@acme.org",
                        preload_file_create_date=datetime.datetime.fromisoformat("2019-12-16T11:50:40+00:00"),
                        preload_file_modify_user="somebody.else@acme.org",
                        preload_file_modify_date=datetime.datetime.fromisoformat("2019-12-20T17:59:03+00:00"),
                        name="vds-file-2",
                        file_size="433645463",
                        checksum="checksum-value",
                        checksum_algorithm="MD5",
                    )
                ],
                checksum="checksum-value",
            ),
            vector_header_mapping=[
                DatasetRegisterBodySegyV1DataVectorHeaderMappingItem(
                    key_name="namespace:reference-data--HeaderKeyName:CMPX:",
                    word_format="namespace:reference-data--WordFormatType:INT:",
                    word_width=2,
                    position=2,
                    uo_m="namespace:reference-data--UnitOfMeasure:m:",
                    scalar_indicator=DatasetRegisterBodySegyV1DataVectorHeaderMappingItemScalarIndicator.STANDARD,
                    scalar_override=12345.6,
                )
            ],
            segy_revision="rev 0",
            extension_properties={
                "key": "value"
            },
        ),
    ),
    acls=DatasetRegisterBodyAcls(
        admins=[
            "data.sdms.tenant.subproject.1b1417e5-fb0e-402a-b725-606723e50b76.admin@slb.p4d.cloud.slb-ds.com"
        ],
        viewers=[
            "data.sdms.tenant.subproject.1b1417e5-fb0e-402a-b725-606723e50b76.viewer@slb.p4d.cloud.slb-ds.com"
        ],
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

**tenantid:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**subprojectid:** `str` — Name of the subproject.
    
</dd>
</dl>

<dl>
<dd>

**datasetid:** `str` — Name of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Hierarchical path of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**ltag:** `typing.Optional[str]` — Legal tag of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**gtags:** `typing.Optional[typing.List[str]]` — Array of global tags associated with the dataset metadata. Once assigned, they can be used to filter datasets.
    
</dd>
</dl>

<dl>
<dd>

**seismicmeta:** `typing.Optional[DatasetRegisterBodySeismicmeta]` — Seismic metadata to be stored as dataecosystem storage record.
    
</dd>
</dl>

<dl>
<dd>

**openzgy_v1:** `typing.Optional[DatasetRegisterBodyOpenzgyV1]` — The dataset representation for optimized seismic access to the OpenZGY framework developed by Schlumberger, storing seismic 3D data for seismic interpretation.
    
</dd>
</dl>

<dl>
<dd>

**segy_v1:** `typing.Optional[DatasetRegisterBodySegyV1]` — A generic representation for  SEGY dataset represented as set of files, e.g. representing original tape reels.
    
</dd>
</dl>

<dl>
<dd>

**acls:** `typing.Optional[DatasetRegisterBodyAcls]` — ACLs with admin groups and viewer groups for the dataset.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset.<a href="src/fern/dataset/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul> <li>Delete a dataset in the seismic store.</li> <li>Required roles: <ul> <li>subproject.admin: if the applied subproject policy is 'uniform'</li> <li>dataset.admin: if the applied subproject policy is 'dataset'</li> </ul> </li></ul>
</dd>
</dl>
</dd>
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

client.dataset.delete(
    tenantid="tenantid",
    subprojectid="subprojectid",
    datasetid="datasetid",
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenantid:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**subprojectid:** `str` — Name of the subproject.
    
</dd>
</dl>

<dl>
<dd>

**datasetid:** `str` — Name of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Hierarchical path of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset.<a href="src/fern/dataset/client.py">patch</a>(...) -> Dataset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
<li>Update the dataset meta information in the seismic store or close (unlock) the dataset. If the endpoint is used without the close parameter, at least one body field is required or the endpoint will return an error.</li>
<li>Required roles:
  <ul>
    <li>subproject.admin: if the applied subproject policy is 'uniform'</li>
    <li>dataset.admin: if the applied subproject policy is 'dataset'</li>
  </ul>
</li>
<li>Patchable fields: <ul>
<li><b>dataset_new_name:</b> new name to use for the dataset (rename).</li>
<li><b>filemetadata:</b> This is a seismic store specific field and describes how the physical data is stored in the cloud storage system (GCS/AzureContainer etc.). This metadata is mainly used by client libraries to correctly reconstruct the dataset. For example you can store a dataset as truncated in multiple objects of 64MB each, name them from 0 to N and save the filemetadata = “{nObject: N, totalSize: 1024, objsize: 64, sizeUnit: MB}”.</li>
<li><b>last_modified_date:</b> Mark this field as true to update the dataset last modified date.</li>
<li><b>gtags:</b> Upsert tags to an existing dataset metadata. If the dataset metadata already has gtags, then new gtags are appended to this list.</li>
<li><b>ltag:</b> Update the existing legalTag value.</b></li>
<li><b>readonly:</b> Update the dataset mode to readonly (true) or to read/write (false).</li></ul></li></ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.dataset import DatasetPatchSeismicmeta, DatasetPatchOpenzgyV1, DatasetPatchOpenzgyV1Acl, DatasetPatchOpenzgyV1Legal, DatasetPatchOpenzgyV1MetaItemUnitOfMeasureId, DatasetPatchOpenzgyV1MetaItemUnitOfMeasureIdKind, DatasetPatchOpenzgyV1Data, DatasetPatchOpenzgyV1DataEndian, DatasetPatchOpenzgyV1DataDatasetProperties, DatasetPatchOpenzgyV1DataDatasetPropertiesFileSourceInfosItem, DatasetPatchSegyV1, DatasetPatchSegyV1Acl, DatasetPatchSegyV1Legal, DatasetPatchSegyV1Ancestry, DatasetPatchSegyV1MetaItemUnitOfMeasureId, DatasetPatchSegyV1MetaItemUnitOfMeasureIdKind, DatasetPatchSegyV1Data, DatasetPatchSegyV1DataEndian, DatasetPatchSegyV1DataDatasetProperties, DatasetPatchSegyV1DataDatasetPropertiesFileSourceInfosItem, DatasetPatchSegyV1DataVectorHeaderMappingItem, DatasetPatchSegyV1DataVectorHeaderMappingItemScalarIndicator, DatasetPatchAcls
import datetime

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.dataset.patch(
    tenantid="tenantid",
    subprojectid="subprojectid",
    datasetid="datasetid",
    path="path",
    dataset_new_name="dsx02",
    metadata={
        "f1": "v1",
        "f2": "v2",
        "f3": "v3"
    },
    filemetadata={
        "f1": "v1",
        "f2": "v2",
        "f3": "v3"
    },
    last_modified_date="Thu Jul 16 2020 04:37:41 GMT+0000 (Coordinated Universal Time)",
    gtags=[
        "tag01",
        "tag02",
        "tag03"
    ],
    ltag="legal-tag",
    readonly=False,
    seismicmeta=DatasetPatchSeismicmeta(
        kind="slb:seistore:seismic2d:1.0.0",
        data={
            "msg": "sample data"
        },
    ),
    openzgy_v1=DatasetPatchOpenzgyV1(
        id="opendes:dataset--FileCollection.Slb.OpenZGY:5771c352-dc52-5d26-9351-2b8dbc9eb474",
        kind="osdu:wks:dataset--FileCollection.Slb.OpenZGY:1.0.0",
        version=1637208623527796,
        acl=DatasetPatchOpenzgyV1Acl(
            owners=[
                "data.default.viewers@opendes.enterprisedata.cloud.slb-ds.com"
            ],
            viewers=[
                "data.default.viewers@opendes.enterprisedata.cloud.slb-ds.com"
            ],
        ),
        legal=DatasetPatchOpenzgyV1Legal(
            legaltags=[
                "opendes-seistore-test-01"
            ],
            other_relevant_data_countries=[
                "US"
            ],
            status="compliant",
        ),
        tags={
            "NameOfKey": "String value"
        },
        create_time=datetime.datetime.fromisoformat("2021-11-16T02:08:16+00:00"),
        create_user="vmanohar@slb.com",
        modify_time=datetime.datetime.fromisoformat("2021-11-18T04:10:23+00:00"),
        modify_user="39916b94-71a9-409e-856e-0f29558fa908",
        meta=[
            DatasetPatchOpenzgyV1MetaItemUnitOfMeasureId(
                kind=DatasetPatchOpenzgyV1MetaItemUnitOfMeasureIdKind.UNIT,
                persistable_reference="{\"abcd\":{\"a\":0.0,\"b\":1200.0,\"c\":3937.0,\"d\":0.0},\"symbol\":\"ft[US]\",\"baseMeasurement\":{\"ancestry\":\"L\",\"type\":\"UM\"},\"type\":\"UAD\"}",
            )
        ],
        data=DatasetPatchOpenzgyV1Data(
            resource_home_region_id="opendes:reference-data--OSDURegion:AWSEastUSA:",
            resource_host_region_i_ds=[
                "opendes:reference-data--OSDURegion:AWSEastUSA:"
            ],
            resource_curation_status="opendes:reference-data--ResourceCurationStatus:CREATED:",
            resource_lifecycle_status="opendes:reference-data--ResourceLifecycleStatus:LOADING:",
            resource_security_classification="opendes:reference-data--ResourceSecurityClassification:RESTRICTED:",
            source="Example Data Source",
            existence_kind="opendes:reference-data--ExistenceKind:Prototype:",
            name="Dataset X221/15",
            description="As originally delivered by ACME.com.",
            total_size="13245217273",
            encoding_format_type_id="opendes:reference-data--EncodingFormatType:text%2Fcsv:",
            schema_format_type_id="opendes:reference-data--SchemaFormatType:CWLS%20LAS3:",
            endian=DatasetPatchOpenzgyV1DataEndian.BIG,
            dataset_properties=DatasetPatchOpenzgyV1DataDatasetProperties(
                file_collection_path="s3://default_bucket/opendes/data/vds-dataset/",
                index_file_path="s3://default_bucket/opendes/data/vds-dataset/vds-dataset.index",
                file_source_infos=[
                    DatasetPatchOpenzgyV1DataDatasetPropertiesFileSourceInfosItem(
                        file_source="s3://default_bucket/opendes/data/vds-dataset/vds-file-1",
                        preload_file_path="s3://staging-area/r7/raw-data/provided/documents/vds-file-1",
                        preload_file_create_user="somebody@acme.org",
                        preload_file_create_date=datetime.datetime.fromisoformat("2019-12-16T11:46:20+00:00"),
                        preload_file_modify_user="somebody.else@acme.org",
                        preload_file_modify_date=datetime.datetime.fromisoformat("2019-12-20T17:20:05+00:00"),
                        name="vds-file-1",
                        file_size="439452464",
                        checksum="checksum-value",
                        checksum_algorithm="MD5",
                    ),
                    DatasetPatchOpenzgyV1DataDatasetPropertiesFileSourceInfosItem(
                        file_source="s3://default_bucket/opendes/data/vds-dataset/vds-file-2",
                        preload_file_path="s3://staging-area/r7/raw-data/provided/documents/vds-file-2",
                        preload_file_create_user="somebody@acme.org",
                        preload_file_create_date=datetime.datetime.fromisoformat("2019-12-16T11:50:40+00:00"),
                        preload_file_modify_user="somebody.else@acme.org",
                        preload_file_modify_date=datetime.datetime.fromisoformat("2019-12-20T17:59:03+00:00"),
                        name="vds-file-2",
                        file_size="433645463",
                        checksum="checksum-value",
                        checksum_algorithm="MD5",
                    )
                ],
                checksum="checksum-value",
            ),
            extension_properties={
                "key": "value"
            },
        ),
    ),
    segy_v1=DatasetPatchSegyV1(
        id="osdu:dataset--FileCollection.SEGY:b47f793a-dc9c-5d11-8d59-6cc611a98926",
        kind="osdu:wks:dataset--FileCollection.SEGY:1.0.0",
        version=1562066009929332,
        acl=DatasetPatchSegyV1Acl(
            owners=[
                "someone@company.com"
            ],
            viewers=[
                "someone@company.com"
            ],
        ),
        legal=DatasetPatchSegyV1Legal(
            legaltags=[
                "Example legaltags"
            ],
            other_relevant_data_countries=[
                "US"
            ],
            status="compliant",
        ),
        tags={
            "NameOfKey": "String value"
        },
        create_time=datetime.datetime.fromisoformat("2020-12-16T11:46:20+00:00"),
        create_user="some-user@some-company-cloud.com",
        modify_time=datetime.datetime.fromisoformat("2020-12-16T11:52:24+00:00"),
        modify_user="some-user@some-company-cloud.com",
        ancestry=DatasetPatchSegyV1Ancestry(
            parents=[
                "parents"
            ],
        ),
        meta=[
            DatasetPatchSegyV1MetaItemUnitOfMeasureId(
                kind=DatasetPatchSegyV1MetaItemUnitOfMeasureIdKind.UNIT,
                persistable_reference="{\"abcd\":{\"a\":0.0,\"b\":1200.0,\"c\":3937.0,\"d\":0.0},\"symbol\":\"ft[US]\",\"baseMeasurement\":{\"ancestry\":\"L\",\"type\":\"UM\"},\"type\":\"UAD\"}",
            )
        ],
        data=DatasetPatchSegyV1Data(
            resource_home_region_id="namespace:reference-data--OSDURegion:AWSEastUSA:",
            resource_host_region_i_ds=[
                "namespace:reference-data--OSDURegion:AWSEastUSA:"
            ],
            resource_curation_status="namespace:reference-data--ResourceCurationStatus:CREATED:",
            resource_lifecycle_status="namespace:reference-data--ResourceLifecycleStatus:LOADING:",
            resource_security_classification="namespace:reference-data--ResourceSecurityClassification:RESTRICTED:",
            source="Example Data Source",
            existence_kind="namespace:reference-data--ExistenceKind:Prototype:",
            name="Dataset X221/15",
            description="As originally delivered by ACME.com.",
            total_size="13245217273",
            encoding_format_type_id="namespace:reference-data--EncodingFormatType:text%2Fcsv:",
            schema_format_type_id="namespace:reference-data--SchemaFormatType:CWLS%20LAS3:",
            endian=DatasetPatchSegyV1DataEndian.BIG,
            dataset_properties=DatasetPatchSegyV1DataDatasetProperties(
                file_collection_path="s3://default_bucket/opendes/data/vds-dataset/",
                index_file_path="s3://default_bucket/opendes/data/vds-dataset/vds-dataset.index",
                file_source_infos=[
                    DatasetPatchSegyV1DataDatasetPropertiesFileSourceInfosItem(
                        file_source="s3://default_bucket/opendes/data/vds-dataset/vds-file-1",
                        preload_file_path="s3://staging-area/r7/raw-data/provided/documents/vds-file-1",
                        preload_file_create_user="somebody@acme.org",
                        preload_file_create_date=datetime.datetime.fromisoformat("2019-12-16T11:46:20+00:00"),
                        preload_file_modify_user="somebody.else@acme.org",
                        preload_file_modify_date=datetime.datetime.fromisoformat("2019-12-20T17:20:05+00:00"),
                        name="vds-file-1",
                        file_size="439452464",
                        checksum="checksum-value",
                        checksum_algorithm="MD5",
                    ),
                    DatasetPatchSegyV1DataDatasetPropertiesFileSourceInfosItem(
                        file_source="s3://default_bucket/opendes/data/vds-dataset/vds-file-2",
                        preload_file_path="s3://staging-area/r7/raw-data/provided/documents/vds-file-2",
                        preload_file_create_user="somebody@acme.org",
                        preload_file_create_date=datetime.datetime.fromisoformat("2019-12-16T11:50:40+00:00"),
                        preload_file_modify_user="somebody.else@acme.org",
                        preload_file_modify_date=datetime.datetime.fromisoformat("2019-12-20T17:59:03+00:00"),
                        name="vds-file-2",
                        file_size="433645463",
                        checksum="checksum-value",
                        checksum_algorithm="MD5",
                    )
                ],
                checksum="checksum-value",
            ),
            vector_header_mapping=[
                DatasetPatchSegyV1DataVectorHeaderMappingItem(
                    key_name="namespace:reference-data--HeaderKeyName:CMPX:",
                    word_format="namespace:reference-data--WordFormatType:INT:",
                    word_width=2,
                    position=2,
                    uo_m="namespace:reference-data--UnitOfMeasure:m:",
                    scalar_indicator=DatasetPatchSegyV1DataVectorHeaderMappingItemScalarIndicator.STANDARD,
                    scalar_override=12345.6,
                )
            ],
            segy_revision="rev 0",
            extension_properties={
                "key": "value"
            },
        ),
    ),
    acls=DatasetPatchAcls(
        admins=[
            "data.sdms.tenant.subproject.1b1417e5-fb0e-402a-b725-606723e50b76.admin@slb.p4d.cloud.slb-ds.com"
        ],
        viewers=[
            "data.sdms.tenant.subproject.1b1417e5-fb0e-402a-b725-606723e50b76.viewer@slb.p4d.cloud.slb-ds.com"
        ],
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

**tenantid:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**subprojectid:** `str` — Name of the subproject.
    
</dd>
</dl>

<dl>
<dd>

**datasetid:** `str` — Name of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Hierarchical path of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**close:** `typing.Optional[str]` — Non null sbit value of the dataset. Using this value here will close the dataset.
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**dataset_new_name:** `typing.Optional[str]` — New name for the dataset.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Generic information about the dataset stored as key value pairs.
    
</dd>
</dl>

<dl>
<dd>

**filemetadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Number of objects and the size in bytes of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**last_modified_date:** `typing.Optional[str]` — Date when the dataset was last modified.
    
</dd>
</dl>

<dl>
<dd>

**gtags:** `typing.Optional[typing.List[str]]` — Array of tags associated with the dataset. After patching these tags, they can be used to filter the datasets.
    
</dd>
</dl>

<dl>
<dd>

**ltag:** `typing.Optional[str]` — Legal tag associated with the dataset.
    
</dd>
</dl>

<dl>
<dd>

**readonly:** `typing.Optional[bool]` — True if the dataset is read only.
    
</dd>
</dl>

<dl>
<dd>

**seismicmeta:** `typing.Optional[DatasetPatchSeismicmeta]` — Seismic metadata associated with the dataset which is used to create a data ecosystem storage record.
    
</dd>
</dl>

<dl>
<dd>

**openzgy_v1:** `typing.Optional[DatasetPatchOpenzgyV1]` — The dataset representation for optimized seismic access to the OpenZGY framework developed by Schlumberger, storing seismic 3D data for seismic interpretation.
    
</dd>
</dl>

<dl>
<dd>

**segy_v1:** `typing.Optional[DatasetPatchSegyV1]` — A generic representation for  SEGY dataset represented as set of files, e.g. representing original tape reels.
    
</dd>
</dl>

<dl>
<dd>

**acls:** `typing.Optional[DatasetPatchAcls]` — ACLs with admin groups and viewer groups for the dataset.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset.<a href="src/fern/dataset/client.py">acquire_a_lock_for_a_dataset_id</a>(...) -> Dataset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
  <li>Open a dataset for read or write and lock its state.</li>
  <li>Required roles open lock for write:
    <ul>
      <li>subproject.admin: if the applied subproject policy is 'uniform'</li>
      <li>dataset.admin: if the applied subproject policy is 'dataset'</li>
    </ul>
  </li>
  <li>Required roles open lock for read:
    <ul>
      <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li>
      <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li>
    </ul>
  </li>
</ul>
operationId: dataset-lock
</dd>
</dl>
</dd>
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

client.dataset.acquire_a_lock_for_a_dataset_id(
    tenantid="tenantid",
    subprojectid="subprojectid",
    datasetid="datasetid",
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenantid:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**subprojectid:** `str` — Name of the subproject.
    
</dd>
</dl>

<dl>
<dd>

**datasetid:** `str` — Name of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Hierarchical path of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**openmode:** `typing.Optional[str]` — Type of the lock which can be set to 'read' (default) or 'write'.
    
</dd>
</dl>

<dl>
<dd>

**wid:** `typing.Optional[float]` — Session identifier issued for a previous write lock acquisition operation.
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset.<a href="src/fern/dataset/client.py">lock_rm</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
  <li>Removes the lock for a dataset id.</li>
  <li>Required roles:
    <ul>
      <li>subproject.admin: if the applied subproject policy is 'uniform'</li>
      <li>dataset.admin: if the applied subproject policy is 'dataset'</li>
    </ul>
  </li>
</ul>
</dd>
</dl>
</dd>
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

client.dataset.lock_rm(
    tenantid="tenantid",
    subprojectid="subprojectid",
    datasetid="datasetid",
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenantid:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**subprojectid:** `str` — Name of the subproject.
    
</dd>
</dl>

<dl>
<dd>

**datasetid:** `str` — Name of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Hierarchical path for the dataset.
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset.<a href="src/fern/dataset/client.py">permission</a>(...) -> DatasetPermission</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
  <li>Retrieve the access permission of a user on a dataset.</li>
  <li>Required roles:
    <ul>
      <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li>
      <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li>
    </ul>
  </li>
</ul>
</dd>
</dl>
</dd>
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

client.dataset.permission(
    tenantid="tenantid",
    subprojectid="subprojectid",
    datasetid="datasetid",
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenantid:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**subprojectid:** `str` — Name of the subproject.
    
</dd>
</dl>

<dl>
<dd>

**datasetid:** `str` — Name of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Hierarchical path for the dataset.
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset.<a href="src/fern/dataset/client.py">ctag_check</a>(...) -> bool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul><li>Check if the provided dataset cTag match the one stored in the metadata catalog.</li><li>Required roles: subproject.admin, subproject.viewer</li></ul>
</dd>
</dl>
</dd>
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

client.dataset.ctag_check(
    tenantid="tenantid",
    subprojectid="subprojectid",
    datasetid="datasetid",
    path="path",
    ctag="ctag",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenantid:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**subprojectid:** `str` — Name of the subproject.
    
</dd>
</dl>

<dl>
<dd>

**datasetid:** `str` — Name of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Hierarchical path of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**ctag:** `str` — Ctag to be validated.
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset.<a href="src/fern/dataset/client.py">add_tag</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
  <li>Upsert tags to an existing dataset metadata. If the dataset metadata already has gtags, then  new gtags are appended to this list.</li>
  <li>Required roles:
    <ul>
      <li>subproject.admin: if the applied subproject policy is 'uniform'</li>
      <li>dataset.admin: if the applied subproject policy is 'dataset'</li>
    </ul>
  </li>
</ul>
</dd>
</dl>
</dd>
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

client.dataset.add_tag(
    tenantid="tenantid",
    subprojectid="subprojectid",
    datasetid="datasetid",
    path="path",
    gtag=[
        "gtag"
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

**tenantid:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**subprojectid:** `str` — Name of the subproject.
    
</dd>
</dl>

<dl>
<dd>

**datasetid:** `str` — Name of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Hierarchical path of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**gtag:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Gtags array list.
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset.<a href="src/fern/dataset/client.py">size</a>(...) -> DatasetSize</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
<li>Compute and retrieve the size of a dataset and the date of when the size was computed.</li>
<li>Required roles: subproject.admin</li></ul>
</dd>
</dl>
</dd>
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

client.dataset.size(
    tenantid="tenantid",
    subprojectid="subprojectid",
    datasetid="datasetid",
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenantid:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**subprojectid:** `str` — Name of the subproject.
    
</dd>
</dl>

<dl>
<dd>

**datasetid:** `str` — Name of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Hierarchical path of the dataset.
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset.<a href="src/fern/dataset/client.py">read_directory</a>(...) -> DatasetAndDirectories</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
<li>List datasets and sub-directories for a directory path.</li>
<li>Required roles: subproject.admin, subproject.viewer</li></ul>
</dd>
</dl>
</dd>
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

client.dataset.read_directory(
    tenantid="tenantid",
    subprojectid="subprojectid",
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenantid:** `str` — The tenant project name.
    
</dd>
</dl>

<dl>
<dd>

**subprojectid:** `str` — The sub-project name.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — The hierarchy path.
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset.<a href="src/fern/dataset/client.py">list</a>(...) -> PaginatedDatasets</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
  <li>Return the list of datasets in a sub-project. The list can be filtered by gtags. Support pagination.</li>
  <li>Required roles: subproject.admin, subproject.viewer</li>
</ul>
</dd>
</dl>
</dd>
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

client.dataset.list(
    tenantid="tenantid",
    subprojectid="subprojectid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenantid:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**subprojectid:** `str` — Name of the subproject.
    
</dd>
</dl>

<dl>
<dd>

**gtag:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Gtags associated with dataset metadata.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[str]` — Limit the number of datasets in the response
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination on the datasets list
    
</dd>
</dl>

<dl>
<dd>

**translate_user_info:** `typing.Optional[bool]` — translate the user-id to a more human readable user info
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset.<a href="src/fern/dataset/client.py">list_post</a>(...) -> PaginatedDatasets</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
  <li>Return the list of datasets in a sub-project. The list can be filtered by gtags. Support pagination.</li>
  <li>Required roles: subproject.admin, subproject.viewer</li>
</ul>
</dd>
</dl>
</dd>
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

client.dataset.list_post(
    tenantid="tenantid",
    subprojectid="subprojectid",
    gtags=[
        "tagA",
        "tagB"
    ],
    limit=10,
    cursor="next-page-token-931fvm19vm1-vm1v1",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenantid:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**subprojectid:** `str` — Name of the subproject.
    
</dd>
</dl>

<dl>
<dd>

**translate_user_info:** `typing.Optional[bool]` — translate the user-id to a more human readable user info
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**gtags:** `typing.Optional[typing.List[str]]` — Array of global tags associated with the dataset metadata. Once assigned, they can be used to filter datasets.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — the max limit of datasets in the response
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — the cursor value required to retrieve the next page of result
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dataset.<a href="src/fern/dataset/client.py">exist</a>(...) -> typing.List[bool]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
<li>Check if the dataset exists.</li>
<li>Required roles: subproject.admin, subproject.viewer</li></ul>
</dd>
</dl>
</dd>
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

client.dataset.exist(
    tenantid="tenantid",
    subprojectid="subprojectid",
    datasets=[
        "a/b/c/dsx01",
        "a/b/c/dsx02"
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

**tenantid:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**subprojectid:** `str` — Name of the subproject.
    
</dd>
</dl>

<dl>
<dd>

**request:** `DatasetCheckList` 
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DatasetDeprecated
<details><summary><code>client.dataset_deprecated.<a href="src/fern/dataset_deprecated/client.py">dataset_sizes</a>(...) -> typing.List[float]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
<li>Return a list with the sizes of the requested datasets.</li>
<li>The correctness is not guarantee since this API returns sizes stored by the user in the dataset manifest.</li>
<li>This API is deprecated, please using /size endpoint to compute and retrieve the size information</li>
<li>Required roles: subproject.admin, subproject.viewer</li></ul>
</dd>
</dl>
</dd>
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

client.dataset_deprecated.dataset_sizes(
    tenantid="tenantid",
    subprojectid="subprojectid",
    datasets=[
        "a/b/c/dsx01",
        "a/b/c/dsx02"
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

**tenantid:** `str` — Name of the tenant
    
</dd>
</dl>

<dl>
<dd>

**subprojectid:** `str` — Name of the subproject.
    
</dd>
</dl>

<dl>
<dd>

**request:** `DatasetCheckList` 
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Utility
<details><summary><code>client.utility.<a href="src/fern/utility/client.py">ls</a>(...) -> LsDatasets</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
<li>Return the list of datasets and sub-directories of a seismic store path.</li>
<li>Required roles: subproject.admin, subproject.viewer</li></ul>
</dd>
</dl>
</dd>
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

client.utility.ls(
    sdpath="sdpath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sdpath:** `str` — Seismic store path, sd://tenant/sub-project/path.
    
</dd>
</dl>

<dl>
<dd>

**wmode:** `typing.Optional[str]` — Working mode, directories or datasets or undefined for both.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — Limits the total number of datasets to return.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Pagination token - this query parameter can be omitted on first call.
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.utility.<a href="src/fern/utility/client.py">storage_tiers</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul><li>Return the list of storage tiers</ul>
</dd>
</dl>
</dd>
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

client.utility.storage_tiers()

```
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

<details><summary><code>client.utility.<a href="src/fern/utility/client.py">cp</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
<li>Copy a seismic store dataset. The source and destination dataset must be in the same sub-project.</li>
<li>Required roles:
  <ul>
    <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li>
    <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li>
  </ul>
</li>
</ul>
</dd>
</dl>
</dd>
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

client.utility.cp(
    sdpath_from="sdpath_from",
    sdpath_to="sdpath_to",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sdpath_from:** `str` — Seismic store source dataset path.
    
</dd>
</dl>

<dl>
<dd>

**sdpath_to:** `str` — Seismic store destination dataset path.
    
</dd>
</dl>

<dl>
<dd>

**lock:** `typing.Optional[bool]` — Lock source and destination while copying.
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.utility.<a href="src/fern/utility/client.py">gcs_access_token</a>(...) -> AccessToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
  <li>Generate a GCS access token for a specified seismic store resource. The source and destination dataset must be in the same sub-project.</li>
  <li>Required roles:
    <ul>
      <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li>
      <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li>
    </ul>
  </li>
</ul>
</dd>
</dl>
</dd>
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

client.utility.gcs_access_token(
    sdpath="sdpath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sdpath:** `str` — Seismic store path in the format sd://tenant/sub-project.
    
</dd>
</dl>

<dl>
<dd>

**readonly:** `typing.Optional[bool]` — Readonly access, true(default) or false.
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.utility.<a href="src/fern/utility/client.py">upload_connection_string</a>(...) -> AccessToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul> <li>Generate the upload connection credential string for a subproject collection or a dataset, depending of the applied access policy (uniform/dataset). <li>These credentials can be used via CSP SDK, on client side, to perform bulk upload.</li> <li> The endpoint response is CSP (Cloud Solution Provider) dependent: <ul> <br/><li><b>Azure</b>: shared access signature (SaS) Url token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'https://{accountName}.blob.core.windows.net/{containerName}?{SASQueryParameters}`' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'SasUrl' <br/>} <br/><br/></li> <li><b>Google</b>: standard access token credential signed and down-scoped by google <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'google_signed_access_token' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3600 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>AWS</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>IBM</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 7200 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> </ul> </li> <li>Required roles: <ul> <li>subproject.admin: if the applied subproject policy is 'uniform'</li> <li>dataset.admin: if the applied subproject policy is 'dataset'</li> </ul> </li> </ul>
</dd>
</dl>
</dd>
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

client.utility.upload_connection_string(
    sdpath="sdpath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sdpath:** `str` — Seismic store path in the format sd://tenant/subproject (for uniform applied policies) or sd://tenant/subproject/dataset (for dataset applied policies)
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.utility.<a href="src/fern/utility/client.py">download_connection_string</a>(...) -> AccessToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul> <li>Generate the download connection credential string for a subproject collection or a dataset, depending of the applied access policy (uniform/dataset). <li>These credentials can be used via CSP SDK, on client side, to perform bulk download.</li> <li> The endpoint response is CSP (Cloud Solution Provider) dependent: <ul> <br/><li><b>Azure</b>: shared access signature (SaS) Url token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'https://{accountName}.blob.core.windows.net/{containerName}?{SASQueryParameters}`' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'SasUrl' <br/>} <br/><br/></li> <li><b>Google</b>: standard access token credential signed and down-scoped by google <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'google_signed_access_token' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3600 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>AWS</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 3599 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> <li><b>IBM</b>: double column separated string containing access key id, the access key secret and the session token <br/> <br/>{ <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_token: 'accessKeyId:secretAccessKey:sessionToken' <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expires_in: 7200 <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type: 'Bearer' <br/>} <br/><br/></li> </ul> </li> <li>Required roles: <ul> <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li> <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li> </ul> </li> </ul>
</dd>
</dl>
</dd>
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

client.utility.download_connection_string(
    sdpath="sdpath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sdpath:** `str` — Seismic store path in the format sd://tenant/subproject (for uniform applied policies) or sd://tenant/subproject/dataset (for dataset applied policies)
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `typing.Optional[str]` — The impersonation token context (required only with impersonation token credentials)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ImpersonationTokenObsolete
<details><summary><code>client.impersonation_token_obsolete.<a href="src/fern/impersonation_token_obsolete/client.py">imp_token</a>(...) -> ImpersonationToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
<li>Generate an impersonation credential token of a user for a set of subproject resources.</li>
<li>Required roles: app.trusted</li></ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Resource
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.impersonation_token_obsolete.imp_token(
    token="ya29.fgdgsdngevrjbinb0exdnberoibnerbnerber-fdsfwefwe_cece.rfd43f3",
    resources=[
        Resource(
            resource="sd://tnx01/spx01",
            readonly=True,
        ),
        Resource(
            resource="sd://tnx01/spx02",
            readonly=False,
        ),
        Resource(
            resource="sd://tnx01/spx03",
        )
    ],
    refresh_url="https://httpstat.us/200",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token:** `str` — Impersonation token that was previously issued.
    
</dd>
</dl>

<dl>
<dd>

**resources:** `typing.List[Resource]` 
    
</dd>
</dl>

<dl>
<dd>

**refresh_url:** `str` — A web service endpoint that the seismic store service will invoke to check if the impersonation token can be refreshed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.impersonation_token_obsolete.<a href="src/fern/impersonation_token_obsolete/client.py">imp_token_refresh</a>(...) -> ImpersonationToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul><li>Refresh an impersonation credential token.</li><li>Required roles: none</li></ul>
</dd>
</dl>
</dd>
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

client.impersonation_token_obsolete.imp_token_refresh(
    token="ya29.fgdgsdngevrjbinb0exdnberoibnerbnerber-fdsfwefwe_cece.rfd43f3",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token:** `str` — Impersonation token
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.impersonation_token_obsolete.<a href="src/fern/impersonation_token_obsolete/client.py">imp_token_patch</a>(...) -> ImpersonationToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
<li>Patch an impersonation credential token's refresh url and generate a new impersonation token.</li>
<li>Required roles: none</li></ul>
</dd>
</dl>
</dd>
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

client.impersonation_token_obsolete.imp_token_patch(
    token="ya29.fgdgsdngevrjbinb0exdnberoibnerbnerber-fdsfwefwe_cece.rfd43f3",
    refresh_url="https://httpstat.us/200",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token:** `str` — Impersonation token that was previously issued.
    
</dd>
</dl>

<dl>
<dd>

**refresh_url:** `str` — New endpoint that the seismic store service will invoke to check if the impersonation token can be refreshed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ImpersonationToken
<details><summary><code>client.impersonation_token.<a href="src/fern/impersonation_token/client.py">generate</a>(...) -> ImpersonationToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul><li>Generate a credential token to impersonate user access for a set of subproject resources.</li><li>Required roles: app.trusted</li></ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Resource
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.impersonation_token.generate(
    user_token="user-token",
    resources=[
        Resource(
            resource="sd://tnx01/spx01",
            readonly=True,
        ),
        Resource(
            resource="sd://tnx01/spx02",
            readonly=False,
        )
    ],
    metadata={
        "jobId": 1234
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_token:** `str` — The credential of the user to impersonate.
    
</dd>
</dl>

<dl>
<dd>

**resources:** `typing.List[Resource]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — A general field to set extra meta-information to the impersonation token signature. These are saved along with the token signatures.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.impersonation_token.<a href="src/fern/impersonation_token/client.py">refresh</a>(...) -> ImpersonationToken</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul><li>Refresh an impersonation credential token.</li><li>Required roles: app.trusted</li></ul>
</dd>
</dl>
</dd>
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

client.impersonation_token.refresh(
    impersonation_token="impersonation-token",
    impersonation_token_context="impersonation-token-context",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**impersonation_token:** `str` — The impersonation token to refresh.
    
</dd>
</dl>

<dl>
<dd>

**impersonation_token_context:** `str` — The impersonation token context.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Subproject
<details><summary><code>client.subproject.<a href="src/fern/subproject/client.py">get</a>(...) -> SubProject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul><li>Return the metadata for a requested sub-project.</li><li>Required roles: subproject.admin</li></ul>
</dd>
</dl>
</dd>
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

client.subproject.get(
    tenantid="tenantid",
    subprojectid="subprojectid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenantid:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**subprojectid:** `str` — Name of the subproject.
    
</dd>
</dl>

<dl>
<dd>

**translate_user_info:** `typing.Optional[bool]` — translate the user-id to a more human readable user info
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subproject.<a href="src/fern/subproject/client.py">create</a>(...) -> SubProject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
<li>Creates a new subproject resource in seismic store.</li>
<li>Required roles: users.datalake.admin</li></ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.subproject import SubProjectCreateBodyAccessPolicy, SubProjectCreateBodyAcls

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.subproject.create(
    tenantid="tenantid",
    subprojectid="subprojectid",
    admin="admin@email",
    storage_class="MULTI_REGIONAL",
    storage_location="US",
    access_policy=SubProjectCreateBodyAccessPolicy.UNIFORM,
    acls=SubProjectCreateBodyAcls(
        admins=[
            "data.sdms.tenant.subproject.1b1417e5-fb0e-402a-b725-606723e50b76.admin@slb.p4d.cloud.slb-ds.com"
        ],
        viewers=[
            "data.sdms.tenant.subproject.1b1417e5-fb0e-402a-b725-606723e50b76.viewer@slb.p4d.cloud.slb-ds.com"
        ],
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

**tenantid:** `str` — The tenant name - In OSDU this match the data-partition-id
    
</dd>
</dl>

<dl>
<dd>

**subprojectid:** `str` — The subproject name. It must match the regex <b>^[a-z][a-z\d\-]*[a-z\d]$</b>
    
</dd>
</dl>

<dl>
<dd>

**ltag:** `typing.Optional[str]` — A valid compliance legal tag. It can be generated and managed via core-compliance-service.
    
</dd>
</dl>

<dl>
<dd>

**admin:** `typing.Optional[str]` — An optional user to set as admin. The user will be added in the first admins acl group
    
</dd>
</dl>

<dl>
<dd>

**storage_class:** `typing.Optional[str]` — Storage class for the bucket (Google Required Only)
    
</dd>
</dl>

<dl>
<dd>

**storage_location:** `typing.Optional[str]` — Storage location for the bucket (Google Required Only)
    
</dd>
</dl>

<dl>
<dd>

**access_policy:** `typing.Optional[SubProjectCreateBodyAccessPolicy]` — The datasets access level mode: "uniform" (uniform data access to all subprojects datasets) or "datasets" (acl can be applied at dataset level)
    
</dd>
</dl>

<dl>
<dd>

**acls:** `typing.Optional[SubProjectCreateBodyAcls]` — The entitlement groups to enable subproject access as admin or viewer. If not specified, default entitlement data groups will be created.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subproject.<a href="src/fern/subproject/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul><li>Delete a subproject in seismic store.</li><li>Required roles: users.datalake.admin</li></ul>
</dd>
</dl>
</dd>
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

client.subproject.delete(
    tenantid="tenantid",
    subprojectid="subprojectid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenantid:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**subprojectid:** `str` — Name of the subproject.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subproject.<a href="src/fern/subproject/client.py">patch</a>(...) -> SubProject</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
  <li>Patch a subproject metadata in seismic store.</li>
  <li>Required roles: subproject.admin</li>
  <li>Possible actions:</li>
  <ul>
    <li>legal tag and/or ACLs groups can be patched by providing new values</li>
    <li>access policy can be changed from <i>uniform</i> to <i>dataset</i></li>
    <li><b>NOTE:</b> It is not possible to change subproject access policy from <i>dataset</i> to <i>uniform</i></li>
    <li><b>NOTE:</b> This operation is eventual consistent and it can take up to 5s before it gets completely applied</li>
  </ul>
</ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.subproject import SubProjectPatchBodyAcls

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.subproject.patch(
    tenantid="tenantid",
    subprojectid="subprojectid",
    ltag="ltag",
    access_policy="dataset",
    acls=SubProjectPatchBodyAcls(
        admins=[
            "data.sdms.tenant.subproject.1b1417e5-fb0e-402a-b725-606723e50b76.admin@slb.p4d.cloud.slb-ds.com",
            "data.sdms.tenant.subproject.1f1tr7fe-fb0e-402a-b725-606723e5356n.admin@slb.p4d.cloud.slb-ds.com"
        ],
        viewers=[
            "data.sdms.tenant.subproject.1b1417e5-fb0e-402a-b725-606723e50b76.viewer@slb.p4d.cloud.slb-ds.com"
        ],
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

**tenantid:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**subprojectid:** `str` — Name of the subproject.
    
</dd>
</dl>

<dl>
<dd>

**ltag:** `str` — Legal tag of the subproject.
    
</dd>
</dl>

<dl>
<dd>

**recursive:** `typing.Optional[bool]` — True if the legal tags of all datasets in a subproject needs to be updated.
    
</dd>
</dl>

<dl>
<dd>

**access_policy:** `typing.Optional[str]` — Access Policy for the subproject.
    
</dd>
</dl>

<dl>
<dd>

**acls:** `typing.Optional[SubProjectPatchBodyAcls]` — ACLs with admin groups and viewer groups. Existing acls will be replaced with the provided acls.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SubProject
<details><summary><code>client.sub_project.<a href="src/fern/sub_project/client.py">sub_project_list</a>(...) -> typing.List[SubProject]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul><li>Return the list of sub-projects in a tenant.</li><li>Required roles: users.datalake.admin</li></ul>
</dd>
</dl>
</dd>
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

client.sub_project.sub_project_list(
    tenantid="tenantid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenantid:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tenant
<details><summary><code>client.tenant.<a href="src/fern/tenant/client.py">get</a>(...) -> Tenant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul><li>Return the tenant metadata.</li><li>Required roles: seistore.system.admin</li></ul>
</dd>
</dl>
</dd>
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

client.tenant.get(
    tenantid="tenantid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenantid:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tenant.<a href="src/fern/tenant/client.py">create</a>(...) -> Tenant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul><li>Register a data partition in seismic-dms.</li><li>Required roles: users.datalake.admin</li></ul>
</dd>
</dl>
</dd>
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

client.tenant.create(
    tenantid="tenantid",
    gcpid="datapartition",
    esd="{datapartition}.{domain}.com",
    default_acls="users.datalake.admins@{datapartition}.{domain}.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tenantid:** `str` — Name of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**gcpid:** `str` — Google cloud project id associated with the tenant. For other providers, name of the data partition.
    
</dd>
</dl>

<dl>
<dd>

**esd:** `str` — Entitlements group Sub Domain (ESD). For instance, if the entitlements group is users.datalake.viewers@{datapartition}.{domain}.com, the esd value is {datapartition}.{domain}.com. It must start with the name of the data partition.
    
</dd>
</dl>

<dl>
<dd>

**default_acls:** `str` — Entitlements authorization group to manage tenant administrators.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TenantObsolete
<details><summary><code>client.tenant_obsolete.<a href="src/fern/tenant_obsolete/client.py">tenant_sdpath</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul><li>Return the seistore path to a tenant associated with the data partition.</li><li>Required roles: none</li></ul>
</dd>
</dl>
</dd>
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

client.tenant_obsolete.tenant_sdpath(
    datapartition="datapartition",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**datapartition:** `str` — Datapartition of the tenant.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users
<details><summary><code>client.users.<a href="src/fern/users/client.py">user_list</a>(...) -> typing.List[typing.List[str]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul><li>List users in subproject's role-based authorization groups.</li><li>Required roles: subproject.admin</li></ul>
</dd>
</dl>
</dd>
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

client.users.user_list(
    sdpath="sdpath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sdpath:** `str` — Seismic store path, sd://tenant/sub-project.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">user_add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul><li>Add a user to a subproject default authorization group if it exists, otherwise, add the user to the first group.</li><li>Required roles: subproject.admin</li></ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.users import UserAddRequestGroup

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.user_add(
    email="test@slb.com",
    path="sd://slb/test_project",
    group=UserAddRequestGroup.EDITOR,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — Email address of the user. Note that this field is used as a principal identifer for entitlements-svc and be configured using the env variable USER_ID_CLAIM_FOR_ENTITLEMENTS_SVC in the Seismic DMS runtime.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Seismic store path in the format sd://tenant/subproject.
    
</dd>
</dl>

<dl>
<dd>

**group:** `UserAddRequestGroup` — Role to be assigned to the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">user_rm</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul><li>Remove a user from subproject default authorization groups if exists, otherwise, remove it from the first authorization group.</li><li>Required roles: subproject.admin</li></ul>
</dd>
</dl>
</dd>
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

client.users.user_rm(
    email="email",
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — Email of the user to remove.
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Path of the subproject.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">user_roles</a>(...) -> UserRoles</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul><li>Retrieve user role in all subprojects of the tenant.</li><li>Required roles: none/li></ul>
</dd>
</dl>
</dd>
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

client.users.user_roles(
    sdpath="sdpath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sdpath:** `str` — Seismic store tenant path, sd://tenant.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.apps.<a href="src/fern/apps/client.py">app_list</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
<li>Retrieve the list of the registered applications in the seismic store.</li>
<li>Required roles: users.datalake.admin</li></ul>
</dd>
</dl>
</dd>
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

client.apps.app_list(
    sdpath="sdpath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sdpath:** `str` — Seismic store tenant path, sd://tenant.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apps.<a href="src/fern/apps/client.py">app_register</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul><li>Register a new application in the seismic store.</li><li>Required roles: users.datalake.admin</li></ul>
</dd>
</dl>
</dd>
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

client.apps.app_register(
    email="email",
    sdpath="sdpath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — Service account email of the application.
    
</dd>
</dl>

<dl>
<dd>

**sdpath:** `str` — Seismic store tenant path, sd://tenant.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apps.<a href="src/fern/apps/client.py">trustedapp_list</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
<li>Return the list of the trusted application in seismic store tenant.
</li><li>Required roles: users.datalake.admin</li></ul>
</dd>
</dl>
</dd>
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

client.apps.trustedapp_list(
    sdpath="sdpath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sdpath:** `str` — Seismic store tenant path in the format sd://tenant.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.apps.<a href="src/fern/apps/client.py">trustedapp_register</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<ul>
<li>Set a registered application as a trusted application in the seismic store.</li>
<li>Required roles: users.datalake.admin</li></ul>
</dd>
</dl>
</dd>
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

client.apps.trustedapp_register(
    email="email",
    sdpath="sdpath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — Service account email of the application.
    
</dd>
</dl>

<dl>
<dd>

**sdpath:** `str` — Seismic store tenant path, sd://tenant.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

