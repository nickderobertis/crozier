# Fern Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=Fern%2FPython)
[![pypi](https://img.shields.io/pypi/v/fern)](https://pypi.python.org/pypi/fern)

The Fern Python library provides convenient access to the Fern APIs from Python.

## Table of Contents

- [Installation](#installation)
- [Reference](#reference)
- [Usage](#usage)
- [Environments](#environments)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [Contributing](#contributing)

## Installation

```sh
pip install fern
```

## Reference

A full reference for this library is available [here](./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from fern import FernApi
from fern.dataset import DatasetRegisterBodySeismicmeta, DatasetRegisterBodyOpenzgyV1, DatasetRegisterBodyOpenzgyV1Acl, DatasetRegisterBodyOpenzgyV1Legal, DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureId, DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureIdKind, DatasetRegisterBodyOpenzgyV1Data, DatasetRegisterBodyOpenzgyV1DataEndian, DatasetRegisterBodyOpenzgyV1DataDatasetProperties, DatasetRegisterBodyOpenzgyV1DataDatasetPropertiesFileSourceInfosItem, DatasetRegisterBodySegyV1, DatasetRegisterBodySegyV1Acl, DatasetRegisterBodySegyV1Legal, DatasetRegisterBodySegyV1Ancestry, DatasetRegisterBodySegyV1MetaItemUnitOfMeasureId, DatasetRegisterBodySegyV1MetaItemUnitOfMeasureIdKind, DatasetRegisterBodySegyV1Data, DatasetRegisterBodySegyV1DataEndian, DatasetRegisterBodySegyV1DataDatasetProperties, DatasetRegisterBodySegyV1DataDatasetPropertiesFileSourceInfosItem, DatasetRegisterBodySegyV1DataVectorHeaderMappingItem, DatasetRegisterBodySegyV1DataVectorHeaderMappingItemScalarIndicator, DatasetRegisterBodyAcls
import datetime

client = FernApi(
    api_key="<value>",
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

## Environments

This SDK allows you to configure different environments for API requests.

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio
from fern.dataset import DatasetRegisterBodySeismicmeta, DatasetRegisterBodyOpenzgyV1, DatasetRegisterBodyOpenzgyV1Acl, DatasetRegisterBodyOpenzgyV1Legal, DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureId, DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureIdKind, DatasetRegisterBodyOpenzgyV1Data, DatasetRegisterBodyOpenzgyV1DataEndian, DatasetRegisterBodyOpenzgyV1DataDatasetProperties, DatasetRegisterBodyOpenzgyV1DataDatasetPropertiesFileSourceInfosItem, DatasetRegisterBodySegyV1, DatasetRegisterBodySegyV1Acl, DatasetRegisterBodySegyV1Legal, DatasetRegisterBodySegyV1Ancestry, DatasetRegisterBodySegyV1MetaItemUnitOfMeasureId, DatasetRegisterBodySegyV1MetaItemUnitOfMeasureIdKind, DatasetRegisterBodySegyV1Data, DatasetRegisterBodySegyV1DataEndian, DatasetRegisterBodySegyV1DataDatasetProperties, DatasetRegisterBodySegyV1DataDatasetPropertiesFileSourceInfosItem, DatasetRegisterBodySegyV1DataVectorHeaderMappingItem, DatasetRegisterBodySegyV1DataVectorHeaderMappingItemScalarIndicator, DatasetRegisterBodyAcls
import datetime

from fern import AsyncFernApi

client = AsyncFernApi(
    api_key="<value>",
)


async def main() -> None:
    await client.dataset.register(
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


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from fern.core.api_error import ApiError

try:
    client.dataset.register(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from fern import FernApi

client = FernApi(...)
response = client.dataset.with_raw_response.register(...)
print(response.headers)  # access the response headers
print(response.status_code)  # access the response status code
print(response.data)  # access the underlying object
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

Which status codes are retried depends on the `retryStatusCodes` generator configuration:

**`legacy`** (current default): retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses) (All server errors, including 500)

**`recommended`**: retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [502](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502) (Bad Gateway)
- [503](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503) (Service Unavailable)
- [504](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/504) (Gateway Timeout)

Use the `max_retries` request option to configure this behavior.

```python
client.dataset.register(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python
from fern import FernApi

client = FernApi(..., timeout=20.0)

# Override timeout for a specific method
client.dataset.register(..., request_options={
    "timeout": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from fern import FernApi

client = FernApi(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
