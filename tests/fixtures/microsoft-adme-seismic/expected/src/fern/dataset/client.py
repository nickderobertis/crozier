

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dataset import Dataset
from ..types.dataset_and_directories import DatasetAndDirectories
from ..types.dataset_permission import DatasetPermission
from ..types.dataset_size import DatasetSize
from ..types.paginated_datasets import PaginatedDatasets
from .raw_client import AsyncRawDatasetClient, RawDatasetClient
from .types.dataset_patch_acls import DatasetPatchAcls
from .types.dataset_patch_openzgy_v1 import DatasetPatchOpenzgyV1
from .types.dataset_patch_segy_v1 import DatasetPatchSegyV1
from .types.dataset_patch_seismicmeta import DatasetPatchSeismicmeta
from .types.dataset_register_body_acls import DatasetRegisterBodyAcls
from .types.dataset_register_body_openzgy_v1 import DatasetRegisterBodyOpenzgyV1
from .types.dataset_register_body_segy_v1 import DatasetRegisterBodySegyV1
from .types.dataset_register_body_seismicmeta import DatasetRegisterBodySeismicmeta


OMIT = typing.cast(typing.Any, ...)


class DatasetClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDatasetClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDatasetClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDatasetClient
        """
        return self._raw_client

    def get(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        seismicmeta: typing.Optional[bool] = None,
        translate_user_info: typing.Optional[bool] = None,
        record_version: typing.Optional[str] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
        <ul> <li>Return the dataset metadata from seismic store.</li> <li>Required roles: <ul> <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li> <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li> </ul> </li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        seismicmeta : typing.Optional[bool]
            Include the seismic storage metadata record if it exists.

        translate_user_info : typing.Optional[bool]
            translate the user-id to a more human readable user info

        record_version : typing.Optional[str]
            Retrieve a specific version of the seismic storage metadata record

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset
            Metadata of the dataset.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.dataset.get(
            tenantid="tenantid",
            subprojectid="subprojectid",
            datasetid="datasetid",
            path="path",
        )
        """
        _response = self._raw_client.get(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            seismicmeta=seismicmeta,
            translate_user_info=translate_user_info,
            record_version=record_version,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    def register(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        ltag: typing.Optional[str] = None,
        type: typing.Optional[str] = OMIT,
        gtags: typing.Optional[typing.Sequence[str]] = OMIT,
        seismicmeta: typing.Optional[DatasetRegisterBodySeismicmeta] = OMIT,
        openzgy_v1: typing.Optional[DatasetRegisterBodyOpenzgyV1] = OMIT,
        segy_v1: typing.Optional[DatasetRegisterBodySegyV1] = OMIT,
        acls: typing.Optional[DatasetRegisterBodyAcls] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
        <ul><li>Register a new dataset in the seismic store.</li><li>Required roles: subproject.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        ltag : typing.Optional[str]
            Legal tag of the dataset.

        type : typing.Optional[str]

        gtags : typing.Optional[typing.Sequence[str]]
            Array of global tags associated with the dataset metadata. Once assigned, they can be used to filter datasets.

        seismicmeta : typing.Optional[DatasetRegisterBodySeismicmeta]
            Seismic metadata to be stored as dataecosystem storage record.

        openzgy_v1 : typing.Optional[DatasetRegisterBodyOpenzgyV1]
            The dataset representation for optimized seismic access to the OpenZGY framework developed by Schlumberger, storing seismic 3D data for seismic interpretation.

        segy_v1 : typing.Optional[DatasetRegisterBodySegyV1]
            A generic representation for  SEGY dataset represented as set of files, e.g. representing original tape reels.

        acls : typing.Optional[DatasetRegisterBodyAcls]
            ACLs with admin groups and viewer groups for the dataset.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset
            Registered dataset metadata.

        Examples
        --------
        import datetime

        from fern.dataset import (
            DatasetRegisterBodyAcls,
            DatasetRegisterBodyOpenzgyV1,
            DatasetRegisterBodyOpenzgyV1Acl,
            DatasetRegisterBodyOpenzgyV1Data,
            DatasetRegisterBodyOpenzgyV1DataDatasetProperties,
            DatasetRegisterBodyOpenzgyV1DataDatasetPropertiesFileSourceInfosItem,
            DatasetRegisterBodyOpenzgyV1DataEndian,
            DatasetRegisterBodyOpenzgyV1Legal,
            DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureId,
            DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureIdKind,
            DatasetRegisterBodySegyV1,
            DatasetRegisterBodySegyV1Acl,
            DatasetRegisterBodySegyV1Ancestry,
            DatasetRegisterBodySegyV1Data,
            DatasetRegisterBodySegyV1DataDatasetProperties,
            DatasetRegisterBodySegyV1DataDatasetPropertiesFileSourceInfosItem,
            DatasetRegisterBodySegyV1DataEndian,
            DatasetRegisterBodySegyV1DataVectorHeaderMappingItem,
            DatasetRegisterBodySegyV1DataVectorHeaderMappingItemScalarIndicator,
            DatasetRegisterBodySegyV1Legal,
            DatasetRegisterBodySegyV1MetaItemUnitOfMeasureId,
            DatasetRegisterBodySegyV1MetaItemUnitOfMeasureIdKind,
            DatasetRegisterBodySeismicmeta,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.dataset.register(
            tenantid="tenantid",
            subprojectid="subprojectid",
            datasetid="datasetid",
            path="path",
            gtags=["tagA", "tagB", "tagC"],
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
                    legaltags=["opendes-seistore-test-01"],
                    other_relevant_data_countries=["US"],
                    status="compliant",
                ),
                tags={"NameOfKey": "String value"},
                create_time=datetime.datetime.fromisoformat(
                    "2021-11-16 02:08:16+00:00",
                ),
                create_user="vmanohar@slb.com",
                modify_time=datetime.datetime.fromisoformat(
                    "2021-11-18 04:10:23+00:00",
                ),
                modify_user="39916b94-71a9-409e-856e-0f29558fa908",
                meta=[
                    DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureId(
                        kind=DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureIdKind.UNIT,
                        persistable_reference='{"abcd":{"a":0.0,"b":1200.0,"c":3937.0,"d":0.0},"symbol":"ft[US]","baseMeasurement":{"ancestry":"L","type":"UM"},"type":"UAD"}',
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
                                preload_file_create_date=datetime.datetime.fromisoformat(
                                    "2019-12-16 11:46:20+00:00",
                                ),
                                preload_file_modify_user="somebody.else@acme.org",
                                preload_file_modify_date=datetime.datetime.fromisoformat(
                                    "2019-12-20 17:20:05+00:00",
                                ),
                                name="vds-file-1",
                                file_size="439452464",
                                checksum="checksum-value",
                                checksum_algorithm="MD5",
                            ),
                            DatasetRegisterBodyOpenzgyV1DataDatasetPropertiesFileSourceInfosItem(
                                file_source="s3://default_bucket/opendes/data/vds-dataset/vds-file-2",
                                preload_file_path="s3://staging-area/r7/raw-data/provided/documents/vds-file-2",
                                preload_file_create_user="somebody@acme.org",
                                preload_file_create_date=datetime.datetime.fromisoformat(
                                    "2019-12-16 11:50:40+00:00",
                                ),
                                preload_file_modify_user="somebody.else@acme.org",
                                preload_file_modify_date=datetime.datetime.fromisoformat(
                                    "2019-12-20 17:59:03+00:00",
                                ),
                                name="vds-file-2",
                                file_size="433645463",
                                checksum="checksum-value",
                                checksum_algorithm="MD5",
                            ),
                        ],
                        checksum="checksum-value",
                    ),
                    extension_properties={"key": "value"},
                ),
            ),
            segy_v1=DatasetRegisterBodySegyV1(
                id="osdu:dataset--FileCollection.SEGY:b47f793a-dc9c-5d11-8d59-6cc611a98926",
                kind="osdu:wks:dataset--FileCollection.SEGY:1.0.0",
                version=1562066009929332,
                acl=DatasetRegisterBodySegyV1Acl(
                    owners=["someone@company.com"],
                    viewers=["someone@company.com"],
                ),
                legal=DatasetRegisterBodySegyV1Legal(
                    legaltags=["Example legaltags"],
                    other_relevant_data_countries=["US"],
                    status="compliant",
                ),
                tags={"NameOfKey": "String value"},
                create_time=datetime.datetime.fromisoformat(
                    "2020-12-16 11:46:20+00:00",
                ),
                create_user="some-user@some-company-cloud.com",
                modify_time=datetime.datetime.fromisoformat(
                    "2020-12-16 11:52:24+00:00",
                ),
                modify_user="some-user@some-company-cloud.com",
                ancestry=DatasetRegisterBodySegyV1Ancestry(
                    parents=["parents"],
                ),
                meta=[
                    DatasetRegisterBodySegyV1MetaItemUnitOfMeasureId(
                        kind=DatasetRegisterBodySegyV1MetaItemUnitOfMeasureIdKind.UNIT,
                        persistable_reference='{"abcd":{"a":0.0,"b":1200.0,"c":3937.0,"d":0.0},"symbol":"ft[US]","baseMeasurement":{"ancestry":"L","type":"UM"},"type":"UAD"}',
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
                                preload_file_create_date=datetime.datetime.fromisoformat(
                                    "2019-12-16 11:46:20+00:00",
                                ),
                                preload_file_modify_user="somebody.else@acme.org",
                                preload_file_modify_date=datetime.datetime.fromisoformat(
                                    "2019-12-20 17:20:05+00:00",
                                ),
                                name="vds-file-1",
                                file_size="439452464",
                                checksum="checksum-value",
                                checksum_algorithm="MD5",
                            ),
                            DatasetRegisterBodySegyV1DataDatasetPropertiesFileSourceInfosItem(
                                file_source="s3://default_bucket/opendes/data/vds-dataset/vds-file-2",
                                preload_file_path="s3://staging-area/r7/raw-data/provided/documents/vds-file-2",
                                preload_file_create_user="somebody@acme.org",
                                preload_file_create_date=datetime.datetime.fromisoformat(
                                    "2019-12-16 11:50:40+00:00",
                                ),
                                preload_file_modify_user="somebody.else@acme.org",
                                preload_file_modify_date=datetime.datetime.fromisoformat(
                                    "2019-12-20 17:59:03+00:00",
                                ),
                                name="vds-file-2",
                                file_size="433645463",
                                checksum="checksum-value",
                                checksum_algorithm="MD5",
                            ),
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
                    extension_properties={"key": "value"},
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
        """
        _response = self._raw_client.register(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            impersonation_token_context=impersonation_token_context,
            ltag=ltag,
            type=type,
            gtags=gtags,
            seismicmeta=seismicmeta,
            openzgy_v1=openzgy_v1,
            segy_v1=segy_v1,
            acls=acls,
            request_options=request_options,
        )
        return _response.data

    def delete(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        <ul> <li>Delete a dataset in the seismic store.</li> <li>Required roles: <ul> <li>subproject.admin: if the applied subproject policy is 'uniform'</li> <li>dataset.admin: if the applied subproject policy is 'dataset'</li> </ul> </li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.dataset.delete(
            tenantid="tenantid",
            subprojectid="subprojectid",
            datasetid="datasetid",
            path="path",
        )
        """
        _response = self._raw_client.delete(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    def patch(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        close: typing.Optional[str] = None,
        impersonation_token_context: typing.Optional[str] = None,
        dataset_new_name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        filemetadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        last_modified_date: typing.Optional[str] = OMIT,
        gtags: typing.Optional[typing.Sequence[str]] = OMIT,
        ltag: typing.Optional[str] = OMIT,
        readonly: typing.Optional[bool] = OMIT,
        seismicmeta: typing.Optional[DatasetPatchSeismicmeta] = OMIT,
        openzgy_v1: typing.Optional[DatasetPatchOpenzgyV1] = OMIT,
        segy_v1: typing.Optional[DatasetPatchSegyV1] = OMIT,
        acls: typing.Optional[DatasetPatchAcls] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
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

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        close : typing.Optional[str]
            Non null sbit value of the dataset. Using this value here will close the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        dataset_new_name : typing.Optional[str]
            New name for the dataset.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Generic information about the dataset stored as key value pairs.

        filemetadata : typing.Optional[typing.Dict[str, typing.Any]]
            Number of objects and the size in bytes of the dataset.

        last_modified_date : typing.Optional[str]
            Date when the dataset was last modified.

        gtags : typing.Optional[typing.Sequence[str]]
            Array of tags associated with the dataset. After patching these tags, they can be used to filter the datasets.

        ltag : typing.Optional[str]
            Legal tag associated with the dataset.

        readonly : typing.Optional[bool]
            True if the dataset is read only.

        seismicmeta : typing.Optional[DatasetPatchSeismicmeta]
            Seismic metadata associated with the dataset which is used to create a data ecosystem storage record.

        openzgy_v1 : typing.Optional[DatasetPatchOpenzgyV1]
            The dataset representation for optimized seismic access to the OpenZGY framework developed by Schlumberger, storing seismic 3D data for seismic interpretation.

        segy_v1 : typing.Optional[DatasetPatchSegyV1]
            A generic representation for  SEGY dataset represented as set of files, e.g. representing original tape reels.

        acls : typing.Optional[DatasetPatchAcls]
            ACLs with admin groups and viewer groups for the dataset.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset
            Metadata of the patched dataset.

        Examples
        --------
        import datetime

        from fern.dataset import (
            DatasetPatchAcls,
            DatasetPatchOpenzgyV1,
            DatasetPatchOpenzgyV1Acl,
            DatasetPatchOpenzgyV1Data,
            DatasetPatchOpenzgyV1DataDatasetProperties,
            DatasetPatchOpenzgyV1DataDatasetPropertiesFileSourceInfosItem,
            DatasetPatchOpenzgyV1DataEndian,
            DatasetPatchOpenzgyV1Legal,
            DatasetPatchOpenzgyV1MetaItemUnitOfMeasureId,
            DatasetPatchOpenzgyV1MetaItemUnitOfMeasureIdKind,
            DatasetPatchSegyV1,
            DatasetPatchSegyV1Acl,
            DatasetPatchSegyV1Ancestry,
            DatasetPatchSegyV1Data,
            DatasetPatchSegyV1DataDatasetProperties,
            DatasetPatchSegyV1DataDatasetPropertiesFileSourceInfosItem,
            DatasetPatchSegyV1DataEndian,
            DatasetPatchSegyV1DataVectorHeaderMappingItem,
            DatasetPatchSegyV1DataVectorHeaderMappingItemScalarIndicator,
            DatasetPatchSegyV1Legal,
            DatasetPatchSegyV1MetaItemUnitOfMeasureId,
            DatasetPatchSegyV1MetaItemUnitOfMeasureIdKind,
            DatasetPatchSeismicmeta,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.dataset.patch(
            tenantid="tenantid",
            subprojectid="subprojectid",
            datasetid="datasetid",
            path="path",
            dataset_new_name="dsx02",
            metadata={"f1": "v1", "f2": "v2", "f3": "v3"},
            filemetadata={"f1": "v1", "f2": "v2", "f3": "v3"},
            last_modified_date="Thu Jul 16 2020 04:37:41 GMT+0000 (Coordinated Universal Time)",
            gtags=["tag01", "tag02", "tag03"],
            ltag="legal-tag",
            readonly=False,
            seismicmeta=DatasetPatchSeismicmeta(
                kind="slb:seistore:seismic2d:1.0.0",
                data={"msg": "sample data"},
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
                    legaltags=["opendes-seistore-test-01"],
                    other_relevant_data_countries=["US"],
                    status="compliant",
                ),
                tags={"NameOfKey": "String value"},
                create_time=datetime.datetime.fromisoformat(
                    "2021-11-16 02:08:16+00:00",
                ),
                create_user="vmanohar@slb.com",
                modify_time=datetime.datetime.fromisoformat(
                    "2021-11-18 04:10:23+00:00",
                ),
                modify_user="39916b94-71a9-409e-856e-0f29558fa908",
                meta=[
                    DatasetPatchOpenzgyV1MetaItemUnitOfMeasureId(
                        kind=DatasetPatchOpenzgyV1MetaItemUnitOfMeasureIdKind.UNIT,
                        persistable_reference='{"abcd":{"a":0.0,"b":1200.0,"c":3937.0,"d":0.0},"symbol":"ft[US]","baseMeasurement":{"ancestry":"L","type":"UM"},"type":"UAD"}',
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
                                preload_file_create_date=datetime.datetime.fromisoformat(
                                    "2019-12-16 11:46:20+00:00",
                                ),
                                preload_file_modify_user="somebody.else@acme.org",
                                preload_file_modify_date=datetime.datetime.fromisoformat(
                                    "2019-12-20 17:20:05+00:00",
                                ),
                                name="vds-file-1",
                                file_size="439452464",
                                checksum="checksum-value",
                                checksum_algorithm="MD5",
                            ),
                            DatasetPatchOpenzgyV1DataDatasetPropertiesFileSourceInfosItem(
                                file_source="s3://default_bucket/opendes/data/vds-dataset/vds-file-2",
                                preload_file_path="s3://staging-area/r7/raw-data/provided/documents/vds-file-2",
                                preload_file_create_user="somebody@acme.org",
                                preload_file_create_date=datetime.datetime.fromisoformat(
                                    "2019-12-16 11:50:40+00:00",
                                ),
                                preload_file_modify_user="somebody.else@acme.org",
                                preload_file_modify_date=datetime.datetime.fromisoformat(
                                    "2019-12-20 17:59:03+00:00",
                                ),
                                name="vds-file-2",
                                file_size="433645463",
                                checksum="checksum-value",
                                checksum_algorithm="MD5",
                            ),
                        ],
                        checksum="checksum-value",
                    ),
                    extension_properties={"key": "value"},
                ),
            ),
            segy_v1=DatasetPatchSegyV1(
                id="osdu:dataset--FileCollection.SEGY:b47f793a-dc9c-5d11-8d59-6cc611a98926",
                kind="osdu:wks:dataset--FileCollection.SEGY:1.0.0",
                version=1562066009929332,
                acl=DatasetPatchSegyV1Acl(
                    owners=["someone@company.com"],
                    viewers=["someone@company.com"],
                ),
                legal=DatasetPatchSegyV1Legal(
                    legaltags=["Example legaltags"],
                    other_relevant_data_countries=["US"],
                    status="compliant",
                ),
                tags={"NameOfKey": "String value"},
                create_time=datetime.datetime.fromisoformat(
                    "2020-12-16 11:46:20+00:00",
                ),
                create_user="some-user@some-company-cloud.com",
                modify_time=datetime.datetime.fromisoformat(
                    "2020-12-16 11:52:24+00:00",
                ),
                modify_user="some-user@some-company-cloud.com",
                ancestry=DatasetPatchSegyV1Ancestry(
                    parents=["parents"],
                ),
                meta=[
                    DatasetPatchSegyV1MetaItemUnitOfMeasureId(
                        kind=DatasetPatchSegyV1MetaItemUnitOfMeasureIdKind.UNIT,
                        persistable_reference='{"abcd":{"a":0.0,"b":1200.0,"c":3937.0,"d":0.0},"symbol":"ft[US]","baseMeasurement":{"ancestry":"L","type":"UM"},"type":"UAD"}',
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
                                preload_file_create_date=datetime.datetime.fromisoformat(
                                    "2019-12-16 11:46:20+00:00",
                                ),
                                preload_file_modify_user="somebody.else@acme.org",
                                preload_file_modify_date=datetime.datetime.fromisoformat(
                                    "2019-12-20 17:20:05+00:00",
                                ),
                                name="vds-file-1",
                                file_size="439452464",
                                checksum="checksum-value",
                                checksum_algorithm="MD5",
                            ),
                            DatasetPatchSegyV1DataDatasetPropertiesFileSourceInfosItem(
                                file_source="s3://default_bucket/opendes/data/vds-dataset/vds-file-2",
                                preload_file_path="s3://staging-area/r7/raw-data/provided/documents/vds-file-2",
                                preload_file_create_user="somebody@acme.org",
                                preload_file_create_date=datetime.datetime.fromisoformat(
                                    "2019-12-16 11:50:40+00:00",
                                ),
                                preload_file_modify_user="somebody.else@acme.org",
                                preload_file_modify_date=datetime.datetime.fromisoformat(
                                    "2019-12-20 17:59:03+00:00",
                                ),
                                name="vds-file-2",
                                file_size="433645463",
                                checksum="checksum-value",
                                checksum_algorithm="MD5",
                            ),
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
                    extension_properties={"key": "value"},
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
        """
        _response = self._raw_client.patch(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            close=close,
            impersonation_token_context=impersonation_token_context,
            dataset_new_name=dataset_new_name,
            metadata=metadata,
            filemetadata=filemetadata,
            last_modified_date=last_modified_date,
            gtags=gtags,
            ltag=ltag,
            readonly=readonly,
            seismicmeta=seismicmeta,
            openzgy_v1=openzgy_v1,
            segy_v1=segy_v1,
            acls=acls,
            request_options=request_options,
        )
        return _response.data

    def acquire_a_lock_for_a_dataset_id(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        openmode: typing.Optional[str] = None,
        wid: typing.Optional[float] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
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

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        openmode : typing.Optional[str]
            Type of the lock which can be set to 'read' (default) or 'write'.

        wid : typing.Optional[float]
            Session identifier issued for a previous write lock acquisition operation.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset
            Acquired a lock and the return value is the dataset metadata with session identifier stored in the 'sbit' attribute.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.dataset.acquire_a_lock_for_a_dataset_id(
            tenantid="tenantid",
            subprojectid="subprojectid",
            datasetid="datasetid",
            path="path",
        )
        """
        _response = self._raw_client.acquire_a_lock_for_a_dataset_id(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            openmode=openmode,
            wid=wid,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    def lock_rm(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        <ul>
          <li>Removes the lock for a dataset id.</li>
          <li>Required roles:
            <ul>
              <li>subproject.admin: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path for the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.dataset.lock_rm(
            tenantid="tenantid",
            subprojectid="subprojectid",
            datasetid="datasetid",
            path="path",
        )
        """
        _response = self._raw_client.lock_rm(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    def permission(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetPermission:
        """
        <ul>
          <li>Retrieve the access permission of a user on a dataset.</li>
          <li>Required roles:
            <ul>
              <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path for the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetPermission
            User access permission on the dataset.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.dataset.permission(
            tenantid="tenantid",
            subprojectid="subprojectid",
            datasetid="datasetid",
            path="path",
        )
        """
        _response = self._raw_client.permission(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    def ctag_check(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        ctag: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        <ul><li>Check if the provided dataset cTag match the one stored in the metadata catalog.</li><li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        ctag : str
            Ctag to be validated.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Return true if the ctag is valid or false if it is invalid.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.dataset.ctag_check(
            tenantid="tenantid",
            subprojectid="subprojectid",
            datasetid="datasetid",
            path="path",
            ctag="ctag",
        )
        """
        _response = self._raw_client.ctag_check(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            ctag=ctag,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    def add_tag(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        gtag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        <ul>
          <li>Upsert tags to an existing dataset metadata. If the dataset metadata already has gtags, then  new gtags are appended to this list.</li>
          <li>Required roles:
            <ul>
              <li>subproject.admin: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        gtag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Gtags array list.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.dataset.add_tag(
            tenantid="tenantid",
            subprojectid="subprojectid",
            datasetid="datasetid",
            path="path",
            gtag=["gtag"],
        )
        """
        _response = self._raw_client.add_tag(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            gtag=gtag,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    def size(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetSize:
        """
        <ul>
        <li>Compute and retrieve the size of a dataset and the date of when the size was computed.</li>
        <li>Required roles: subproject.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetSize
            Size of the dataset and the date of when the size was computed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.dataset.size(
            tenantid="tenantid",
            subprojectid="subprojectid",
            datasetid="datasetid",
            path="path",
        )
        """
        _response = self._raw_client.size(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    def read_directory(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetAndDirectories:
        """
        <ul>
        <li>List datasets and sub-directories for a directory path.</li>
        <li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        tenantid : str
            The tenant project name.

        subprojectid : str
            The sub-project name.

        path : str
            The hierarchy path.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetAndDirectories
            The list of datasets and directories in the requested directory path.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.dataset.read_directory(
            tenantid="tenantid",
            subprojectid="subprojectid",
            path="path",
        )
        """
        _response = self._raw_client.read_directory(
            tenantid,
            subprojectid,
            path=path,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    def list(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        gtag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        translate_user_info: typing.Optional[bool] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDatasets:
        """
        <ul>
          <li>Return the list of datasets in a sub-project. The list can be filtered by gtags. Support pagination.</li>
          <li>Required roles: subproject.admin, subproject.viewer</li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        gtag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Gtags associated with dataset metadata.

        limit : typing.Optional[str]
            Limit the number of datasets in the response

        cursor : typing.Optional[str]
            Cursor for pagination on the datasets list

        translate_user_info : typing.Optional[bool]
            translate the user-id to a more human readable user info

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDatasets
            Paginated dataset list with nextPageCursor. If the request does not provide limit or cursor the results will be the whole path conent and the response is a plain array of datasets [ {dataset1}, {datase2}, ... ]

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.dataset.list(
            tenantid="tenantid",
            subprojectid="subprojectid",
        )
        """
        _response = self._raw_client.list(
            tenantid,
            subprojectid,
            gtag=gtag,
            limit=limit,
            cursor=cursor,
            translate_user_info=translate_user_info,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    def list_post(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        translate_user_info: typing.Optional[bool] = None,
        impersonation_token_context: typing.Optional[str] = None,
        type: typing.Optional[str] = OMIT,
        gtags: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDatasets:
        """
        <ul>
          <li>Return the list of datasets in a sub-project. The list can be filtered by gtags. Support pagination.</li>
          <li>Required roles: subproject.admin, subproject.viewer</li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        translate_user_info : typing.Optional[bool]
            translate the user-id to a more human readable user info

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        type : typing.Optional[str]

        gtags : typing.Optional[typing.Sequence[str]]
            Array of global tags associated with the dataset metadata. Once assigned, they can be used to filter datasets.

        limit : typing.Optional[float]
            the max limit of datasets in the response

        cursor : typing.Optional[str]
            the cursor value required to retrieve the next page of result

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDatasets
            Paginated dataset list with nextPageCursor. If the request does not provide limit or cursor the results will be the whole path conent and the response is a plain array of datasets [ {dataset1}, {datase2}, ... ]

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.dataset.list_post(
            tenantid="tenantid",
            subprojectid="subprojectid",
            gtags=["tagA", "tagB"],
            limit=10.0,
            cursor="next-page-token-931fvm19vm1-vm1v1",
        )
        """
        _response = self._raw_client.list_post(
            tenantid,
            subprojectid,
            translate_user_info=translate_user_info,
            impersonation_token_context=impersonation_token_context,
            type=type,
            gtags=gtags,
            limit=limit,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data

    def exist(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        datasets: typing.Sequence[str],
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[bool]:
        """
        <ul>
        <li>Check if the dataset exists.</li>
        <li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasets : typing.Sequence[str]
            Array of datasets inside the subproject.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[bool]
            A list of Boolean values for all the input datasets in the request body. If a value is true, then the corresponding dataset exists and if it is false, then the dataset does not exist.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.dataset.exist(
            tenantid="tenantid",
            subprojectid="subprojectid",
            datasets=["a/b/c/dsx01", "a/b/c/dsx02"],
        )
        """
        _response = self._raw_client.exist(
            tenantid,
            subprojectid,
            datasets=datasets,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data


class AsyncDatasetClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDatasetClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDatasetClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDatasetClient
        """
        return self._raw_client

    async def get(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        seismicmeta: typing.Optional[bool] = None,
        translate_user_info: typing.Optional[bool] = None,
        record_version: typing.Optional[str] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
        <ul> <li>Return the dataset metadata from seismic store.</li> <li>Required roles: <ul> <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li> <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li> </ul> </li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        seismicmeta : typing.Optional[bool]
            Include the seismic storage metadata record if it exists.

        translate_user_info : typing.Optional[bool]
            translate the user-id to a more human readable user info

        record_version : typing.Optional[str]
            Retrieve a specific version of the seismic storage metadata record

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset
            Metadata of the dataset.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dataset.get(
                tenantid="tenantid",
                subprojectid="subprojectid",
                datasetid="datasetid",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            seismicmeta=seismicmeta,
            translate_user_info=translate_user_info,
            record_version=record_version,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    async def register(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        ltag: typing.Optional[str] = None,
        type: typing.Optional[str] = OMIT,
        gtags: typing.Optional[typing.Sequence[str]] = OMIT,
        seismicmeta: typing.Optional[DatasetRegisterBodySeismicmeta] = OMIT,
        openzgy_v1: typing.Optional[DatasetRegisterBodyOpenzgyV1] = OMIT,
        segy_v1: typing.Optional[DatasetRegisterBodySegyV1] = OMIT,
        acls: typing.Optional[DatasetRegisterBodyAcls] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
        <ul><li>Register a new dataset in the seismic store.</li><li>Required roles: subproject.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        ltag : typing.Optional[str]
            Legal tag of the dataset.

        type : typing.Optional[str]

        gtags : typing.Optional[typing.Sequence[str]]
            Array of global tags associated with the dataset metadata. Once assigned, they can be used to filter datasets.

        seismicmeta : typing.Optional[DatasetRegisterBodySeismicmeta]
            Seismic metadata to be stored as dataecosystem storage record.

        openzgy_v1 : typing.Optional[DatasetRegisterBodyOpenzgyV1]
            The dataset representation for optimized seismic access to the OpenZGY framework developed by Schlumberger, storing seismic 3D data for seismic interpretation.

        segy_v1 : typing.Optional[DatasetRegisterBodySegyV1]
            A generic representation for  SEGY dataset represented as set of files, e.g. representing original tape reels.

        acls : typing.Optional[DatasetRegisterBodyAcls]
            ACLs with admin groups and viewer groups for the dataset.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset
            Registered dataset metadata.

        Examples
        --------
        import asyncio
        import datetime

        from fern.dataset import (
            DatasetRegisterBodyAcls,
            DatasetRegisterBodyOpenzgyV1,
            DatasetRegisterBodyOpenzgyV1Acl,
            DatasetRegisterBodyOpenzgyV1Data,
            DatasetRegisterBodyOpenzgyV1DataDatasetProperties,
            DatasetRegisterBodyOpenzgyV1DataDatasetPropertiesFileSourceInfosItem,
            DatasetRegisterBodyOpenzgyV1DataEndian,
            DatasetRegisterBodyOpenzgyV1Legal,
            DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureId,
            DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureIdKind,
            DatasetRegisterBodySegyV1,
            DatasetRegisterBodySegyV1Acl,
            DatasetRegisterBodySegyV1Ancestry,
            DatasetRegisterBodySegyV1Data,
            DatasetRegisterBodySegyV1DataDatasetProperties,
            DatasetRegisterBodySegyV1DataDatasetPropertiesFileSourceInfosItem,
            DatasetRegisterBodySegyV1DataEndian,
            DatasetRegisterBodySegyV1DataVectorHeaderMappingItem,
            DatasetRegisterBodySegyV1DataVectorHeaderMappingItemScalarIndicator,
            DatasetRegisterBodySegyV1Legal,
            DatasetRegisterBodySegyV1MetaItemUnitOfMeasureId,
            DatasetRegisterBodySegyV1MetaItemUnitOfMeasureIdKind,
            DatasetRegisterBodySeismicmeta,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dataset.register(
                tenantid="tenantid",
                subprojectid="subprojectid",
                datasetid="datasetid",
                path="path",
                gtags=["tagA", "tagB", "tagC"],
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
                        legaltags=["opendes-seistore-test-01"],
                        other_relevant_data_countries=["US"],
                        status="compliant",
                    ),
                    tags={"NameOfKey": "String value"},
                    create_time=datetime.datetime.fromisoformat(
                        "2021-11-16 02:08:16+00:00",
                    ),
                    create_user="vmanohar@slb.com",
                    modify_time=datetime.datetime.fromisoformat(
                        "2021-11-18 04:10:23+00:00",
                    ),
                    modify_user="39916b94-71a9-409e-856e-0f29558fa908",
                    meta=[
                        DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureId(
                            kind=DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureIdKind.UNIT,
                            persistable_reference='{"abcd":{"a":0.0,"b":1200.0,"c":3937.0,"d":0.0},"symbol":"ft[US]","baseMeasurement":{"ancestry":"L","type":"UM"},"type":"UAD"}',
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
                                    preload_file_create_date=datetime.datetime.fromisoformat(
                                        "2019-12-16 11:46:20+00:00",
                                    ),
                                    preload_file_modify_user="somebody.else@acme.org",
                                    preload_file_modify_date=datetime.datetime.fromisoformat(
                                        "2019-12-20 17:20:05+00:00",
                                    ),
                                    name="vds-file-1",
                                    file_size="439452464",
                                    checksum="checksum-value",
                                    checksum_algorithm="MD5",
                                ),
                                DatasetRegisterBodyOpenzgyV1DataDatasetPropertiesFileSourceInfosItem(
                                    file_source="s3://default_bucket/opendes/data/vds-dataset/vds-file-2",
                                    preload_file_path="s3://staging-area/r7/raw-data/provided/documents/vds-file-2",
                                    preload_file_create_user="somebody@acme.org",
                                    preload_file_create_date=datetime.datetime.fromisoformat(
                                        "2019-12-16 11:50:40+00:00",
                                    ),
                                    preload_file_modify_user="somebody.else@acme.org",
                                    preload_file_modify_date=datetime.datetime.fromisoformat(
                                        "2019-12-20 17:59:03+00:00",
                                    ),
                                    name="vds-file-2",
                                    file_size="433645463",
                                    checksum="checksum-value",
                                    checksum_algorithm="MD5",
                                ),
                            ],
                            checksum="checksum-value",
                        ),
                        extension_properties={"key": "value"},
                    ),
                ),
                segy_v1=DatasetRegisterBodySegyV1(
                    id="osdu:dataset--FileCollection.SEGY:b47f793a-dc9c-5d11-8d59-6cc611a98926",
                    kind="osdu:wks:dataset--FileCollection.SEGY:1.0.0",
                    version=1562066009929332,
                    acl=DatasetRegisterBodySegyV1Acl(
                        owners=["someone@company.com"],
                        viewers=["someone@company.com"],
                    ),
                    legal=DatasetRegisterBodySegyV1Legal(
                        legaltags=["Example legaltags"],
                        other_relevant_data_countries=["US"],
                        status="compliant",
                    ),
                    tags={"NameOfKey": "String value"},
                    create_time=datetime.datetime.fromisoformat(
                        "2020-12-16 11:46:20+00:00",
                    ),
                    create_user="some-user@some-company-cloud.com",
                    modify_time=datetime.datetime.fromisoformat(
                        "2020-12-16 11:52:24+00:00",
                    ),
                    modify_user="some-user@some-company-cloud.com",
                    ancestry=DatasetRegisterBodySegyV1Ancestry(
                        parents=["parents"],
                    ),
                    meta=[
                        DatasetRegisterBodySegyV1MetaItemUnitOfMeasureId(
                            kind=DatasetRegisterBodySegyV1MetaItemUnitOfMeasureIdKind.UNIT,
                            persistable_reference='{"abcd":{"a":0.0,"b":1200.0,"c":3937.0,"d":0.0},"symbol":"ft[US]","baseMeasurement":{"ancestry":"L","type":"UM"},"type":"UAD"}',
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
                                    preload_file_create_date=datetime.datetime.fromisoformat(
                                        "2019-12-16 11:46:20+00:00",
                                    ),
                                    preload_file_modify_user="somebody.else@acme.org",
                                    preload_file_modify_date=datetime.datetime.fromisoformat(
                                        "2019-12-20 17:20:05+00:00",
                                    ),
                                    name="vds-file-1",
                                    file_size="439452464",
                                    checksum="checksum-value",
                                    checksum_algorithm="MD5",
                                ),
                                DatasetRegisterBodySegyV1DataDatasetPropertiesFileSourceInfosItem(
                                    file_source="s3://default_bucket/opendes/data/vds-dataset/vds-file-2",
                                    preload_file_path="s3://staging-area/r7/raw-data/provided/documents/vds-file-2",
                                    preload_file_create_user="somebody@acme.org",
                                    preload_file_create_date=datetime.datetime.fromisoformat(
                                        "2019-12-16 11:50:40+00:00",
                                    ),
                                    preload_file_modify_user="somebody.else@acme.org",
                                    preload_file_modify_date=datetime.datetime.fromisoformat(
                                        "2019-12-20 17:59:03+00:00",
                                    ),
                                    name="vds-file-2",
                                    file_size="433645463",
                                    checksum="checksum-value",
                                    checksum_algorithm="MD5",
                                ),
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
                        extension_properties={"key": "value"},
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
        """
        _response = await self._raw_client.register(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            impersonation_token_context=impersonation_token_context,
            ltag=ltag,
            type=type,
            gtags=gtags,
            seismicmeta=seismicmeta,
            openzgy_v1=openzgy_v1,
            segy_v1=segy_v1,
            acls=acls,
            request_options=request_options,
        )
        return _response.data

    async def delete(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        <ul> <li>Delete a dataset in the seismic store.</li> <li>Required roles: <ul> <li>subproject.admin: if the applied subproject policy is 'uniform'</li> <li>dataset.admin: if the applied subproject policy is 'dataset'</li> </ul> </li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dataset.delete(
                tenantid="tenantid",
                subprojectid="subprojectid",
                datasetid="datasetid",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    async def patch(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        close: typing.Optional[str] = None,
        impersonation_token_context: typing.Optional[str] = None,
        dataset_new_name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        filemetadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        last_modified_date: typing.Optional[str] = OMIT,
        gtags: typing.Optional[typing.Sequence[str]] = OMIT,
        ltag: typing.Optional[str] = OMIT,
        readonly: typing.Optional[bool] = OMIT,
        seismicmeta: typing.Optional[DatasetPatchSeismicmeta] = OMIT,
        openzgy_v1: typing.Optional[DatasetPatchOpenzgyV1] = OMIT,
        segy_v1: typing.Optional[DatasetPatchSegyV1] = OMIT,
        acls: typing.Optional[DatasetPatchAcls] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
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

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        close : typing.Optional[str]
            Non null sbit value of the dataset. Using this value here will close the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        dataset_new_name : typing.Optional[str]
            New name for the dataset.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Generic information about the dataset stored as key value pairs.

        filemetadata : typing.Optional[typing.Dict[str, typing.Any]]
            Number of objects and the size in bytes of the dataset.

        last_modified_date : typing.Optional[str]
            Date when the dataset was last modified.

        gtags : typing.Optional[typing.Sequence[str]]
            Array of tags associated with the dataset. After patching these tags, they can be used to filter the datasets.

        ltag : typing.Optional[str]
            Legal tag associated with the dataset.

        readonly : typing.Optional[bool]
            True if the dataset is read only.

        seismicmeta : typing.Optional[DatasetPatchSeismicmeta]
            Seismic metadata associated with the dataset which is used to create a data ecosystem storage record.

        openzgy_v1 : typing.Optional[DatasetPatchOpenzgyV1]
            The dataset representation for optimized seismic access to the OpenZGY framework developed by Schlumberger, storing seismic 3D data for seismic interpretation.

        segy_v1 : typing.Optional[DatasetPatchSegyV1]
            A generic representation for  SEGY dataset represented as set of files, e.g. representing original tape reels.

        acls : typing.Optional[DatasetPatchAcls]
            ACLs with admin groups and viewer groups for the dataset.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset
            Metadata of the patched dataset.

        Examples
        --------
        import asyncio
        import datetime

        from fern.dataset import (
            DatasetPatchAcls,
            DatasetPatchOpenzgyV1,
            DatasetPatchOpenzgyV1Acl,
            DatasetPatchOpenzgyV1Data,
            DatasetPatchOpenzgyV1DataDatasetProperties,
            DatasetPatchOpenzgyV1DataDatasetPropertiesFileSourceInfosItem,
            DatasetPatchOpenzgyV1DataEndian,
            DatasetPatchOpenzgyV1Legal,
            DatasetPatchOpenzgyV1MetaItemUnitOfMeasureId,
            DatasetPatchOpenzgyV1MetaItemUnitOfMeasureIdKind,
            DatasetPatchSegyV1,
            DatasetPatchSegyV1Acl,
            DatasetPatchSegyV1Ancestry,
            DatasetPatchSegyV1Data,
            DatasetPatchSegyV1DataDatasetProperties,
            DatasetPatchSegyV1DataDatasetPropertiesFileSourceInfosItem,
            DatasetPatchSegyV1DataEndian,
            DatasetPatchSegyV1DataVectorHeaderMappingItem,
            DatasetPatchSegyV1DataVectorHeaderMappingItemScalarIndicator,
            DatasetPatchSegyV1Legal,
            DatasetPatchSegyV1MetaItemUnitOfMeasureId,
            DatasetPatchSegyV1MetaItemUnitOfMeasureIdKind,
            DatasetPatchSeismicmeta,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dataset.patch(
                tenantid="tenantid",
                subprojectid="subprojectid",
                datasetid="datasetid",
                path="path",
                dataset_new_name="dsx02",
                metadata={"f1": "v1", "f2": "v2", "f3": "v3"},
                filemetadata={"f1": "v1", "f2": "v2", "f3": "v3"},
                last_modified_date="Thu Jul 16 2020 04:37:41 GMT+0000 (Coordinated Universal Time)",
                gtags=["tag01", "tag02", "tag03"],
                ltag="legal-tag",
                readonly=False,
                seismicmeta=DatasetPatchSeismicmeta(
                    kind="slb:seistore:seismic2d:1.0.0",
                    data={"msg": "sample data"},
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
                        legaltags=["opendes-seistore-test-01"],
                        other_relevant_data_countries=["US"],
                        status="compliant",
                    ),
                    tags={"NameOfKey": "String value"},
                    create_time=datetime.datetime.fromisoformat(
                        "2021-11-16 02:08:16+00:00",
                    ),
                    create_user="vmanohar@slb.com",
                    modify_time=datetime.datetime.fromisoformat(
                        "2021-11-18 04:10:23+00:00",
                    ),
                    modify_user="39916b94-71a9-409e-856e-0f29558fa908",
                    meta=[
                        DatasetPatchOpenzgyV1MetaItemUnitOfMeasureId(
                            kind=DatasetPatchOpenzgyV1MetaItemUnitOfMeasureIdKind.UNIT,
                            persistable_reference='{"abcd":{"a":0.0,"b":1200.0,"c":3937.0,"d":0.0},"symbol":"ft[US]","baseMeasurement":{"ancestry":"L","type":"UM"},"type":"UAD"}',
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
                                    preload_file_create_date=datetime.datetime.fromisoformat(
                                        "2019-12-16 11:46:20+00:00",
                                    ),
                                    preload_file_modify_user="somebody.else@acme.org",
                                    preload_file_modify_date=datetime.datetime.fromisoformat(
                                        "2019-12-20 17:20:05+00:00",
                                    ),
                                    name="vds-file-1",
                                    file_size="439452464",
                                    checksum="checksum-value",
                                    checksum_algorithm="MD5",
                                ),
                                DatasetPatchOpenzgyV1DataDatasetPropertiesFileSourceInfosItem(
                                    file_source="s3://default_bucket/opendes/data/vds-dataset/vds-file-2",
                                    preload_file_path="s3://staging-area/r7/raw-data/provided/documents/vds-file-2",
                                    preload_file_create_user="somebody@acme.org",
                                    preload_file_create_date=datetime.datetime.fromisoformat(
                                        "2019-12-16 11:50:40+00:00",
                                    ),
                                    preload_file_modify_user="somebody.else@acme.org",
                                    preload_file_modify_date=datetime.datetime.fromisoformat(
                                        "2019-12-20 17:59:03+00:00",
                                    ),
                                    name="vds-file-2",
                                    file_size="433645463",
                                    checksum="checksum-value",
                                    checksum_algorithm="MD5",
                                ),
                            ],
                            checksum="checksum-value",
                        ),
                        extension_properties={"key": "value"},
                    ),
                ),
                segy_v1=DatasetPatchSegyV1(
                    id="osdu:dataset--FileCollection.SEGY:b47f793a-dc9c-5d11-8d59-6cc611a98926",
                    kind="osdu:wks:dataset--FileCollection.SEGY:1.0.0",
                    version=1562066009929332,
                    acl=DatasetPatchSegyV1Acl(
                        owners=["someone@company.com"],
                        viewers=["someone@company.com"],
                    ),
                    legal=DatasetPatchSegyV1Legal(
                        legaltags=["Example legaltags"],
                        other_relevant_data_countries=["US"],
                        status="compliant",
                    ),
                    tags={"NameOfKey": "String value"},
                    create_time=datetime.datetime.fromisoformat(
                        "2020-12-16 11:46:20+00:00",
                    ),
                    create_user="some-user@some-company-cloud.com",
                    modify_time=datetime.datetime.fromisoformat(
                        "2020-12-16 11:52:24+00:00",
                    ),
                    modify_user="some-user@some-company-cloud.com",
                    ancestry=DatasetPatchSegyV1Ancestry(
                        parents=["parents"],
                    ),
                    meta=[
                        DatasetPatchSegyV1MetaItemUnitOfMeasureId(
                            kind=DatasetPatchSegyV1MetaItemUnitOfMeasureIdKind.UNIT,
                            persistable_reference='{"abcd":{"a":0.0,"b":1200.0,"c":3937.0,"d":0.0},"symbol":"ft[US]","baseMeasurement":{"ancestry":"L","type":"UM"},"type":"UAD"}',
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
                                    preload_file_create_date=datetime.datetime.fromisoformat(
                                        "2019-12-16 11:46:20+00:00",
                                    ),
                                    preload_file_modify_user="somebody.else@acme.org",
                                    preload_file_modify_date=datetime.datetime.fromisoformat(
                                        "2019-12-20 17:20:05+00:00",
                                    ),
                                    name="vds-file-1",
                                    file_size="439452464",
                                    checksum="checksum-value",
                                    checksum_algorithm="MD5",
                                ),
                                DatasetPatchSegyV1DataDatasetPropertiesFileSourceInfosItem(
                                    file_source="s3://default_bucket/opendes/data/vds-dataset/vds-file-2",
                                    preload_file_path="s3://staging-area/r7/raw-data/provided/documents/vds-file-2",
                                    preload_file_create_user="somebody@acme.org",
                                    preload_file_create_date=datetime.datetime.fromisoformat(
                                        "2019-12-16 11:50:40+00:00",
                                    ),
                                    preload_file_modify_user="somebody.else@acme.org",
                                    preload_file_modify_date=datetime.datetime.fromisoformat(
                                        "2019-12-20 17:59:03+00:00",
                                    ),
                                    name="vds-file-2",
                                    file_size="433645463",
                                    checksum="checksum-value",
                                    checksum_algorithm="MD5",
                                ),
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
                        extension_properties={"key": "value"},
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


        asyncio.run(main())
        """
        _response = await self._raw_client.patch(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            close=close,
            impersonation_token_context=impersonation_token_context,
            dataset_new_name=dataset_new_name,
            metadata=metadata,
            filemetadata=filemetadata,
            last_modified_date=last_modified_date,
            gtags=gtags,
            ltag=ltag,
            readonly=readonly,
            seismicmeta=seismicmeta,
            openzgy_v1=openzgy_v1,
            segy_v1=segy_v1,
            acls=acls,
            request_options=request_options,
        )
        return _response.data

    async def acquire_a_lock_for_a_dataset_id(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        openmode: typing.Optional[str] = None,
        wid: typing.Optional[float] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
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

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        openmode : typing.Optional[str]
            Type of the lock which can be set to 'read' (default) or 'write'.

        wid : typing.Optional[float]
            Session identifier issued for a previous write lock acquisition operation.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset
            Acquired a lock and the return value is the dataset metadata with session identifier stored in the 'sbit' attribute.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dataset.acquire_a_lock_for_a_dataset_id(
                tenantid="tenantid",
                subprojectid="subprojectid",
                datasetid="datasetid",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.acquire_a_lock_for_a_dataset_id(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            openmode=openmode,
            wid=wid,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    async def lock_rm(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        <ul>
          <li>Removes the lock for a dataset id.</li>
          <li>Required roles:
            <ul>
              <li>subproject.admin: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path for the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dataset.lock_rm(
                tenantid="tenantid",
                subprojectid="subprojectid",
                datasetid="datasetid",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.lock_rm(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    async def permission(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetPermission:
        """
        <ul>
          <li>Retrieve the access permission of a user on a dataset.</li>
          <li>Required roles:
            <ul>
              <li>subproject.admin, subproject.viewer: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin, dataset.viewer: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path for the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetPermission
            User access permission on the dataset.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dataset.permission(
                tenantid="tenantid",
                subprojectid="subprojectid",
                datasetid="datasetid",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.permission(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    async def ctag_check(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        ctag: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        <ul><li>Check if the provided dataset cTag match the one stored in the metadata catalog.</li><li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        ctag : str
            Ctag to be validated.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Return true if the ctag is valid or false if it is invalid.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dataset.ctag_check(
                tenantid="tenantid",
                subprojectid="subprojectid",
                datasetid="datasetid",
                path="path",
                ctag="ctag",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ctag_check(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            ctag=ctag,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    async def add_tag(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        gtag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        <ul>
          <li>Upsert tags to an existing dataset metadata. If the dataset metadata already has gtags, then  new gtags are appended to this list.</li>
          <li>Required roles:
            <ul>
              <li>subproject.admin: if the applied subproject policy is 'uniform'</li>
              <li>dataset.admin: if the applied subproject policy is 'dataset'</li>
            </ul>
          </li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        gtag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Gtags array list.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dataset.add_tag(
                tenantid="tenantid",
                subprojectid="subprojectid",
                datasetid="datasetid",
                path="path",
                gtag=["gtag"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_tag(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            gtag=gtag,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    async def size(
        self,
        tenantid: str,
        subprojectid: str,
        datasetid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetSize:
        """
        <ul>
        <li>Compute and retrieve the size of a dataset and the date of when the size was computed.</li>
        <li>Required roles: subproject.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasetid : str
            Name of the dataset.

        path : str
            Hierarchical path of the dataset.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetSize
            Size of the dataset and the date of when the size was computed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dataset.size(
                tenantid="tenantid",
                subprojectid="subprojectid",
                datasetid="datasetid",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.size(
            tenantid,
            subprojectid,
            datasetid,
            path=path,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    async def read_directory(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        path: str,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetAndDirectories:
        """
        <ul>
        <li>List datasets and sub-directories for a directory path.</li>
        <li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        tenantid : str
            The tenant project name.

        subprojectid : str
            The sub-project name.

        path : str
            The hierarchy path.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetAndDirectories
            The list of datasets and directories in the requested directory path.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dataset.read_directory(
                tenantid="tenantid",
                subprojectid="subprojectid",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_directory(
            tenantid,
            subprojectid,
            path=path,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    async def list(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        gtag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        translate_user_info: typing.Optional[bool] = None,
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDatasets:
        """
        <ul>
          <li>Return the list of datasets in a sub-project. The list can be filtered by gtags. Support pagination.</li>
          <li>Required roles: subproject.admin, subproject.viewer</li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        gtag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Gtags associated with dataset metadata.

        limit : typing.Optional[str]
            Limit the number of datasets in the response

        cursor : typing.Optional[str]
            Cursor for pagination on the datasets list

        translate_user_info : typing.Optional[bool]
            translate the user-id to a more human readable user info

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDatasets
            Paginated dataset list with nextPageCursor. If the request does not provide limit or cursor the results will be the whole path conent and the response is a plain array of datasets [ {dataset1}, {datase2}, ... ]

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dataset.list(
                tenantid="tenantid",
                subprojectid="subprojectid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            tenantid,
            subprojectid,
            gtag=gtag,
            limit=limit,
            cursor=cursor,
            translate_user_info=translate_user_info,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data

    async def list_post(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        translate_user_info: typing.Optional[bool] = None,
        impersonation_token_context: typing.Optional[str] = None,
        type: typing.Optional[str] = OMIT,
        gtags: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        cursor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDatasets:
        """
        <ul>
          <li>Return the list of datasets in a sub-project. The list can be filtered by gtags. Support pagination.</li>
          <li>Required roles: subproject.admin, subproject.viewer</li>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        translate_user_info : typing.Optional[bool]
            translate the user-id to a more human readable user info

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        type : typing.Optional[str]

        gtags : typing.Optional[typing.Sequence[str]]
            Array of global tags associated with the dataset metadata. Once assigned, they can be used to filter datasets.

        limit : typing.Optional[float]
            the max limit of datasets in the response

        cursor : typing.Optional[str]
            the cursor value required to retrieve the next page of result

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDatasets
            Paginated dataset list with nextPageCursor. If the request does not provide limit or cursor the results will be the whole path conent and the response is a plain array of datasets [ {dataset1}, {datase2}, ... ]

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dataset.list_post(
                tenantid="tenantid",
                subprojectid="subprojectid",
                gtags=["tagA", "tagB"],
                limit=10.0,
                cursor="next-page-token-931fvm19vm1-vm1v1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_post(
            tenantid,
            subprojectid,
            translate_user_info=translate_user_info,
            impersonation_token_context=impersonation_token_context,
            type=type,
            gtags=gtags,
            limit=limit,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data

    async def exist(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        datasets: typing.Sequence[str],
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[bool]:
        """
        <ul>
        <li>Check if the dataset exists.</li>
        <li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        datasets : typing.Sequence[str]
            Array of datasets inside the subproject.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[bool]
            A list of Boolean values for all the input datasets in the request body. If a value is true, then the corresponding dataset exists and if it is false, then the dataset does not exist.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dataset.exist(
                tenantid="tenantid",
                subprojectid="subprojectid",
                datasets=["a/b/c/dsx01", "a/b/c/dsx02"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.exist(
            tenantid,
            subprojectid,
            datasets=datasets,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data
